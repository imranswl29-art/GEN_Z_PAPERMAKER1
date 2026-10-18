import subprocess

with open('assets/index-DAioIUjd.js', 'r', encoding='utf-8') as f:
    text = f.read()

# -------------------------------------------------------------
# 1. Date Sheet (aq) Mode Segmented Control
# -------------------------------------------------------------
pos_aq = text.find('aq=({currentUser:n,activeHeader:e,onOpenSchoolProfile:t})=>{')
pos_btn_aq = text.find('Printable A4 Preview', pos_aq)
end_aq = pos_btn_aq + len('Printable A4 Preview")}]})]}')
start_aq = text.rfind('l.jsxs("div",{className:"flex items-center gap-1.5 p-1.5 bg-slate-100', 0, pos_btn_aq)
if start_aq != -1 and end_aq != -1:
    old_aq_mode = text[start_aq:end_aq]
    new_aq_mode = 'l.jsxs("div",{className:"segmented-control",children:[l.jsxs("button",{type:"button",onClick:()=>o("editor"),className:"segmented-btn " + (a==="editor"?"segmented-btn-active":"segmented-btn-inactive"),children:[l.jsx(J2,{className:"w-3.5 h-3.5"}),l.jsx("span",{children:"Interactive Editor"})]}),l.jsxs("button",{type:"button",onClick:()=>o("preview"),className:"segmented-btn " + (a==="preview"?"segmented-btn-active":"segmented-btn-inactive"),children:[l.jsx(e8,{className:"w-3.5 h-3.5"}),l.jsx("span",{children:"Printable A4 Preview"})]})]})'
    text = text[:start_aq] + new_aq_mode + text[end_aq:]
    print("1. Refactored Date Sheet (aq) mode buttons to segmented control!")
else:
    print("1. Error finding Date Sheet mode chunk")

# -------------------------------------------------------------
# 2. Result Card / Marksheet (lq) Mode Segmented Control
# -------------------------------------------------------------
pos_lq = text.find('lq=({currentUser:n,activeHeader:e,onOpenSchoolProfile:t})=>{')
pos_btn_lq = text.find('Class Master Sheet', pos_lq)
end_lq = pos_btn_lq + len('Class Master Sheet")}]})]}')
start_lq = text.rfind('l.jsxs("div",{className:"flex flex-wrap items-center gap-1.5 p-1.5 bg-slate-100', 0, pos_btn_lq)
if start_lq != -1 and end_lq != -1:
    old_lq_mode = text[start_lq:end_lq]
    new_lq_mode = 'l.jsxs("div",{className:"segmented-control",children:[l.jsxs("button",{type:"button",onClick:()=>o("editor"),className:"segmented-btn " + (a==="editor"?"segmented-btn-active":"segmented-btn-inactive"),children:[l.jsx(J2,{className:"w-3.5 h-3.5"}),l.jsx("span",{children:"Marks Entry"})]}),l.jsxs("button",{type:"button",onClick:()=>o("singleCard"),className:"segmented-btn " + (a==="singleCard"?"segmented-btn-active":"segmented-btn-inactive"),children:[l.jsx(z3,{className:"w-3.5 h-3.5"}),l.jsx("span",{children:"A4 Result Card"})]}),l.jsxs("button",{type:"button",onClick:()=>o("masterSheet"),className:"segmented-btn " + (a==="masterSheet"?"segmented-btn-active":"segmented-btn-inactive"),children:[l.jsx(n8,{className:"w-3.5 h-3.5"}),l.jsx("span",{children:"Master Sheet"})]})]})'
    text = text[:start_lq] + new_lq_mode + text[end_lq:]
    print("2. Refactored Result Card (lq) mode buttons to segmented control!")
else:
    print("2. Error finding Result Card mode chunk")

# -------------------------------------------------------------
# 3. Saved Papers Archive 5-button rush -> View & Print + Options ▾
# -------------------------------------------------------------
pos_sp_btn = text.find('title:"Delete this saved paper"')
if pos_sp_btn != -1:
    end_sp = pos_sp_btn + len('title:"Delete this saved paper",children:[l.jsx(Ql,{className:"w-3.5 h-3.5"}),l.jsx("span",{children:"Delete"})]})]}')
    start_sp = text.rfind('l.jsxs("div",{className:"flex items-center gap-1.5 pt-2 border-t border-slate-100"', 0, pos_sp_btn)
    if start_sp != -1 and end_sp != -1:
        new_sp_chunk = 'l.jsxs("div",{className:"flex items-center justify-between gap-2 pt-2 border-t border-slate-100",children:[l.jsxs("button",{type:"button",onClick:()=>qe(ge),className:"btn-3d btn-3d-blue flex items-center justify-center gap-1.5 flex-1 py-1.5 text-white rounded-lg text-xs font-black shadow-xs cursor-pointer",title:"View and print question paper on A4 sheet",children:[l.jsx(SAFE_od,{className:"w-3.5 h-3.5 text-blue-100 shrink-0"}),l.jsx("span",{children:"View & Print"})]}),l.jsxs("details",{className:"relative inline-block text-left no-print",children:[l.jsxs("summary",{className:"btn-3d btn-3d-indigo flex items-center gap-1 px-3 py-1.5 text-white rounded-lg text-xs font-black shadow-xs cursor-pointer list-none select-none",title:"Export & Paper Options",children:[l.jsx("span",{children:"Options ▾"})]}),l.jsxs("div",{className:"dropdown-menu-panel",children:[l.jsxs("button",{type:"button",onClick:evt=>{evt.currentTarget.closest("details")?.removeAttribute("open");z0(ge);},className:"dropdown-menu-item text-blue-700 hover:bg-blue-50",title:"Download editable Microsoft Word document",children:[l.jsx(Xu,{className:"w-3.5 h-3.5 text-blue-600"}),l.jsx("span",{children:"Download Word (.doc)"})]}),l.jsxs("button",{type:"button",onClick:evt=>{evt.currentTarget.closest("details")?.removeAttribute("open");E(ge);te(!0);},className:"dropdown-menu-item text-emerald-700 hover:bg-emerald-50",title:"View and print Answer Key",children:[l.jsx(SAFE_ad,{className:"w-3.5 h-3.5 text-emerald-600"}),l.jsx("span",{children:"Answer Key (Key & Solutions)"})]}),l.jsxs("button",{type:"button",onClick:evt=>{evt.currentTarget.closest("details")?.removeAttribute("open");E(ge);T(!0);},className:"dropdown-menu-item text-purple-700 hover:bg-purple-50",title:"Print OMR Bubble Sheet",children:[l.jsx(Rw,{className:"w-3.5 h-3.5 text-purple-600"}),l.jsx("span",{children:"Bubble Sheet (OMR Sheet)"})]}),l.jsxs("button",{type:"button",onClick:evt=>{evt.currentTarget.closest("details")?.removeAttribute("open");window.confirm(`Are you sure you want to delete "${ge.header.subjectName}" paper?`)&&St(ge.id);},className:"dropdown-menu-item text-rose-700 hover:bg-rose-50 border-t border-slate-100",title:"Delete saved paper",children:[l.jsx(Ql,{className:"w-3.5 h-3.5 text-rose-600"}),l.jsx("span",{children:"Delete Paper"})]})]})]})]})'
        text = text[:start_sp] + new_sp_chunk + text[end_sp:]
        print("3. Refactored Saved Papers buttons into View & Print + Options ▾ dropdown!")
    else:
        print("3. Error finding Saved Papers chunk")
else:
    print("3. Delete this saved paper button not found")

with open('assets/index-DAioIUjd.js', 'w', encoding='utf-8') as f:
    f.write(text)

res = subprocess.run(['node', '--check', 'assets/index-DAioIUjd.js'], capture_output=True, text=True)
print('CHECK RESULT:', res.returncode)
if res.returncode != 0:
    print('Syntax error:', res.stderr[:500])
else:
    print('SUCCESS! ALL CONTROLS CONSOLIDATED WITH ZERO ERRORS!')
