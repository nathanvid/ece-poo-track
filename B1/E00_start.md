# Step 00 - Start the project

**At the end:** your own repository holds the project, and
`uv run main.py` prints a summary of the festival.

The project is the platform of the Deauville Festival du Rire. The website is
already written; behind it, everything is yours to build, in Python. Today
there is almost nothing: some data and a file of a few lines. Each step adds
one thing that works.

## Get the starter

1. Download the starter (the trainer gives the link): **Code → Download
   ZIP**, unzip it where you keep your projects, outside OneDrive.
2. Open the folder in VS Code, then a terminal (`Terminal > New Terminal`).
3. Turn it into a uv project, then run the given file:

   ```bash
   uv init --no-package
   uv run main.py
   ```

   `uv init` adds `pyproject.toml` (the project card) and `.python-version`.
   It keeps the files already there.

What is in the folder:

| Path                 | What it is                                                         |
| -------------------- | ------------------------------------------------------------------ |
| `README.md`          | the brief: what the platform must do, and every rule. Read it now. |
| `data/festival.json` | the 2027 edition: venues, artists, performances                    |
| `main.py`            | three lines that read the data, one that prints the name           |
| `web/`               | the website and the admin: you will plug them in at step 06        |
| `API.md`             | what the website will ask your program, from step 06               |

## Learn

Open `data/festival.json` in VS Code. JSON is text; `json.load` turns it into
Python values:

| JSON                     | Python | Read it with                 |
| ------------------------ | ------ | ---------------------------- |
| `{"name": "Le Kiosque"}` | `dict` | `venue["name"]`              |
| `[{...}, {...}]`         | `list` | `venues[0]`, `venues[-1]`    |
| `"2027-06-10"`           | `str`  | it is text, not a date (yet) |
| `120`                    | `int`  | `venue["capacity"] + 1`      |

`festival["venues"][0]["name"]`: the festival, its list of venues, the first
one, its name. Read such a line from left to right.

On the side: [side/e00_playlist.py](side/e00_playlist.py) does the same on
a playlist.

```bash
uv run python B1/side/e00_playlist.py      # from the track folder
```

## Do

Complete `main.py` so that it prints exactly:

```
Deauville Festival du Rire 2027
From 2027-06-10 to 2027-06-13
4 venues, 12 artists, 23 performances
```

Every value comes from the data: if a venue is added to the file, the
numbers change without touching the code. `len()` counts the elements of a
list.

## Check

Run `uv run main.py` and compare with the text above, character by character.
Then change `"name"` in the data file, run again, and put it back.

## Going further

Practice repository: `B1/examples/02_variables_types.ipynb`,
`03_strings.ipynb`; exercises `B1/exercises/01_variables_io`.
