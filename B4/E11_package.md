# Step 11 - A real package

**At the end:** the project installs like any Python tool: `uv run deauville
programme 2027-06-11`, `uv run deauville serve`, and `uv build` produces a
wheel. The storage is a replaceable part.

Your files sit next to each other at the root of the folder, imported by
their file name. It works from this folder only, and nothing says which file
is the program. A package gives the code a name, a place (`src/<name>/`), and
commands.

## Learn

- **Layout**: `src/<name>/__init__.py` makes a package; its modules are
  imported as `from <name>.festival import Festival`, from anywhere.
- **pyproject.toml**: `[project.scripts]` declares a command
  (`deauville = "deauville.cli:main"`), `[build-system]` how to build it.
  `uv sync` installs the project in its own environment.
- **An interface for storage**: an abstract class with `load()` and `save()`;
  the JSON file is one implementation. The festival does not know where it
  is stored; tests can use a storage in memory.
- `uvicorn.run(app, ...)` starts the server from Python: the command line can
  offer `serve`.

On the side: [side/e11_storage.py](side/e11_storage.py), one interface and
two storages; `B4/examples/greetings` in the practice repository, a complete
small package.

## Do

1. Choose the package name, create `src/<name>/` and move your modules into
   it, one subject per module. Fix the imports.
2. In `pyproject.toml`: the command, and the build system:

   ```toml
   [project.scripts]
   deauville = "<name>.cli:main"

   [build-system]
   requires = ["hatchling"]
   build-backend = "hatchling.build"

   [tool.hatch.build.targets.wheel]
   packages = ["src/<name>"]
   ```

   then `uv sync`.

3. The storage behind an interface; the API and the command line receive a
   storage instead of opening the file themselves.
4. A command `serve` that starts the API, and an option for another data
   file (`--data`), handy for tests and for the trainer.

## Check

```bash
uv run deauville programme 2027-06-11     # the output of step 04
uv run deauville serve                    # website and admin as in step 10
uv run pytest                             # every test still passes
uv build                                  # dist/<name>-0.1.0-py3-none-any.whl
```

Delete `.venv`, `uv sync`, run the four lines again: still fine.

## Going further

Practice repository: `B4/packaging.md`, `B4/examples/greetings`; exercises
`B4/exercises/04_modules_package`, `03_abstract_classes/storage`.
