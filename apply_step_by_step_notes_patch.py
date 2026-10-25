import subprocess
import os

with open('assets/index-DAioIUjd.js', 'r', encoding='utf-8') as f:
    text = f.read()

def check(step_name):
    global text
    with open('step_check.js', 'w', encoding='utf-8') as f:
        f.write(text)
    res = subprocess.run(['node', '--check', 'step_check.js'], capture_output=True, text=True)
    if res.returncode != 0:
        print(f"FAILED AT {step_name}:")
        print(res.stderr[:500])
        return False
    else:
        print(f"PASSED {step_name}")
        return True

assert check("Step 0: Original File Check")

# Now load NotesPortalComponent code
with open('patch_bundle_notes_portal.py', 'r') as pf:
    p_code = pf.read()

s_start = p_code.find('const SUBJECT_METADATA_9TH =')
s_end = p_code.find("'''\n\n# Check if NotesPortalComponent")
notes_portal_code = p_code[s_start:s_end].strip()

# 1. NotesPortalComponent insert
pos_cq = text.find('function cq()')
text = text[:pos_cq] + notes_portal_code + "\n\n" + text[pos_cq:]
assert check("Step 1: NotesPortalComponent Definition Insert")

# 2. Add to Sidebar B8
old_b8 = '{id:"question_bank",label:"Question Bank",icon:Kf,badge:"Matric 9-10",badgeColor:"bg-indigo-600 text-white"}'
new_b8 = '{id:"question_bank",label:"Question Bank",icon:Kf,badge:"Matric 9-10",badgeColor:"bg-indigo-600 text-white"},{id:"notes_portal",label:"Notes 9th & 10th",icon:Kf,badge:"PTBB Solved",badgeColor:"bg-purple-600 text-white"}'
assert old_b8 in text
text = text.replace(old_b8, new_b8, 1)
assert check("Step 2: Sidebar B8 Item")

# 3. Add to Header Bar
old_header_div = 'l.jsx("div",{className:"flex items-center gap-2 shrink-0",children:m?l.jsxs("button",{type:"button",onClick:Ke,className:"btn-3d btn-3d-rose flex items-center gap-1.5 px-3 py-2 text-white rounded-xl text-xs font-black cursor-pointer shadow-sm",title:"Direct Logout",children:[l.jsxs("svg",{className:"w-3.5 h-3.5 text-white",viewBox:"0 0 24 24",fill:"none",stroke:"currentColor",strokeWidth:"2.2",strokeLinecap:"round",strokeLinejoin:"round",children:[l.jsx("path",{d:"M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"}),l.jsx("polyline",{points:"16 17 21 12 16 7"}),l.jsx("line",{x1:"21",x2:"9",y1:"12",y2:"12"})]}),l.jsx("span",{children:"Logout"})]}):l.jsx("button",{onClick:()=>R(!0),className:"btn-3d px-3.5 py-2 text-white font-black rounded-xl text-xs cursor-pointer",style:{backgroundColor:"#2563eb",border:"1px solid #1d4ed8",color:"#ffffff"},children:"Login"})})'

new_header_div = '''l.jsxs("div",{className:"flex items-center gap-2 shrink-0",children:[l.jsxs("button",{type:"button",onClick:()=>{e("notes_portal");o(!1)},className:"btn-3d btn-3d-purple flex items-center gap-1.5 px-3 py-1.5 sm:px-3.5 sm:py-2 text-white rounded-xl text-xs font-black cursor-pointer shadow-sm hover:scale-[1.02] transition-transform",title:"Official PTBB Solved Notes for Class 9th & 10th (MCQs & Short Questions)",children:[l.jsxs("svg",{className:"w-4 h-4 text-purple-200",viewBox:"0 0 24 24",fill:"none",stroke:"currentColor",strokeWidth:"2.2",strokeLinecap:"round",strokeLinejoin:"round",children:[l.jsx("path",{d:"M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"}),l.jsx("path",{d:"M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"})]}),l.jsx("span",{children:"Notes 9th & 10th"}),l.jsx("span",{className:"hidden md:inline-block bg-purple-900/60 text-purple-200 text-[10px] px-1.5 py-0.5 rounded-md font-bold",children:"PTBB"})]}),m?l.jsxs("button",{type:"button",onClick:Ke,className:"btn-3d btn-3d-rose flex items-center gap-1.5 px-3 py-2 text-white rounded-xl text-xs font-black cursor-pointer shadow-sm",title:"Direct Logout",children:[l.jsxs("svg",{className:"w-3.5 h-3.5 text-white",viewBox:"0 0 24 24",fill:"none",stroke:"currentColor",strokeWidth:"2.2",strokeLinecap:"round",strokeLinejoin:"round",children:[l.jsx("path",{d:"M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"}),l.jsx("polyline",{points:"16 17 21 12 16 7"}),l.jsx("line",{x1:"21",x2:"9",y1:"12",y2:"12"})]}),l.jsx("span",{children:"Logout"})]}):l.jsx("button",{onClick:()=>R(!0),className:"btn-3d px-3.5 py-2 text-white font-black rounded-xl text-xs cursor-pointer",style:{backgroundColor:"#2563eb",border:"1px solid #1d4ed8",color:"#ffffff"},children:"Login"})]})'''

assert old_header_div in text, "old_header_div not found in text"
text = text.replace(old_header_div, new_header_div, 1)
assert check("Step 3: Top Header Bar Button")

# 4. Add to Dashboard m8 Action Cards Line
old_m8_cards = 'l.jsxs("div",{className:"grid grid-cols-2 sm:grid-cols-4 gap-4",children:['
new_m8_cards = '''l.jsxs("div",{className:"grid grid-cols-2 sm:grid-cols-5 gap-3.5",children:[l.jsxs("div",{onClick:()=>C&&C("notes_portal"),className:"card-3d p-4 flex flex-col justify-between cursor-pointer hover:border-purple-400 hover:shadow-md transition-all group bg-gradient-to-b from-white to-purple-50/40",title:"Open Official PTBB Solved Notes for 9th and 10th Classes",children:[l.jsxs("div",{className:"flex items-center justify-between mb-1",children:[l.jsx("span",{className:"text-[11px] font-black uppercase tracking-wider text-purple-900 group-hover:text-purple-700 transition-colors",children:"Notes 9th & 10th"}),l.jsx("div",{className:"w-8 h-8 rounded-lg bg-purple-600 text-white flex items-center justify-center shadow-xs shrink-0 group-hover:scale-110 transition-transform",children:l.jsxs("svg",{className:"w-4 h-4 text-white",viewBox:"0 0 24 24",fill:"none",stroke:"currentColor",strokeWidth:"2.2",strokeLinecap:"round",strokeLinejoin:"round",children:[l.jsx("path",{d:"M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"}),l.jsx("path",{d:"M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"})]})})]}),l.jsx("div",{className:"text-base font-black text-slate-950 mt-1",children:"Solved Notes"}),l.jsx("span",{className:"text-[11px] text-purple-700 font-bold mt-0.5 group-hover:underline",children:"168 Chapters (MCQs & SQs) →"})]}),'''

assert old_m8_cards in text, "old_m8_cards not found in text"
text = text.replace(old_m8_cards, new_m8_cards, 1)
assert check("Step 4: Dashboard m8 Card")

# 5. Add to main view router
old_main_router = 'n==="dashboard"&&l.jsx(AppTabErrorBoundary'
new_main_router = 'n==="notes_portal"&&l.jsx(AppTabErrorBoundary,{onReset:()=>e("dashboard"),children:l.jsx(NotesPortalComponent,{currentUser:m,onBack:()=>e("dashboard")})}),n==="dashboard"&&l.jsx(AppTabErrorBoundary'

assert old_main_router in text, "old_main_router not found in text"
text = text.replace(old_main_router, new_main_router, 1)
assert check("Step 5: Main View Router")

with open('assets/index-DAioIUjd.js', 'w', encoding='utf-8') as out_f:
    out_f.write(text)

print("ALL STEPS SUCCEEDED! Saved to assets/index-DAioIUjd.js")
