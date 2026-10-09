with open('server.ts', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Upgrade dedupeQuestions in server.ts
old_dedupe = '''function dedupeQuestions(paper){const seenStatements=new Set;if(paper.objectiveSection?.questions){paper.objectiveSection.questions=paper.objectiveSection.questions.filter(q=>{const key=(q.statementEn||q.statementUr||"").trim().toLowerCase();if(!key||seenStatements.has(key))return false;seenStatements.add(key);return true});paper.objectiveSection.questions.forEach((q,idx)=>{q.qNo=idx+1});paper.objectiveSection.totalMarks=paper.objectiveSection.questions.length}if(paper.subjectiveSection?.part1_shortQuestions){paper.subjectiveSection.part1_shortQuestions.forEach(grp=>{if(grp.questions){grp.questions=grp.questions.filter(q=>{const key=(q.statementEn||q.statementUr||"").trim().toLowerCase();if(!key||seenStatements.has(key))return false;seenStatements.add(key);return true});grp.questions.forEach((q,idx)=>{q.subNo=idx+1})}})}return paper}'''

new_dedupe = '''function dedupeQuestions(paper){
  const normalizeKey = (s) => (s || "").replace(/[^a-zA-Z0-9\u0600-\u06FF]/g, "").toLowerCase().trim();
  const seenKeys = new Set();

  // Deduplicate Section-A Objective (MCQs)
  if (paper.objectiveSection?.questions) {
    paper.objectiveSection.questions = paper.objectiveSection.questions.filter(q => {
      const enKey = normalizeKey(q.statementEn);
      const urKey = normalizeKey(q.statementUr);
      const key = enKey || urKey;
      if (!key || seenKeys.has(key)) return false;
      if (enKey) seenKeys.add(enKey);
      if (urKey) seenKeys.add(urKey);
      return true;
    });
    paper.objectiveSection.questions.forEach((q, idx) => { q.qNo = idx + 1; });
    paper.objectiveSection.totalMarks = paper.objectiveSection.questions.length;
  }

  // Deduplicate Section-B Part-1 Short Questions across all groups & against MCQs
  if (paper.subjectiveSection?.part1_shortQuestions) {
    paper.subjectiveSection.part1_shortQuestions.forEach(grp => {
      if (grp.questions) {
        grp.questions = grp.questions.filter(q => {
          const enKey = normalizeKey(q.statementEn);
          const urKey = normalizeKey(q.statementUr);
          const key = enKey || urKey;
          if (!key || seenKeys.has(key)) return false;
          if (enKey) seenKeys.add(enKey);
          if (urKey) seenKeys.add(urKey);
          return true;
        });
        grp.questions.forEach((q, idx) => { q.subNo = idx + 1; });
      }
    });
  }

  // Deduplicate Section-C Part-2 Long Questions against MCQs, Short Questions, and each other
  if (paper.subjectiveSection?.part2_longQuestions?.questions) {
    paper.subjectiveSection.part2_longQuestions.questions = paper.subjectiveSection.part2_longQuestions.questions.filter(lq => {
      const parts = lq.parts || [];
      const partStatements = parts.map(p => (p.statementEn || "") + " " + (p.statementUr || "")).join(" ");
      const mainStatement = (lq.statementEn || "") + " " + (lq.statementUr || "") + " " + partStatements;
      const key = normalizeKey(mainStatement);
      if (!key || seenKeys.has(key)) return false;
      seenKeys.add(key);
      parts.forEach(p => {
        const pEn = normalizeKey(p.statementEn);
        const pUr = normalizeKey(p.statementUr);
        if (pEn) seenKeys.add(pEn);
        if (pUr) seenKeys.add(pUr);
      });
      return true;
    });
    paper.subjectiveSection.part2_longQuestions.questions.forEach((lq, idx) => {
      lq.qNo = idx + 5;
    });
  }

  return paper;
}'''

if old_dedupe in text:
    text = text.replace(old_dedupe, new_dedupe, 1)
    print("  [✓] Updated dedupeQuestions with full cross-section deduplication")
else:
    print("  [!] old_dedupe not found directly, looking for pos...")
    pos = text.find('function dedupeQuestions(')
    end = text.find('__name(dedupeQuestions', pos)
    if pos != -1 and end != -1:
        text = text[:pos] + new_dedupe + '\n' + text[end:]
        print("  [✓] Replaced dedupeQuestions by slice")

with open('server.ts', 'w', encoding='utf-8') as f:
    f.write(text)

print("Saved updated server.ts")
