# Reading list — student starter

A small Python + pytest project for practicing Test Driven Development. This is the **student exercise project**;
it mirrors the instructor's `todone` demo so every TDD move
transfers.

## Setup

From the project root, create and activate a virtual environment:

```
python -m venv venv
source venv/bin/activate
```

On Windows, use `venv\Scripts\activate` instead.

Then install dependencies:

```
pip install -r requirements.txt
```

Run the tests with:

```
pytest
```

Pytest will report no tests at first. That's expected — you'll
TDD them into existence as you follow the steps of TDD.

## Project layout

| | |
|---|---|
| `requirements.txt` | Project dependencies (pytest) |
| `src/` | Your implementation. Empty — you'll create modules here as tests demand them. |
| `tests/` | Your tests. Empty — same. |
| `features/books.feature` | Gherkin scenarios for L1–L3 exercises |
| `features/remove-and-filter.feature` | Feature-handover exercise for L4 |
| `BACKLOG.md` | Candidate features for the L4 selection-autonomy discussion |

Imports work like this: a module at `src/books.py` is importable
as `from books import ...` from your test file at
`tests/test_books.py`. The pytest config sets `pythonpath = ["src"]`
so this works without packaging.
