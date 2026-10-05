"""Step 12, on the side: testing an API without starting a server.

uv run pytest B5/side -v
"""

import json

import pytest
from e12_notes_api import create_app
from fastapi.testclient import TestClient


# tmp_path: a new empty folder for each test, deleted afterwards. The real
# notes.json is never touched, and no test depends on another.
@pytest.fixture
def notes_file(tmp_path):
    path = tmp_path / "notes.json"
    path.write_text(json.dumps(["buy bread"]), encoding="utf-8")
    return path


@pytest.fixture
def client(notes_file):
    return TestClient(create_app(notes_file))


def test_list(client):
    response = client.get("/api/notes")
    assert response.status_code == 200
    assert response.json() == ["buy bread"]


def test_add_is_saved(client, notes_file):
    response = client.post("/api/notes", json={"text": "  call Lou "})
    assert response.status_code == 201
    assert response.json() == {"id": 1, "text": "call Lou"}
    assert json.loads(notes_file.read_text(encoding="utf-8"))[-1] == "call Lou"


def test_errors(client):
    assert client.post("/api/notes", json={"text": " "}).status_code == 422
    assert client.post("/api/notes", json={"words": "x"}).status_code == 422
    response = client.delete("/api/notes/7")
    assert response.status_code == 404
    assert response.json() == {"detail": "No note 7."}


def test_delete(client):
    assert client.delete("/api/notes/0").status_code == 204
    assert client.get("/api/notes").json() == []
