# Step 03, on the side: removing accents, one character at a time.
# Run from the track folder: uv run python B2/side/e03_slugs.py

import unicodedata

word = "Crème brûlée"

# NFKD splits "è" into "e" + a separate accent mark.
decomposed = unicodedata.normalize("NFKD", word)
print(len(word), len(decomposed))  # 12 15: three accents became characters

# Encoding to ASCII with "ignore" drops what ASCII cannot hold: the accents.
plain = decomposed.encode("ascii", "ignore").decode("ascii")
print(plain)  # Creme brulee

# Then keep letters and digits, and put one dash for anything else.
result = ""
for char in plain.lower():
    if char.isalnum():
        result += char
    elif not result.endswith("-"):
        result += "-"
print(result)  # creme-brulee
