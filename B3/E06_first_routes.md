# Step 06 - The website lights up

**At the end:** `uv run uvicorn api:app --reload` starts a server; on
<http://127.0.0.1:8000> the website shows the dates of the festival, the tabs
of the days, the venues and the artists. The programme stays empty: that is
step 07.

The website of `web/public/` is written, but it is only HTML and JavaScript:
it cannot read `festival.json`, it cannot call your Python functions. It asks
a server through HTTP, at the addresses listed in `API.md`. Your program
becomes that server.

## Learn

- **HTTP**: the browser sends a request (`GET /api/venues`), the server
  answers a status (`200` OK, `404` not found…) and a body, here JSON.
- **FastAPI**: a route is a function with a decorator. What it returns
  becomes JSON.

  ```python
  @app.get("/api/venues")
  def list_venues() -> list[dict]: ...
  ```

- **Modules**: `api.py` needs the functions of `main.py`, but `main.py` runs
  its commands as soon as it is imported. Move the functions about the
  festival into a file of their own (say `festival.py`); `main.py` keeps the
  command line, `api.py` the routes, and both import the same functions.
  `if __name__ == "__main__":` runs a block only when the file is the one
  started.
- **Static files**: `app.mount("/", StaticFiles(directory="web/public",
html=True))`, after the routes, serves the website.

On the side: [side/e06_quotes_api.py](side/e06_quotes_api.py) (an API of
quotes, with a 404), [side/e06_temperatures.py](side/e06_temperatures.py)
and [side/e06_weather_report.py](side/e06_weather_report.py) (one file
imports another).

```bash
uv run uvicorn e06_quotes_api:app --reload --app-dir B3/side
```

## Do

1. Split your code: the festival functions in one module, the command line in
   another. Every command of step 05 still works.
2. `uv add fastapi uvicorn`, then `api.py` with the first three routes of
   `API.md`: `GET /api/festival`, `GET /api/venues`, `GET /api/artists`. Read
   the _Objects_ section of `API.md`: field names are a contract, the
   website reads exactly those.
3. Serve `web/public/` at `/`.
4. Open <http://127.0.0.1:8000/docs>: FastAPI lists your routes and lets you
   call them.

## Check

```bash
uv run uvicorn api:app --reload
```

| Open                                 | You see                                                                                                                                                              |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <http://127.0.0.1:8000/api/festival> | `{"name": "Deauville Festival du Rire 2027", "first_day": "2027-06-10", "last_day": "2027-06-13", "days": ["2027-06-10", "2027-06-11", "2027-06-12", "2027-06-13"]}` |
| <http://127.0.0.1:8000/api/venues>   | 4 venues, each with `slug`, `name`, `capacity`, `address`, in the order of the file                                                                                  |
| <http://127.0.0.1:8000/api/artists>  | 12 artists with their `slug`, Élodie Marchal first (sorted by slug)                                                                                                  |
| <http://127.0.0.1:8000/>             | dates, days, venue filter, artist grid                                                                                                                               |

The website calls routes that do not exist yet: in the browser console
(`F12`), `404` on `/api/programme` and `/api/now`. Expected.

## Going further

Practice repository: `B5/examples/01_http_json.ipynb`, `02_routes.ipynb`;
exercises `B5/exercises/01_first_routes`; `B4/packaging.md` (modules).
