# MIL-002 Lecture Steps

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-06 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [42b3a09] |

---
## Purpose

Decide whether the Day 55 lecture material (routes, URL variables, HTML rendering, decorators) is implemented, tested and readable, so the final game can reuse it.

## Deliverable

One small module per lecture step under `src/higher_lower/lectures/`, each runnable on its own, with the assignment's function names, plus pytest tests for each.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The URL-path step serves `/`, `/bye` and `/username/<name>` with debug mode available | Yes | No |
| 2 | The HTML step returns an `<h1>` with inline CSS, a paragraph and an image | Yes | No |
| 3 | `make_bold`, `make_emphasis` and `make_underlined` wrap text in `<b>`, `<em>` and `<u>` | Yes | No |
| 4 | `is_authenticated` runs the function only for a logged-in `User`, using `*args` and `**kwargs` | Yes | No |
| 5 | Tests for every step pass | Yes | No |
| 6 | Docstrings use Doxygen comments | Yes | No |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-001 | Needs the project skeleton and constants |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 3 and 4 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-10 — follows MIL-001 within the Business Case's few-day effort.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Implement URL paths and variable routes step | Build the lecture's Flask app with routes `/`, `/bye` and `/username/<name>` (with a converter such as `<int:number>`), runnable in debug mode, so S02 can see how Flask parses URL paths. | No | |
| 2 | Implement HTML rendering step | Return an `<h1>` with inline CSS centring, a paragraph and images (a still image and a GIF with a width attribute) from a route, showing that Flask returns HTML strings. | No | |
| 3 | Implement make_bold, make_emphasis and make_underlined | Write the three decorators with the assignment's names and apply them to the `/bye` route, so HTML tags are added without repeating them in each function. | No | |
| 4 | Implement is_authenticated with *args and **kwargs | Write the `User` class and the `is_authenticated` decorator that reads the first positional argument, so a blog post can be created only by a logged-in user. | No | |
| 5 | Test the lecture steps with pytest | Write pytest tests with the Flask test client for each step, with no network access, so the behaviour is proven. | No | |

---

[BC-001]: ../business-case.md
[42b3a09]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/055-higher-lower/commit/42b3a093b773c9743ae3c104e1c30bf3dc480d7c
