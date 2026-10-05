# Step 05 - Rules, errors and saving

**At the end:** `uv run main.py add` schedules a solo show if the rules of
the brief allow it, saves it in the data file, and every mistake gives a
sentence instead of a traceback.

Until now the program only reads. As soon as it writes, it must refuse what
breaks the festival: a venue booked twice, an artist on two stages, a show on
15 June.

## Learn

- `raise ValueError("Le Kiosque is busy with After Hours.")` stops the
  function at once, and goes up to the first caller that catches it.
- `try: ... except ValueError as error: print(f"Error: {error}")` catches it.
  Catch in **one** place, `main`, not in every function: the functions that
  check rules only raise.
- Catch precisely: `except json.JSONDecodeError`, `except
FileNotFoundError`. `except Exception` also hides your own bugs.
- Writing: `open(path, "w", encoding="utf-8")` and `json.dump(data, file,
ensure_ascii=False, indent=2)`. Now you can explain the three lines of
  step 00.
- Two shows are too close when `start1 < end2 + gap and start2 < end1 + gap`.
  Draw it on paper with two bars on a time line.

On the side: [side/e05_room_bookings.py](side/e05_room_bookings.py), room
bookings with rules, a damaged file, and a JSON file written back.

## Do

1. A function that checks a new performance against the rules of the brief
   (_Venues, performances and time_): known venue and artists, duration from 1
   to 360 minutes, a day of the festival, 30 minutes for the venue, 30 minutes
   for each artist in any role. It raises `ValueError` with a sentence.
2. `add`: asks title, artist, venue, start, duration; checks; adds; saves.
3. `cancel ID`: the id of a performance is its venue slug and its start,
   `le-kiosque-2027-06-12-0100`. Unknown id: an error.
4. Every wrong input (a day like `June-11`, a duration like `half an hour`, a
   damaged data file) prints `Error: ...` with a sentence, and the program
   stops with exit code 1 (`sys.exit(1)`).

Commit before testing `add`: you will damage the data file at least once.
`git restore data/festival.json` brings it back.

## Check

```
$ uv run main.py add
Title: Too Late
Artist (slug): karim-benali
Venue (slug): le-kiosque
Start (YYYY-MM-DDTHH:MM): 2027-06-12T02:15
Duration (minutes): 30
Error: Le Kiosque is busy with After Hours (2027-06-12 01:00-02:00).
```

Other answers (any title; the last one is `Morning Coffee`):

| Answers (artist, venue, start, duration)                        | Expected                                                                 |
| --------------------------------------------------------------- | ------------------------------------------------------------------------ |
| `max-pellerin`, `la-cabane`, `2027-06-11T23:00`, `30`           | `Error: Max Pellerin is on stage in Late Laughs.`                        |
| `karim-benali`, `la-cabane`, `2027-06-14T08:00`, `30`           | `Error: 2027-06-14 is not a day of the festival.`                        |
| `karim-benali`, `la-cabane`, `2027-06-13T08:00`, `half an hour` | `Error: 'half an hour' is not a number of minutes.`                      |
| `karim-benali`, `la-cabane`, `2027-06-13T08:00`, `30`           | `Added: la-cabane-2027-06-13-0800`, first line of `programme 2027-06-13` |

```
$ uv run main.py cancel la-cabane-2027-06-13-0800
Cancelled: Morning Coffee
$ uv run main.py programme June-11
Error: 'June-11' is not a day, use YYYY-MM-DD.
```

Your sentences may be worded differently; they must name what is wrong.

## Going further

Practice repository: `B2/examples/02_errors.ipynb`, `03_files.ipynb`;
exercises `B2/exercises/02_errors`, `03_files`.
