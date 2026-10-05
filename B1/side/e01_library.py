# Step 01, on the side: loops, conditions, counting with a dict.
# Run from the track folder: uv run python B1/side/e01_library.py

import json

with open("B1/side/library.json", encoding="utf-8") as file:
    library = json.load(file)

books = library["books"]

# Loop over a list of dicts, add up a value (an "accumulator").
total_pages = 0
for book in books:
    print(f"- {book['title']} ({book['pages']} pages)")
    total_pages += book["pages"]
print(f"Total: {total_pages} pages")

# Keep only some of them: a condition inside the loop.
print("Available:")
for book in books:
    if book["borrowed_by"] == "":
        print(f"- {book['title']}")

# Count by genre: a dict whose keys appear while looping.
genres = {}
for book in books:
    genre = book["genre"]
    if genre in genres:
        genres[genre] += 1
    else:
        genres[genre] = 1
print(genres)

# The biggest one: keep the best so far, compare each book to it.
thickest = books[0]
for book in books:
    if book["pages"] > thickest["pages"]:
        thickest = book
print(f"Thickest: {thickest['title']}")
