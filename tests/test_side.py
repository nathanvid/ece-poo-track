"""Every side example runs, from the track folder, as the sheets say."""

import importlib.util
import os
import subprocess
import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

TRACK = Path(__file__).parent.parent

# Scripts and what to type for them.
SCRIPTS = {
    "B1/side/e00_playlist.py": "",
    "B1/side/e01_library.py": "",
    "B1/side/e02_opening_hours.py": "sunday\nWednesday\n",
    "B2/side/e03_shopping.py": "",
    "B2/side/e03_slugs.py": "",
    "B2/side/e04_night_buses.py": "",
    "B2/side/e05_room_bookings.py": "",
    "B3/side/e06_temperatures.py": "",
    "B3/side/e06_weather_report.py": "",
    "B3/side/e07_movie.py": "",
    "B3/side/e08_library.py": "",
    "B4/side/e09_messages.py": "",
    "B4/side/e10_bank.py": "",
    "B4/side/e11_storage.py": "",
}


def test_every_script_is_listed():
    found = set()
    for path in TRACK.glob("B*/side/*.py"):
        name = path.name
        if name.startswith("test_") or name.endswith("_api.py"):
            continue
        found.add(path.relative_to(TRACK).as_posix())
    assert found == set(SCRIPTS)


@pytest.mark.parametrize("script", sorted(SCRIPTS))
def test_script_runs(script):
    env = dict(os.environ, PYTHONUTF8="1", PYTHONIOENCODING="utf-8")
    result = subprocess.run(
        [sys.executable, script],
        cwd=TRACK,
        input=SCRIPTS[script],
        capture_output=True,
        text=True,
        encoding="utf-8",
        env=env,
        timeout=20,
    )
    assert result.returncode == 0, result.stderr
    assert result.stdout.strip() != ""


def load(path: str):
    """Import a side module the way uvicorn --app-dir does."""
    folder = str(TRACK / Path(path).parent)
    sys.path.insert(0, folder)
    try:
        spec = importlib.util.spec_from_file_location(Path(path).stem, TRACK / path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    finally:
        sys.path.remove(folder)


def test_quotes_api():
    client = TestClient(load("B3/side/e06_quotes_api.py").app)
    assert len(client.get("/api/quotes").json()) == 3
    assert len(client.get("/api/quotes", params={"author": "Groucho Marx"}).json()) == 2
    assert client.get("/api/quotes/9").status_code == 404
    assert client.get("/api/quotes/abc").status_code == 422


def test_bank_api():
    client = TestClient(load("B4/side/e10_bank_api.py").app)
    assert client.post("/api/accounts", json={"owner": "Lou"}).status_code == 201
    response = client.post("/api/accounts/lou/deposits", json={"amount": 50})
    assert response.json() == {"owner": "Lou", "balance": 50}
    too_much = client.post("/api/accounts/lou/withdrawals", json={"amount": 80})
    assert too_much.status_code == 409
    unknown = client.post("/api/accounts/zoe/deposits", json={"amount": 5})
    assert unknown.status_code == 404
