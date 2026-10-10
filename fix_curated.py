with open("src/data/questionBankStore.ts", "r", encoding="utf-8") as f:
    text = f.read()

import re

# Ensure all questions returned by generateCuratedQuestionsForChapter have category
# In curated:
# mcqs: map each to have category: m.category || "SLO Conceptual"
# shortQuestions: map each to have category: s.category || "In-Text & Box Questions"
# longQuestions: map each to have category: l.category || "Past Board Papers"

text = text.replace(
    'return{mcqs,shortQuestions,longQuestions}',
    'return{mcqs:mcqs.map(m=>({...m,category:m.category||"SLO Conceptual"})),shortQuestions:shortQuestions.map(s=>({...s,category:s.category||"In-Text & Box Questions"})),longQuestions:longQuestions.map(l=>({...l,category:l.category||"Past Board Papers"}))}'
)

with open("src/data/questionBankStore.ts", "w", encoding="utf-8") as f:
    f.write(text)

print("Fixed curated categories!")
