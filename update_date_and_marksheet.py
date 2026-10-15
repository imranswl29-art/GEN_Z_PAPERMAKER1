import re

print("Reading assets/index-DAioIUjd.js...")
with open('assets/index-DAioIUjd.js', 'r', encoding='utf-8') as f:
    text = f.read()

# -------------------------------------------------------------
# 1. Update iC and add setPrintOrientation
# -------------------------------------------------------------
old_iC = 'function iC(n,e,t){const r=document.getElementById(n);if(!r)return console.error(`Target element with id "${n}" not found for PDF export.`),window.print(),!1;try{t&&t("Rendering high-resolution A4 document..."),await new Promise(y=>setTimeout(y,150));const a=210,o=297,A=8,u=8,f=a-A*2,B=o-u*2,m=new Xt({orientation:"portrait",unit:"mm",format:"a4",compress:!0});await Oh(r,m,f,B,A,u,!0);const C=e.endsWith(".pdf")?e:`${e}.pdf`;return m.save(C),t&&t("Downloaded successfully!"),!0}catch(a){return console.warn("PDF export error, falling back to print:",a),window.print(),!1}}'

new_iC = '''function setPrintOrientation(orientation = "portrait"){let s=document.getElementById("print-orientation-style");if(!s){s=document.createElement("style");s.id="print-orientation-style";document.head.appendChild(s);}s.innerHTML=`@media print { @page { size: ${orientation} !important; margin: 6mm !important; } }`;}
function iC(n,e,t,orientation = "portrait"){const r=document.getElementById(n);if(!r)return console.error(`Target element with id "${n}" not found for PDF export.`),window.print(),!1;try{t&&t("Rendering high-resolution A4 document..."),await new Promise(y=>setTimeout(y,150));const isLand=orientation==="landscape";const a=isLand?297:210,o=isLand?210:297,A=8,u=8,f=a-A*2,B=o-u*2,m=new Xt({orientation:isLand?"landscape":"portrait",unit:"mm",format:"a4",compress:!0});await Oh(r,m,f,B,A,u,!0);const C=e.endsWith(".pdf")?e:`${e}.pdf`;return m.save(C),t&&t("Downloaded successfully!"),!0}catch(a){return console.warn("PDF export error, falling back to print:",a),window.print(),!1}}'''

assert old_iC in text, 'old_iC not found in bundle'
text = text.replace(old_iC, new_iC, 1)
print("[✓] Updated iC and added setPrintOrientation")

# -------------------------------------------------------------
# 2. Update aq (DateSheet):
# -------------------------------------------------------------
old_aq_state = 'const r=_T(n,e),[a,o]=Ee.useState("editor"),[A,u]=Ee.useState(!1),[f,B]=Ee.useState(""),[m,C]=Ee.useState(null),'
new_aq_state = 'const r=_T(n,e),[a,o]=Ee.useState("editor"),[A,u]=Ee.useState(!1),[f,B]=Ee.useState(""),[m,C]=Ee.useState(null),[dsOrientation,setDsOrientation]=Ee.useState("portrait"),'
assert old_aq_state in text, 'old_aq_state not found'
text = text.replace(old_aq_state, new_aq_state, 1)

old_aq_T = 'T=()=>{const D=document.title,U=E.classLevel.replace(/\\s+/g,"_"),Q=F.replace(/\\s+/g,"_");document.title=`${U}_Date_Sheet_${Q}`,window.print(),setTimeout(()=>{document.title=D},1500)}'
new_aq_T = 'T=()=>{setPrintOrientation(dsOrientation);const D=document.title,U=E.classLevel.replace(/\\s+/g,"_"),Q=F.replace(/\\s+/g,"_");document.title=`${U}_Date_Sheet_${Q}_${dsOrientation.toUpperCase()}`,window.print(),setTimeout(()=>{document.title=D},1500)}'
assert old_aq_T in text, 'old_aq_T not found'
text = text.replace(old_aq_T, new_aq_T, 1)

old_aq_H = 'await iC("datesheet-print-container",Q,pe=>{B(pe)})&&y("Date Sheet PDF downloaded successfully!")'
new_aq_H = 'await iC("datesheet-print-container",Q,pe=>{B(pe)},dsOrientation)&&y(`Date Sheet PDF downloaded successfully in ${dsOrientation} orientation!`)'
assert old_aq_H in text, 'old_aq_H not found'
text = text.replace(old_aq_H, new_aq_H, 1)

old_aq_btn_bar = 'l.jsxs("button",{type:"button",onClick:T,className:"btn-print-preview"'
pos_aq_btn = text.find(old_aq_btn_bar, 2104599)
assert pos_aq_btn != -1, 'old_aq_btn_bar not found in aq'

new_aq_btn_bar = '''l.jsxs("div",{className:"flex items-center gap-1 bg-slate-100 p-1 rounded-xl border border-slate-200 mr-1 no-print",children:[l.jsxs("button",{type:"button",onClick:()=>{setDsOrientation("portrait");setPrintOrientation("portrait");},className:`flex items-center gap-1 px-3 py-1.5 rounded-lg text-xs font-bold transition-all cursor-pointer ${dsOrientation==="portrait"?"bg-white text-blue-700 shadow-xs font-black ring-1 ring-blue-300":"text-slate-600 hover:text-slate-900"}`,title:"Portrait (Vertical Orientation) - عمودی انداز",children:[l.jsx("span",{children:"📄"}),l.jsx("span",{children:"Portrait (عمودی)"})]}),l.jsxs("button",{type:"button",onClick:()=>{setDsOrientation("landscape");setPrintOrientation("landscape");},className:`flex items-center gap-1 px-3 py-1.5 rounded-lg text-xs font-bold transition-all cursor-pointer ${dsOrientation==="landscape"?"bg-white text-blue-700 shadow-xs font-black ring-1 ring-blue-300":"text-slate-600 hover:text-slate-900"}`,title:"Landscape (Horizontal Orientation) - افقی انداز",children:[l.jsx("span",{children:"📑"}),l.jsx("span",{children:"Landscape (افقی)"})]})]}),l.jsxs("button",{type:"button",onClick:T,className:"btn-print-preview"'''

text = text[:pos_aq_btn] + new_aq_btn_bar + text[pos_aq_btn + len(old_aq_btn_bar):]

old_ds_container = 'className:`${a==="preview"?"block":"hidden print:block"} bg-white rounded-2xl shadow-xl border border-slate-300 p-6 sm:p-10 max-w-4xl mx-auto print:border-none print:shadow-none print:p-0 print:m-0 print:max-w-none print:w-full`,id:"datesheet-print-container"'
new_ds_container = 'className:`${a==="preview"?"block":"hidden print:block"} bg-white rounded-2xl shadow-xl border border-slate-300 p-6 sm:p-10 ${dsOrientation==="landscape"?"max-w-6xl landscape-mode":"max-w-4xl portrait-mode"} mx-auto print:border-none print:shadow-none print:p-0 print:m-0 print:max-w-none print:w-full`,id:"datesheet-print-container"'
assert old_ds_container in text, 'old_ds_container not found'
text = text.replace(old_ds_container, new_ds_container, 1)
print("[✓] Updated DateSheet (aq) with Landscape and Portrait options")

# -------------------------------------------------------------
# 3. Update lq (Marksheet & Result Card):
# -------------------------------------------------------------
# Add msOrientation, savedSheets, studentSearch, printAllCards
old_lq_state = 'lq=({currentUser:n,activeHeader:e,onOpenSchoolProfile:t})=>{const r=_T(n,e),[a,o]=Ee.useState("editor"),[A,u]=Ee.useState("st-1"),[m_sec,setM_sec]=Ee.useState("all"),[f,B]=Ee.useState(!1),[m,C]=Ee.useState(""),[y,v]=Ee.useState(null),E=Ee.useRef(null),[I,O]=Ee.useState(null),F=S=>{v(S),setTimeout(()=>v(null),3e3)},'

new_lq_state = '''lq=({currentUser:n,activeHeader:e,onOpenSchoolProfile:t})=>{const r=_T(n,e),[a,o]=Ee.useState("editor"),[A,u]=Ee.useState("st-1"),[m_sec,setM_sec]=Ee.useState("all"),[f,B]=Ee.useState(!1),[m,C]=Ee.useState(""),[y,v]=Ee.useState(null),E=Ee.useRef(null),[I,O]=Ee.useState(null),[msOrientation,setMsOrientation]=Ee.useState("portrait"),[studentSearch,setStudentSearch]=Ee.useState(""),[printAllCards,setPrintAllCards]=Ee.useState(!1),[savedSheets,setSavedSheets]=Ee.useState(()=>{try{const raw=localStorage.getItem("ptbb_all_marksheets");if(raw){const p=JSON.parse(raw);if(Array.isArray(p)&&p.length>0)return p;}}catch(e){}return[];}),F=S=>{v(S),setTimeout(()=>v(null),3e3)},'''

assert old_lq_state in text, 'old_lq_state not found'
text = text.replace(old_lq_state, new_lq_state, 1)

# In lq useEffect, sync savedSheets from /api/marksheets
old_lq_fetch = '''fetch(`/api/marksheets${n!=null&&n.id?`?userId=${encodeURIComponent(n.id)}`:""}`).then(S=>S.json()).then(S=>{Array.isArray(S)&&S.length>0&&(Z(S[0]),localStorage.setItem("ptbb_marksheet_data",JSON.stringify(S[0])))}).catch(()=>{})'''

new_lq_fetch = '''fetch(`/api/marksheets${n!=null&&n.id?`?userId=${encodeURIComponent(n.id)}`:""}`).then(S=>S.json()).then(S=>{if(Array.isArray(S)&&S.length>0){setSavedSheets(S);localStorage.setItem("ptbb_all_marksheets",JSON.stringify(S));Z(S[0]);localStorage.setItem("ptbb_marksheet_data",JSON.stringify(S[0]));}}).catch(()=>{})'''

assert old_lq_fetch in text, 'old_lq_fetch not found'
text = text.replace(old_lq_fetch, new_lq_fetch, 1)

# Add saveCurrentSheet, loadSavedSheet, createNewSheet, deleteSavedSheet, printAllCardsAction helper functions
old_lq_actions = '''const ne=R.subjects.reduce((S,V)=>S+V.totalMarks,0),'''

new_lq_actions = '''const saveCurrentSheet=(sheetToSave=R)=>{const updated={...sheetToSave,id:sheetToSave.id||`ms-${Date.now()}`,userId:(n&&n.id)||"guest",updatedAt:new Date().toISOString()};Z(updated);setSavedSheets(prev=>{const idx=prev.findIndex(s=>s.id===updated.id);const next=idx>=0?prev.map((s,i)=>i===idx?updated:s):[updated,...prev];localStorage.setItem("ptbb_all_marksheets",JSON.stringify(next));localStorage.setItem("ptbb_marksheet_data",JSON.stringify(updated));return next;});fetch("/api/marksheets",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(updated)}).catch(()=>{});F(`کلاس '${updated.classLevel}' سیشن '${updated.session}' کا ڈیٹا محفوظ ہو گیا!`);};
const loadSavedSheet=(id)=>{const found=savedSheets.find(s=>s.id===id);if(found){Z(found);if(found.students&&found.students.length>0){u(found.students[0].id);}localStorage.setItem("ptbb_marksheet_data",JSON.stringify(found));F(`کلاس '${found.classLevel}' لوڈ ہو گئی`);}};
const createNewSheetForClassSession=(cls="10th Class (Science Group)",sess="2025-2026")=>{const newSubs=getSubjectsPresetForClass(cls);const newSheet={id:`ms-${Date.now()}-${Math.random().toString(36).substring(2,6)}`,classLevel:cls,session:sess,examCategory:"Annual Examination",subjects:newSubs,students:[{id:`st-${Date.now()}-1`,rollNo:"1",name:"Muhammad Ahmad",fatherName:"Muhammad Ali",section:"A",attendance:"98%",rank:"1st",remarks:"Excellent academic consistency.",marks:{}},{id:`st-${Date.now()}-2`,rollNo:"2",name:"Fatima Noor",fatherName:"Tariq Mahmood",section:"A",attendance:"95%",rank:"2nd",remarks:"Hardworking student.",marks:{}}]};saveCurrentSheet(newSheet);};
const printAllCardsAction=()=>{setPrintOrientation(msOrientation);const V=document.title;document.title=`All_Result_Cards_${R.classLevel.replace(/\\s+/g,"_")}_${R.session}_${msOrientation.toUpperCase()}`;setPrintAllCards(!0);setTimeout(()=>{window.print();setTimeout(()=>{document.title=V;setPrintAllCards(!1);},1500);},250);};
const ne=R.subjects.reduce((S,V)=>S+V.totalMarks,0),'''

assert old_lq_actions in text, 'old_lq_actions not found'
text = text.replace(old_lq_actions, new_lq_actions, 1)

# In ue (Print single result card): use setPrintOrientation
old_ue = 'ue=S=>{const V=document.title;document.title=`Result_Card_Roll_${S.rollNo}_${S.name.replace(/\\s+/g,"_")}`,window.print(),setTimeout(()=>{document.title=V},1500)}'
new_ue = 'ue=S=>{setPrintOrientation(msOrientation);const V=document.title;document.title=`Result_Card_Roll_${S.rollNo}_${S.name.replace(/\\s+/g,"_")}_${msOrientation.toUpperCase()}`,window.print(),setTimeout(()=>{document.title=V},1500)}'
assert old_ue in text, 'old_ue not found'
text = text.replace(old_ue, new_ue, 1)

# In Ne (Download single result card PDF): pass msOrientation to iC
old_Ne = 'await iC("resultcard-print-container",V,ae=>{C(ae)})&&F("Result Card PDF downloaded successfully!")'
new_Ne = 'await iC("resultcard-print-container",V,ae=>{C(ae)},msOrientation)&&F(`Result Card PDF downloaded successfully in ${msOrientation} orientation!`)'
assert old_Ne in text, 'old_Ne not found'
text = text.replace(old_Ne, new_Ne, 1)

# In Ce (Print master sheet): use setPrintOrientation
old_Ce = 'Ce=()=>{o("masterSheet");const S=document.title;document.title=`Master_Marksheet_${R.classLevel.replace(/\\s+/g,"_")}`,window.print(),setTimeout(()=>{document.title=S},1500)}'
new_Ce = 'Ce=()=>{o("masterSheet");setPrintOrientation(msOrientation);const S=document.title;document.title=`Master_Marksheet_${R.classLevel.replace(/\\s+/g,"_")}_${msOrientation.toUpperCase()}`,window.print(),setTimeout(()=>{document.title=S},1500)}'
assert old_Ce in text, 'old_Ce not found'
text = text.replace(old_Ce, new_Ce, 1)

# In k (Download master sheet PDF): pass msOrientation to iC
old_k = 'await iC("mastersheet-print-container",S,q=>{C(q)})&&F("Master Marksheet PDF downloaded successfully!")'
new_k = 'await iC("mastersheet-print-container",S,q=>{C(q)},msOrientation)&&F(`Master Marksheet PDF downloaded successfully in ${msOrientation} orientation!`)'
assert old_k in text, 'old_k not found'
text = text.replace(old_k, new_k, 1)

# Update the Class dropdown in editor to make it fully editable text input with presets and session input
old_class_select = '''children:[l.jsx("label",{className:"block text-xs font-black uppercase tracking-wider text-slate-700 mb-1.5",children:"Class / Grade Level (e.g. Nursery, Prep to 10th):"}),l.jsx("select",{value:R.classLevel,onChange:S=>{const nCls=S.target.value;const newSubs=getSubjectsPresetForClass(nCls);Z(prev=>({...prev,classLevel:nCls,subjects:newSubs}));},className:"w-full px-3 py-2.5 rounded-xl border border-slate-300 font-bold text-xs bg-slate-50 focus:bg-white focus:outline-none focus:ring-2 focus:ring-blue-500 shadow-xs cursor-pointer",children:CLASSES_PRESETS.map(cls=>l.jsx("option",{value:cls,children:cls},cls))})]}),'''

new_class_select = '''children:[l.jsx("label",{className:"block text-xs font-black uppercase tracking-wider text-slate-700 mb-1.5",children:"Class / Grade Level (Editable - تبدیل یا ٹائپ کریں):"}),l.jsx("input",{type:"text",value:R.classLevel,onChange:S=>Z(prev=>({...prev,classLevel:S.target.value})),placeholder:"Enter or edit class name (e.g. 9th Science, 10th Arts, Grade 8, Prep...)",className:"w-full px-3.5 py-2.5 rounded-xl border-2 border-blue-400 font-black text-xs text-slate-900 bg-white focus:ring-2 focus:ring-blue-500 shadow-xs"}),l.jsxs("div",{className:"flex flex-wrap items-center gap-1 pt-1.5",children:[l.jsx("span",{className:"text-[10px] font-bold text-slate-500",children:"Quick Presets:"}),CLASSES_PRESETS.slice(0,8).map(cls=>l.jsx("button",{key:cls,type:"button",onClick:()=>{const newSubs=getSubjectsPresetForClass(cls);Z(prev=>({...prev,classLevel:cls,subjects:newSubs}));F("Loaded preset for "+cls);},className:`px-2 py-0.5 rounded text-[10px] font-bold border cursor-pointer ${R.classLevel===cls?"bg-blue-600 text-white border-blue-600":"bg-slate-100 text-slate-700 hover:bg-slate-200 border-slate-300"}`},cls))]})]}),'''

assert old_class_select in text, 'old_class_select not found'
text = text.replace(old_class_select, new_class_select, 1)

# In editor header, add Class & Session Manager banner at top of lq
old_lq_top_card = 'l.jsxs("div",{className:"card-3d p-5 sm:p-6 bg-white border border-slate-200",children:[l.jsxs("div",{className:"flex flex-col lg:flex-row items-start lg:items-center justify-between gap-4",'

new_lq_top_card = '''l.jsxs("div",{className:"bg-gradient-to-r from-blue-900 via-indigo-900 to-slate-900 text-white p-3.5 sm:p-4 rounded-2xl shadow-lg border border-blue-700 flex flex-wrap items-center justify-between gap-3 no-print",children:[l.jsxs("div",{className:"flex items-center gap-2.5 flex-wrap",children:[l.jsx("span",{className:"text-xs font-black uppercase tracking-wider text-amber-300 flex items-center gap-1",children:[l.jsx("span",{children:"📚"}),l.jsx("span",{children:"Class & Session Sheet:"})]}),l.jsxs("select",{value:R.id,onChange:S=>loadSavedSheet(S.target.value),className:"bg-slate-800 text-white font-black text-xs px-3 py-1.5 rounded-xl border border-blue-400 focus:ring-2 focus:ring-amber-400 cursor-pointer shadow-inner",children:[savedSheets.length===0&&l.jsx("option",{value:R.id,children:`${R.classLevel} • ${R.session}`}),savedSheets.map(s=>l.jsxs("option",{value:s.id,children:[s.classLevel," • Session ",s.session," (",(s.students||[]).length," Students)"]},s.id))]}),l.jsxs("button",{type:"button",onClick:()=>saveCurrentSheet(R),className:"btn-3d btn-3d-emerald flex items-center gap-1.5 px-3 py-1.5 text-white rounded-xl text-xs font-black cursor-pointer shadow-sm hover:brightness-110",title:"Save current class & session marksheet data permanently",children:[l.jsx("span",{children:"💾"}),l.jsx("span",{children:"Save Current Sheet Data"})]}),l.jsxs("button",{type:"button",onClick:()=>{const cls=prompt("Enter Class Name (کلاس کا نام لکھیں):","10th Class (Science Group)");if(cls){const sess=prompt("Enter Academic Session (تعلیمی سیشن لکھیں):",R.session||"2025-2026")||"2025-2026";createNewSheetForClassSession(cls,sess);}},className:"btn-3d bg-indigo-700 hover:bg-indigo-600 flex items-center gap-1.5 px-3 py-1.5 text-white rounded-xl text-xs font-black cursor-pointer shadow-sm",title:"Create a new class or session dataset",children:[l.jsx("span",{children:"➕"}),l.jsx("span",{children:"New Class / Session"})]})]}),l.jsxs("div",{className:"flex items-center gap-2",children:[l.jsxs("button",{type:"button",onClick:()=>exportMasterGazetteToExcel(R,r,m_sec),className:"btn-3d btn-3d-green flex items-center gap-1.5 px-3.5 py-1.5 text-white rounded-xl text-xs font-black cursor-pointer shadow-sm hover:brightness-110",title:"Download complete marksheet data in Excel (.xls) format anytime",children:[l.jsx("span",{children:"📊"}),l.jsx("span",{children:"Download in Excel"})]})]})]}),l.jsxs("div",{className:"card-3d p-5 sm:p-6 bg-white border border-slate-200",children:[l.jsxs("div",{className:"flex flex-col lg:flex-row items-start lg:items-center justify-between gap-4",'''

assert old_lq_top_card in text, 'old_lq_top_card not found'
text = text.replace(old_lq_top_card, new_lq_top_card, 1)

# In toolbar of lq, add Orientation switcher (Portrait / Landscape)
old_lq_toolbar = 'l.jsxs("div",{className:"flex flex-wrap items-center gap-2",children:[a==="singleCard"&&P&&l.jsxs(l.Fragment,'

new_lq_toolbar = '''l.jsxs("div",{className:"flex flex-wrap items-center gap-2",children:[l.jsxs("div",{className:"flex items-center gap-1 bg-slate-100 p-1 rounded-xl border border-slate-200 mr-1 no-print",children:[l.jsxs("button",{type:"button",onClick:()=>{setMsOrientation("portrait");setPrintOrientation("portrait");},className:`flex items-center gap-1 px-3 py-1.5 rounded-lg text-xs font-bold transition-all cursor-pointer ${msOrientation==="portrait"?"bg-white text-blue-700 shadow-xs font-black ring-1 ring-blue-300":"text-slate-600 hover:text-slate-900"}`,title:"Portrait (Vertical Orientation) - عمودی انداز",children:[l.jsx("span",{children:"📄"}),l.jsx("span",{children:"Portrait (عمودی)"})]}),l.jsxs("button",{type:"button",onClick:()=>{setMsOrientation("landscape");setPrintOrientation("landscape");},className:`flex items-center gap-1 px-3 py-1.5 rounded-lg text-xs font-bold transition-all cursor-pointer ${msOrientation==="landscape"?"bg-white text-blue-700 shadow-xs font-black ring-1 ring-blue-300":"text-slate-600 hover:text-slate-900"}`,title:"Landscape (Horizontal Orientation) - افقی انداز",children:[l.jsx("span",{children:"📑"}),l.jsx("span",{children:"Landscape (افقی)"})]})]}),a==="singleCard"&&P&&l.jsxs(l.Fragment,'

assert old_lq_toolbar in text, 'old_lq_toolbar not found'
text = text.replace(old_lq_toolbar, new_lq_toolbar, 1)

# In singleCard toolbar, add "Print ALL Cards" and "Download ALL Cards PDF" buttons alongside single card buttons
old_single_card_btns = 'title:"Download single student result card Word (.doc)",children:[l.jsx(Xu,{className:"w-4 h-4 text-blue-200"}),l.jsx("span",{children:"Download Card (.doc)"})]})]})'

new_single_card_btns = '''title:"Download single student result card Word (.doc)",children:[l.jsx(Xu,{className:"w-4 h-4 text-blue-200"}),l.jsx("span",{children:"Download Card (.doc)"})]}),l.jsxs("button",{type:"button",onClick:printAllCardsAction,className:"btn-3d btn-3d-purple flex items-center gap-1.5 px-3.5 py-2.5 text-white rounded-xl text-xs font-black cursor-pointer shadow-md",title:"Print ALL students result cards in one go",children:[l.jsx(SAFE_od,{className:"w-4 h-4 text-purple-200"}),l.jsx("span",{children:"Print ALL Cards"})]}),l.jsxs("button",{type:"button",onClick:()=>exportMasterGazetteToExcel(R,r,m_sec),className:"btn-3d btn-3d-green flex items-center gap-1.5 px-3.5 py-2.5 text-white rounded-xl text-xs font-black cursor-pointer shadow-md",title:"Export complete class result marksheet to Excel",children:[l.jsx("span",{children:"📊"}),l.jsx("span",{children:"Excel (.xls)"})]})]})'''

assert old_single_card_btns in text, 'old_single_card_btns not found'
text = text.replace(old_single_card_btns, new_single_card_btns, 1)

# In singleCard student navigation bar, add Instant Student Search by name / roll number
old_student_nav_bar = 'children:[l.jsx("span",{className:"text-xs font-black text-slate-700 uppercase tracking-wide",children:"Select Candidate / Student:"}),l.jsxs("select",{value:P.id,onChange:S=>u(S.target.value),'

new_student_nav_bar = '''children:[l.jsx("span",{className:"text-xs font-black text-slate-700 uppercase tracking-wide",children:"Search / Select Student:"}),l.jsx("input",{type:"text",value:studentSearch,onChange:S=>setStudentSearch(S.target.value),placeholder:"🔍 Search student by name or roll no...",className:"px-3 py-1.5 rounded-xl border border-slate-300 font-bold text-xs bg-white text-slate-900 w-48 focus:ring-2 focus:ring-blue-500"}),l.jsxs("select",{value:P.id,onChange:S=>u(S.target.value),'''

assert old_student_nav_bar in text, 'old_student_nav_bar not found'
text = text.replace(old_student_nav_bar, new_student_nav_bar, 1)

# In resultcard-print-container, make width and mode dynamic for landscape vs portrait
old_rc_container = 'className:"bg-white rounded-2xl shadow-xl border border-slate-300 p-6 sm:p-10 max-w-4xl mx-auto print:border-none print:shadow-none print:p-0 print:m-0 print:max-w-none print:w-full",children:'

new_rc_container = 'className:`bg-white rounded-2xl shadow-xl border border-slate-300 p-6 sm:p-8 ${msOrientation==="landscape"?"max-w-6xl landscape-mode":"max-w-4xl portrait-mode"} mx-auto print:border-none print:shadow-none print:p-0 print:m-0 print:max-w-none print:w-full`,children:'

assert old_rc_container in text, 'old_rc_container not found'
text = text.replace(old_rc_container, new_rc_container, 1)

# In mastersheet-print-container, make width dynamic for landscape vs portrait
old_ms_container = 'className:"bg-white rounded-2xl shadow-xl border border-slate-300 p-6 sm:p-8 max-w-5xl mx-auto print:border-none print:shadow-none print:p-0 print:m-0 print:max-w-none print:w-full overflow-x-auto",children:'

new_ms_container = 'className:`bg-white rounded-2xl shadow-xl border border-slate-300 p-6 sm:p-8 ${msOrientation==="landscape"?"max-w-7xl landscape-mode":"max-w-5xl portrait-mode"} mx-auto print:border-none print:shadow-none print:p-0 print:m-0 print:max-w-none print:w-full overflow-x-auto`,children:'

assert old_ms_container in text, 'old_ms_container not found'
text = text.replace(old_ms_container, new_ms_container, 1)

print("Writing updated assets/index-DAioIUjd.js...")
with open('assets/index-DAioIUjd.js', 'w', encoding='utf-8') as f:
    f.write(text)

print("[✓] Successfully updated all DateSheet, Marksheet, ResultCard, and Orientation features!")
