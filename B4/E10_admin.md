# Step 10 - The admin: writing through the API

**At the end:** on <http://127.0.0.1:8000/admin/> the organisers schedule,
move and cancel performances, register participants and add artists. Every
rule holds, every refusal is a clear message, every change is saved.

The website only read. The admin writes, so the API receives data from
outside: a lineup on a busy stage, a workshop already full, a body with a
missing field. Two questions come with it. Can any code bypass the rules?
(Try `festival.performances.append(...)` or its equivalent in your code.)
And how does a route know whether an error means "not found" (`404`),
"conflict" (`409`) or "invalid value" (`422`)?

## Learn

- **Encapsulation**: `_performances` with an underscore is "not for the
  outside". Read through methods or properties that return a **copy**. Change
  only through methods that check the rules.
- **Your own exceptions**: `class FestivalError(Exception)` and subclasses
  (not found, conflict, invalid…). `except FestivalError` catches the whole
  family; the type says what went wrong.
- **One exception handler** in the API turns each type into a status:
  `@app.exception_handler(FestivalError)`. Routes never write `try`.
- **Request bodies**: a `pydantic.BaseModel` describes the JSON expected;
  FastAPI refuses another shape with a `422`.
- `POST` creates (`201`), `PUT` replaces (`200`), `DELETE` removes (`204`,
  no body).

On the side: [side/e10_bank.py](side/e10_bank.py) (an account nobody can
cheat, a family of errors) and [side/e10_bank_api.py](side/e10_bank_api.py)
(write routes, bodies, a handler).

```bash
uv run uvicorn e10_bank_api:app --reload --app-dir B4/side
```

## Do

1. Close the doors: the collections of the festival and of a lineup or a
   workshop cannot be changed from outside.
2. Replace `ValueError` by your family of errors; the command line catches
   the family, the API maps it to the statuses of `API.md` (_Errors_).
3. The routes of _Write (admin)_ in `API.md`. After each change, save the
   data file. Moving a performance that breaks a rule changes nothing.
4. Serve `web/admin/` at `/admin/` (before the mount of `/`).
5. Tests: the rules of step 09 through the festival, and a refused move
   leaving the schedule as it was.

## Check

In the admin, then restart the server and reload: what you did is still
there.

| Do                                                            | Expected                                    |
| ------------------------------------------------------------- | ------------------------------------------- |
| a solo show at Le Kiosque, 13 June 11:00, 45 min, Nora Lebrun | listed, and on the website                  |
| the same at 11:30                                             | refused: Le Kiosque is busy                 |
| Nora Lebrun at Grand Casino, 13 June 12:00                    | refused: Nora Lebrun is on stage            |
| a lineup with one act                                         | refused: at least two acts                  |
| _Edit_ the first show: move it to 12:00                       | its id becomes `le-kiosque-2027-06-13-1200` |
| _Edit_ it to 15:00 (Maya Choukri plays there)                 | refused, the show stays at 12:00            |
| _Register_ a participant in Stand-up Lab, twice the same name | the second is refused                       |
| add the artist `Zoé Tanguy`, then `zoe tanguy`                | the second is refused: it already exists    |

## Going further

Practice repository: `B4/examples/01_encapsulation.ipynb`,
`B5/examples/03_bodies_errors.ipynb`; exercises `B4/exercises/01_encapsulation`,
`B5/exercises/02_bodies_errors`.
