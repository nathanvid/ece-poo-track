# Step 00, on the side: read a JSON file and print a few values.
# Run from the track folder: uv run python B1/side/e00_playlist.py

import json

# "open the file, give it to json.load": you get Python dicts and lists.
with open("B1/side/playlist.json", encoding="utf-8") as file:
    playlist = json.load(file)

print(type(playlist))  # a dict: keys "name", "owner", "songs"
print(playlist["name"])  # a value, found by its key
print(f"By {playlist['owner']}")  # inside an f-string: other quotes

songs = playlist["songs"]  # a list of dicts
print(f"{len(songs)} songs")
print(f"First: {songs[0]['title']}")  # first element, then its key
print(f"Last: {songs[-1]['title']} by {songs[-1]['artist']}")
