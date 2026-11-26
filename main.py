import os

# The printer speaks for itself: an error code, a quit, and an exact
# sheet count — weary, literal, and faintly passive-aggressive.
LINE = "ERROR E-47: I didn't jam, I quit — after 12,438 pages, one thump, and zero thank-yous, your report lives in me now."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
