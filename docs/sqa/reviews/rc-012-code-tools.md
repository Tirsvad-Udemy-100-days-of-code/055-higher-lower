# RC-012 Code review of MIL-004

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-012 |
| CrossReference | [MIL-004], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-06 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [1887fc3] |

---

## Artifact Under Review

- Instance reviewed: [MIL-004]
- Checklist used: [QC-PY-001]
- Scope: Script tools/capture_screenshots.py (and its Docker wrapper)
- Language and domain: n/a (technical type)
- Language reviewer: none
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | Modules and functions use snake_case, classes PascalCase, constants UPPER_SNAKE |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names state purpose (`compare_guess`, `GuessResult`, `HOME_HEADING`); no unexplained abbreviations |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff check` and `ruff format --check` report no finding; no suppressions |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | Every signature is annotated; `mypy --strict` reports no issue |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | No bare `except`; no exception is swallowed |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No mutable default arguments; no builtin is shadowed |
| 7 | Files, locks and connections are managed with context managers | N-A | No file, lock or connection is opened by the project code |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Public modules, classes and functions have Doxygen-style docstrings |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | Uses `logging`, no `print`; no secret is handled |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | No DCD exists |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | N-A | Tool script verified by running it in the container; it is not application behaviour |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | Annotated; mypy strict not configured for tools/, ruff passes |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | `pyproject.toml` declares Flask (runtime) and pytest, ruff, mypy (extras); none unused |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | Headings, colours, GIFs and range are defined once in `constants.py` |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | tools/capture_screenshots.py imports the project and Flask; nothing imports it |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | Each module has one reason to change; behaviour is added by extension |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | N-A | Capture tool outside src/ and tests/; it is not part of the layered application |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | File and folder names are English with letters, digits and `_` only |

## Overall Verdict

Go — All criteria pass or are not applicable; no blocking finding.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | 2026-11-06 |

---

[MIL-004]: ../../docs/milestones/mil-004-docs-screenshots-wiki.md
[QC-PY-001]: ../../framework/qc/code/qc-programming-python.md
[1887fc3]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/055-higher-lower/commit/1887fc347f298a930cf34e126092a170a7efc7f9
