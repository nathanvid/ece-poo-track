# Step 06, on the side: using the functions of another file of the folder.
# Run from the track folder: uv run python B3/side/e06_weather_report.py

from e06_temperatures import to_fahrenheit, warmest

readings = {"Brest": 14.5, "Lille": 11.0, "Nice": 22.0}

for city, celsius in readings.items():
    print(f"{city}: {celsius} °C = {to_fahrenheit(celsius):.1f} °F")
print(f"Warmest: {warmest(readings)}")
