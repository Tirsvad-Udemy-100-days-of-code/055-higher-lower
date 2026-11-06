# MIL-004 Docs, Screenshots and Wiki

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-06 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [42b3a09] |

---
## Purpose

Decide whether the documentation lets S02 and S03 understand and run the project: screenshots of each lecture step, the finished README and a wiki in English, Danish and Bahasa Malaysia.

## Deliverable

A screenshot for each of the six lecture steps, a README that shows them and explains how to run the project and its tests, and wiki pages in `en`, `da` and `ms` that explain what each lecture step teaches.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Six screenshots exist, one per lecture step, taken in a container or sandbox, not on the host desktop | Yes | No |
| 2 | The README shows every screenshot | Yes | No |
| 3 | The wiki has the same pages in `en`, `da` and `ms` | Yes | No |
| 4 | Each wiki page explains what the lecture step teaches | Yes | No |
| 5 | `check-readme.sh` and `check-languages.sh` pass | Yes | No |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-003 | The finished application is what the screenshots show |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 5 and 6 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-11-16 — closes the few-day effort stated in the Business Case.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Capture lecture step screenshots in a container | Run each lecture app and the game in a Docker container (Linux) with a headless browser and capture one screenshot per lecture step, so the host desktop is never used (`framework/process/gui-testing.md`). | No | |
| 2 | Add screenshots and step overview to README | Show each screenshot in the README with a one-line description of the lecture step. | No | |
| 3 | Write the English wiki | Write the wiki pages in English following `framework/process/wiki.md`: one page per lecture step with its screenshot and what was gained. | No | |
| 4 | Write the Danish wiki | Translate the English wiki to Danish with the same page structure. | No | |
| 5 | Write the Bahasa Malaysia wiki | Translate the English wiki to Bahasa Malaysia with the same page structure. | No | |
| 6 | Publish the wiki | Publish the three language wikis to the git host wiki, if the host exposes it, and check the pages. | No | |

---

[BC-001]: ../business-case.md
[42b3a09]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/055-higher-lower/commit/42b3a093b773c9743ae3c104e1c30bf3dc480d7c
