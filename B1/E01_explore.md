# Step 01 - Explore the data

**At the end:** `uv run main.py` answers six questions about the festival,
computed from the data.

Before building anything, look at what the data holds. Each question below is
a loop over a list, sometimes with a condition, sometimes counting.

## Learn

| You want                      | Pattern                                            |
| ----------------------------- | -------------------------------------------------- |
| do something for each element | `for venue in festival["venues"]:`                 |
| keep only some elements       | an `if` inside the loop                            |
| a total                       | `total = 0` before the loop, `total += ...` inside |
| count by category             | a dict: `counts[key] = counts.get(key, 0) + 1`     |
| the biggest                   | keep the best so far, compare each element to it   |

On the side: [side/e01_library.py](side/e01_library.py) uses each pattern on
the books of a library.

## Do

Add to `main.py`, after the summary of step 00. The expected output is
below: same numbers, same order. The layout may differ a little.

1. Each venue with its seats and address, then the total number of seats.
2. The number of performances of each kind (`"kind"` in the data).
3. The performances at Le Kiosque, with their start. Look at what
   `"venue"` holds in a performance: it is not the name.
4. The longest performance.
5. For each workshop: its day, and how many people are registered out of
   the places (`"participants"`, `"max_participants"`).
6. `[ext.]` The artists on stage the most often. Careful: an artist can be the
   `"artist"` of a solo, the `"host"` or one of the `"acts"` of a lineup, or
   the `"teacher"` of a workshop. Several artists may share the first place.

## Check

```
Venues:
- Grand Casino: 650 seats (Seafront, main hall)
- Théâtre des Planches: 320 seats (Town centre)
- Le Kiosque: 120 seats (Beach promenade)
- La Cabane: 40 seats (Beach, next to the lifeguard post)
Total: 1130 seats

lineup: 6
solo: 13
workshop: 4

At Le Kiosque:
- 2027-06-10T22:30 Open Mic Night
- 2027-06-11T15:00 Writing a Punchline
- 2027-06-11T23:30 Late Laughs
- 2027-06-12T01:00 After Hours
- 2027-06-12T15:00 New Faces
- 2027-06-12T23:30 Midnight Snack
- 2027-06-13T15:00 First Time Here

Longest: Closing Gala (130 min)

Improv for Beginners on 2027-06-11: 3/12 registered
Writing a Punchline on 2027-06-11: 1/20 registered
Stand-up Lab on 2027-06-12: 4/10 registered
Improv for Beginners on 2027-06-13: 0/12 registered

On stage 4 times: nora-lebrun, max-pellerin, lea-fontaine, karim-benali, hugo-lemaire, maya-choukri, ines-moreau
```

## Commit

Not yet: Git comes in step 03. Keep a copy of your folder if you are worried.

## Going further

Practice repository: `B1/examples/05_conditions.ipynb` to `08_dicts.ipynb`;
exercises `B1/exercises/03_loops`, `04_lists`, `05_dicts`.
