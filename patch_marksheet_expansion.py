import re

print("Loading assets/index-DAioIUjd.js...")
with open("assets/index-DAioIUjd.js", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Add exportWholeSchoolConsolidatedGazette if not yet defined
if "function exportWholeSchoolConsolidatedGazette" not in text:
    ws_gazette = '''function exportWholeSchoolConsolidatedGazette(sheetsList, brand) {
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
    pos_exp = text.find("function exportMasterGazetteToExcel")
    assert pos_exp != -1, "exportMasterGazetteToExcel not found"
    text = text[:pos_exp] + ws_gazette + text[pos_exp:]
    print("[✓] Added exportWholeSchoolConsolidatedGazette function")

# 2. In lq, inject helper functions (fileInputRef, msOrientation, autoCalculateRanks, setGlobalPassingPercentage, handleImportCSV, printAllCardsAction)
old_lq_marker = 'Le=S=>{tq(S,R,r),F("Result Card MS Word document downloaded!")},'
new_lq_marker = '''Le=S=>{tq(S,R,r),F("Result Card MS Word document downloaded!")},
fileInputRef=Ee.useRef(null),
[msOrientation,setMsOrientation]=Ee.useState("portrait"),
autoCalculateRanks=()=>{
  const list=[...R.students];
  const withScores=list.map(st=>{
    const tot=R.subjects.reduce((sum,sub)=>sum+Number((st.marks&&st.marks[sub.id])||0),0);
    return {...st,_tot:tot};
  });
  withScores.sort((a,b)=>b._tot-a._tot);
  const updated=withScores.map((st,i)=>{
    const pos=i===0?"1st":i===1?"2nd":i===2?"3rd":`${i+1}th`;
    const {_tot,...rest}=st;
    return {...rest,rank:pos};
  });
  Z(prev=>({...prev,students:updated}));
  F("تمام طلباء کی پوزیشنز خودکار طور پر کیلکولیٹ ہو گئیں!");
},
setGlobalPassingPercentage=(pct=33)=>{
  Z(prev=>({...prev,subjects:prev.subjects.map(s=>({...s,passingMarks:Math.ceil(s.totalMarks*(pct/100))}))}));
  F(`تمام مضامین کے پاسنگ مارکس ${pct}% کر دیے گئے!`);
},
handleImportCSV=(evt)=>{
  const file=evt.target.files&&evt.target.files[0];
  if(!file)return;
  const reader=new FileReader;
  reader.onload=(e)=>{
    const content=e.target.result;
    if(typeof content!=="string")return;
    const lines=content.split(/\\r?\\n/).map(l=>l.trim()).filter(Boolean);
    if(lines.length<2)return alert("File is empty or invalid format.");
    const headers=lines[0].split(/[,\\t]/).map(h=>h.trim().toLowerCase());
    const rollIdx=headers.findIndex(h=>h.includes("roll"));
    const nameIdx=headers.findIndex(h=>h.includes("name")&&!h.includes("father"));
    const fatherIdx=headers.findIndex(h=>h.includes("father"));
    const secIdx=headers.findIndex(h=>h.includes("section")||h.includes("sec"));

    const subIndices=R.subjects.map(sub=>{
      const idx=headers.findIndex(h=>h.includes(sub.name.toLowerCase())||sub.name.toLowerCase().includes(h));
      return {subId:sub.id,colIdx:idx};
    });

    const parsedStudents=[];
    for(let i=1;i<lines.length;i++){
      const cols=lines[i].split(/[,\\t]/).map(c=>c.trim().replace(/^["']|["']$/g,""));
      if(cols.length<2)continue;
      const rollNo=rollIdx>=0?cols[rollIdx]:String(i);
      const name=nameIdx>=0?cols[nameIdx]:`Student ${i}`;
      const fatherName=fatherIdx>=0?cols[fatherIdx]:"Father Name";
      const section=secIdx>=0?cols[secIdx]:"A";
      const marks={};
      subIndices.forEach(({subId,colIdx})=>{
        if(colIdx>=0&&cols[colIdx]!==undefined){
          marks[subId]=Number(cols[colIdx])||0;
        }
      });
      parsedStudents.push({
        id:`st-${Date.now()}-${i}`,
        rollNo,
        name,
        fatherName,
        section,
        attendance:"95%",
        rank:"",
        remarks:"Satisfactory performance.",
        marks
      });
    }
    if(parsedStudents.length>0){
      Z(prev=>({...prev,students:parsedStudents}));
      F(`کامیابی کے ساتھ ${parsedStudents.length} طلباء کا ڈیٹا امپورٹ ہو گیا!`);
    }
  };
  reader.readAsText(file);
  if(fileInputRef.current)fileInputRef.current.value="";
},
printAllCardsAction=()=>{
  setPrintOrientation(msOrientation);
  const prevTitle=document.title;
  document.title=`All_Result_Cards_${R.classLevel.replace(/\\s+/g,"_")}_${R.session}_${msOrientation.toUpperCase()}`;
  window.print();
  setTimeout(()=>{document.title=prevTitle},1500);
},'''

if old_lq_marker in text and "autoCalculateRanks" not in text:
    text = text.replace(old_lq_marker, new_lq_marker, 1)
    print("[✓] Added helper functions to lq")

# In ue and Ce: call setPrintOrientation(msOrientation)
old_ue = 'ue=S=>{const V=document.title;document.title=`Result_Card_Roll_${S.rollNo}_${S.name.replace(/\\s+/g,"_")}`,window.print(),setTimeout(()=>{document.title=V},1500)}'
new_ue = 'ue=S=>{setPrintOrientation(msOrientation);const V=document.title;document.title=`Result_Card_Roll_${S.rollNo}_${S.name.replace(/\\s+/g,"_")}_${msOrientation.toUpperCase()}`,window.print(),setTimeout(()=>{document.title=V},1500)}'
if old_ue in text:
    text = text.replace(old_ue, new_ue, 1)

old_Ce = 'Ce=()=>{o("masterSheet");const S=document.title;document.title=`Master_Marksheet_${R.classLevel.replace(/\\s+/g,"_")}`,window.print(),setTimeout(()=>{document.title=S},1500)}'
new_Ce = 'Ce=()=>{o("masterSheet");setPrintOrientation(msOrientation);const S=document.title;document.title=`Master_Marksheet_${R.classLevel.replace(/\\s+/g,"_")}_${msOrientation.toUpperCase()}`,window.print(),setTimeout(()=>{document.title=S},1500)}'
if old_Ce in text:
    text = text.replace(old_Ce, new_Ce, 1)

# In Ne (PDF single card): pass msOrientation to iC
old_Ne = 'await iC("resultcard-print-container",V,ae=>{C(ae)})&&F("Result Card PDF downloaded successfully!")'
new_Ne = 'await iC("resultcard-print-container",V,ae=>{C(ae)},msOrientation)&&F(`Result Card PDF downloaded successfully in ${msOrientation} orientation!`)'
if old_Ne in text:
    text = text.replace(old_Ne, new_Ne, 1)

# In k (PDF master sheet): pass msOrientation to iC
old_k = 'await iC("mastersheet-print-container",S,q=>{C(q)})&&F("Master Marksheet PDF downloaded successfully!")'
new_k = 'await iC("mastersheet-print-container",S,q=>{C(q)},msOrientation)&&F(`Master Marksheet PDF downloaded successfully in ${msOrientation} orientation!`)'
if old_k in text:
    text = text.replace(old_k, new_k, 1)

# In lq's return statement: add the top management banner
old_lq_return = 'return l.jsxs("div",{className:"space-y-6 max-w-7xl mx-auto font-sans text-slate-800",children:[y&&l.jsxs("div",{className:"fixed top-16 right-6 z-50 bg-slate-900 text-white px-4 py-2.5 rounded-xl shadow-2xl text-xs font-bold flex items-center gap-2 animate-in fade-in slide-in-from-top-2 no-print",children:[l.jsx(TC,{className:"w-4 h-4 text-emerald-400"}),l.jsx("span",{children:y})]}),l.jsx("input",{ref:E,type:"file",accept:"image/*",className:"hidden",onChange:ce}),'

new_lq_return = '''return l.jsxs("div",{className:"space-y-6 max-w-7xl mx-auto font-sans text-slate-800",children:[y&&l.jsxs("div",{className:"fixed top-16 right-6 z-50 bg-slate-900 text-white px-4 py-2.5 rounded-xl shadow-2xl text-xs font-bold flex items-center gap-2 animate-in fade-in slide-in-from-top-2 no-print",children:[l.jsx(TC,{className:"w-4 h-4 text-emerald-400"}),l.jsx("span",{children:y})]}),
l.jsx("input",{ref:E,type:"file",accept:"image/*",className:"hidden",onChange:ce}),
l.jsx("input",{ref:fileInputRef,type:"file",accept:".csv,.tsv,.txt",className:"hidden",onChange:handleImportCSV}),
l.jsxs("div",{className:"bg-gradient-to-r from-blue-900 via-indigo-900 to-slate-900 text-white p-3.5 sm:p-4 rounded-2xl shadow-lg border border-blue-700 flex flex-wrap items-center justify-between gap-3 no-print",children:[
  l.jsxs("div",{className:"flex items-center gap-2 flex-wrap",children:[
    l.jsx("span",{className:"text-xs font-black uppercase tracking-wider text-amber-300 flex items-center gap-1",children:[l.jsx("span",{children:"📚"}),l.jsx("span",{children:"Class Data & Controls:"})]}),
    l.jsxs("button",{type:"button",onClick:()=>fileInputRef.current&&fileInputRef.current.click(),className:"btn-3d bg-slate-800 hover:bg-slate-700 border border-slate-600 flex items-center gap-1.5 px-3 py-1.5 text-white rounded-xl text-xs font-black cursor-pointer shadow-sm",title:"Import student marks from Excel / CSV",children:[l.jsx("span",{children:"📥"}),l.jsx("span",{children:"Import Marks (CSV/Excel)"})]}),
    l.jsxs("button",{type:"button",onClick:autoCalculateRanks,className:"btn-3d btn-3d-amber flex items-center gap-1.5 px-3 py-1.5 text-slate-950 rounded-xl text-xs font-black cursor-pointer shadow-sm hover:brightness-110",title:"Auto calculate student class positions (1st, 2nd, 3rd) based on total marks",children:[l.jsx("span",{children:"⚡"}),l.jsx("span",{children:"Auto-Calculate Positions (پوزیشنز)"})]})
  ]}),
  l.jsxs("div",{className:"flex items-center gap-2 flex-wrap",children:[
    l.jsxs("button",{type:"button",onClick:()=>exportMasterGazetteToExcel(R,r,m_sec),className:"btn-3d btn-3d-green flex items-center gap-1.5 px-3.5 py-1.5 text-white rounded-xl text-xs font-black cursor-pointer shadow-sm hover:brightness-110",title:"Download complete class marksheet data in Excel (.xls) format",children:[l.jsx("span",{children:"📊"}),l.jsx("span",{children:"Class Excel (.xls)"})]}),
    l.jsxs("button",{type:"button",onClick:()=>exportWholeSchoolConsolidatedGazette([R],r),className:"btn-3d bg-purple-700 hover:bg-purple-600 flex items-center gap-1.5 px-3.5 py-1.5 text-white rounded-xl text-xs font-black cursor-pointer shadow-sm hover:brightness-110",title:"Export Whole School Consolidated Gazette across multiple grades",children:[l.jsx("span",{children:"🏫"}),l.jsx("span",{children:"Whole School Gazette"})]})
  ]})
]}),'''

if old_lq_return in text and "Class Data & Controls:" not in text:
    text = text.replace(old_lq_return, new_lq_return, 1)
    print("[✓] Added top management banner in lq")

# In singleCard toolbar: add orientation switcher and "Print ALL Cards"
old_single_card_toolbar = 'title:"Download single student result card Word (.doc)",children:[l.jsx(Xu,{className:"w-4 h-4 text-blue-200"}),l.jsx("span",{children:"Download Card (.doc)"})]})]})'
new_single_card_toolbar = '''title:"Download single student result card Word (.doc)",children:[l.jsx(Xu,{className:"w-4 h-4 text-blue-200"}),l.jsx("span",{children:"Download Card (.doc)"})]}),
l.jsxs("button",{type:"button",onClick:printAllCardsAction,className:"btn-3d btn-3d-purple flex items-center gap-1.5 px-3.5 py-2.5 text-white rounded-xl text-xs font-black cursor-pointer shadow-md",title:"Print ALL students result cards in one go",children:[l.jsx(SAFE_od,{className:"w-4 h-4 text-purple-200"}),l.jsx("span",{children:"Print ALL Cards"})]}),
l.jsxs("div",{className:"flex items-center gap-1 bg-slate-100 p-1 rounded-xl border border-slate-200 no-print",children:[
  l.jsxs("button",{type:"button",onClick:()=>{setMsOrientation("portrait");setPrintOrientation("portrait");},className:`flex items-center gap-1 px-3 py-1.5 rounded-lg text-xs font-bold transition-all cursor-pointer ${msOrientation==="portrait"?"bg-white text-blue-700 shadow-xs font-black ring-1 ring-blue-300":"text-slate-600 hover:text-slate-900"}`,title:"Portrait (Vertical)",children:[l.jsx("span",{children:"📄"}),l.jsx("span",{children:"Portrait (عمودی)"})]}),
  l.jsxs("button",{type:"button",onClick:()=>{setMsOrientation("landscape");setPrintOrientation("landscape");},className:`flex items-center gap-1 px-3 py-1.5 rounded-lg text-xs font-bold transition-all cursor-pointer ${msOrientation==="landscape"?"bg-white text-blue-700 shadow-xs font-black ring-1 ring-blue-300":"text-slate-600 hover:text-slate-900"}`,title:"Landscape (Horizontal)",children:[l.jsx("span",{children:"📑"}),l.jsx("span",{children:"Landscape (افقی)"})]})
]})]})'''

if old_single_card_toolbar in text:
    text = text.replace(old_single_card_toolbar, new_single_card_toolbar, 1)
    print("[✓] Added Print ALL Cards and orientation switcher in singleCard toolbar")

# In masterSheet toolbar: add orientation switcher
old_ms_toolbar = 'title:"Print full class master sheet / broadsheet",children:[l.jsx(SAFE_od,{className:"w-4 h-4 text-emerald-100"}),l.jsx("span",{children:"Print & Preview"})]})'
new_ms_toolbar = '''title:"Print full class master sheet / broadsheet",children:[l.jsx(SAFE_od,{className:"w-4 h-4 text-emerald-100"}),l.jsx("span",{children:"Print & Preview"})]}),
l.jsxs("div",{className:"flex items-center gap-1 bg-slate-100 p-1 rounded-xl border border-slate-200 mr-1 no-print",children:[
  l.jsxs("button",{type:"button",onClick:()=>{setMsOrientation("portrait");setPrintOrientation("portrait");},className:`flex items-center gap-1 px-3 py-1.5 rounded-lg text-xs font-bold transition-all cursor-pointer ${msOrientation==="portrait"?"bg-white text-blue-700 shadow-xs font-black ring-1 ring-blue-300":"text-slate-600 hover:text-slate-900"}`,title:"Portrait (Vertical)",children:[l.jsx("span",{children:"📄"}),l.jsx("span",{children:"Portrait (عمودی)"})]}),
  l.jsxs("button",{type:"button",onClick:()=>{setMsOrientation("landscape");setPrintOrientation("landscape");},className:`flex items-center gap-1 px-3 py-1.5 rounded-lg text-xs font-bold transition-all cursor-pointer ${msOrientation==="landscape"?"bg-white text-blue-700 shadow-xs font-black ring-1 ring-blue-300":"text-slate-600 hover:text-slate-900"}`,title:"Landscape (Horizontal)",children:[l.jsx("span",{children:"📑"}),l.jsx("span",{children:"Landscape (افقی)"})]})
]})'''

if old_ms_toolbar in text:
    text = text.replace(old_ms_toolbar, new_ms_toolbar, 1)
    print("[✓] Added orientation switcher in masterSheet toolbar")

# In resultcard-print-container, make width dynamic based on msOrientation
old_rc_c = 'id:"resultcard-print-container",className:"bg-white rounded-2xl shadow-xl border border-slate-300 p-6 sm:p-10 max-w-4xl mx-auto'
new_rc_c = 'id:"resultcard-print-container",className:`bg-white rounded-2xl shadow-xl border border-slate-300 p-6 sm:p-10 ${msOrientation==="landscape"?"max-w-6xl landscape-mode":"max-w-4xl portrait-mode"} mx-auto`'
if old_rc_c in text:
    text = text.replace(old_rc_c, new_rc_c, 1)

# In mastersheet-print-container, make width dynamic based on msOrientation
old_ms_c = 'id:"mastersheet-print-container",className:"bg-white rounded-2xl shadow-xl border border-slate-300 p-6 sm:p-8 max-w-5xl mx-auto'
new_ms_c = 'id:"mastersheet-print-container",className:`bg-white rounded-2xl shadow-xl border border-slate-300 p-6 sm:p-8 ${msOrientation==="landscape"?"max-w-7xl landscape-mode":"max-w-5xl portrait-mode"} mx-auto`'
if old_ms_c in text:
    text = text.replace(old_ms_c, new_ms_c, 1)

with open("assets/index-DAioIUjd.js", "w", encoding="utf-8") as f:
    f.write(text)

print("[✓] Successfully wrote all marksheet feature expansions!")
