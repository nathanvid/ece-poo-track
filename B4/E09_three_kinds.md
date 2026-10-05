# Step 09 - Three kinds of performances

**At the end:** solo shows, lineups and workshops are three classes of one
family; each one checks its own rules and writes its own summary. The word
`kind` appears in one place: where the file is read.

Count the `if ... kind == ...` in your code: the artists of a performance,
its summary, its view, its capacity, its fields in the file… Every new kind
of performance would mean visiting all of them. And the rules of the brief
for each kind (_Three kinds of performances_) are not checked yet.

## Learn

- **Inheritance**: `class Lineup(Performance):` gets everything of
  `Performance`, and adds or replaces. `super().__init__(...)` runs the
  common part.
- **Polymorphism**: `performance.summary()` runs the method of the object's
  own class. The caller never asks which kind it is.
- **Abstract class**: `class Performance(ABC)` with `@abstractmethod`: every
  subclass must write that method, and a bare `Performance` cannot be created.
- A **class attribute** (`kind = "lineup"`) is shared by every object of the
  class.
- From the file: the `"kind"` field chooses the class, once, in the loader
  (a dict `{"solo": SoloShow, ...}` does it without `if`).

On the side: [side/e09_messages.py](side/e09_messages.py), emails, SMS and
letters with an abstract cost.

## Do

1. A base class for what every performance shares, and one subclass per
   kind. Decide what is common and what is not: start, end and festival day
   are common; who is on stage and the summary are not.
2. The rules of each kind, from the brief: minimum age 0 to 18; lineup with at
   least 2 acts, each once, a host who is not an act, 10 minutes per act and
   3 for the host between two acts; workshop with at least 1 place, places =
   `min(max_participants, venue seats)`.
3. The views of `API.md`: common fields in the base class, each subclass adds
   its own (`artist` and `min_age`, `host` and `acts`, `teacher`,
   `max_participants`, `participants` and `places_left`).
4. Tests for each new rule. Your tests of step 08 still pass.

## Check

| Check                                               | Expected                                                 |
| --------------------------------------------------- | -------------------------------------------------------- |
| `summary` of `le-kiosque-2027-06-12-0100`           | `hosted by Tom Vasseur, with Hugo Lemaire, Maya Choukri` |
| `summary` of `la-cabane-2027-06-11-1030`            | `with Inès Moreau, 3/12 places taken`                    |
| `summary` of `grand-casino-2027-06-11-2030`         | `Léa Fontaine`                                           |
| a lineup of 3 acts in 35 minutes, in a test         | refused; in 36 minutes, accepted                         |
| a workshop of 999 places at Grand Casino, in a test | 650 places                                               |
| a `Performance` created directly                    | `TypeError`                                              |
| search `kind ==` in your code                       | only in the loader, if anywhere                          |
| the website                                         | badges `16+` and "place(s) left" on the cards            |

## Going further

Practice repository: `B4/examples/02_inheritance.ipynb`,
`03_abstract_classes.ipynb`; exercises `B4/exercises/02_inheritance`,
`03_abstract_classes`.
