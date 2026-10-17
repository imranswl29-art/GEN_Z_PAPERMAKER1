import os
import subprocess
import re

print("=== Assembling Clean Refactored Bundle ===")

# Read orig (from DPUomzbq which has full aq, lq, eq)
with open('assets/index-DPUomzbq.js', 'r', encoding='utf-8') as f:
    orig = f.read()

# Read curr (from DAioIUjd which has Notes, Question Bank, and other features)
with open('assets/index-DAioIUjd.js', 'r', encoding='utf-8') as f:
    curr = f.read()

# 1. First, restore eq, aq, and lq from orig into curr to fix the accidental truncation
pos_eq_orig = orig.find('function eq(n,e){')
pos_Aq_orig = orig.find('Aq=({currentUser:n})=>')

pos_eq_curr = curr.find('function eq(n,e){')
pos_Aq_curr = curr.find('Aq=({currentUser:n})=>')

assert pos_eq_orig != -1 and pos_Aq_orig != -1, "Orig boundaries not found"
assert pos_eq_curr != -1 and pos_Aq_curr != -1, "Curr boundaries not found"

# Extract full eq, aq, lq from orig
eq_aq_lq_block = orig[pos_eq_orig:pos_Aq_orig]
print(f"Extracted eq_aq_lq_block from orig ({len(eq_aq_lq_block)} chars)")

# Splice into curr
text = curr[:pos_eq_curr] + eq_aq_lq_block + curr[pos_Aq_curr:]
print(f"Spliced into curr. Current text length: {len(text)}")

# -------------------------------------------------------------------------
# 2. Add Helper Functions (setPrintOrientation, exportWholeSchoolConsolidatedGazette)
# -------------------------------------------------------------------------
# Add setPrintOrientation if not already defined
# Ensure iC is async without duplicates
text = re.sub(r'(?:async\s+)*function\s+iC\(n,e,t,orientation\s*=\s*"portrait"\)', 'async function iC(n,e,t,orientation = "portrait")', text)

if "function setPrintOrientation" not in text:
    old_iC = 'function iC(n,e,t){const r=document.getElementById(n);if(!r)return console.error(`Target element with id "${n}" not found for PDF export.`),window.print(),!1;try{t&&t("Rendering high-resolution A4 document..."),await new Promise(y=>setTimeout(y,150));const a=210,o=297,A=8,u=8,f=a-A*2,B=o-u*2,m=new Xt({orientation:"portrait",unit:"mm",format:"a4",compress:!0});await Oh(r,m,f,B,A,u,!0);const C=e.endsWith(".pdf")?e:`${e}.pdf`;return m.save(C),t&&t("Downloaded successfully!"),!0}catch(a){return console.warn("PDF export error, falling back to print:",a),window.print(),!1}}'
    new_iC = '''function setPrintOrientation(orientation = "portrait"){let s=document.getElementById("print-orientation-style");if(!s){s=document.createElement("style");s.id="print-orientation-style";document.head.appendChild(s);}s.innerHTML=`@media print { @page { size: ${orientation} !important; margin: 6mm !important; } }`;}
async function iC(n,e,t,orientation = "portrait"){const r=document.getElementById(n);if(!r)return console.error(`Target element with id "${n}" not found for PDF export.`),window.print(),!1;try{t&&t("Rendering high-resolution A4 document..."),await new Promise(y=>setTimeout(y,150));const isLand=orientation==="landscape";const a=isLand?297:210,o=isLand?210:297,A=8,u=8,f=a-A*2,B=o-u*2,m=new Xt({orientation:isLand?"landscape":"portrait",unit:"mm",format:"a4",compress:!0});await Oh(r,m,f,B,A,u,!0);const C=e.endsWith(".pdf")?e:`${e}.pdf`;return m.save(C),t&&t("Downloaded successfully!"),!0}catch(a){return console.warn("PDF export error, falling back to print:",a),window.print(),!1}}'''
    if old_iC in text:
        text = text.replace(old_iC, new_iC, 1)
        print("[✓] Added setPrintOrientation and updated iC")
    else:
        print("[i] old_iC not found or already updated")

# Add exportWholeSchoolConsolidatedGazette and exportMasterGazetteToExcel helpers before aq
ws_gazette_code = '''
function exportWholeSchoolConsolidatedGazette(sheetsList, brand) {
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
        if (m < (sub.passingMarks || 0)) isPass = false;
      });
      if (isPass) passedCount++; else failedCount++;
      return { ...st, obt };
    });
    scored.sort((a, b) => b.obt - a.obt);
    const top1 = scored[0] ? `${scored[0].name} (${scored[0].obt}/${totalSubs})` : "-";
    const top2 = scored[1] ? `${scored[1].name} (${scored[1].obt}/${totalSubs})` : "-";
    const top3 = scored[2] ? `${scored[2].name} (${scored[2].obt}/${totalSubs})` : "-";
    const passPct = count > 0 ? (passedCount / count * 100).toFixed(1) : "0.0";
    const bg = idx % 2 === 0 ? "#ffffff" : "#f8fafc";
    rows += `
      <tr>
        <td align="center" style="background-color: ${bg}; padding: 6pt; border: 1pt solid #cbd5e1;">${idx + 1}</td>
        <td style="background-color: ${bg}; padding: 6pt; border: 1pt solid #cbd5e1; font-weight: bold; color: #1e3a8a;">${sheet.classLevel}</td>
        <td align="center" style="background-color: ${bg}; padding: 6pt; border: 1pt solid #cbd5e1;">${sheet.session}</td>
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
function exportMasterGazetteToExcel(sheet, brand, sectionFilter = "all") {
  const brandTitle = (brand && (brand.instituteName || brand.schoolName)) || "PUNJAB GROUP OF SCIENCE ACADEMIES";
  const brandCampus = (brand && (brand.campusName || brand.address)) || "Main Campus, Lahore";
  const subjects = sheet.subjects || [];
  const allStudents = sheet.students || [];
  const students = sectionFilter === "all" ? allStudents : allStudents.filter(s => (s.section || "A").toUpperCase() === sectionFilter.toUpperCase());
  const grandTotalMarks = subjects.reduce((sum, s) => sum + s.totalMarks, 0);

  let subHeaders = "";
  subjects.forEach(s => {
    subHeaders += `<th style="background-color:#1e3a8a;color:#ffffff;padding:6pt 4pt;border:1pt solid #93c5fd;font-size:9pt;text-align:center;">${s.name}<br/><span style="font-size:7.5pt;font-weight:normal;">(${s.totalMarks})</span></th>`;
  });

  let studentRows = "";
  students.forEach((st, idx) => {
    let obt = 0;
    let isPass = true;
    let markCols = "";
    subjects.forEach(sub => {
      const m = Number((st.marks && st.marks[sub.id]) || 0);
      obt += m;
      const pass = sub.passingMarks || 0;
      const isFailed = m < pass;
      if (isFailed) isPass = false;
      markCols += `<td align="center" style="border:1pt solid #cbd5e1;padding:5pt;font-weight:bold;${isFailed ? 'color:#b91c1c;background-color:#fee2e2;' : 'color:#1e293b;'}">${m}</td>`;
    });
    const pct = grandTotalMarks > 0 ? (obt / grandTotalMarks * 100).toFixed(1) : "0.0";
    const grade = pct >= 80 ? "A+" : pct >= 70 ? "A" : pct >= 60 ? "B" : pct >= 50 ? "C" : pct >= 40 ? "D" : pct >= 33 ? "E" : "F";
    const bg = idx % 2 === 0 ? "#ffffff" : "#f8fafc";
    studentRows += `
      <tr style="background-color:${bg};">
        <td align="center" style="border:1pt solid #cbd5e1;padding:5pt;font-weight:bold;">${st.rollNo}</td>
        <td style="border:1pt solid #cbd5e1;padding:5pt;font-weight:bold;color:#1e3a8a;">${st.name}</td>
        <td style="border:1pt solid #cbd5e1;padding:5pt;color:#475569;">${st.fatherName || "-"}</td>
        <td align="center" style="border:1pt solid #cbd5e1;padding:5pt;font-weight:bold;">${st.section || "A"}</td>
        ${markCols}
        <td align="center" style="border:1pt solid #cbd5e1;padding:5pt;font-weight:bold;color:#0f172a;background-color:#f1f5f9;">${obt} / ${grandTotalMarks}</td>
        <td align="center" style="border:1pt solid #cbd5e1;padding:5pt;font-weight:bold;color:#1d4ed8;background-color:#eff6ff;">${pct}%</td>
        <td align="center" style="border:1pt solid #cbd5e1;padding:5pt;font-weight:bold;${isPass ? 'color:#047857;background-color:#ecfdf5;' : 'color:#b91c1c;background-color:#fee2e2;'}">${grade}</td>
        <td align="center" style="border:1pt solid #cbd5e1;padding:5pt;font-weight:bold;color:#7c3aed;">${st.rank || "-"}</td>
        <td align="center" style="border:1pt solid #cbd5e1;padding:5pt;font-weight:bold;color:${isPass ? '#047857' : '#b91c1c'};">${isPass ? "PASS" : "FAIL"}</td>
      </tr>
    `;
  });

  const html = `<!DOCTYPE html><html xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:x="urn:schemas-microsoft-com:office:excel" xmlns="http://www.w3.org/TR/REC-html40">
  <head><meta http-equiv="Content-Type" content="application/vnd.ms-excel; charset=utf-8">
  <title>${brandTitle} - Master Marksheet Gazette</title>
  <style>
    body { font-family: 'Segoe UI', Calibri, Arial, sans-serif; font-size: 10pt; }
    table { border-collapse: collapse; width: 100%; }
    .header { background-color: #0f2942; color: #ffffff; font-size: 14pt; font-weight: bold; text-align: center; padding: 12pt; }
    .sub { background-color: #1e3a8a; color: #e2e8f0; font-size: 10pt; text-align: center; padding: 6pt; }
  </style>
  </head>
  <body>
    <table>
      <tr><td colspan="${7 + subjects.length}" class="header">${brandTitle}</td></tr>
      <tr><td colspan="${7 + subjects.length}" class="sub">${brandCampus} &bull; CONSOLIDATED MASTER MARKSHEET GAZETTE &bull; CLASS: ${sheet.classLevel.toUpperCase()} &bull; SESSION: ${sheet.session} ${sectionFilter !== "all" ? `&bull; SECTION: ${sectionFilter}` : ""}</td></tr>
      <tr><td colspan="${7 + subjects.length}" style="padding: 4pt;"></td></tr>
      <thead>
        <tr style="background-color:#0f172a;color:#ffffff;font-size:9.5pt;">
          <th style="padding:6pt;border:1pt solid #475569;">Roll #</th>
          <th style="padding:6pt;border:1pt solid #475569;">Student Name</th>
          <th style="padding:6pt;border:1pt solid #475569;">Father's Name</th>
          <th style="padding:6pt;border:1pt solid #475569;">Sec</th>
          ${subHeaders}
          <th style="padding:6pt;border:1pt solid #475569;background-color:#0284c7;">Total Obt</th>
          <th style="padding:6pt;border:1pt solid #475569;background-color:#2563eb;">%</th>
          <th style="padding:6pt;border:1pt solid #475569;background-color:#4f46e5;">Grade</th>
          <th style="padding:6pt;border:1pt solid #475569;background-color:#7c3aed;">Pos</th>
          <th style="padding:6pt;border:1pt solid #475569;background-color:#059669;">Status</th>
        </tr>
      </thead>
      <tbody>
        ${studentRows}
      </tbody>
    </table>
  </body></html>`;

  const blob = new Blob(["\\ufeff", html], { type: "application/vnd.ms-excel;charset=utf-8" });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = `${brandTitle.replace(/\\s+/g, "_")}_${sheet.classLevel.replace(/\\s+/g, "_")}_Master_Gazette.xls`;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
}
'''

if "function exportWholeSchoolConsolidatedGazette" not in text:
    target_rq = 'const rq=["Students must report'
    text = text.replace(target_rq, ws_gazette_code + "\n" + target_rq, 1)
    print("[✓] Added Excel & Whole School Gazette helper functions before const rq")

# -------------------------------------------------------------------------
# 3. Refactor Date Sheet (aq) Toolbar & Orientation
# -------------------------------------------------------------------------
# Add dsOrientation state to aq
old_aq_state = 'const r=_T(n,e),[a,o]=Ee.useState("editor"),[A,u]=Ee.useState(!1),[f,B]=Ee.useState(""),[m,C]=Ee.useState(null),'
new_aq_state = 'const r=_T(n,e),[a,o]=Ee.useState("editor"),[A,u]=Ee.useState(!1),[f,B]=Ee.useState(""),[m,C]=Ee.useState(null),[dsOrientation,setDsOrientation]=Ee.useState("portrait"),'
if old_aq_state in text:
    text = text.replace(old_aq_state, new_aq_state, 1)

# Update T in aq to setPrintOrientation
old_aq_T = 'T=()=>{const D=document.title,U=E.classLevel.replace(/\\s+/g,"_"),Q=F.replace(/\\s+/g,"_");document.title=`${U}_Date_Sheet_${Q}`,window.print(),setTimeout(()=>{document.title=D},1500)}'
new_aq_T = 'T=()=>{setPrintOrientation(dsOrientation);const D=document.title,U=E.classLevel.replace(/\\s+/g,"_"),Q=F.replace(/\\s+/g,"_");document.title=`${U}_Date_Sheet_${Q}_${dsOrientation.toUpperCase()}`,window.print(),setTimeout(()=>{document.title=D},1500)}'
if old_aq_T in text:
    text = text.replace(old_aq_T, new_aq_T, 1)

# Update H in aq to pass dsOrientation to iC
old_aq_H = 'await iC("datesheet-print-container",Q,pe=>{B(pe)})&&y("Date Sheet PDF downloaded successfully!")'
new_aq_H = 'await iC("datesheet-print-container",Q,pe=>{B(pe)},dsOrientation)&&y(`Date Sheet PDF downloaded successfully in ${dsOrientation} orientation!`)'
if old_aq_H in text:
    text = text.replace(old_aq_H, new_aq_H, 1)

# Replace aq action buttons with Segmented Pills + Print + Modern "Downloads ▾" Dropdown
old_aq_btns = 'l.jsxs("div",{className:"flex flex-wrap items-center gap-2",children:[l.jsxs("button",{type:"button",onClick:T,className:"btn-print-preview",title:"Open browser print dialog for A4 Date Sheet",children:[l.jsx(SAFE_od,{className:"w-4 h-4 text-emerald-100"}),l.jsx("span",{children:"Print & Preview"})]}),l.jsxs("button",{type:"button",onClick:H,disabled:A,className:"btn-3d btn-3d-red flex items-center gap-2 px-4 py-2.5 text-white rounded-xl text-xs font-black cursor-pointer shadow-md disabled:opacity-50",title:"Download high-resolution PDF",children:[A?l.jsx(Sc,{className:"w-4 h-4 animate-spin"}):l.jsx(SAFE_ad,{className:"w-4 h-4"}),l.jsx("span",{children:A?f||"Rendering PDF...":"Download PDF"})]}),l.jsxs("button",{type:"button",onClick:G,className:"btn-3d btn-3d-navy flex items-center gap-2 px-4 py-2.5 text-white rounded-xl text-xs font-black cursor-pointer shadow-md",title:"Download editable Microsoft Word .doc file",children:[l.jsx(Xu,{className:"w-4 h-4 text-blue-200"}),l.jsx("span",{children:"Download Word (.doc)"})]})]})'
new_aq_btns = '''l.jsxs("div",{className:"flex flex-wrap items-center gap-2",children:[l.jsxs("div",{className:"flex items-center gap-1 bg-slate-100 p-1 rounded-xl border border-slate-200 no-print",children:[l.jsxs("button",{type:"button",onClick:()=>{setDsOrientation("portrait");setPrintOrientation("portrait");},className:`flex items-center gap-1 px-3 py-1.5 rounded-lg text-xs font-bold transition-all cursor-pointer ${dsOrientation==="portrait"?"bg-white text-blue-700 shadow-xs font-black ring-1 ring-blue-300":"text-slate-600 hover:text-slate-900"}`,title:"Portrait (Vertical Orientation)",children:[l.jsx("span",{children:"📄"}),l.jsx("span",{children:"Portrait"})]}),l.jsxs("button",{type:"button",onClick:()=>{setDsOrientation("landscape");setPrintOrientation("landscape");},className:`flex items-center gap-1 px-3 py-1.5 rounded-lg text-xs font-bold transition-all cursor-pointer ${dsOrientation==="landscape"?"bg-white text-blue-700 shadow-xs font-black ring-1 ring-blue-300":"text-slate-600 hover:text-slate-900"}`,title:"Landscape (Horizontal Orientation)",children:[l.jsx("span",{children:"📑"}),l.jsx("span",{children:"Landscape"})]})]}),l.jsxs("button",{type:"button",onClick:T,className:"btn-print-preview",title:"Open browser print dialog for A4 Date Sheet",children:[l.jsx(SAFE_od,{className:"w-4 h-4 text-emerald-100"}),l.jsx("span",{children:"Print & Preview"})]}),l.jsxs("details",{className:"relative inline-block text-left no-print",children:[l.jsxs("summary",{className:"btn-3d btn-3d-red flex items-center gap-2 px-4 py-2 text-white rounded-xl text-xs font-black cursor-pointer shadow-md list-none select-none",title:"Export & Download Options",children:[A?l.jsx(Sc,{className:"w-4 h-4 animate-spin"}):l.jsx(SAFE_ad,{className:"w-4 h-4 text-white"}),l.jsx("span",{children:A?f||"Rendering...":"Downloads ▾"})]}),l.jsxs("div",{className:"dropdown-menu-panel",children:[l.jsxs("button",{type:"button",onClick:e=>{e.currentTarget.closest("details")?.removeAttribute("open");H();},disabled:A,className:"dropdown-menu-item text-rose-700 hover:bg-rose-50",title:"Download high-resolution PDF",children:[l.jsx(SAFE_ad,{className:"w-3.5 h-3.5 text-rose-600"}),l.jsx("span",{children:"Download PDF (.pdf)"})]}),l.jsxs("button",{type:"button",onClick:e=>{e.currentTarget.closest("details")?.removeAttribute("open");G();},className:"dropdown-menu-item text-blue-700 hover:bg-blue-50",title:"Download editable Microsoft Word document",children:[l.jsx(Xu,{className:"w-3.5 h-3.5 text-blue-600"}),l.jsx("span",{children:"Download Word (.doc)"})]})]})]})]})'''

if old_aq_btns in text:
    text = text.replace(old_aq_btns, new_aq_btns, 1)
    print("[✓] Date Sheet Generator toolbar refactored into compact dropdown & orientation pills")
else:
    print("[!] old_aq_btns not found")

# Make datesheet container responsive to orientation
old_ds_container = 'className:`${a==="preview"?"block":"hidden print:block"} bg-white rounded-2xl shadow-xl border border-slate-300 p-6 sm:p-10 max-w-4xl mx-auto print:border-none print:shadow-none print:p-0 print:m-0 print:max-w-none print:w-full`,id:"datesheet-print-container"'
new_ds_container = 'className:`${a==="preview"?"block":"hidden print:block"} bg-white rounded-2xl shadow-xl border border-slate-300 p-6 sm:p-10 ${dsOrientation==="landscape"?"max-w-6xl landscape-mode":"max-w-4xl portrait-mode"} mx-auto print:border-none print:shadow-none print:p-0 print:m-0 print:max-w-none print:w-full`,id:"datesheet-print-container"'
if old_ds_container in text:
    text = text.replace(old_ds_container, new_ds_container, 1)

# -------------------------------------------------------------------------
# 4. Refactor Result Card & Marksheet Generator (lq)
# -------------------------------------------------------------------------
# Add state to lq: msOrientation, studentSearch, printAllCards, savedSheets, m_sec
old_lq_state = 'lq=({currentUser:n,activeHeader:e,onOpenSchoolProfile:t})=>{const r=_T(n,e),[a,o]=Ee.useState("editor"),[A,u]=Ee.useState("st-1"),[f,B]=Ee.useState(!1),[m,C]=Ee.useState(""),[y,v]=Ee.useState(null),E=Ee.useRef(null),[I,O]=Ee.useState(null),F=S=>{v(S),setTimeout(()=>v(null),3e3)},'
new_lq_state = '''lq=({currentUser:n,activeHeader:e,onOpenSchoolProfile:t})=>{const r=_T(n,e),[a,o]=Ee.useState("editor"),[A,u]=Ee.useState("st-1"),[m_sec,setM_sec]=Ee.useState("all"),[f,B]=Ee.useState(!1),[m,C]=Ee.useState(""),[y,v]=Ee.useState(null),E=Ee.useRef(null),[I,O]=Ee.useState(null),[msOrientation,setMsOrientation]=Ee.useState("portrait"),[studentSearch,setStudentSearch]=Ee.useState(""),[printAllCards,setPrintAllCards]=Ee.useState(!1),[savedSheets,setSavedSheets]=Ee.useState(()=>{try{const raw=localStorage.getItem("ptbb_all_marksheets");if(raw){const p=JSON.parse(raw);if(Array.isArray(p)&&p.length>0)return p;}}catch(e){}return[];}),F=S=>{v(S),setTimeout(()=>v(null),3e3)},'''

if old_lq_state in text:
    text = text.replace(old_lq_state, new_lq_state, 1)

# Add helper actions inside lq right before const ne=R.subjects.reduce
old_lq_actions = '''const ne=R.subjects.reduce((S,V)=>S+V.totalMarks,0),'''
new_lq_actions = '''const fileInputRef = Ee.useRef(null);
const autoCalculateRanks = () => {
  const list = [...R.students];
  const withScores = list.map(st => {
    const tot = R.subjects.reduce((sum, sub) => sum + Number((st.marks && st.marks[sub.id]) || 0), 0);
    return { ...st, _tot: tot };
  });
  withScores.sort((a, b) => b._tot - a._tot);
  const updated = withScores.map((st, i) => {
    const pos = i === 0 ? "1st" : i === 1 ? "2nd" : i === 2 ? "3rd" : `${i + 1}th`;
    const { _tot, ...rest } = st;
    return { ...rest, rank: pos };
  });
  Z(prev => ({ ...prev, students: updated }));
  F("All student class positions and ranks calculated successfully!");
};
const setGlobalPassingPercentage = (pct = 33) => {
  Z(prev => ({
    ...prev,
    subjects: prev.subjects.map(s => ({
      ...s,
      passingMarks: Math.ceil(s.totalMarks * (pct / 100))
    }))
  }));
  F(`All subjects passing threshold updated to ${pct}%!`);
};
const handleImportCSV = (evt) => {
  const file = evt.target.files && evt.target.files[0];
  if (!file) return;
  const reader = new FileReader();
  reader.onload = (e) => {
    const content = e.target.result;
    if (typeof content !== "string") return;
    const lines = content.split(/\\r?\\n/).map(l => l.trim()).filter(Boolean);
    if (lines.length < 2) return alert("File is empty or invalid format.");
    const headers = lines[0].split(/[,\\t]/).map(h => h.trim().toLowerCase());
    const rollIdx = headers.findIndex(h => h.includes("roll"));
    const nameIdx = headers.findIndex(h => h.includes("name") && !h.includes("father"));
    const fatherIdx = headers.findIndex(h => h.includes("father"));
    const secIdx = headers.findIndex(h => h.includes("section") || h.includes("sec"));

    const subIndices = R.subjects.map(sub => {
      const idx = headers.findIndex(h => h.includes(sub.name.toLowerCase()) || sub.name.toLowerCase().includes(h));
      return { subId: sub.id, colIdx: idx };
    });

    const parsedStudents = [];
    for (let i = 1; i < lines.length; i++) {
      const cols = lines[i].split(/[,\\t]/).map(c => c.trim().replace(/^["']|["']$/g, ""));
      if (cols.length < 2) continue;
      const rollNo = rollIdx >= 0 ? cols[rollIdx] : String(i);
      const name = nameIdx >= 0 ? cols[nameIdx] : `Student ${i}`;
      const fatherName = fatherIdx >= 0 ? cols[fatherIdx] : "Father Name";
      const section = secIdx >= 0 ? cols[secIdx] : "A";
      const marks = {};
      subIndices.forEach(({ subId, colIdx }) => {
        if (colIdx >= 0 && cols[colIdx] !== undefined) {
          marks[subId] = Number(cols[colIdx]) || 0;
        }
      });
      parsedStudents.push({
        id: `st-${Date.now()}-${i}`,
        rollNo,
        name,
        fatherName,
        section,
        attendance: "95%",
        rank: "",
        remarks: "Satisfactory performance.",
        marks
      });
    }
    if (parsedStudents.length > 0) {
      Z(prev => ({ ...prev, students: parsedStudents }));
      F(`Successfully imported data for ${parsedStudents.length} students!`);
    }
  };
  reader.readAsText(file);
  if (fileInputRef.current) fileInputRef.current.value = "";
};
const saveCurrentSheet=(sheetToSave=R)=>{
  const updated={...sheetToSave,id:sheetToSave.id||`ms-${Date.now()}`,userId:(n&&n.id)||"guest",updatedAt:new Date().toISOString()};
  Z(updated);
  setSavedSheets(prev=>{
    const idx=prev.findIndex(s=>s.id===updated.id);
    const next=idx>=0?prev.map((s,i)=>i===idx?updated:s):[updated,...prev];
    localStorage.setItem("ptbb_all_marksheets",JSON.stringify(next));
    localStorage.setItem("ptbb_marksheet_data",JSON.stringify(updated));
    return next;
  });
  fetch("/api/marksheets",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(updated)}).catch(()=>{});
  F(`Class '${updated.classLevel}' Session '${updated.session}' data saved successfully!`);
};
const loadSavedSheet=(id)=>{
  const found=savedSheets.find(s=>s.id===id);
  if(found){
    Z(found);
    if(found.students&&found.students.length>0){u(found.students[0].id);}
    localStorage.setItem("ptbb_marksheet_data",JSON.stringify(found));
    F(`Loaded marksheet for '${found.classLevel}'`);
  }
};
const createNewSheetForClassSession=(cls="10th Class (Science Group)",sess="2025-2026")=>{
  const newSubs=[
    {id:"sub-1",name:"Physics",totalMarks:60,passingMarks:20},
    {id:"sub-2",name:"Chemistry",totalMarks:60,passingMarks:20},
    {id:"sub-3",name:"Biology / Comp",totalMarks:60,passingMarks:20},
    {id:"sub-4",name:"Mathematics",totalMarks:75,passingMarks:25},
    {id:"sub-5",name:"English",totalMarks:75,passingMarks:25},
    {id:"sub-6",name:"Urdu",totalMarks:75,passingMarks:25},
    {id:"sub-7",name:"Islamiyat",totalMarks:50,passingMarks:17},
    {id:"sub-8",name:"Tarjuma Quran",totalMarks:50,passingMarks:17}
  ];
  const newSheet={
    id:`ms-${Date.now()}-${Math.random().toString(36).substring(2,6)}`,
    classLevel:cls,
    session:sess,
    examCategory:"Annual Examination",
    subjects:newSubs,
    students:[
      {id:`st-${Date.now()}-1`,rollNo:"1",name:"Muhammad Ahmad",fatherName:"Muhammad Ali",section:"A",attendance:"98%",rank:"1st",remarks:"Excellent academic consistency.",marks:{}},
      {id:`st-${Date.now()}-2`,rollNo:"2",name:"Fatima Noor",fatherName:"Tariq Mahmood",section:"A",attendance:"95%",rank:"2nd",remarks:"Hardworking student.",marks:{}}
    ]
  };
  saveCurrentSheet(newSheet);
};
const printAllCardsAction=()=>{
  setPrintOrientation(msOrientation);
  const V=document.title;
  document.title=`All_Result_Cards_${R.classLevel.replace(/\\s+/g,"_")}_${R.session}_${msOrientation.toUpperCase()}`;
  setPrintAllCards(!0);
  setTimeout(()=>{
    window.print();
    setTimeout(()=>{
      document.title=V;
      setPrintAllCards(!1);
    },1500);
  },250);
};
const ne=R.subjects.reduce((S,V)=>S+V.totalMarks,0),'''

if old_lq_actions in text:
    text = text.replace(old_lq_actions, new_lq_actions, 1)

# Update handlers in lq to use msOrientation
old_ue = 'ue=S=>{const V=document.title;document.title=`Result_Card_Roll_${S.rollNo}_${S.name.replace(/\\s+/g,"_")}`,window.print(),setTimeout(()=>{document.title=V},1500)}'
new_ue = 'ue=S=>{setPrintOrientation(msOrientation);const V=document.title;document.title=`Result_Card_Roll_${S.rollNo}_${S.name.replace(/\\s+/g,"_")}_${msOrientation.toUpperCase()}`,window.print(),setTimeout(()=>{document.title=V},1500)}'
if old_ue in text:
    text = text.replace(old_ue, new_ue, 1)

old_Ne = 'await iC("resultcard-print-container",V,ae=>{C(ae)})&&F("Result Card PDF downloaded successfully!")'
new_Ne = 'await iC("resultcard-print-container",V,ae=>{C(ae)},msOrientation)&&F(`Result Card PDF downloaded successfully in ${msOrientation} orientation!`)'
if old_Ne in text:
    text = text.replace(old_Ne, new_Ne, 1)

old_Ce = 'Ce=()=>{o("masterSheet");const S=document.title;document.title=`Master_Marksheet_${R.classLevel.replace(/\\s+/g,"_")}`,window.print(),setTimeout(()=>{document.title=S},1500)}'
new_Ce = 'Ce=()=>{o("masterSheet");setPrintOrientation(msOrientation);const S=document.title;document.title=`Master_Marksheet_${R.classLevel.replace(/\\s+/g,"_")}_${msOrientation.toUpperCase()}`,window.print(),setTimeout(()=>{document.title=S},1500)}'
if old_Ce in text:
    text = text.replace(old_Ce, new_Ce, 1)

old_k = 'await iC("mastersheet-print-container",S,q=>{C(q)})&&F("Master Marksheet PDF downloaded successfully!")'
new_k = 'await iC("mastersheet-print-container",S,q=>{C(q)},msOrientation)&&F(`Master Marksheet PDF downloaded successfully in ${msOrientation} orientation!`)'
if old_k in text:
    text = text.replace(old_k, new_k, 1)

# Add Class & Session Bar at the top of lq
old_lq_card = 'l.jsxs("div",{className:"card-3d p-5 sm:p-6 bg-white border border-slate-200",children:[l.jsxs("div",{className:"flex flex-col lg:flex-row items-start lg:items-center justify-between gap-4",'
new_lq_top_bar = '''l.jsxs("div",{className:"bg-gradient-to-r from-blue-900 via-indigo-900 to-slate-900 text-white p-3.5 sm:p-4 rounded-2xl shadow-lg border border-blue-700 flex flex-wrap items-center justify-between gap-3 no-print",children:[l.jsxs("div",{className:"flex items-center gap-2.5 flex-wrap",children:[l.jsx("span",{className:"text-xs font-black uppercase tracking-wider text-amber-300 flex items-center gap-1",children:[l.jsx("span",{children:"📚"}),l.jsx("span",{children:"Class & Session Sheet:"})]}),l.jsxs("select",{value:R.id,onChange:S=>loadSavedSheet(S.target.value),className:"bg-slate-800 text-white font-black text-xs px-3 py-1.5 rounded-xl border border-blue-400 focus:ring-2 focus:ring-amber-400 cursor-pointer shadow-inner",children:[savedSheets.length===0&&l.jsx("option",{value:R.id,children:`${R.classLevel} • ${R.session}`}),savedSheets.map(s=>l.jsxs("option",{value:s.id,children:[s.classLevel," • Session ",s.session," (",(s.students||[]).length," Students)"]},s.id))]}),l.jsxs("button",{type:"button",onClick:()=>saveCurrentSheet(R),className:"btn-3d btn-3d-emerald flex items-center gap-1.5 px-3 py-1.5 text-white rounded-xl text-xs font-black cursor-pointer shadow-sm hover:brightness-110",title:"Save current class & session marksheet data permanently",children:[l.jsx("span",{children:"💾"}),l.jsx("span",{children:"Save Current Sheet Data"})]}),l.jsxs("button",{type:"button",onClick:()=>{const cls=prompt("Enter Class Name (e.g. 9th Science, 10th Arts, Grade 8):","10th Class (Science Group)");if(cls){const sess=prompt("Enter Academic Session (e.g. 2025-2026):",R.session||"2025-2026")||"2025-2026";createNewSheetForClassSession(cls,sess);}},className:"btn-3d bg-indigo-700 hover:bg-indigo-600 flex items-center gap-1.5 px-3 py-1.5 text-white rounded-xl text-xs font-black cursor-pointer shadow-sm",title:"Create a new class or session dataset",children:[l.jsx("span",{children:"➕"}),l.jsx("span",{children:"New Class / Session"})]})]}),l.jsxs("div",{className:"flex items-center gap-2",children:[l.jsxs("button",{type:"button",onClick:()=>exportMasterGazetteToExcel(R,r,m_sec),className:"btn-3d btn-3d-green flex items-center gap-1.5 px-3.5 py-1.5 text-white rounded-xl text-xs font-black cursor-pointer shadow-sm hover:brightness-110",title:"Download complete marksheet data in Excel (.xls) format anytime",children:[l.jsx("span",{children:"📊"}),l.jsx("span",{children:"Download in Excel"})]})]})]}),l.jsxs("div",{className:"card-3d p-5 sm:p-6 bg-white border border-slate-200",children:[l.jsxs("div",{className:"flex flex-col lg:flex-row items-start lg:items-center justify-between gap-4",'''

if old_lq_card in text:
    text = text.replace(old_lq_card, new_lq_top_bar, 1)

# Single Card Toolbar: Segmented Pills + Print + Modern "Downloads ▾" Dropdown
old_rc_single = 'a==="singleCard"&&P&&l.jsxs(l.Fragment,{children:[l.jsxs("button",{type:"button",onClick:()=>ue(P),className:"btn-print-preview",title:"Print single student result card on standard A4",children:[l.jsx(SAFE_od,{className:"w-4 h-4 text-emerald-100"}),l.jsx("span",{children:"Print & Preview"})]}),l.jsxs("button",{type:"button",onClick:()=>Ne(P),disabled:f,className:"btn-3d btn-3d-red flex items-center gap-2 px-4 py-2.5 text-white rounded-xl text-xs font-black cursor-pointer shadow-md disabled:opacity-50",title:"Download single student result card PDF",children:[f?l.jsx(Sc,{className:"w-4 h-4 animate-spin"}):l.jsx(SAFE_ad,{className:"w-4 h-4"}),l.jsx("span",{children:f?m||"Rendering...":"Download Card (PDF)"})]}),l.jsxs("button",{type:"button",onClick:()=>Le(P),className:"btn-3d btn-3d-navy flex items-center gap-2 px-4 py-2.5 text-white rounded-xl text-xs font-black cursor-pointer shadow-md",title:"Download single student result card Word (.doc)",children:[l.jsx(Xu,{className:"w-4 h-4 text-blue-200"}),l.jsx("span",{children:"Download Card (.doc)"})]})]})'
new_rc_single = '''a==="singleCard"&&P&&l.jsxs(l.Fragment,{children:[l.jsxs("div",{className:"flex items-center gap-1 bg-slate-100 p-1 rounded-xl border border-slate-200 no-print",children:[l.jsxs("button",{type:"button",onClick:()=>{setMsOrientation("portrait");setPrintOrientation("portrait");},className:`flex items-center gap-1 px-3 py-1.5 rounded-lg text-xs font-bold transition-all cursor-pointer ${msOrientation==="portrait"?"bg-white text-blue-700 shadow-xs font-black ring-1 ring-blue-300":"text-slate-600 hover:text-slate-900"}`,title:"Portrait (Vertical Orientation)",children:[l.jsx("span",{children:"📄"}),l.jsx("span",{children:"Portrait"})]}),l.jsxs("button",{type:"button",onClick:()=>{setMsOrientation("landscape");setPrintOrientation("landscape");},className:`flex items-center gap-1 px-3 py-1.5 rounded-lg text-xs font-bold transition-all cursor-pointer ${msOrientation==="landscape"?"bg-white text-blue-700 shadow-xs font-black ring-1 ring-blue-300":"text-slate-600 hover:text-slate-900"}`,title:"Landscape (Horizontal Orientation)",children:[l.jsx("span",{children:"📑"}),l.jsx("span",{children:"Landscape"})]})]}),l.jsxs("button",{type:"button",onClick:()=>ue(P),className:"btn-print-preview",title:"Print single student result card on standard A4",children:[l.jsx(SAFE_od,{className:"w-4 h-4 text-emerald-100"}),l.jsx("span",{children:"Print & Preview"})]}),l.jsxs("details",{className:"relative inline-block text-left no-print",children:[l.jsxs("summary",{className:"btn-3d btn-3d-red flex items-center gap-2 px-4 py-2 text-white rounded-xl text-xs font-black cursor-pointer shadow-md list-none select-none",title:"Export & Download Options",children:[f?l.jsx(Sc,{className:"w-4 h-4 animate-spin"}):l.jsx(SAFE_ad,{className:"w-4 h-4 text-white"}),l.jsx("span",{children:f?m||"Rendering...":"Downloads ▾"})]}),l.jsxs("div",{className:"dropdown-menu-panel",children:[l.jsxs("button",{type:"button",onClick:e=>{e.currentTarget.closest("details")?.removeAttribute("open");Ne(P);},disabled:f,className:"dropdown-menu-item text-rose-700 hover:bg-rose-50",title:"Download single student result card PDF",children:[l.jsx(SAFE_ad,{className:"w-3.5 h-3.5 text-rose-600"}),l.jsx("span",{children:"Download Card (PDF)"})]}),l.jsxs("button",{type:"button",onClick:e=>{e.currentTarget.closest("details")?.removeAttribute("open");Le(P);},className:"dropdown-menu-item text-blue-700 hover:bg-blue-50",title:"Download single student result card Word (.doc)",children:[l.jsx(Xu,{className:"w-3.5 h-3.5 text-blue-600"}),l.jsx("span",{children:"Download Card (.doc)"})]}),l.jsxs("button",{type:"button",onClick:e=>{e.currentTarget.closest("details")?.removeAttribute("open");printAllCardsAction();},className:"dropdown-menu-item text-purple-700 hover:bg-purple-50",title:"Print all students result cards in one go",children:[l.jsx(SAFE_od,{className:"w-3.5 h-3.5 text-purple-600"}),l.jsx("span",{children:"Print ALL Cards"})]})]})]})]})'''

if old_rc_single in text:
    text = text.replace(old_rc_single, new_rc_single, 1)
    print("[✓] Result Card single card toolbar refactored")

# Master Sheet Toolbar: Segmented Pills + Print + Filter Section + Modern "Export Options ▾" Dropdown
old_rc_master = 'a==="masterSheet"&&l.jsxs(l.Fragment,{children:[l.jsxs("button",{type:"button",onClick:Ce,className:"btn-print-preview",title:"Print full class master sheet / broadsheet",children:[l.jsx(SAFE_od,{className:"w-4 h-4 text-emerald-100"}),l.jsx("span",{children:"Print & Preview"})]}),l.jsxs("button",{type:"button",onClick:k,disabled:f,className:"btn-3d btn-3d-red flex items-center gap-2 px-4 py-2.5 text-white rounded-xl text-xs font-black cursor-pointer shadow-md disabled:opacity-50",children:[f?l.jsx(Sc,{className:"w-4 h-4 animate-spin"}):l.jsx(SAFE_ad,{className:"w-4 h-4"}),l.jsx("span",{children:f?m||"Rendering...":"Export Master (PDF)"})]}),l.jsxs("button",{type:"button",onClick:Y,className:"btn-3d btn-3d-navy flex items-center gap-2 px-4 py-2.5 text-white rounded-xl text-xs font-black cursor-pointer shadow-md",children:[l.jsx(Xu,{className:"w-4 h-4 text-blue-200"}),l.jsx("span",{children:"Export Master (.doc)"})]})]})'
new_rc_master = '''a==="masterSheet"&&l.jsxs(l.Fragment,{children:[l.jsxs("div",{className:"flex items-center gap-1 bg-slate-100 p-1 rounded-xl border border-slate-200 mr-1 no-print",children:[l.jsxs("button",{type:"button",onClick:()=>{setMsOrientation("portrait");setPrintOrientation("portrait");},className:`flex items-center gap-1 px-3 py-1.5 rounded-lg text-xs font-bold transition-all cursor-pointer ${msOrientation==="portrait"?"bg-white text-blue-700 shadow-xs font-black ring-1 ring-blue-300":"text-slate-600 hover:text-slate-900"}`,title:"Portrait (Vertical Orientation)",children:[l.jsx("span",{children:"📄"}),l.jsx("span",{children:"Portrait"})]}),l.jsxs("button",{type:"button",onClick:()=>{setMsOrientation("landscape");setPrintOrientation("landscape");},className:`flex items-center gap-1 px-3 py-1.5 rounded-lg text-xs font-bold transition-all cursor-pointer ${msOrientation==="landscape"?"bg-white text-blue-700 shadow-xs font-black ring-1 ring-blue-300":"text-slate-600 hover:text-slate-900"}`,title:"Landscape (Horizontal Orientation)",children:[l.jsx("span",{children:"📑"}),l.jsx("span",{children:"Landscape"})]})]}),l.jsxs("button",{type:"button",onClick:Ce,className:"btn-print-preview",title:"Print full class master sheet / broadsheet",children:[l.jsx(SAFE_od,{className:"w-4 h-4 text-emerald-100"}),l.jsx("span",{children:"Print & Preview"})]}),l.jsxs("div",{className:"flex items-center gap-2 bg-slate-50 px-3 py-1.5 rounded-xl border border-slate-200 shadow-2xs mr-1",children:[l.jsx("span",{className:"text-xs font-black text-slate-600 uppercase tracking-wide hidden sm:inline",children:"Filter Section:"}),l.jsxs("select",{value:m_sec,onChange:S=>setM_sec(S.target.value),className:"px-2.5 py-1 rounded-lg border border-slate-300 font-bold text-xs bg-white focus:outline-none focus:ring-2 focus:ring-blue-500 shadow-xs cursor-pointer",children:[l.jsx("option",{value:"all",children:"All Sections (A, B, C, D)"}),l.jsx("option",{value:"A",children:"Section A"}),l.jsx("option",{value:"B",children:"Section B"}),l.jsx("option",{value:"C",children:"Section C"}),l.jsx("option",{value:"D",children:"Section D"})]})]}),l.jsxs("details",{className:"relative inline-block text-left no-print",children:[l.jsxs("summary",{className:"btn-3d btn-3d-emerald flex items-center gap-2 px-4 py-2 text-white rounded-xl text-xs font-black cursor-pointer shadow-md list-none select-none",title:"Export Options",children:[f?l.jsx(Sc,{className:"w-4 h-4 animate-spin"}):l.jsx(SAFE_ad,{className:"w-4 h-4 text-emerald-100"}),l.jsx("span",{children:f?m||"Rendering...":"Export Options ▾"})]}),l.jsxs("div",{className:"dropdown-menu-panel",children:[l.jsxs("button",{type:"button",onClick:e=>{e.currentTarget.closest("details")?.removeAttribute("open");k();},disabled:f,className:"dropdown-menu-item text-rose-700 hover:bg-rose-50",title:"Export Master Marksheet PDF",children:[l.jsx(SAFE_ad,{className:"w-3.5 h-3.5 text-rose-600"}),l.jsx("span",{children:"Export Master (PDF)"})]}),l.jsxs("button",{type:"button",onClick:e=>{e.currentTarget.closest("details")?.removeAttribute("open");exportMasterGazetteToExcel(R,r,m_sec);},className:"dropdown-menu-item text-emerald-700 hover:bg-emerald-50",title:"Download Consolidated Master Marksheet in Excel (.xls)",children:[l.jsx(SAFE_sd,{className:"w-3.5 h-3.5 text-emerald-600"}),l.jsx("span",{children:"Download Excel (.xls)"})]}),l.jsxs("button",{type:"button",onClick:e=>{e.currentTarget.closest("details")?.removeAttribute("open");Y();},className:"dropdown-menu-item text-blue-700 hover:bg-blue-50",title:"Export Master Document in Word (.doc)",children:[l.jsx(Xu,{className:"w-3.5 h-3.5 text-blue-600"}),l.jsx("span",{children:"Export Master (.doc)"})]})]})]})]})'''

if old_rc_master in text:
    text = text.replace(old_rc_master, new_rc_master, 1)
    print("[✓] Result Card master sheet toolbar refactored")

# In Student Marks Entry Sheet header: add Add Student, Auto-Calculate, and Data & Export Dropdown
old_st_table_btn = 'l.jsxs("button",{type:"button",onClick:D,className:"btn-3d btn-3d-blue flex items-center gap-1.5 px-3.5 py-2 text-white rounded-xl text-xs font-black cursor-pointer shadow-md",children:[l.jsx(SA,{className:"w-4 h-4"}),l.jsx("span",{children:"Add New Student"})]})'
new_st_table_btn = '''l.jsxs("div",{className:"flex items-center gap-2 flex-wrap",children:[l.jsx("input",{ref:fileInputRef,type:"file",accept:".csv,.tsv,.txt",className:"hidden",onChange:handleImportCSV}),l.jsxs("button",{type:"button",onClick:D,className:"btn-3d btn-3d-blue flex items-center gap-1.5 px-3.5 py-1.5 text-white rounded-xl text-xs font-black cursor-pointer shadow-md",children:[l.jsx(SA,{className:"w-4 h-4"}),l.jsx("span",{children:"Add New Student"})]}),l.jsxs("button",{type:"button",onClick:autoCalculateRanks,className:"btn-3d btn-3d-amber flex items-center gap-1.5 px-3.5 py-1.5 text-slate-950 rounded-xl text-xs font-black cursor-pointer shadow-sm hover:brightness-110",title:"Auto calculate student class positions (1st, 2nd, 3rd) based on total marks",children:[l.jsx("span",{children:"⚡"}),l.jsx("span",{children:"Auto-Calculate Positions"})]}),l.jsxs("details",{className:"relative inline-block text-left no-print",children:[l.jsxs("summary",{className:"btn-3d bg-slate-800 hover:bg-slate-700 border border-slate-600 flex items-center gap-1.5 px-3.5 py-1.5 text-white rounded-xl text-xs font-black cursor-pointer shadow-sm list-none select-none",title:"Data Import and Export Controls",children:[l.jsx("span",{children:"📊"}),l.jsx("span",{children:"Data & Export ▾"})]}),l.jsxs("div",{className:"dropdown-menu-panel",children:[l.jsxs("button",{type:"button",onClick:e=>{e.currentTarget.closest("details")?.removeAttribute("open");fileInputRef.current&&fileInputRef.current.click();},className:"dropdown-menu-item text-slate-700 hover:bg-slate-50",title:"Import student marks from Excel or CSV file",children:[l.jsx("span",{children:"📥"}),l.jsx("span",{children:"Import Marks (CSV/Excel)"})]}),l.jsxs("button",{type:"button",onClick:e=>{e.currentTarget.closest("details")?.removeAttribute("open");exportMasterGazetteToExcel(R,r,m_sec);},className:"dropdown-menu-item text-emerald-700 hover:bg-emerald-50",title:"Download complete class marksheet data in Excel (.xls) format",children:[l.jsx("span",{children:"📊"}),l.jsx("span",{children:"Class Excel (.xls)"})]}),l.jsxs("button",{type:"button",onClick:e=>{e.currentTarget.closest("details")?.removeAttribute("open");exportWholeSchoolConsolidatedGazette(savedSheets.length>0?savedSheets:[R],r);},className:"dropdown-menu-item text-purple-700 hover:bg-purple-50",title:"Export Whole School Consolidated Gazette across multiple grades",children:[l.jsx("span",{children:"🏫"}),l.jsx("span",{children:"Whole School Gazette"})]})]})]})]})'''

if old_st_table_btn in text:
    text = text.replace(old_st_table_btn, new_st_table_btn, 1)
    print("[✓] Student marks entry table toolbar refactored")

# Update resultcard and mastersheet containers for responsive layout
old_rc_c = 'className:"bg-white rounded-2xl shadow-xl border border-slate-300 p-6 sm:p-10 max-w-4xl mx-auto print:border-none print:shadow-none print:p-0 print:m-0 print:max-w-none print:w-full",id:"resultcard-print-container"'
new_rc_c = 'className:`bg-white rounded-2xl shadow-xl border border-slate-300 p-6 sm:p-8 ${msOrientation==="landscape"?"max-w-6xl landscape-mode":"max-w-4xl portrait-mode"} mx-auto print:border-none print:shadow-none print:p-0 print:m-0 print:max-w-none print:w-full`,id:"resultcard-print-container"'
if old_rc_c in text:
    text = text.replace(old_rc_c, new_rc_c, 1)

old_ms_c = 'className:"bg-white rounded-2xl shadow-xl border border-slate-300 p-6 sm:p-8 max-w-5xl mx-auto print:border-none print:shadow-none print:p-0 print:m-0 print:max-w-none print:w-full overflow-x-auto",id:"mastersheet-print-container"'
new_ms_c = 'className:`bg-white rounded-2xl shadow-xl border border-slate-300 p-6 sm:p-8 ${msOrientation==="landscape"?"max-w-7xl landscape-mode":"max-w-5xl portrait-mode"} mx-auto print:border-none print:shadow-none print:p-0 print:m-0 print:max-w-none print:w-full overflow-x-auto`,id:"mastersheet-print-container"'
if old_ms_c in text:
    text = text.replace(old_ms_c, new_ms_c, 1)

# In Single Card student selector: add search input
old_st_select = 'children:[l.jsx("span",{className:"text-xs font-black text-slate-700 uppercase tracking-wide",children:"Select Candidate / Student:"}),l.jsxs("select",{value:P.id,onChange:S=>u(S.target.value),'
new_st_select = '''children:[l.jsx("span",{className:"text-xs font-black text-slate-700 uppercase tracking-wide",children:"Search / Select Student:"}),l.jsx("input",{type:"text",value:studentSearch,onChange:S=>setStudentSearch(S.target.value),placeholder:"🔍 Search student name/roll...",className:"px-3 py-1.5 rounded-xl border border-slate-300 font-bold text-xs bg-white text-slate-900 w-48 focus:ring-2 focus:ring-blue-500"}),l.jsxs("select",{value:P.id,onChange:S=>u(S.target.value),'''
if old_st_select in text:
    text = text.replace(old_st_select, new_st_select, 1)

# -------------------------------------------------------------------------
# 5. Global 100% English Language Standardization (Strict Zero Urdu in Controls)
# -------------------------------------------------------------------------
# Orientation buttons & titles
text = text.replace('title:"Portrait (Vertical Orientation) - عمودی انداز"', 'title:"Portrait (Vertical Orientation)"')
text = text.replace('title:"Landscape (Horizontal Orientation) - افقی انداز"', 'title:"Landscape (Horizontal Orientation)"')
text = text.replace('children: "Portrait (عمودی)"', 'children: "Portrait"')
text = text.replace('children: "Landscape (افقی)"', 'children: "Landscape"')
text = text.replace('children:"Portrait (عمودی)"', 'children:"Portrait"')
text = text.replace('children:"Landscape (افقی)"', 'children:"Landscape"')

# Auto-calculate positions & toast
text = text.replace('children:"Auto-Calculate Positions (پوزیشنز)"', 'children:"Auto-Calculate Positions"')
text = text.replace('children:"Auto-Rank (پوزیشنز)"', 'children:"Auto-Calculate Positions"')
text = text.replace('تمام طلباء کی پوزیشنز خودکار طور پر کیلکولیٹ ہو گئیں!', 'All student class positions and ranks calculated successfully!')

# Question Bank Add Modal
text = text.replace('children: "Urdu Nastaliq Statement (اردو سوال):"', 'children: "Urdu Nastaliq Statement (Optional):"')
text = text.replace('placeholder: "مثلاً: یکساں اسراع کی تعریف کریں اور اس کا ایس آئی یونٹ لکھیں۔"', 'placeholder: "e.g. Enter optional Urdu translation or leave blank"')

# Toasts and labels in Urdu
text = text.replace('کلاس کا نام لکھیں', 'Enter Class Name')
text = text.replace('تعلیمی سیشن لکھیں', 'Enter Academic Session')
text = text.replace('تبدیل یا ٹائپ کریں', 'Editable')
text = text.replace('کا ڈیٹا محفوظ ہو گیا!', 'data saved successfully!')
text = text.replace('لوڈ ہو گئی', 'loaded successfully')

print("[✓] Zero Urdu standardization applied")

# Save refactored bundle
js_path = "assets/index-DAioIUjd.js"
with open(js_path, "w", encoding="utf-8") as f:
    f.write(text)

print(f"Saved {js_path} (length: {len(text)})")

# Test syntax with node --check
res = subprocess.run(["node", "--check", js_path], capture_output=True, text=True)
if res.returncode == 0:
    print("[✓✓✓] node --check passed cleanly for assets/index-DAioIUjd.js!")
else:
    print("[X] node --check failed:")
    print(res.stderr[:800])
    exit(1)

print("=== All Refactorings Completed and Validated ===")
