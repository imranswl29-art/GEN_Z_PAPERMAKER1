with open("src/data/questionBankStore.ts", "r", encoding="utf-8") as f:
    text = f.read()

# Update existingMCQs
text = text.replace(
    'const existingMCQs=(chapter.mcqs||[]).map((m,i)=>({...m,qNo:allMCQs.length+i+1,chapterRef:chapter.number}));',
    'const existingMCQs=(chapter.mcqs||[]).map((m,i)=>({...m,qNo:allMCQs.length+i+1,chapterRef:chapter.number,category:m.category||"Textbook Exercises"}));'
)

# Update existingShorts
text = text.replace(
    'const existingShorts=(chapter.shortQuestions||[]).map((s,i)=>({...s,subNo:allShorts.length+i+1,chapterRef:chapter.number}));',
    'const existingShorts=(chapter.shortQuestions||[]).map((s,i)=>({...s,subNo:allShorts.length+i+1,chapterRef:chapter.number,category:s.category||"Textbook Exercises"}));'
)

# Update existingLongs
text = text.replace(
    'parts:l.parts||[{partLabel:"a",statementEn:l.statementEn||"",statementUr:l.statementUr||"",marks:5}],chapterRef:`Unit ${chapter.number}`}));',
    'parts:l.parts||[{partLabel:"a",statementEn:l.statementEn||"",statementUr:l.statementUr||"",marks:5}],chapterRef:`Unit ${chapter.number}`,category:l.category||"Past Board Papers"}));'
)

# In curated questions, ensure category is set
text = text.replace(
    'correctOption:"C",chapterRef:chNo}',
    'correctOption:"C",chapterRef:chNo,category:"SLO Conceptual"}'
)

with open("src/data/questionBankStore.ts", "w", encoding="utf-8") as f:
    f.write(text)

print("Updated questionBankStore.ts categories successfully!")
