"""Step 11, on the side: an interface, two storages, code that works with both.

uv run python B4/side/e11_storage.py
"""

import json
from abc import ABC, abstractmethod
from pathlib import Path


class NotesStorage(ABC):
    """Where the notes live. The rest of the program only knows this."""

    @abstractmethod
    def load(self) -> list[str]: ...

    @abstractmethod
    def save(self, notes: list[str]) -> None: ...


class JsonStorage(NotesStorage):
    def __init__(self, path: Path) -> None:
        self.path = path

    def load(self) -> list[str]:
        if not self.path.exists():
            return []
        return json.loads(self.path.read_text(encoding="utf-8"))

    def save(self, notes: list[str]) -> None:
        self.path.parent.mkdir(exist_ok=True)
        self.path.write_text(json.dumps(notes, ensure_ascii=False), encoding="utf-8")


class MemoryStorage(NotesStorage):
    """Nothing on disk: handy for tests."""

    def __init__(self) -> None:
        self._notes: list[str] = []

    def load(self) -> list[str]:
        return list(self._notes)

    def save(self, notes: list[str]) -> None:
        self._notes = list(notes)


def add_note(storage: NotesStorage, note: str) -> int:
    """Works with any storage: it only calls load and save."""
    notes = storage.load()
    notes.append(note)
    storage.save(notes)
    return len(notes)


if __name__ == "__main__":
    for storage in [JsonStorage(Path("B4/side/output/notes.json")), MemoryStorage()]:
        count = add_note(storage, "buy bread")
        print(f"{type(storage).__name__}: {count} note(s)")
