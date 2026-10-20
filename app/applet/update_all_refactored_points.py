import subprocess
import os

print("--- Starting Full UI/UX Refactoring ---")

with open('assets/index-DAioIUjd.js', 'r', encoding='utf-8') as f:
    text = f.read()

def verify(label):
    global text
    with open('test_verify.js', 'w', encoding='utf-8') as f:
        f.write(text)
    res = subprocess.run(['node', '--check', 'test_verify.js'], capture_output=True, text=True)
    if res.returncode != 0:
        print(f"FAILED AT: {label}")
        print(res.stderr[:400])
        exit(1)
    else:
        print(f"PASSED: {label}")

verify("Baseline check")

# =========================================================================
# 1. TOP NAVIGATION & HEADER BAR CLEANUP
# =========================================================================
# Find exact boundaries of right side header
pos_h = text.find('bg-white border-b border-slate-200 px-3 sm:px-6 py-2.5 sm:py-3.5')
if pos_h != -1:
    pos_right_start = text.find('l.jsxs("div",{className:"flex items-center gap-1.5 sm:gap-2 shrink-0"', pos_h)
    pos_right_end = text.find('children:"Login"})]})', pos_right_start) + len('children:"Login"})]})')
    
    clean_header_right = 'l.jsxs("div",{className:"flex items-center gap-2 shrink-0",children:[m?l.jsxs("button",{type:"button",onClick:Ke,className:"btn-3d btn-3d-rose flex items-center gap-1.5 px-3.5 py-2 text-white rounded-xl text-xs font-black cursor-pointer shadow-sm hover:opacity-95 transition-all",title:"Direct Logout",children:[l.jsxs("svg",{className:"w-3.5 h-3.5 text-white",viewBox:"0 0 24 24",fill:"none",stroke:"currentColor",strokeWidth:"2.2",strokeLinecap:"round",strokeLinejoin:"round",children:[l.jsx("path",{d:"M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"}),l.jsx("polyline",{points:"16 17 21 12 16 7"}),l.jsx("line",{x1:"21",x2:"9",y1:"12",y2:"12"})]}),l.jsx("span",{children:"Logout"})]}):l.jsx("button",{type:"button",onClick:()=>R(!0),className:"btn-3d px-3.5 py-2 text-white font-black rounded-xl text-xs cursor-pointer",style:{backgroundColor:"#2563eb",border:"1px solid #1d4ed8",color:"#ffffff"},children:"Login"})]})'
    
    text = text[:pos_right_start] + clean_header_right + text[pos_right_end:]
    verify("1. Top Navigation & Header Bar Cleanup (Clean Logout Only)")

# =========================================================================
# 2. STANDARDIZATION: RECENT GENERATED PAPERS 3-DOTS ACTION MENU
# =========================================================================
pos_saved = text.find('Recent Generated Question Papers')
if pos_saved != -1:
    pos_btns = text.find('View Paper', pos_saved)
    pos_div_start = text.rfind('l.jsxs("div",{className:"flex items-center', 0, pos_btns)
    pos_div_end = text.find(']})]},y.id))', pos_btns) + len(']})')
    
    clean_recent_btns = 'l.jsxs("div",{className:"flex items-center gap-2 shrink-0",children:[l.jsx("button",{type:"button",onClick:()=>A(y),className:"btn-3d btn-3d-blue px-3.5 py-1.5 text-white rounded-xl font-black text-xs cursor-pointer shadow-xs",children:"View Paper"}),l.jsxs("details",{className:"relative inline-block text-left no-print",children:[l.jsx("summary",{className:"p-2 rounded-xl border border-slate-300 hover:bg-slate-100 text-slate-700 cursor-pointer list-none select-none transition-colors",title:"More actions",children:l.jsxs("svg",{className:"w-4 h-4",viewBox:"0 0 24 24",fill:"none",stroke:"currentColor",strokeWidth:"2.2",strokeLinecap:"round",strokeLinejoin:"round",children:[l.jsx("circle",{cx:"12",cy:"12",r:"1.5"}),l.jsx("circle",{cx:"19",cy:"12",r:"1.5"}),l.jsx("circle",{cx:"5",cy:"12",r:"1.5"})]})}),l.jsxs("div",{className:"dropdown-menu-panel right-0 min-w-[12rem]",children:[l.jsxs("button",{type:"button",onClick:evt=>{evt.currentTarget.closest("details")?.removeAttribute("open");z0(y);},className:"dropdown-menu-item text-blue-700 hover:bg-blue-50",children:[l.jsx(Xu,{className:"w-3.5 h-3.5 text-blue-600"}),l.jsx("span",{children:"MS Word (.doc)"})]}),l.jsxs("button",{type:"button",onClick:evt=>{evt.currentTarget.closest("details")?.removeAttribute("open");B(y);},className:"dropdown-menu-item text-emerald-700 hover:bg-emerald-50",children:[l.jsx("span",{className:"w-3.5 h-3.5 flex items-center justify-center font-bold text-emerald-600",children:"🔑"}),l.jsx("span",{children:"Answer Key"})]}),l.jsxs("button",{type:"button",onClick:evt=>{evt.currentTarget.closest("details")?.removeAttribute("open");f(y);},className:"dropdown-menu-item text-purple-700 hover:bg-purple-50",children:[l.jsx("span",{className:"w-3.5 h-3.5 flex items-center justify-center font-bold text-purple-600",children:"📝"}),l.jsx("span",{children:"Bubble Sheet"})]}),m&&l.jsxs("button",{type:"button",onClick:evt=>{evt.currentTarget.closest("details")?.removeAttribute("open");window.confirm(`Are you sure you want to delete "${y.header.subjectName}" paper?`)&&m(y.id);},className:"dropdown-menu-item text-rose-700 hover:bg-rose-50 border-t border-slate-100",children:[l.jsx(Ql,{className:"w-3.5 h-3.5 text-rose-600"}),l.jsx("span",{children:"Delete Paper"})]})]})]})]})'
    
    text = text[:pos_div_start] + clean_recent_btns + text[pos_div_end:]
    verify("2. Action Buttons in Recent Papers List (Consolidated 3-dots Menu)")

# =========================================================================
# 3. STRICT 100% ENGLISH UI LOCALIZATION
# =========================================================================
if 'titleEn:"Dynamics (قوت اور حرکت)"' in text:
    text = text.replace('titleEn:"Dynamics (قوت اور حرکت)"', 'titleEn:"Dynamics"')
if 'subjectName:"Physics (طبیعیات)"' in text:
    text = text.replace('subjectName:"Physics (طبیعیات)"', 'subjectName:"Physics"')

verify("3. Strict English UI Localization (Removed Urdu Subtitles from Metadata)")

# =========================================================================
# 4. EXAM & TEST TYPE SELECTION IN CREATE PAPER (XK Step 6)
# =========================================================================
old_xk_exam = 'l.jsxs("div",{children:[l.jsx("label",{className:"block text-xs font-black text-slate-800 mb-1",children:"Exam Title:"}),l.jsx("input",{type:"text",value:me,onChange:Oe=>ue(Oe.target.value),className:"w-full px-3 py-2 border-2 border-slate-300 rounded-xl font-bold text-slate-900 focus:border-blue-600 focus:outline-none"})]})'

new_xk_exam = 'l.jsxs("div",{className:"space-y-1.5",children:[l.jsx("label",{className:"block text-xs font-black text-slate-800 mb-1",children:"Exam & Test Type:"}),l.jsxs("select",{value:["Annual Examination","1st Term Examination","2nd Term Examination","Mid-Term Examination","December Test Session","Send-Up Examination","Pre-Board Examination","Weekly Test Series","Monthly Assessment"].includes(me)?me:"Custom Title",onChange:Oe=>{const val=Oe.target.value;if(val==="Custom Title"){if(["Annual Examination","1st Term Examination","2nd Term Examination","Mid-Term Examination","December Test Session","Send-Up Examination","Pre-Board Examination","Weekly Test Series","Monthly Assessment"].includes(me))ue("");}else{ue(val);}},className:"w-full px-3 py-2 border-2 border-slate-300 rounded-xl font-bold text-slate-900 bg-white focus:border-blue-600 focus:outline-none shadow-xs",children:[l.jsx("option",{value:"Annual Examination",children:"Annual Examination"}),l.jsx("option",{value:"1st Term Examination",children:"1st Term Examination"}),l.jsx("option",{value:"2nd Term Examination",children:"2nd Term Examination"}),l.jsx("option",{value:"Mid-Term Examination",children:"Mid-Term Examination"}),l.jsx("option",{value:"December Test Session",children:"December Test Session"}),l.jsx("option",{value:"Send-Up Examination",children:"Send-Up Examination"}),l.jsx("option",{value:"Pre-Board Examination",children:"Pre-Board Examination"}),l.jsx("option",{value:"Weekly Test Series",children:"Weekly Test Series"}),l.jsx("option",{value:"Monthly Assessment",children:"Monthly Assessment"}),l.jsx("option",{value:"Custom Title",children:"Custom Title..."})]}),(!["Annual Examination","1st Term Examination","2nd Term Examination","Mid-Term Examination","December Test Session","Send-Up Examination","Pre-Board Examination","Weekly Test Series","Monthly Assessment"].includes(me))&&l.jsx("input",{type:"text",value:me,onChange:Oe=>ue(Oe.target.value),placeholder:"Enter custom exam title (e.g. Grand Test Session 2026)...",className:"w-full px-3 py-2 mt-1.5 border-2 border-blue-400 rounded-xl font-bold text-slate-900 focus:border-blue-600 focus:outline-none"})]})'

if old_xk_exam in text:
    text = text.replace(old_xk_exam, new_xk_exam, 1)
    verify("4. Exam & Test Type Selector in Create Paper (XK Step 6)")

# =========================================================================
# 5. EXAM & TEST TYPE SELECTION IN MANUAL BUILDER (y8 Step 5)
# =========================================================================
old_y8_exam = 'l.jsxs("div",{children:[l.jsx("label",{className:"block font-bold text-slate-700 mb-1",children:"Exam Title"}),l.jsx("input",{type:"text",value:Be,onChange:Ie=>xe(Ie.target.value),className:"w-full px-3 py-2 bg-white border border-slate-300 rounded-lg font-semibold"})]})'

new_y8_exam = 'l.jsxs("div",{className:"space-y-1.5",children:[l.jsx("label",{className:"block font-bold text-slate-700 mb-1",children:"Exam & Test Type:"}),l.jsxs("select",{value:["Annual Examination","1st Term Examination","2nd Term Examination","Mid-Term Examination","December Test Session","Send-Up Examination","Pre-Board Examination","Weekly Test Series","Monthly Assessment"].includes(Be)?Be:"Custom Title",onChange:Ie=>{const val=Ie.target.value;if(val==="Custom Title"){if(["Annual Examination","1st Term Examination","2nd Term Examination","Mid-Term Examination","December Test Session","Send-Up Examination","Pre-Board Examination","Weekly Test Series","Monthly Assessment"].includes(Be))xe("");}else{xe(val);}},className:"w-full px-3 py-2 bg-white border border-slate-300 rounded-lg font-bold text-slate-900 focus:border-blue-600 focus:outline-none shadow-xs",children:[l.jsx("option",{value:"Annual Examination",children:"Annual Examination"}),l.jsx("option",{value:"1st Term Examination",children:"1st Term Examination"}),l.jsx("option",{value:"2nd Term Examination",children:"2nd Term Examination"}),l.jsx("option",{value:"Mid-Term Examination",children:"Mid-Term Examination"}),l.jsx("option",{value:"December Test Session",children:"December Test Session"}),l.jsx("option",{value:"Send-Up Examination",children:"Send-Up Examination"}),l.jsx("option",{value:"Pre-Board Examination",children:"Pre-Board Examination"}),l.jsx("option",{value:"Weekly Test Series",children:"Weekly Test Series"}),l.jsx("option",{value:"Monthly Assessment",children:"Monthly Assessment"}),l.jsx("option",{value:"Custom Title",children:"Custom Title..."})]}),(!["Annual Examination","1st Term Examination","2nd Term Examination","Mid-Term Examination","December Test Session","Send-Up Examination","Pre-Board Examination","Weekly Test Series","Monthly Assessment"].includes(Be))&&l.jsx("input",{type:"text",value:Be,onChange:Ie=>xe(Ie.target.value),placeholder:"Enter custom exam title (e.g. Grand Test Session 2026)...",className:"w-full px-3 py-2 mt-1.5 border border-blue-400 rounded-lg font-bold text-slate-900 focus:border-blue-600 focus:outline-none"})]})'

if old_y8_exam in text:
    text = text.replace(old_y8_exam, new_y8_exam, 1)
    verify("5. Exam & Test Type Selector in Manual Builder (y8 Step 5)")

# Write updated bundle
with open('assets/index-DAioIUjd.js', 'w', encoding='utf-8') as f:
    f.write(text)

print("SUCCESS: assets/index-DAioIUjd.js updated and verified!")
EOF
