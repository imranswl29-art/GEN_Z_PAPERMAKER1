with open("src/data/massiveQuestionBankEngine.ts", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "<a href" in line:
        print(f"Found on line {i+1}: {line}")
        lines[i] = "          { en: \"<a href='...'>\", ur: \"<a href='...'>\" },\n"

with open("src/data/massiveQuestionBankEngine.ts", "w", encoding="utf-8") as f:
    f.writelines(lines)

print("Updated line successfully!")
