# Step 12 - The whole contract, tested

**At the end:** every line of `API.md` is implemented, and tests check the
API through HTTP without starting a server and without touching
`data/festival.json`.

The website and the admin work, but `API.md` holds more than they use (the
`?venue=` filter, `PUT` on a busy slot, a `500` when the file cannot be
written…). And testing the admin by hand after every change takes ten
minutes. An API is a contract: tests prove it is kept.

## Learn

- **`TestClient(app)`** sends requests to the application directly:
  `client.post("/api/performances", json=body)`, then
  `response.status_code`, `response.json()`.
- **An application factory**: a function `create_app(storage)` that builds
  the application around a storage. The server gives it the real file, each
  test a copy in `tmp_path`. A global `festival = ...` at the top of the
  module makes tests depend on each other.
- **Status codes**: read the _Errors_ section of `API.md` again; a test per
  line of that table.

On the side: [side/e12_notes_api.py](side/e12_notes_api.py) and
[side/test_e12_notes_api.py](side/test_e12_notes_api.py), a small API built
by a factory and its tests.

```bash
uv run pytest B5/side -v
```

## Do

1. The application built by a function that receives the storage.
2. Go through `API.md` line by line, with a test for each behaviour: reading
   routes and their filters, each error status, `PUT` that changes the id,
   `PUT` refused that changes nothing, a workshop full, `DELETE` twice.
3. Fix what the tests reveal.

## Check

```bash
uv run pytest -v
```

Every test passes, `data/festival.json` is unchanged afterwards
(`git status`), and `uv run deauville serve` still runs the website and the
admin.

The trainer will start your server on a fresh copy of the data and call each
route of `API.md`: what is in the contract is checked, what is not is free.

## Going further

Practice repository: `B5/api.md`, `B5/examples/03_bodies_errors.ipynb`;
exercises `B5/exercises/02_bodies_errors`, `03_festival_api`.
