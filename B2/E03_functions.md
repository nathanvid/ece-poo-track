# Step 03 - Functions and commands

**At the end:** `main.py` is made of functions, answers several commands
typed in the terminal, and lives on GitHub.

`main.py` is a long list of instructions. To add a feature you scroll, to
reuse a piece you copy it. And the venue slug of step 02 is computed in a
loop where nobody can find it again. Each job becomes a function with a name.

## Learn

- `def name(parameters) -> type:` then `return`. A function that **returns**
  can be reused anywhere; a function that **prints** only serves the
  terminal. Keep the printing at the end of the chain.
- `sys.argv` holds the words typed after the file name:
  `uv run main.py programme 2027-06-11` gives
  `["main.py", "programme", "2027-06-11"]`.
- A real slug removes accents: `unicodedata.normalize("NFKD", text)` splits
  `"é"` into `"e"` + accent, `.encode("ascii", "ignore")` drops the accent.
- Git: a commit is a saved version of the whole folder, with a message. See
  `B2/git.md` in the practice repository to create the GitHub repository.

On the side: [side/e03_shopping.py](side/e03_shopping.py) (functions and
commands), [side/e03_slugs.py](side/e03_slugs.py) (accents, step by step).

## Do

1. A function that turns any name into its slug:
   `"Théâtre des Planches"` → `"theatre-des-planches"`,
   `"Élodie  Marchal !"` → `"elodie-marchal"`. The hand-made replacements of
   step 02 disappear.
2. Rewrite what exists as functions: reading the file, finding a venue or an
   artist from its slug, the programme of a day…
3. Commands:

   | Command                               | Prints                                        |
   | ------------------------------------- | --------------------------------------------- |
   | `uv run main.py`                      | the summary of step 00                        |
   | `uv run main.py venues`               | each venue with its slug and seats, the total |
   | `uv run main.py programme 2027-06-11` | the programme of the day                      |
   | `uv run main.py artist max-pellerin`  | the performances of an artist, with the role  |
   | anything else                         | how to use the program                        |

   The role is `solo`, `host`, `act` or `teacher`. The questions of step 01
   can stay as commands of their own, or go: your choice.

4. `git init`, a `.gitignore` (the starter has one), a first commit, then the
   repository on GitHub. From now on: one commit each time something new
   works.

## Check

```
$ uv run main.py venues
grand-casino: Grand Casino, 650 seats
theatre-des-planches: Théâtre des Planches, 320 seats
le-kiosque: Le Kiosque, 120 seats
la-cabane: La Cabane, 40 seats
Total: 1130 seats

$ uv run main.py artist max-pellerin
Max Pellerin
2027-06-10 20:30 | Grand Casino | Opening Gala (act)
2027-06-11 23:30 | Le Kiosque | Late Laughs (solo)
2027-06-12 21:00 | Théâtre des Planches | Deauville Comedy Club (host)
2027-06-13 20:30 | Grand Casino | Closing Gala (act)

$ uv run main.py artist nobody
No artist 'nobody'.
```

`programme 2027-06-11` prints the same lines as in step 02. The bug of
After Hours is still there.

## Going further

Practice repository: `B2/examples/01_functions.ipynb`, `05_libraries.ipynb`,
`git.md`; exercises `B2/exercises/01_functions`.
