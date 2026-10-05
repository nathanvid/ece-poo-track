"""Step 05, on the side: rules that raise errors, a caller that explains them,
and a JSON file written back.

    uv run python B2/side/e05_room_bookings.py
"""

import json
from pathlib import Path

OUTPUT = Path("B2/side/output/bookings.json")


def check_booking(bookings: list[dict], new: dict) -> None:
    """Raise ValueError, with a sentence for the user, if `new` breaks a rule."""
    if new["people"] < 1:
        raise ValueError("A booking needs at least one person.")
    if not 8 <= new["start_hour"] < 20:
        raise ValueError(f"The rooms open from 8 to 20, not at {new['start_hour']}.")
    for other in bookings:
        same_room = other["room"] == new["room"]
        if same_room and other["start_hour"] == new["start_hour"]:
            raise ValueError(
                f"{new['room']} is already booked at {new['start_hour']} by "
                f"{other['name']}."
            )


def book(bookings: list[dict], new: dict) -> None:
    check_booking(bookings, new)  # if it raises, the next line never runs
    bookings.append(new)


def load(path: Path) -> list[dict]:
    """Raise ValueError with a clear message instead of a traceback."""
    try:
        with open(path, encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []  # no file yet: no booking yet
    except json.JSONDecodeError as error:
        raise ValueError(f"{path} is damaged (line {error.lineno}).") from None


def save(bookings: list[dict], path: Path) -> None:
    path.parent.mkdir(exist_ok=True)
    with open(path, "w", encoding="utf-8") as file:
        # ensure_ascii=False keeps "é" readable, indent=2 keeps the file readable.
        json.dump(bookings, file, ensure_ascii=False, indent=2)


def main() -> None:
    bookings = []
    wishes = [
        {"name": "Lou", "room": "Salle Verte", "start_hour": 10, "people": 4},
        {"name": "Yanis", "room": "Salle Verte", "start_hour": 10, "people": 2},
        {"name": "Zoé", "room": "Salle Bleue", "start_hour": 22, "people": 3},
        {"name": "Inès", "room": "Salle Bleue", "start_hour": 9, "people": 6},
    ]
    for wish in wishes:
        try:
            book(bookings, wish)
            print(f"OK for {wish['name']}")
        except ValueError as error:
            print(f"Refused for {wish['name']}: {error}")

    save(bookings, OUTPUT)
    print(f"{len(load(OUTPUT))} bookings saved in {OUTPUT}")

    # A damaged file gives a sentence, not a traceback.
    OUTPUT.write_text("[{", encoding="utf-8")
    try:
        load(OUTPUT)
    except ValueError as error:
        print(f"Error: {error}")


main()
