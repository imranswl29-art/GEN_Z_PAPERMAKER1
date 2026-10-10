with open("server.ts", "r", encoding="utf-8") as f:
    text = f.read()

target = 'const fallbackMCQs=[1,2,3,4,5].map(i=>({statementEn:`[BISE Board Past Paper] High-yield conceptual question on ${req.body?.chapterTitle||"curriculum"} (Variant ${i}):`,statementUr:`[\\u0628\\u0648\\u0631\\u0688 \\u0633\\u0627\\u0628\\u0642\\u06C1 \\u067E\\u0631\\u0686\\u06C1] ${req.body?.chapterTitle||"\\u0646\\u0635\\u0627\\u0628"} \\u0633\\u06D2 \\u0645\\u062A\\u0639\\u0644\\u0642 \\u0627\\u06C1\\u0645 \\u062A\\u0635\\u0648\\u0651\\u0631\\u0627\\u062A\\u06CC \\u0633\\u0648\\u0627\\u0644 (\\u0648\\u0631\\u0698\\u0646 ${i}):`,options:[{key:"A",textEn:"Standard Board Definition A",textUr:"\\u0645\\u0639\\u06CC\\u0627\\u0631\\u06CC \\u0628\\u0648\\u0631\\u0688 \\u062A\\u0639\\u0631\\u06CC\\u0641 (\\u0627\\u0644\\u0641)"},{key:"B",textEn:"Primary Law Principle B",textUr:"\\u0628\\u0646\\u06CC\\u0627\\u062F\\u06CC \\u0633\\u0627\\u0626\\u0646\\u0633\\u06CC \\u0627\\u0635\\u0648\\u0644 (\\u0628)"},{key:"C",textEn:"Experimental Conclusion C",textUr:"\\u062A\\u062C\\u0631\\u0628\\u0627\\u062A\\u06CC \\u0646\\u062A\\u06CC\\u062C\\u06C1 (\\u062C)"},{key:"D",textEn:"Applied Modern Formula D",textUr:"\\u0627\\u0637\\u0644\\u0627\\u0642\\u06CC \\u06A9\\u0644\\u06CC\\u06C1 (\\u062F)"}],correctOption:"B",category:"Past Board Papers"}));const fallbackShorts=[1,2,3,4,5].map(i=>({statementEn:`State the governing scientific principle and two key observations of ${req.body?.chapterTitle||"this topic"} (Part ${i}).`,statementUr:`${req.body?.chapterTitle||"\\u0627\\u0633 \\u0645\\u0648\\u0636\\u0648\\u0639"} \\u06A9\\u0627 \\u0628\\u0646\\u06CC\\u0627\\u062F\\u06CC \\u0633\\u0627\\u0626\\u0646\\u0633\\u06CC \\u0627\\u0635\\u0648\\u0644 \\u0627\\u0648\\u0631 \\u062F\\u0648 \\u06A9\\u0644\\u06CC\\u062F\\u06CC \\u0645\\u0634\\u0627\\u06C1\\u062F\\u0627\\u062A \\u062A\\u062D\\u0631\\u06CC\\u0631 \\u06A9\\u0631\\u06CC\\u06BA\\u06D4 (\\u062D\\u0635\\u06C1 ${i})`,marks:2,category:"SLO Conceptual"}));res.json({mcqs:fallbackMCQs,shortQuestions:fallbackShorts,longQuestions:[]})'

replacement = '''const subQuery = (req.body?.subjectName || "Physics").toLowerCase();
const clsQuery = (req.body?.classLevel || "9th").toLowerCase();
const matchedSub = MASTER_PTBB_SUBJECTS.find(s => (clsQuery.includes("10") ? s.id.startsWith("10th") : s.id.startsWith("9th")) && (s.nameEn.toLowerCase().includes(subQuery) || subQuery.includes(s.nameEn.toLowerCase()))) || MASTER_PTBB_SUBJECTS[0];
const targetCh = Number(req.body?.chapterNo || 1);
const pool = getQuestionsForSubjectAndChapters(matchedSub.id, [targetCh]);
res.json({ mcqs: pool.mcqs.slice(0, 15), shortQuestions: pool.shortQuestions.slice(0, 15), longQuestions: pool.longQuestions.slice(0, 3) })'''

if target in text:
    text = text.replace(target, replacement)
    with open("server.ts", "w", encoding="utf-8") as f:
        f.write(text)
    print("Successfully patched server.ts batch fallback!")
else:
    print("Target string not found in server.ts")
