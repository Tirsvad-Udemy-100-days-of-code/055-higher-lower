# Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-06 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [42b3a09] |

---
## Purpose

This analysis names the people who care about the Higher or Lower project and what each needs, so later documents cite stakeholder IDs. It uses the power/interest grid.

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant, Product Owner, developer and reviewer | Private | HIGH | HIGH | Manage Closely | Finish the assignment with professional quality |
| S02 | Udemy coursists | Fellow course participants | Udemy course community | LOW | HIGH | Keep Informed | Readable, runnable code with the assignment's function names, and run instructions |
| S03 | GitHub viewers | Repository visitors | Public | LOW | MEDIUM | Monitor | A clear description, topics and README, and no runtime dependencies beyond the need |

## Power/Interest Classification Rationale

- **Manage Closely (S01):** decides scope, writes and reviews everything.
- **Keep Informed (S02):** cannot change the project but depends on its README and code to learn.
- **Monitor (S03):** browses the repository; the only need is a clear first impression.

## Primary Concerns and FURPS+ Mapping

| Concern ID | Stakeholder | Concern | FURPS+ attribute |
| --- | --- | --- | --- |
| CN-001 | S01 | The game works as the assignment describes | Functionality |
| CN-002 | S01 | Work is planned, reviewed and traceable per pull request | Supportability |
| CN-003 | S02 | Code is readable and uses the assignment's function names | Usability |
| CN-004 | S02 | The README explains how to run the app and the tests | Usability |
| CN-005 | S02 | Each lecture step has a screenshot and an explanation in English, Danish and Bahasa Malaysia | Usability |
| CN-006 | S03 | The repository has a description, topics and a clear README | Usability |
| CN-007 | S03 | No runtime dependencies beyond Flask | Supportability |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| CM-001 | Chat with S01 | At plan acceptance and at the end of the run | Plan dry run, then run summary | All milestones |
| CM-002 | Pull request | Once per milestone | Reviewed change set | Each milestone |
| CM-003 | README and wiki | At release | Instructions, screenshots, explanations | Documentation milestone |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| S01 wants a small solution; S02 and S03 want clear documentation in three languages | S01, S02, S03 | Keep the code small and put the explanation in the README and wiki |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | CN-001 | Objectives 1, 2 and 3 in [BC-001] |
| S01 | CN-002 | Branch and pull request constraint in [BC-001] |
| S02 | CN-003, CN-004 | Objectives 3, 4 and 5 in [BC-001] |
| S02 | CN-005 | Objective 6 in [BC-001] |
| S03 | CN-006, CN-007 | Objective 7 and success criterion 6 in [BC-001] |

## Sign-Off

| Stakeholder | Decision | Date |
| --- | --- | --- |
| S01 | Go (RC-002, AI as stand-in for S01) | 2026-11-06 |

---

[BC-001]: ./business-case.md
[42b3a09]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/055-higher-lower/commit/42b3a093b773c9743ae3c104e1c30bf3dc480d7c
