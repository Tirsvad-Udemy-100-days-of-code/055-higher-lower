# MIL-001 Project Setup

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-06 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [42b3a09] |

---
## Purpose

Decide whether the project skeleton is sound enough to build the lecture steps on: tooling, configuration, folder layout and repository metadata.

## Deliverable

A Python project with `pyproject.toml`, a Python `.gitignore`, `src/` and `tests/` folders, `constants.py`, a `Doxyfile`, a README from the framework template that explains the local `.venv` and the test run, and a repository description and topics on the git host.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `pyproject.toml` requires Python 3.13 or later and lists Flask as the only runtime dependency | Yes | No |
| 2 | `python -m pytest` runs in a fresh `.venv` and exits with 0 | Yes | No |
| 3 | `.gitignore` ignores `.venv`, caches and `.env` | Yes | No |
| 4 | The README states how to create and use `.venv` and runs `python -m pip install --upgrade pip` | Yes | No |
| 5 | The repository has a description and topics on the git host | Yes | No |

## Dependencies

| Depends on | Reason |
| --- | --- |
| BC-001, SA-001, PP-001 | The baseline must be accepted before code |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 5 and 7 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-08 — inside the few-day effort stated in the Business Case.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add pyproject.toml and project layout | Create `pyproject.toml` (Python 3.13 or later, Flask as the only runtime dependency, pytest as a test extra), the `src/higher_lower/` package and `tests/` folder with a smoke test, so `python -m pytest` runs. | No | |
| 2 | Add constants.py | Create `src/higher_lower/constants.py` holding the heading text, colours, GIF URLs and the number range, so no literal is repeated in the code. | No | |
| 3 | Add Python .gitignore | Add a Python `.gitignore` that also ignores `.venv`, caches, `.env` and generated Doxygen output, so no secret or build output is committed. | No | |
| 4 | Add Doxyfile | Add a `Doxyfile` configured for the Python sources and Doxygen comment style, so API documentation can be generated. | No | |
| 5 | Write README with venv and test instructions | Fill the framework README template: purpose, how to create and use `.venv`, upgrade pip, install, run, test. Lecture screenshots are added by MIL-004. | No | |
| 6 | Set repository description and topics | Set a description and topics on the git host repository through its API, reading the token from `.env` without importing `.env` into the project. | No | |

---

[BC-001]: ../business-case.md
[42b3a09]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/055-higher-lower/commit/42b3a093b773c9743ae3c104e1c30bf3dc480d7c
