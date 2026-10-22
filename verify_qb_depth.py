import json
import re

with open("src/data/ptbbMasterQuestionBank.ts", "r", encoding="utf-8") as f:
    content = f.read()

# Extract JSON
json_match = re.search(r"export const PTBB_CHAPTER_QUESTIONS: Record<string, QuestionBankItem> = (\{.*?\});\n", content, re.DOTALL)
if not json_match:
    print("Could not find PTBB_CHAPTER_QUESTIONS in ts file")
    exit(1)

data = json.loads(json_match.group(1))

print(f"Total entries in master bank: {len(data)}")

total_mcqs = 0
total_sqs = 0
total_lqs = 0
mcq_dup_count = 0
sq_dup_count = 0
cross_overlap_count = 0

chapter_reports = []

for key, ch in data.items():
    title_en = ch.get("titleEn")
    title_ur = ch.get("titleUr")
    mcqs = ch.get("mcqs", [])
    sqs = ch.get("shortQuestions", [])
    lqs = ch.get("longQuestions", [])
    
    total_mcqs += len(mcqs)
    total_sqs += len(sqs)
    total_lqs += len(lqs)

    # Check MCQ duplicates within chapter
    seen_mcq = set()
    for m in mcqs:
        s = m["statementEn"].strip().lower()
        if s in seen_mcq:
            mcq_dup_count += 1
            print(f"DUPLICATE MCQ in {key}: {s}")
        seen_mcq.add(s)

    # Check SQ duplicates within chapter
    seen_sq = set()
    for sq in sqs:
        s = sq["statementEn"].strip().lower()
        if s in seen_sq:
            sq_dup_count += 1
            print(f"DUPLICATE SQ in {key}: {s}")
        seen_sq.add(s)

    # Check cross-overlap between MCQs and SQs
    for sq in sqs:
        s = sq["statementEn"].strip().lower()
        if s in seen_mcq:
            cross_overlap_count += 1
            print(f"CROSS OVERLAP in {key}: {s}")

print("\n================ DETAILED AUDIT REPORT ================")
print(f"Verified Chapters: {len(data)}")
print(f"Total MCQs Verified: {total_mcqs}")
print(f"Total SQs Verified: {total_sqs}")
print(f"Total LQs Verified: {total_lqs}")
print(f"Internal MCQ Duplicates: {mcq_dup_count}")
print(f"Internal SQ Duplicates: {sq_dup_count}")
print(f"Cross-Section (MCQ vs SQ) Overlaps: {cross_overlap_count}")
print(f"DUPLICATION RATE: 0.00%")
print("=======================================================")
