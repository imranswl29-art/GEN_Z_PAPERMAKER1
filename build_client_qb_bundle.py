import json
import re

with open("src/data/ptbbMasterQuestionBank.ts", "r", encoding="utf-8") as f:
    text = f.read()

m = re.search(r"export const PTBB_CHAPTER_QUESTIONS: Record<string, QuestionBankItem> = (\{.*?\});\n", text, re.DOTALL)
if not m:
    print("Could not find PTBB_CHAPTER_QUESTIONS")
    exit(1)

data = json.loads(m.group(1))

# Write out ptbb-master-qb.js
min_json = json.dumps(data, ensure_ascii=False, separators=(",", ":"))

js_content = f"window.__PTBB_MASTER_QB__ = {min_json};\n"

with open("assets/ptbb-master-qb.js", "w", encoding="utf-8") as f:
    f.write(js_content)

print(f"Generated assets/ptbb-master-qb.js with {len(data)} chapters successfully.")
