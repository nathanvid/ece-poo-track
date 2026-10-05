# B3 - A web API, then classes

## Steps

| Step                                             | Notions                                                                        |
| ------------------------------------------------ | ------------------------------------------------------------------------------ |
| [06 The website lights up](E06_first_routes.md)  | HTTP, FastAPI routes, modules, `__name__`, static files                        |
| [07 The first classes](E07_classes.md)           | `class`, `self`, `@property`, methods, `@dataclass`, path and query parameters |
| [08 The festival object](E08_festival_object.md) | a class holding a collection, `__lt__` `__eq__` `__str__`, pytest              |

Step 08 done before B4: the programme and "on stage now" on the website, tests passing.

## Side examples

Run them from the track folder, e.g.

```bash
uv run uvicorn e06_quotes_api:app --reload --app-dir B3/side
```

| File                                                | Shows                                                  |
| --------------------------------------------------- | ------------------------------------------------------ |
| [e06_quotes_api.py](side/e06_quotes_api.py)         | an API of quotes: list, filter, 404                    |
| [e06_temperatures.py](side/e06_temperatures.py)     | a module with a demo under `if __name__ == "__main__"` |
| [e06_weather_report.py](side/e06_weather_report.py) | a file importing the module above                      |
| [e07_movie.py](side/e07_movie.py)                   | a class with a property and a view; a dataclass        |
| [e08_library.py](side/e08_library.py)               | a library holding its books and its rules              |
| [test_e08_library.py](side/test_e08_library.py)     | its tests: fixture, assert, `pytest.raises`            |

## Practice repository

Optional, for more practice: `B3/examples`, `B3/testing.md`, `B5/examples/01_http_json.ipynb` and `02_routes.ipynb`, exercises `B3/exercises/01` to `04`, `B5/exercises/01_first_routes`.
