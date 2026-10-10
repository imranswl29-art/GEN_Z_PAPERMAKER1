import os
import json
import re

# Directory structure setup
BASE_DIR = "src/data/notes"
os.makedirs(BASE_DIR, exist_ok=True)

# Let's inspect ptbbData.ts to extract subject and chapter information accurately
with open("src/data/ptbbData.ts", "r", encoding="utf-8") as f:
    ptbb_content = f.read()

print("Successfully loaded ptbbData.ts, length:", len(ptbb_content))
