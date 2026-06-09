# TDD Reading list

A small Python + pytest project for practicing Test Driven Development. 

## Setup

From the project root, create and activate a virtual environment:

```
python3 -m venv .venv
source .venv/bin/activate
```

On Windows, use `.venv\Scripts\activate` instead.

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

Work through the features one by one, in the order of your choosing. Make sure to practice Test Driven Development as you go.

## 3 Rules of TDD
1. Write no production code unless it is to make a failing unit test pass.
1. Write only enough of a unit test to fail (compilation failures count as a failure).
1. Write only enough production code to pass the currently failing test.

**NOTE**: Refactoring after step 3. Refactor ONLY when all tests pass.

## Project layout

| | |
|---|---|
| `requirements.txt` | Project dependencies (pytest) |
| `src/` | Your implementation. Empty — you'll create modules here as tests demand them. |
| `tests/` | Your tests. Empty — same. |
| `features/books.feature` | Gherkin scenarios for L1–L3 exercises |
| `features/remove-and-filter.feature` | Feature-handover exercise for L4 |


## Import Note
* a module at `src/books.py` is importable
as `from books import ...` from a test file at
`tests/test_books.py`. 
* The pytest config sets `pythonpath = ["src"]`
so this works without packaging.
