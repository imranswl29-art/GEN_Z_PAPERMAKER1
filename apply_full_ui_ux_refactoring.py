import subprocess
import os

with open('assets/index-DAioIUjd.js', 'r', encoding='utf-8') as f:
    text = f.read()

def check(step_name):
    global text
    with open('step_test.js', 'w', encoding='utf-8') as f:
        f.write(text)
    res = subprocess.run(['node', '--check', 'step_test.js'], capture_output=True, text=True)
    if res.returncode != 0:
        print(f"FAILED AT {step_name}:")
        print(res.stderr[:500])
        exit(1)
    else:
        print(f"PASSED {step_name}")

check("Initial Check")

# =========================================================================
# STEP 1: Top Navigation & Header Bar Cleanup
# =========================================================================
old_header_right = 'l.jsxs("div",{className:"flex items-center gap-1.5 sm:gap-2 shrink-0",children:[l.jsxs("button",{onClick:()=>dt("9th"),className:"btn-3d btn-3d-indigo flex items-center gap-1.5 px-3 py-2 text-white rounded-xl text-xs font-black cursor-pointer",title:"Handpick Questions Manually from Question Bank in 6 Guided Steps",children:[l.jsxs("svg",{className:"w-4 h-4 text-indigo-100",viewBox:"0 0 24 24",fill:"none",stroke:"currentColor",strokeWidth:"2.2",strokeLinecap:"round",strokeLinejoin:"round",children:[l.jsx("path",{d:"M21 10.5V19a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2v2"}),l.jsx("path",{d:"m9 11 3 3L22 4"})]}),l.jsx("span",{className:"hidden lg:inline",children:"Manual Selection"})]}),l.jsxs("button",{onClick:()=>We("9th"),className:"btn-3d btn-3d-blue flex items-center gap-1.5 px-3.5 py-2 text-white rounded-xl text-xs font-black cursor-pointer",children:[l.jsxs("svg",{className:"w-4 h-4 text-blue-100",viewBox:"0 0 24 24",fill:"none",stroke:"currentColor",strokeWidth:"2.2",strokeLinecap:"round",strokeLinejoin:"round",children:[l.jsx("path",{d:"M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z"}),l.jsx("polyline",{points:"14 2 14 8 20 8"}),l.jsx("line",{x1:"12",x2:"12",y1:"12",y2:"18"}),l.jsx("line",{x1:"9",x2:"15",y1:"15",y2:"15"})]}),l.jsx("span",{children:"New Paper"})]}),(m==null?void 0:m.role)==="admin"&&l.jsxs("button",{onClick:()=>G(!0),className:"btn-3d btn-3d-amber flex items-center gap-1.5 px-3 py-2 text-slate-950 rounded-xl text-xs font-black cursor-pointer shadow-sm",title:"Super Admin Portal",children:[l.jsxs("svg",{className:"w-4 h-4 text-slate-950",viewBox:"0 0 24 24",fill:"none",stroke:"currentColor",strokeWidth:"2.2",strokeLinecap:"round",strokeLinejoin:"round",children:[l.jsx("path",{d:"M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"}),l.jsx("path",{d:"m9 12 2 2 4-4"})]}),l.jsx("span",{className:"hidden xl:inline",children:"Admin"})]}),l.jsxs("button",{onClick:()=>oe(!0),title:"School Monogram & Details",className:"btn-3d btn-3d-amber flex items-center gap-1.5 px-3.5 py-2 rounded-xl text-xs font-black cursor-pointer shadow-sm",children:[l.jsx(SAFE_sd,{className:"w-4 h-4 text-slate-950"}),l.jsx("span",{className:"hidden xl:inline",children:"Monogram"})]}),m?l.jsxs("div",{className:"flex items-center gap-2",children:[l.jsxs("button",{onClick:()=>oe(!0),className:"flex items-center gap-2 p-1 rounded-xl hover:bg-slate-100 transition-colors cursor-pointer",title:`${m.name} (${m.schoolName})`,children:[l.jsx("div",{className:"w-8 h-8 rounded-full text-white flex items-center justify-center font-bold text-xs uppercase shadow-xs shrink-0",style:{backgroundColor:"#0f172a",color:"#ffffff"},children:m.username.slice(0,2)}),l.jsxs("div",{className:"hidden 2xl:block text-left text-xs",children:[l.jsx("div",{className:"font-extrabold text-slate-900 leading-tight truncate max-w-[120px]",children:m.name}),l.jsx("div",{className:"text-[10px] text-blue-700 font-semibold truncate max-w-[120px]",children:m.schoolName})]})]}),l.jsxs("button",{type:"button",onClick:Ke,className:"btn-3d btn-3d-rose flex items-center gap-1.5 px-3 py-2 text-white rounded-xl text-xs font-black cursor-pointer shadow-sm",title:"Direct Logout",children:[l.jsxs("svg",{className:"w-3.5 h-3.5 text-white",viewBox:"0 0 24 24",fill:"none",stroke:"currentColor",strokeWidth:"2.2",strokeLinecap:"round",strokeLinejoin:"round",children:[l.jsx("path",{d:"M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"}),l.jsx("polyline",{points:"16 17 21 12 16 7"}),l.jsx("line",{x1:"21",x2:"9",y1:"12",y2:"12"})]}),l.jsx("span",{children:"Logout"})]})]})'

new_header_right = 'l.jsxs("div",{className:"flex items-center gap-2 shrink-0",children:[m?l.jsxs("button",{type:"button",onClick:Ke,className:"btn-3d btn-3d-rose flex items-center gap-1.5 px-3.5 py-2 text-white rounded-xl text-xs font-black cursor-pointer shadow-sm hover:opacity-95 transition-all",title:"Direct Logout",children:[l.jsxs("svg",{className:"w-3.5 h-3.5 text-white",viewBox:"0 0 24 24",fill:"none",stroke:"currentColor",strokeWidth:"2.2",strokeLinecap:"round",strokeLinejoin:"round",children:[l.jsx("path",{d:"M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"}),l.jsx("polyline",{points:"16 17 21 12 16 7"}),l.jsx("line",{x1:"21",x2:"9",y1:"12",y2:"12"})]}),l.jsx("span",{children:"Logout"})]}):l.jsx("button",{type:"button",onClick:()=>R(!0),className:"btn-3d px-3.5 py-2 text-white font-black rounded-xl text-xs cursor-pointer",style:{backgroundColor:"#2563eb",border:"1px solid #1d4ed8",color:"#ffffff"},children:"Login"})]})'

if old_header_right in text:
    text = text.replace(old_header_right, new_header_right, 1)
    check("Step 1: Top Navigation & Header Bar Cleanup")
else:
    print("Warning: old_header_right not found in text!")

# =========================================================================
# STEP 2: Recent Generated Question Papers Action Buttons -> 3-dots Menu
# =========================================================================
old_recent_btns = 'l.jsxs("div",{className:"flex items-center gap-1.5 flex-wrap",children:[l.jsx("button",{onClick:()=>A(y),className:"btn-3d btn-3d-blue px-3 py-1.5 text-white rounded-lg font-bold text-[11px] cursor-pointer",children:"View Paper"}),l.jsxs("button",{onClick:()=>z0(y),className:"btn-3d btn-3d-navy flex items-center gap-1 px-3 py-1.5 text-white rounded-lg font-bold text-[11px] cursor-pointer",children:[l.jsx(Xu,{className:"w-3 h-3 text-blue-200"}),l.jsx("span",{children:"MS Word"})]}),l.jsx("button",{onClick:()=>B(y),className:"btn-3d btn-3d-emerald px-3 py-1.5 text-white rounded-lg font-bold text-[11px] cursor-pointer",children:"Answer Key"}),l.jsx("button",{onClick:()=>f(y),className:"btn-3d btn-3d-purple px-3 py-1.5 text-white rounded-lg font-bold text-[11px] cursor-pointer",children:"Bubble Sheet"}),m&&l.jsxs("button",{type:"button",onClick:()=>{window.confirm(`Are you sure you want to delete "${y.header.subjectName}" paper?`)&&m(y.id)},className:"btn-3d btn-3d-ruby flex items-center gap-1 px-2.5 py-1.5 text-white rounded-lg font-bold text-[11px] cursor-pointer",title:"Delete this paper from saved list",children:[l.jsx(Ql,{className:"w-3 h-3"}),l.jsx("span",{children:"Delete"})]})]})'

new_recent_btns = 'l.jsxs("div",{className:"flex items-center gap-2 shrink-0",children:[l.jsx("button",{type:"button",onClick:()=>A(y),className:"btn-3d btn-3d-blue px-3.5 py-1.5 text-white rounded-xl font-black text-xs cursor-pointer shadow-xs",children:"View Paper"}),l.jsxs("details",{className:"relative inline-block text-left no-print",children:[l.jsx("summary",{className:"p-2 rounded-xl border border-slate-300 hover:bg-slate-100 text-slate-700 cursor-pointer list-none select-none transition-colors",title:"More actions",children:l.jsxs("svg",{className:"w-4 h-4",viewBox:"0 0 24 24",fill:"none",stroke:"currentColor",strokeWidth:"2.2",strokeLinecap:"round",strokeLinejoin:"round",children:[l.jsx("circle",{cx:"12",cy:"12",r:"1.5"}),l.jsx("circle",{cx:"19",cy:"12",r:"1.5"}),l.jsx("circle",{cx:"5",cy:"12",r:"1.5"})]})}),l.jsxs("div",{className:"dropdown-menu-panel right-0 min-w-[12rem]",children:[l.jsxs("button",{type:"button",onClick:evt=>{evt.currentTarget.closest("details")?.removeAttribute("open");z0(y);},className:"dropdown-menu-item text-blue-700 hover:bg-blue-50",children:[l.jsx(Xu,{className:"w-3.5 h-3.5 text-blue-600"}),l.jsx("span",{children:"MS Word (.doc)"})]}),l.jsxs("button",{type:"button",onClick:evt=>{evt.currentTarget.closest("details")?.removeAttribute("open");B(y);},className:"dropdown-menu-item text-emerald-700 hover:bg-emerald-50",children:[l.jsx("span",{className:"w-3.5 h-3.5 flex items-center justify-center font-bold text-emerald-600",children:"🔑"}),l.jsx("span",{children:"Answer Key"})]}),l.jsxs("button",{type:"button",onClick:evt=>{evt.currentTarget.closest("details")?.removeAttribute("open");f(y);},className:"dropdown-menu-item text-purple-700 hover:bg-purple-50",children:[l.jsx("span",{className:"w-3.5 h-3.5 flex items-center justify-center font-bold text-purple-600",children:"📝"}),l.jsx("span",{children:"Bubble Sheet"})]}),m&&l.jsxs("button",{type:"button",onClick:evt=>{evt.currentTarget.closest("details")?.removeAttribute("open");window.confirm(`Are you sure you want to delete "${y.header.subjectName}" paper?`)&&m(y.id);},className:"dropdown-menu-item text-rose-700 hover:bg-rose-50 border-t border-slate-100",children:[l.jsx(Ql,{className:"w-3.5 h-3.5 text-rose-600"}),l.jsx("span",{children:"Delete Paper"})]})]})]})]})'

if old_recent_btns in text:
    text = text.replace(old_recent_btns, new_recent_btns, 1)
    check("Step 2: Recent Generated Question Papers Consolidated 3-dots Menu")
else:
    print("Warning: old_recent_btns not found in text!")

# =========================================================================
# STEP 3: Strict 100% English UI Localization
# =========================================================================
if 'titleEn:"Dynamics (قوت اور حرکت)"' in text:
    text = text.replace('titleEn:"Dynamics (قوت اور حرکت)"', 'titleEn:"Dynamics"')
    print("[✓] Replaced Dynamics Urdu label in titleEn")

if 'subjectName:"Physics (طبیعیات)"' in text:
    text = text.replace('subjectName:"Physics (طبیعیات)"', 'subjectName:"Physics"')
    print("[✓] Replaced Physics Urdu label in subjectName")

check("Step 3: English Localization & Urdu Subtitle Removal")

# =========================================================================
# STEP 4: Exam & Test Type Selection in Create Paper (XK Step 6)
# =========================================================================
old_xk_exam = 'l.jsxs("div",{children:[l.jsx("label",{className:"block text-xs font-black text-slate-800 mb-1",children:"Exam Title:"}),l.jsx("input",{type:"text",value:me,onChange:Oe=>ue(Oe.target.value),className:"w-full px-3 py-2 border-2 border-slate-300 rounded-xl font-bold text-slate-900 focus:border-blue-600 focus:outline-none"})]})'

new_xk_exam = '''l.jsxs("div",{className:"space-y-1.5",children:[l.jsx("label",{className:"block text-xs font-black text-slate-800 mb-1",children:"Exam & Test Type:"}),l.jsxs("select",{value:["Annual Examination","1st Term Examination","2nd Term Examination","Mid-Term Examination","December Test Session","Send-Up Examination","Pre-Board Examination","Weekly Test Series","Monthly Assessment"].includes(me)?me:"Custom Title",onChange:Oe=>{const val=Oe.target.value;if(val==="Custom Title"){if(["Annual Examination","1st Term Examination","2nd Term Examination","Mid-Term Examination","December Test Session","Send-Up Examination","Pre-Board Examination","Weekly Test Series","Monthly Assessment"].includes(me))ue("");}else{ue(val);}},className:"w-full px-3 py-2 border-2 border-slate-300 rounded-xl font-bold text-slate-900 bg-white focus:border-blue-600 focus:outline-none shadow-xs",children:[l.jsx("option",{value:"Annual Examination",children:"Annual Examination"}),l.jsx("option",{value:"1st Term Examination",children:"1st Term Examination"}),l.jsx("option",{value:"2nd Term Examination",children:"2nd Term Examination"}),l.jsx("option",{value:"Mid-Term Examination",children:"Mid-Term Examination"}),l.jsx("option",{value:"December Test Session",children:"December Test Session"}),l.jsx("option",{value:"Send-Up Examination",children:"Send-Up Examination"}),l.jsx("option",{value:"Pre-Board Examination",children:"Pre-Board Examination"}),l.jsx("option",{value:"Weekly Test Series",children:"Weekly Test Series"}),l.jsx("option",{value:"Monthly Assessment",children:"Monthly Assessment"}),l.jsx("option",{value:"Custom Title",children:"Custom Title..."})]}),(!["Annual Examination","1st Term Examination","2nd Term Examination","Mid-Term Examination","December Test Session","Send-Up Examination","Pre-Board Examination","Weekly Test Series","Monthly Assessment"].includes(me))&&l.jsx("input",{type:"text",value:me,onChange:Oe=>ue(Oe.target.value),placeholder:"Enter custom exam title (e.g. Grand Test Session 2026)...",className:"w-full px-3 py-2 mt-1.5 border-2 border-blue-400 rounded-xl font-bold text-slate-900 focus:border-blue-600 focus:outline-none"})]})'''

if old_xk_exam in text:
    text = text.replace(old_xk_exam, new_xk_exam, 1)
    check("Step 4: Exam & Test Type Selection in Create Paper (XK Step 6)")
else:
    print("Warning: old_xk_exam not found in text!")

# =========================================================================
# STEP 5: Exam & Test Type Selection in Manual Builder (y8 Step 5)
# =========================================================================
old_y8_exam = 'l.jsxs("div",{children:[l.jsx("label",{className:"block font-bold text-slate-700 mb-1",children:"Exam Title"}),l.jsx("input",{type:"text",value:Be,onChange:Ie=>xe(Ie.target.value),className:"w-full px-3 py-2 bg-white border border-slate-300 rounded-lg font-semibold"})]})'

new_y8_exam = '''l.jsxs("div",{className:"space-y-1.5",children:[l.jsx("label",{className:"block font-bold text-slate-700 mb-1",children:"Exam & Test Type:"}),l.jsxs("select",{value:["Annual Examination","1st Term Examination","2nd Term Examination","Mid-Term Examination","December Test Session","Send-Up Examination","Pre-Board Examination","Weekly Test Series","Monthly Assessment"].includes(Be)?Be:"Custom Title",onChange:Ie=>{const val=Ie.target.value;if(val==="Custom Title"){if(["Annual Examination","1st Term Examination","2nd Term Examination","Mid-Term Examination","December Test Session","Send-Up Examination","Pre-Board Examination","Weekly Test Series","Monthly Assessment"].includes(Be))xe("");}else{xe(val);}},className:"w-full px-3 py-2 bg-white border border-slate-300 rounded-lg font-bold text-slate-900 focus:border-blue-600 focus:outline-none shadow-xs",children:[l.jsx("option",{value:"Annual Examination",children:"Annual Examination"}),l.jsx("option",{value:"1st Term Examination",children:"1st Term Examination"}),l.jsx("option",{value:"2nd Term Examination",children:"2nd Term Examination"}),l.jsx("option",{value:"Mid-Term Examination",children:"Mid-Term Examination"}),l.jsx("option",{value:"December Test Session",children:"December Test Session"}),l.jsx("option",{value:"Send-Up Examination",children:"Send-Up Examination"}),l.jsx("option",{value:"Pre-Board Examination",children:"Pre-Board Examination"}),l.jsx("option",{value:"Weekly Test Series",children:"Weekly Test Series"}),l.jsx("option",{value:"Monthly Assessment",children:"Monthly Assessment"}),l.jsx("option",{value:"Custom Title",children:"Custom Title..."})]}),(!["Annual Examination","1st Term Examination","2nd Term Examination","Mid-Term Examination","December Test Session","Send-Up Examination","Pre-Board Examination","Weekly Test Series","Monthly Assessment"].includes(Be))&&l.jsx("input",{type:"text",value:Be,onChange:Ie=>xe(Ie.target.value),placeholder:"Enter custom exam title (e.g. Grand Test Session 2026)...",className:"w-full px-3 py-2 mt-1.5 border border-blue-400 rounded-lg font-bold text-slate-900 focus:border-blue-600 focus:outline-none"})]})'''

if old_y8_exam in text:
    text = text.replace(old_y8_exam, new_y8_exam, 1)
    check("Step 5: Exam & Test Type Selection in Manual Builder (y8 Step 5)")
else:
    print("Warning: old_y8_exam not found in text!")

# Save to assets/index-DAioIUjd.js
with open('assets/index-DAioIUjd.js', 'w', encoding='utf-8') as f:
    f.write(text)

print("SUCCESSFULLY SAVED assets/index-DAioIUjd.js!")
