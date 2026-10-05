# Step 02, on the side: ask until the answer is valid, then filter.
# Run from the track folder: uv run python B1/side/e02_opening_hours.py

opening = [
    {"day": "monday", "from": "14:00", "to": "18:00"},
    {"day": "wednesday", "from": "10:00", "to": "12:30"},
    {"day": "wednesday", "from": "14:00", "to": "19:00"},
    {"day": "saturday", "from": "10:00", "to": "17:00"},
]

# The possible answers, built from the data (no duplicates).
days = []
for slot in opening:
    if slot["day"] not in days:
        days.append(slot["day"])

# .strip() removes spaces, .lower() accepts "Wednesday".
day = input("Which day? ").strip().lower()
while day not in days:
    print(f"Closed on {day!r}. Open on: {', '.join(days)}")
    day = input("Which day? ").strip().lower()

print(f"Open on {day}:")
for slot in opening:
    if slot["day"] == day:
        print(f"{slot['from']} - {slot['to']}")

# Strings compare letter by letter: "09:30" < "10:00" works because
# both have the same shape. "9:30" < "10:00" would be False.
print("09:30" < "10:00", "9:30" < "10:00")
