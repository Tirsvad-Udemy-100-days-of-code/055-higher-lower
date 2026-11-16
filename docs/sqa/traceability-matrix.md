# Traceability Matrix

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001], [SA-001], [PP-001], [MIL-001], [MIL-002], [MIL-003], [MIL-004], [MIL-005], [RC-001], [RC-002], [RC-003], [RC-004], [RC-005], [RC-006], [RC-007], [RC-008], [RC-009], [RC-010], [RC-011], [RC-012], [RC-013], [RC-014], [RC-015], [RC-016], [RC-017] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-16 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version; accepted with the baseline milestone MIL-005 (autonomous, not independent) | pending |

---

## Purpose

Tracks backward and forward links between the artifact instances of Higher or Lower so that the traceability of the documents is measurable. A row is added or updated whenever an instance is created or reviewed. The matrix is new in MIL-005; before that the project had no traceability matrix, and the links below are read from the documents and review records that exist.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | Business Case | en | education | - | [SA-001], [PP-001], [MIL-005] | [RC-014], [RC-001] |
| [SA-001] | Stakeholder Analysis | en | it | [BC-001] | [PP-001] | [RC-002] |
| [PP-001] | Project Plan | en | education | [BC-001], [SA-001] | [MIL-001], [MIL-002], [MIL-003], [MIL-004], [MIL-005] | [RC-015], [RC-003] |
| [MIL-001] | Milestone | en | it | [BC-001] | - | [RC-004], [RC-008] |
| [MIL-002] | Milestone | en | it | [BC-001] | - | [RC-005], [RC-009] |
| [MIL-003] | Milestone | en | it | [BC-001] | - | [RC-006], [RC-010] |
| [MIL-004] | Milestone | en | it | [BC-001] | [MIL-005] | [RC-007], [RC-012] |
| [MIL-005] | Milestone | en | education | [PP-001], [BC-001], [MIL-004] | - | [RC-016] |
| Wiki (`docs/wiki/`) | Wiki | en, da, ms | education | [BC-001], [MIL-005] | - | [RC-017], [RC-013], [RC-011] |

## Concern Coverage

| Concern (CN-ID) | Views that answer it | Decisions (ADR) | Quality check (TP) | Status |
| --- | --- | --- | --- | --- |
| - | - | - | - | No concern recorded: the project has no architecture description, so no CN-ID exists |

## Open Inconsistencies

| # | Views | Inconsistency | Found in (RC-ID) | Status | Resolved in |
| --- | --- | --- | --- | --- | --- |
| - | - | none found | - | Closed | - |

## Coverage Notes

- In Upstream, `-` means foundational; in Downstream, `-` means nothing is built on it yet.
- Code is traced through its milestone: [RC-008], [RC-009] and [RC-010] review the code of MIL-001, MIL-002 and MIL-003; [RC-012] reviews the screenshot tool of MIL-004 and [RC-011] and [RC-013] review its wiki.
- The wiki (`docs/wiki/`) is documentation, not an artifact with an ID or a Language and Domain row; it has its own review records, [RC-017], [RC-013] and [RC-011]. The domain of [BC-001], [PP-001], [MIL-005] and the wiki is `education` since [MIL-005]; the other documents keep the domain `it` they were accepted with (see the Open Issues of [PP-001]). [MIL-005] changes no source, test, screenshot or wiki file; its only other change of a file outside `docs/` is the indentation of `tools/capture_screenshots.sh` (task 6).
- No `AD`, `TP`, `ADR` or view exists.

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[MIL-001]: ../milestones/mil-001-project-setup.md
[MIL-002]: ../milestones/mil-002-lecture-steps.md
[MIL-003]: ../milestones/mil-003-higher-lower-game.md
[MIL-004]: ../milestones/mil-004-docs-screenshots-wiki.md
[MIL-005]: ../milestones/mil-005-framework-baseline.md
[RC-001]: ./reviews/rc-001-business-case.md
[RC-002]: ./reviews/rc-002-stakeholder-analysis.md
[RC-003]: ./reviews/rc-003-project-plan.md
[RC-004]: ./reviews/rc-004-mil-001.md
[RC-005]: ./reviews/rc-005-mil-002.md
[RC-006]: ./reviews/rc-006-mil-003.md
[RC-007]: ./reviews/rc-007-mil-004.md
[RC-008]: ./reviews/rc-008-code-mil-001.md
[RC-009]: ./reviews/rc-009-code-mil-002.md
[RC-010]: ./reviews/rc-010-code-mil-003.md
[RC-011]: ./reviews/rc-011-wiki.md
[RC-012]: ./reviews/rc-012-code-tools.md
[RC-013]: ./reviews/rc-013-wiki-published.md
[RC-014]: ./reviews/rc-014-business-case-baseline.md
[RC-015]: ./reviews/rc-015-project-plan-baseline.md
[RC-016]: ./reviews/rc-016-milestone-005.md
[RC-017]: ./reviews/rc-017-wiki-baseline.md
