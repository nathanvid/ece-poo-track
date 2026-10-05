# Step 07 - The programme, and the first classes

**At the end:** the programme of each day appears on the website, and an
artist's page lists their shows. Venues, artists and performances are
objects of your own classes.

`/api/programme` must send, for each performance, its `end`, its
`festival_day`, its `venue_name`, its `id`, the list of its `artists` with
their names… (see _Performance_ in `API.md`). With dicts, each value is one
more function call, in the route **and** in the command line: the same
computation in two places, which will differ one day. Data and what is
computed from it belong together: that is a class.

## Learn

- `class`, `__init__`, `self`: each object holds its own attributes.
- `@property`: `performance.end` reads like an attribute, computed each time.
- Methods: `performance.involves(artist)`, `performance.to_view()`.
- `@dataclass` writes `__init__` for classes that are mostly data;
  `__post_init__` checks the values.
- Building objects from the file: one function reads the JSON and returns
  objects. After it, nobody touches the dicts of the file any more.

On the side: [side/e07_movie.py](side/e07_movie.py): screenings and cinemas,
with a property, a check in `__init__`, a view for an API, a dataclass.

## Do

1. Decide which classes you need for the data of the file, and what each one
   computes. Write it in your README before the code: a few lines per class.
2. Load the file into objects. The command line and the API both use them.
   The outputs of step 05 do not change.
3. Routes: `GET /api/programme` (filters `?day=` and `?venue=`),
   `GET /api/performances/{id}`, `GET /api/artists/{slug}` with its
   `performances`. Unknown slug or id: `404` with `{"detail": "a sentence"}`
   (`raise HTTPException(status_code=404, detail=...)`). Type the parameter
   `day: date | None = None`: FastAPI refuses `?day=June 11` with a `422` by
   itself.
4. The three kinds of performances do not have the same fields: a single
   class with some `None` fields will do for now. Notice every
   `if self.kind == ...` you write. Step 09 is about them.

## Check

| Open                                                  | You see                                             |
| ----------------------------------------------------- | --------------------------------------------------- |
| <http://127.0.0.1:8000/>                              | the cards of Thursday; Friday ends with After Hours |
| <http://127.0.0.1:8000/artist.html?slug=max-pellerin> | four shows, from Opening Gala to Closing Gala       |
| `/api/programme?venue=le-kiosque`                     | 7 performances                                      |
| `/api/programme?venue=nowhere`                        | `404`, `{"detail": "No venue 'nowhere'."}`          |
| `/api/performances/le-kiosque-2027-06-12-0100`        | below                                               |

```json
{
  "id": "le-kiosque-2027-06-12-0100",
  "kind": "lineup",
  "title": "After Hours",
  "venue": "le-kiosque",
  "venue_name": "Le Kiosque",
  "start": "2027-06-12T01:00",
  "end": "2027-06-12T02:00",
  "duration_minutes": 60,
  "festival_day": "2027-06-11",
  "description": "The last show of Friday night, after midnight.",
  "summary": "hosted by Tom Vasseur, with Hugo Lemaire, Maya Choukri",
  "capacity": 120,
  "host": "tom-vasseur",
  "acts": ["hugo-lemaire", "maya-choukri"],
  "artists": [
    { "slug": "tom-vasseur", "name": "Tom Vasseur" },
    { "slug": "hugo-lemaire", "name": "Hugo Lemaire" },
    { "slug": "maya-choukri", "name": "Maya Choukri" }
  ]
}
```

The order of the keys does not matter; the names and values do. A workshop
adds `teacher`, `max_participants`, `participants` and `places_left`
(`la-cabane-2027-06-11-1030`: 9 places left); a solo show adds `artist` and
`min_age`.

## Going further

Practice repository: `B3/examples/01_objects.ipynb` to
`04_dataclass_property.ipynb`; exercises `B3/exercises/02_classes`,
`04_dataclass_property`.
