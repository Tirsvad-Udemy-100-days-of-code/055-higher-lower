# MIL-003 Higher or Lower Game

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-06 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---
## Purpose

Decide whether the final project, the Higher or Lower game as a website, meets the assignment.

## Deliverable

A Flask application (`server.py` entry point, as the assignment names it, delegating to the package) with the home route, the guess route, a game module that holds the logic and tests that cover every answer path.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `/` shows an `<h1>` "Guess a number between 0 and 9" and a GIF | Yes | No |
| 2 | `/<int:guess>` answers too low, too high or correct, each with a different heading colour and GIF | Yes | No |
| 3 | The secret number is random in the range from `constants.py` and fixed for the process | Yes | No |
| 4 | Tests cover low, high, correct, home and a number outside the range | Yes | No |
| 5 | `python server.py` starts the app as the README says | Yes | No |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-002 | Reuses the HTML rendering step and the app layout |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 1, 2 and 4 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-12 — follows MIL-002 within the Business Case's few-day effort.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Implement game logic | Write a pure function that compares a guess with the secret number and returns low, high or correct, so the rule can be tested without Flask. | No | |
| 2 | Implement home and guess routes | Build the Flask app factory and the routes `/` and `/<int:guess>` that render the headings, colours and GIFs from `constants.py`. | No | |
| 3 | Add server.py entry point | Add `server.py` at the project root, the file name the assignment asks for, that starts the app. | No | |
| 4 | Test the game with pytest | Test the logic and routes with a fixed secret number, covering low, high, correct, home and out-of-range input. | No | |

---

[BC-001]: ../business-case.md
