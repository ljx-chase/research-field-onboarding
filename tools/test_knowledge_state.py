from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT = (
    Path(__file__).resolve().parents[1]
    / "field-onboarding"
    / "scripts"
    / "knowledge_state.py"
)
SPEC = importlib.util.spec_from_file_location("knowledge_state", SCRIPT)
assert SPEC and SPEC.loader
state_runtime = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(state_runtime)


class KnowledgeStateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.state = state_runtime.initial_state(
            "session-1", "topological photonics", "read-paper", language="zh-CN"
        )

    def add(
        self,
        concept_id: str,
        self_report: str,
        prerequisites: list[str] | None = None,
    ) -> None:
        state_runtime.add_concept(
            self.state,
            concept_id,
            concept_id.replace("-", " "),
            self_report,
            prerequisites or [],
        )

    def add_node(self, concept_id: str, prerequisites: list[str] | None = None) -> None:
        state_runtime.add_concept(
            self.state,
            concept_id,
            concept_id.replace("-", " "),
            None,
            prerequisites or [],
            on_map=True,
        )

    def map_states(self) -> dict[str, str]:
        return state_runtime.summarize(self.state)["map_states"]

    def test_initial_state_is_valid(self) -> None:
        state_runtime.validate(self.state)
        self.assertEqual("unknown", self.state["field_status"])
        self.assertEqual(
            {
                "explanation_style": "physical-picture",
                "technical_register": "peer-new-to-field",
            },
            self.state["preferences"],
        )

    def test_preferences_can_change_independently(self) -> None:
        state_runtime.set_preferences(self.state, explanation_style="derivation-first")
        self.assertEqual(
            "derivation-first", self.state["preferences"]["explanation_style"]
        )
        self.assertEqual(
            "peer-new-to-field", self.state["preferences"]["technical_register"]
        )

    def test_invalid_preferences_do_not_mutate_state(self) -> None:
        before = self.state.copy()
        before["preferences"] = self.state["preferences"].copy()
        with self.assertRaisesRegex(state_runtime.StateError, "invalid explanation"):
            state_runtime.set_preferences(self.state, explanation_style="baby-talk")
        self.assertEqual(before, self.state)

    def test_used_anchor_is_covered_but_untested(self) -> None:
        self.add("berry-phase", "used")
        concept = self.state["concepts"]["berry-phase"]
        self.assertEqual("covered", concept["progress"])
        self.assertEqual("untested", concept["evidence"])

    def test_ready_concepts_follow_dependencies(self) -> None:
        self.add("berry-phase", "new")
        self.add("berry-curvature", "new", ["berry-phase"])
        self.assertEqual(["berry-phase"], state_runtime.ready_concepts(self.state))
        state_runtime.activate(self.state, "berry-phase")
        state_runtime.record_checkpoint(self.state, "berry-phase", "pass", [])
        self.assertEqual(
            ["berry-curvature"], state_runtime.ready_concepts(self.state)
        )

    def test_failed_checkpoint_overrides_used_anchor(self) -> None:
        self.add("berry-phase", "used")
        self.add("berry-curvature", "new", ["berry-phase"])
        self.assertEqual(
            ["berry-curvature"], state_runtime.ready_concepts(self.state)
        )
        state_runtime.record_checkpoint(
            self.state, "berry-phase", "fail", ["confuses two phases"]
        )
        self.assertEqual([], state_runtime.ready_concepts(self.state))
        self.assertEqual("berry-phase", self.state["current_concept"])

    def test_blocked_concept_cannot_be_activated(self) -> None:
        self.add("a", "new")
        self.add("b", "new", ["a"])
        with self.assertRaisesRegex(state_runtime.StateError, "blocked"):
            state_runtime.activate(self.state, "b")

    def test_dependency_cycles_are_rejected(self) -> None:
        self.add("a", "new")
        self.add("b", "new", ["a"])
        before = self.state.copy()
        before["concepts"] = {
            key: value.copy() for key, value in self.state["concepts"].items()
        }
        with self.assertRaisesRegex(state_runtime.StateError, "cycle"):
            state_runtime.add_concept(self.state, "a", "A", "new", ["b"])
        self.assertEqual(before, self.state)

    def test_atomic_round_trip(self) -> None:
        self.add("berry-phase", "learned")
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "session.json"
            state_runtime.save(self.state, path)
            self.assertEqual(self.state, state_runtime.load(path))

    def test_map_nodes_take_no_self_report_and_start_new(self) -> None:
        self.add("linear-algebra", "learned")
        self.add_node("band-topology", ["linear-algebra"])
        self.assertEqual({"band-topology": "new"}, self.map_states())
        with self.assertRaisesRegex(state_runtime.StateError, "no self_report"):
            state_runtime.add_concept(
                self.state, "edge-states", "edge states", "used", [], on_map=True
            )

    def test_map_states_follow_teaching_and_checkpoints(self) -> None:
        self.add_node("berry-phase")
        self.add_node("chern-number", ["berry-phase"])
        state_runtime.activate(self.state, "berry-phase")
        self.assertEqual("taught", self.map_states()["berry-phase"])
        state_runtime.record_checkpoint(self.state, "berry-phase", "pass", [])
        self.assertEqual("checked", self.map_states()["berry-phase"])
        state_runtime.activate(self.state, "chern-number")
        state_runtime.record_checkpoint(self.state, "chern-number", "fail", [])
        self.assertEqual(
            {"berry-phase": "checked", "chern-number": "taught"}, self.map_states()
        )

    def test_skipped_checkpoint_marks_taught_and_unblocks(self) -> None:
        self.add_node("berry-phase")
        self.add_node("chern-number", ["berry-phase"])
        state_runtime.activate(self.state, "berry-phase")
        state_runtime.mark(self.state, "berry-phase", "taught")
        concept = self.state["concepts"]["berry-phase"]
        self.assertEqual("covered", concept["progress"])
        self.assertEqual("untested", concept["evidence"])
        self.assertIsNone(self.state["current_concept"])
        self.assertEqual(["chern-number"], state_runtime.ready_concepts(self.state))

    def test_skip_needs_a_reason_and_does_not_block_dependents(self) -> None:
        self.add_node("photonic-crystals")
        self.add_node("edge-states", ["photonic-crystals"])
        with self.assertRaisesRegex(state_runtime.StateError, "reason"):
            state_runtime.mark(self.state, "photonic-crystals", "skipped")
        with self.assertRaisesRegex(state_runtime.StateError, "reason"):
            state_runtime.mark(self.state, "photonic-crystals", "taught", "why")
        state_runtime.mark(
            self.state, "photonic-crystals", "skipped", "not needed for this paper"
        )
        self.assertEqual("skipped", self.map_states()["photonic-crystals"])
        self.assertEqual(["edge-states"], state_runtime.ready_concepts(self.state))

    def test_taught_node_cannot_be_skipped(self) -> None:
        self.add_node("berry-phase")
        state_runtime.mark(self.state, "berry-phase", "taught")
        before = json.loads(json.dumps(self.state))
        with self.assertRaisesRegex(state_runtime.StateError, "already taught"):
            state_runtime.mark(self.state, "berry-phase", "skipped", "changed mind")
        self.assertEqual(before, self.state)

    def test_teaching_a_skipped_node_clears_its_reason(self) -> None:
        self.add_node("edge-states")
        state_runtime.mark(self.state, "edge-states", "skipped", "off path")
        state_runtime.activate(self.state, "edge-states")
        self.assertIsNone(self.state["concepts"]["edge-states"]["skip_reason"])
        self.assertEqual("taught", self.map_states()["edge-states"])

    def test_map_source_is_labelled(self) -> None:
        self.assertIsNone(state_runtime.summarize(self.state)["map"])
        with self.assertRaisesRegex(state_runtime.StateError, "verification"):
            state_runtime.set_map(self.state, "a review's headings", "probably")
        self.assertIsNone(self.state["map"])
        state_runtime.set_map(self.state, "a review's headings", "unverified")
        self.assertEqual(
            {"source": "a review's headings", "verification": "unverified"},
            self.state["map"],
        )

    def test_pasted_map_is_restored(self) -> None:
        pasted = {
            "berry-phase": "checked",
            "chern-number": "taught",
            "edge-states": "new",
            "photonic-crystals": "skipped",
        }
        self.add_node("berry-phase")
        self.add_node("chern-number", ["berry-phase"])
        self.add_node("edge-states", ["chern-number"])
        self.add_node("photonic-crystals")
        state_runtime.mark(self.state, "berry-phase", "checked")
        state_runtime.mark(self.state, "chern-number", "taught")
        state_runtime.mark(self.state, "photonic-crystals", "skipped", "already yours")
        self.assertEqual(pasted, self.map_states())
        self.assertEqual(["edge-states"], state_runtime.ready_concepts(self.state))

    def test_prerequisite_and_map_node_cannot_share_an_id(self) -> None:
        self.add("berry-phase", "used")
        with self.assertRaisesRegex(state_runtime.StateError, "already a prerequisite"):
            self.add_node("berry-phase")

    def test_cli_records_map_states(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = str(Path(directory) / "session.json")

            def run(*arguments: str) -> dict:
                result = subprocess.run(
                    [sys.executable, str(SCRIPT), arguments[0], path, *arguments[1:]],
                    capture_output=True,
                    text=True,
                    check=True,
                )
                return json.loads(result.stdout)

            run("init", "--session-id", "s", "--field", "rl", "--goal", "read-paper")
            run("set-map", "--source", "a textbook", "--verification", "verified")
            run("add", "--id", "mdp", "--label", "MDPs", "--on-map")
            run("add", "--id", "bandits", "--label", "bandits", "--on-map")
            run("mark", "--id", "mdp", "--as", "taught")
            run("mark", "--id", "bandits", "--as", "skipped", "--reason", "off path")
            summary = run("summary")
        self.assertEqual("verified", summary["map"]["verification"])
        self.assertEqual({"mdp": "taught", "bandits": "skipped"}, summary["map_states"])


if __name__ == "__main__":
    unittest.main()
