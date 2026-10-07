import { DateSheetData, MarksheetData, StudentMarksRecord, UnifiedSchoolBranding } from '../types/extraDocs';

/**
 * Downloads an MSO HTML formatted .doc file
 */
function downloadWordDoc(contentHtml: string, fileName: string) {
  const fullHtml = `
  <html xmlns:o='urn:schemas-microsoft-com:office:office'
        xmlns:w='urn:schemas-microsoft-com:office:word'
        xmlns='http://www.w3.org/TR/REC-html40'>
  <head>
    <meta charset="utf-8">
    <title>${fileName}</title>
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
        color: #0f172a;
        line-height: 1.3;
      }
      table {
        border-collapse: collapse;
        width: 100%;
      }
      th, td {
        padding: 5pt 6pt;
        vertical-align: middle;
      }
      .header-title {
        font-size: 15pt;
        font-weight: 800;
        text-align: center;
        text-transform: uppercase;
        color: #1e3a8a;
      }
      .sub-title {
        font-size: 10.5pt;
        font-weight: bold;
        text-align: center;
        color: #475569;
      }
      .badge-title {
        font-size: 11.5pt;
        font-weight: 800;
        text-align: center;
        background-color: #1e3a8a;
        color: #ffffff;
        padding: 4pt 8pt;
      }
    </style>
  </head>
  <body>
    ${contentHtml}
  </body>
  </html>
  `;

  const blob = new Blob(['\uFEFF' + fullHtml], {
    type: 'application/msword;charset=utf-8',
  });
  const safeName = fileName.endsWith('.doc') ? fileName : `${fileName}.doc`;
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = safeName;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
}

/**
 * Exports Date Sheet to editable MS Word (.doc)
 */
export function exportDateSheetToWord(
  dateSheet: DateSheetData,
  branding: UnifiedSchoolBranding
) {
  const examTitle = dateSheet.customExamTitle || dateSheet.examType;

  const rowsHtml = dateSheet.rows
    .map(
      (r, idx) => `
    <tr style="background-color: ${idx % 2 === 0 ? '#ffffff' : '#f8fafc'};">
      <td align="center" style="border: 1pt solid #cbd5e1; font-weight: bold;">${idx + 1}</td>
      <td style="border: 1pt solid #cbd5e1; font-weight: bold;">${r.date || 'TBD'}</td>
      <td style="border: 1pt solid #cbd5e1; font-weight: bold; color: #1e3a8a;">${r.day || '-'}</td>
      <td style="border: 1pt solid #cbd5e1; font-size: 10.5pt; font-weight: bold;">${r.subject}</td>
      <td style="border: 1pt solid #cbd5e1; color: #334155;">${r.paperType || 'Standard Syllabus'}</td>
      <td align="center" style="border: 1pt solid #cbd5e1; font-weight: bold;">${r.timings || dateSheet.examTimings}</td>
    </tr>
  `
    )
    .join('');

  const rulesHtml = dateSheet.instructions
    .map(
      (ins, i) => `
    <div style="margin-bottom: 3pt; font-size: 9pt; color: #1e293b;">
      <strong>${i + 1}.</strong> ${ins}
    </div>
  `
    )
    .join('');

  const html = `
    <!-- Header -->
    <div style="text-align: center; border-bottom: 2pt solid #1e3a8a; padding-bottom: 8pt; margin-bottom: 10pt;">
      <div class="header-title">${branding.schoolName}</div>
      <div class="sub-title">${branding.campusName} &bull; ${branding.address}</div>
      <div style="font-size: 8.5pt; color: #64748b; margin-top: 2pt;">Phone: ${branding.phone} &bull; Pattern: ${branding.boardPattern || 'BISE Punjab'}</div>
      
      <div style="margin-top: 8pt; background-color: #1e3a8a; color: #ffffff; padding: 4pt 8pt; font-size: 11pt; font-weight: 800; letter-spacing: 0.5pt;">
        OFFICIAL DATE SHEET: ${examTitle.toUpperCase()} (${dateSheet.session})
      </div>
      
      <table style="margin-top: 6pt; font-size: 9pt; font-weight: bold;">
        <tr>
          <td width="33%" align="left">Class / Grade: <span style="color: #1e3a8a;">${dateSheet.classLevel}</span></td>
          <td width="33%" align="center">Shift: <span style="color: #1e3a8a;">${dateSheet.shift}</span></td>
          <td width="34%" align="right">Exam Timings: <span style="color: #1e3a8a;">${dateSheet.examTimings}</span></td>
        </tr>
      </table>
    </div>

    <!-- Date Sheet Table -->
    <table border="1" cellpadding="5" cellspacing="0" style="border-collapse: collapse; border: 1pt solid #cbd5e1; margin-bottom: 14pt;">
      <tr style="background-color: #0f172a; color: #ffffff; font-weight: 800; font-size: 9.5pt;">
        <th width="6%" align="center">Sr#</th>
        <th width="16%" align="left">Date</th>
        <th width="14%" align="left">Day</th>
        <th width="26%" align="left">Subject</th>
        <th width="24%" align="left">Paper / Syllabus Details</th>
        <th width="14%" align="center">Timing</th>
      </tr>
      ${rowsHtml}
    </table>

    <!-- General Instructions -->
    <div style="border: 1pt solid #cbd5e1; background-color: #f8fafc; padding: 8pt; margin-bottom: 24pt;">
      <div style="font-weight: 800; font-size: 9.5pt; color: #1e3a8a; margin-bottom: 4pt; border-bottom: 1pt solid #e2e8f0; padding-bottom: 2pt;">
        GENERAL EXAMINATION RULES & GUIDELINES FOR STUDENTS:
      </div>
      ${rulesHtml}
    </div>

    <!-- Signatures -->
    <table style="margin-top: 30pt; font-size: 9pt; font-weight: bold; text-align: center;">
      <tr>
        <td width="33%" style="border-top: 1pt solid #94a3b8; padding-top: 4pt;">
          Class Incharge
        </td>
        <td width="34%" style="border-top: 1pt solid #94a3b8; padding-top: 4pt;">
          Controller of Examinations
        </td>
        <td width="33%" style="border-top: 1pt solid #94a3b8; padding-top: 4pt;">
          Principal / Headmaster
        </td>
      </tr>
    </table>
  `;

  const fileName = `${dateSheet.classLevel.replace(/\s+/g, '_')}_Date_Sheet_${examTitle.replace(/\s+/g, '_')}.doc`;
  downloadWordDoc(html, fileName);
}

/**
 * Exports Single Student Result Card to editable MS Word (.doc)
 */
export function exportSingleResultCardToWord(
  student: StudentMarksRecord,
  marksheet: MarksheetData,
  branding: UnifiedSchoolBranding
) {
  const totalMaxMarks = marksheet.subjects.reduce((sum, s) => sum + s.totalMarks, 0);
  const totalObtMarks = marksheet.subjects.reduce((sum, s) => sum + (student.marks[s.id] ?? 0), 0);
  const percentage = totalMaxMarks > 0 ? ((totalObtMarks / totalMaxMarks) * 100).toFixed(1) : '0.0';

  const rowsHtml = marksheet.subjects
    .map((s, idx) => {
      const obt = student.marks[s.id] ?? 0;
      const isPass = obt >= s.passingMarks;
      const pct = s.totalMarks > 0 ? (obt / s.totalMarks) * 100 : 0;
      let grade = 'F';
      if (pct >= 90) grade = 'A+';
      else if (pct >= 80) grade = 'A';
      else if (pct >= 70) grade = 'B';
      else if (pct >= 60) grade = 'C';
      else if (pct >= 50) grade = 'D';
      else if (pct >= 40) grade = 'E';

      return `
      <tr style="background-color: ${idx % 2 === 0 ? '#ffffff' : '#f8fafc'};">
        <td align="center" style="border: 1pt solid #cbd5e1; font-weight: bold;">${idx + 1}</td>
        <td style="border: 1pt solid #cbd5e1; font-weight: bold;">${s.name}</td>
        <td align="center" style="border: 1pt solid #cbd5e1;">${s.totalMarks}</td>
        <td align="center" style="border: 1pt solid #cbd5e1; color: #64748b;">${s.passingMarks}</td>
        <td align="center" style="border: 1pt solid #cbd5e1; font-weight: 800; font-size: 10.5pt; color: ${isPass ? '#0f172a' : '#b91c1c'};">
          ${obt}
        </td>
        <td align="center" style="border: 1pt solid #cbd5e1; font-weight: bold; color: ${isPass ? '#059669' : '#b91c1c'};">
          ${grade}
        </td>
        <td align="center" style="border: 1pt solid #cbd5e1; font-weight: bold; color: ${isPass ? '#059669' : '#b91c1c'};">
          ${isPass ? 'PASS' : 'FAIL'}
        </td>
      </tr>
    `;
    })
    .join('');

  const html = `
    <!-- Header -->
    <div style="text-align: center; border-bottom: 2pt solid #1e3a8a; padding-bottom: 8pt; margin-bottom: 8pt;">
      <div class="header-title">${branding.schoolName}</div>
      <div class="sub-title">${branding.campusName} &bull; ${branding.address}</div>
      <div style="font-size: 8.5pt; color: #64748b; margin-top: 2pt;">Phone: ${branding.phone} &bull; ${branding.boardPattern || 'BISE Punjab'}</div>
      
      <div style="margin-top: 8pt; background-color: #1e3a8a; color: #ffffff; padding: 5pt 10pt; font-size: 12pt; font-weight: 800;">
        PROGRESS REPORT CARD / MARKSHEET (${marksheet.session})
      </div>
      <div style="font-size: 9.5pt; font-weight: bold; color: #1e3a8a; margin-top: 3pt;">
        EXAMINATION: ${marksheet.examCategory.toUpperCase()}
      </div>
    </div>

    <!-- Student Credentials Box -->
    <table border="1" cellpadding="6" cellspacing="0" style="border-collapse: collapse; border: 1.5pt solid #1e3a8a; margin-bottom: 12pt; background-color: #f8fafc; font-size: 9.5pt;">
      <tr>
        <td width="20%" style="font-weight: bold; color: #475569;">Roll Number:</td>
        <td width="30%" style="font-weight: 800; color: #1e3a8a; font-size: 11pt;">${student.rollNo}</td>
        <td width="20%" style="font-weight: bold; color: #475569;">Class & Grade:</td>
        <td width="30%" style="font-weight: bold;">${marksheet.classLevel}</td>
      </tr>
      <tr>
        <td style="font-weight: bold; color: #475569;">Student Name:</td>
        <td style="font-weight: 800; font-size: 10.5pt;">${student.name}</td>
        <td style="font-weight: bold; color: #475569;">Father's Name:</td>
        <td style="font-weight: bold;">${student.fatherName || '-'}</td>
      </tr>
      <tr>
        <td style="font-weight: bold; color: #475569;">Attendance:</td>
        <td style="font-weight: bold;">${student.attendance || '95%'}</td>
        <td style="font-weight: bold; color: #475569;">Position / Rank:</td>
        <td style="font-weight: 800; color: #059669;">${student.rank || '-'}</td>
      </tr>
    </table>

    <!-- Subject Marks Breakdown -->
    <table border="1" cellpadding="5" cellspacing="0" style="border-collapse: collapse; border: 1pt solid #cbd5e1; margin-bottom: 10pt;">
      <tr style="background-color: #0f172a; color: #ffffff; font-weight: 800; font-size: 9pt;">
        <th width="6%" align="center">Sr#</th>
        <th width="34%" align="left">Subject Name</th>
        <th width="14%" align="center">Total Marks</th>
        <th width="14%" align="center">Pass Marks</th>
        <th width="14%" align="center">Obtained</th>
        <th width="9%" align="center">Grade</th>
        <th width="9%" align="center">Status</th>
      </tr>
      ${rowsHtml}
      <tr style="background-color: #e2e8f0; font-weight: 800; font-size: 10pt;">
        <td colspan="2" align="right" style="border: 1pt solid #cbd5e1; padding-right: 8pt;">GRAND TOTAL:</td>
        <td align="center" style="border: 1pt solid #cbd5e1;">${totalMaxMarks}</td>
        <td align="center" style="border: 1pt solid #cbd5e1;">-</td>
        <td align="center" style="border: 1pt solid #cbd5e1; font-size: 11pt; color: #1e3a8a;">${totalObtMarks}</td>
        <td align="center" style="border: 1pt solid #cbd5e1; color: #1e3a8a;">${student.grade || 'A'}</td>
        <td align="center" style="border: 1pt solid #cbd5e1; color: ${student.status === 'FAIL' ? '#b91c1c' : '#059669'};">
          ${student.status || 'PASS'}
        </td>
      </tr>
    </table>

    <!-- Performance Summary Box -->
    <table border="1" cellpadding="6" cellspacing="0" style="border-collapse: collapse; border: 1pt solid #cbd5e1; margin-bottom: 12pt; background-color: #f1f5f9; text-align: center; font-weight: bold;">
      <tr>
        <td width="25%">Percentage: <span style="font-size: 11pt; color: #1e3a8a;">${percentage}%</span></td>
        <td width="25%">Grade: <span style="font-size: 11pt; color: #1e3a8a;">${student.grade || 'A'}</span></td>
        <td width="25%">Final Result: <span style="font-size: 11pt; color: ${student.status === 'FAIL' ? '#b91c1c' : '#059669'};">${student.status || 'PASS'}</span></td>
        <td width="25%">Rank: <span style="font-size: 11pt; color: #059669;">${student.rank || '-'}</span></td>
      </tr>
    </table>

    <!-- Teacher Remarks -->
    <div style="border: 1pt solid #cbd5e1; padding: 6pt 8pt; margin-bottom: 24pt; font-size: 9pt;">
      <strong>Teacher's Assessment & Remarks:</strong>
      <span style="color: #1e3a8a; font-weight: bold; margin-left: 6pt;">${student.remarks || 'Shows consistent effort and commendable dedication. Keep up the high standard!'}</span>
    </div>

    <!-- Signatures Table -->
    <table style="margin-top: 35pt; font-size: 9pt; font-weight: bold; text-align: center;">
      <tr>
        <td width="25%" style="border-top: 1pt solid #94a3b8; padding-top: 4pt;">Class Teacher</td>
        <td width="25%" style="border-top: 1pt solid #94a3b8; padding-top: 4pt;">Exam Incharge</td>
        <td width="25%" style="border-top: 1pt solid #94a3b8; padding-top: 4pt;">Parent / Guardian</td>
        <td width="25%" style="border-top: 1pt solid #94a3b8; padding-top: 4pt;">Principal / Seal</td>
      </tr>
    </table>
  `;

  const fileName = `Result_Card_Roll_${student.rollNo}_${student.name.replace(/\s+/g, '_')}.doc`;
  downloadWordDoc(html, fileName);
}

/**
 * Exports Class-Wide Consolidated Master Sheet to MS Word (.doc)
 */
export function exportMasterSheetToWord(
  marksheet: MarksheetData,
  branding: UnifiedSchoolBranding
) {
  const totalMaxMarks = marksheet.subjects.reduce((sum, s) => sum + s.totalMarks, 0);

  const subjectHeaders = marksheet.subjects
    .map((s) => `<th align="center" style="font-size: 8pt; padding: 3pt;">${s.name}<br/><span style="color:#cbd5e1; font-size:7pt;">(${s.totalMarks})</span></th>`)
    .join('');

  const rowsHtml = marksheet.students
    .map((st, idx) => {
      const subjectCols = marksheet.subjects
        .map((s) => {
          const obt = st.marks[s.id] ?? 0;
          const isPass = obt >= s.passingMarks;
          return `<td align="center" style="border: 1pt solid #cbd5e1; font-size: 8.5pt; color: ${isPass ? '#0f172a' : '#b91c1c'}; font-weight: ${isPass ? 'normal' : 'bold'};">${obt}</td>`;
        })
        .join('');

      const obtTotal = marksheet.subjects.reduce((sum, s) => sum + (st.marks[s.id] ?? 0), 0);
      const pct = totalMaxMarks > 0 ? ((obtTotal / totalMaxMarks) * 100).toFixed(1) : '0';

      return `
      <tr style="background-color: ${idx % 2 === 0 ? '#ffffff' : '#f8fafc'};">
        <td align="center" style="border: 1pt solid #cbd5e1; font-weight: bold; font-size: 8.5pt;">${st.rollNo}</td>
        <td style="border: 1pt solid #cbd5e1; font-weight: bold; font-size: 8.5pt;">${st.name}</td>
        <td style="border: 1pt solid #cbd5e1; font-size: 8pt; color: #475569;">${st.fatherName || '-'}</td>
        ${subjectCols}
        <td align="center" style="border: 1pt solid #cbd5e1; font-weight: 800; font-size: 9pt; color: #1e3a8a;">${obtTotal}</td>
        <td align="center" style="border: 1pt solid #cbd5e1; font-size: 8.5pt; font-weight: bold;">${pct}%</td>
        <td align="center" style="border: 1pt solid #cbd5e1; font-weight: bold; font-size: 8.5pt;">${st.grade || 'A'}</td>
        <td align="center" style="border: 1pt solid #cbd5e1; font-weight: bold; font-size: 8pt; color: ${st.status === 'FAIL' ? '#b91c1c' : '#059669'};">
          ${st.status || 'PASS'}
        </td>
        <td align="center" style="border: 1pt solid #cbd5e1; font-weight: bold; font-size: 8pt;">${st.rank || '-'}</td>
      </tr>
    `;
    })
    .join('');

  const html = `
    <!-- Header -->
    <div style="text-align: center; border-bottom: 2pt solid #1e3a8a; padding-bottom: 6pt; margin-bottom: 8pt;">
      <div class="header-title">${branding.schoolName}</div>
      <div class="sub-title">${branding.campusName} &bull; ${branding.address}</div>
      <div style="margin-top: 6pt; background-color: #1e3a8a; color: #ffffff; padding: 4pt 8pt; font-size: 11pt; font-weight: 800;">
        CONSOLIDATED RESULT GAZETTE / MASTER SHEET (${marksheet.session})
      </div>
      <div style="font-size: 9pt; font-weight: bold; color: #334155; margin-top: 3pt;">
        Class: ${marksheet.classLevel} &bull; Examination: ${marksheet.examCategory} &bull; Total Students: ${marksheet.students.length}
      </div>
    </div>

    <!-- Master Table -->
    <table border="1" cellpadding="4" cellspacing="0" style="border-collapse: collapse; border: 1pt solid #cbd5e1; margin-bottom: 14pt; width: 100%;">
      <tr style="background-color: #0f172a; color: #ffffff; font-weight: 800; font-size: 8.5pt;">
        <th width="6%" align="center">Roll#</th>
        <th width="14%" align="left">Student Name</th>
        <th width="12%" align="left">Father's Name</th>
        ${subjectHeaders}
        <th width="8%" align="center">Total<br/><span style="font-size:7pt;">(${totalMaxMarks})</span></th>
        <th width="6%" align="center">%</th>
        <th width="5%" align="center">Grd</th>
        <th width="6%" align="center">Result</th>
        <th width="5%" align="center">Rank</th>
      </tr>
      ${rowsHtml}
    </table>

    <!-- Signatures -->
    <table style="margin-top: 30pt; font-size: 8.5pt; font-weight: bold; text-align: center;">
      <tr>
        <td width="33%" style="border-top: 1pt solid #94a3b8; padding-top: 4pt;">Class Incharge</td>
        <td width="34%" style="border-top: 1pt solid #94a3b8; padding-top: 4pt;">Controller of Examinations</td>
        <td width="33%" style="border-top: 1pt solid #94a3b8; padding-top: 4pt;">Principal / Headmaster</td>
      </tr>
    </table>
  `;

  const fileName = `Master_Marksheet_${marksheet.classLevel.replace(/\s+/g, '_')}_${marksheet.examCategory.replace(/\s+/g, '_')}.doc`;
  downloadWordDoc(html, fileName);
}
