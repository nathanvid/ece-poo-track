# B5 - The whole contract, tested, shipped

## Steps

| Step                                          | Notions                                                        |
| --------------------------------------------- | -------------------------------------------------------------- |
| [12 The whole contract](E12_full_contract.md) | `TestClient`, an application factory, `tmp_path`, status codes |
| [13 Ship it](E13_ship.md)                     | ruff, annotations, docstrings, README, fresh clone, oral       |

The last push before the deadline is graded, then the oral.

## Side examples

Run them from the track folder, e.g.

```bash
uv run pytest B5/side -v
```

| File                                                | Shows                                       |
| --------------------------------------------------- | ------------------------------------------- |
| [e12_notes_api.py](side/e12_notes_api.py)           | an API built by `create_app(path)`          |
| [test_e12_notes_api.py](side/test_e12_notes_api.py) | its tests, each on its own copy of the data |

## Practice repository

Optional, for more practice: `B5/api.md`, `B5/examples`, exercises `B5/exercises/02_bodies_errors`, `03_festival_api`.
