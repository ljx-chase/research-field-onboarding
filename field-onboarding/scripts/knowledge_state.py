#!/usr/bin/env python3
"""Optional, dependency-free session state for the Field Onboarding skill.

This is an agent-facing helper. End users should never need to invoke it or
edit its JSON files themselves.
"""

from __future__ import annotations

import argparse
import copy
import json
import os
import tempfile
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


VERSION = "0.3.0"
SELF_REPORTS = {"used", "learned", "new"}
EVIDENCE = {"untested", "pass", "partial", "fail"}
PROGRESS = {"queued", "active", "covered", "skipped"}
FIELD_STATUS = {"unknown", "settled", "emerging", "contested"}
EXPLANATION_STYLES = {"physical-picture", "balanced", "derivation-first"}
TECHNICAL_REGISTERS = {"foundational", "peer-new-to-field", "specialist-bridge"}
MAP_VERIFICATION = {"verified", "unverified"}
MARKS = {"taught", "checked", "skipped"}


class StateError(ValueError):
    pass


def initial_state(
    session_id: str,
    field: str,
    goal: str,
    artifact: str | None = None,
    language: str | None = None,
    explanation_style: str = "physical-picture",
    technical_register: str = "peer-new-to-field",
) -> dict[str, Any]:
    state = {
        "version": VERSION,
        "session_id": required_text(session_id, "session_id"),
        "target": {
            "field": required_text(field, "field"),
            "goal": required_text(goal, "goal"),
            "artifact": artifact,
        },
        "language": language,
        "preferences": {
            "explanation_style": explanation_style,
            "technical_register": technical_register,
        },
        "field_status": "unknown",
        "map": None,
        "concepts": {},
        "current_concept": None,
        "events": [],
    }
    validate(state)
    return state


def load(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        state = json.load(handle)
    validate(state)
    return state


def save(state: dict[str, Any], path: Path) -> None:
    validate(state)
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(
        prefix=f".{path.name}.", suffix=".tmp", dir=path.parent
    )
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            json.dump(state, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
        os.replace(temporary, path)
    except BaseException:
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass
        raise


def validate(state: dict[str, Any]) -> None:
    if not isinstance(state, dict):
        raise StateError("state must be an object")
    if state.get("version") != VERSION:
        raise StateError(f"unsupported state version: {state.get('version')}")
    required_text(state.get("session_id"), "session_id")
    target = state.get("target")
    if not isinstance(target, dict):
        raise StateError("target must be an object")
    required_text(target.get("field"), "target.field")
    required_text(target.get("goal"), "target.goal")
    if target.get("artifact") is not None and not isinstance(target["artifact"], str):
        raise StateError("target.artifact must be a string or null")
    preferences = state.get("preferences")
    if not isinstance(preferences, dict):
        raise StateError("preferences must be an object")
    if preferences.get("explanation_style") not in EXPLANATION_STYLES:
        raise StateError(
            f"invalid explanation style: {preferences.get('explanation_style')}"
        )
    if preferences.get("technical_register") not in TECHNICAL_REGISTERS:
        raise StateError(
            f"invalid technical register: {preferences.get('technical_register')}"
        )
    if state.get("field_status") not in FIELD_STATUS:
        raise StateError(f"invalid field status: {state.get('field_status')}")
    field_map = state.get("map")
    if field_map is not None:
        if not isinstance(field_map, dict):
            raise StateError("map must be an object or null")
        required_text(field_map.get("source"), "map.source")
        if field_map.get("verification") not in MAP_VERIFICATION:
            raise StateError(
                f"invalid map verification: {field_map.get('verification')}"
            )

    concepts = state.get("concepts")
    if not isinstance(concepts, dict):
        raise StateError("concepts must be an object")
    for concept_id, concept in concepts.items():
        required_text(concept_id, "concept_id")
        if not isinstance(concept, dict):
            raise StateError(f"concept {concept_id!r} must be an object")
        required_text(concept.get("label"), f"{concept_id}.label")
        if not isinstance(concept.get("on_map"), bool):
            raise StateError(f"invalid on_map for {concept_id!r}")
        if concept["on_map"]:
            if concept.get("self_report") is not None:
                raise StateError(f"map node {concept_id!r} takes no self_report")
        elif concept.get("self_report") not in SELF_REPORTS:
            raise StateError(f"invalid self_report for {concept_id!r}")
        if concept.get("evidence") not in EVIDENCE:
            raise StateError(f"invalid evidence for {concept_id!r}")
        if concept.get("progress") not in PROGRESS:
            raise StateError(f"invalid progress for {concept_id!r}")
        prerequisites = concept.get("prerequisites")
        if not isinstance(prerequisites, list) or not all(
            isinstance(item, str) and item for item in prerequisites
        ):
            raise StateError(f"invalid prerequisites for {concept_id!r}")
        if len(prerequisites) != len(set(prerequisites)):
            raise StateError(f"duplicate prerequisite for {concept_id!r}")
        for prerequisite in prerequisites:
            if prerequisite not in concepts:
                raise StateError(
                    f"{concept_id!r} references missing prerequisite {prerequisite!r}"
                )
        misconceptions = concept.get("misconceptions")
        if not isinstance(misconceptions, list) or not all(
            isinstance(item, str) and item for item in misconceptions
        ):
            raise StateError(f"invalid misconceptions for {concept_id!r}")
        if concept["progress"] == "skipped":
            required_text(concept.get("skip_reason"), f"{concept_id}.skip_reason")
        elif concept.get("skip_reason") is not None:
            raise StateError(f"skip_reason set but {concept_id!r} is not skipped")
    reject_cycles(concepts)

    current = state.get("current_concept")
    if current is not None and current not in concepts:
        raise StateError(f"unknown current concept: {current}")
    active = [key for key, value in concepts.items() if value["progress"] == "active"]
    if len(active) > 1 or active != ([] if current is None else [current]):
        raise StateError("current_concept must match the only active concept")
    if not isinstance(state.get("events"), list):
        raise StateError("events must be an array")


def add_concept(
    state: dict[str, Any],
    concept_id: str,
    label: str,
    self_report: str | None,
    prerequisites: list[str],
    on_map: bool = False,
) -> None:
    concept_id = required_text(concept_id, "concept_id")
    if on_map:
        if self_report is not None:
            raise StateError(
                "map nodes take no self_report; skip one the user already has"
            )
    elif self_report not in SELF_REPORTS:
        raise StateError(f"invalid self_report: {self_report}")
    if concept_id in prerequisites:
        raise StateError("a concept cannot depend on itself")
    missing = [item for item in prerequisites if item not in state["concepts"]]
    if missing:
        raise StateError(f"missing prerequisites: {', '.join(missing)}")
    candidate = copy.deepcopy(state)
    existing = candidate["concepts"].get(concept_id)
    if existing:
        if existing["on_map"] != on_map:
            kind = "map node" if existing["on_map"] else "prerequisite"
            raise StateError(f"{concept_id!r} is already a {kind}; use another id")
        existing.update(
            label=required_text(label, "label"),
            self_report=self_report,
            prerequisites=list(dict.fromkeys(prerequisites)),
        )
    else:
        candidate["concepts"][concept_id] = {
            "label": required_text(label, "label"),
            "self_report": self_report,
            "evidence": "untested",
            "progress": "covered" if self_report == "used" else "queued",
            "prerequisites": list(dict.fromkeys(prerequisites)),
            "misconceptions": [],
            "on_map": on_map,
            "skip_reason": None,
        }
    validate(candidate)
    state.clear()
    state.update(candidate)


def set_map(state: dict[str, Any], source: str, verification: str) -> None:
    if verification not in MAP_VERIFICATION:
        raise StateError(f"invalid map verification: {verification}")
    candidate = copy.deepcopy(state)
    candidate["map"] = {
        "source": required_text(source, "source"),
        "verification": verification,
    }
    validate(candidate)
    state.clear()
    state.update(candidate)


def mark(
    state: dict[str, Any], concept_id: str, node_state: str, reason: str | None = None
) -> None:
    """Record a node state that no checkpoint produced.

    `taught`: the rung was delivered but the checkpoint was skipped.
    `skipped`: the node was deliberately left out, for `reason`.
    `checked`: only when restoring a pasted map; in-session, a passed
    checkpoint records it.
    """
    if concept_id not in state["concepts"]:
        raise StateError(f"unknown concept: {concept_id}")
    if node_state not in MARKS:
        raise StateError(f"invalid mark: {node_state}")
    if (node_state == "skipped") != (reason is not None):
        raise StateError("a reason is required for skipped, and only for skipped")
    candidate = copy.deepcopy(state)
    concept = candidate["concepts"][concept_id]
    if node_state == "skipped":
        if concept["progress"] == "covered" or concept["evidence"] == "pass":
            raise StateError(f"{concept_id!r} was already taught; it cannot be skipped")
        concept["progress"] = "skipped"
        concept["skip_reason"] = required_text(reason, "reason")
    else:
        concept["progress"] = "covered"
        concept["skip_reason"] = None
        if node_state == "checked":
            concept["evidence"] = "pass"
    if candidate["current_concept"] == concept_id:
        candidate["current_concept"] = None
    validate(candidate)
    state.clear()
    state.update(candidate)


def set_preferences(
    state: dict[str, Any],
    explanation_style: str | None = None,
    technical_register: str | None = None,
) -> None:
    if explanation_style is None and technical_register is None:
        raise StateError("at least one preference must be supplied")
    candidate = copy.deepcopy(state)
    if explanation_style is not None:
        if explanation_style not in EXPLANATION_STYLES:
            raise StateError(f"invalid explanation style: {explanation_style}")
        candidate["preferences"]["explanation_style"] = explanation_style
    if technical_register is not None:
        if technical_register not in TECHNICAL_REGISTERS:
            raise StateError(f"invalid technical register: {technical_register}")
        candidate["preferences"]["technical_register"] = technical_register
    validate(candidate)
    state.clear()
    state.update(candidate)


def ready_concepts(state: dict[str, Any]) -> list[str]:
    validate(state)
    return sorted(
        concept_id
        for concept_id, concept in state["concepts"].items()
        if concept["progress"] == "queued"
        and all(satisfied(state["concepts"][item]) for item in concept["prerequisites"])
    )


def activate(state: dict[str, Any], concept_id: str) -> None:
    if concept_id not in state["concepts"]:
        raise StateError(f"unknown concept: {concept_id}")
    blocked = [
        item
        for item in state["concepts"][concept_id]["prerequisites"]
        if not satisfied(state["concepts"][item])
    ]
    if blocked:
        raise StateError(f"concept is blocked by: {', '.join(blocked)}")
    for concept in state["concepts"].values():
        if concept["progress"] == "active":
            concept["progress"] = "queued"
    state["concepts"][concept_id]["progress"] = "active"
    state["concepts"][concept_id]["skip_reason"] = None
    state["current_concept"] = concept_id
    validate(state)


def record_checkpoint(
    state: dict[str, Any], concept_id: str, result: str, misconceptions: list[str]
) -> None:
    if concept_id not in state["concepts"]:
        raise StateError(f"unknown concept: {concept_id}")
    if result not in {"pass", "partial", "fail"}:
        raise StateError(f"invalid checkpoint result: {result}")
    concept = state["concepts"][concept_id]
    concept["evidence"] = result
    concept["misconceptions"] = list(dict.fromkeys(misconceptions))
    concept["progress"] = "covered" if result == "pass" else "active"
    concept["skip_reason"] = None
    if result == "pass":
        if state["current_concept"] == concept_id:
            state["current_concept"] = None
    else:
        for key, item in state["concepts"].items():
            if key != concept_id and item["progress"] == "active":
                item["progress"] = "queued"
        state["current_concept"] = concept_id
    validate(state)


def satisfied(concept: dict[str, Any]) -> bool:
    # A skipped node is a deliberate black box, so it never blocks dependents.
    if concept["progress"] == "skipped" or concept["evidence"] == "pass":
        return True
    if concept["evidence"] in {"partial", "fail"}:
        return False
    return concept["self_report"] == "used" or concept["progress"] == "covered"


def map_state(concept: dict[str, Any]) -> str:
    if concept["progress"] == "skipped":
        return "skipped"
    if concept["evidence"] == "pass":
        return "checked"
    if concept["progress"] in {"active", "covered"}:
        return "taught"
    return "new"


def summarize(state: dict[str, Any]) -> dict[str, Any]:
    return {
        "target": state["target"],
        "preferences": state["preferences"],
        "field_status": state["field_status"],
        "map": state["map"],
        "map_states": {
            concept_id: map_state(concept)
            for concept_id, concept in state["concepts"].items()
            if concept["on_map"]
        },
        "current_concept": state["current_concept"],
        "ready": ready_concepts(state),
        "concepts": state["concepts"],
    }


def reject_cycles(concepts: dict[str, dict[str, Any]]) -> None:
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(concept_id: str) -> None:
        if concept_id in visiting:
            raise StateError(f"dependency cycle includes {concept_id!r}")
        if concept_id in visited:
            return
        visiting.add(concept_id)
        for prerequisite in concepts[concept_id]["prerequisites"]:
            visit(prerequisite)
        visiting.remove(concept_id)
        visited.add(concept_id)

    for concept_id in concepts:
        visit(concept_id)


def record_event(
    state: dict[str, Any], event_type: str, payload: dict[str, Any], operation_id: str | None
) -> bool:
    event_id = operation_id or str(uuid.uuid4())
    if any(event.get("id") == event_id for event in state["events"]):
        return False
    state["events"].append(
        {
            "id": event_id,
            "type": event_type,
            "at": datetime.now(timezone.utc).isoformat(),
            "payload": payload,
        }
    )
    return True


def required_text(value: Any, name: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise StateError(f"{name} must be a non-empty string")
    return value.strip()


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(description=__doc__)
    commands = root.add_subparsers(dest="command", required=True)

    init = commands.add_parser("init")
    init.add_argument("state", type=Path)
    init.add_argument("--session-id", required=True)
    init.add_argument("--field", required=True)
    init.add_argument("--goal", required=True)
    init.add_argument("--artifact")
    init.add_argument("--language")
    init.add_argument(
        "--style", choices=sorted(EXPLANATION_STYLES), default="physical-picture"
    )
    init.add_argument(
        "--register",
        choices=sorted(TECHNICAL_REGISTERS),
        default="peer-new-to-field",
    )
    init.add_argument("--force", action="store_true")

    validate_command = commands.add_parser("validate")
    validate_command.add_argument("state", type=Path)

    add = commands.add_parser("add")
    add.add_argument("state", type=Path)
    add.add_argument("--id", required=True)
    add.add_argument("--label", required=True)
    kind = add.add_mutually_exclusive_group(required=True)
    kind.add_argument("--self-report", choices=sorted(SELF_REPORTS))
    kind.add_argument("--on-map", action="store_true")
    add.add_argument("--requires", action="append", default=[])
    add.add_argument("--operation-id")

    field_status = commands.add_parser("set-field-status")
    field_status.add_argument("state", type=Path)
    field_status.add_argument("--status", choices=sorted(FIELD_STATUS), required=True)
    field_status.add_argument("--operation-id")

    map_command = commands.add_parser("set-map")
    map_command.add_argument("state", type=Path)
    map_command.add_argument("--source", required=True)
    map_command.add_argument(
        "--verification", choices=sorted(MAP_VERIFICATION), required=True
    )
    map_command.add_argument("--operation-id")

    mark_command = commands.add_parser("mark")
    mark_command.add_argument("state", type=Path)
    mark_command.add_argument("--id", required=True)
    mark_command.add_argument(
        "--as", dest="node_state", choices=sorted(MARKS), required=True
    )
    mark_command.add_argument("--reason")
    mark_command.add_argument("--operation-id")

    preferences = commands.add_parser("set-preferences")
    preferences.add_argument("state", type=Path)
    preferences.add_argument("--style", choices=sorted(EXPLANATION_STYLES))
    preferences.add_argument("--register", choices=sorted(TECHNICAL_REGISTERS))
    preferences.add_argument("--operation-id")

    next_command = commands.add_parser("next")
    next_command.add_argument("state", type=Path)

    activate_command = commands.add_parser("activate")
    activate_command.add_argument("state", type=Path)
    activate_command.add_argument("--id", required=True)
    activate_command.add_argument("--operation-id")

    checkpoint = commands.add_parser("checkpoint")
    checkpoint.add_argument("state", type=Path)
    checkpoint.add_argument("--id", required=True)
    checkpoint.add_argument("--result", choices=["pass", "partial", "fail"], required=True)
    checkpoint.add_argument("--misconception", action="append", default=[])
    checkpoint.add_argument("--operation-id")

    summary = commands.add_parser("summary")
    summary.add_argument("state", type=Path)
    return root


def main() -> int:
    args = parser().parse_args()
    if args.command == "init":
        if args.state.exists() and not args.force:
            raise StateError(f"state already exists: {args.state}")
        state = initial_state(
            args.session_id,
            args.field,
            args.goal,
            args.artifact,
            args.language,
            args.style,
            args.register,
        )
        save(state, args.state)
        print(json.dumps({"state": str(args.state), "status": "initialized"}))
        return 0

    state = load(args.state)
    if args.command == "validate":
        print(json.dumps({"status": "valid", "version": state["version"]}))
    elif args.command == "next":
        print(json.dumps({"ready": ready_concepts(state)}, ensure_ascii=False))
    elif args.command == "summary":
        print(json.dumps(summarize(state), ensure_ascii=False))
    else:
        operation_id = args.operation_id
        if operation_id and any(
            event.get("id") == operation_id for event in state["events"]
        ):
            print(json.dumps({"status": "already-applied", "operation_id": operation_id}))
            return 0
        if args.command == "add":
            add_concept(
                state,
                args.id,
                args.label,
                args.self_report,
                args.requires,
                args.on_map,
            )
            event_type = "concept.upserted"
            payload = {"concept_id": args.id}
        elif args.command == "set-field-status":
            state["field_status"] = args.status
            event_type = "field_status.set"
            payload = {"status": args.status}
        elif args.command == "set-map":
            set_map(state, args.source, args.verification)
            event_type = "map.set"
            payload = {"source": args.source, "verification": args.verification}
        elif args.command == "mark":
            mark(state, args.id, args.node_state, args.reason)
            event_type = "concept.marked"
            payload = {"concept_id": args.id, "state": args.node_state}
        elif args.command == "set-preferences":
            set_preferences(state, args.style, args.register)
            event_type = "preferences.set"
            payload = {
                key: value
                for key, value in {
                    "explanation_style": args.style,
                    "technical_register": args.register,
                }.items()
                if value is not None
            }
        elif args.command == "activate":
            activate(state, args.id)
            event_type = "concept.activated"
            payload = {"concept_id": args.id}
        elif args.command == "checkpoint":
            record_checkpoint(state, args.id, args.result, args.misconception)
            event_type = "checkpoint.recorded"
            payload = {"concept_id": args.id, "result": args.result}
        record_event(state, event_type, payload, operation_id)
        save(state, args.state)
        print(json.dumps({"status": "applied", "operation": event_type}))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except StateError as error:
        raise SystemExit(f"state error: {error}") from error
