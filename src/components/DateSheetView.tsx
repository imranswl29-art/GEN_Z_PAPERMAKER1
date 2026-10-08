import React, { useState, useEffect, useRef } from 'react';
import { DateSheetData, DateSheetRow } from '../types/extraDocs';
import { UserAccount } from '../types/user';
import { PaperHeaderInfo } from '../types/paper';
import { getSchoolBranding } from '../utils/branding';
import { SchoolMonogram } from './SchoolMonogram';
import { exportDateSheetToWord } from '../utils/exportExtraDocsWord';
import { exportElementToPdf } from '../utils/exportPdf';
import {
  fetchDateSheetsFromFirestore,
  saveDateSheetToFirestore,
} from '../firebase';
import {
  Calendar,
  Printer,
  Download,
  Plus,
  Trash2,
  Building2,
  CheckCircle,
  Clock,
  ArrowUp,
  ArrowDown,
  RotateCcw,
  Sparkles,
  FileDown,
  Edit3,
  Eye,
  Sliders,
  ShieldCheck,
  ChevronRight,
  Loader2,
} from 'lucide-react';

interface DateSheetViewProps {
  currentUser: UserAccount | null;
  activeHeader?: PaperHeaderInfo;
  onOpenSchoolProfile: () => void;
}

const DEFAULT_INSTRUCTIONS = [
  'Students must report to the examination hall at least 15 minutes before the scheduled time.',
  'Original Roll Number Slip and institutional ID card are strictly mandatory for entrance.',
  'Mobile phones, programmable calculators, smart watches, and unauthorized material are strictly prohibited.',
  'Students must bring their own stationery (blue/black markers, pens, rulers, compasses).',
  'Any candidate found using unfair means or talking during examination will be penalized as per Board Rules.',
  'Answer sheets with mutilated roll number bubbles or torn corners will be disqualified.',
];

const PRESET_9TH_SUBJECTS = [
  { subject: 'English (Compulsory)', syllabus: 'Full Book (Objective & Subjective)' },
  { subject: 'Biology / Computer Science', syllabus: 'Full Book - Chapters 1 to 9 (Theory)' },
  { subject: 'Chemistry', syllabus: 'Full Book - Chapters 1 to 8' },
  { subject: 'Mathematics (Science)', syllabus: 'Full Book - Units 1 to 17' },
  { subject: 'Physics', syllabus: 'Full Book - Units 1 to 9' },
  { subject: 'Islamiat (Compulsory)', syllabus: 'Full Book & Quranic Verses' },
  { subject: 'Tarjuma-tul-Quran-ul-Majeed', syllabus: 'Complete Prescribed Surahs' },
  { subject: 'Urdu (Compulsory)', syllabus: 'Full Book (Nazam, Ghazal & Sabaq)' },
  { subject: 'Pakistan Studies', syllabus: 'Full Book - Chapters 1 to 4' },
];

const PRESET_10TH_SUBJECTS = [
  { subject: 'English (Compulsory)', syllabus: 'Full Book (Lessons 1-13, Essays & Grammar)' },
  { subject: 'Physics', syllabus: 'Full Book - Units 10 to 18' },
  { subject: 'Chemistry', syllabus: 'Full Book - Units 9 to 16' },
  { subject: 'Mathematics (Science)', syllabus: 'Full Book - Units 1 to 13' },
  { subject: 'Biology / Computer Science', syllabus: 'Full Book - Theory & Practical Guidelines' },
  { subject: 'Islamiat (Compulsory)', syllabus: 'Full Book & Surah Ahzab' },
  { subject: 'Tarjuma-tul-Quran-ul-Majeed', syllabus: 'Prescribed Surahs & translation' },
  { subject: 'Pakistan Studies', syllabus: 'Full Book - Chapters 5 to 8' },
  { subject: 'Urdu (Compulsory)', syllabus: 'Full Book (Hissa Nasr, Nazam & Mazameen)' },
];

export const DateSheetView: React.FC<DateSheetViewProps> = ({
  currentUser,
  activeHeader,
  onOpenSchoolProfile,
}) => {
  const branding = getSchoolBranding(currentUser, activeHeader);
  const [activeSubTab, setActiveSubTab] = useState<'editor' | 'preview'>('editor');
  const [isExportingPdf, setIsExportingPdf] = useState(false);
  const [pdfStatusText, setPdfStatusText] = useState('');
  const [toastMsg, setToastMsg] = useState<string | null>(null);

  const showToast = (msg: string) => {
    setToastMsg(msg);
    setTimeout(() => setToastMsg(null), 3000);
  };

  // Helper to compute day from date string YYYY-MM-DD
  const getDayFromDate = (dateStr: string): string => {
    if (!dateStr) return '';
    try {
      const parts = dateStr.split('-');
      if (parts.length === 3) {
        const d = new Date(parseInt(parts[0]), parseInt(parts[1]) - 1, parseInt(parts[2]));
        return d.toLocaleDateString('en-US', { weekday: 'long' });
      }
    } catch {}
    return '';
  };

  // State
  const [dateSheet, setDateSheet] = useState<DateSheetData>(() => {
    const saved = localStorage.getItem('ptbb_active_datesheet');
    if (saved) {
      try {
        return JSON.parse(saved);
      } catch (e) {}
    }
    // Default initial date sheet
    const today = new Date();
    today.setDate(today.getDate() + 7);
    const startDateStr = today.toISOString().split('T')[0];

    const initialRows: DateSheetRow[] = PRESET_9TH_SUBJECTS.map((sub, idx) => {
      const rowDate = new Date(today);
      rowDate.setDate(today.getDate() + idx * 2); // Every 2 days
      const dStr = rowDate.toISOString().split('T')[0];
      return {
        id: `row-${idx + 1}-${Date.now()}`,
        date: dStr,
        day: rowDate.toLocaleDateString('en-US', { weekday: 'long' }),
        subject: sub.subject,
        paperType: sub.syllabus,
        timings: '08:30 AM - 11:30 AM',
      };
    });

    return {
      id: `ds-${Date.now()}`,
      examType: 'Annual Examination',
      customExamTitle: '',
      classLevel: '9th Class (Matric Part-I)',
      session: '2025-2026',
      examTimings: '08:30 AM - 11:30 AM',
      startDate: startDateStr,
      shift: 'Morning Shift',
      instructions: DEFAULT_INSTRUCTIONS,
      rows: initialRows,
    };
  });

  const isInitialLoadedRef = useRef(false);

  // Fetch DateSheet from permanent database on mount/user change
  useEffect(() => {
    fetchDateSheetsFromFirestore(currentUser?.id)
      .then((cloudSheets) => {
        if (Array.isArray(cloudSheets) && cloudSheets.length > 0) {
          setDateSheet(cloudSheets[0]);
          localStorage.setItem('ptbb_active_datesheet', JSON.stringify(cloudSheets[0]));
        }
      })
      .catch(() => {
        // Fallback to Express backend if offline
        fetch(`/api/datesheets${currentUser?.id ? `?userId=${encodeURIComponent(currentUser.id)}` : ''}`)
          .then((res) => res.json())
          .then((data) => {
            if (Array.isArray(data) && data.length > 0) {
              setDateSheet(data[0]);
              localStorage.setItem('ptbb_active_datesheet', JSON.stringify(data[0]));
            }
          })
          .catch(() => {});
      })
      .finally(() => {
        isInitialLoadedRef.current = true;
      });
  }, [currentUser?.id]);

  // Permanent database auto-persist to Firestore and backend API
  useEffect(() => {
    if (!isInitialLoadedRef.current) return;
    localStorage.setItem('ptbb_active_datesheet', JSON.stringify(dateSheet));
    const sheetWithUser = {
      ...dateSheet,
      userId: currentUser?.id || 'guest',
      updatedAt: new Date().toISOString(),
    };
    saveDateSheetToFirestore(sheetWithUser).catch((e) =>
      console.warn('Firestore datesheet sync:', e)
    );
    fetch('/api/datesheets', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(sheetWithUser),
    }).catch(() => {});
  }, [dateSheet, currentUser?.id]);

  const examDisplayTitle = dateSheet.customExamTitle.trim() || dateSheet.examType;

  // Handlers
  const handleUpdateField = <K extends keyof DateSheetData>(key: K, val: DateSheetData[K]) => {
    setDateSheet((prev) => ({ ...prev, [key]: val }));
  };

  const handleUpdateRow = (rowId: string, field: keyof DateSheetRow, val: string) => {
    setDateSheet((prev) => {
      const updatedRows = prev.rows.map((r) => {
        if (r.id === rowId) {
          const updated = { ...r, [field]: val };
          if (field === 'date') {
            updated.day = getDayFromDate(val) || updated.day;
          }
          return updated;
        }
        return r;
      });
      return { ...prev, rows: updatedRows };
    });
  };

  const handleAddRow = () => {
    const lastRow = dateSheet.rows[dateSheet.rows.length - 1];
    let nextDateStr = '';
    let nextDayStr = '';

    if (lastRow?.date) {
      try {
        const parts = lastRow.date.split('-');
        const nextD = new Date(parseInt(parts[0]), parseInt(parts[1]) - 1, parseInt(parts[2]));
        nextD.setDate(nextD.getDate() + 2);
        nextDateStr = nextD.toISOString().split('T')[0];
        nextDayStr = nextD.toLocaleDateString('en-US', { weekday: 'long' });
      } catch {}
    }

    const newRow: DateSheetRow = {
      id: `row-${Date.now()}`,
      date: nextDateStr,
      day: nextDayStr || 'Monday',
      subject: 'New Subject',
      paperType: 'Full Book (Objective & Subjective)',
      timings: dateSheet.examTimings,
    };

    setDateSheet((prev) => ({
      ...prev,
      rows: [...prev.rows, newRow],
    }));
    showToast('Added custom row to Date Sheet');
  };

  const handleRemoveRow = (id: string) => {
    setDateSheet((prev) => ({
      ...prev,
      rows: prev.rows.filter((r) => r.id !== id),
    }));
  };

  const handleMoveRow = (index: number, direction: 'up' | 'down') => {
    if (
      (direction === 'up' && index === 0) ||
      (direction === 'down' && index === dateSheet.rows.length - 1)
    )
      return;
    const targetIdx = direction === 'up' ? index - 1 : index + 1;
    const newRows = [...dateSheet.rows];
    const temp = newRows[index];
    newRows[index] = newRows[targetIdx];
    newRows[targetIdx] = temp;
    setDateSheet((prev) => ({ ...prev, rows: newRows }));
  };

  const handleLoadPreset = (preset: '9th' | '10th') => {
    const subjects = preset === '9th' ? PRESET_9TH_SUBJECTS : PRESET_10TH_SUBJECTS;
    const today = new Date();
    today.setDate(today.getDate() + 7);

    const newRows: DateSheetRow[] = subjects.map((sub, idx) => {
      const rowDate = new Date(today);
      rowDate.setDate(today.getDate() + idx * 2);
      const dStr = rowDate.toISOString().split('T')[0];
      return {
        id: `row-${preset}-${idx + 1}-${Date.now()}`,
        date: dStr,
        day: rowDate.toLocaleDateString('en-US', { weekday: 'long' }),
        subject: sub.subject,
        paperType: sub.syllabus,
        timings: dateSheet.examTimings,
      };
    });

    setDateSheet((prev) => ({
      ...prev,
      classLevel: preset === '9th' ? '9th Class (Matric Part-I)' : '10th Class (Matric Part-II)',
      rows: newRows,
    }));
    showToast(`Loaded ${preset} Class standard schedule!`);
  };

  const handlePrint = () => {
    const prevTitle = document.title;
    const cleanClass = dateSheet.classLevel.replace(/\s+/g, '_');
    const cleanExam = examDisplayTitle.replace(/\s+/g, '_');
    document.title = `${cleanClass}_Date_Sheet_${cleanExam}`;
    window.print();
    setTimeout(() => {
      document.title = prevTitle;
    }, 1500);
  };

  const handleDownloadPdf = async () => {
    setActiveSubTab('preview');
    setIsExportingPdf(true);
    setPdfStatusText('Preparing Date Sheet PDF...');
    // Allow DOM to update preview visibility
    await new Promise((r) => setTimeout(r, 250));

    const cleanClass = dateSheet.classLevel.replace(/\s+/g, '_');
    const cleanExam = examDisplayTitle.replace(/\s+/g, '_');
    const fileName = `${cleanClass}_Date_Sheet_${cleanExam}.pdf`;

    try {
      const ok = await exportElementToPdf('datesheet-print-container', fileName, (msg) => {
        setPdfStatusText(msg);
      });
      if (ok) {
        showToast('Date Sheet PDF downloaded successfully!');
      }
    } finally {
      setIsExportingPdf(false);
    }
  };

  const handleDownloadWord = () => {
    exportDateSheetToWord(dateSheet, branding);
    showToast('Date Sheet MS Word document downloaded!');
  };

  return (
    <div className="space-y-6 max-w-7xl mx-auto font-sans text-slate-800">
      {/* Toast Alert */}
      {toastMsg && (
        <div className="fixed top-16 right-6 z-50 bg-slate-900 text-white px-4 py-2.5 rounded-xl shadow-2xl text-xs font-bold flex items-center gap-2 animate-in fade-in slide-in-from-top-2 no-print">
          <CheckCircle className="w-4 h-4 text-emerald-400" />
          <span>{toastMsg}</span>
        </div>
      )}

      {/* Top Header Card */}
      <div className="card-3d p-5 sm:p-6 bg-white border border-slate-200">
        <div className="flex flex-col lg:flex-row items-start lg:items-center justify-between gap-4">
          <div className="flex items-center gap-3.5">
            <div className="w-12 h-12 rounded-2xl bg-gradient-to-tr from-blue-700 to-indigo-600 flex items-center justify-center text-white shadow-md shrink-0">
              <Calendar className="w-6 h-6 text-white" />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <span className="text-[10px] font-black uppercase tracking-wider px-2 py-0.5 rounded bg-blue-100 text-blue-900">
                  Item #8 &bull; Official Document
                </span>
                <span className="text-[11px] font-bold text-slate-500">A4 Printable Format</span>
              </div>
              <h1 className="text-xl sm:text-2xl font-black text-slate-950 tracking-tight mt-0.5">
                Date Sheet Generator
              </h1>
              <p className="text-xs text-slate-600 font-medium">
                Design, customize, edit, and print official school examination date sheets with auto-fetched school monogram & branding
              </p>
            </div>
          </div>

          {/* Quick Tab Switcher */}
          <div className="flex items-center gap-1.5 p-1.5 bg-slate-100 rounded-2xl border-2 border-slate-200 w-full lg:w-auto justify-end">
            <button
              onClick={() => setActiveSubTab('editor')}
              className={`px-4 py-2 rounded-xl text-xs font-black transition-all cursor-pointer flex items-center gap-1.5 ${
                activeSubTab === 'editor'
                  ? 'btn-3d btn-3d-blue text-white shadow-md'
                  : 'bg-white border-2 border-slate-300 text-slate-800 hover:bg-slate-50 hover:border-slate-400 font-extrabold shadow-2xs'
              }`}
            >
              <Edit3 className="w-3.5 h-3.5 text-blue-600" />
              <span>Interactive Editor</span>
            </button>
            <button
              onClick={() => setActiveSubTab('preview')}
              className={`px-4 py-2 rounded-xl text-xs font-black transition-all cursor-pointer flex items-center gap-1.5 ${
                activeSubTab === 'preview'
                  ? 'btn-3d btn-3d-emerald text-white shadow-md'
                  : 'bg-white border-2 border-slate-300 text-slate-800 hover:bg-slate-50 hover:border-slate-400 font-extrabold shadow-2xs'
              }`}
            >
              <Eye className="w-3.5 h-3.5 text-emerald-600" />
              <span>Printable A4 Preview</span>
            </button>
          </div>
        </div>

        {/* Global Action Bar with Vivid Multi-Color Buttons */}
        <div className="mt-5 pt-4 border-t border-slate-200 flex flex-wrap items-center justify-between gap-3">
          <div className="flex items-center gap-2">
            <button
              type="button"
              onClick={onOpenSchoolProfile}
              className="btn-3d btn-3d-amber flex items-center gap-1.5 px-3.5 py-2 rounded-xl text-xs font-black cursor-pointer shadow-sm"
              title="Edit School Name, Monogram Logo, Address and Phone"
            >
              <Building2 className="w-4 h-4 text-slate-950" />
              <span>Edit School Branding</span>
            </button>

            <span className="text-xs text-slate-500 font-medium hidden sm:inline">
              Linked School: <strong className="text-slate-800">{branding.schoolName}</strong>
            </span>
          </div>

          {/* Color-Coded Actions */}
          <div className="flex flex-wrap items-center gap-2">
            {/* Standardized "Print & Preview" Button Fix (12px 24px) */}
            <button
              type="button"
              onClick={handlePrint}
              className="btn-print-preview"
              title="Open browser print dialog for A4 Date Sheet"
            >
              <Printer className="w-4 h-4 text-emerald-100" />
              <span>Print & Preview</span>
            </button>

            {/* High-Visibility Crimson / Red PDF Export Button */}
            <button
              type="button"
              onClick={handleDownloadPdf}
              disabled={isExportingPdf}
              className="btn-3d btn-3d-red flex items-center gap-2 px-4 py-2.5 text-white rounded-xl text-xs font-black cursor-pointer shadow-md disabled:opacity-50"
              title="Download high-resolution PDF"
            >
              {isExportingPdf ? (
                <Loader2 className="w-4 h-4 animate-spin" />
              ) : (
                <FileDown className="w-4 h-4" />
              )}
              <span>{isExportingPdf ? (pdfStatusText || 'Rendering PDF...') : 'Download PDF'}</span>
            </button>

            {/* Deep Navy / Cobalt MS Word (.docx) Export Button */}
            <button
              type="button"
              onClick={handleDownloadWord}
              className="btn-3d btn-3d-navy flex items-center gap-2 px-4 py-2.5 text-white rounded-xl text-xs font-black cursor-pointer shadow-md"
              title="Download editable Microsoft Word .doc file"
            >
              <Download className="w-4 h-4 text-blue-200" />
              <span>Download Word (.doc)</span>
            </button>
          </div>
        </div>
      </div>

      {/* VIEW SUB-TAB: INTERACTIVE EDITOR */}
      {activeSubTab === 'editor' && (
        <div className="space-y-6">
          {/* Controls & Configuration Card */}
          <div className="card-3d p-5 bg-white border border-slate-200 space-y-4">
            <div className="flex items-center justify-between border-b border-slate-200 pb-3">
              <div className="flex items-center gap-2 text-slate-900 font-black text-sm">
                <Sliders className="w-4 h-4 text-blue-600" />
                <span>Date Sheet Parameters & Exam Details</span>
              </div>
              <div className="flex items-center gap-2">
                <button
                  type="button"
                  onClick={() => handleLoadPreset('9th')}
                  className="btn-3d btn-3d-blue text-[11px] font-black px-3 py-1.5 rounded-lg text-white cursor-pointer"
                >
                  Load 9th Science Preset
                </button>
                <button
                  type="button"
                  onClick={() => handleLoadPreset('10th')}
                  className="btn-3d btn-3d-indigo text-[11px] font-black px-3 py-1.5 rounded-lg text-white cursor-pointer"
                >
                  Load 10th Science Preset
                </button>
              </div>
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 text-xs">
              {/* Exam Type Preset */}
              <div>
                <label className="block font-bold text-slate-700 mb-1">Exam Type / Category:</label>
                <select
                  value={dateSheet.examType}
                  onChange={(e) => handleUpdateField('examType', e.target.value)}
                  className="w-full px-3 py-2 rounded-xl border border-slate-300 font-semibold focus:outline-none focus:ring-2 focus:ring-blue-500"
                >
                  <option value="Annual Examination">Annual Examination</option>
                  <option value="1st Term Examination">1st Term Examination</option>
                  <option value="2nd Term Examination">2nd Term Examination</option>
                  <option value="Mid-Term Examination">Mid-Term Examination</option>
                  <option value="December Test Session">December Test Session</option>
                  <option value="Send-Up Examination">Send-Up Examination</option>
                  <option value="Pre-Board Examination">Pre-Board Examination</option>
                  <option value="Weekly Test Series">Weekly Test Series</option>
                  <option value="Monthly Assessment">Monthly Assessment</option>
                  <option value="Custom Title">Custom Title...</option>
                </select>
              </div>

              {/* Custom Exam Title */}
              <div>
                <label className="block font-bold text-slate-700 mb-1">
                  Custom Exam Title (Optional):
                </label>
                <input
                  type="text"
                  placeholder="e.g. Grand Test Series 2026"
                  value={dateSheet.customExamTitle}
                  onChange={(e) => handleUpdateField('customExamTitle', e.target.value)}
                  className="w-full px-3 py-2 rounded-xl border border-slate-300 font-semibold focus:outline-none focus:ring-2 focus:ring-blue-500"
                />
              </div>

              {/* Class / Grade */}
              <div>
                <label className="block font-bold text-slate-700 mb-1">Class / Grade & Section:</label>
                <input
                  type="text"
                  value={dateSheet.classLevel}
                  onChange={(e) => handleUpdateField('classLevel', e.target.value)}
                  placeholder="e.g. 9th Class (Science Group)"
                  className="w-full px-3 py-2 rounded-xl border border-slate-300 font-bold focus:outline-none focus:ring-2 focus:ring-blue-500"
                />
              </div>

              {/* Academic Session */}
              <div>
                <label className="block font-bold text-slate-700 mb-1">Academic Session:</label>
                <input
                  type="text"
                  value={dateSheet.session}
                  onChange={(e) => handleUpdateField('session', e.target.value)}
                  placeholder="e.g. 2025-2026"
                  className="w-full px-3 py-2 rounded-xl border border-slate-300 font-bold focus:outline-none focus:ring-2 focus:ring-blue-500"
                />
              </div>

              {/* Exam Timings */}
              <div>
                <label className="block font-bold text-slate-700 mb-1">General Exam Timings:</label>
                <div className="relative">
                  <Clock className="w-3.5 h-3.5 text-slate-400 absolute left-3 top-3" />
                  <input
                    type="text"
                    value={dateSheet.examTimings}
                    onChange={(e) => handleUpdateField('examTimings', e.target.value)}
                    placeholder="e.g. 08:30 AM - 11:30 AM"
                    className="w-full pl-8 pr-3 py-2 rounded-xl border border-slate-300 font-bold focus:outline-none focus:ring-2 focus:ring-blue-500"
                  />
                </div>
              </div>

              {/* Shift */}
              <div>
                <label className="block font-bold text-slate-700 mb-1">Exam Shift:</label>
                <select
                  value={dateSheet.shift}
                  onChange={(e) => handleUpdateField('shift', e.target.value)}
                  className="w-full px-3 py-2 rounded-xl border border-slate-300 font-semibold focus:outline-none focus:ring-2 focus:ring-blue-500"
                >
                  <option value="Morning Shift">Morning Shift</option>
                  <option value="Evening Shift">Evening Shift</option>
                  <option value="Double Shift (Both)">Double Shift (Both)</option>
                </select>
              </div>

              {/* Start Date */}
              <div>
                <label className="block font-bold text-slate-700 mb-1">Start Date Picker:</label>
                <input
                  type="date"
                  value={dateSheet.startDate}
                  onChange={(e) => handleUpdateField('startDate', e.target.value)}
                  className="w-full px-3 py-2 rounded-xl border border-slate-300 font-semibold focus:outline-none focus:ring-2 focus:ring-blue-500"
                />
              </div>

              {/* Quick Summary */}
              <div className="bg-slate-50 border border-slate-200 rounded-xl p-2.5 flex flex-col justify-center">
                <span className="text-[10px] font-bold uppercase text-slate-500">Summary:</span>
                <span className="font-extrabold text-slate-900 truncate">
                  {examDisplayTitle} &bull; {dateSheet.rows.length} Papers
                </span>
                <span className="text-[11px] text-blue-700 font-bold">{dateSheet.classLevel}</span>
              </div>
            </div>
          </div>

          {/* Dynamic & 100% Editable Date Sheet Table Card */}
          <div className="card-3d p-5 bg-white border border-slate-200 space-y-4">
            <div className="flex flex-wrap items-center justify-between gap-3 border-b border-slate-200 pb-3">
              <div>
                <h3 className="font-black text-sm text-slate-950">Dynamic Schedule Table</h3>
                <p className="text-xs text-slate-600">
                  Every cell is 100% editable inline. Changes automatically sync to preview and exports.
                </p>
              </div>

              {/* Add Custom Row Button (Vibrant Amber / Orange #D97706) */}
              <button
                type="button"
                onClick={handleAddRow}
                className="btn-3d btn-3d-amber flex items-center gap-1.5 px-3.5 py-2 text-slate-950 rounded-xl text-xs font-black cursor-pointer shadow-md"
              >
                <Plus className="w-4 h-4 text-slate-950" />
                <span>Add Custom Row</span>
              </button>
            </div>

            <div className="overflow-x-auto">
              <table className="w-full text-xs text-left border-collapse border border-slate-200">
                <thead>
                  <tr className="bg-slate-900 text-white font-extrabold uppercase text-[11px]">
                    <th className="p-2.5 text-center w-12 border border-slate-800">#</th>
                    <th className="p-2.5 w-36 border border-slate-800">Date</th>
                    <th className="p-2.5 w-28 border border-slate-800">Day</th>
                    <th className="p-2.5 w-52 border border-slate-800">Subject</th>
                    <th className="p-2.5 border border-slate-800">Paper Type / Syllabus Details</th>
                    <th className="p-2.5 w-36 border border-slate-800">Timings</th>
                    <th className="p-2.5 text-center w-28 border border-slate-800">Actions</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-slate-200">
                  {dateSheet.rows.map((row, idx) => (
                    <tr
                      key={row.id}
                      className={`hover:bg-blue-50/50 transition-colors ${
                        idx % 2 === 0 ? 'bg-white' : 'bg-slate-50'
                      }`}
                    >
                      {/* Sr */}
                      <td className="p-2 text-center font-bold text-slate-700 border border-slate-200">
                        {idx + 1}
                      </td>

                      {/* Date */}
                      <td className="p-1.5 border border-slate-200">
                        <input
                          type="date"
                          value={row.date}
                          onChange={(e) => handleUpdateRow(row.id, 'date', e.target.value)}
                          className="w-full px-2 py-1 rounded-lg border border-slate-300 font-bold text-xs"
                        />
                      </td>

                      {/* Day */}
                      <td className="p-1.5 border border-slate-200">
                        <input
                          type="text"
                          value={row.day}
                          onChange={(e) => handleUpdateRow(row.id, 'day', e.target.value)}
                          placeholder="Monday"
                          className="w-full px-2 py-1 rounded-lg border border-slate-300 font-extrabold text-blue-900 text-xs"
                        />
                      </td>

                      {/* Subject */}
                      <td className="p-1.5 border border-slate-200">
                        <input
                          type="text"
                          value={row.subject}
                          onChange={(e) => handleUpdateRow(row.id, 'subject', e.target.value)}
                          placeholder="Subject Name"
                          className="w-full px-2 py-1 rounded-lg border border-slate-300 font-black text-slate-900 text-xs"
                        />
                      </td>

                      {/* Paper Type / Syllabus */}
                      <td className="p-1.5 border border-slate-200">
                        <input
                          type="text"
                          value={row.paperType}
                          onChange={(e) => handleUpdateRow(row.id, 'paperType', e.target.value)}
                          placeholder="e.g. Full Book (Objective & Subjective)"
                          className="w-full px-2 py-1 rounded-lg border border-slate-300 font-medium text-slate-700 text-xs"
                        />
                      </td>

                      {/* Timings */}
                      <td className="p-1.5 border border-slate-200">
                        <input
                          type="text"
                          value={row.timings || dateSheet.examTimings}
                          onChange={(e) => handleUpdateRow(row.id, 'timings', e.target.value)}
                          placeholder="08:30 AM - 11:30 AM"
                          className="w-full px-2 py-1 rounded-lg border border-slate-300 font-semibold text-slate-800 text-xs"
                        />
                      </td>

                      {/* Actions */}
                      <td className="p-1.5 text-center border border-slate-200">
                        <div className="flex items-center justify-center gap-1">
                          <button
                            type="button"
                            disabled={idx === 0}
                            onClick={() => handleMoveRow(idx, 'up')}
                            className="p-1 rounded text-slate-500 hover:text-blue-700 hover:bg-slate-200 disabled:opacity-30 cursor-pointer"
                            title="Move Up"
                          >
                            <ArrowUp className="w-3.5 h-3.5" />
                          </button>
                          <button
                            type="button"
                            disabled={idx === dateSheet.rows.length - 1}
                            onClick={() => handleMoveRow(idx, 'down')}
                            className="p-1 rounded text-slate-500 hover:text-blue-700 hover:bg-slate-200 disabled:opacity-30 cursor-pointer"
                            title="Move Down"
                          >
                            <ArrowDown className="w-3.5 h-3.5" />
                          </button>
                          <button
                            type="button"
                            onClick={() => handleRemoveRow(row.id)}
                            className="p-1 rounded text-rose-600 hover:bg-rose-100 cursor-pointer"
                            title="Remove Row"
                          >
                            <Trash2 className="w-3.5 h-3.5" />
                          </button>
                        </div>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>

          {/* General Examination Rules & Guidelines Card */}
          <div className="card-3d p-5 bg-white border border-slate-200 space-y-3">
            <div className="flex items-center justify-between border-b border-slate-200 pb-2.5">
              <div className="flex items-center gap-2 font-black text-sm text-slate-900">
                <ShieldCheck className="w-4 h-4 text-emerald-600" />
                <span>General Examination Rules & Student Instructions</span>
              </div>
              <button
                type="button"
                onClick={() =>
                  setDateSheet((prev) => ({
                    ...prev,
                    instructions: [
                      ...prev.instructions,
                      'Students must maintain complete silence in the examination center.',
                    ],
                  }))
                }
                className="text-xs font-bold text-blue-700 hover:text-blue-900 cursor-pointer flex items-center gap-1"
              >
                <Plus className="w-3.5 h-3.5" />
                <span>Add Instruction</span>
              </button>
            </div>

            <div className="space-y-2">
              {dateSheet.instructions.map((ins, idx) => (
                <div key={idx} className="flex items-center gap-2">
                  <span className="w-5 text-right font-extrabold text-slate-600 text-xs">
                    {idx + 1}.
                  </span>
                  <input
                    type="text"
                    value={ins}
                    onChange={(e) => {
                      const updated = [...dateSheet.instructions];
                      updated[idx] = e.target.value;
                      setDateSheet((prev) => ({ ...prev, instructions: updated }));
                    }}
                    className="flex-1 px-3 py-1.5 rounded-lg border border-slate-300 text-xs font-medium text-slate-800 focus:outline-none focus:ring-1 focus:ring-blue-500"
                  />
                  <button
                    type="button"
                    onClick={() => {
                      const updated = dateSheet.instructions.filter((_, i) => i !== idx);
                      setDateSheet((prev) => ({ ...prev, instructions: updated }));
                    }}
                    className="p-1.5 text-rose-600 hover:bg-rose-50 rounded cursor-pointer"
                    title="Delete instruction"
                  >
                    <Trash2 className="w-3.5 h-3.5" />
                  </button>
                </div>
              ))}
            </div>
          </div>
        </div>
      )}

      {/* VIEW SUB-TAB: PRINTABLE A4 PREVIEW (Auto-Adjusting Header Context & Clean Geometry) */}
      <div
        className={`${
          activeSubTab === 'preview' ? 'block' : 'hidden print:block'
        } bg-white rounded-2xl shadow-xl border border-slate-300 p-6 sm:p-10 max-w-4xl mx-auto print:border-none print:shadow-none print:p-0 print:m-0 print:max-w-none print:w-full`}
        id="datesheet-print-container"
      >
        {/* ======================= OFFICIAL A4 HEADER ======================= */}
        <div className="paper-header border-b-2 border-slate-900 pb-4 mb-4 text-center">
          <div className="header-row flex items-center justify-between gap-4">
            {/* Left Monogram */}
            <div className="school-monogram-container shrink-0">
              <SchoolMonogram
                logoUrl={branding.logoUrl}
                schoolName={branding.schoolName}
                size={75}
              />
            </div>

            {/* Center School Details */}
            <div className="school-name-col flex-1 min-w-0 px-2 text-center">
              <h1 className="school-name-title text-xl sm:text-2xl font-black uppercase text-slate-950 tracking-tight leading-tight">
                {branding.schoolName}
              </h1>
              <div className="text-xs sm:text-sm font-bold text-slate-700 tracking-wide mt-0.5">
                {branding.campusName} &bull; {branding.address}
              </div>
              <div className="text-[11px] text-slate-600 font-semibold mt-0.5">
                Phone: {branding.phone} &bull; Affiliated: {branding.boardPattern || 'BISE Punjab'}
              </div>
            </div>

            {/* Right Official Shift & Verification Badge (Replaces Duplicate Monogram) */}
            <div className="shrink-0 hidden sm:flex flex-col items-center justify-center p-2 rounded-xl bg-slate-50 border border-slate-300 w-24 text-center">
              <span className="text-[9px] uppercase font-black text-blue-900 tracking-wider">Exam Shift</span>
              <span className="text-[11px] font-extrabold text-slate-900 mt-0.5">{dateSheet.shift.split(' ')[0]}</span>
              <span className="text-[9px] font-bold text-emerald-700 mt-0.5">Verified</span>
            </div>
          </div>

          {/* Official Banner */}
          <div className="mt-3.5 bg-blue-900 text-white font-black py-1.5 px-4 rounded text-xs sm:text-sm uppercase tracking-wider shadow-xs">
            Official Examination Date Sheet &bull; Session {dateSheet.session}
          </div>

          {/* Sub Header Statement */}
          <div className="mt-2 text-xs font-black text-slate-900 uppercase">
            {examDisplayTitle} &bull; {dateSheet.classLevel}
          </div>

          {/* Metadata Row */}
          <div className="mt-2 pt-2 border-t border-slate-300 grid grid-cols-3 text-[11px] font-bold text-slate-800">
            <div className="text-left">
              Shift: <span className="text-blue-900 font-black">{dateSheet.shift}</span>
            </div>
            <div className="text-center">
              Timings: <span className="text-blue-900 font-black">{dateSheet.examTimings}</span>
            </div>
            <div className="text-right">
              Issue Date:{' '}
              <span className="text-blue-900 font-black">
                {new Date().toLocaleDateString('en-GB')}
              </span>
            </div>
          </div>
        </div>

        {/* ======================= DATE SHEET TABLE ======================= */}
        <div className="overflow-visible mb-6">
          <table className="w-full text-xs border-collapse border border-slate-900">
            <thead>
              <tr className="bg-slate-900 text-white font-extrabold uppercase text-[11px]">
                <th className="p-2 border border-slate-900 text-center w-10">Sr#</th>
                <th className="p-2 border border-slate-900 text-left w-28">Date</th>
                <th className="p-2 border border-slate-900 text-left w-24">Day</th>
                <th className="p-2 border border-slate-900 text-left w-48">Subject</th>
                <th className="p-2 border border-slate-900 text-left">Syllabus / Paper Details</th>
                <th className="p-2 border border-slate-900 text-center w-32">Timings</th>
              </tr>
            </thead>
            <tbody>
              {dateSheet.rows.map((r, idx) => (
                <tr
                  key={r.id}
                  className={`border border-slate-900 ${
                    idx % 2 === 0 ? 'bg-white' : 'bg-slate-50'
                  }`}
                >
                  <td className="p-2 border border-slate-900 text-center font-bold text-slate-950">
                    {idx + 1}
                  </td>
                  <td className="p-2 border border-slate-900 font-bold text-slate-950">
                    {r.date || 'TBD'}
                  </td>
                  <td className="p-2 border border-slate-900 font-extrabold text-blue-950">
                    {r.day}
                  </td>
                  <td className="p-2 border border-slate-900 font-black text-slate-950">
                    {r.subject}
                  </td>
                  <td className="p-2 border border-slate-900 font-medium text-slate-800">
                    {r.paperType}
                  </td>
                  <td className="p-2 border border-slate-900 text-center font-bold text-slate-950">
                    {r.timings || dateSheet.examTimings}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>

        {/* ======================= GENERAL INSTRUCTIONS BOX ======================= */}
        <div className="border border-slate-800 bg-slate-50 p-3.5 rounded-lg mb-8">
          <div className="font-black text-xs text-blue-950 uppercase tracking-wide border-b border-slate-300 pb-1 mb-2">
            Important Guidelines & Rules for Candidates:
          </div>
          <ol className="list-decimal list-inside space-y-1 text-[11px] font-semibold text-slate-800 leading-relaxed">
            {dateSheet.instructions.map((ins, i) => (
              <li key={i}>{ins}</li>
            ))}
          </ol>
        </div>

        {/* ======================= OFFICIAL SIGNATURES ======================= */}
        <div className="pt-6 border-t border-slate-400 grid grid-cols-3 text-center text-xs font-bold text-slate-900">
          <div>
            <div className="w-36 border-t-2 border-slate-800 mx-auto pt-1 font-black">
              Class Incharge
            </div>
            <div className="text-[10px] text-slate-600">Verification Signature</div>
          </div>
          <div>
            <div className="w-40 border-t-2 border-slate-800 mx-auto pt-1 font-black">
              Controller Examinations
            </div>
            <div className="text-[10px] text-slate-600">Administrative Seal</div>
          </div>
          <div>
            <div className="w-36 border-t-2 border-slate-800 mx-auto pt-1 font-black">
              Principal / Headmaster
            </div>
            <div className="text-[10px] text-slate-600">Official Stamp</div>
          </div>
        </div>

        <div className="text-center text-[10px] text-slate-500 font-mono mt-8 border-t border-slate-200 pt-2">
          Generated via PTBB BISE Punjab Examination Portal &bull; System Verified Document
        </div>
      </div>
    </div>
  );
};
