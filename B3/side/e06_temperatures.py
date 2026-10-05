"""Step 06, on the side: a module, imported by another file.

uv run python B3/side/e06_temperatures.py     runs the demo below
uv run python B3/side/e06_weather_report.py   imports this file, no demo
"""


def to_fahrenheit(celsius: float) -> float:
    return celsius * 9 / 5 + 32


def warmest(readings: dict[str, float]) -> str:
    """The city with the highest temperature."""
    best = ""
    for city, celsius in readings.items():
        if best == "" or celsius > readings[best]:
            best = city
    return best


# __name__ is "__main__" only when this file is the one that was run.
# When another file imports it, this block is skipped.
if __name__ == "__main__":
    print(to_fahrenheit(20))
    print(warmest({"Brest": 14.5, "Nice": 22.0}))
