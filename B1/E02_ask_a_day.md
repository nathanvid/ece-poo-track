# Step 02 - The programme of a day

**At the end:** `uv run main.py` asks for a day and prints its programme,
with the names of the venues.

The first real feature: a festival-goer wants the programme of Friday.

## Learn

- `input("Day (YYYY-MM-DD): ")` waits for the user and returns a `str`.
  `.strip()` removes the spaces around it.
- Ask again until the answer is valid: a `while` loop whose condition is
  "the answer is not one of the possible ones".
- A string has slices: `"2027-06-11T21:30"[:10]` is `"2027-06-11"`,
  `[11:]` is `"21:30"`.
- A dict to find something fast: build `{slug: name}` once, before the loop,
  then `venue_names["le-kiosque"]` gives `"Le Kiosque"`.

On the side: [side/e02_opening_hours.py](side/e02_opening_hours.py) asks a
day until it is valid, then filters a list.

## Do

1. The list of the festival days, found from the data.
2. Ask for a day until it is one of them.
3. Print the performances starting that day: time, venue **name**, title,
   kind.

Performances refer to their venue by a slug, `"theatre-des-planches"`,
built from the name: lower case, dashes instead of spaces. Build it in the
same way from each venue name. `"Théâtre"` will resist: replace its accents
by hand for now (`.replace("é", "e")`). Step 03 does better.

## Check

```
Day (YYYY-MM-DD): June 11
No performance on 'June 11'. Days: 2027-06-10, 2027-06-11, 2027-06-12, 2027-06-13
Day (YYYY-MM-DD): 2027-06-11
Programme for 2027-06-11:
10:30 | La Cabane | Improv for Beginners (workshop)
15:00 | Le Kiosque | Writing a Punchline (workshop)
18:00 | Théâtre des Planches | Nothing Serious (solo)
20:30 | Grand Casino | Tall Tales (solo)
21:30 | Théâtre des Planches | Straight Face (solo)
23:30 | Le Kiosque | Late Laughs (solo)
```

## A bug to keep

Ask for `2027-06-12`. The first line is `01:00 | Le Kiosque | After Hours`.
The festival-goer reads "Saturday 1 am"… but for the festival, a show at 1 am
is the end of **Friday** night. The brief says it: a festival day ends at
06:00.

Comparing the first 10 letters of a string cannot express "before 6 am, it is
still the day before". Write this bug in your README, under _Known bugs_. It
is fixed in step 04, with real dates.

## Going further

Practice repository: `B1/examples/03_strings.ipynb`, `04_input_output.py`;
exercises `B1/exercises/02_conditions`, `05_dicts/programme.py`.
