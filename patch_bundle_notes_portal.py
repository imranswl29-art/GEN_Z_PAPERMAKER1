import subprocess
import os

print("Building NotesPortalComponent patch script...")

with open('assets/index-DAioIUjd.js', 'r', encoding='utf-8') as f:
    text = f.read()

def verify_syntax(content, desc):
    with open('step_check.js', 'w', encoding='utf-8') as f_out:
        f_out.write(content)
    res = subprocess.run(['node', '--check', 'step_check.js'], capture_output=True, text=True)
    if res.returncode != 0:
        print(f"SYNTAX ERROR AT {desc}:")
        print(res.stderr[:500])
        return False
    print(f"SYNTAX OK: {desc}")
    return True

# 1. NotesPortalComponent Definition
notes_portal_code = '''
const SUBJECT_METADATA_9TH = [
  { id: "physics", nameEn: "Physics", nameUr: "طبیعیات", chaptersCount: 9, icon: "⚡" },
  { id: "chemistry", nameEn: "Chemistry", nameUr: "کیمسٹری", chaptersCount: 8, icon: "🧪" },
  { id: "biology", nameEn: "Biology", nameUr: "حیاتیات", chaptersCount: 9, icon: "🧬" },
  { id: "mathematics", nameEn: "Mathematics", nameUr: "ریاضی", chaptersCount: 17, icon: "📐" },
  { id: "computer", nameEn: "Computer Science", nameUr: "کمپیوٹر سائنس", chaptersCount: 5, icon: "💻" },
  { id: "english", nameEn: "English", nameUr: "انگریزی لازمی", chaptersCount: 12, icon: "📖" },
  { id: "urdu", nameEn: "Urdu", nameUr: "اردو لازمی", chaptersCount: 7, icon: "✍️" },
  { id: "islamiyat", nameEn: "Islamiat Compulsory", nameUr: "اسلامیات لازمی", chaptersCount: 6, icon: "🕌" },
  { id: "tarjuma_quran", nameEn: "Tarjuma-tul-Quran-ul-Majeed", nameUr: "ترجمۃ القرآن المجید", chaptersCount: 6, icon: "📜" },
  { id: "pakstudies", nameEn: "Pakistan Studies", nameUr: "مطالعہ پاکستان", chaptersCount: 5, icon: "🇵🇰" }
];

const SUBJECT_METADATA_10TH = [
  { id: "physics", nameEn: "Physics", nameUr: "طبیعیات", chaptersCount: 9, icon: "⚡" },
  { id: "chemistry", nameEn: "Chemistry", nameUr: "کیمسٹری", chaptersCount: 8, icon: "🧪" },
  { id: "biology", nameEn: "Biology", nameUr: "حیاتیات", chaptersCount: 9, icon: "🧬" },
  { id: "mathematics", nameEn: "Mathematics", nameUr: "ریاضی", chaptersCount: 13, icon: "📐" },
  { id: "computer", nameEn: "Computer Science", nameUr: "کمپیوٹر سائنس", chaptersCount: 5, icon: "💻" },
  { id: "english", nameEn: "English", nameUr: "انگریزی لازمی", chaptersCount: 13, icon: "📖" },
  { id: "urdu", nameEn: "Urdu", nameUr: "اردو لازمی", chaptersCount: 10, icon: "✍️" },
  { id: "islamiyat", nameEn: "Islamiat Compulsory", nameUr: "اسلامیات لازمی", chaptersCount: 6, icon: "🕌" },
  { id: "tarjuma_quran", nameEn: "Tarjuma-tul-Quran-ul-Majeed", nameUr: "ترجمۃ القرآن المجید", chaptersCount: 6, icon: "📜" },
  { id: "pakstudies", nameEn: "Pakistan Studies", nameUr: "مطالعہ پاکستان", chaptersCount: 5, icon: "🇵🇰" }
];

const NotesPortalComponent = ({ currentUser, onBack }) => {
  const [selectedClass, setSelectedClass] = Ee.useState("9th");
  const [selectedSubjectId, setSelectedSubjectId] = Ee.useState("physics");
  const [selectedChapterNo, setSelectedChapterNo] = Ee.useState(1);
  const [sectionFilter, setSectionFilter] = Ee.useState("all");
  const [languageView, setLanguageView] = Ee.useState("bilingual");
  const [searchQuery, setSearchQuery] = Ee.useState("");
  const [printFilter, setPrintFilter] = Ee.useState("all");
  const [copySuccess, setCopySuccess] = Ee.useState(false);
  const [loadingNotes, setLoadingNotes] = Ee.useState(false);
  const [remoteNotes, setRemoteNotes] = Ee.useState(null);

  const subjectsList = selectedClass === "10th" ? SUBJECT_METADATA_10TH : SUBJECT_METADATA_9TH;
  const currentSubject = subjectsList.find(s => s.id === selectedSubjectId) || subjectsList[0];

  Ee.useEffect(() => {
    setSelectedChapterNo(1);
  }, [selectedClass, selectedSubjectId]);

  // Load from master bundle or fetch
  const clsNorm = selectedClass === "10th" ? "class10" : "class9";
  const masterKey = `${clsNorm}_${selectedSubjectId}_ch${selectedChapterNo}`;
  const windowMasterNotes = (typeof window !== "undefined" && window.__PTBB_MASTER_NOTES__) || {};
  const localChapterData = windowMasterNotes[masterKey] || windowMasterNotes[`${selectedClass}-${selectedSubjectId}_ch${selectedChapterNo}`];

  Ee.useEffect(() => {
    if (!localChapterData) {
      setLoadingNotes(true);
      fetch(`/api/notes/${clsNorm}/${selectedSubjectId}/${selectedChapterNo}`)
        .then(r => r.json())
        .then(data => {
          setRemoteNotes(data);
          setLoadingNotes(false);
        })
        .catch(() => setLoadingNotes(false));
    } else {
      setRemoteNotes(null);
    }
  }, [clsNorm, selectedSubjectId, selectedChapterNo, localChapterData]);

  const chapterData = localChapterData || remoteNotes || {
    titleEn: `Unit ${selectedChapterNo}`,
    titleUr: `یونٹ ${selectedChapterNo}`,
    summaryEn: "Comprehensive solved PTBB board revision notes.",
    summaryUr: "پنجاب ٹیکسٹ بک بورڈ کے سرکاری نصاب کے مطابق جامع حل شدہ نوٹس۔",
    mcqs: [],
    shortQuestions: [],
    comprehensive_topics: []
  };

  const mcqs = chapterData.mcqs || [];
  const shortQuestions = chapterData.shortQuestions || chapterData.short_questions || [];
  const topics = chapterData.comprehensive_topics || [];

  // Filter based on search query
  const qClean = searchQuery.toLowerCase().trim();
  const filteredMcqs = Ee.useMemo(() => {
    if (!qClean) return mcqs;
    return mcqs.filter(m => 
      (m.statementEn || m.questionEn || "").toLowerCase().includes(qClean) ||
      (m.statementUr || m.questionUr || "").includes(qClean) ||
      (m.explanationEn || "").toLowerCase().includes(qClean) ||
      (m.optionsEn || []).some(opt => opt.toLowerCase().includes(qClean))
    );
  }, [mcqs, qClean]);

  const filteredShorts = Ee.useMemo(() => {
    if (!qClean) return shortQuestions;
    return shortQuestions.filter(s => 
      (s.statementEn || s.questionEn || "").toLowerCase().includes(qClean) ||
      (s.statementUr || s.questionUr || "").includes(qClean) ||
      (s.answerEn || "").toLowerCase().includes(qClean) ||
      (s.answerUr || "").includes(qClean)
    );
  }, [shortQuestions, qClean]);

  // Print handlers
  const handlePrint = (filterMode = "all") => {
    setPrintFilter(filterMode);
    setTimeout(() => {
      window.print();
    }, 150);
  };

  // Download MS Word .doc
  const handleDownloadDoc = () => {
    const el = document.getElementById("notes-printable-container");
    if (!el) return;
    const htmlContent = `
      <html xmlns:o='urn:schemas-microsoft-com:office:office' xmlns:w='urn:schemas-microsoft-com:office:word' xmlns='http://www.w3.org/TR/REC-html40'>
      <head><meta charset='utf-8'><title>${currentSubject.nameEn}_Unit_${selectedChapterNo}_Notes</title>
      <style>
        body { font-family: 'Segoe UI', Arial, sans-serif; margin: 1.5cm; }
        h1, h2, h3 { color: #0f172a; }
        .mcq-box { border-bottom: 1px solid #cbd5e1; padding: 8px 0; margin-bottom: 8px; }
        .sq-box { border-left: 3px solid #2563eb; padding-left: 10px; margin-bottom: 12px; }
      </style>
      </head>
      <body>${el.innerHTML}</body>
      </html>
    `;
    const blob = new Blob(['\\ufeff' + htmlContent], { type: 'application/msword' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = `PTBB_Class_${selectedClass}_${currentSubject.nameEn}_Unit_${selectedChapterNo}_Solved_Notes.doc`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  };

  // Copy notes to clipboard
  const handleCopyNotes = () => {
    let copyText = `PTBB OFFICIAL SOLVED NOTES - CLASS ${selectedClass.toUpperCase()}\\n`;
    copyText += `Subject: ${currentSubject.nameEn} (${currentSubject.nameUr})\\n`;
    copyText += `Unit ${selectedChapterNo}: ${chapterData.titleEn} (${chapterData.titleUr})\\n\\n`;
    copyText += `=== SECTION A: SOLVED MCQS ===\\n`;
    filteredMcqs.forEach((m, idx) => {
      copyText += `Q.${idx + 1}: ${m.statementEn || m.questionEn}\\n`;
      if (m.statementUr || m.questionUr) copyText += `${m.statementUr || m.questionUr}\\n`;
      (m.options || []).forEach((opt, oIdx) => {
        const key = opt.key || ["A", "B", "C", "D"][oIdx];
        copyText += `   (${key}) ${opt.textEn || opt} | ${opt.textUr || ""}\\n`;
      });
      copyText += `Correct: (${m.correctOption || "A"})\\nExplanation: ${m.explanationEn || ""}\\n\\n`;
    });
    copyText += `\\n=== SECTION B: SOLVED SHORT QUESTIONS ===\\n`;
    filteredShorts.forEach((s, idx) => {
      copyText += `Q.${idx + 1}: ${s.statementEn || s.questionEn} [2 Marks]\\n`;
      if (s.statementUr || s.questionUr) copyText += `${s.statementUr || s.questionUr}\\n`;
      copyText += `Ans: ${s.answerEn || ""}\\n${s.answerUr || ""}\\n\\n`;
    });

    navigator.clipboard.writeText(copyText).then(() => {
      setCopySuccess(true);
      setTimeout(() => setCopySuccess(false), 2500);
    });
  };

  return l.jsxs("div", {
    className: "space-y-6 max-w-7xl mx-auto font-sans text-slate-800",
    children: [
      // Top Control Bar
      l.jsxs("div", {
        className: "bg-white p-4 sm:p-6 rounded-2xl border border-slate-200 shadow-sm no-print space-y-5",
        children: [
          // Header & Back Button
          l.jsxs("div", {
            className: "flex flex-wrap items-center justify-between gap-3 border-b border-slate-100 pb-4",
            children: [
              l.jsxs("div", {
                className: "flex items-center gap-3",
                children: [
                  l.jsx("button", {
                    type: "button",
                    onClick: onBack,
                    className: "btn-3d flex items-center gap-1.5 px-3.5 py-2 bg-slate-100 text-slate-700 hover:text-slate-900 rounded-xl text-xs font-bold cursor-pointer border border-slate-200",
                    title: "Return to Main Dashboard",
                    children: [
                      l.jsx("span", { children: "←" }),
                      l.jsx("span", { children: "Back to Dashboard" })
                    ]
                  }),
                  l.jsxs("div", {
                    children: [
                      l.jsxs("h1", {
                        className: "text-lg sm:text-2xl font-black text-slate-900 tracking-tight flex items-center gap-2",
                        children: [
                          l.jsx("span", { className: "text-purple-600", children: "📚" }),
                          l.jsx("span", { children: "PTBB Official Solved Notes" }),
                          l.jsx("span", { className: "text-xs font-extrabold px-2 py-0.5 rounded-full bg-purple-100 text-purple-800 border border-purple-200", children: "9th & 10th Class" })
                        ]
                      }),
                      l.jsx("p", {
                        className: "text-xs text-slate-500 font-medium",
                        children: "Authentic chapter-by-chapter solved MCQs & Short Questions with complete board solutions for teachers and students"
                      })
                    ]
                  })
                ]
              }),
              // Action Buttons
              l.jsxs("div", {
                className: "flex items-center gap-2 flex-wrap",
                children: [
                  l.jsxs("button", {
                    type: "button",
                    onClick: () => handlePrint("all"),
                    className: "btn-3d btn-3d-purple flex items-center gap-1.5 px-3.5 py-2 text-white rounded-xl text-xs font-black cursor-pointer shadow-sm",
                    title: "Print Complete Notes for Classroom Distribution",
                    children: [
                      l.jsx("span", { children: "🖨️" }),
                      l.jsx("span", { children: "Print Complete Notes" })
                    ]
                  }),
                  l.jsxs("button", {
                    type: "button",
                    onClick: handleDownloadDoc,
                    className: "btn-3d flex items-center gap-1.5 px-3.5 py-2 bg-blue-50 text-blue-800 border border-blue-200 hover:bg-blue-100 rounded-xl text-xs font-black cursor-pointer shadow-xs",
                    title: "Download Editable Word Document (.doc)",
                    children: [
                      l.jsx("span", { children: "📄" }),
                      l.jsx("span", { children: "Download Word (.doc)" })
                    ]
                  }),
                  l.jsxs("button", {
                    type: "button",
                    onClick: handleCopyNotes,
                    className: `btn-3d flex items-center gap-1.5 px-3 py-2 rounded-xl text-xs font-bold cursor-pointer border transition-all ${copySuccess ? "bg-emerald-600 text-white border-emerald-700" : "bg-slate-100 text-slate-700 border-slate-200 hover:bg-slate-200"}`,
                    title: "Copy clean text to clipboard",
                    children: [
                      l.jsx("span", { children: copySuccess ? "✓" : "📋" }),
                      l.jsx("span", { children: copySuccess ? "Copied Successfully!" : "Copy Notes" })
                    ]
                  })
                ]
              })
            ]
          }),

          // Class Selector Line
          l.jsxs("div", {
            className: "flex items-center gap-3 flex-wrap",
            children: [
              l.jsx("span", { className: "text-xs font-black text-slate-700 uppercase tracking-wider", children: "Select Class:" }),
              l.jsxs("button", {
                type: "button",
                onClick: () => setSelectedClass("9th"),
                className: `px-4 py-2 rounded-xl text-xs font-extrabold cursor-pointer transition-all ${selectedClass === "9th" ? "bg-gradient-to-r from-blue-700 to-indigo-700 text-white shadow-md border-2 border-blue-500 scale-[1.02]" : "bg-slate-100 text-slate-700 hover:bg-slate-200 border border-slate-200"}`,
                children: [l.jsx("span", { children: "📘 Class 9th (Matric Part-I)" })]
              }),
              l.jsxs("button", {
                type: "button",
                onClick: () => setSelectedClass("10th"),
                className: `px-4 py-2 rounded-xl text-xs font-extrabold cursor-pointer transition-all ${selectedClass === "10th" ? "bg-gradient-to-r from-purple-700 to-pink-700 text-white shadow-md border-2 border-purple-500 scale-[1.02]" : "bg-slate-100 text-slate-700 hover:bg-slate-200 border border-slate-200"}`,
                children: [l.jsx("span", { children: "📙 Class 10th (Matric Part-II)" })]
              })
            ]
          }),

          // Subjects Horizontal Line
          l.jsxs("div", {
            className: "space-y-1.5",
            children: [
              l.jsx("div", { className: "text-xs font-black text-slate-700 uppercase tracking-wider", children: "Select Book / Subject:" }),
              l.jsx("div", {
                className: "flex items-center gap-2 overflow-x-auto pb-2 scrollbar-none",
                children: subjectsList.map(sub => 
                  l.jsxs("button", {
                    key: sub.id,
                    type: "button",
                    onClick: () => setSelectedSubjectId(sub.id),
                    className: `flex items-center gap-1.5 px-3 py-2 rounded-xl text-xs font-bold whitespace-nowrap shrink-0 cursor-pointer transition-all border ${selectedSubjectId === sub.id ? "bg-slate-900 text-white border-slate-950 shadow-md ring-2 ring-purple-400/40" : "bg-white text-slate-700 border-slate-200 hover:bg-slate-50"}`,
                    children: [
                      l.jsx("span", { children: sub.icon }),
                      l.jsx("span", { children: sub.nameEn }),
                      l.jsx("span", { className: "text-[10px] opacity-75 font-normal", children: `(${sub.chaptersCount} Ch)` })
                    ]
                  })
                )
              })
            ]
          }),

          // Chapters Horizontal Grid
          l.jsxs("div", {
            className: "space-y-1.5",
            children: [
              l.jsxs("div", {
                className: "flex items-center justify-between",
                children: [
                  l.jsxs("div", { className: "text-xs font-black text-slate-700 uppercase tracking-wider", children: ["Select Chapter / Unit for ", currentSubject.nameEn, ":"] }),
                  l.jsxs("span", { className: "text-xs text-purple-700 font-bold", children: ["Active Unit: ", selectedChapterNo, " of ", currentSubject.chaptersCount] })
                ]
              }),
              l.jsx("div", {
                className: "flex items-center gap-1.5 overflow-x-auto pb-1 scrollbar-none",
                children: Array.from({ length: currentSubject.chaptersCount }, (_, i) => i + 1).map(chNum => 
                  l.jsxs("button", {
                    key: chNum,
                    type: "button",
                    onClick: () => setSelectedChapterNo(chNum),
                    className: `px-3.5 py-1.5 rounded-xl text-xs font-black shrink-0 cursor-pointer transition-all border ${selectedChapterNo === chNum ? "bg-purple-700 text-white border-purple-800 shadow-sm ring-2 ring-purple-300" : "bg-slate-50 text-slate-700 border-slate-200 hover:bg-purple-50 hover:text-purple-900"}`,
                    children: ["Unit ", chNum]
                  })
                )
              })
            ]
          }),

          // Filter & Search Controls
          l.jsxs("div", {
            className: "pt-2 border-t border-slate-100 flex flex-wrap items-center justify-between gap-3",
            children: [
              // Section Filter Tabs
              l.jsxs("div", {
                className: "segmented-control",
                children: [
                  l.jsxs("button", {
                    type: "button",
                    onClick: () => setSectionFilter("all"),
                    className: `segmented-btn ${sectionFilter === "all" ? "segmented-btn-active" : "segmented-btn-inactive"}`,
                    children: [l.jsx("span", { children: "All Notes" }), l.jsx("span", { className: "text-[10px] opacity-75", children: `(${mcqs.length + shortQuestions.length})` })]
                  }),
                  l.jsxs("button", {
                    type: "button",
                    onClick: () => setSectionFilter("mcqs"),
                    className: `segmented-btn ${sectionFilter === "mcqs" ? "segmented-btn-active" : "segmented-btn-inactive"}`,
                    children: [l.jsx("span", { children: "MCQs Only" }), l.jsx("span", { className: "text-[10px] opacity-75", children: `(${mcqs.length})` })]
                  }),
                  l.jsxs("button", {
                    type: "button",
                    onClick: () => setSectionFilter("shorts"),
                    className: `segmented-btn ${sectionFilter === "shorts" ? "segmented-btn-active" : "segmented-btn-inactive"}`,
                    children: [l.jsx("span", { children: "Short Questions" }), l.jsx("span", { className: "text-[10px] opacity-75", children: `(${shortQuestions.length})` })]
                  }),
                  l.jsx("button", {
                    type: "button",
                    onClick: () => setSectionFilter("theory"),
                    className: `segmented-btn ${sectionFilter === "theory" ? "segmented-btn-active" : "segmented-btn-inactive"}`,
                    children: "Summary & Formulas"
                  })
                ]
              }),

              // Language Mode Switcher
              l.jsxs("div", {
                className: "flex items-center gap-1 text-xs font-bold text-slate-700",
                children: [
                  l.jsx("span", { className: "text-slate-500 mr-1", children: "View:" }),
                  l.jsx("button", {
                    type: "button",
                    onClick: () => setLanguageView("bilingual"),
                    className: `px-2.5 py-1 rounded-lg border text-xs cursor-pointer ${languageView === "bilingual" ? "bg-purple-100 text-purple-900 border-purple-300 font-extrabold" : "bg-white text-slate-600 border-slate-200"}`,
                    children: "Bilingual"
                  }),
                  l.jsx("button", {
                    type: "button",
                    onClick: () => setLanguageView("english"),
                    className: `px-2.5 py-1 rounded-lg border text-xs cursor-pointer ${languageView === "english" ? "bg-purple-100 text-purple-900 border-purple-300 font-extrabold" : "bg-white text-slate-600 border-slate-200"}`,
                    children: "English Only"
                  }),
                  l.jsx("button", {
                    type: "button",
                    onClick: () => setLanguageView("urdu"),
                    className: `px-2.5 py-1 rounded-lg border text-xs cursor-pointer ${languageView === "urdu" ? "bg-purple-100 text-purple-900 border-purple-300 font-extrabold" : "bg-white text-slate-600 border-slate-200"}`,
                    children: "اردو میڈیم"
                  })
                ]
              }),

              // Search Box
              l.jsxs("div", {
                className: "relative w-full sm:w-64",
                children: [
                  l.jsx("input", {
                    type: "text",
                    value: searchQuery,
                    onChange: e => setSearchQuery(e.target.value),
                    placeholder: "Search question or formula...",
                    className: "w-full pl-8 pr-3 py-1.5 text-xs font-medium border border-slate-300 rounded-xl focus:border-purple-600 focus:outline-none bg-slate-50"
                  }),
                  l.jsx("span", { className: "absolute left-2.5 top-2 text-slate-400 text-xs", children: "🔍" }),
                  searchQuery && l.jsx("button", {
                    type: "button",
                    onClick: () => setSearchQuery(""),
                    className: "absolute right-2.5 top-1.5 text-slate-400 hover:text-slate-600 text-xs font-bold cursor-pointer",
                    children: "✕"
                  })
                ]
              })
            ]
          })
        ]
      }),

      // PRINT & PREVIEW CONTAINER
      l.jsxs("div", {
        id: "notes-printable-container",
        className: "bg-white p-6 sm:p-10 rounded-2xl border border-slate-200 shadow-md relative overflow-hidden",
        children: [
          // Printable Document Header
          l.jsxs("div", {
            className: "border-b-2 border-black pb-4 mb-6 text-center space-y-1.5",
            children: [
              l.jsx("h1", {
                className: "text-xl sm:text-2xl font-black text-black uppercase tracking-tight",
                children: (currentUser == null ? void 0 : currentUser.schoolName) || "PUNJAB BOARD CENTRAL REVISION ACADEMY"
              }),
              l.jsxs("div", {
                className: "text-xs font-bold text-slate-800 flex items-center justify-center gap-2 flex-wrap",
                children: [
                  l.jsx("span", { children: (currentUser == null ? void 0 : currentUser.campusName) || "Campus Office" }),
                  l.jsx("span", { children: "•" }),
                  l.jsxs("span", { children: ["Class: ", selectedClass, " Matriculation"] }),
                  l.jsx("span", { children: "•" }),
                  l.jsxs("span", { children: ["Subject: ", currentSubject.nameEn, " (", currentSubject.nameUr, ")"] })
                ]
              }),
              l.jsxs("div", {
                className: "inline-block bg-slate-100 border border-black px-4 py-1 rounded-full text-xs font-black text-black mt-1",
                children: [
                  "UNIT ", selectedChapterNo, ": ", chapterData.titleEn,
                  chapterData.titleUr ? ` • ${chapterData.titleUr}` : ""
                ]
              }),
              // Student Info Fields for Teachers & Classroom Practice
              l.jsxs("div", {
                className: "pt-2 mt-2 border-t border-slate-300 grid grid-cols-2 sm:grid-cols-4 gap-2 text-[11px] font-bold text-slate-700 text-left",
                children: [
                  l.jsx("div", { children: "Student Name: ________________" }),
                  l.jsx("div", { children: "Roll Number: ________________" }),
                  l.jsx("div", { children: "Date: ________________________" }),
                  l.jsxs("div", { children: ["Total MCQs: ", mcqs.length, " | SQs: ", shortQuestions.length] })
                ]
              })
            ]
          }),

          // Chapter Conceptual Summary & SLOs Banner
          (sectionFilter === "all" || sectionFilter === "theory") && l.jsxs("div", {
            className: "bg-purple-50 border border-purple-200 rounded-xl p-4 mb-6 space-y-2 break-inside-avoid",
            children: [
              l.jsxs("div", {
                className: "flex items-center justify-between",
                children: [
                  l.jsx("h2", { className: "text-xs font-black text-purple-950 uppercase tracking-wider", children: "📘 Chapter Conceptual Overview & Learning Outcomes:" }),
                  l.jsx("span", { className: "text-[10px] font-bold px-2 py-0.5 rounded bg-purple-200 text-purple-900", children: "Official PTBB Curriculum 2026" })
                ]
              }),
              (languageView === "bilingual" || languageView === "english") && l.jsx("p", {
                className: "text-xs text-slate-800 leading-relaxed font-medium",
                children: chapterData.summaryEn
              }),
              (languageView === "bilingual" || languageView === "urdu") && l.jsx("p", {
                className: "text-xs text-slate-800 font-urdu leading-loose text-right",
                dir: "rtl",
                children: chapterData.summaryUr
              })
            ]
          }),

          // SECTION A: SOLVED MULTIPLE CHOICE QUESTIONS (MCQs) - FIRST!
          (sectionFilter === "all" || sectionFilter === "mcqs") && (printFilter === "all" || printFilter === "mcqs") && l.jsxs("div", {
            className: "space-y-4 mb-8",
            children: [
              // Section Title Header
              l.jsxs("div", {
                className: "border-b-2 border-slate-900 pb-2 flex items-center justify-between",
                children: [
                  l.jsxs("h2", {
                    className: "text-sm sm:text-base font-black text-slate-950 flex items-center gap-2",
                    children: [
                      l.jsx("span", { className: "w-6 h-6 rounded-md bg-blue-700 text-white flex items-center justify-center text-xs", children: "A" }),
                      l.jsx("span", { children: "SECTION - A: SOLVED MULTIPLE CHOICE QUESTIONS (MCQs)" })
                    ]
                  }),
                  l.jsxs("div", {
                    className: "text-xs font-black text-blue-700 no-print flex items-center gap-2",
                    children: [
                      l.jsxs("span", { children: [filteredMcqs.length, " Solved Questions"] }),
                      l.jsxs("button", {
                        type: "button",
                        onClick: () => handlePrint("mcqs"),
                        className: "px-2 py-0.5 bg-blue-100 hover:bg-blue-200 text-blue-800 rounded text-[11px] font-bold cursor-pointer",
                        children: ["🖨️ Print MCQs Only"]
                      })
                    ]
                  })
                ]
              }),

              // MCQs Grid / List
              filteredMcqs.length === 0 ? l.jsx("div", { className: "text-center py-6 text-xs text-slate-400", children: "No MCQs match the current search filter." }) :
              l.jsx("div", {
                className: "space-y-3",
                children: filteredMcqs.map((mcq, idx) => 
                  l.jsxs("div", {
                    key: mcq.id || idx,
                    className: "border border-slate-300 p-3.5 rounded-xl bg-white break-inside-avoid space-y-2 shadow-2xs",
                    children: [
                      // Question Statement
                      l.jsxs("div", {
                        className: "flex items-start justify-between gap-3",
                        children: [
                          l.jsxs("div", {
                            className: "space-y-1 flex-1",
                            children: [
                              (languageView === "bilingual" || languageView === "english") && l.jsxs("div", {
                                className: "font-black text-xs text-slate-900 leading-snug",
                                children: [
                                  l.jsx("span", { className: "text-blue-700 mr-1.5 font-mono", children: `Q.${idx + 1}` }),
                                  mcq.statementEn || mcq.questionEn
                                ]
                              }),
                              (languageView === "bilingual" || languageView === "urdu") && (mcq.statementUr || mcq.questionUr) && l.jsx("div", {
                                className: "font-urdu text-xs text-slate-900 leading-loose text-right",
                                dir: "rtl",
                                children: mcq.statementUr || mcq.questionUr
                              })
                            ]
                          }),
                          l.jsxs("span", {
                            className: "shrink-0 px-2.5 py-0.5 rounded-full bg-emerald-100 text-emerald-900 border border-emerald-300 text-[11px] font-black tracking-wide",
                            children: [
                              "Ans: ", mcq.correctOption || "A"
                            ]
                          })
                        ]
                      }),

                      // 4 Options (A, B, C, D)
                      l.jsx("div", {
                        className: "grid grid-cols-1 sm:grid-cols-2 gap-1.5 pt-1",
                        children: (mcq.options || []).map((opt, oIdx) => {
                          const key = opt.key || ["A", "B", "C", "D"][oIdx];
                          const isCorrect = key === mcq.correctOption;
                          const textEn = opt.textEn || (typeof opt === "string" ? opt : "");
                          const textUr = opt.textUr || "";
                          return l.jsxs("div", {
                            key: key,
                            className: `flex items-center justify-between px-3 py-1.5 rounded-lg border text-xs font-semibold ${isCorrect ? "bg-emerald-50 border-emerald-400 text-emerald-950 ring-1 ring-emerald-300" : "bg-slate-50 border-slate-200 text-slate-700"}`,
                            children: [
                              l.jsxs("div", {
                                className: "flex items-center gap-1.5 min-w-0",
                                children: [
                                  l.jsx("span", { className: `w-5 h-5 rounded-full flex items-center justify-center font-black text-[10px] ${isCorrect ? "bg-emerald-600 text-white" : "bg-slate-200 text-slate-700"}`, children: key }),
                                  (languageView === "bilingual" || languageView === "english") && l.jsx("span", { className: "truncate", children: textEn })
                                ]
                              }),
                              (languageView === "bilingual" || languageView === "urdu") && textUr && l.jsx("span", { className: "font-urdu text-[11px] text-right shrink-0", dir: "rtl", children: textUr })
                            ]
                          });
                        })
                      }),

                      // Solved Board Explanation
                      (mcq.explanationEn || mcq.explanationUr) && l.jsxs("div", {
                        className: "bg-slate-50 border-l-2 border-emerald-500 pl-2.5 py-1 text-[11px] text-slate-600 space-y-0.5",
                        children: [
                          (languageView === "bilingual" || languageView === "english") && mcq.explanationEn && l.jsxs("div", {
                            children: [l.jsx("strong", { className: "text-slate-800", children: "Key Explanation: " }), mcq.explanationEn]
                          }),
                          (languageView === "bilingual" || languageView === "urdu") && mcq.explanationUr && l.jsx("div", {
                            className: "font-urdu text-right text-slate-700",
                            dir: "rtl",
                            children: mcq.explanationUr
                          })
                        ]
                      })
                    ]
                  })
                )
              })
            ]
          }),

          // SECTION B: SOLVED SHORT QUESTIONS (2 MARKS) - SECOND!
          (sectionFilter === "all" || sectionFilter === "shorts") && (printFilter === "all" || printFilter === "shorts") && l.jsxs("div", {
            className: "space-y-4 mb-8",
            children: [
              // Section Title Header
              l.jsxs("div", {
                className: "border-b-2 border-slate-900 pb-2 flex items-center justify-between",
                children: [
                  l.jsxs("h2", {
                    className: "text-sm sm:text-base font-black text-slate-950 flex items-center gap-2",
                    children: [
                      l.jsx("span", { className: "w-6 h-6 rounded-md bg-purple-700 text-white flex items-center justify-center text-xs", children: "B" }),
                      l.jsx("span", { children: "SECTION - B: SOLVED SHORT QUESTIONS (2 MARKS EACH)" })
                    ]
                  }),
                  l.jsxs("div", {
                    className: "text-xs font-black text-purple-700 no-print flex items-center gap-2",
                    children: [
                      l.jsxs("span", { children: [filteredShorts.length, " Solved Questions"] }),
                      l.jsxs("button", {
                        type: "button",
                        onClick: () => handlePrint("shorts"),
                        className: "px-2 py-0.5 bg-purple-100 hover:bg-purple-200 text-purple-800 rounded text-[11px] font-bold cursor-pointer",
                        children: ["🖨️ Print Shorts Only"]
                      })
                    ]
                  })
                ]
              }),

              // Short Questions List
              filteredShorts.length === 0 ? l.jsx("div", { className: "text-center py-6 text-xs text-slate-400", children: "No short questions match the current search filter." }) :
              l.jsx("div", {
                className: "space-y-3.5",
                children: filteredShorts.map((sq, idx) => 
                  l.jsxs("div", {
                    key: sq.id || idx,
                    className: "border border-slate-300 p-4 rounded-xl bg-white break-inside-avoid space-y-2 shadow-2xs",
                    children: [
                      // Question Statement & Marks Badge
                      l.jsxs("div", {
                        className: "flex items-start justify-between gap-3 border-b border-slate-100 pb-2",
                        children: [
                          l.jsxs("div", {
                            className: "space-y-1 flex-1",
                            children: [
                              (languageView === "bilingual" || languageView === "english") && l.jsxs("div", {
                                className: "font-black text-xs sm:text-sm text-slate-900 leading-snug",
                                children: [
                                  l.jsx("span", { className: "text-purple-700 mr-1.5 font-mono", children: `Q.${idx + 1}` }),
                                  sq.statementEn || sq.questionEn
                                ]
                              }),
                              (languageView === "bilingual" || languageView === "urdu") && (sq.statementUr || sq.questionUr) && l.jsx("div", {
                                className: "font-urdu text-xs sm:text-sm text-slate-900 leading-loose text-right",
                                dir: "rtl",
                                children: sq.statementUr || sq.questionUr
                              })
                            ]
                          }),
                          l.jsx("span", {
                            className: "shrink-0 px-2 py-0.5 rounded bg-slate-100 text-slate-800 border border-slate-300 text-[10px] font-mono font-black",
                            children: "[2 Marks]"
                          })
                        ]
                      }),

                      // Solved Model Board Answer
                      l.jsxs("div", {
                        className: "bg-slate-50 border-l-3 border-purple-600 p-3 rounded-r-lg space-y-1.5",
                        children: [
                          l.jsx("div", { className: "text-[10px] font-black uppercase tracking-wider text-purple-900", children: "✓ Standard Board Model Answer:" }),
                          (languageView === "bilingual" || languageView === "english") && sq.answerEn && l.jsx("div", {
                            className: "text-xs text-slate-800 font-medium leading-relaxed whitespace-pre-line",
                            children: sq.answerEn
                          }),
                          (languageView === "bilingual" || languageView === "urdu") && sq.answerUr && l.jsx("div", {
                            className: "text-xs text-slate-800 font-urdu leading-loose text-right whitespace-pre-line",
                            dir: "rtl",
                            children: sq.answerUr
                          })
                        ]
                      })
                    ]
                  })
                )
              })
            ]
          }),

          // SECTION C: KEY TOPICS, LAWS & DETAILED REVISION POINTS
          (sectionFilter === "all" || sectionFilter === "theory") && topics.length > 0 && l.jsxs("div", {
            className: "space-y-4 mb-6",
            children: [
              l.jsxs("div", {
                className: "border-b-2 border-slate-900 pb-2",
                children: [
                  l.jsxs("h2", {
                    className: "text-sm sm:text-base font-black text-slate-950 flex items-center gap-2",
                    children: [
                      l.jsx("span", { className: "w-6 h-6 rounded-md bg-emerald-700 text-white flex items-center justify-center text-xs", children: "C" }),
                      l.jsx("span", { children: "SECTION - C: CORE THEORETICAL TOPICS & GOVERNING LAWS" })
                    ]
                  })
                ]
              }),
              l.jsx("div", {
                className: "grid grid-cols-1 md:grid-cols-2 gap-3.5",
                children: topics.map((top, idx) => 
                  l.jsxs("div", {
                    key: top.topicNo || idx,
                    className: "border border-slate-200 p-4 rounded-xl bg-slate-50/70 break-inside-avoid space-y-2",
                    children: [
                      l.jsxs("h3", {
                        className: "font-black text-xs text-slate-900 flex items-center justify-between",
                        children: [
                          l.jsxs("span", { children: [top.topicNo || (idx + 1), ". ", top.titleEn] }),
                          top.titleUr && l.jsx("span", { className: "font-urdu text-[11px] text-slate-600", children: top.titleUr })
                        ]
                      }),
                      l.jsx("p", { className: "text-xs text-slate-700 leading-relaxed font-medium", children: top.contentEn }),
                      top.keyPointsEn && top.keyPointsEn.length > 0 && l.jsx("ul", {
                        className: "list-disc pl-4 text-[11px] text-slate-600 space-y-0.5",
                        children: top.keyPointsEn.map((pt, pIdx) => l.jsx("li", { key: pIdx, children: pt }))
                      })
                    ]
                  })
                )
              })
            ]
          }),

          // Institutional Footer on Printed Notes
          l.jsxs("div", {
            className: "pt-4 mt-8 border-t border-slate-300 text-center text-[10px] text-slate-500 font-medium space-y-1",
            children: [
              l.jsxs("div", { children: ["Punjab Textbook Board (PTBB / BISE Punjab Pattern) Official Solved Curriculum Series • Class ", selectedClass, " ", currentSubject.nameEn] }),
              l.jsx("div", { children: "All Questions and Solutions Strictly Verified Against Punjab Curriculum and Textbook Board Lahore" })
            ]
          })
        ]
      })
    ]
  });
};
'''

# Check if NotesPortalComponent already defined in text
if "const NotesPortalComponent =" not in text:
    pos_cq = text.find('function cq()')
    if pos_cq != -1:
        text = text[:pos_cq] + notes_portal_code + "\n" + text[pos_cq:]
        print("[✓] Inserted NotesPortalComponent before function cq()")
    else:
        print("[!] Could not find function cq()")
else:
    print("[!] NotesPortalComponent already present, replacing with updated version...")
    # replace existing
    start_pos = text.find('const SUBJECT_METADATA_9TH =')
    end_pos = text.find('function cq()')
    if start_pos != -1 and end_pos != -1:
        text = text[:start_pos] + notes_portal_code + "\n" + text[end_pos:]
        print("[✓] Replaced NotesPortalComponent before function cq()")

# 2. Add "notes_portal" to Sidebar B8 navigation
old_b8_item = '{id:"question_bank",label:"Question Bank",icon:Kf,badge:"Matric 9-10",badgeColor:"bg-indigo-600 text-white"}'
new_b8_item = '{id:"question_bank",label:"Question Bank",icon:Kf,badge:"Matric 9-10",badgeColor:"bg-indigo-600 text-white"},{id:"notes_portal",label:"Notes 9th & 10th",icon:Kf,badge:"PTBB Solved",badgeColor:"bg-purple-600 text-white"}'

if old_b8_item in text:
    text = text.replace(old_b8_item, new_b8_item, 1)
    print("[✓] Added Notes 9th & 10th to Sidebar B8")
else:
    print("[!] old_b8_item already patched or not found")

# 3. Add "Notes 9th & 10th" button to top header bar across the Dashboard
old_header_btns = 'l.jsx("div",{className:"flex items-center gap-2 shrink-0",children:m?l.jsxs("button",{type:"button",onClick:Ke,className:"btn-3d btn-3d-rose'
new_header_btns = 'l.jsxs("div",{className:"flex items-center gap-2 shrink-0",children:[l.jsxs("button",{type:"button",onClick:()=>{e("notes_portal");o(!1)},className:"btn-3d btn-3d-purple flex items-center gap-1.5 px-3 py-1.5 sm:px-3.5 sm:py-2 text-white rounded-xl text-xs font-black cursor-pointer shadow-sm hover:scale-[1.02] transition-transform",title:"Official PTBB Solved Notes for Class 9th & 10th (MCQs & Short Questions)",children:[l.jsxs("svg",{className:"w-4 h-4 text-purple-200",viewBox:"0 0 24 24",fill:"none",stroke:"currentColor",strokeWidth:"2.2",strokeLinecap:"round",strokeLinejoin:"round",children:[l.jsx("path",{d:"M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"}),l.jsx("path",{d:"M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"})]}),l.jsx("span",{children:"Notes 9th & 10th"}),l.jsx("span",{className:"hidden md:inline-block bg-purple-900/60 text-purple-200 text-[10px] px-1.5 py-0.5 rounded-md font-bold",children:"PTBB"})]}),m?l.jsxs("button",{type:"button",onClick:Ke,className:"btn-3d btn-3d-rose'

if old_header_btns in text:
    text = text.replace(old_header_btns, new_header_btns, 1)
    print("[✓] Added Notes 9th & 10th button to Header Bar")
else:
    print("[!] old_header_btns already patched or not found")

# 4. Add "Notes 9th & 10th" to Dashboard m8 Action Cards Line
old_m8_cards = 'l.jsxs("div",{className:"grid grid-cols-2 sm:grid-cols-4 gap-4",children:['
new_m8_cards = '''l.jsxs("div",{className:"grid grid-cols-2 sm:grid-cols-5 gap-3.5",children:[l.jsxs("div",{onClick:()=>C&&C("notes_portal"),className:"card-3d p-4 flex flex-col justify-between cursor-pointer hover:border-purple-400 hover:shadow-md transition-all group bg-gradient-to-b from-white to-purple-50/40",title:"Open Official PTBB Solved Notes for 9th and 10th Classes",children:[l.jsxs("div",{className:"flex items-center justify-between mb-1",children:[l.jsx("span",{className:"text-[11px] font-black uppercase tracking-wider text-purple-900 group-hover:text-purple-700 transition-colors",children:"Notes 9th & 10th"}),l.jsx("div",{className:"w-8 h-8 rounded-lg bg-purple-600 text-white flex items-center justify-center shadow-xs shrink-0 group-hover:scale-110 transition-transform",children:l.jsxs("svg",{className:"w-4 h-4 text-white",viewBox:"0 0 24 24",fill:"none",stroke:"currentColor",strokeWidth:"2.2",strokeLinecap:"round",strokeLinejoin:"round",children:[l.jsx("path",{d:"M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"}),l.jsx("path",{d:"M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"})]})})]}),l.jsx("div",{className:"text-base font-black text-slate-950 mt-1",children:"Solved Notes"}),l.jsx("span",{className:"text-[11px] text-purple-700 font-bold mt-0.5 group-hover:underline",children:"168 Chapters (MCQs & SQs) →"})]}),'''

if old_m8_cards in text:
    text = text.replace(old_m8_cards, new_m8_cards, 1)
    print("[✓] Added Notes 9th & 10th Card to Dashboard m8 Line")
else:
    print("[!] old_m8_cards already patched or not found")

# 5. Add n === "notes_portal" to main routing
old_main_router = 'n==="dashboard"&&l.jsx(AppTabErrorBoundary'
new_main_router = 'n==="notes_portal"&&l.jsx(AppTabErrorBoundary,{onReset:()=>e("dashboard"),children:l.jsx(NotesPortalComponent,{currentUser:m,onBack:()=>e("dashboard")})}),n==="dashboard"&&l.jsx(AppTabErrorBoundary'

if old_main_router in text:
    text = text.replace(old_main_router, new_main_router, 1)
    print("[✓] Added notes_portal tab handler to main view router")
else:
    print("[!] old_main_router already patched or not found")

# Verify syntax
if verify_syntax(text, "Final Patched Bundle with Notes Portal"):
    with open('assets/index-DAioIUjd.js', 'w', encoding='utf-8') as f_out:
        f_out.write(text)
    print("SUCCESS: assets/index-DAioIUjd.js updated cleanly!")
else:
    print("FAILED: Syntax errors found. Bundle was not modified.")
    exit(1)
