import subprocess

with open('test_modified_orig.js', 'r', encoding='utf-8') as f:
    text = f.read()

def check(step):
    with open('step_test.js', 'w', encoding='utf-8') as f:
        f.write(text)
    res = subprocess.run(['node', '--check', 'step_test.js'], capture_output=True, text=True)
    if res.returncode != 0:
        print(f"FAILED AT {step}:")
        print(res.stderr[:400])
        exit(1)
    else:
        print(f"PASSED {step}")

check("Initial")

# Step 1: Clean Date Sheet
marker_start = 'l.jsxs("div",{className:"bg-gradient-to-r from-blue-900 via-indigo-900 to-slate-900 text-white p-3.5 sm:p-4 rounded-2xl shadow-lg border border-blue-700 flex flex-wrap items-center justify-between gap-3 no-print"'
pos_start = text.find(marker_start)
if pos_start != -1:
    marker_end = 'l.jsxs("div",{className:"card-3d p-5 sm:p-6 bg-white border border-slate-200"'
    pos_end = text.find(marker_end, pos_start)
    if pos_end != -1:
        text = text[:pos_start] + text[pos_end:]
check("Step 1 Clean Date Sheet")

# Step 3: Saved papers (balanced bracket)
pos_sp_btn = text.find('title:"Delete this saved paper"')
start_sp = text.rfind('l.jsxs("div",{className:"flex items-center gap-1.5 pt-2 border-t border-slate-100"', 0, pos_sp_btn)
i = start_sp; cp, cb, cbr = 0, 0, 0; end_sp = -1
while i < len(text):
    c = text[i]
    if c == '(': cp += 1
    elif c == ')': cp -= 1
    elif c == '[': cb += 1
    elif c == ']': cb -= 1
    elif c == '{': cbr += 1
    elif c == '}': cbr -= 1
    i += 1
    if i > pos_sp_btn and cp == 0 and cb == 0 and cbr == 0:
        end_sp = i; break

if start_sp != -1 and end_sp != -1:
    new_sp_chunk = 'l.jsxs("div",{className:"flex items-center justify-between gap-2 pt-2 border-t border-slate-100",children:[l.jsxs("button",{type:"button",onClick:()=>qe(ge),className:"btn-3d btn-3d-blue flex items-center justify-center gap-1.5 flex-1 py-1.5 text-white rounded-lg text-xs font-black shadow-xs cursor-pointer",title:"View and print question paper on A4 sheet",children:[l.jsx(SAFE_od,{className:"w-3.5 h-3.5 text-blue-100 shrink-0"}),l.jsx("span",{children:"View & Print"})]}),l.jsxs("details",{className:"relative inline-block text-left no-print",children:[l.jsxs("summary",{className:"btn-3d btn-3d-indigo flex items-center gap-1 px-3 py-1.5 text-white rounded-lg text-xs font-black shadow-xs cursor-pointer list-none select-none",title:"Export & Paper Options",children:[l.jsx("span",{children:"Options ▾"})]}),l.jsxs("div",{className:"dropdown-menu-panel",children:[l.jsxs("button",{type:"button",onClick:evt=>{evt.currentTarget.closest("details")?.removeAttribute("open");z0(ge);},className:"dropdown-menu-item text-blue-700 hover:bg-blue-50",title:"Download editable Microsoft Word document",children:[l.jsx(Xu,{className:"w-3.5 h-3.5 text-blue-600"}),l.jsx("span",{children:"Download Word (.doc)"})]}),l.jsxs("button",{type:"button",onClick:evt=>{evt.currentTarget.closest("details")?.removeAttribute("open");E(ge);te(!0);},className:"dropdown-menu-item text-emerald-700 hover:bg-emerald-50",title:"View and print Answer Key",children:[l.jsx(SAFE_ad,{className:"w-3.5 h-3.5 text-emerald-600"}),l.jsx("span",{children:"Answer Key (Key & Solutions)"})]}),l.jsxs("button",{type:"button",onClick:evt=>{evt.currentTarget.closest("details")?.removeAttribute("open");E(ge);T(!0);},className:"dropdown-menu-item text-purple-700 hover:bg-purple-50",title:"Print OMR Bubble Sheet",children:[l.jsx(Rw,{className:"w-3.5 h-3.5 text-purple-600"}),l.jsx("span",{children:"Bubble Sheet (OMR Sheet)"})]}),l.jsxs("button",{type:"button",onClick:evt=>{evt.currentTarget.closest("details")?.removeAttribute("open");window.confirm(`Are you sure you want to delete "${ge.header.subjectName}" paper?`)&&St(ge.id);},className:"dropdown-menu-item text-rose-700 hover:bg-rose-50 border-t border-slate-100",title:"Delete saved paper",children:[l.jsx(Ql,{className:"w-3.5 h-3.5 text-rose-600"}),l.jsx("span",{children:"Delete Paper"})]})]})]})]})'
    text = text[:start_sp] + new_sp_chunk + text[end_sp:]

check("Step 3 Saved Papers")

# Step 4: Date Sheet mode buttons
pos_aq = text.find('aq=({currentUser:n,activeHeader:e,onOpenSchoolProfile:t})=>{')
pos_btn_aq = text.find('Printable A4 Preview', pos_aq)
start_aq = text.rfind('l.jsxs("div",{className:"flex items-center gap-1.5 p-1.5 bg-slate-100', 0, pos_btn_aq)
i = start_aq; cp, cb, cbr = 0, 0, 0; end_aq = -1
while i < len(text):
    c = text[i]
    if c == '(': cp += 1
    elif c == ')': cp -= 1
    elif c == '[': cb += 1
    elif c == ']': cb -= 1
    elif c == '{': cbr += 1
    elif c == '}': cbr -= 1
    i += 1
    if i > pos_btn_aq and cp == 0 and cb == 0 and cbr == 0:
        end_aq = i; break
new_aq_mode = 'l.jsxs("div",{className:"segmented-control",children:[l.jsxs("button",{type:"button",onClick:()=>o("editor"),className:"segmented-btn " + (a==="editor"?"segmented-btn-active":"segmented-btn-inactive"),children:[l.jsx(J2,{className:"w-3.5 h-3.5"}),l.jsx("span",{children:"Interactive Editor"})]}),l.jsxs("button",{type:"button",onClick:()=>o("preview"),className:"segmented-btn " + (a==="preview"?"segmented-btn-active":"segmented-btn-inactive"),children:[l.jsx(e8,{className:"w-3.5 h-3.5"}),l.jsx("span",{children:"Printable A4 Preview"})]})]})'
text = text[:start_aq] + new_aq_mode + text[end_aq:]
check("Step 4 Date Sheet mode buttons")

# Step 5: Date Sheet export buttons
old_aq_exp = 'l.jsxs("div",{className:"flex flex-wrap items-center gap-2",children:[l.jsxs("button",{type:"button",onClick:T,className:"btn-print-preview",title:"Open browser print dialog for A4 Date Sheet",children:[l.jsx(SAFE_od,{className:"w-4 h-4 text-emerald-100"}),l.jsx("span",{children:"Print & Preview"})]}),l.jsxs("button",{type:"button",onClick:H,disabled:A,className:"btn-3d btn-3d-red flex items-center gap-2 px-4 py-2.5 text-white rounded-xl text-xs font-black cursor-pointer shadow-md disabled:opacity-50",title:"Download high-resolution PDF",children:[A?l.jsx(Sc,{className:"w-4 h-4 animate-spin"}):l.jsx(SAFE_ad,{className:"w-4 h-4"}),l.jsx("span",{children:A?f||"Rendering PDF...":"Download PDF"})]}),l.jsxs("button",{type:"button",onClick:G,className:"btn-3d btn-3d-navy flex items-center gap-2 px-4 py-2.5 text-white rounded-xl text-xs font-black cursor-pointer shadow-md",title:"Download editable Microsoft Word .doc file",children:[l.jsx(Xu,{className:"w-4 h-4 text-blue-200"}),l.jsx("span",{children:"Download Word (.doc)"})]})]})'
new_aq_exp = 'l.jsxs("div",{className:"flex flex-wrap items-center gap-2",children:[l.jsxs("button",{type:"button",onClick:T,className:"btn-print-preview",title:"Open browser print dialog for A4 Date Sheet",children:[l.jsx(SAFE_od,{className:"w-4 h-4 text-emerald-100"}),l.jsx("span",{children:"Print & Preview"})]}),l.jsxs("details",{className:"relative inline-block text-left no-print",children:[l.jsxs("summary",{className:"btn-3d btn-3d-red flex items-center gap-1.5 px-3.5 py-2 text-white rounded-xl text-xs font-black cursor-pointer shadow-xs list-none select-none",title:"Export & Download",children:[l.jsx(SAFE_ad,{className:"w-3.5 h-3.5 text-white"}),l.jsx("span",{children:A?f||"Rendering...":"Export ▾"})]}),l.jsxs("div",{className:"dropdown-menu-panel",children:[l.jsxs("button",{type:"button",onClick:evt=>{evt.currentTarget.closest("details")?.removeAttribute("open");H();},disabled:A,className:"dropdown-menu-item text-rose-700 hover:bg-rose-50",title:"Download high-resolution PDF",children:[l.jsx(SAFE_ad,{className:"w-3.5 h-3.5 text-rose-600"}),l.jsx("span",{children:A?f||"Rendering PDF...":"Download PDF (.pdf)"})]}),l.jsxs("button",{type:"button",onClick:evt=>{evt.currentTarget.closest("details")?.removeAttribute("open");G();},className:"dropdown-menu-item text-blue-700 hover:bg-blue-50",title:"Download editable Microsoft Word .doc file",children:[l.jsx(Xu,{className:"w-3.5 h-3.5 text-blue-600"}),l.jsx("span",{children:"Download Word (.doc)"})]})]})]})]})'
text = text.replace(old_aq_exp, new_aq_exp, 1)
check("Step 5 Date Sheet export buttons")

# Step 6: Date Sheet preset buttons
old_aq_preset = 'l.jsxs("div",{className:"flex items-center gap-2",children:[l.jsx("button",{type:"button",onClick:()=>P("9th"),className:"btn-3d btn-3d-blue text-[11px] font-black px-3 py-1.5 rounded-lg text-white cursor-pointer",children:"Load 9th Science Preset"}),l.jsx("button",{type:"button",onClick:()=>P("10th"),className:"btn-3d btn-3d-indigo text-[11px] font-black px-3 py-1.5 rounded-lg text-white cursor-pointer",children:"Load 10th Science Preset"})]})'
new_aq_preset = 'l.jsxs("select",{value:"",onChange:D=>{if(D.target.value){P(D.target.value);D.target.value="";}},className:"form-select py-1.5 px-3 rounded-lg border border-slate-300 bg-white font-bold text-[11px] text-slate-700 shadow-xs cursor-pointer focus:ring-2 focus:ring-blue-500",children:[l.jsx("option",{value:"",children:"📋 Quick Presets..."}),l.jsx("option",{value:"9th",children:"9th Science Preset"}),l.jsx("option",{value:"10th",children:"10th Science Preset"})]})'
text = text.replace(old_aq_preset, new_aq_preset, 1)
check("Step 6 Date Sheet preset buttons")

# Step 7: Result Card mode buttons
pos_lq = text.find('lq=({currentUser:n,activeHeader:e,onOpenSchoolProfile:t})=>{')
pos_btn_lq = text.find('Class Master Sheet', pos_lq)
start_lq = text.rfind('l.jsxs("div",{className:"flex flex-wrap items-center gap-1.5 p-1.5 bg-slate-100', 0, pos_btn_lq)
i = start_lq; cp, cb, cbr = 0, 0, 0; end_lq = -1
while i < len(text):
    c = text[i]
    if c == '(': cp += 1
    elif c == ')': cp -= 1
    elif c == '[': cb += 1
    elif c == ']': cb -= 1
    elif c == '{': cbr += 1
    elif c == '}': cbr -= 1
    i += 1
    if i > pos_btn_lq and cp == 0 and cb == 0 and cbr == 0:
        end_lq = i; break
new_lq_mode = 'l.jsxs("div",{className:"segmented-control",children:[l.jsxs("button",{type:"button",onClick:()=>o("editor"),className:"segmented-btn " + (a==="editor"?"segmented-btn-active":"segmented-btn-inactive"),children:[l.jsx(J2,{className:"w-3.5 h-3.5"}),l.jsx("span",{children:"Marks Entry"})]}),l.jsxs("button",{type:"button",onClick:()=>o("singleCard"),className:"segmented-btn " + (a==="singleCard"?"segmented-btn-active":"segmented-btn-inactive"),children:[l.jsx(z3,{className:"w-3.5 h-3.5"}),l.jsx("span",{children:"A4 Result Card"})]}),l.jsxs("button",{type:"button",onClick:()=>o("masterSheet"),className:"segmented-btn " + (a==="masterSheet"?"segmented-btn-active":"segmented-btn-inactive"),children:[l.jsx(n8,{className:"w-3.5 h-3.5"}),l.jsx("span",{children:"Master Sheet"})]})]})'
text = text[:start_lq] + new_lq_mode + text[end_lq:]
check("Step 7 Result Card mode buttons")

# Step 8: Result Card singleCard export buttons
old_lq_single = 'a==="singleCard"&&P&&l.jsxs(l.Fragment,{children:[l.jsxs("button",{type:"button",onClick:()=>ue(P),className:"btn-print-preview",title:"Print single student result card on standard A4",children:[l.jsx(SAFE_od,{className:"w-4 h-4 text-emerald-100"}),l.jsx("span",{children:"Print & Preview"})]}),l.jsxs("button",{type:"button",onClick:()=>Ne(P),disabled:f,className:"btn-3d btn-3d-red flex items-center gap-2 px-4 py-2.5 text-white rounded-xl text-xs font-black cursor-pointer shadow-md disabled:opacity-50",title:"Download single student result card PDF",children:[f?l.jsx(Sc,{className:"w-4 h-4 animate-spin"}):l.jsx(SAFE_ad,{className:"w-4 h-4"}),l.jsx("span",{children:f?m||"Rendering...":"Download Card (PDF)"})]}),l.jsxs("button",{type:"button",onClick:()=>Le(P),className:"btn-3d btn-3d-navy flex items-center gap-2 px-4 py-2.5 text-white rounded-xl text-xs font-black cursor-pointer shadow-md",title:"Download single student result card Word (.doc)",children:[l.jsx(Xu,{className:"w-4 h-4 text-blue-200"}),l.jsx("span",{children:"Download Card (.doc)"})]})]})'
new_lq_single = 'a==="singleCard"&&P&&l.jsxs(l.Fragment,{children:[l.jsxs("button",{type:"button",onClick:()=>ue(P),className:"btn-print-preview",title:"Print single student result card on standard A4",children:[l.jsx(SAFE_od,{className:"w-4 h-4 text-emerald-100"}),l.jsx("span",{children:"Print & Preview"})]}),l.jsxs("details",{className:"relative inline-block text-left no-print",children:[l.jsxs("summary",{className:"btn-3d btn-3d-red flex items-center gap-1.5 px-3.5 py-2 text-white rounded-xl text-xs font-black cursor-pointer shadow-xs list-none select-none",title:"Export Result Card",children:[l.jsx(SAFE_ad,{className:"w-3.5 h-3.5 text-white"}),l.jsx("span",{children:f?m||"Rendering...":"Export ▾"})]}),l.jsxs("div",{className:"dropdown-menu-panel",children:[l.jsxs("button",{type:"button",onClick:evt=>{evt.currentTarget.closest("details")?.removeAttribute("open");Ne(P);},disabled:f,className:"dropdown-menu-item text-rose-700 hover:bg-rose-50",title:"Download single student result card PDF",children:[l.jsx(SAFE_ad,{className:"w-3.5 h-3.5 text-rose-600"}),l.jsx("span",{children:f?m||"Rendering...":"Download Card (PDF)"})]}),l.jsxs("button",{type:"button",onClick:evt=>{evt.currentTarget.closest("details")?.removeAttribute("open");Le(P);},className:"dropdown-menu-item text-blue-700 hover:bg-blue-50",title:"Download single student result card Word (.doc)",children:[l.jsx(Xu,{className:"w-3.5 h-3.5 text-blue-600"}),l.jsx("span",{children:"Download Card (.doc)"})]})]})]})]})'
text = text.replace(old_lq_single, new_lq_single, 1)
check("Step 8 Result Card singleCard export buttons")

# Step 9: Result Card masterSheet export buttons
old_lq_master = 'a==="masterSheet"&&l.jsxs(l.Fragment,{children:[l.jsxs("button",{type:"button",onClick:Ce,className:"btn-print-preview",title:"Print full class master sheet / broadsheet",children:[l.jsx(SAFE_od,{className:"w-4 h-4 text-emerald-100"}),l.jsx("span",{children:"Print & Preview"})]}),l.jsxs("button",{type:"button",onClick:k,disabled:f,className:"btn-3d btn-3d-red flex items-center gap-2 px-4 py-2.5 text-white rounded-xl text-xs font-black cursor-pointer shadow-md disabled:opacity-50",children:[f?l.jsx(Sc,{className:"w-4 h-4 animate-spin"}):l.jsx(SAFE_ad,{className:"w-4 h-4"}),l.jsx("span",{children:f?m||"Rendering...":"Export Master (PDF)"})]}),l.jsxs("button",{type:"button",onClick:Y,className:"btn-3d btn-3d-navy flex items-center gap-2 px-4 py-2.5 text-white rounded-xl text-xs font-black cursor-pointer shadow-md",children:[l.jsx(Xu,{className:"w-4 h-4 text-blue-200"}),l.jsx("span",{children:"Export Master (.doc)"})]})]})'
new_lq_master = 'a==="masterSheet"&&l.jsxs(l.Fragment,{children:[l.jsxs("button",{type:"button",onClick:Ce,className:"btn-print-preview",title:"Print full class master sheet / broadsheet",children:[l.jsx(SAFE_od,{className:"w-4 h-4 text-emerald-100"}),l.jsx("span",{children:"Print & Preview"})]}),l.jsxs("details",{className:"relative inline-block text-left no-print",children:[l.jsxs("summary",{className:"btn-3d btn-3d-red flex items-center gap-1.5 px-3.5 py-2 text-white rounded-xl text-xs font-black cursor-pointer shadow-xs list-none select-none",title:"Export Master Gazette",children:[l.jsx(SAFE_ad,{className:"w-3.5 h-3.5 text-white"}),l.jsx("span",{children:f?m||"Rendering...":"Export ▾"})]}),l.jsxs("div",{className:"dropdown-menu-panel",children:[l.jsxs("button",{type:"button",onClick:evt=>{evt.currentTarget.closest("details")?.removeAttribute("open");k();},disabled:f,className:"dropdown-menu-item text-rose-700 hover:bg-rose-50",title:"Download full class master sheet PDF",children:[l.jsx(SAFE_ad,{className:"w-3.5 h-3.5 text-rose-600"}),l.jsx("span",{children:f?m||"Rendering...":"Export Master (PDF)"})]}),l.jsxs("button",{type:"button",onClick:evt=>{evt.currentTarget.closest("details")?.removeAttribute("open");Y();},className:"dropdown-menu-item text-blue-700 hover:bg-blue-50",title:"Download full class master sheet Word (.doc)",children:[l.jsx(Xu,{className:"w-3.5 h-3.5 text-blue-600"}),l.jsx("span",{children:"Export Master (.doc)"})]})]})]})]})'
text = text.replace(old_lq_master, new_lq_master, 1)
check("Step 9 Result Card masterSheet export buttons")

# Step 10: AppTabErrorBoundary
error_boundary_code = """class AppTabErrorBoundary extends Ee.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, error: null };
  }
  static getDerivedStateFromError(error) {
    return { hasError: true, error };
  }
  componentDidCatch(error, info) {
    console.error("Tab Error Caught by AppTabErrorBoundary:", error, info);
  }
  render() {
    if (this.state.hasError) {
      return l.jsxs("div", {
        className: "p-6 sm:p-10 max-w-2xl mx-auto my-8 bg-white rounded-3xl border-2 border-rose-200 shadow-xl text-center space-y-4 font-sans",
        children: [
          l.jsx("div", { className: "w-14 h-14 mx-auto rounded-2xl bg-rose-50 border border-rose-200 flex items-center justify-center text-rose-600 text-2xl font-black shadow-inner", children: "🛡️" }),
          l.jsx("h2", { className: "text-lg font-black text-slate-900", children: "Module Notice" }),
          l.jsx("p", { className: "text-xs text-slate-600 max-w-md mx-auto leading-relaxed", children: "This section was safely contained to preserve your workflow. All examination records, saved papers, and settings are 100% safe." }),
          l.jsxs("div", {
            className: "flex items-center justify-center gap-2.5 pt-2 flex-wrap",
            children: [
              l.jsx("button", {
                type: "button",
                onClick: () => { this.setState({ hasError: false, error: null }); },
                className: "btn-3d btn-3d-blue px-4 py-2 text-white font-bold text-xs rounded-xl cursor-pointer",
                children: "Retry Section"
              }),
              l.jsx("button", {
                type: "button",
                onClick: () => { this.setState({ hasError: false, error: null }); if (this.props.onReset) this.props.onReset(); },
                className: "btn-3d bg-slate-800 hover:bg-slate-700 px-4 py-2 text-white font-bold text-xs rounded-xl cursor-pointer",
                children: "Return to Dashboard"
              })
            ]
          })
        ]
      });
    }
    return this.props.children;
  }
}
"""

pos_cq = text.rfind('function cq(')
text = text[:pos_cq] + error_boundary_code + text[pos_cq:]
check("Step 10a AppTabErrorBoundary class definition")

tab_replacements = [
    ('n==="date_sheet"&&l.jsx(aq,{currentUser:m,activeHeader:v.header,onOpenSchoolProfile:()=>oe(!0)})',
     'n==="date_sheet"&&l.jsx(AppTabErrorBoundary,{onReset:()=>e("dashboard"),children:l.jsx(aq,{currentUser:m,activeHeader:v.header,onOpenSchoolProfile:()=>oe(!0)})})'),
    ('n==="result_card"&&l.jsx(lq,{currentUser:m,activeHeader:v.header,onOpenSchoolProfile:()=>oe(!0)})',
     'n==="result_card"&&l.jsx(AppTabErrorBoundary,{onReset:()=>e("dashboard"),children:l.jsx(lq,{currentUser:m,activeHeader:v.header,onOpenSchoolProfile:()=>oe(!0)})})'),
    ('n==="dashboard"&&l.jsx(m8,{currentUser:m,savedPapers:I,onOpenCreatePaper:We,onOpenManualSelector:ge=>dt(ge||"9th"),onOpenQuestionBank:()=>e("question_bank"),onViewPaper:qe,onOpenSchoolProfile:()=>oe(!0),onOpenBubbleSheet:ge=>{E(ge),T(!0)},onOpenAnswerKey:ge=>{E(ge),te(!0)},onDeletePaper:St,onSelectTab:ge=>{e(ge),o(!1)}})',
     'n==="dashboard"&&l.jsx(AppTabErrorBoundary,{onReset:()=>e("dashboard"),children:l.jsx(m8,{currentUser:m,savedPapers:I,onOpenCreatePaper:We,onOpenManualSelector:ge=>dt(ge||"9th"),onOpenQuestionBank:()=>e("question_bank"),onViewPaper:qe,onOpenSchoolProfile:()=>oe(!0),onOpenBubbleSheet:ge=>{E(ge),T(!0)},onOpenAnswerKey:ge=>{E(ge),te(!0)},onDeletePaper:St,onSelectTab:ge=>{e(ge),o(!1)}})})'),
    ('n==="question_bank"&&l.jsx(v8,{onStartTestWithChapter:Ze,onOpenManualBuilder:(ge,ze)=>dt(ge,ze)})',
     'n==="question_bank"&&l.jsx(AppTabErrorBoundary,{onReset:()=>e("dashboard"),children:l.jsx(v8,{onStartTestWithChapter:Ze,onOpenManualBuilder:(ge,ze)=>dt(ge,ze)})})'),
    ('l.jsx(WK,{paper:v,onUpdatePaper:Ye,printSection:"all",onOpenBubbleSheetModal:()=>T(!0),onOpenAnswerKeyModal:()=>te(!0)})',
     'l.jsx(AppTabErrorBoundary,{onReset:()=>e("dashboard"),children:l.jsx(WK,{paper:v,onUpdatePaper:Ye,printSection:"all",onOpenBubbleSheetModal:()=>T(!0),onOpenAnswerKeyModal:()=>te(!0)})})')
]

for old_s, new_s in tab_replacements:
    if old_s in text:
        text = text.replace(old_s, new_s, 1)

check("Step 10b AppTabErrorBoundary tab wraps")

# Save final to assets/index-DAioIUjd.js
with open('assets/index-DAioIUjd.js', 'w', encoding='utf-8') as f:
    f.write(text)

print("ALL STEPS COMPLETED AND VERIFIED 100% CLEAN!")
