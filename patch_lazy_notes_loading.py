import re

with open("assets/index-DAioIUjd.js", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Update getNotesForSubjectAndChapter
old_fn_start = 'function getNotesForSubjectAndChapter(subjectId, chapterNo, subjectObj, chapterObj) {'
new_fn_start = '''const MODULAR_NOTES_CACHE = {};
function normalizeModularNotes(raw) {
  if (!raw) return raw;
  const clone = { ...raw };
  clone.chapterNo = clone.chapter_no || clone.chapterNo || 1;
  clone.titleEn = (clone.chapter_title && clone.chapter_title.en) || clone.titleEn || "";
  clone.titleUr = (clone.chapter_title && clone.chapter_title.ur) || clone.titleUr || "";
  clone.summaryEn = clone.summaryEn || "";
  clone.summaryUr = clone.summaryUr || "";
  if (Array.isArray(clone.mcqs)) {
    clone.mcqs = clone.mcqs.map((m, i) => {
      const qEn = m.question_en || m.questionEn || "";
      const qUr = m.question_ur || m.questionUr || "";
      let optsEn = m.optionsEn;
      let optsUr = m.optionsUr;
      if (!optsEn && m.options_en) {
        optsEn = [m.options_en.A || "", m.options_en.B || "", m.options_en.C || "", m.options_en.D || ""];
      }
      if (!optsUr && m.options_ur) {
        optsUr = [m.options_ur.A || "", m.options_ur.B || "", m.options_ur.C || "", m.options_ur.D || ""];
      }
      let cIdx = m.correctIndex;
      if (cIdx === undefined && m.correct_answer) {
        cIdx = ["A", "B", "C", "D"].indexOf(m.correct_answer);
        if (cIdx === -1) cIdx = 0;
      }
      return {
        ...m,
        id: m.id || `mcq-${i+1}`,
        questionEn: qEn,
        questionUr: qUr,
        optionsEn: optsEn || ["A", "B", "C", "D"],
        optionsUr: optsUr || ["الف", "ب", "ج", "د"],
        correctIndex: cIdx !== undefined ? cIdx : 0,
        explanationEn: m.explanation_en || m.explanationEn || "",
        explanationUr: m.explanation_ur || m.explanationUr || ""
      };
    });
  }
  const sqList = clone.short_questions || clone.shortQuestions || [];
  clone.shortQuestions = sqList.map((sq, i) => ({
    ...sq,
    id: sq.id || `sq-${i+1}`,
    questionEn: sq.question_en || sq.questionEn || "",
    questionUr: sq.question_ur || sq.questionUr || "",
    answerEn: sq.answer_en || sq.answerEn || "",
    answerUr: sq.answer_ur || sq.answerUr || ""
  }));
  return clone;
}

function getNotesForSubjectAndChapter(subjectId, chapterNo, subjectObj, chapterObj) {
  const cls = (subjectObj && (subjectObj.classLevel || (subjectId.startsWith("10th") ? "class10" : "class9")) || "class9").toLowerCase().replace(/[^a-z0-9]/g, "");
  const sub = (subjectId || "").replace(/^(9th|10th)-?/, "").replace(/-/g, "_");
  const cacheKey = `${cls}-${sub}-${chapterNo}`;

  if (MODULAR_NOTES_CACHE[cacheKey]) {
    return MODULAR_NOTES_CACHE[cacheKey];
  }

  // Asynchronous lazy background fetch on-demand
  if (typeof window !== "undefined" && typeof fetch !== "undefined") {
    fetch(`/api/notes/${cls}/${sub}/${chapterNo}`)
      .then(r => r.ok ? r.json() : null)
      .then(data => {
        if (data) {
          const normalized = normalizeModularNotes(data);
          MODULAR_NOTES_CACHE[cacheKey] = normalized;
          window.dispatchEvent(new CustomEvent("ptbb_notes_loaded", { detail: { cacheKey, data: normalized } }));
        }
      })
      .catch(() => {});
  }
'''

if old_fn_start in text:
    text = text.replace(old_fn_start, new_fn_start, 1)
    print("[✓] Replaced getNotesForSubjectAndChapter with modular dynamic loader")
else:
    print("[!] old_fn_start not found")

# 2. Add listener & state in the notes component
target_use_memo = 'const notesData = Ee.useMemo(() => {    if (!currentSubject) return null;    return getNotesForSubjectAndChapter(currentSubject.id, selectedChapterNo, currentSubject, currentChapter);  }, [currentSubject, selectedChapterNo, currentChapter]);'
new_use_memo = '''const [notesCacheRevision, setNotesCacheRevision] = Ee.useState(0);
  Ee.useEffect(() => {
    const handleLoaded = () => setNotesCacheRevision(v => v + 1);
    window.addEventListener("ptbb_notes_loaded", handleLoaded);
    return () => window.removeEventListener("ptbb_notes_loaded", handleLoaded);
  }, []);
  const notesData = Ee.useMemo(() => {
    if (!currentSubject) return null;
    return getNotesForSubjectAndChapter(currentSubject.id, selectedChapterNo, currentSubject, currentChapter);
  }, [currentSubject, selectedChapterNo, currentChapter, notesCacheRevision]);'''

if target_use_memo in text:
    text = text.replace(target_use_memo, new_use_memo, 1)
    print("[✓] Added notesCacheRevision hook to notes component")
else:
    print("[!] target_use_memo not found")

with open("assets/index-DAioIUjd.js", "w", encoding="utf-8") as f:
    f.write(text)

print("Saved assets/index-DAioIUjd.js successfully!")
