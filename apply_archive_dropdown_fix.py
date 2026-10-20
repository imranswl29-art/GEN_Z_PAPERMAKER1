import subprocess

with open('assets/index-DAioIUjd.js', 'r', encoding='utf-8') as f:
    text = f.read()

pos_saved = text.find('n==="saved_papers"&&')
pos_options = text.find('Options ▾', pos_saved)
pos_start = text.rfind('l.jsxs("details",{className:"relative inline-block text-left no-print"', 0, pos_options)
pos_end = text.find('Delete Paper"})]})', pos_options) + len('Delete Paper"})]})')

target = text[pos_start:pos_end]

replacement = 'l.jsxs("div",{className:"relative inline-block text-left no-print archive-dropdown-container",children:[l.jsxs("button",{type:"button",onClick:ev=>{ev.stopPropagation();setOpenArchiveDropdownId(openArchiveDropdownId===ge.id?null:ge.id);},className:"btn-3d btn-3d-indigo flex items-center gap-1 px-3 py-1.5 text-white rounded-lg text-xs font-black shadow-xs cursor-pointer select-none",title:"Export & Paper Options",children:[l.jsx("span",{children:"Options ▾"})]}),openArchiveDropdownId===ge.id&&l.jsxs("div",{className:"absolute right-0 bottom-full mb-2 z-50 min-w-[14rem] bg-white border border-slate-200 rounded-xl shadow-2xl p-1.5 space-y-1 animate-in fade-in zoom-in-95",style:{backgroundColor:"#ffffff",zIndex:9999},onClick:ev=>ev.stopPropagation(),children:[l.jsxs("button",{type:"button",onClick:()=>{setOpenArchiveDropdownId(null);z0(ge);},className:"w-full flex items-center gap-2.5 px-3 py-2 text-xs font-bold text-slate-800 hover:bg-blue-50 hover:text-blue-700 rounded-lg text-left transition-colors cursor-pointer",title:"Download editable Microsoft Word document",children:[l.jsx(Xu,{className:"w-4 h-4 text-blue-600 shrink-0"}),l.jsx("span",{children:"Download Word (.doc)"})]}),l.jsxs("button",{type:"button",onClick:()=>{setOpenArchiveDropdownId(null);E(ge);te(!0);},className:"w-full flex items-center gap-2.5 px-3 py-2 text-xs font-bold text-slate-800 hover:bg-emerald-50 hover:text-emerald-700 rounded-lg text-left transition-colors cursor-pointer",title:"View and print Answer Key",children:[l.jsx(SAFE_ad,{className:"w-4 h-4 text-emerald-600 shrink-0"}),l.jsx("span",{children:"Answer Key (Key & Solutions)"})]}),l.jsxs("button",{type:"button",onClick:()=>{setOpenArchiveDropdownId(null);E(ge);T(!0);},className:"w-full flex items-center gap-2.5 px-3 py-2 text-xs font-bold text-slate-800 hover:bg-purple-50 hover:text-purple-700 rounded-lg text-left transition-colors cursor-pointer",title:"View official OMR bubble sheet",children:[l.jsx(Rw,{className:"w-4 h-4 text-purple-600 shrink-0"}),l.jsx("span",{children:"OMR Bubble Sheet"})]}),m&&l.jsxs("button",{type:"button",onClick:()=>{setOpenArchiveDropdownId(null);window.confirm(`Are you sure you want to delete "${ge.header.subjectName}" paper?`)&&St(ge.id);},className:"w-full flex items-center gap-2.5 px-3 py-2 text-xs font-bold text-red-600 hover:bg-red-50 rounded-lg text-left border-t border-slate-100 transition-colors cursor-pointer",title:"Delete this paper from saved list",children:[l.jsx(Ql,{className:"w-4 h-4 text-red-600 shrink-0"}),l.jsx("span",{children:"Delete Paper"})]})]})]})'

new_text = text[:pos_start] + replacement + text[pos_end:]

with open('assets/index-DAioIUjd.js', 'w', encoding='utf-8') as f:
    f.write(new_text)

res = subprocess.run(['node', '--check', 'assets/index-DAioIUjd.js'], capture_output=True, text=True)
if res.returncode == 0:
    print('SUCCESS! Saved papers single open dropdown passed node check!')
else:
    print('Failed:', res.stderr[:400])
    exit(1)
