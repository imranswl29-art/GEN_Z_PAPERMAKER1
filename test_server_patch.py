import subprocess, re

with open("server.ts", "r") as f:
    text = f.read()

# 1. Update CANDIDATE_MODELS
old_cand = 'CANDIDATE_MODELS=["gemini-2.5-flash","gemini-2.5-flash-lite","gemini-flash-latest","gemini-3.1-flash-lite"];'
new_cand = 'CANDIDATE_MODELS=["gemini-3.8-flash","gemini-flash-latest","gemini-3.1-flash-lite","gemini-2.5-flash"];'
assert old_cand in text, "old_cand not found"
text = text.replace(old_cand, new_cand, 1)

print("[✓] CANDIDATE_MODELS updated")
