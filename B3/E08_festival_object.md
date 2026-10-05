# Step 08 - The festival holds the rules, and tests prove it

**At the end:** "On stage now" appears on the website, one object holds the
whole festival and its rules, and `uv run pytest` checks every rule of the
brief.

Your rules of step 05 still work on lists of dicts, and the new classes do
not know them. Where do they go? Not in a route (the command line would not
check them), not in `main.py` (the API would not). In the object that holds
the venues, the artists and the schedule: the festival itself.

## Learn

- A class that holds a collection: `self._performances` and methods to add,
  find, list. The methods are the only way in, so the rules always apply.
- Special methods: `__lt__` lets `sorted()` order performances (by start,
  then venue name); `__eq__` says when two artists are the same (same slug);
  `__str__` gives the line printed by the command line.
- **pytest**: a function `test_...` that builds a situation, acts, and
  `assert`s. `pytest.raises(ValueError)` checks that a rule refuses. A
  fixture builds a fresh festival for each test.

On the side: [side/e08_library.py](side/e08_library.py) (a library that
holds its books and its loan rules, `__lt__` and `__str__`) and
[side/test_e08_library.py](side/test_e08_library.py) (its tests).

```bash
uv run pytest B3/side -v
```

## Do

1. A class for the festival: name, days, venues, artists, performances.
   Adding a performance checks every rule of step 05. The programme of a day,
   the performances of an artist, what is on stage at a moment, the next
   ones: methods.
2. The command line and the API go through it. `add` and `cancel` too.
3. `GET /api/now` (`?at=` replaces the current time): `now_playing` and
   `up_next` (3 at most).
4. `uv add --dev pytest`, a folder `tests/`, and at least one test per rule:
   venue busy, artist busy in another venue, artist busy as an act of a
   lineup, a show at 01:00 belonging to the previous day, a day outside the
   festival, a duration of 0 or 361, an unknown venue or artist.

## Check

| Check                                        | Expected                                                                   |
| -------------------------------------------- | -------------------------------------------------------------------------- |
| <http://127.0.0.1:8000/?at=2027-06-11T21:00> | On stage now: Tall Tales; up next: Straight Face, Late Laughs, After Hours |
| <http://127.0.0.1:8000/?at=2027-06-12T01:30> | On stage now: After Hours                                                  |
| `uv run pytest`                              | every test passes, at least one per rule above                             |
| the commands of step 05                      | same outputs                                                               |

Try to break your own rules: can `main.py` add a performance without the
check? If one line of code can, step 10 will close that door.

## Going further

Practice repository: `B3/examples/03_special_methods.ipynb`, `testing.md`;
exercises `B3/exercises/03_special_methods`.
