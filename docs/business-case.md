# Business Case

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-06 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---
## Executive Summary

Day 55 of the Udemy course "100 Days of Code: The Complete Python Pro Bootcamp" asks the participant to build a "Higher or Lower" guessing game as a Flask website. This project delivers that assignment as a small, readable, runnable Python project with tests, documentation, a screenshot for every lecture step and a wiki in English, Danish and Bahasa Malaysia. It is published as a public learning repository that other course participants can read and compare against.

## Methodological and Standards Foundation

The project follows the SQA and QC framework mounted at `framework/` and Larman's *Applying UML and Patterns* where a design artifact is needed. Quality is judged against ISO/IEC 25010:2023. Source code follows the framework's Python conventions and Clean Architecture; tests use pytest.

## Problem Statement

Course participants who finish the Day 55 assignment have no common, readable reference to compare against. Shared solutions are scattered and often lack tests, run instructions or an explanation of what each lecture step teaches. The belief that would kill the idea if false: other participants find a documented, step-by-step solution more useful than the bare assignment code. The idea is a hunch, but it costs only the author's time.

## Business Opportunity

A single repository that holds the finished assignment, explains each lecture step (Flask routes, URL variables, HTML rendering, decorators with `*args` and `**kwargs`) and ties screenshots to the code makes the course material easier to reuse and shows the author's craft to repository visitors.

## Objectives

1. Deliver a Flask application whose home route shows the heading "Guess a number between 0 and 9" and a GIF.
2. Deliver a route `/<int:guess>` that compares the guess with a random number and answers "too low", "too high" or "correct", each with its own heading colour and GIF.
3. Deliver the lecture's decorator exercises (`make_bold`, `make_emphasis`, `make_underlined`, `is_authenticated`) with the assignment's function names.
4. Cover the game logic and the routes with pytest tests.
5. Document in the README how to create and use a local `.venv`, run the application and run the tests.
6. Provide a screenshot for every lecture step in the README and a wiki in English, Danish and Bahasa Malaysia that explains what each step teaches.
7. Publish the repository with a description and topics.

## Scope

### In Scope

- Flask application in `src/`, tests in `tests/`, documents in `docs/`.
- Constants in `constants.py`, project configuration in `pyproject.toml`, a Python `.gitignore`, Doxygen comments and a `Doxyfile`.
- README from the framework template; wiki in `en`, `da` and `ms`.
- A screenshot of each lecture step.
- Repository description and topics on the git host.

### Out of Scope

- Persistent storage, user accounts, deployment to a hosting service.
- Anything from other course days.
- Testing a GUI on the host desktop; browser checks run in a container or sandbox (`framework/process/gui-testing.md`).

## Expected Benefits

### Tangible Benefits

- A runnable, tested repository other participants can clone.
- A README and a three-language wiki that explain every lecture step.

### Intangible Benefits

- Practice in Flask, decorators, testing and documentation.
- A visible, well-structured example for repository visitors.

## Strategic Alignment

The project supports the participant's goal of completing the 100 Days of Code course with professional habits: planned work, tests, reviewed documents and traceable pull requests.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | Game behaviour | Home, too low, too high and correct pages all work | pytest passes for every answer path |
| 2 | Tests | All tests pass on Python 3.13 or later | `python -m pytest` exits with 0 |
| 3 | Run instructions | A new reader runs the app from the README alone | README steps reproduce a running app |
| 4 | Lecture coverage | One screenshot per lecture step | Screenshots listed in the README and in each wiki language |
| 5 | Wiki | Three languages | Pages exist in en, da and ms for every lecture step |
| 6 | Runtime dependencies | Only Flask | `pyproject.toml` lists one runtime dependency |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Giphy GIF links stop working | Pages show a broken image | Keep GIF URLs in `constants.py`; tests do not depend on the network |
| Screenshots need a browser | The host desktop would be taken over | Capture screenshots in a container or sandbox, never on the host desktop |
| Translation errors in da or ms | Misleading wiki text | Keep wiki pages short and structurally identical across languages; S01 reviews |
| Token leak | Credential exposure | Tokens stay in `.env`, which git ignores and the project never imports |

## Assumptions

- S01 is the Product Owner, developer and reviewer; in autonomous mode the AI acts as stand-in reviewer and each review record says so.
- S02 and S03 cannot be reached during the project; their needs come from the assignment text.
- The idea is a hunch with no cost, so no riskiest-assumption test is needed.
- `origin` is `ssh://git@git.tirsystem.com:10022/Tirsvad-Udemy-100-days-of-code/055-higher-lower.git`; the user also named `https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code`, which is treated as the owning organisation or repository family (an open point in the Project Plan).
- The application has a user interface made of four pages; the wireframes are the assignment's own screenshots and the presentation pattern is MVC for the route layer.

## Constraints

- Duration: about ten days, from 2026-11-06 to 2026-11-16; effort is the author's own time and there is no budget.
- Python 3.13 or later, a local `.venv`, pytest, `pyproject.toml`.
- Folders `src/`, `tests/`, `docs/`.
- A branch and a pull request per milestone; no direct commits to `main`.
- No runtime dependency beyond Flask.
- Tokens are read from `.env` for personal use only; the project does not test or import them.
- The PO language is English and the domain is IT.

## Cost–Benefit Assessment

| Costs | Benefits |
| --- | --- |
| Author time of a few days, no money | A reusable learning repository and a portfolio example |
| Effort for three wiki languages | Wider readership for S02 and S03 |

The assessment is qualitative because the project has no budget and no revenue.

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Completes the assignment, owns and reviews the work |
| S02 | Reads and runs the code, compares solutions |
| S03 | Browses the repository for ideas |

## Recommendation

Proceed — the scope is small, the cost is time only and the result is a reusable, documented learning project.
