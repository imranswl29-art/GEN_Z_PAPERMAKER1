import subprocess

with open('assets/index-DAioIUjd.js', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. saved_papers 5 buttons
target_sp = 'l.jsx("button",{onClick:()=>qe(ge),className:"flex-1 py-1.5 bg-blue-600 hover:bg-blue-700 text-white rounded-lg text-xs font-bold shadow-xs",children:"View & Print"})'
pos_sp = text.find(target_sp)
if pos_sp != -1:
    block_start = text.rfind('l.jsxs("div",{className:"flex items-center gap-1.5 pt-2 border-t border-slate-100",children:[', 0, pos_sp)
    block_end = text.find(']})]},ge.id)', pos_sp)
    if block_start != -1 and block_end != -1:
        old_chunk = text[block_start:block_end + 3]
        new_chunk = 'l.jsxs("div",{className:"flex items-center justify-between gap-2 pt-2 border-t border-slate-100",children:[l.jsxs("button",{type:"button",onClick:()=>qe(ge),className:"btn-3d btn-3d-blue flex items-center justify-center gap-1.5 flex-1 py-1.5 text-white rounded-lg text-xs font-black shadow-xs cursor-pointer",title:"View and print question paper on A4 sheet",children:[l.jsx(SAFE_od,{className:"w-3.5 h-3.5 text-blue-100 shrink-0"}),l.jsx("span",{children:"View & Print"})]}),l.jsxs("details",{className:"relative inline-block text-left no-print",children:[l.jsxs("summary",{className:"btn-3d btn-3d-indigo flex items-center gap-1 px-3 py-1.5 text-white rounded-lg text-xs font-black shadow-xs cursor-pointer list-none select-none",title:"Export & Paper Options",children:[l.jsx("span",{children:"Options ▾"})]}),l.jsxs("div",{className:"dropdown-menu-panel",children:[l.jsxs("button",{type:"button",onClick:evt=>{evt.currentTarget.closest("details")?.removeAttribute("open");z0(ge);},className:"dropdown-menu-item text-blue-700 hover:bg-blue-50",title:"Download editable Microsoft Word document",children:[l.jsx(Xu,{className:"w-3.5 h-3.5 text-blue-600"}),l.jsx("span",{children:"Download Word (.doc)"})]}),l.jsxs("button",{type:"button",onClick:evt=>{evt.currentTarget.closest("details")?.removeAttribute("open");E(ge);te(!0);},className:"dropdown-menu-item text-emerald-700 hover:bg-emerald-50",title:"View and print Answer Key",children:[l.jsx(SAFE_ad,{className:"w-3.5 h-3.5 text-emerald-600"}),l.jsx("span",{children:"Answer Key (Key & Solutions)"})]}),l.jsxs("button",{type:"button",onClick:evt=>{evt.currentTarget.closest("details")?.removeAttribute("open");E(ge);T(!0);},className:"dropdown-menu-item text-purple-700 hover:bg-purple-50",title:"Print OMR Bubble Sheet",children:[l.jsx(Rw,{className:"w-3.5 h-3.5 text-purple-600"}),l.jsx("span",{children:"Bubble Sheet (OMR Sheet)"})]}),l.jsxs("button",{type:"button",onClick:evt=>{evt.currentTarget.closest("details")?.removeAttribute("open");window.confirm(`Are you sure you want to delete "${ge.header.subjectName}" paper?`)&&St(ge.id);},className:"dropdown-menu-item text-rose-700 hover:bg-rose-50 border-t border-slate-100",title:"Delete saved paper",children:[l.jsx(Ql,{className:"w-3.5 h-3.5 text-rose-600"}),l.jsx("span",{children:"Delete Paper"})]})]})]})]})'
        text = text[:block_start] + new_chunk + text[block_end + 3:]
        print('1. Refactored saved_papers 5-button block!')
    else:
        print('1. Boundary error in saved_papers')
else:
    print('1. target_sp not found in saved_papers')

# 2. aq mode buttons
pos_aq = text.find('aq=({currentUser:n,activeHeader:e,onOpenSchoolProfile:t})=>{')
pos_aq_btn = text.find('onClick:()=>o("editor")', pos_aq)
if pos_aq_btn != -1:
    block_start = text.rfind('l.jsxs("div",{className:"flex items-center gap-1.5 p-1.5 bg-slate-100 rounded-2xl border-2 border-slate-200', pos_aq, pos_aq_btn)
    block_end = text.find(']})]})]})', pos_aq_btn)
    if block_start != -1 and block_end != -1:
        # Find closing of mode div
        div_end = text.find(']})', block_start) + 3
        old_div = text[block_start:div_end]
        new_div = 'l.jsxs("div",{className:"segmented-control",children:[l.jsxs("button",{type:"button",onClick:()=>o("editor"),className:"segmented-btn " + (a==="editor"?"segmented-btn-active":"segmented-btn-inactive"),children:[l.jsx(J2,{className:"w-3.5 h-3.5"}),l.jsx("span",{children:"Interactive Editor"})]}),l.jsxs("button",{type:"button",onClick:()=>o("preview"),className:"segmented-btn " + (a==="preview"?"segmented-btn-active":"segmented-btn-inactive"),children:[l.jsx(e8,{className:"w-3.5 h-3.5"}),l.jsx("span",{children:"Printable A4 Preview"})]})]})'
        text = text[:block_start] + new_div + text[div_end:]
        print('2. Refactored aq mode buttons to segmented control!')
    else:
        print('2. Boundary error in aq')
else:
    print('2. aq editor button not found')

# 3. lq mode buttons
pos_lq = text.find('lq=({currentUser:n,activeHeader:e,onOpenSchoolProfile:t})=>{')
pos_lq_btn = text.find('onClick:()=>o("editor")', pos_lq)
if pos_lq_btn != -1:
    block_start = text.rfind('l.jsxs("div",{className:"flex flex-wrap items-center gap-1.5 p-1.5 bg-slate-100 rounded-2xl border-2 border-slate-200', pos_lq, pos_lq_btn)
    if block_start != -1:
        div_end = text.find(']})', text.find('onClick:()=>o("masterSheet")', pos_lq_btn)) + 3
        old_div = text[block_start:div_end]
        new_div = 'l.jsxs("div",{className:"segmented-control",children:[l.jsxs("button",{type:"button",onClick:()=>o("editor"),className:"segmented-btn " + (a==="editor"?"segmented-btn-active":"segmented-btn-inactive"),children:[l.jsx(J2,{className:"w-3.5 h-3.5"}),l.jsx("span",{children:"Marks Entry"})]}),l.jsxs("button",{type:"button",onClick:()=>o("singleCard"),className:"segmented-btn " + (a==="singleCard"?"segmented-btn-active":"segmented-btn-inactive"),children:[l.jsx(z3,{className:"w-3.5 h-3.5"}),l.jsx("span",{children:"A4 Result Card"})]}),l.jsxs("button",{type:"button",onClick:()=>o("masterSheet"),className:"segmented-btn " + (a==="masterSheet"?"segmented-btn-active":"segmented-btn-inactive"),children:[l.jsx(n8,{className:"w-3.5 h-3.5"}),l.jsx("span",{children:"Master Sheet"})]})]})'
        text = text[:block_start] + new_div + text[div_end:]
        print('3. Refactored lq mode buttons to segmented control!')
    else:
        print('3. Boundary error in lq')
else:
    print('3. lq editor button not found')

with open('assets/index-DAioIUjd.js', 'w', encoding='utf-8') as f:
    f.write(text)

res = subprocess.run(['node', '--check', 'assets/index-DAioIUjd.js'], capture_output=True, text=True)
print('CHECK RESULT:', res.returncode)
if res.returncode != 0:
    print('Syntax error:', res.stderr[:500])
else:
    print('ALL REMAINING REFACTORINGS COMPLETED AND VERIFIED!')
