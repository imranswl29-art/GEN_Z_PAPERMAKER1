import React, { useState } from 'react';
import { Printer, X, FileDown, Loader2 } from 'lucide-react';
import { GeneratedExamPaper } from '../types/paper';
import { exportElementToPdf } from '../utils/exportPdf';

interface BubbleSheetViewProps {
  paper: GeneratedExamPaper;
  onClose?: () => void;
  isEmbedded?: boolean;
  savedPapers?: GeneratedExamPaper[];
  onSelectPaper?: (paper: GeneratedExamPaper) => void;
}

export const BubbleSheetView: React.FC<BubbleSheetViewProps> = ({
  paper,
  onClose,
  isEmbedded = false,
  savedPapers,
  onSelectPaper,
}) => {
  const [isDownloadingPdf, setIsDownloadingPdf] = useState(false);
  const mcqCount = paper.objectiveSection.questions.length || 15;
  const digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
  const rollCols = 6;

  const handlePrint = () => {
    const prevTitle = document.title;
    const cleanSubject = (paper.header.subjectName || 'Paper').replace(/\s+/g, '_');
    const cleanClass = paper.header.classLevel || '9th';
    document.title = `${cleanClass}_Class_${cleanSubject}_OMR_Bubble_Sheet`;
    window.print();
    setTimeout(() => {
      document.title = prevTitle;
    }, 1500);
  };

  const handleDownloadPdf = async () => {
    setIsDownloadingPdf(true);
    try {
      const cleanSubject = (paper.header.subjectName || 'Paper').replace(/[^a-zA-Z0-9_-]/g, '_');
      const cleanClass = paper.header.classLevel || '9th';
      const fileName = `${cleanClass}_Class_${cleanSubject}_OMR_Bubble_Sheet.pdf`;
      await exportElementToPdf('bubble-sheet-printable-area', fileName);
    } finally {
      setIsDownloadingPdf(false);
    }
  };

  return (
    <div
      className={
        isEmbedded
          ? 'w-full max-w-5xl mx-auto space-y-4 print:static print:p-0 print:m-0 print:bg-white print:overflow-visible print:block print:w-full print:h-auto font-sans pb-12'
          : 'fixed inset-0 z-50 bg-black/60 flex items-center justify-center p-4 overflow-y-auto print:static print:p-0 print:m-0 print:bg-white print:overflow-visible print:block print:w-full print:h-auto'
      }
    >
      <div
        className={
          isEmbedded
            ? 'bg-white rounded-2xl shadow-xl border border-slate-300 flex flex-col overflow-hidden print:max-w-none print:w-full print:max-h-none print:shadow-none print:rounded-none print:border-none print:overflow-visible print:block'
            : 'bg-white rounded-xl shadow-2xl max-w-4xl w-full max-h-[90vh] flex flex-col overflow-hidden print:max-w-none print:w-full print:max-h-none print:shadow-none print:rounded-none print:border-none print:overflow-visible print:block'
        }
      >
        {/* Top bar (hidden in print) */}
        <div className="p-4 bg-slate-900 text-white flex flex-wrap items-center justify-between gap-3 no-print">
          <div className="flex items-center gap-3">
            <span className="font-bold text-lg">BISE Punjab MCQ Response Sheet (OMR Bubble Sheet)</span>
            <span className="text-xs bg-emerald-500/20 text-emerald-300 px-2.5 py-0.5 rounded font-mono">
              {paper.header.classLevel} · {paper.header.subjectName}
            </span>
          </div>

          {/* Quick Paper Switcher for Saved Papers if in full view */}
          {savedPapers && savedPapers.length > 0 && onSelectPaper && (
            <div className="flex items-center gap-2">
              <span className="text-xs text-slate-400 font-bold hidden md:inline">Select Paper:</span>
              <select
                value={paper.id}
                onChange={(e) => {
                  const found = savedPapers.find((p) => p.id === e.target.value);
                  if (found) onSelectPaper(found);
                }}
                className="bg-slate-800 text-white border border-slate-700 text-xs rounded-lg px-2.5 py-1.5 font-bold cursor-pointer"
              >
                {savedPapers.map((sp) => (
                  <option key={sp.id} value={sp.id}>
                    {sp.header.classLevel} {sp.header.subjectName} ({sp.header.examTitle})
                  </option>
                ))}
              </select>
            </div>
          )}

          <div className="flex items-center gap-2">
            <button
              onClick={handleDownloadPdf}
              disabled={isDownloadingPdf}
              className="btn-3d btn-3d-red flex items-center gap-1.5 px-3 py-1.5 text-white rounded-lg text-xs font-bold cursor-pointer disabled:opacity-50"
              title="Download Full OMR Bubble Sheet as A4 PDF"
            >
              {isDownloadingPdf ? <Loader2 className="w-3.5 h-3.5 animate-spin" /> : <FileDown className="w-3.5 h-3.5" />}
              <span>{isDownloadingPdf ? 'Downloading PDF...' : 'Download PDF'}</span>
            </button>
            <button
              onClick={handlePrint}
              className="btn-print-preview"
            >
              <Printer className="w-4 h-4 text-emerald-100" />
              <span>Print & Preview</span>
            </button>
            {onClose && (
              <button
                onClick={onClose}
                className="p-1.5 hover:bg-slate-800 text-slate-400 hover:text-white rounded-lg transition-colors cursor-pointer flex items-center gap-1 text-xs"
                title={isEmbedded ? 'Back to Dashboard' : 'Close'}
              >
                {isEmbedded ? <span>Back</span> : <X className="w-5 h-5" />}
              </button>
            )}
          </div>
        </div>

        {/* Printable Sheet Content */}
        <div id="bubble-sheet-printable-area" className="p-6 md:p-10 overflow-y-auto bg-white print-container font-sans text-slate-900">
          <div className="border-2 border-slate-900 p-6 rounded-sm bg-white relative">
            {/* Header */}
            <div className="paper-header border-b-2 border-slate-900 pb-3 mb-4 text-center">
              <div className="header-row flex items-center justify-between gap-3 mb-2">
                <div className="school-monogram-container shrink-0">
                  <div className="w-14 h-14 border-2 border-slate-900 rounded-full p-1 bg-white flex items-center justify-center overflow-hidden shrink-0 shadow-2xs">
                    {paper.header.customLogoUrl ? (
                      <img
                        src={paper.header.customLogoUrl}
                        alt="School Monogram"
                        className="w-full h-full object-contain"
                      />
                    ) : (
                      <div className="w-full h-full rounded-full bg-slate-900 text-white flex flex-col items-center justify-center p-1 text-center">
                        <span className="text-[8px] font-black uppercase tracking-tighter">OMR SEAL</span>
                      </div>
                    )}
                  </div>
                </div>
                <div className="school-name-col flex-1 text-center min-w-0 px-2">
                  <h1 className="school-name-title text-xl sm:text-2xl font-black uppercase tracking-tight text-slate-950 font-serif leading-tight">
                    {paper.header.instituteName}
                  </h1>
                  <p className="text-xs sm:text-sm font-bold text-slate-700 mt-0.5">
                    {paper.header.campusName ? `${paper.header.campusName} • ` : ''}
                    {paper.header.boardPattern || 'BISE PUNJAB BOARD EXAMINATION'}
                  </p>
                </div>
                <div className="shrink-0 text-right font-mono text-[10px] font-bold border border-slate-900 px-2.5 py-1 rounded bg-slate-50">
                  <div className="text-slate-700">RESPONSE SHEET</div>
                  <div className="text-blue-900 font-black">{paper.header.classLevel.toUpperCase()} CLASS</div>
                </div>
              </div>

              <div className="flex justify-between items-center text-xs mt-2 font-medium border-t border-slate-300 pt-2 px-2 bg-slate-50/60 p-1.5">
                <span>Class: <strong>{paper.header.classLevel}</strong></span>
                <span>Subject: <strong>{paper.header.subjectName}</strong></span>
                <span>Date: <strong>{paper.header.dateStr}</strong></span>
                <span>Max MCQs: <strong>{mcqCount}</strong></span>
              </div>
            </div>

            {/* Student info and Roll Number Bubble Grid */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6 pb-4 border-b border-slate-300">
              <div className="space-y-3">
                <div className="flex items-center gap-2">
                  <span className="text-xs font-bold uppercase w-28">Student Name:</span>
                  <div className="flex-1 border-b border-dashed border-slate-500 h-6"></div>
                </div>
                <div className="flex items-center gap-2">
                  <span className="text-xs font-bold uppercase w-28">Father Name:</span>
                  <div className="flex-1 border-b border-dashed border-slate-500 h-6"></div>
                </div>
                <div className="flex items-center gap-2">
                  <span className="text-xs font-bold uppercase w-28">Section / Group:</span>
                  <div className="flex-1 border-b border-dashed border-slate-500 h-6"></div>
                </div>
                <div className="flex items-center gap-2">
                  <span className="text-xs font-bold uppercase w-28">Paper Code:</span>
                  <div className="flex gap-2">
                    {['A', 'B', 'C', 'D'].map((code) => (
                      <div key={code} className="flex items-center gap-1 text-xs">
                        <span className="w-5 h-5 rounded-full border border-slate-800 flex items-center justify-center font-bold text-[10px]">
                          {code}
                        </span>
                      </div>
                    ))}
                  </div>
                </div>
              </div>

              {/* Roll Number OMR Grid */}
              <div className="border border-slate-400 p-2 bg-slate-50 rounded">
                <div className="text-[11px] font-bold text-center mb-1 uppercase tracking-wide">
                  Roll Number
                </div>
                <div className="flex justify-center gap-1.5 mb-1.5">
                  {Array.from({ length: rollCols }).map((_, c) => (
                    <div key={c} className="w-6 h-6 border-2 border-slate-700 bg-white"></div>
                  ))}
                </div>
                <div className="space-y-0.5">
                  {digits.map((d) => (
                    <div key={d} className="flex justify-center gap-1.5">
                      {Array.from({ length: rollCols }).map((_, c) => (
                        <div
                          key={c}
                          className="w-5 h-5 rounded-full border border-slate-600 flex items-center justify-center text-[10px] font-mono text-slate-700 bg-white"
                        >
                          {d}
                        </div>
                      ))}
                    </div>
                  ))}
                </div>
              </div>
            </div>

            {/* Bubble Rows for MCQs */}
            <div className="mb-4">
              <h3 className="text-xs font-bold uppercase tracking-wider text-center bg-slate-800 text-white py-1 mb-3">
                Question Response Bubbles (Fill One Circle per Question completely)
              </h3>
              <div className="bubble-grid-print grid grid-cols-2 sm:grid-cols-3 gap-x-6 gap-y-2">
                {Array.from({ length: Math.max(mcqCount, 15) }).map((_, idx) => {
                  const qNum = idx + 1;
                  return (
                    <div
                      key={qNum}
                      className="flex items-center justify-between border-b border-slate-200 py-1 px-1 text-xs"
                    >
                      <span className="font-bold w-6 text-slate-800">Q.{qNum}</span>
                      <div className="flex items-center gap-2">
                        {['A', 'B', 'C', 'D'].map((opt) => (
                          <div
                            key={opt}
                            className="w-6 h-6 rounded-full border border-slate-800 flex items-center justify-center text-[11px] font-bold hover:bg-slate-200 cursor-pointer"
                          >
                            {opt}
                          </div>
                        ))}
                      </div>
                    </div>
                  );
                })}
              </div>
            </div>

            {/* Instructions */}
            <div className="mt-4 pt-3 border-t border-slate-400 text-[10px] text-slate-600 space-y-1">
              <div className="font-bold uppercase text-slate-800">Official Instructions:</div>
              <p>1. Use Blue or Black ballpoint/marker only. Do not use ink pen or pencil.</p>
              <p>2. Fill the circle completely and darkly. Incomplete, faint, or cut bubbles will be marked incorrect.</p>
              <p>3. Do not fold or tear this response sheet. Any stray marks on this sheet will cancel marks.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};
