#!/usr/bin/env python3
import sys

print("Reading bundle assets/index-DAioIUjd.js...")
with open('assets/index-DAioIUjd.js', 'r', encoding='utf-8') as f:
    code = f.read()

orig_len = len(code)

# 1. EXCEL EXPORTS: Remove invisible white text and ensure 100% black text on light fills
# Replace DateSheet Excel Header and Table styles
old_ds_excel = """  const html = `<!DOCTYPE html><html xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:x="urn:schemas-microsoft-com:office:excel" xmlns="http://www.w3.org/TR/REC-html40">  <head><meta http-equiv="Content-Type" content="application/vnd.ms-excel; charset=utf-8">  <title>${brandTitle} - Date Sheet</title>  <style>    body { font-family: 'Segoe UI', Calibri, Arial, sans-serif; font-size: 10pt; }    table { border-collapse: collapse; width: 100%; }    .header { background-color: #0f172a; color: #ffffff; font-size: 14pt; font-weight: bold; text-align: center; padding: 10pt; }    .sub { background-color: #1e3a8a; color: #f8fafc; font-size: 10pt; text-align: center; padding: 6pt; font-weight: 600; }    th { background-color: #1e293b; color: #ffffff; padding: 8pt; border: 1pt solid #475569; font-size: 9.5pt; text-align: center; }  </style>  </head>  <body>    <table>      <tr><td colspan="6" class="header">${brandTitle}</td></tr>      <tr><td colspan="6" class="sub">${brandCampus} &bull; OFFICIAL DATE SHEET &bull; ${examTitle.toUpperCase()}</td></tr>      <tr>        <td colspan="3" style="padding: 6pt; font-weight: bold; border-bottom: 2pt solid #1e3a8a;">Class / Grade: ${ds.classLevel}</td>        <td colspan="3" align="right" style="padding: 6pt; font-weight: bold; border-bottom: 2pt solid #1e3a8a;">Session: ${ds.session || "2025-2026"} &bull; Shift: ${ds.shift || "Morning"}</td>      </tr>      <tr><td colspan="6" style="height: 6pt;"></td></tr>      <thead>        <tr>          <th>Sr#</th>          <th>Examination Date (تاریخ)</th>          <th>Day (دن)</th>          <th>Subject Name (مضمون)</th>          <th>Syllabus / Paper Scope</th>          <th>Exam Timings (وقت)</th>        </tr>      </thead>"""

new_ds_excel = """  const html = `<!DOCTYPE html><html xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:x="urn:schemas-microsoft-com:office:excel" xmlns="http://www.w3.org/TR/REC-html40">  <head><meta http-equiv="Content-Type" content="application/vnd.ms-excel; charset=utf-8">  <title>${brandTitle} - Date Sheet</title>  <style>    body { font-family: 'Segoe UI', Calibri, Arial, sans-serif; font-size: 10pt; color: #000000; }    table { border-collapse: collapse; width: 100%; }    td, th { mso-line-height-rule: exactly; }  </style>  </head>  <body>    <table border="1" cellpadding="5" cellspacing="0" style="border-collapse:collapse; width:100%;">      <tr><td colspan="6" style="background-color: #f1f5f9; color: #000000; font-size: 14pt; font-weight: 900; text-align: center; padding: 10pt; border: 1.5pt solid #475569;">${brandTitle}</td></tr>      <tr><td colspan="6" style="background-color: #e2e8f0; color: #000000; font-size: 10.5pt; text-align: center; padding: 6pt; font-weight: bold; border: 1pt solid #64748b;">${brandCampus} &bull; OFFICIAL DATE SHEET &bull; ${examTitle.toUpperCase()}</td></tr>      <tr>        <td colspan="3" style="padding: 6pt; font-weight: bold; color: #000000; border: 1pt solid #cbd5e1; background-color: #ffffff;">Class / Grade: <strong>${ds.classLevel}</strong></td>        <td colspan="3" align="right" style="padding: 6pt; font-weight: bold; color: #000000; border: 1pt solid #cbd5e1; background-color: #ffffff;">Session: ${ds.session || "2025-2026"} &bull; Shift: ${ds.shift || "Morning"}</td>      </tr>      <thead>        <tr style="background-color: #cbd5e1;">          <th style="background-color: #cbd5e1; color: #000000; font-weight: 900; padding: 8pt; border: 1pt solid #475569; text-align: center;">Sr#</th>          <th style="background-color: #cbd5e1; color: #000000; font-weight: 900; padding: 8pt; border: 1pt solid #475569; text-align: left;">Examination Date (تاریخ)</th>          <th style="background-color: #cbd5e1; color: #000000; font-weight: 900; padding: 8pt; border: 1pt solid #475569; text-align: left;">Day (دن)</th>          <th style="background-color: #cbd5e1; color: #000000; font-weight: 900; padding: 8pt; border: 1pt solid #475569; text-align: left;">Subject Name (مضمون)</th>          <th style="background-color: #cbd5e1; color: #000000; font-weight: 900; padding: 8pt; border: 1pt solid #475569; text-align: left;">Syllabus / Paper Scope</th>          <th style="background-color: #cbd5e1; color: #000000; font-weight: 900; padding: 8pt; border: 1pt solid #475569; text-align: center;">Exam Timings (وقت)</th>        </tr>      </thead>"""

if old_ds_excel in code:
    code = code.replace(old_ds_excel, new_ds_excel, 1)
    print("✓ Updated DateSheet Excel export formatting.")
else:
    print("✗ DateSheet Excel pattern not found.")

# Replace ResultCard Excel Header and Table styles
old_rc_excel = """  const html = `<!DOCTYPE html><html xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:x="urn:schemas-microsoft-com:office:excel" xmlns="http://www.w3.org/TR/REC-html40">  <head><meta http-equiv="Content-Type" content="application/vnd.ms-excel; charset=utf-8">  <title>${brandTitle} - Result Card Roll ${st.rollNo}</title>  <style>    body { font-family: 'Segoe UI', Calibri, Arial, sans-serif; font-size: 10pt; }    table { border-collapse: collapse; width: 100%; }    .header { background-color: #0f172a; color: #ffffff; font-size: 14pt; font-weight: bold; text-align: center; padding: 10pt; }    .sub { background-color: #1e3a8a; color: #f8fafc; font-size: 10pt; text-align: center; padding: 6pt; font-weight: 600; }    th { background-color: #1e293b; color: #ffffff; padding: 8pt; border: 1pt solid #475569; font-size: 9.5pt; text-align: center; }  </style>  </head>  <body>    <table>      <tr><td colspan="8" class="header">${brandTitle}</td></tr>      <tr><td colspan="8" class="sub">${brandCampus} &bull; OFFICIAL STUDENT EXAMINATION RESULT CARD</td></tr>"""

new_rc_excel = """  const html = `<!DOCTYPE html><html xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:x="urn:schemas-microsoft-com:office:excel" xmlns="http://www.w3.org/TR/REC-html40">  <head><meta http-equiv="Content-Type" content="application/vnd.ms-excel; charset=utf-8">  <title>${brandTitle} - Result Card Roll ${st.rollNo}</title>  <style>    body { font-family: 'Segoe UI', Calibri, Arial, sans-serif; font-size: 10pt; color: #000000; }    table { border-collapse: collapse; width: 100%; }    td, th { mso-line-height-rule: exactly; }  </style>  </head>  <body>    <table border="1" cellpadding="5" cellspacing="0" style="border-collapse:collapse; width:100%;">      <tr><td colspan="8" style="background-color: #f1f5f9; color: #000000; font-size: 14pt; font-weight: 900; text-align: center; padding: 10pt; border: 1.5pt solid #475569;">${brandTitle}</td></tr>      <tr><td colspan="8" style="background-color: #e2e8f0; color: #000000; font-size: 10.5pt; text-align: center; padding: 6pt; font-weight: bold; border: 1pt solid #64748b;">${brandCampus} &bull; OFFICIAL STUDENT EXAMINATION RESULT CARD</td></tr>"""

if old_rc_excel in code:
    code = code.replace(old_rc_excel, new_rc_excel, 1)
    print("✓ Updated ResultCard Excel export header formatting.")
else:
    print("✗ ResultCard Excel pattern not found.")

# Update ResultCard Excel <thead>
old_rc_thead = """      <thead>        <tr>          <th>Sr#</th>          <th>Subject Name</th>          <th>Total Marks</th>          <th>Pass Marks</th>          <th>Marks Obtained</th>          <th>Percentage %</th>          <th>Grade</th>          <th>Status</th>        </tr>      </thead>"""

new_rc_thead = """      <thead>        <tr style="background-color: #cbd5e1;">          <th style="background-color: #cbd5e1; color: #000000; font-weight: 900; padding: 8pt; border: 1pt solid #475569; text-align: center;">Sr#</th>          <th style="background-color: #cbd5e1; color: #000000; font-weight: 900; padding: 8pt; border: 1pt solid #475569; text-align: left;">Subject Name</th>          <th style="background-color: #cbd5e1; color: #000000; font-weight: 900; padding: 8pt; border: 1pt solid #475569; text-align: center;">Total Marks</th>          <th style="background-color: #cbd5e1; color: #000000; font-weight: 900; padding: 8pt; border: 1pt solid #475569; text-align: center;">Pass Marks</th>          <th style="background-color: #cbd5e1; color: #000000; font-weight: 900; padding: 8pt; border: 1pt solid #475569; text-align: center;">Marks Obtained</th>          <th style="background-color: #cbd5e1; color: #000000; font-weight: 900; padding: 8pt; border: 1pt solid #475569; text-align: center;">Percentage %</th>          <th style="background-color: #cbd5e1; color: #000000; font-weight: 900; padding: 8pt; border: 1pt solid #475569; text-align: center;">Grade</th>          <th style="background-color: #cbd5e1; color: #000000; font-weight: 900; padding: 8pt; border: 1pt solid #475569; text-align: center;">Status</th>        </tr>      </thead>"""

if old_rc_thead in code:
    code = code.replace(old_rc_thead, new_rc_thead, 1)
    print("✓ Updated ResultCard Excel thead.")

# Update ResultCard Excel Grand Total Row to crisp black
old_rc_total = """        <tr style="background-color: #e2e8f0; font-weight: bold;">          <td colspan="2" align="right" style="padding: 8pt; border: 1.5pt solid #475569; font-size: 11pt;">GRAND TOTAL / OVERALL:</td>          <td align="center" style="padding: 8pt; border: 1.5pt solid #475569; font-size: 11pt;">${totalMax}</td>          <td align="center" style="padding: 8pt; border: 1.5pt solid #475569;">-</td>          <td align="center" style="padding: 8pt; border: 1.5pt solid #475569; font-size: 12pt; color: #1e3a8a;">${totalObtained}</td>          <td align="center" style="padding: 8pt; border: 1.5pt solid #475569; font-size: 11pt;">${overallPct}%</td>          <td align="center" style="padding: 8pt; border: 1.5pt solid #475569; font-size: 12pt; color: #d97706;">${overallGrade}</td>          <td align="center" style="padding: 8pt; border: 1.5pt solid #475569; font-size: 11pt; color: ${hasFailed ? "#b91c1c" : "#047857"};">${finalStatus}</td>        </tr>"""

new_rc_total = """        <tr style="background-color: #e2e8f0; font-weight: bold; color: #000000;">          <td colspan="2" align="right" style="padding: 8pt; border: 1.5pt solid #475569; font-size: 11pt; color: #000000;">GRAND TOTAL / OVERALL:</td>          <td align="center" style="padding: 8pt; border: 1.5pt solid #475569; font-size: 11pt; color: #000000;">${totalMax}</td>          <td align="center" style="padding: 8pt; border: 1.5pt solid #475569; color: #000000;">-</td>          <td align="center" style="padding: 8pt; border: 1.5pt solid #475569; font-size: 12pt; color: #000000; font-weight: 900;">${totalObtained}</td>          <td align="center" style="padding: 8pt; border: 1.5pt solid #475569; font-size: 11pt; color: #000000;">${overallPct}%</td>          <td align="center" style="padding: 8pt; border: 1.5pt solid #475569; font-size: 12pt; color: #000000; font-weight: 900;">${overallGrade}</td>          <td align="center" style="padding: 8pt; border: 1.5pt solid #475569; font-size: 11pt; color: ${hasFailed ? "#b91c1c" : "#047857"}; font-weight: 900;">${finalStatus}</td>        </tr>"""

if old_rc_total in code:
    code = code.replace(old_rc_total, new_rc_total, 1)
    print("✓ Updated ResultCard Excel total row.")

# Replace Master Gazette Excel Header
old_mg_excel = """  const html = `<!DOCTYPE html><html xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:x="urn:schemas-microsoft-com:office:excel" xmlns="http://www.w3.org/TR/REC-html40">  <head><meta http-equiv="Content-Type" content="application/vnd.ms-excel; charset=utf-8">  <title>${brandTitle} - Marksheet Gazette</title>  <style>    body { font-family: 'Segoe UI', Calibri, Arial, sans-serif; font-size: 9.5pt; }    table { border-collapse: collapse; width: 100%; }    .header { background-color: #0f172a; color: #ffffff; font-size: 14pt; font-weight: bold; text-align: center; padding: 10pt; }    .sub { background-color: #1e3a8a; color: #f8fafc; font-size: 10pt; text-align: center; padding: 6pt; font-weight: 600; }    th { background-color: #1e293b; color: #ffffff; padding: 6pt; border: 1pt solid #475569; font-size: 9pt; text-align: center; }  </style>  </head>  <body>    <table>      <tr><td colspan="${totalCols}" class="header">${brandTitle}</td></tr>      <tr><td colspan="${totalCols}" class="sub">${brandCampus} &bull; CONSOLIDATED RESULT GAZETTE / MASTER SHEET</td></tr>"""

new_mg_excel = """  const html = `<!DOCTYPE html><html xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:x="urn:schemas-microsoft-com:office:excel" xmlns="http://www.w3.org/TR/REC-html40">  <head><meta http-equiv="Content-Type" content="application/vnd.ms-excel; charset=utf-8">  <title>${brandTitle} - Marksheet Gazette</title>  <style>    body { font-family: 'Segoe UI', Calibri, Arial, sans-serif; font-size: 9.5pt; color: #000000; }    table { border-collapse: collapse; width: 100%; }    td, th { mso-line-height-rule: exactly; }  </style>  </head>  <body>    <table border="1" cellpadding="5" cellspacing="0" style="border-collapse:collapse; width:100%;">      <tr><td colspan="${totalCols}" style="background-color: #f1f5f9; color: #000000; font-size: 14pt; font-weight: 900; text-align: center; padding: 10pt; border: 1.5pt solid #475569;">${brandTitle}</td></tr>      <tr><td colspan="${totalCols}" style="background-color: #e2e8f0; color: #000000; font-size: 10.5pt; text-align: center; padding: 6pt; font-weight: bold; border: 1pt solid #64748b;">${brandCampus} &bull; CONSOLIDATED RESULT GAZETTE / MASTER SHEET</td></tr>"""

if old_mg_excel in code:
    code = code.replace(old_mg_excel, new_mg_excel, 1)
    print("✓ Updated Master Gazette Excel header.")

# Update Master Gazette subject headers to crisp dark
old_mg_subheaders = """  const subjectHeaders = (marksheet.subjects || []).map(sub => `    <th style="padding: 6pt; border: 1pt solid #475569; font-size: 9pt;">${sub.name}<br/><span style="color: #94a3b8; font-size: 8pt;">(${sub.totalMarks})</span></th>  `).join("");"""

new_mg_subheaders = """  const subjectHeaders = (marksheet.subjects || []).map(sub => `    <th style="background-color: #cbd5e1; color: #000000; font-weight: 900; padding: 6pt; border: 1pt solid #475569; font-size: 9pt;">${sub.name}<br/><span style="color: #334155; font-size: 8pt; font-weight: bold;">(${sub.totalMarks})</span></th>  `).join("");"""

if old_mg_subheaders in code:
    code = code.replace(old_mg_subheaders, new_mg_subheaders, 1)
    print("✓ Updated Master Gazette subject headers.")

# 2. BUBBLE SHEET COMPONENT (QS): Zero overlap for date, roll number, and bubbles
old_qs_header_info = """l.jsxs("div",{className:"flex justify-between items-center text-xs mt-2 font-medium border-t border-slate-300 pt-2 px-2 bg-slate-50/60 p-1.5",children:[l.jsxs("span",{children:["Class: ",l.jsx("strong",{children:n.header.classLevel})]}),l.jsxs("span",{children:["Subject: ",l.jsx("strong",{children:n.header.subjectName})]}),l.jsxs("span",{children:["Date: ",l.jsx("strong",{children:n.header.dateStr})]}),l.jsxs("span",{children:["Max MCQs: ",l.jsx("strong",{children:u})]})]})"""

new_qs_header_info = """l.jsxs("div",{className:"grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs mt-2.5 font-bold border-t-2 border-slate-900 pt-2.5 px-2 bg-slate-50 text-slate-900 text-center",children:[l.jsxs("div",{className:"p-1.5 border border-slate-300 rounded bg-white shadow-2xs",children:[l.jsx("span",{className:"text-slate-500 font-semibold block text-[10px] uppercase",children:"Class:"}),l.jsx("span",{className:"text-slate-950 font-black",children:n.header.classLevel})]}),l.jsxs("div",{className:"p-1.5 border border-slate-300 rounded bg-white shadow-2xs",children:[l.jsx("span",{className:"text-slate-500 font-semibold block text-[10px] uppercase",children:"Subject:"}),l.jsx("span",{className:"text-slate-950 font-black",children:n.header.subjectName})]}),l.jsxs("div",{className:"p-1.5 border border-slate-300 rounded bg-white shadow-2xs",children:[l.jsx("span",{className:"text-slate-500 font-semibold block text-[10px] uppercase",children:"Date:"}),l.jsx("span",{className:"text-blue-950 font-black",children:n.header.dateStr})]}),l.jsxs("div",{className:"p-1.5 border border-slate-300 rounded bg-white shadow-2xs",children:[l.jsx("span",{className:"text-slate-500 font-semibold block text-[10px] uppercase",children:"Max MCQs:"}),l.jsx("span",{className:"text-slate-950 font-black",children:u})]})]})"""

if old_qs_header_info in code:
    code = code.replace(old_qs_header_info, new_qs_header_info, 1)
    print("✓ Fixed Bubble Sheet Date & Header Info collision.")
else:
    print("✗ old_qs_header_info not found.")

# Fix Bubble Sheet Roll Number Table layout
old_qs_rollno = """l.jsxs("div",{className:"border border-slate-400 p-2 bg-slate-50 rounded",children:[l.jsx("div",{className:"text-[11px] font-bold text-center mb-1 uppercase tracking-wide",children:"Roll Number"}),l.jsx("div",{className:"flex justify-center gap-1.5 mb-1.5",children:Array.from({length:B}).map((y,v)=>l.jsx("div",{className:"w-6 h-6 border-2 border-slate-700 bg-white"},v))}),l.jsx("div",{className:"space-y-0.5",children:f.map(y=>l.jsx("div",{className:"flex justify-center gap-1.5",children:Array.from({length:B}).map((v,E)=>l.jsx("div",{className:"w-5 h-5 rounded-full border border-slate-600 flex items-center justify-center text-[10px] font-mono text-slate-700 bg-white",children:y},E))},y))})]})"""

new_qs_rollno = """l.jsxs("div",{className:"border-2 border-slate-900 p-2.5 bg-slate-50 rounded-lg shadow-2xs text-center",children:[l.jsx("div",{className:"text-[11px] font-black text-center mb-1.5 uppercase tracking-wide text-slate-900",children:"Candidate Roll Number"}),l.jsxs("table",{className:"roll-number-table mx-auto border-collapse",style:{borderSpacing:"3px",borderCollapse:"separate"},children:[l.jsx("thead",{children:l.jsx("tr",{children:Array.from({length:B}).map((y,v)=>l.jsx("td",{className:"w-6 h-6 min-w-[24px] border-2 border-slate-900 bg-white text-center font-black text-xs p-0 shadow-2xs"},v))})}),l.jsx("tbody",{children:f.map(y=>l.jsx("tr",{children:Array.from({length:B}).map((v,E)=>l.jsx("td",{className:"p-0.5 text-center align-middle",children:l.jsx("div",{className:"omr-bubble w-5 h-5 min-w-[20px] min-h-[20px] rounded-full border border-slate-800 flex items-center justify-center text-[10px] font-mono font-bold text-slate-800 bg-white mx-auto shadow-2xs",children:y})},E))},y))})]})]})"""

if old_qs_rollno in code:
    code = code.replace(old_qs_rollno, new_qs_rollno, 1)
    print("✓ Fixed Bubble Sheet Roll Number box overlap.")
else:
    print("✗ old_qs_rollno not found.")

# Fix Question Response Bubbles in QS
old_qs_bubbles = """l.jsx("div",{className:"bubble-grid-print grid grid-cols-2 sm:grid-cols-3 gap-x-6 gap-y-2",children:Array.from({length:Math.max(u,15)}).map((y,v)=>{const E=v+1;return l.jsxs("div",{className:"flex items-center justify-between border-b border-slate-200 py-1 px-1 text-xs",children:[l.jsxs("span",{className:"font-bold w-6 text-slate-800",children:["Q.",E]}),l.jsx("div",{className:"flex items-center gap-2",children:["A","B","C","D"].map(I=>l.jsx("div",{className:"w-6 h-6 rounded-full border border-slate-800 flex items-center justify-center text-[11px] font-bold hover:bg-slate-200 cursor-pointer",children:I},I))})]},E)})})"""

new_qs_bubbles = """l.jsx("div",{className:"bubble-grid-print grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-x-4 gap-y-2 print:grid-cols-2",children:Array.from({length:Math.max(u,15)}).map((y,v)=>{const E=v+1;return l.jsxs("div",{className:"flex items-center justify-between border border-slate-300 rounded px-2.5 py-1 bg-white text-xs shadow-2xs",children:[l.jsxs("span",{className:"font-black text-slate-900 w-8 shrink-0",children:["Q.",E]}),l.jsx("div",{className:"flex items-center gap-1.5 shrink-0",children:["A","B","C","D"].map(I=>l.jsx("div",{className:"omr-bubble w-5 h-5 min-w-[20px] min-h-[20px] rounded-full border border-slate-900 flex items-center justify-center text-[10px] font-black text-slate-900 bg-white hover:bg-slate-200 cursor-pointer shrink-0 shadow-2xs",children:I},I))})]},E)})})"""

if old_qs_bubbles in code:
    code = code.replace(old_qs_bubbles, new_qs_bubbles, 1)
    print("✓ Fixed Bubble Sheet MCQ response bubble overlap.")
else:
    print("✗ old_qs_bubbles not found.")

# 3. ANSWER KEY (jS): Replace all white text on white paper with high-contrast printer safe styling
old_js_sec_a = """l.jsxs("div",{className:"bg-slate-900 text-white px-3 py-1.5 rounded-xs flex items-center justify-between text-xs font-black uppercase tracking-wider",children:[l.jsx("span",{children:"SECTION - A: SOLVED MULTIPLE CHOICE QUESTIONS (MCQs)"}),l.jsxs("span",{children:[n.objectiveSection.totalMarks," Marks"]})]})"""

new_js_sec_a = """l.jsxs("div",{className:"bg-slate-100 text-slate-950 border-2 border-slate-900 px-3 py-1.5 rounded flex items-center justify-between text-xs font-black uppercase tracking-wider print:bg-slate-100 print:text-black",children:[l.jsx("span",{children:"SECTION - A: SOLVED MULTIPLE CHOICE QUESTIONS (MCQs)"}),l.jsxs("span",{children:[n.objectiveSection.totalMarks," Marks"]})]})"""

if old_js_sec_a in code:
    code = code.replace(old_js_sec_a, new_js_sec_a, 1)
    print("✓ Fixed Answer Key Section A header contrast.")
else:
    print("✗ old_js_sec_a not found.")

# Fix solved badge in jS
old_js_badge = """l.jsx("div",{className:"answer-key-solved-badge w-8 h-8 rounded-lg bg-emerald-600 text-white font-black text-sm flex items-center justify-center shrink-0 shadow-xs",children:O.correctOption})"""

new_js_badge = """l.jsx("div",{className:"answer-key-solved-badge w-8 h-8 rounded-lg border-2 border-emerald-800 bg-emerald-50 text-emerald-950 font-black text-sm flex items-center justify-center shrink-0 shadow-xs print:bg-emerald-50 print:text-black print:border-black",children:O.correctOption})"""

if old_js_badge in code:
    code = code.replace(old_js_badge, new_js_badge, 1)
    print("✓ Fixed Answer Key badge contrast.")
else:
    print("✗ old_js_badge not found.")

# Fix Section B and C header in jS
old_js_sec_bc = """l.jsxs("div",{className:"bg-slate-900 text-white px-3 py-1.5 rounded-xs flex items-center justify-between text-xs font-black uppercase tracking-wider",children:[l.jsx("span",{children:"SECTION - B & C: SUBJECTIVE QUESTION MARKING SCHEME & MODEL ANSWERS"}),l.jsxs("span",{children:[n.subjectiveSection.totalMarks," Marks"]})]})"""

new_js_sec_bc = """l.jsxs("div",{className:"bg-slate-100 text-slate-950 border-2 border-slate-900 px-3 py-1.5 rounded flex items-center justify-between text-xs font-black uppercase tracking-wider print:bg-slate-100 print:text-black",children:[l.jsx("span",{children:"SECTION - B & C: SUBJECTIVE QUESTION MARKING SCHEME & MODEL ANSWERS"}),l.jsxs("span",{children:[n.subjectiveSection.totalMarks," Marks"]})]})"""

if old_js_sec_bc in code:
    code = code.replace(old_js_sec_bc, new_js_sec_bc, 1)
    print("✓ Fixed Answer Key Section B&C header contrast.")
else:
    print("✗ old_js_sec_bc not found.")

# 4. RESULT CARD & MARKSHEET (lq): Fix high-contrast banners and headers
old_rc_banner = """l.jsxs("div",{className:"mt-3.5 bg-blue-900 text-white font-black py-1.5 px-4 rounded text-xs sm:text-sm uppercase tracking-wider shadow-xs",children:["Progress Report Card / Annual Result Sheet • Session ",R.session]})"""

new_rc_banner = """l.jsxs("div",{className:"mt-3.5 bg-slate-100 text-slate-950 border-2 border-slate-900 font-black py-1.5 px-4 rounded text-xs sm:text-sm uppercase tracking-wider shadow-xs print:bg-slate-100 print:text-black",children:["Progress Report Card / Annual Result Sheet • Session ",R.session]})"""

if old_rc_banner in code:
    code = code.replace(old_rc_banner, new_rc_banner, 1)
    print("✓ Fixed Result Card banner contrast.")
else:
    print("✗ old_rc_banner not found.")

old_rc_tbl_head = """l.jsxs("tr",{className:"bg-slate-900 text-white font-extrabold uppercase text-[11px]",children:[l.jsx("th",{className:"p-2 border border-slate-900 text-center w-10",children:"Sr#"}),l.jsx("th",{className:"p-2 border border-slate-900 text-left",children:"Subject Name"}),l.jsx("th",{className:"p-2 border border-slate-900 text-center w-24",children:"Total Marks"}),l.jsx("th",{className:"p-2 border border-slate-900 text-center w-24",children:"Pass Marks"}),l.jsx("th",{className:"p-2 border border-slate-900 text-center w-28",children:"Marks Obtained"}),l.jsx("th",{className:"p-2 border border-slate-900 text-center w-20",children:"Grade"}),l.jsx("th",{className:"p-2 border border-slate-900 text-center w-24",children:"Remarks"})]})"""

new_rc_tbl_head = """l.jsxs("tr",{className:"bg-slate-200 text-slate-950 font-black uppercase text-[11px] border-b-2 border-slate-900 print:bg-slate-200 print:text-black",children:[l.jsx("th",{className:"p-2 border border-slate-900 text-center w-10 text-slate-950 font-black",children:"Sr#"}),l.jsx("th",{className:"p-2 border border-slate-900 text-left text-slate-950 font-black",children:"Subject Name"}),l.jsx("th",{className:"p-2 border border-slate-900 text-center w-24 text-slate-950 font-black",children:"Total Marks"}),l.jsx("th",{className:"p-2 border border-slate-900 text-center w-24 text-slate-950 font-black",children:"Pass Marks"}),l.jsx("th",{className:"p-2 border border-slate-900 text-center w-28 text-slate-950 font-black",children:"Marks Obtained"}),l.jsx("th",{className:"p-2 border border-slate-900 text-center w-20 text-slate-950 font-black",children:"Grade"}),l.jsx("th",{className:"p-2 border border-slate-900 text-center w-24 text-slate-950 font-black",children:"Remarks"})]})"""

if old_rc_tbl_head in code:
    code = code.replace(old_rc_tbl_head, new_rc_tbl_head, 1)
    print("✓ Fixed Result Card table header contrast.")
else:
    print("✗ old_rc_tbl_head not found.")

# Marksheet Gazette banner and header
old_mg_banner = """l.jsxs("div",{className:"mt-2.5 bg-blue-900 text-white font-black py-1 px-4 rounded text-xs uppercase tracking-wider",children:["Consolidated Result Gazette / Master Sheet • Session ",R.session]})"""

new_mg_banner = """l.jsxs("div",{className:"mt-2.5 bg-slate-100 text-slate-950 border-2 border-slate-900 font-black py-1 px-4 rounded text-xs uppercase tracking-wider print:bg-slate-100 print:text-black",children:["Consolidated Result Gazette / Master Sheet • Session ",R.session]})"""

if old_mg_banner in code:
    code = code.replace(old_mg_banner, new_mg_banner, 1)
    print("✓ Fixed Marksheet Gazette banner contrast.")
else:
    print("✗ old_mg_banner not found.")

# Marksheet Gazette table header
old_mg_head = """l.jsx("thead",{children:l.jsxs("tr",{className:"bg-slate-900 text-white font-extrabold uppercase text-[10px]",children:[l.jsx("th",{className:"p-1.5 border border-slate-900 text-center w-12",children:"Roll#"}),l.jsx("th",{className:"p-1.5 border border-slate-900 text-left w-36",children:"Student Name"}),l.jsx("th",{className:"p-1.5 border border-slate-900 text-left w-32",children:"Father's Name"}),R.subjects.map(S=>l.jsxs("th",{className:"p-1.5 border border-slate-900 text-center",children:[l.jsx("div",{children:S.name}),l.jsxs("div",{className:"text-[8px] text-blue-300",children:["(",S.totalMarks,")"]})]},S.id)),l.jsxs("th",{className:"p-1.5 border border-slate-900 text-center w-16",children:["Total",l.jsxs("div",{className:"text-[8px] text-blue-300",children:["(",ne,")"]})]}),l.jsx("th",{className:"p-1.5 border border-slate-900 text-center w-12",children:"%"}),l.jsx("th",{className:"p-1.5 border border-slate-900 text-center w-10",children:"Grd"}),l.jsx("th",{className:"p-1.5 border border-slate-900 text-center w-14",children:"Result"}),l.jsx("th",{className:"p-1.5 border border-slate-900 text-center w-12",children:"Rank"})]})})"""

new_mg_head = """l.jsx("thead",{children:l.jsxs("tr",{className:"bg-slate-200 text-slate-950 font-black uppercase text-[10px] border-b-2 border-slate-900 print:bg-slate-200 print:text-black",children:[l.jsx("th",{className:"p-1.5 border border-slate-900 text-center w-12 text-slate-950 font-black",children:"Roll#"}),l.jsx("th",{className:"p-1.5 border border-slate-900 text-left w-36 text-slate-950 font-black",children:"Student Name"}),l.jsx("th",{className:"p-1.5 border border-slate-900 text-left w-32 text-slate-950 font-black",children:"Father's Name"}),R.subjects.map(S=>l.jsxs("th",{className:"p-1.5 border border-slate-900 text-center text-slate-950 font-black",children:[l.jsx("div",{children:S.name}),l.jsxs("div",{className:"text-[8px] text-slate-600 font-bold",children:["(",S.totalMarks,")"]})]},S.id)),l.jsxs("th",{className:"p-1.5 border border-slate-900 text-center w-16 text-slate-950 font-black",children:["Total",l.jsxs("div",{className:"text-[8px] text-slate-600 font-bold",children:["(",ne,")"]})]}),l.jsx("th",{className:"p-1.5 border border-slate-900 text-center w-12 text-slate-950 font-black",children:"%"}),l.jsx("th",{className:"p-1.5 border border-slate-900 text-center w-10 text-slate-950 font-black",children:"Grd"}),l.jsx("th",{className:"p-1.5 border border-slate-900 text-center w-14 text-slate-950 font-black",children:"Result"}),l.jsx("th",{className:"p-1.5 border border-slate-900 text-center w-12 text-slate-950 font-black",children:"Rank"})]})})"""

if old_mg_head in code:
    code = code.replace(old_mg_head, new_mg_head, 1)
    print("✓ Fixed Marksheet Gazette table header contrast.")
else:
    print("✗ old_mg_head not found.")

# 5. WORD EXPORT: Protect MS Word structure from scattering
# In Word helper ly(n,e): add strict MSO table styles
old_ly = """      table {        border-collapse: collapse;        width: 100%;      }      th, td {        padding: 5pt 6pt;        vertical-align: middle;      }      .header-title {        font-size: 15pt;        font-weight: 800;        text-align: center;        text-transform: uppercase;        color: #1e3a8a;      }      .sub-title {        font-size: 10.5pt;        font-weight: bold;        text-align: center;        color: #475569;      }      .badge-title {        font-size: 11.5pt;        font-weight: 800;        text-align: center;        background-color: #1e3a8a;        color: #ffffff;        padding: 4pt 8pt;      }"""

new_ly = """      table {        mso-table-lspace: 0pt !important;        mso-table-rspace: 0pt !important;        border-collapse: collapse !important;        width: 100% !important;        max-width: 100% !important;        margin: 0 auto !important;      }      th, td {        padding: 5pt 6pt;        vertical-align: middle;        mso-line-height-rule: exactly;        word-wrap: break-word;      }      .header-title {        font-size: 15pt;        font-weight: 900;        text-align: center;        text-transform: uppercase;        color: #000000;      }      .sub-title {        font-size: 10.5pt;        font-weight: bold;        text-align: center;        color: #334155;      }      .badge-title {        font-size: 11.5pt;        font-weight: 900;        text-align: center;        background-color: #f1f5f9;        color: #000000;        border: 1.5pt solid #000000;        padding: 4pt 8pt;      }"""

if old_ly in code:
    code = code.replace(old_ly, new_ly, 1)
    print("✓ Updated Word export helper ly.")
else:
    print("✗ old_ly not found.")

# In z0: ensure MCQ item tables don't scatter
old_z0_mcq_table = """<table width="100%" cellpadding="6" cellspacing="0" border="0" style="border-collapse:collapse; margin-bottom:6pt; page-break-inside:avoid; border-bottom:1pt solid #cbd5e1;">"""
new_z0_mcq_table = """<table width="100%" cellpadding="4" cellspacing="0" border="0" style="mso-table-lspace:0pt; mso-table-rspace:0pt; border-collapse:collapse; width:100%; table-layout:fixed; margin-bottom:6pt; page-break-inside:avoid; border-bottom:1pt solid #cbd5e1;">"""

if old_z0_mcq_table in code:
    code = code.replace(old_z0_mcq_table, new_z0_mcq_table)
    print("✓ Updated z0 MCQ tables to fixed layout without scattering.")

# In z0: ensure Short Questions group tables don't scatter
old_z0_sq_table = """<table width="100%" cellpadding="0" cellspacing="0" border="0" style="border-collapse:collapse; margin-bottom:12pt; page-break-inside:avoid; border:1pt solid #94a3b8;">"""
new_z0_sq_table = """<table width="100%" cellpadding="0" cellspacing="0" border="0" style="mso-table-lspace:0pt; mso-table-rspace:0pt; border-collapse:collapse; width:100%; table-layout:fixed; margin-bottom:12pt; page-break-inside:avoid; border:1pt solid #94a3b8;">"""

if old_z0_sq_table in code:
    code = code.replace(old_z0_sq_table, new_z0_sq_table)
    print("✓ Updated z0 SQ tables with MSO alignment.")

# Write updated code
with open('assets/index-DAioIUjd.js', 'w', encoding='utf-8') as f:
    f.write(code)

print(f"assets/index-DAioIUjd.js updated successfully! (size diff: {len(code) - orig_len})")
