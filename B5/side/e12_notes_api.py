"""Step 12, on the side: an application built by a function, so tests can
give it their own data file.

    uv run uvicorn e12_notes_api:app --reload --app-dir B5/side
    uv run pytest B5/side -v
"""

import json
from pathlib import Path

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class NoteIn(BaseModel):
    text: str


def create_app(path: Path) -> FastAPI:
    """A new application around the notes stored in `path`."""
    app = FastAPI(title="Notes")

    def load() -> list[str]:
        if not path.exists():
            return []
        return json.loads(path.read_text(encoding="utf-8"))

    def save(notes: list[str]) -> None:
        path.write_text(json.dumps(notes, ensure_ascii=False), encoding="utf-8")

    # The routes are defined inside create_app: they use its `path`.
    @app.get("/api/notes")
    def list_notes() -> list[str]:
        return load()

    @app.post("/api/notes", status_code=201)
    def add_note(body: NoteIn) -> dict:
        if body.text.strip() == "":
            raise HTTPException(status_code=422, detail="A note needs a text.")
        notes = load()
        notes.append(body.text.strip())
        save(notes)
        return {"id": len(notes) - 1, "text": notes[-1]}

    @app.delete("/api/notes/{note_id}", status_code=204)
    def delete_note(note_id: int) -> None:
        notes = load()
        if not 0 <= note_id < len(notes):
            raise HTTPException(status_code=404, detail=f"No note {note_id}.")
        notes.pop(note_id)
        save(notes)

    return app


# For uvicorn: the real file. The tests never use it.
app = create_app(Path("B5/side/notes.json"))
