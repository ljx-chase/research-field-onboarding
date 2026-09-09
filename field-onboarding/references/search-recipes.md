# Search recipes

Use these when you need to verify a reference, check how settled a field is, or
hand the reader a way to find ground truth you could not give them.

Two rules govern everything here. If you can search, search, and label what you
found as verified. If you cannot, give the reader the query itself rather than a
citation you have not checked. A query they can run is worth more than a
citation they cannot trust.

## Is there a review?

This is the first question in an unfamiliar field, and the answer decides
whether you are teaching consensus or reconstructing it.

- OpenAlex, reviews only, most cited first:
  `https://api.openalex.org/works?filter=title_and_abstract.search:<TOPIC>,type:review&sort=cited_by_count:desc&per-page=10`
- Plain search, for a human rather than an API:
  `<TOPIC> review` or `<TOPIC> tutorial` on Google Scholar, sorted by citations
- Annual Reviews, Reviews of Modern Physics, Chemical Reviews, and Physics
  Reports are worth checking by name in the physical sciences; a hit there
  usually means the field is settled enough to have a canonical account

If nothing comes back, that is itself the finding: say the field has no review
yet and switch to the unsettled-field mode in `SKILL.md`.

## How current is my picture?

- Recent work only:
  `https://api.openalex.org/works?filter=title_and_abstract.search:<TOPIC>,from_publication_date:<YYYY-MM-DD>&sort=publication_date:desc`
- arXiv, newest first:
  `https://arxiv.org/list/<ARCHIVE>/recent`, or
  `https://export.arxiv.org/api/query?search_query=all:<TOPIC>&sortBy=submittedDate&sortOrder=descending&max_results=20`

Compare what comes back against the account you were about to give. If the
recent work uses vocabulary you did not plan to teach, your picture is stale and
you should say so.

## Does this specific paper exist?

Never assert a title, author list, or year you have not checked, and never
attach a DOI or arXiv ID you did not retrieve.

- By DOI: `https://api.crossref.org/works/<DOI>`
- By title: `https://api.openalex.org/works?filter=title.search:<EXACT TITLE>`
- By arXiv ID: `https://export.arxiv.org/api/query?id_list=<ID>`

A miss means one of two things, and you should say which you believe: the work
does not exist, or it exists outside the index. Do not quietly keep the citation
either way.

## Who is working on this now?

Useful when there is no review and Rung 5 has to be built from groups rather
than from a canonical account.

- Most cited recent work in the area:
  `https://api.openalex.org/works?filter=title_and_abstract.search:<TOPIC>,from_publication_date:<YYYY>-01-01&sort=cited_by_count:desc`
- Then read off the recurring last authors and affiliations rather than guessing
  at them

## Handing the query to the reader

When you cannot search, write the query out in a form they can paste, and say
what to do with the result. For example: run the review query above; if it
returns something from the last five years with a few hundred citations, read
its introduction and section headings, and that will give you the prerequisite
list this session could not.

OpenAlex, Crossref, and the arXiv API are all open and need no key, so a reader
can run any of these in a browser.
