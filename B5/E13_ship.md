# Step 13 - Ship it

**At the end:** a stranger clones your repository, follows your README, and
everything runs. You can explain every file of it.

## Do

1. Tools, clean:

   ```bash
   uv run ruff format .
   uv run ruff check .
   uv run pytest
   uv build
   ```

2. Type annotations on every function, a docstring on every class and on the
   functions whose name is not enough.
3. The README is yours, the brief goes:
   - what the project does;
   - install, run (command line, server), run the tests;
   - **your structure**: the modules and classes, and why. The questions of
     the brief: where the rules live, how errors say which rule, what would
     change with a database;
   - what is done, what is not, the known bugs.
4. The fresh-clone test: clone your repository into another folder,
   `uv sync`, then each command of your README.

## The oral

Short and individual, on your repository. You explain your structure and one
route from the URL to the rule that answers it, then make a small change
live (for example a new filter on `/api/programme`). The point is to check
that you understand the code you submitted, including the parts an
assistant wrote.

## Levels

| Level | Criteria                                                                                                        |
| ----- | --------------------------------------------------------------------------------------------------------------- |
| P1    | runs from a fresh clone; the rules of the brief hold; clear error messages; readable code (steps 00 to 08)      |
| P2    | coherent classes: inheritance, abstract classes, encapsulation, your own errors, storage apart (steps 09 to 11) |
| P3    | the whole `API.md`, your tests, ruff clean, annotations and docstrings, `uv build` (steps 12 and 13)            |

Extension: a second storage in SQLite (e.g. SQLModel), chosen with an option,
without changing the festival classes.
