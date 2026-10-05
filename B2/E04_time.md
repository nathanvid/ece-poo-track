# Step 04 - Real dates and times

**At the end:** the bug of step 02 is fixed, every line shows when the show
ends, and `uv run main.py now 2027-06-11T21:00` tells what is on stage.

`"2027-06-12T01:00"[:10]` is a piece of text: it cannot "move back 6 hours",
it cannot tell when a show of 75 minutes ends. `datetime` can.

## Learn

| Need                     | Code                                                     |
| ------------------------ | -------------------------------------------------------- |
| text → moment            | `datetime.fromisoformat("2027-06-12T01:00")`             |
| text → day               | `date.fromisoformat("2027-06-11")`                       |
| a duration               | `timedelta(minutes=75)`, `timedelta(hours=6)`            |
| end of a show            | `start + timedelta(minutes=duration)`                    |
| the day of a moment      | `moment.date()`                                          |
| display                  | `f"{start:%H:%M}"`, `f"{day:%A %d %B}"` → Friday 11 June |
| compare                  | `start <= at < end`                                      |
| sort by a computed value | `sorted(performances, key=start_of)`                     |

The rule of the brief, in one line: the festival day of a show is the date
of its start **minus 6 hours**.

On the side: [side/e04_night_buses.py](side/e04_night_buses.py), a bus
company whose service day ends at 4 am.

## Do

1. Functions for the start, the end and the festival day of a performance.
2. `programme DAY`: the shows of that festival day, with start and end.
   After Hours moves to Friday. Fix the _Known bugs_ of your README.
3. `artist SLUG`: the festival day before each line.
4. `now MOMENT`: the shows on stage at that moment, then the next 3.

## Check

```
$ uv run main.py programme 2027-06-11
Programme for Friday 11 June:
10:30-12:30 | La Cabane | Improv for Beginners (workshop)
15:00-16:30 | Le Kiosque | Writing a Punchline (workshop)
18:00-19:15 | Théâtre des Planches | Nothing Serious (solo)
20:30-21:50 | Grand Casino | Tall Tales (solo)
21:30-22:40 | Théâtre des Planches | Straight Face (solo)
23:30-00:30 | Le Kiosque | Late Laughs (solo)
01:00-02:00 | Le Kiosque | After Hours (lineup)

$ uv run main.py artist max-pellerin
Max Pellerin
Thu 10 20:30-22:30 | Grand Casino | Opening Gala (act)
Fri 11 23:30-00:30 | Le Kiosque | Late Laughs (solo)
Sat 12 21:00-22:40 | Théâtre des Planches | Deauville Comedy Club (host)
Sun 13 20:30-22:40 | Grand Casino | Closing Gala (act)

$ uv run main.py now 2027-06-11T21:00
On stage at 2027-06-11 21:00:
- Tall Tales at Grand Casino, until 21:50
Up next:
- 21:30-22:40 | Théâtre des Planches | Straight Face (solo)
- 23:30-00:30 | Le Kiosque | Late Laughs (solo)
- 01:00-02:00 | Le Kiosque | After Hours (lineup)

$ uv run main.py now 2027-06-12T01:30
On stage at 2027-06-12 01:30:
- After Hours at Le Kiosque, until 02:00
Up next:
- 10:30-12:30 | La Cabane | Stand-up Lab (workshop)
- 11:00-12:00 | Théâtre des Planches | Brunch & Punchlines (solo)
- 15:00-16:30 | Le Kiosque | New Faces (lineup)
```

Try `uv run main.py programme June-11`: a traceback. That is step 05.

## Going further

Practice repository: `B2/examples/04_decorators.ipynb` (`sorted` with
`key=`); exercises `B2/exercises/01_functions/timing.py`.
