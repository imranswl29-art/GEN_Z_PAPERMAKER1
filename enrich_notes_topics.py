import json, os, glob

print("Checking notes directory...")
files = glob.glob('src/data/notes/*/*/*.json')
print(f"Found {len(files)} notes files to enrich.")
