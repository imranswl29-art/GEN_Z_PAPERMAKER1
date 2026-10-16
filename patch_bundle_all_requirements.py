import re, subprocess

print("Loading assets/index-DAioIUjd.js...")
with open("assets/index-DAioIUjd.js", "r", encoding="utf-8") as f:
    text = f.read()

orig_len = len(text)

# =========================================================================
# REQUIREMENT 1: Top Header Sticky Fix
# =========================================================================
old_header_style = 'className:"bg-white border-b border-slate-200 px-4 sm:px-6 py-3 sticky top-0 z-[1000] shadow-sm no-print flex items-center justify-between gap-4 w-full",style:{position:"sticky",top:0,zIndex:1000}'
new_header_style = 'className:"bg-white border-b border-slate-200 px-4 sm:px-6 py-3 relative shadow-sm no-print flex items-center justify-between gap-4 w-full",style:{position:"relative"}'

if old_header_style in text:
    text = text.replace(old_header_style, new_header_style, 1)
    print("[✓] Req 1: Removed sticky/fixed from top header bar")
else:
    print("[!] old_header_style already replaced or not found")

# =========================================================================
# REQUIREMENT 4: Examination Paper Portrait / Landscape Toggle (WK & ET)
# =========================================================================
old_et = 'function ET(n,e="exam-paper-container",t,r="all"){const a=document.getElementById(e);if(!a)return console.error(`Target element with id "${e}" not found for PDF export.`),window.print(),!1;try{t&&t("Preparing high-resolution exam sheet..."),await new Promise(R=>setTimeout(R,150));const o=210,A=297,u=8,f=8,B=o-u*2,m=A-f*2,C=new Xt({orientation:"portrait",unit:"mm",format:"a4",compress:!0}),'
new_et = 'function ET(n,e="exam-paper-container",t,r="all",orientation="portrait"){const a=document.getElementById(e);if(!a)return console.error(`Target element with id "${e}" not found for PDF export.`),window.print(),!1;try{t&&t("Preparing high-resolution exam sheet..."),await new Promise(R=>setTimeout(R,150));const isLand=orientation==="landscape";const o=isLand?297:210,A=isLand?210:297,u=8,f=8,B=o-u*2,m=A-f*2,C=new Xt({orientation:isLand?"landscape":"portrait",unit:"mm",format:"a4",compress:!0}),'

if old_et in text:
    text = text.replace(old_et, new_et, 1)
    print("[✓] Req 4: Updated ET to accept orientation")
else:
    print("[!] old_et already updated or not found")

old_wk_state = 'WK=({paper:n,onUpdatePaper:e,printSection:t,onOpenBubbleSheetModal:r,onOpenAnswerKeyModal:a})=>{const[o,A]=Ee.useState(t==="objective"||t==="subjective"?t:"all"),[u,f]=Ee.useState(!1),[B,m]=Ee.useState(!1),[C,y]=Ee.useState(!1),[v,E]=Ee.useState(""),[I,O]=Ee.useState(null),[F]=Ee.useState(()=>"50"+(Math.floor(Math.random()*89)+10)),R=_x.useRef(null);'
new_wk_state = 'WK=({paper:n,onUpdatePaper:e,printSection:t,onOpenBubbleSheetModal:r,onOpenAnswerKeyModal:a})=>{const[o,A]=Ee.useState(t==="objective"||t==="subjective"?t:"all"),[u,f]=Ee.useState(!1),[B,m]=Ee.useState(!1),[C,y]=Ee.useState(!1),[v,E]=Ee.useState(""),[I,O]=Ee.useState(null),[paperOrientation,setPaperOrientation]=Ee.useState("portrait"),[F]=Ee.useState(()=>"50"+(Math.floor(Math.random()*89)+10)),R=_x.useRef(null);'

if old_wk_state in text:
    text = text.replace(old_wk_state, new_wk_state, 1)

old_wk_Z = 'document.title=`${Y}_Class_${k}${S}_Exam_Paper`,window.print(),setTimeout(()=>{document.title=Ce},1500)}'
new_wk_Z = 'setPrintOrientation(paperOrientation);document.title=`${Y}_Class_${k}${S}_Exam_Paper_${paperOrientation.toUpperCase()}`,window.print(),setTimeout(()=>{document.title=Ce},1500)}'

if old_wk_Z in text:
    text = text.replace(old_wk_Z, new_wk_Z, 1)

old_wk_ne = 'await ET(n,"exam-paper-container",k=>{E(k)},o)||m(!0)'
new_wk_ne = 'await ET(n,"exam-paper-container",k=>{E(k)},o,paperOrientation)||m(!0)'

if old_wk_ne in text:
    text = text.replace(old_wk_ne, new_wk_ne, 1)

old_wk_toolbar_btn = 'l.jsxs("button",{type:"button",onClick:Z,className:"btn-print-preview",title:"Print Full A4 Paper directly with print preview"'
new_wk_toolbar_btn = '''l.jsxs("div",{className:"flex items-center gap-1 bg-slate-100 p-1 rounded-xl border border-slate-200 mr-1 no-print",children:[l.jsxs("button",{type:"button",onClick:()=>{setPaperOrientation("portrait");setPrintOrientation("portrait");},className:`flex items-center gap-1 px-3 py-1.5 rounded-lg text-xs font-bold transition-all cursor-pointer ${paperOrientation==="portrait"?"bg-white text-blue-700 shadow-xs font-black ring-1 ring-blue-300":"text-slate-600 hover:text-slate-900"}`,title:"Portrait (Vertical Orientation) - عمودی انداز",children:[l.jsx("span",{children:"📄"}),l.jsx("span",{children:"Portrait (عمودی)"})]}),l.jsxs("button",{type:"button",onClick:()=>{setPaperOrientation("landscape");setPrintOrientation("landscape");},className:`flex items-center gap-1 px-3 py-1.5 rounded-lg text-xs font-bold transition-all cursor-pointer ${paperOrientation==="landscape"?"bg-white text-blue-700 shadow-xs font-black ring-1 ring-blue-300":"text-slate-600 hover:text-slate-900"}`,title:"Landscape (Horizontal Orientation) - افقی انداز",children:[l.jsx("span",{children:"📑"}),l.jsx("span",{children:"Landscape (افقی)"})]})]}),l.jsxs("button",{type:"button",onClick:Z,className:"btn-print-preview",title:"Print Full A4 Paper directly with print preview"'''

if old_wk_toolbar_btn in text:
    text = text.replace(old_wk_toolbar_btn, new_wk_toolbar_btn, 1)

# In WK paper container, add dynamic max-w based on paperOrientation
pos_c = text.find('id:"exam-paper-container"')
if pos_c != -1:
    end_div = text.find('>', pos_c)
    container_tag = text[pos_c:end_div]
    if "landscape-mode" not in container_tag:
        # replace className
        new_tag = re.sub(r'className:"([^"]+)"', r'className:`\1 ${paperOrientation==="landscape"?"max-w-6xl landscape-mode":"max-w-4xl portrait-mode"}`', container_tag)
        text = text[:pos_c] + new_tag + text[end_div:]
        print("[✓] Updated exam-paper-container className with landscape-mode support")

# =========================================================================
# REQUIREMENT 3: Complete AI Solved Notes Section (Class 9th & 10th)
# =========================================================================
pos_norm_start = text.find("function normalizeModularNotes(raw) {")
pos_norm_end = text.find("function getNotesForSubjectAndChapter", pos_norm_start)

if pos_norm_start != -1 and pos_norm_end != -1:
    new_norm_code = '''function normalizeModularNotes(raw) {
  if (!raw) return raw;
  const clone = { ...raw };
  clone.chapterNo = clone.chapter_no || clone.chapterNo || 1;
  clone.titleEn = (clone.chapter_title && clone.chapter_title.en) || clone.titleEn || "";
  clone.titleUr = (clone.chapter_title && clone.chapter_title.ur) || clone.titleUr || "";
  clone.summaryEn = clone.summaryEn || "";
  clone.summaryUr = clone.summaryUr || "";

  // Normalize and deduplicate comprehensive topics
  const rawTopics = clone.comprehensive_topics || clone.topics || [];
  const seenTopics = new Set();
  clone.comprehensive_topics = (Array.isArray(rawTopics) && rawTopics.length > 0 ? rawTopics : [
    {
      topicNo: 1,
      titleEn: `Fundamental Principles, Governing Laws & Key Concepts of ${clone.titleEn || "Unit " + clone.chapterNo}`,
      titleUr: `${clone.titleUr || "یونٹ " + clone.chapterNo} کے بنیادی سائنسی اصول، قوانین اور تفصیلی نوٹس`,
      contentEn: `In-depth academic review of governing definitions, standard SI units, scientific formulas, and experimental methods prescribed by the Punjab Textbook Board (PTBB).`,
      contentUr: `پنجاب ٹیکسٹ بک بورڈ کے نصاب کے مطابق بنیادی تعریفات، معیاری ایس آئی اکائیاں، سائنسی کلیات اور امتحانی فارمولوں کا مکمل احاطہ۔`,
      keyPointsEn: [
        `Strict adherence to official Student Learning Outcomes (SLOs).`,
        `Standard board derivations and step-by-step formula applications.`,
        `High-frequency past BISE Punjab paper conceptual questions.`
      ],
      keyPointsUr: [
        `پنجاب بورڈ کے طے شدہ تدریسی مقاصد کے عین مطابق تیاری۔`,
        `معیاری فارمولا کا اخذ اور حسابی مسائل کا درست طریقہ کار۔`,
        `ماضی کے بورڈ امتحانات میں بار بار پوچھے جانے والے اہم ترین نکات۔`
      ]
    }
  ]).filter(tp => {
    const k = ((tp.titleEn || "") + "|" + (tp.titleUr || "")).trim().toLowerCase();
    if (!k || seenTopics.has(k)) return false;
    seenTopics.add(k);
    return true;
  });

  if (Array.isArray(clone.mcqs)) {
    const seenM = new Set();
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
    }).filter(m => {
      const k = (m.questionEn || "").trim().toLowerCase();
      if (!k || seenM.has(k)) return false;
      seenM.add(k);
      return true;
    });
  }

  const sqList = clone.short_questions || clone.shortQuestions || [];
  const seenS = new Set();
  clone.shortQuestions = sqList.map((sq, i) => ({
    ...sq,
    id: sq.id || `sq-${i+1}`,
    questionEn: sq.question_en || sq.questionEn || "",
    questionUr: sq.question_ur || sq.questionUr || "",
    answerEn: sq.answer_en || sq.answerEn || "",
    answerUr: sq.answer_ur || sq.answerUr || ""
  })).filter(sq => {
    const k = (sq.questionEn || "").trim().toLowerCase();
    if (!k || seenS.has(k)) return false;
    seenS.add(k);
    return true;
  });

  return clone;
}\n\n'''
    text = text[:pos_norm_start] + new_norm_code + text[pos_norm_end:]
    print("[✓] Updated normalizeModularNotes with deduplication and comprehensive_topics")

# In ClassNotesView state: add isAiGenerating, notesOrientation, handleGenerateAiNotes
pos_hook = text.find('const [notesCacheRevision, setNotesCacheRevision] = Ee.useState(0);')
if pos_hook != -1 and "handleGenerateAiNotes" not in text:
    hook_expansion = '''const [notesCacheRevision, setNotesCacheRevision] = Ee.useState(0);
  const [isAiGenerating, setIsAiGenerating] = Ee.useState(false);
  const [notesOrientation, setNotesOrientation] = Ee.useState("portrait");
  const handleGenerateAiNotes = async () => {
    if (!currentSubject) return;
    try {
      setIsAiGenerating(true);
      const res = await fetch("/api/generate-notes", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          classLevel: selectedClass || "9th",
          subjectName: currentSubject.nameEn || "Physics",
          chapterNo: selectedChapterNo || 1,
          chapterTitle: currentChapter ? currentChapter.titleEn : ""
        })
      });
      if (res.ok) {
        const data = await res.json();
        const cls = (selectedClass || "class9").toLowerCase().replace(/[^a-z0-9]/g, "");
        const sub = (currentSubject.id || "").replace(/^(9th|10th)-?/, "").replace(/-/g, "_");
        const cacheKey = `${cls}-${sub}-${selectedChapterNo}`;
        const norm = normalizeModularNotes(data);
        MODULAR_NOTES_CACHE[cacheKey] = norm;
        setNotesCacheRevision(v => v + 1);
        window.dispatchEvent(new CustomEvent("ptbb_notes_loaded", { detail: { cacheKey, data: norm } }));
      }
    } catch (e) {
      console.warn("AI Notes Generation error:", e);
    } finally {
      setIsAiGenerating(false);
    }
  };'''
    text = text[:pos_hook] + hook_expansion + text[pos_hook + len('const [notesCacheRevision, setNotesCacheRevision] = Ee.useState(0);'):]
    print("[✓] Added handleGenerateAiNotes and notesOrientation to ClassNotesView")

# In exportNotesToPDF, accept orientation
pos_exp_pdf = text.find('function exportNotesToPDF(elementId, selectedClass, subjectNameEn, chapterNo, effectiveLangMode')
if pos_exp_pdf != -1:
    pos_end_decl = text.find('const pdf = new Xt({', pos_exp_pdf)
    old_pdf_decl = text[pos_exp_pdf:pos_end_decl]
    new_pdf_decl = '''function exportNotesToPDF(elementId, selectedClass, subjectNameEn, chapterNo, effectiveLangMode, orientation = "portrait") {  const element = document.getElementById(elementId);  if (!element) {    console.error("PDF target element not found: " + elementId);    return;  }  const filename = `${selectedClass}_Class_${subjectNameEn.replace(/\\s+/g, '_')}_Unit_${chapterNo}_Solved_Notes_${effectiveLangMode}_${orientation.toUpperCase()}.pdf`;  try {    const isLand = orientation === "landscape"; const a = isLand ? 297 : 210, o = isLand ? 210 : 297, A = 8, u = 8, f = a - A * 2, B = o - u * 2;    '''
    text = text[:pos_exp_pdf] + new_pdf_decl + text[pos_end_decl:]
    print("[✓] Updated exportNotesToPDF with orientation support")

# In ClassNotesView handleDownloadPDF, pass notesOrientation
old_call_pdf = 'await exportNotesToPDF("notes-print-sheet", selectedClass, currentSubject.nameEn, notesData.chapterNo, effectiveLangMode);'
new_call_pdf = 'setPrintOrientation(notesOrientation); await exportNotesToPDF("notes-print-sheet", selectedClass, currentSubject.nameEn, notesData.chapterNo, effectiveLangMode, notesOrientation);'
if old_call_pdf in text:
    text = text.replace(old_call_pdf, new_call_pdf, 1)

# In ClassNotesView toolbar, add AI Notes button and Orientation toggle
marker_notes_tool = 'title: `Download Solved Notes as PDF Document (${effectiveLangMode.toUpperCase()})`,'
if marker_notes_tool in text and "AI Solved Notes (Gemini)" not in text:
    tool_inject = '''title: `Download Solved Notes as PDF Document (${effectiveLangMode.toUpperCase()})`,
                  }),
                  // AI Solved Notes Generation Button (Gemini AI Powered)
                  l.jsxs("button", {
                    type: "button",
                    disabled: isAiGenerating,
                    onClick: handleGenerateAiNotes,
                    className: "min-h-[44px] max-h-[48px] inline-flex items-center gap-2 px-4 py-2.5 bg-gradient-to-r from-purple-700 via-indigo-700 to-blue-700 hover:from-purple-600 hover:to-indigo-600 text-white rounded-xl text-xs font-black cursor-pointer shadow-md hover:shadow-lg active:scale-95 transition-all disabled:opacity-60",
                    title: "Generate or refresh 100% comprehensive solved notes with Gemini AI",
                    children: [
                      isAiGenerating ? l.jsx(Sc, { className: "w-4 h-4 animate-spin text-purple-200" }) : l.jsx("span", { children: "✨" }),
                      l.jsx("span", { children: isAiGenerating ? "Generating Notes with Gemini..." : "AI Solved Notes (Gemini)" })
                    ]
                  }),
                  // Orientation switcher
                  l.jsxs("div", {
                    className: "flex items-center gap-1 bg-slate-100 p-1 rounded-xl border border-slate-200 no-print",
                    children: [
                      l.jsxs("button", {
                        type: "button",
                        onClick: () => { setNotesOrientation("portrait"); setPrintOrientation("portrait"); },
                        className: `flex items-center gap-1 px-3 py-1.5 rounded-lg text-xs font-bold transition-all cursor-pointer ${notesOrientation === "portrait" ? "bg-white text-blue-700 shadow-xs font-black ring-1 ring-blue-300" : "text-slate-600 hover:text-slate-900"}`,
                        title: "Portrait (Vertical)",
                        children: [l.jsx("span", { children: "📄" }), l.jsx("span", { children: "Portrait (عمودی)" })]
                      }),
                      l.jsxs("button", {
                        type: "button",
                        onClick: () => { setNotesOrientation("landscape"); setPrintOrientation("landscape"); },
                        className: `flex items-center gap-1 px-3 py-1.5 rounded-lg text-xs font-bold transition-all cursor-pointer ${notesOrientation === "landscape" ? "bg-white text-blue-700 shadow-xs font-black ring-1 ring-blue-300" : "text-slate-600 hover:text-slate-900"}`,
                        title: "Landscape (Horizontal)",
                        children: [l.jsx("span", { children: "📑" }), l.jsx("span", { children: "Landscape (افقی)" })]
                      })
                    ]'''
    text = text.replace(marker_notes_tool, tool_inject, 1)
    print("[✓] Added AI Solved Notes button & Orientation toggle in ClassNotesView")

# In notes-print-sheet, render Section C (Conceptual Review & Comprehensive Topics)
pos_sec_b = text.find('Section B: Solved Short Questions')
if pos_sec_b != -1 and "Section C: Conceptual Review" not in text:
    pos_footer_stamp = text.find('// Notes Footer Signature & Stamp Box', pos_sec_b)
    if pos_footer_stamp != -1:
        sec_c_markup = '''// Section C: Conceptual Review & Solved Comprehensive Topics
              l.jsxs("div", {
                className: "space-y-4 pt-4 border-t-2 border-slate-200",
                children: [
                  l.jsxs("div", {
                    className: "border-l-4 border-indigo-700 pl-3 py-0.5 flex items-center justify-between",
                    children: [
                      l.jsx("h4", {
                        className: "text-sm sm:text-base font-black text-slate-900 uppercase tracking-wide",
                        children: "Section C: Conceptual Review & Comprehensive Solved Topics"
                      }),
                      l.jsx("span", {
                        className: "text-xs font-bold text-slate-500",
                        children: "In-Depth Theory, Laws & Solved Board Problems"
                      })
                    ]
                  }),
                  l.jsx("div", {
                    className: "space-y-4",
                    children: (notesData.comprehensive_topics || []).map((tp, tpIdx) => {
                      return l.jsxs("div", {
                        key: tpIdx,
                        className: "p-4 sm:p-5 rounded-xl border border-slate-200 bg-white space-y-3 shadow-2xs page-break-inside-avoid",
                        children: [
                          l.jsxs("div", {
                            className: "flex items-start justify-between gap-2 border-b border-slate-100 pb-2.5",
                            children: [
                              l.jsxs("div", {
                                className: "flex items-start gap-2",
                                children: [
                                  l.jsxs("span", {
                                    className: "px-2.5 py-0.5 rounded bg-indigo-100 text-indigo-900 font-black text-xs shrink-0",
                                    children: ["Topic ", tp.topicNo || (tpIdx + 1)]
                                  }),
                                  l.jsx("h5", {
                                    className: "font-black text-slate-900 text-sm leading-relaxed",
                                    children: effectiveLangMode === "urdu" ? (tp.titleUr || tp.titleEn) : tp.titleEn
                                  })
                                ]
                              }),
                              effectiveLangMode !== "english" && tp.titleUr && l.jsx("span", {
                                className: "font-urdu text-right text-sm text-indigo-900 font-bold pr-2",
                                dir: "rtl",
                                children: tp.titleUr
                              })
                            ]
                          }),
                          effectiveLangMode !== "urdu" && tp.contentEn && l.jsx("div", {
                            className: "text-slate-700 text-xs sm:text-sm leading-relaxed whitespace-pre-line font-medium",
                            children: tp.contentEn
                          }),
                          effectiveLangMode !== "english" && tp.contentUr && l.jsx("div", {
                            className: "font-urdu text-right text-slate-900 text-sm leading-relaxed whitespace-pre-line font-semibold pt-1",
                            dir: "rtl",
                            children: tp.contentUr
                          }),
                          tp.keyPointsEn && tp.keyPointsEn.length > 0 && l.jsxs("div", {
                            className: "bg-slate-50 border border-slate-200 rounded-lg p-3 space-y-1.5 text-xs",
                            children: [
                              l.jsx("span", {
                                className: "font-black text-indigo-900 text-[11px] uppercase tracking-wider block",
                                children: "✔ Key Examination Takeaways & Board Formulae:"
                              }),
                              l.jsx("ul", {
                                className: "list-disc list-inside space-y-1 text-slate-700 font-medium",
                                children: tp.keyPointsEn.map((pt, pIdx) => l.jsx("li", { key: pIdx, children: pt }))
                              })
                            ]
                          })
                        ]
                      });
                    })
                  })
                ]
              }),
              '''
        text = text[:pos_footer_stamp] + sec_c_markup + text[pos_footer_stamp:]
        print("[✓] Rendered Section C in notes-print-sheet")

# =========================================================================
# REQUIREMENT 5: Result Card & Marksheet Generator Feature Expansion
# =========================================================================
helper_tools = '''
function exportWholeSchoolConsolidatedGazette(sheetsList, brand) {
  const brandTitle = (brand && (brand.instituteName || brand.schoolName)) || "PUNJAB GROUP OF SCIENCE ACADEMIES";
  const brandCampus = (brand && (brand.campusName || brand.address)) || "Main Campus, Lahore";
  const sheets = Array.isArray(sheetsList) && sheetsList.length > 0 ? sheetsList : [];
  
  let rows = "";
  let grandTotalStudents = 0;
  let grandTotalPassed = 0;
  let grandTotalFailed = 0;

  sheets.forEach((sheet, idx) => {
    const students = sheet.students || [];
    const totalSubs = (sheet.subjects || []).reduce((sum, s) => sum + s.totalMarks, 0);
    const count = students.length;
    grandTotalStudents += count;

    let passedCount = 0;
    let failedCount = 0;
    
    const scored = students.map(st => {
      let obt = 0;
      let isPass = true;
      (sheet.subjects || []).forEach(sub => {
        const m = Number((st.marks && st.marks[sub.id]) || 0);
        obt += m;
        if (m < sub.passingMarks) isPass = false;
      });
      if (isPass) passedCount++; else failedCount++;
      const pct = totalSubs > 0 ? (obt / totalSubs * 100).toFixed(1) : "0.0";
      return { ...st, _obt: obt, _pct: pct, _isPass: isPass };
    });
    grandTotalPassed += passedCount;
    grandTotalFailed += failedCount;

    scored.sort((a, b) => b._obt - a._obt);
    const top1 = scored[0] ? `${scored[0].name} (Roll# ${scored[0].rollNo} - ${scored[0]._obt} M / ${scored[0]._pct}%)` : "-";
    const top2 = scored[1] ? `${scored[1].name} (Roll# ${scored[1].rollNo} - ${scored[1]._obt} M / ${scored[1]._pct}%)` : "-";
    const top3 = scored[2] ? `${scored[2].name} (Roll# ${scored[2].rollNo} - ${scored[2]._obt} M / ${scored[2]._pct}%)` : "-";
    const passPct = count > 0 ? (passedCount / count * 100).toFixed(1) : "0.0";

    const isEven = idx % 2 === 0;
    const bg = isEven ? "#ffffff" : "#f8fafc";

    rows += `
      <tr>
        <td align="center" style="background-color: ${bg}; padding: 6pt; border: 1pt solid #cbd5e1; font-weight: bold;">${idx + 1}</td>
        <td style="background-color: ${bg}; padding: 6pt; border: 1pt solid #cbd5e1; font-weight: bold; color: #1e3a8a;">${sheet.classLevel}</td>
        <td align="center" style="background-color: ${bg}; padding: 6pt; border: 1pt solid #cbd5e1;">${sheet.session || "2025-2026"}</td>
        <td align="center" style="background-color: ${bg}; padding: 6pt; border: 1pt solid #cbd5e1; font-weight: bold;">${count}</td>
        <td align="center" style="background-color: #ecfdf5; padding: 6pt; border: 1pt solid #cbd5e1; font-weight: bold; color: #047857;">${passedCount}</td>
        <td align="center" style="background-color: #fee2e2; padding: 6pt; border: 1pt solid #cbd5e1; font-weight: bold; color: #b91c1c;">${failedCount}</td>
        <td align="center" style="background-color: ${bg}; padding: 6pt; border: 1pt solid #cbd5e1; font-weight: bold; color: #1d4ed8;">${passPct}%</td>
        <td style="background-color: ${bg}; padding: 6pt; border: 1pt solid #cbd5e1; font-size: 9pt;">${top1}</td>
        <td style="background-color: ${bg}; padding: 6pt; border: 1pt solid #cbd5e1; font-size: 9pt;">${top2}</td>
        <td style="background-color: ${bg}; padding: 6pt; border: 1pt solid #cbd5e1; font-size: 9pt;">${top3}</td>
      </tr>
    `;
  });

  const grandPassPct = grandTotalStudents > 0 ? (grandTotalPassed / grandTotalStudents * 100).toFixed(1) : "0.0";

  const html = `<!DOCTYPE html><html xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:x="urn:schemas-microsoft-com:office:excel" xmlns="http://www.w3.org/TR/REC-html40">
  <head><meta http-equiv="Content-Type" content="application/vnd.ms-excel; charset=utf-8">
  <title>${brandTitle} - Whole School Consolidated Gazette</title>
  <style>
    body { font-family: 'Segoe UI', Calibri, Arial, sans-serif; font-size: 10pt; }
    table { border-collapse: collapse; width: 100%; }
    .header { background-color: #0f2942; color: #ffffff; font-size: 14pt; font-weight: bold; text-align: center; padding: 12pt; }
    .sub { background-color: #1e3a8a; color: #e2e8f0; font-size: 10.5pt; text-align: center; padding: 6pt; }
    th { background-color: #1e293b; color: #ffffff; padding: 8pt 5pt; border: 1pt solid #475569; font-size: 9.5pt; text-align: center; }
  </style>
  </head>
  <body>
    <table>
      <tr><td colspan="10" class="header">${brandTitle}</td></tr>
      <tr><td colspan="10" class="sub">${brandCampus} &bull; WHOLE SCHOOL CONSOLIDATED EXAMINATION GAZETTE &bull; ACADEMIC YEAR 2025-2026</td></tr>
      <tr><td colspan="10" style="padding: 4pt;"></td></tr>
      <thead>
        <tr>
          <th>#</th>
          <th>Class / Grade Level</th>
          <th>Session</th>
          <th>Total Enrolled</th>
          <th>Passed</th>
          <th>Failed</th>
          <th>Overall Pass %</th>
          <th>1st Position Holder</th>
          <th>2nd Position Holder</th>
          <th>3rd Position Holder</th>
        </tr>
      </thead>
      <tbody>
        ${rows}
        <tr style="background-color: #e2e8f0; font-weight: bold;">
          <td colspan="3" align="right" style="padding: 8pt; border: 1pt solid #94a3b8; font-size: 11pt;">WHOLE SCHOOL TOTAL / AVERAGE:</td>
          <td align="center" style="padding: 8pt; border: 1pt solid #94a3b8; font-size: 11pt;">${grandTotalStudents}</td>
          <td align="center" style="padding: 8pt; border: 1pt solid #94a3b8; font-size: 11pt; color: #047857;">${grandTotalPassed}</td>
          <td align="center" style="padding: 8pt; border: 1pt solid #94a3b8; font-size: 11pt; color: #b91c1c;">${grandTotalFailed}</td>
          <td align="center" style="padding: 8pt; border: 1pt solid #94a3b8; font-size: 11pt; color: #1d4ed8;">${grandPassPct}%</td>
          <td colspan="3" align="center" style="padding: 8pt; border: 1pt solid #94a3b8; color: #475569;">Consolidated Institution Performance Summary</td>
        </tr>
      </tbody>
    </table>
  </body></html>`;

  const blob = new Blob(["\\ufeff", html], { type: "application/vnd.ms-excel;charset=utf-8" });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = `${brandTitle.replace(/\\s+/g, "_")}_Whole_School_Consolidated_Gazette.xls`;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
}
'''

if "function exportWholeSchoolConsolidatedGazette" not in text:
    text = text.replace("function exportMasterGazetteToExcel", helper_tools + "function exportMasterGazetteToExcel", 1)

# In lq component: add autoCalculateRanks, setGlobalPassingPercentage, fileInputRef, handleImportCSV
old_lq_funcs_marker = 'const saveCurrentSheet=(sheetToSave=R)=>{'

new_lq_funcs = '''const fileInputRef = Ee.useRef(null);
const autoCalculateRanks = () => {
  const list = [...R.students];
  const withScores = list.map(st => {
    const tot = R.subjects.reduce((sum, sub) => sum + Number((st.marks && st.marks[sub.id]) || 0), 0);
    return { ...st, _tot: tot };
  });
  withScores.sort((a, b) => b._tot - a._tot);
  const updated = withScores.map((st, i) => {
    const pos = i === 0 ? "1st" : i === 1 ? "2nd" : i === 2 ? "3rd" : `${i + 1}th`;
    const { _tot, ...rest } = st;
    return { ...rest, rank: pos };
  });
  Z(prev => ({ ...prev, students: updated }));
  F("تمام طلباء کی پوزیشنز خودکار طور پر کیلکولیٹ ہو گئیں!");
};
const setGlobalPassingPercentage = (pct = 33) => {
  Z(prev => ({
    ...prev,
    subjects: prev.subjects.map(s => ({
      ...s,
      passingMarks: Math.ceil(s.totalMarks * (pct / 100))
    }))
  }));
  F(`تمام مضامین کے پاسنگ مارکس ${pct}% کر دیے گئے!`);
};
const handleImportCSV = (evt) => {
  const file = evt.target.files && evt.target.files[0];
  if (!file) return;
  const reader = new FileReader();
  reader.onload = (e) => {
    const content = e.target.result;
    if (typeof content !== "string") return;
    const lines = content.split(/\\r?\\n/).map(l => l.trim()).filter(Boolean);
    if (lines.length < 2) return alert("File is empty or invalid format.");
    const headers = lines[0].split(/[,\\t]/).map(h => h.trim().toLowerCase());
    const rollIdx = headers.findIndex(h => h.includes("roll"));
    const nameIdx = headers.findIndex(h => h.includes("name") && !h.includes("father"));
    const fatherIdx = headers.findIndex(h => h.includes("father"));
    const secIdx = headers.findIndex(h => h.includes("section") || h.includes("sec"));

    const subIndices = R.subjects.map(sub => {
      const idx = headers.findIndex(h => h.includes(sub.name.toLowerCase()) || sub.name.toLowerCase().includes(h));
      return { subId: sub.id, colIdx: idx };
    });

    const parsedStudents = [];
    for (let i = 1; i < lines.length; i++) {
      const cols = lines[i].split(/[,\\t]/).map(c => c.trim().replace(/^["']|["']$/g, ""));
      if (cols.length < 2) continue;
      const rollNo = rollIdx >= 0 ? cols[rollIdx] : String(i);
      const name = nameIdx >= 0 ? cols[nameIdx] : `Student ${i}`;
      const fatherName = fatherIdx >= 0 ? cols[fatherIdx] : "Father Name";
      const section = secIdx >= 0 ? cols[secIdx] : "A";
      const marks = {};
      subIndices.forEach(({ subId, colIdx }) => {
        if (colIdx >= 0 && cols[colIdx] !== undefined) {
          marks[subId] = Number(cols[colIdx]) || 0;
        }
      });
      parsedStudents.push({
        id: `st-${Date.now()}-${i}`,
        rollNo,
        name,
        fatherName,
        section,
        attendance: "95%",
        rank: "",
        remarks: "Satisfactory performance.",
        marks
      });
    }
    if (parsedStudents.length > 0) {
      Z(prev => ({ ...prev, students: parsedStudents }));
      F(`کامیابی کے ساتھ ${parsedStudents.length} طلباء کا ڈیٹا امپورٹ ہو گیا!`);
    }
  };
  reader.readAsText(file);
  if (fileInputRef.current) fileInputRef.current.value = "";
};
const saveCurrentSheet=(sheetToSave=R)=>{'''

if old_lq_funcs_marker in text and "autoCalculateRanks" not in text:
    text = text.replace(old_lq_funcs_marker, new_lq_funcs, 1)

# In top card of lq: add Whole School Gazette, Import Excel, and Auto-Rank controls
old_lq_top_actions = '''l.jsxs("button",{type:"button",onClick:()=>exportMasterGazetteToExcel(R,r,m_sec),className:"btn-3d btn-3d-green flex items-center gap-1.5 px-3.5 py-1.5 text-white rounded-xl text-xs font-black cursor-pointer shadow-sm hover:brightness-110",title:"Download complete marksheet data in Excel (.xls) format anytime",children:[l.jsx("span",{children:"📊"}),l.jsx("span",{children:"Download in Excel"})]})'''

new_lq_top_actions = '''l.jsx("input",{ref:fileInputRef,type:"file",accept:".csv,.tsv,.txt",className:"hidden",onChange:handleImportCSV}),
l.jsxs("button",{type:"button",onClick:()=>fileInputRef.current&&fileInputRef.current.click(),className:"btn-3d bg-slate-800 hover:bg-slate-700 border border-slate-600 flex items-center gap-1.5 px-3 py-1.5 text-white rounded-xl text-xs font-black cursor-pointer shadow-sm",title:"Import marks from CSV or Excel file",children:[l.jsx("span",{children:"📥"}),l.jsx("span",{children:"Import CSV/Excel"})]}),
l.jsxs("button",{type:"button",onClick:autoCalculateRanks,className:"btn-3d btn-3d-amber flex items-center gap-1.5 px-3 py-1.5 text-slate-950 rounded-xl text-xs font-black cursor-pointer shadow-sm hover:brightness-110",title:"Auto calculate student class positions (1st, 2nd, 3rd) based on total marks",children:[l.jsx("span",{children:"⚡"}),l.jsx("span",{children:"Auto-Rank (پوزیشنز)"})]}),
l.jsxs("button",{type:"button",onClick:()=>exportMasterGazetteToExcel(R,r,m_sec),className:"btn-3d btn-3d-green flex items-center gap-1.5 px-3.5 py-1.5 text-white rounded-xl text-xs font-black cursor-pointer shadow-sm hover:brightness-110",title:"Download complete class marksheet data in Excel (.xls) format",children:[l.jsx("span",{children:"📊"}),l.jsx("span",{children:"Class Excel (.xls)"})]}),
l.jsxs("button",{type:"button",onClick:()=>exportWholeSchoolConsolidatedGazette(savedSheets.length>0?savedSheets:[R],r),className:"btn-3d bg-purple-800 hover:bg-purple-700 border border-purple-500 flex items-center gap-1.5 px-3.5 py-1.5 text-white rounded-xl text-xs font-black cursor-pointer shadow-sm hover:brightness-110",title:"Export all-school consolidated summary report across multiple grades",children:[l.jsx("span",{children:"🏫"}),l.jsx("span",{children:"Whole School Gazette"})]})'''

if old_lq_top_actions in text:
    text = text.replace(old_lq_top_actions, new_lq_top_actions, 1)

# In subjects management section of lq: add quick Passing Threshold Controls
old_sub_header = '''l.jsxs("div",{className:"flex items-center justify-between",children:[l.jsx("h3",{className:"font-black text-sm text-slate-900 uppercase tracking-wide",children:"Subjects & Total Marks Allocation:"})'''

new_sub_header = '''l.jsxs("div",{className:"flex flex-wrap items-center justify-between gap-2",children:[l.jsxs("div",{className:"flex items-center gap-2",children:[l.jsx("h3",{className:"font-black text-sm text-slate-900 uppercase tracking-wide",children:"Subjects & Marks:"}),l.jsxs("div",{className:"flex items-center gap-1 bg-slate-100 p-1 rounded-lg border border-slate-200 text-xs",children:[l.jsx("span",{className:"text-[10px] font-bold text-slate-500 px-1",children:"Passing %:"}),l.jsx("button",{type:"button",onClick:()=>setGlobalPassingPercentage(33),className:"px-2 py-0.5 rounded bg-white text-blue-800 font-black border border-slate-300 hover:bg-blue-50 text-[10px] cursor-pointer",children:"33% (Board)"}),l.jsx("button",{type:"button",onClick:()=>setGlobalPassingPercentage(40),className:"px-2 py-0.5 rounded bg-white text-blue-800 font-black border border-slate-300 hover:bg-blue-50 text-[10px] cursor-pointer",children:"40%"}),l.jsx("button",{type:"button",onClick:()=>setGlobalPassingPercentage(50),className:"px-2 py-0.5 rounded bg-white text-blue-800 font-black border border-slate-300 hover:bg-blue-50 text-[10px] cursor-pointer",children:"50%"})]})]})'''

if old_sub_header in text:
    text = text.replace(old_sub_header, new_sub_header, 1)

# Save file
with open("assets/index-DAioIUjd.js", "w", encoding="utf-8") as f:
    f.write(text)

print(f"File updated successfully! Orig len: {orig_len} -> New len: {len(text)}")
