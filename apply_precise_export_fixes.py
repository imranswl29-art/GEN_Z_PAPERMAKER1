#!/usr/bin/env python3
import sys

with open('assets/index-DAioIUjd.js', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. DateSheet Excel replacement
idx1 = code.find('function exportDateSheetToExcel(ds, brand)')
h1 = code.find('const html = `', idx1)
h1_end = code.find('downloadExcelFile(html,', h1)
assert h1 != -1 and h1_end != -1, "DateSheet HTML chunk not found!"

new_ds_html = """const html = `<!DOCTYPE html><html xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:x="urn:schemas-microsoft-com:office:excel" xmlns="http://www.w3.org/TR/REC-html40">
  <head><meta http-equiv="Content-Type" content="application/vnd.ms-excel; charset=utf-8">
  <title>${brandTitle} - Date Sheet</title>
  <style>
    body { font-family: 'Segoe UI', Calibri, Arial, sans-serif; font-size: 10pt; color: #000000; }
    table { border-collapse: collapse; width: 100%; }
    td, th { mso-line-height-rule: exactly; }
  </style>
  </head>
  <body>
    <table border="1" cellpadding="5" cellspacing="0" style="border-collapse:collapse; width:100%;">
      <tr><td colspan="6" style="background-color: #f1f5f9; color: #000000; font-size: 14pt; font-weight: 900; text-align: center; padding: 10pt; border: 1.5pt solid #475569;">${brandTitle}</td></tr>
      <tr><td colspan="6" style="background-color: #e2e8f0; color: #000000; font-size: 10.5pt; text-align: center; padding: 6pt; font-weight: bold; border: 1pt solid #64748b;">${brandCampus} &bull; OFFICIAL DATE SHEET &bull; ${examTitle.toUpperCase()}</td></tr>
      <tr>
        <td colspan="3" style="padding: 6pt; font-weight: bold; color: #000000; border: 1pt solid #cbd5e1; background-color: #ffffff;">Class / Grade: <strong>${ds.classLevel}</strong></td>
        <td colspan="3" align="right" style="padding: 6pt; font-weight: bold; color: #000000; border: 1pt solid #cbd5e1; background-color: #ffffff;">Session: ${ds.session || "2025-2026"} &bull; Shift: ${ds.shift || "Morning"}</td>
      </tr>
      <tr><td colspan="6" style="height: 6pt; border: none; background-color: #ffffff;"></td></tr>
      <thead>
        <tr style="background-color: #cbd5e1;">
          <th style="background-color: #cbd5e1; color: #000000; font-weight: 900; padding: 8pt; border: 1pt solid #475569; text-align: center;">Sr#</th>
          <th style="background-color: #cbd5e1; color: #000000; font-weight: 900; padding: 8pt; border: 1pt solid #475569; text-align: left;">Examination Date (تاریخ)</th>
          <th style="background-color: #cbd5e1; color: #000000; font-weight: 900; padding: 8pt; border: 1pt solid #475569; text-align: left;">Day (دن)</th>
          <th style="background-color: #cbd5e1; color: #000000; font-weight: 900; padding: 8pt; border: 1pt solid #475569; text-align: left;">Subject Name (مضمون)</th>
          <th style="background-color: #cbd5e1; color: #000000; font-weight: 900; padding: 8pt; border: 1pt solid #475569; text-align: left;">Syllabus / Paper Scope</th>
          <th style="background-color: #cbd5e1; color: #000000; font-weight: 900; padding: 8pt; border: 1pt solid #475569; text-align: center;">Exam Timings (وقت)</th>
        </tr>
      </thead>
      <tbody>
        ${rows}
      </tbody>
    </table>
    <br/>
    <div style="background-color: #f8fafc; border: 1pt solid #cbd5e1; padding: 8pt; color: #000000;">
      <strong style="color: #000000; font-size: 10.5pt;">Important Examination Instructions & Rules (امتحانی ہدایات):</strong>
      <ol style="margin-top: 6pt; padding-left: 20pt; color: #000000;">
        ${instructions}
      </ol>
    </div>
    <br/>
    <table style="margin-top: 20pt; text-align: center; font-weight: bold; width: 100%; color: #000000;">
      <tr>
        <td style="border-top: 1.5pt solid #475569; padding-top: 6pt; width: 33%; color: #000000;">Class Incharge</td>
        <td style="border-top: 1.5pt solid #475569; padding-top: 6pt; width: 34%; color: #000000;">Controller of Examinations</td>
        <td style="border-top: 1.5pt solid #475569; padding-top: 6pt; width: 33%; color: #000000;">Principal / Headmaster</td>
      </tr>
    </table>
  </body></html>`;  """

code = code[:h1] + new_ds_html + code[h1_end:]
print("✓ DateSheet Excel chunk replaced successfully.")

# 2. ResultCard Excel replacement
idx2 = code.find('function exportResultCardToExcel(st, marksheet, brand)')
h2 = code.find('const html = `', idx2)
h2_end = code.find('downloadExcelFile(html,', h2)
assert h2 != -1 and h2_end != -1, "ResultCard HTML chunk not found!"

new_rc_html = """const html = `<!DOCTYPE html><html xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:x="urn:schemas-microsoft-com:office:excel" xmlns="http://www.w3.org/TR/REC-html40">
  <head><meta http-equiv="Content-Type" content="application/vnd.ms-excel; charset=utf-8">
  <title>${brandTitle} - Result Card Roll ${st.rollNo}</title>
  <style>
    body { font-family: 'Segoe UI', Calibri, Arial, sans-serif; font-size: 10pt; color: #000000; }
    table { border-collapse: collapse; width: 100%; }
    td, th { mso-line-height-rule: exactly; }
  </style>
  </head>
  <body>
    <table border="1" cellpadding="5" cellspacing="0" style="border-collapse:collapse; width:100%;">
      <tr><td colspan="8" style="background-color: #f1f5f9; color: #000000; font-size: 14pt; font-weight: 900; text-align: center; padding: 10pt; border: 1.5pt solid #475569;">${brandTitle}</td></tr>
      <tr><td colspan="8" style="background-color: #e2e8f0; color: #000000; font-size: 10.5pt; text-align: center; padding: 6pt; font-weight: bold; border: 1pt solid #64748b;">${brandCampus} &bull; OFFICIAL STUDENT EXAMINATION RESULT CARD</td></tr>
      <tr>
        <td colspan="4" style="padding: 6pt; border: 1pt solid #cbd5e1; font-weight: bold; color: #000000; background-color: #ffffff;">Roll Number: <span style="font-size: 12pt; color: #000000; font-weight: 900;">${st.rollNo}</span></td>
        <td colspan="4" style="padding: 6pt; border: 1pt solid #cbd5e1; font-weight: bold; color: #000000; background-color: #ffffff;">Candidate Name: <span style="font-size: 11pt; color: #000000; font-weight: 900;">${st.name}</span></td>
      </tr>
      <tr>
        <td colspan="4" style="padding: 6pt; border: 1pt solid #cbd5e1; font-weight: bold; color: #000000; background-color: #ffffff;">Father's Name: ${st.fatherName || "-"}</td>
        <td colspan="4" style="padding: 6pt; border: 1pt solid #cbd5e1; font-weight: bold; color: #000000; background-color: #ffffff;">Class & Section: ${marksheet.classLevel} (Section ${st.section || "A"})</td>
      </tr>
      <tr>
        <td colspan="4" style="padding: 6pt; border: 1pt solid #cbd5e1; font-weight: bold; color: #000000; background-color: #ffffff;">Academic Session: ${marksheet.session || "2025-2026"} &bull; ${marksheet.examCategory || "Annual"}</td>
        <td colspan="4" style="padding: 6pt; border: 1pt solid #cbd5e1; font-weight: bold; color: #000000; background-color: #ffffff;">Attendance: ${st.attendance || "96%"} &bull; Position / Rank: <span style="color: #000000; font-size: 11pt; font-weight: 900;">${st.rank || "-"}</span></td>
      </tr>
      <tr><td colspan="8" style="height: 6pt; border: none; background-color: #ffffff;"></td></tr>
      <thead>
        <tr style="background-color: #cbd5e1;">
          <th style="background-color: #cbd5e1; color: #000000; font-weight: 900; padding: 8pt; border: 1pt solid #475569; text-align: center;">Sr#</th>
          <th style="background-color: #cbd5e1; color: #000000; font-weight: 900; padding: 8pt; border: 1pt solid #475569; text-align: left;">Subject Name</th>
          <th style="background-color: #cbd5e1; color: #000000; font-weight: 900; padding: 8pt; border: 1pt solid #475569; text-align: center;">Total Marks</th>
          <th style="background-color: #cbd5e1; color: #000000; font-weight: 900; padding: 8pt; border: 1pt solid #475569; text-align: center;">Pass Marks</th>
          <th style="background-color: #cbd5e1; color: #000000; font-weight: 900; padding: 8pt; border: 1pt solid #475569; text-align: center;">Marks Obtained</th>
          <th style="background-color: #cbd5e1; color: #000000; font-weight: 900; padding: 8pt; border: 1pt solid #475569; text-align: center;">Percentage %</th>
          <th style="background-color: #cbd5e1; color: #000000; font-weight: 900; padding: 8pt; border: 1pt solid #475569; text-align: center;">Grade</th>
          <th style="background-color: #cbd5e1; color: #000000; font-weight: 900; padding: 8pt; border: 1pt solid #475569; text-align: center;">Status</th>
        </tr>
      </thead>
      <tbody>
        ${rows}
        <tr style="background-color: #e2e8f0; font-weight: bold; color: #000000;">
          <td colspan="2" align="right" style="padding: 8pt; border: 1.5pt solid #475569; font-size: 11pt; color: #000000;">GRAND TOTAL / OVERALL:</td>
          <td align="center" style="padding: 8pt; border: 1.5pt solid #475569; font-size: 11pt; color: #000000;">${totalMax}</td>
          <td align="center" style="padding: 8pt; border: 1.5pt solid #475569; color: #000000;">-</td>
          <td align="center" style="padding: 8pt; border: 1.5pt solid #475569; font-size: 12pt; color: #000000; font-weight: 900;">${totalObtained}</td>
          <td align="center" style="padding: 8pt; border: 1.5pt solid #475569; font-size: 11pt; color: #000000;">${overallPct}%</td>
          <td align="center" style="padding: 8pt; border: 1.5pt solid #475569; font-size: 12pt; color: #000000; font-weight: 900;">${overallGrade}</td>
          <td align="center" style="padding: 8pt; border: 1.5pt solid #475569; font-size: 11pt; color: ${hasFailed ? "#b91c1c" : "#047857"}; font-weight: 900;">${finalStatus}</td>
        </tr>
      </tbody>
    </table>
    <br/>
    <div style="background-color: #f8fafc; border: 1pt solid #cbd5e1; padding: 8pt; font-size: 9.5pt; color: #000000;">
      <strong>Remarks & Observations:</strong> ${st.remarks || "Diligent and consistent effort. Keep striving for academic excellence."}
    </div>
    <br/>
    <table style="margin-top: 25pt; text-align: center; font-weight: bold; width: 100%; color: #000000;">
      <tr>
        <td style="border-top: 1.5pt solid #475569; padding-top: 6pt; width: 33%; color: #000000;">Class Incharge</td>
        <td style="border-top: 1.5pt solid #475569; padding-top: 6pt; width: 34%; color: #000000;">Controller of Examinations</td>
        <td style="border-top: 1.5pt solid #475569; padding-top: 6pt; width: 33%; color: #000000;">Principal / Headmaster</td>
      </tr>
    </table>
  </body></html>`;  """

code = code[:h2] + new_rc_html + code[h2_end:]
print("✓ ResultCard Excel chunk replaced successfully.")

# 3. ly Word export helper replacement
idx3 = code.find('function ly(n,e){')
h3 = code.find('const t=`', idx3)
h3_end = code.find('`,r=new Blob([', h3)
assert h3 != -1 and h3_end != -1, "ly HTML chunk not found!"

new_ly_html = """const t=`
  <html xmlns:o='urn:schemas-microsoft-com:office:office'
        xmlns:w='urn:schemas-microsoft-com:office:word'
        xmlns='http://www.w3.org/TR/REC-html40'>
  <head>
    <meta charset="utf-8">
    <title>${e}</title>
    <!--[if gte mso 9]>
    <xml>
      <w:WordDocument>
        <w:View>Print</w:View>
        <w:Zoom>100</w:Zoom>
        <w:DoNotOptimizeForBrowser/>
      </w:WordDocument>
    </xml>
    <![endif]-->
    <style>
      @page {
        size: 210mm 297mm;
        margin: 12mm 12mm 12mm 12mm;
        mso-page-orientation: portrait;
      }
      body {
        font-family: 'Calibri', 'Arial', sans-serif;
        font-size: 10pt;
        color: #000000;
        line-height: 1.3;
      }
      table {
        mso-table-lspace: 0pt !important;
        mso-table-rspace: 0pt !important;
        border-collapse: collapse !important;
        width: 100% !important;
        max-width: 100% !important;
        margin: 0 auto !important;
      }
      th, td {
        padding: 5pt 6pt;
        vertical-align: middle;
        mso-line-height-rule: exactly;
        word-wrap: break-word;
      }
      .header-title {
        font-size: 15pt;
        font-weight: 900;
        text-align: center;
        text-transform: uppercase;
        color: #000000;
      }
      .sub-title {
        font-size: 10.5pt;
        font-weight: bold;
        text-align: center;
        color: #334155;
      }
      .badge-title {
        font-size: 11.5pt;
        font-weight: 900;
        text-align: center;
        background-color: #f1f5f9;
        color: #000000;
        border: 1.5pt solid #000000;
        padding: 4pt 8pt;
      }
    </style>
  </head>
  <body>
    ${n}
  </body>
  </html>
  `"""

code = code[:h3] + new_ly_html + code[h3_end:]
print("✓ ly Word helper chunk replaced successfully.")

# 4. Section B in jS (Answer Key)
target_sec_b = 'className:"bg-slate-900 text-white px-3 py-1.5 rounded-xs flex items-center justify-between text-xs font-black uppercase tracking-wider",children:[l.jsx("span",{children:"SECTION - B: SUBJECTIVE MARKING RUBRICS & MODEL GUIDELINES"}),l.jsxs("span",{children:[n.subjectiveSection.totalMarks," Marks"]})]}'
replace_sec_b = 'className:"bg-slate-100 text-slate-950 border-2 border-slate-900 px-3 py-1.5 rounded flex items-center justify-between text-xs font-black uppercase tracking-wider print:bg-slate-100 print:text-black",children:[l.jsx("span",{children:"SECTION - B: SUBJECTIVE MARKING RUBRICS & MODEL GUIDELINES"}),l.jsxs("span",{children:[n.subjectiveSection.totalMarks," Marks"]})]}'

if target_sec_b in code:
    code = code.replace(target_sec_b, replace_sec_b, 1)
    print("✓ Replaced Section B in jS with printer-safe high contrast.")
else:
    print("Warning: target_sec_b not found directly, let's search substring.")
    sub = '"SECTION - B: SUBJECTIVE MARKING RUBRICS & MODEL GUIDELINES"'
    pos = code.find(sub)
    if pos != -1:
        start_div = code.rfind('l.jsxs("div",{className:"', 0, pos)
        end_cls = code.find('",children:[', start_div)
        code = code[:start_div] + 'l.jsxs("div",{className:"bg-slate-100 text-slate-950 border-2 border-slate-900 px-3 py-1.5 rounded flex items-center justify-between text-xs font-black uppercase tracking-wider print:bg-slate-100 print:text-black' + code[end_cls:]
        print("✓ Successfully replaced Section B class in jS!")

# Save final bundle
with open('assets/index-DAioIUjd.js', 'w', encoding='utf-8') as f:
    f.write(code)

print("All precise export and print fixes applied successfully to bundle!")
