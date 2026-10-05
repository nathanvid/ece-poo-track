# Step 04, on the side: dates, times, durations, and a day that ends at 4 am.
# Run from the track folder: uv run python B2/side/e04_night_buses.py

from datetime import date, datetime, timedelta

# A night bus company: its "service day" ends at 04:00, so the 01:15 bus on
# Saturday is the last bus of the Friday service.
SERVICE_DAY_CHANGE = timedelta(hours=4)

departures = [
    {"line": "N1", "start": "2027-03-05T22:40", "minutes": 35},
    {"line": "N2", "start": "2027-03-05T23:50", "minutes": 50},
    {"line": "N1", "start": "2027-03-06T01:15", "minutes": 35},
    {"line": "N2", "start": "2027-03-06T06:10", "minutes": 50},
]

# Text -> datetime, and back with a format.
first = datetime.fromisoformat(departures[0]["start"])
print(first.year, first.hour, first.minute)
print(f"{first:%A %d %B, %H:%M}")  # Friday 05 March, 22:40

# datetime + timedelta = datetime. The day changes by itself after midnight.
arrival = datetime.fromisoformat(departures[1]["start"]) + timedelta(minutes=50)
print(f"N2 arrives at {arrival:%Y-%m-%d %H:%M}")


def service_day(departure: dict) -> date:
    """Move back 4 hours, then keep the date: 01:15 on Saturday -> Friday."""
    start = datetime.fromisoformat(departure["start"])
    return (start - SERVICE_DAY_CHANGE).date()


friday = date(2027, 3, 5)
print("Friday service:")
for departure in departures:
    if service_day(departure) == friday:
        print(f"- {departure['line']} at {departure['start'][11:]}")

# Comparing datetimes: "is it running at that moment?"
at = datetime(2027, 3, 6, 1, 30)
for departure in departures:
    start = datetime.fromisoformat(departure["start"])
    end = start + timedelta(minutes=departure["minutes"])
    if start <= at < end:
        print(f"At {at:%H:%M}, {departure['line']} is on the road until {end:%H:%M}")

# Sorting by a computed value: key= gives, for each element, what to compare.
latest_first = sorted(departures, key=lambda d: d["start"], reverse=True)
print(latest_first[0]["start"])
