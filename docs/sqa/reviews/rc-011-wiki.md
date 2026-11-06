# RC-011 Wiki review

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-011 |
| CrossReference | [MIL-004], [QC-WIKI-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-06 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [9be5031] |

---

## Artifact Under Review

- Instance reviewed: [MIL-004]
- Checklist used: [QC-WIKI-001]
- Scope: full review of docs/wiki/ (25 files), the deliverable of MIL-004 tasks 3 to 5
- Language and domain: en, da, ms (wiki, not a PO-language artifact type)
- Language reviewer: none; the Danish and Bahasa Malaysia translations are by the AI and are not independently checked
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The wiki has a `_Sidebar.md`, because the host lists subpages only through it | Pass | docs/wiki/_Sidebar.md exists |
| 2 | The sidebar starts with the wiki's title in bold, then one list of the pages in the primary language (English), `Home` first | Pass | Sidebar starts with the bold title Higher or Lower, then one English page list with Home first |
| 3 | The page list holds a link to every English page of the wiki, and no link points to a page that does not exist | Pass | All seven English pages are listed; a script checked that every link in the pages resolves to a file |
| 4 | A `**Related**` section follows the page list only when the wiki has related wikis (for example the checklists wiki for a framework wiki); each entry is a link to that wiki's Home. A wiki with nothing related has no such section | N-A | The wiki has no related wikis, so no Related section |
| 5 | A `**Languages**` section is the last section of the sidebar. It has one line per language, the language written in that language, linking to that language's `Home` page | Pass | Languages section is last: English, Dansk, Bahasa Melayu, each linking to its Home |
| 6 | The sidebar does not repeat the page list per language | Pass | The page list appears once |
| 7 | A sidebar produced by a generator carries a comment that says so and names the generator; the generator is changed, not the page | N-A | The sidebar is hand-written, not generated |
| 8 | The wiki has a `Languages` line on each page (criterion 11), so the sidebar is not the only way to switch language | Pass | Every page starts with the language line |
| 9 | Every wiki exists in English and, as a minimum, in the language the project's registry names as the PO language; further languages are added on top, never instead of English | Pass | English, Danish and Bahasa Malaysia exist; the PO language is English |
| 10 | Every English page has a page in each other language of the wiki: the page sets are identical | Pass | Eight pages (Home, six lecture pages, Run-and-Test) exist in each language |
| 11 | Every page starts with the language line, with the current language in bold and a link to the same page in each other language | Pass | Each page starts with the language line, current language in bold |
| 12 | A page in a language other than English is named `<Page>-<code>.md`, with a BCP 47 code; English has no suffix | Pass | Danish and Bahasa Malaysia pages are named Page-da.md and Page-ms.md; English has no suffix |
| 13 | Code blocks, commands, file names and IDs stay in English in every language | Pass | Code, commands, file names and IDs are English in every language |
| 14 | The sidebar, every page and every link were checked on the published wiki after the change, not only in the repository | Pending | Can be checked only on the published wiki after the merge; the publish workflow copies docs/wiki on merge. To be closed by a delta re-review |
| 15 | A change to the layout rules (sections, order, naming) is made in the generator or template and in this checklist's source rules together | N-A | No change to layout rules |
| 16 | The wiki folder (`docs/wiki/`) is flat: every page, `Home.md` and `_Sidebar.md` included, is directly in it, and languages are told apart by file name, never by a subfolder | Pass | All pages and the sidebar are directly in docs/wiki, no subfolder |

## Overall Verdict

Go-with-conditions — All criteria pass except 14, which can only be checked on the published wiki after the merge (Pending); the action item closes it.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Check the published sidebar, every page and every link on the host after the merge and record a delta re-review | S01 | 2026-11-16 |
| Native-speaker check of the Danish and Bahasa Malaysia text | S01 | 2026-11-16 |

---

[MIL-004]: ../../docs/milestones/mil-004-docs-screenshots-wiki.md
[QC-WIKI-001]: ../../framework/qc/artifacts/qc-wiki.md
[9be5031]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/055-higher-lower/commit/9be50311a022aa5df44af273ccc48723ab854b4d
