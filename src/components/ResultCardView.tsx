import React, { useState, useEffect, useRef } from 'react';
import {
  MarksheetData,
  StudentMarksRecord,
  SubjectConfig,
} from '../types/extraDocs';
import { UserAccount } from '../types/user';
import { PaperHeaderInfo } from '../types/paper';
import { getSchoolBranding } from '../utils/branding';
import { SchoolMonogram } from './SchoolMonogram';
import {
  exportSingleResultCardToWord,
  exportMasterSheetToWord,
} from '../utils/exportExtraDocsWord';
import { exportElementToPdf } from '../utils/exportPdf';
import {
  fetchMarksheetsFromFirestore,
  saveMarksheetToFirestore,
} from '../firebase';
import {
  Award,
  Printer,
  Download,
  Plus,
  Trash2,
  Building2,
  CheckCircle,
  FileDown,
  Edit3,
  Eye,
  Sliders,
  User,
  Upload,
  Image as ImageIcon,
  ChevronRight,
  BookOpen,
  Check,
  AlertTriangle,
  ArrowLeft,
  X,
  Sparkles,
  Users,
  FileSpreadsheet,
  FileText,
  Loader2,
} from 'lucide-react';

interface ResultCardViewProps {
  currentUser: UserAccount | null;
  activeHeader?: PaperHeaderInfo;
  onOpenSchoolProfile: () => void;
}

const DEFAULT_SUBJECTS_9TH: SubjectConfig[] = [
  { id: 'sub-1', name: 'English', totalMarks: 75, passingMarks: 25 },
  { id: 'sub-2', name: 'Urdu', totalMarks: 75, passingMarks: 25 },
  { id: 'sub-3', name: 'Islamiat', totalMarks: 50, passingMarks: 17 },
  { id: 'sub-4', name: 'Pak Studies', totalMarks: 50, passingMarks: 17 },
  { id: 'sub-5', name: 'Mathematics', totalMarks: 75, passingMarks: 25 },
  { id: 'sub-6', name: 'Physics', totalMarks: 60, passingMarks: 20 },
  { id: 'sub-7', name: 'Chemistry', totalMarks: 60, passingMarks: 20 },
  { id: 'sub-8', name: 'Biology / CS', totalMarks: 60, passingMarks: 20 },
  { id: 'sub-9', name: 'Tarjuma Quran', totalMarks: 50, passingMarks: 17 },
];

const INITIAL_SAMPLE_STUDENTS: StudentMarksRecord[] = [
  {
    id: 'st-1',
    rollNo: '101',
    name: 'Muhammad Ali',
    fatherName: 'Tariq Mehmood',
    attendance: '98%',
    rank: '1st',
    remarks: 'Outstanding analytical skills and exemplary conduct. Keep it up!',
    marks: {
      'sub-1': 68,
      'sub-2': 70,
      'sub-3': 46,
      'sub-4': 45,
      'sub-5': 72,
      'sub-6': 56,
      'sub-7': 55,
      'sub-8': 58,
      'sub-9': 48,
    },
  },
  {
    id: 'st-2',
    rollNo: '102',
    name: 'Fatima Zahra',
    fatherName: 'Rashid Khan',
    attendance: '96%',
    rank: '2nd',
    remarks: 'Consistent academic excellence and brilliant presentation.',
    marks: {
      'sub-1': 65,
      'sub-2': 68,
      'sub-3': 44,
      'sub-4': 43,
      'sub-5': 69,
      'sub-6': 54,
      'sub-7': 52,
      'sub-8': 55,
      'sub-9': 47,
    },
  },
  {
    id: 'st-3',
    rollNo: '103',
    name: 'Ahmad Hassan',
    fatherName: 'Muhammad Saeed',
    attendance: '94%',
    rank: '3rd',
    remarks: 'Very hardworking and dedicated student. Great achievement!',
    marks: {
      'sub-1': 60,
      'sub-2': 63,
      'sub-3': 41,
      'sub-4': 40,
      'sub-5': 65,
      'sub-6': 50,
      'sub-7': 48,
      'sub-8': 51,
      'sub-9': 44,
    },
  },
  {
    id: 'st-4',
    rollNo: '104',
    name: 'Ayesha Noor',
    fatherName: 'Abdul Rehman',
    attendance: '91%',
    rank: '4th',
    remarks: 'Good progress; needs slight focus on Mathematics calculations.',
    marks: {
      'sub-1': 58,
      'sub-2': 61,
      'sub-3': 39,
      'sub-4': 38,
      'sub-5': 55,
      'sub-6': 46,
      'sub-7': 45,
      'sub-8': 48,
      'sub-9': 42,
    },
  },
];

export const ResultCardView: React.FC<ResultCardViewProps> = ({
  currentUser,
  activeHeader,
  onOpenSchoolProfile,
}) => {
  const branding = getSchoolBranding(currentUser, activeHeader);
  const [activeTabMode, setActiveTabMode] = useState<'editor' | 'singleCard' | 'masterSheet'>('editor');
  const [selectedStudentId, setSelectedStudentId] = useState<string>('st-1');
  const [isExportingPdf, setIsExportingPdf] = useState(false);
  const [pdfStatusText, setPdfStatusText] = useState('');
  const [toastMsg, setToastMsg] = useState<string | null>(null);

  // Hidden file input for student photo
  const studentPhotoInputRef = useRef<HTMLInputElement>(null);
  const [targetPhotoStudentId, setTargetPhotoStudentId] = useState<string | null>(null);

  const showToast = (msg: string) => {
    setToastMsg(msg);
    setTimeout(() => setToastMsg(null), 3000);
  };

  // Marksheet Data State
  const [marksheet, setMarksheet] = useState<MarksheetData>(() => {
    const saved = localStorage.getItem('ptbb_marksheet_data');
    if (saved) {
      try {
        return JSON.parse(saved);
      } catch (e) {}
    }
    return {
      id: `ms-${Date.now()}`,
      classLevel: '9th Class (Science Group)',
      session: '2025-2026',
      examCategory: 'Annual Examination',
      subjects: DEFAULT_SUBJECTS_9TH,
      students: INITIAL_SAMPLE_STUDENTS,
    };
  });

  const isInitialLoadedRef = useRef(false);

  // Fetch Marksheet data from permanent database on mount/user change
  useEffect(() => {
    fetchMarksheetsFromFirestore(currentUser?.id)
      .then((cloudMarksheets) => {
        if (Array.isArray(cloudMarksheets) && cloudMarksheets.length > 0) {
          setMarksheet(cloudMarksheets[0]);
          localStorage.setItem('ptbb_marksheet_data', JSON.stringify(cloudMarksheets[0]));
        }
      })
      .catch(() => {
        // Fallback to Express backend if offline
        fetch(`/api/marksheets${currentUser?.id ? `?userId=${encodeURIComponent(currentUser.id)}` : ''}`)
          .then((res) => res.json())
          .then((data) => {
            if (Array.isArray(data) && data.length > 0) {
              setMarksheet(data[0]);
              localStorage.setItem('ptbb_marksheet_data', JSON.stringify(data[0]));
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
    localStorage.setItem('ptbb_marksheet_data', JSON.stringify(marksheet));
    const marksheetWithUser = {
      ...marksheet,
      userId: currentUser?.id || 'guest',
      updatedAt: new Date().toISOString(),
    };
    saveMarksheetToFirestore(marksheetWithUser).catch((e) =>
      console.warn('Firestore marksheet sync:', e)
    );
    fetch('/api/marksheets', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(marksheetWithUser),
    }).catch(() => {});
  }, [marksheet, currentUser?.id]);

  // Derived grand totals
  const totalMaxMarks = marksheet.subjects.reduce((sum, s) => sum + s.totalMarks, 0);

  // Helper for computing student stats
  const computeStudentStats = (st: StudentMarksRecord) => {
    const obt = marksheet.subjects.reduce((sum, s) => sum + (st.marks[s.id] ?? 0), 0);
    const pct = totalMaxMarks > 0 ? (obt / totalMaxMarks) * 100 : 0;

    let grade = 'F';
    if (pct >= 90) grade = 'A+';
    else if (pct >= 80) grade = 'A';
    else if (pct >= 70) grade = 'B';
    else if (pct >= 60) grade = 'C';
    else if (pct >= 50) grade = 'D';
    else if (pct >= 40) grade = 'E';

    // Status: Check if failed any subject
    const hasFailedAny = marksheet.subjects.some((s) => (st.marks[s.id] ?? 0) < s.passingMarks);
    const status: 'PASS' | 'FAIL' = hasFailedAny ? 'FAIL' : 'PASS';

    return {
      totalObtained: obt,
      percentage: parseFloat(pct.toFixed(1)),
      grade: st.grade || grade,
      status: st.status || status,
    };
  };

  const selectedStudent =
    marksheet.students.find((s) => s.id === selectedStudentId) || marksheet.students[0];

  // Subject Management
  const handleAddSubject = () => {
    const newSub: SubjectConfig = {
      id: `sub-${Date.now()}`,
      name: 'New Subject',
      totalMarks: 75,
      passingMarks: 25,
    };
    setMarksheet((prev) => ({
      ...prev,
      subjects: [...prev.subjects, newSub],
    }));
    showToast('New subject added to curriculum');
  };

  const handleUpdateSubject = (id: string, field: keyof SubjectConfig, val: any) => {
    setMarksheet((prev) => ({
      ...prev,
      subjects: prev.subjects.map((s) => (s.id === id ? { ...s, [field]: val } : s)),
    }));
  };

  const handleRemoveSubject = (id: string) => {
    if (marksheet.subjects.length <= 1) {
      alert('At least one subject is required.');
      return;
    }
    setMarksheet((prev) => ({
      ...prev,
      subjects: prev.subjects.filter((s) => s.id !== id),
    }));
  };

  // Student Management
  const handleAddStudent = () => {
    const nextRoll = (marksheet.students.length + 101).toString();
    const newSt: StudentMarksRecord = {
      id: `st-${Date.now()}`,
      rollNo: nextRoll,
      name: `Student ${marksheet.students.length + 1}`,
      fatherName: 'Father Name',
      attendance: '95%',
      rank: '',
      remarks: 'Satisfactory performance; keep studying hard.',
      marks: {},
    };
    setMarksheet((prev) => ({
      ...prev,
      students: [...prev.students, newSt],
    }));
    setSelectedStudentId(newSt.id);
    showToast(`Added student Roll# ${nextRoll}`);
  };

  const handleUpdateStudent = (id: string, field: keyof StudentMarksRecord, val: any) => {
    setMarksheet((prev) => ({
      ...prev,
      students: prev.students.map((st) => (st.id === id ? { ...st, [field]: val } : st)),
    }));
  };

  const handleUpdateStudentMark = (studentId: string, subjectId: string, markVal: number) => {
    setMarksheet((prev) => ({
      ...prev,
      students: prev.students.map((st) => {
        if (st.id === studentId) {
          const updatedMarks = { ...st.marks, [subjectId]: markVal };
          return { ...st, marks: updatedMarks };
        }
        return st;
      }),
    }));
  };

  const handleRemoveStudent = (id: string) => {
    if (marksheet.students.length <= 1) {
      alert('At least one student record is required.');
      return;
    }
    setMarksheet((prev) => ({
      ...prev,
      students: prev.students.filter((st) => st.id !== id),
    }));
    if (selectedStudentId === id) {
      const remaining = marksheet.students.filter((st) => st.id !== id);
      if (remaining[0]) setSelectedStudentId(remaining[0].id);
    }
  };

  // Photo Upload Handler
  const handleTriggerPhotoUpload = (studentId: string) => {
    setTargetPhotoStudentId(studentId);
    studentPhotoInputRef.current?.click();
  };

  const handlePhotoFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file && targetPhotoStudentId) {
      const reader = new FileReader();
      reader.onload = () => {
        if (typeof reader.result === 'string') {
          handleUpdateStudent(targetPhotoStudentId, 'photoUrl', reader.result);
          showToast('Student photo uploaded successfully!');
        }
      };
      reader.readAsDataURL(file);
    }
    // Reset file input
    if (studentPhotoInputRef.current) studentPhotoInputRef.current.value = '';
  };

  const handleRemovePhoto = (studentId: string) => {
    handleUpdateStudent(studentId, 'photoUrl', undefined);
    showToast('Student photo removed');
  };

  // Printing & Exports
  const handlePrintSingle = (student: StudentMarksRecord) => {
    const prevTitle = document.title;
    document.title = `Result_Card_Roll_${student.rollNo}_${student.name.replace(/\s+/g, '_')}`;
    window.print();
    setTimeout(() => {
      document.title = prevTitle;
    }, 1500);
  };

  const handleDownloadSinglePdf = async (student: StudentMarksRecord) => {
    setSelectedStudentId(student.id);
    setActiveTabMode('singleCard');
    setIsExportingPdf(true);
    setPdfStatusText(`Generating Roll ${student.rollNo} Result Card PDF...`);
    // Settle layout
    await new Promise((r) => setTimeout(r, 250));
    const fileName = `Result_Card_Roll_${student.rollNo}_${student.name.replace(/\s+/g, '_')}.pdf`;
    try {
      const ok = await exportElementToPdf('resultcard-print-container', fileName, (msg) => {
        setPdfStatusText(msg);
      });
      if (ok) showToast('Result Card PDF downloaded successfully!');
    } finally {
      setIsExportingPdf(false);
    }
  };

  const handleDownloadSingleWord = (student: StudentMarksRecord) => {
    exportSingleResultCardToWord(student, marksheet, branding);
    showToast('Result Card MS Word document downloaded!');
  };

  const handlePrintMasterSheet = () => {
    setActiveTabMode('masterSheet');
    const prevTitle = document.title;
    document.title = `Master_Marksheet_${marksheet.classLevel.replace(/\s+/g, '_')}`;
    window.print();
    setTimeout(() => {
      document.title = prevTitle;
    }, 1500);
  };

  const handleDownloadMasterSheetPdf = async () => {
    setActiveTabMode('masterSheet');
    setIsExportingPdf(true);
    setPdfStatusText('Generating Master Marksheet PDF...');
    // Settle layout
    await new Promise((r) => setTimeout(r, 250));
    const fileName = `Master_Marksheet_${marksheet.classLevel.replace(/\s+/g, '_')}.pdf`;
    try {
      const ok = await exportElementToPdf('mastersheet-print-container', fileName, (msg) => {
        setPdfStatusText(msg);
      });
      if (ok) showToast('Master Marksheet PDF downloaded successfully!');
    } finally {
      setIsExportingPdf(false);
    }
  };

  const handleDownloadMasterSheetWord = () => {
    exportMasterSheetToWord(marksheet, branding);
    showToast('Master Marksheet Word document downloaded!');
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

      {/* Hidden File Input for Student Photo */}
      <input
        ref={studentPhotoInputRef}
        type="file"
        accept="image/*"
        className="hidden"
        onChange={handlePhotoFileChange}
      />

      {/* Top Header Card */}
      <div className="card-3d p-5 sm:p-6 bg-white border border-slate-200">
        <div className="flex flex-col lg:flex-row items-start lg:items-center justify-between gap-4">
          <div className="flex items-center gap-3.5">
            <div className="w-12 h-12 rounded-2xl bg-gradient-to-tr from-amber-600 to-indigo-700 flex items-center justify-center text-white shadow-md shrink-0">
              <Award className="w-6 h-6 text-white" />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <span className="text-[10px] font-black uppercase tracking-wider px-2 py-0.5 rounded bg-amber-100 text-amber-950">
                  Item #9 &bull; Academic Evaluation
                </span>
                <span className="text-[11px] font-bold text-slate-500">
                  A4 Single Card &amp; Master Gazette
                </span>
              </div>
              <h1 className="text-xl sm:text-2xl font-black text-slate-950 tracking-tight mt-0.5">
                Result Card &amp; Marksheet Generator
              </h1>
              <p className="text-xs text-slate-600 font-medium">
                Manage dynamic marks entry, student photos, auto-calculations, and generate high-precision A4 result cards and consolidated master sheets
              </p>
            </div>
          </div>

          {/* Sub-Tab Navigation Bar */}
          <div className="flex flex-wrap items-center gap-1.5 p-1.5 bg-slate-100 rounded-2xl border-2 border-slate-200 w-full lg:w-auto justify-end">
            <button
              onClick={() => setActiveTabMode('editor')}
              className={`px-3.5 py-2 rounded-xl text-xs font-black transition-all cursor-pointer flex items-center gap-1.5 ${
                activeTabMode === 'editor'
                  ? 'btn-3d btn-3d-blue text-white shadow-md'
                  : 'bg-white border-2 border-slate-300 text-slate-800 hover:bg-slate-50 hover:border-slate-400 font-extrabold shadow-2xs'
              }`}
            >
              <Edit3 className="w-3.5 h-3.5 text-blue-600" />
              <span>Marks Entry Table</span>
            </button>

            <button
              onClick={() => setActiveTabMode('singleCard')}
              className={`px-3.5 py-2 rounded-xl text-xs font-black transition-all cursor-pointer flex items-center gap-1.5 ${
                activeTabMode === 'singleCard'
                  ? 'btn-3d btn-3d-emerald text-white shadow-md'
                  : 'bg-white border-2 border-slate-300 text-slate-800 hover:bg-slate-50 hover:border-slate-400 font-extrabold shadow-2xs'
              }`}
            >
              <FileText className="w-3.5 h-3.5 text-emerald-600" />
              <span>Single A4 Result Card</span>
            </button>

            <button
              onClick={() => setActiveTabMode('masterSheet')}
              className={`px-3.5 py-2 rounded-xl text-xs font-black transition-all cursor-pointer flex items-center gap-1.5 ${
                activeTabMode === 'masterSheet'
                  ? 'btn-3d btn-3d-indigo text-white shadow-md'
                  : 'bg-white border-2 border-slate-300 text-slate-800 hover:bg-slate-50 hover:border-slate-400 font-extrabold shadow-2xs'
              }`}
            >
              <FileSpreadsheet className="w-3.5 h-3.5 text-indigo-600" />
              <span>Class Master Sheet</span>
            </button>
          </div>
        </div>

        {/* Action Header Bar */}
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

          {/* Quick Exports depending on current view mode */}
          <div className="flex flex-wrap items-center gap-2">
            {activeTabMode === 'singleCard' && selectedStudent && (
              <>
                <button
                  type="button"
                  onClick={() => handlePrintSingle(selectedStudent)}
                  className="btn-print-preview"
                  title="Print single student result card on standard A4"
                >
                  <Printer className="w-4 h-4 text-emerald-100" />
                  <span>Print & Preview</span>
                </button>
                <button
                  type="button"
                  onClick={() => handleDownloadSinglePdf(selectedStudent)}
                  disabled={isExportingPdf}
                  className="btn-3d btn-3d-red flex items-center gap-2 px-4 py-2.5 text-white rounded-xl text-xs font-black cursor-pointer shadow-md disabled:opacity-50"
                  title="Download single student result card PDF"
                >
                  {isExportingPdf ? (
                    <Loader2 className="w-4 h-4 animate-spin" />
                  ) : (
                    <FileDown className="w-4 h-4" />
                  )}
                  <span>{isExportingPdf ? (pdfStatusText || 'Rendering...') : 'Download Card (PDF)'}</span>
                </button>
                <button
                  type="button"
                  onClick={() => handleDownloadSingleWord(selectedStudent)}
                  className="btn-3d btn-3d-navy flex items-center gap-2 px-4 py-2.5 text-white rounded-xl text-xs font-black cursor-pointer shadow-md"
                  title="Download single student result card Word (.doc)"
                >
                  <Download className="w-4 h-4 text-blue-200" />
                  <span>Download Card (.doc)</span>
                </button>
              </>
            )}

            {activeTabMode === 'masterSheet' && (
              <>
                <button
                  type="button"
                  onClick={handlePrintMasterSheet}
                  className="btn-print-preview"
                  title="Print full class master sheet / broadsheet"
                >
                  <Printer className="w-4 h-4 text-emerald-100" />
                  <span>Print & Preview</span>
                </button>
                <button
                  type="button"
                  onClick={handleDownloadMasterSheetPdf}
                  disabled={isExportingPdf}
                  className="btn-3d btn-3d-red flex items-center gap-2 px-4 py-2.5 text-white rounded-xl text-xs font-black cursor-pointer shadow-md disabled:opacity-50"
                >
                  {isExportingPdf ? (
                    <Loader2 className="w-4 h-4 animate-spin" />
                  ) : (
                    <FileDown className="w-4 h-4" />
                  )}
                  <span>{isExportingPdf ? (pdfStatusText || 'Rendering...') : 'Export Master (PDF)'}</span>
                </button>
                <button
                  type="button"
                  onClick={handleDownloadMasterSheetWord}
                  className="btn-3d btn-3d-navy flex items-center gap-2 px-4 py-2.5 text-white rounded-xl text-xs font-black cursor-pointer shadow-md"
                >
                  <Download className="w-4 h-4 text-blue-200" />
                  <span>Export Master (.doc)</span>
                </button>
              </>
            )}
          </div>
        </div>
      </div>

      {/* ========================================================================= */}
      {/* MODE 1: INTERACTIVE MARKS ENTRY & CURRICULUM SETUP                         */}
      {/* ========================================================================= */}
      {activeTabMode === 'editor' && (
        <div className="space-y-6">
          {/* Header Configuration Card */}
          <div className="card-3d p-5 bg-white border border-slate-200 space-y-4">
            <div className="flex items-center justify-between border-b border-slate-200 pb-3">
              <div className="flex items-center gap-2 font-black text-sm text-slate-900">
                <Sliders className="w-4 h-4 text-blue-600" />
                <span>Class, Exam &amp; Session Configuration</span>
              </div>
              <div className="text-xs font-bold text-slate-500">
                Total Exam Marks: <strong className="text-blue-900 text-sm font-black">{totalMaxMarks}</strong>
              </div>
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 text-xs">
              <div>
                <label className="block font-bold text-slate-700 mb-1">Class / Grade Input:</label>
                <input
                  type="text"
                  value={marksheet.classLevel}
                  onChange={(e) => setMarksheet({ ...marksheet, classLevel: e.target.value })}
                  placeholder="e.g. 10th Class (Science Group)"
                  className="w-full px-3 py-2 rounded-xl border border-slate-300 font-bold focus:outline-none focus:ring-2 focus:ring-blue-500"
                />
              </div>

              <div>
                <label className="block font-bold text-slate-700 mb-1">Academic Session:</label>
                <input
                  type="text"
                  value={marksheet.session}
                  onChange={(e) => setMarksheet({ ...marksheet, session: e.target.value })}
                  placeholder="e.g. 2025-2026"
                  className="w-full px-3 py-2 rounded-xl border border-slate-300 font-bold focus:outline-none focus:ring-2 focus:ring-blue-500"
                />
              </div>

              <div>
                <label className="block font-bold text-slate-700 mb-1">Exam Category / Title:</label>
                <input
                  type="text"
                  value={marksheet.examCategory}
                  onChange={(e) => setMarksheet({ ...marksheet, examCategory: e.target.value })}
                  placeholder="e.g. Annual Examination"
                  className="w-full px-3 py-2 rounded-xl border border-slate-300 font-bold focus:outline-none focus:ring-2 focus:ring-blue-500"
                />
              </div>

              <div className="bg-slate-50 border border-slate-200 rounded-xl p-2.5 flex flex-col justify-center">
                <span className="text-[10px] font-bold uppercase text-slate-500">Curriculum Overview:</span>
                <span className="font-extrabold text-slate-900">
                  {marksheet.subjects.length} Subjects &bull; {marksheet.students.length} Students
                </span>
                <span className="text-[11px] text-emerald-700 font-bold">Auto-Rank &amp; Pass/Fail Active</span>
              </div>
            </div>
          </div>

          {/* Dynamic Subject Curriculum Manager */}
          <div className="card-3d p-5 bg-white border border-slate-200 space-y-4">
            <div className="flex flex-wrap items-center justify-between gap-3 border-b border-slate-200 pb-3">
              <div>
                <h3 className="font-black text-sm text-slate-950">Subject Curriculum &amp; Total Marks</h3>
                <p className="text-xs text-slate-600">
                  Add, rename or remove subjects for any class. Total exam marks calculate automatically.
                </p>
              </div>

              {/* Add Custom Subject Button (Vibrant Amber / Orange #D97706) */}
              <button
                type="button"
                onClick={handleAddSubject}
                className="btn-3d btn-3d-amber flex items-center gap-1.5 px-3.5 py-2 text-slate-950 rounded-xl text-xs font-black cursor-pointer shadow-md"
              >
                <Plus className="w-4 h-4 text-slate-950" />
                <span>Add Custom Subject</span>
              </button>
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-3 text-xs">
              {marksheet.subjects.map((sub, idx) => (
                <div
                  key={sub.id}
                  className="p-3 bg-slate-50 border border-slate-200 rounded-xl space-y-2 hover:border-blue-400 transition-colors"
                >
                  <div className="flex items-center justify-between">
                    <span className="font-bold text-slate-500 text-[10px] uppercase">
                      Sub #{idx + 1}
                    </span>
                    <button
                      type="button"
                      onClick={() => handleRemoveSubject(sub.id)}
                      className="text-rose-600 hover:text-rose-800 p-0.5 cursor-pointer"
                      title="Remove Subject"
                    >
                      <Trash2 className="w-3.5 h-3.5" />
                    </button>
                  </div>

                  <input
                    type="text"
                    value={sub.name}
                    onChange={(e) => handleUpdateSubject(sub.id, 'name', e.target.value)}
                    placeholder="Subject Name"
                    className="w-full px-2.5 py-1.5 rounded-lg border border-slate-300 font-extrabold text-slate-900 text-xs"
                  />

                  <div className="grid grid-cols-2 gap-2 text-[11px]">
                    <div>
                      <label className="text-slate-500 font-bold">Total Marks:</label>
                      <input
                        type="number"
                        min="1"
                        value={sub.totalMarks}
                        onChange={(e) =>
                          handleUpdateSubject(sub.id, 'totalMarks', parseInt(e.target.value) || 0)
                        }
                        className="w-full px-2 py-1 rounded border border-slate-300 font-black text-blue-900"
                      />
                    </div>
                    <div>
                      <label className="text-slate-500 font-bold">Passing:</label>
                      <input
                        type="number"
                        min="0"
                        value={sub.passingMarks}
                        onChange={(e) =>
                          handleUpdateSubject(sub.id, 'passingMarks', parseInt(e.target.value) || 0)
                        }
                        className="w-full px-2 py-1 rounded border border-slate-300 font-bold text-slate-700"
                      />
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* Dynamic Student Marks Entry Table Card */}
          <div className="card-3d p-5 bg-white border border-slate-200 space-y-4">
            <div className="flex flex-wrap items-center justify-between gap-3 border-b border-slate-200 pb-3">
              <div>
                <h3 className="font-black text-sm text-slate-950">Student Marks Entry Sheet</h3>
                <p className="text-xs text-slate-600">
                  Enter student credentials, upload photos (optional), and input subject marks. Total, % and Grade compute live with manual override support.
                </p>
              </div>

              {/* Add Student Button (Vivid Deep Blue #1E40AF) */}
              <button
                type="button"
                onClick={handleAddStudent}
                className="btn-3d btn-3d-blue flex items-center gap-1.5 px-3.5 py-2 text-white rounded-xl text-xs font-black cursor-pointer shadow-md"
              >
                <Plus className="w-4 h-4" />
                <span>Add New Student</span>
              </button>
            </div>

            <div className="overflow-x-auto">
              <table className="w-full text-xs text-left border-collapse border border-slate-200 min-w-[900px]">
                <thead>
                  <tr className="bg-slate-900 text-white font-extrabold uppercase text-[11px]">
                    <th className="p-2 text-center w-14 border border-slate-800">Roll#</th>
                    <th className="p-2 w-14 text-center border border-slate-800">Photo</th>
                    <th className="p-2 w-44 border border-slate-800">Student Name</th>
                    <th className="p-2 w-36 border border-slate-800">Father's Name</th>
                    {marksheet.subjects.map((sub) => (
                      <th
                        key={sub.id}
                        className="p-2 text-center border border-slate-800 max-w-[90px]"
                        title={`${sub.name} (Max: ${sub.totalMarks})`}
                      >
                        <div className="truncate">{sub.name}</div>
                        <div className="text-[9px] text-blue-300 font-normal">/{sub.totalMarks}</div>
                      </th>
                    ))}
                    <th className="p-2 text-center w-20 border border-slate-800">Obt. Marks</th>
                    <th className="p-2 text-center w-16 border border-slate-800">%</th>
                    <th className="p-2 text-center w-14 border border-slate-800">Grade</th>
                    <th className="p-2 text-center w-16 border border-slate-800">Status</th>
                    <th className="p-2 text-center w-28 border border-slate-800">Actions</th>
                  </tr>
                </thead>
                <tbody className="divide-y divide-slate-200">
                  {marksheet.students.map((st, sIdx) => {
                    const stats = computeStudentStats(st);
                    return (
                      <tr
                        key={st.id}
                        className={`hover:bg-blue-50/50 transition-colors ${
                          sIdx % 2 === 0 ? 'bg-white' : 'bg-slate-50'
                        }`}
                      >
                        {/* Roll No */}
                        <td className="p-1.5 text-center border border-slate-200">
                          <input
                            type="text"
                            value={st.rollNo}
                            onChange={(e) => handleUpdateStudent(st.id, 'rollNo', e.target.value)}
                            className="w-12 text-center px-1 py-1 rounded font-black text-blue-900 border border-slate-300 text-xs"
                          />
                        </td>

                        {/* Optional Student Photo */}
                        <td className="p-1.5 text-center border border-slate-200">
                          <div className="flex items-center justify-center">
                            {st.photoUrl ? (
                              <div className="relative group">
                                <img
                                  src={st.photoUrl}
                                  alt="Student"
                                  className="w-8 h-8 rounded-full object-cover border border-slate-300 shadow-2xs"
                                />
                                <button
                                  type="button"
                                  onClick={() => handleRemovePhoto(st.id)}
                                  className="absolute -top-1 -right-1 w-4 h-4 bg-rose-600 text-white rounded-full flex items-center justify-center text-[10px] opacity-0 group-hover:opacity-100 transition-opacity cursor-pointer"
                                  title="Remove Photo"
                                >
                                  &times;
                                </button>
                              </div>
                            ) : (
                              <button
                                type="button"
                                onClick={() => handleTriggerPhotoUpload(st.id)}
                                className="w-8 h-8 rounded-full bg-slate-200 hover:bg-blue-100 text-slate-500 hover:text-blue-700 flex items-center justify-center transition-colors cursor-pointer"
                                title="Upload Student Photo (Optional)"
                              >
                                <Upload className="w-3.5 h-3.5" />
                              </button>
                            )}
                          </div>
                        </td>

                        {/* Name */}
                        <td className="p-1.5 border border-slate-200">
                          <input
                            type="text"
                            value={st.name}
                            onChange={(e) => handleUpdateStudent(st.id, 'name', e.target.value)}
                            placeholder="Student Name"
                            className="w-full px-2 py-1 rounded font-black text-slate-900 border border-slate-300 text-xs"
                          />
                        </td>

                        {/* Father Name */}
                        <td className="p-1.5 border border-slate-200">
                          <input
                            type="text"
                            value={st.fatherName}
                            onChange={(e) => handleUpdateStudent(st.id, 'fatherName', e.target.value)}
                            placeholder="Father's Name"
                            className="w-full px-2 py-1 rounded font-medium text-slate-700 border border-slate-300 text-xs"
                          />
                        </td>

                        {/* Subject Marks */}
                        {marksheet.subjects.map((sub) => {
                          const obtVal = st.marks[sub.id] ?? '';
                          const numObt = Number(obtVal);
                          const isFail = numObt > 0 && numObt < sub.passingMarks;
                          return (
                            <td key={sub.id} className="p-1.5 text-center border border-slate-200">
                              <input
                                type="number"
                                min="0"
                                max={sub.totalMarks}
                                value={obtVal}
                                onChange={(e) =>
                                  handleUpdateStudentMark(
                                    st.id,
                                    sub.id,
                                    e.target.value === '' ? 0 : parseInt(e.target.value) || 0
                                  )
                                }
                                className={`w-14 text-center px-1 py-1 rounded font-black text-xs border ${
                                  isFail
                                    ? 'border-rose-400 bg-rose-50 text-rose-700'
                                    : 'border-slate-300 text-slate-900'
                                }`}
                              />
                            </td>
                          );
                        })}

                        {/* Total Obtained */}
                        <td className="p-1.5 text-center font-black text-blue-950 border border-slate-200 text-xs">
                          {stats.totalObtained}
                        </td>

                        {/* Percentage */}
                        <td className="p-1.5 text-center font-bold text-slate-800 border border-slate-200 text-xs">
                          {stats.percentage}%
                        </td>

                        {/* Grade */}
                        <td className="p-1.5 text-center font-black text-blue-900 border border-slate-200 text-xs">
                          {stats.grade}
                        </td>

                        {/* Status */}
                        <td className="p-1.5 text-center border border-slate-200 text-xs font-black">
                          <span
                            className={`px-1.5 py-0.5 rounded text-[10px] ${
                              stats.status === 'PASS'
                                ? 'bg-emerald-100 text-emerald-800'
                                : 'bg-rose-100 text-rose-800'
                            }`}
                          >
                            {stats.status}
                          </span>
                        </td>

                        {/* Actions */}
                        <td className="p-1.5 text-center border border-slate-200">
                          <div className="flex items-center justify-center gap-1.5">
                            <button
                              type="button"
                              onClick={() => {
                                setSelectedStudentId(st.id);
                                setActiveTabMode('singleCard');
                              }}
                              className="px-2 py-1 bg-emerald-600 hover:bg-emerald-700 text-white rounded text-[10px] font-black cursor-pointer shadow-2xs"
                              title="View Single Student A4 Result Card"
                            >
                              View Card
                            </button>
                            <button
                              type="button"
                              onClick={() => handleRemoveStudent(st.id)}
                              className="p-1 text-rose-600 hover:bg-rose-100 rounded cursor-pointer"
                              title="Delete Student"
                            >
                              <Trash2 className="w-3.5 h-3.5" />
                            </button>
                          </div>
                        </td>
                      </tr>
                    );
                  })}
                </tbody>
              </table>
            </div>
          </div>
        </div>
      )}

      {/* ========================================================================= */}
      {/* MODE 2: SINGLE STUDENT A4 RESULT CARD PREVIEW & PRINT                      */}
      {/* ========================================================================= */}
      {activeTabMode === 'singleCard' && selectedStudent && (
        <div className="space-y-4">
          {/* Student Selector Toolbar */}
          <div className="card-3d p-4 bg-white border border-slate-200 flex flex-wrap items-center justify-between gap-3 no-print">
            <div className="flex items-center gap-2">
              <span className="text-xs font-bold text-slate-700">Select Student:</span>
              <select
                value={selectedStudentId}
                onChange={(e) => setSelectedStudentId(e.target.value)}
                className="px-3 py-1.5 rounded-xl border border-slate-300 font-bold text-xs focus:ring-2 focus:ring-blue-500"
              >
                {marksheet.students.map((st) => (
                  <option key={st.id} value={st.id}>
                    Roll #{st.rollNo} - {st.name}
                  </option>
                ))}
              </select>
            </div>

            <div className="flex items-center gap-2">
              <button
                type="button"
                onClick={() => handleTriggerPhotoUpload(selectedStudent.id)}
                className="btn-3d btn-3d-slate flex items-center gap-1.5 px-3 py-1.5 text-white rounded-xl text-xs font-bold cursor-pointer"
              >
                <ImageIcon className="w-3.5 h-3.5 text-blue-300" />
                <span>{selectedStudent.photoUrl ? 'Change Student Photo' : 'Upload Student Photo (Optional)'}</span>
              </button>
              {selectedStudent.photoUrl && (
                <button
                  type="button"
                  onClick={() => handleRemovePhoto(selectedStudent.id)}
                  className="px-2.5 py-1.5 bg-rose-100 text-rose-800 hover:bg-rose-200 rounded-xl text-xs font-bold cursor-pointer"
                >
                  Remove Photo
                </button>
              )}
            </div>
          </div>

          {/* PRINTABLE A4 SINGLE RESULT CARD */}
          <div
            id="resultcard-print-container"
            className="bg-white rounded-2xl shadow-xl border border-slate-300 p-6 sm:p-10 max-w-4xl mx-auto print:border-none print:shadow-none print:p-0 print:m-0 print:max-w-none print:w-full"
          >
            {/* Header with Unified Branding & Monogram */}
            <div className="paper-header border-b-2 border-slate-900 pb-3 mb-4 text-center">
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
                    Phone: {branding.phone} &bull; Affiliated with: {branding.boardPattern || 'BISE Punjab'}
                  </div>
                </div>

                {/* Right Verification Seal (Replaces duplicate monogram) */}
                <div className="shrink-0 hidden sm:flex flex-col items-center justify-center p-2 rounded-xl bg-slate-50 border border-slate-300 w-24 text-center">
                  <span className="text-[9px] uppercase font-black text-blue-900 tracking-wider">Report Card</span>
                  <span className="text-[11px] font-extrabold text-slate-900 mt-0.5">{marksheet.session}</span>
                  <span className="text-[9px] font-bold text-emerald-700 mt-0.5">Official</span>
                </div>
              </div>

              {/* Title Banner */}
              <div className="mt-3.5 bg-blue-900 text-white font-black py-1.5 px-4 rounded text-xs sm:text-sm uppercase tracking-wider shadow-xs">
                Progress Report Card / Annual Result Sheet &bull; Session {marksheet.session}
              </div>

              <div className="mt-2 text-xs font-black text-slate-900 uppercase">
                Examination: {marksheet.examCategory} &bull; Class: {marksheet.classLevel}
              </div>
            </div>

            {/* Student Credentials Box with Optional Photo */}
            <div className="border border-slate-900 bg-slate-50 p-3.5 rounded-lg mb-5 flex flex-col sm:flex-row items-center gap-4">
              {/* Photo Container: Crisp 3:4 aspect ratio with high-contrast fallback icon */}
              <div className="shrink-0 w-24 h-32 rounded-lg border-2 border-slate-700 bg-white p-1 overflow-hidden shadow-xs flex flex-col items-center justify-center">
                {selectedStudent.photoUrl ? (
                  <img
                    src={selectedStudent.photoUrl}
                    alt={selectedStudent.name}
                    className="w-full h-full object-cover rounded"
                    style={{ imageRendering: '-webkit-optimize-contrast' }}
                  />
                ) : (
                  <div className="flex flex-col items-center justify-center p-2 text-center w-full h-full bg-slate-50 rounded">
                    <div className="w-12 h-12 rounded-full bg-blue-100 flex items-center justify-center border border-blue-300 mb-1">
                      <User className="w-6 h-6 text-blue-700" />
                    </div>
                    <span className="text-[9px] font-black uppercase text-slate-800 tracking-wider">Candidate</span>
                    <span className="text-[8px] text-slate-500 font-semibold">(Photo ID)</span>
                  </div>
                )}
              </div>

              {/* Credentials Grid */}
              <div className="flex-1 w-full grid grid-cols-2 sm:grid-cols-3 gap-2.5 text-xs">
                <div>
                  <span className="text-[10px] font-bold uppercase text-slate-500 block">
                    Roll Number:
                  </span>
                  <span className="text-sm font-black text-blue-950">
                    {selectedStudent.rollNo}
                  </span>
                </div>

                <div>
                  <span className="text-[10px] font-bold uppercase text-slate-500 block">
                    Student Name:
                  </span>
                  <span className="text-xs font-black text-slate-950">
                    {selectedStudent.name}
                  </span>
                </div>

                <div>
                  <span className="text-[10px] font-bold uppercase text-slate-500 block">
                    Father's Name:
                  </span>
                  <span className="text-xs font-bold text-slate-800">
                    {selectedStudent.fatherName || '-'}
                  </span>
                </div>

                <div>
                  <span className="text-[10px] font-bold uppercase text-slate-500 block">
                    Class &amp; Section:
                  </span>
                  <span className="text-xs font-bold text-slate-800">
                    {marksheet.classLevel}
                  </span>
                </div>

                <div>
                  <span className="text-[10px] font-bold uppercase text-slate-500 block">
                    Attendance:
                  </span>
                  <span className="text-xs font-bold text-slate-800">
                    {selectedStudent.attendance || '95%'}
                  </span>
                </div>

                <div>
                  <span className="text-[10px] font-bold uppercase text-slate-500 block">
                    Class Position / Rank:
                  </span>
                  <span className="text-xs font-black text-emerald-800">
                    {selectedStudent.rank || 'Good'}
                  </span>
                </div>
              </div>
            </div>

            {/* Subject Breakdown Table */}
            <div className="overflow-visible mb-5">
              <table className="w-full text-xs border-collapse border border-slate-900">
                <thead>
                  <tr className="bg-slate-900 text-white font-extrabold uppercase text-[11px]">
                    <th className="p-2 border border-slate-900 text-center w-10">Sr#</th>
                    <th className="p-2 border border-slate-900 text-left">Subject Name</th>
                    <th className="p-2 border border-slate-900 text-center w-24">Total Marks</th>
                    <th className="p-2 border border-slate-900 text-center w-24">Pass Marks</th>
                    <th className="p-2 border border-slate-900 text-center w-28">Marks Obtained</th>
                    <th className="p-2 border border-slate-900 text-center w-20">Grade</th>
                    <th className="p-2 border border-slate-900 text-center w-24">Remarks</th>
                  </tr>
                </thead>
                <tbody>
                  {marksheet.subjects.map((sub, idx) => {
                    const obt = selectedStudent.marks[sub.id] ?? 0;
                    const isPass = obt >= sub.passingMarks;
                    const pct = sub.totalMarks > 0 ? (obt / sub.totalMarks) * 100 : 0;
                    let gr = 'F';
                    if (pct >= 90) gr = 'A+';
                    else if (pct >= 80) gr = 'A';
                    else if (pct >= 70) gr = 'B';
                    else if (pct >= 60) gr = 'C';
                    else if (pct >= 50) gr = 'D';
                    else if (pct >= 40) gr = 'E';

                    return (
                      <tr
                        key={sub.id}
                        className={`border border-slate-900 ${
                          idx % 2 === 0 ? 'bg-white' : 'bg-slate-50'
                        }`}
                      >
                        <td className="p-2 border border-slate-900 text-center font-bold text-slate-900">
                          {idx + 1}
                        </td>
                        <td className="p-2 border border-slate-900 font-extrabold text-slate-950">
                          {sub.name}
                        </td>
                        <td className="p-2 border border-slate-900 text-center font-bold text-slate-900">
                          {sub.totalMarks}
                        </td>
                        <td className="p-2 border border-slate-900 text-center font-medium text-slate-600">
                          {sub.passingMarks}
                        </td>
                        <td className="p-2 border border-slate-900 text-center font-black text-sm text-slate-950">
                          {obt}
                        </td>
                        <td className="p-2 border border-slate-900 text-center font-black text-blue-900">
                          {gr}
                        </td>
                        <td className="p-2 border border-slate-900 text-center font-black">
                          <span className={isPass ? 'text-emerald-700' : 'text-rose-700'}>
                            {isPass ? 'PASS' : 'FAIL'}
                          </span>
                        </td>
                      </tr>
                    );
                  })}

                  {/* Grand Totals Row */}
                  {(() => {
                    const stats = computeStudentStats(selectedStudent);
                    return (
                      <tr className="bg-slate-200 border-2 border-slate-900 font-black text-xs">
                        <td colSpan={2} className="p-2.5 text-right uppercase border border-slate-900">
                          GRAND TOTAL MARKS:
                        </td>
                        <td className="p-2.5 text-center border border-slate-900">
                          {totalMaxMarks}
                        </td>
                        <td className="p-2.5 text-center border border-slate-900">-</td>
                        <td className="p-2.5 text-center text-sm text-blue-950 border border-slate-900">
                          {stats.totalObtained}
                        </td>
                        <td className="p-2.5 text-center text-sm text-blue-950 border border-slate-900">
                          {stats.grade}
                        </td>
                        <td
                          className={`p-2.5 text-center text-sm border border-slate-900 ${
                            stats.status === 'PASS' ? 'text-emerald-800' : 'text-rose-800'
                          }`}
                        >
                          {stats.status}
                        </td>
                      </tr>
                    );
                  })()}
                </tbody>
              </table>
            </div>

            {/* Performance Summary Banner */}
            {(() => {
              const stats = computeStudentStats(selectedStudent);
              return (
                <div className="grid grid-cols-4 gap-2 border border-slate-900 bg-blue-50 p-3 rounded-lg text-center mb-5 text-xs font-black">
                  <div>
                    <span className="text-[10px] text-slate-600 uppercase block font-bold">
                      Percentage:
                    </span>
                    <span className="text-sm text-blue-950">{stats.percentage}%</span>
                  </div>
                  <div>
                    <span className="text-[10px] text-slate-600 uppercase block font-bold">
                      Overall Grade:
                    </span>
                    <span className="text-sm text-blue-950">{stats.grade}</span>
                  </div>
                  <div>
                    <span className="text-[10px] text-slate-600 uppercase block font-bold">
                      Final Result:
                    </span>
                    <span
                      className={`text-sm ${
                        stats.status === 'PASS' ? 'text-emerald-800' : 'text-rose-800'
                      }`}
                    >
                      {stats.status}
                    </span>
                  </div>
                  <div>
                    <span className="text-[10px] text-slate-600 uppercase block font-bold">
                      Position:
                    </span>
                    <span className="text-sm text-blue-950">
                      {selectedStudent.rank || '-'}
                    </span>
                  </div>
                </div>
              );
            })()}

            {/* Grading Scale Criteria Legend & Teacher Remarks */}
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 mb-6">
              {/* Grading Legend */}
              <div className="border border-slate-300 p-2.5 rounded text-[10px]">
                <div className="font-black text-slate-800 uppercase mb-1">
                  Official BISE Grading Formula:
                </div>
                <div className="grid grid-cols-4 gap-1 text-center font-bold text-slate-700">
                  <div className="bg-slate-100 p-1 rounded">A+ : 90%+</div>
                  <div className="bg-slate-100 p-1 rounded">A : 80-89%</div>
                  <div className="bg-slate-100 p-1 rounded">B : 70-79%</div>
                  <div className="bg-slate-100 p-1 rounded">C : 60-69%</div>
                  <div className="bg-slate-100 p-1 rounded">D : 50-59%</div>
                  <div className="bg-slate-100 p-1 rounded">E : 40-49%</div>
                  <div className="bg-rose-100 text-rose-800 p-1 rounded col-span-2">
                    F (Fail) : &lt;40%
                  </div>
                </div>
              </div>

              {/* Teacher Remarks Box */}
              <div className="border border-slate-300 p-2.5 rounded text-xs flex flex-col justify-between">
                <div>
                  <div className="font-black text-slate-800 uppercase text-[10px] mb-1">
                    Class Teacher's Remarks &amp; Conduct:
                  </div>
                  <div className="italic text-slate-800 font-medium leading-relaxed">
                    "{selectedStudent.remarks || 'Shows consistent effort and commendable dedication. Keep up the high standard!'}"
                  </div>
                </div>
                <div className="text-[10px] font-bold text-slate-500 mt-1">
                  General Conduct: Excellent &bull; Punctuality: Regular
                </div>
              </div>
            </div>

            {/* Official Four Signatures */}
            <div className="pt-6 border-t border-slate-400 grid grid-cols-4 text-center text-xs font-bold text-slate-900">
              <div>
                <div className="w-28 border-t-2 border-slate-800 mx-auto pt-1 font-black">
                  Class Teacher
                </div>
              </div>
              <div>
                <div className="w-32 border-t-2 border-slate-800 mx-auto pt-1 font-black">
                  Exam Incharge
                </div>
              </div>
              <div>
                <div className="w-28 border-t-2 border-slate-800 mx-auto pt-1 font-black">
                  Parent / Guardian
                </div>
              </div>
              <div>
                <div className="w-32 border-t-2 border-slate-800 mx-auto pt-1 font-black">
                  Principal / Seal
                </div>
              </div>
            </div>

            <div className="text-center text-[10px] text-slate-500 font-mono mt-8 border-t border-slate-200 pt-2">
              Automated Academic Evaluation System &bull; System Verified Marksheet
            </div>
          </div>
        </div>
      )}

      {/* ========================================================================= */}
      {/* MODE 3: CLASS-WIDE MASTER BROADSHEET GAZETTE PREVIEW & PRINT               */}
      {/* ========================================================================= */}
      {activeTabMode === 'masterSheet' && (
        <div className="space-y-4">
          <div
            id="mastersheet-print-container"
            className="bg-white rounded-2xl shadow-xl border border-slate-300 p-6 sm:p-8 max-w-5xl mx-auto print:border-none print:shadow-none print:p-0 print:m-0 print:max-w-none print:w-full overflow-x-auto"
          >
            {/* Header */}
            <div className="border-b-2 border-slate-900 pb-3 mb-4 text-center">
              <div className="flex items-center justify-between gap-4">
                <SchoolMonogram logoUrl={branding.logoUrl} schoolName={branding.schoolName} size={65} />
                <div className="flex-1 text-center">
                  <h1 className="text-lg sm:text-xl font-black uppercase text-slate-950">
                    {branding.schoolName}
                  </h1>
                  <div className="text-xs font-bold text-slate-700">
                    {branding.campusName} &bull; {branding.address}
                  </div>
                  <div className="text-[10px] text-slate-600 font-semibold">
                    Phone: {branding.phone} &bull; {branding.boardPattern}
                  </div>
                </div>
                <div className="hidden sm:flex flex-col items-center justify-center p-2 rounded-xl bg-slate-50 border border-slate-300 w-24 text-center">
                  <span className="text-[9px] uppercase font-black text-blue-900 tracking-wider">Gazette</span>
                  <span className="text-[11px] font-extrabold text-slate-900 mt-0.5">{marksheet.session}</span>
                  <span className="text-[9px] font-bold text-emerald-700 mt-0.5">Verified</span>
                </div>
              </div>

              <div className="mt-2.5 bg-blue-900 text-white font-black py-1 px-4 rounded text-xs uppercase tracking-wider">
                Consolidated Result Gazette / Master Sheet &bull; Session {marksheet.session}
              </div>

              <div className="mt-1.5 text-xs font-black text-slate-900 uppercase">
                Class: {marksheet.classLevel} &bull; Examination: {marksheet.examCategory} &bull; Total Candidates: {marksheet.students.length}
              </div>
            </div>

            {/* Broadsheet Table */}
            <table className="w-full text-xs border-collapse border border-slate-900 min-w-[700px]">
              <thead>
                <tr className="bg-slate-900 text-white font-extrabold uppercase text-[10px]">
                  <th className="p-1.5 border border-slate-900 text-center w-12">Roll#</th>
                  <th className="p-1.5 border border-slate-900 text-left w-36">Student Name</th>
                  <th className="p-1.5 border border-slate-900 text-left w-32">Father's Name</th>
                  {marksheet.subjects.map((sub) => (
                    <th key={sub.id} className="p-1.5 border border-slate-900 text-center">
                      <div>{sub.name}</div>
                      <div className="text-[8px] text-blue-300">({sub.totalMarks})</div>
                    </th>
                  ))}
                  <th className="p-1.5 border border-slate-900 text-center w-16">
                    Total
                    <div className="text-[8px] text-blue-300">({totalMaxMarks})</div>
                  </th>
                  <th className="p-1.5 border border-slate-900 text-center w-12">%</th>
                  <th className="p-1.5 border border-slate-900 text-center w-10">Grd</th>
                  <th className="p-1.5 border border-slate-900 text-center w-14">Result</th>
                  <th className="p-1.5 border border-slate-900 text-center w-12">Rank</th>
                </tr>
              </thead>
              <tbody>
                {marksheet.students.map((st, sIdx) => {
                  const stats = computeStudentStats(st);
                  return (
                    <tr
                      key={st.id}
                      className={`border border-slate-900 ${
                        sIdx % 2 === 0 ? 'bg-white' : 'bg-slate-50'
                      }`}
                    >
                      <td className="p-1.5 border border-slate-900 text-center font-black text-blue-950">
                        {st.rollNo}
                      </td>
                      <td className="p-1.5 border border-slate-900 font-extrabold text-slate-950">
                        {st.name}
                      </td>
                      <td className="p-1.5 border border-slate-900 text-slate-700">
                        {st.fatherName || '-'}
                      </td>

                      {marksheet.subjects.map((sub) => {
                        const obt = st.marks[sub.id] ?? 0;
                        const isPass = obt >= sub.passingMarks;
                        return (
                          <td
                            key={sub.id}
                            className={`p-1.5 border border-slate-900 text-center font-bold ${
                              isPass ? 'text-slate-900' : 'text-rose-700 font-black'
                            }`}
                          >
                            {obt}
                          </td>
                        );
                      })}

                      <td className="p-1.5 border border-slate-900 text-center font-black text-blue-950">
                        {stats.totalObtained}
                      </td>
                      <td className="p-1.5 border border-slate-900 text-center font-bold">
                        {stats.percentage}%
                      </td>
                      <td className="p-1.5 border border-slate-900 text-center font-black text-blue-900">
                        {stats.grade}
                      </td>
                      <td
                        className={`p-1.5 border border-slate-900 text-center font-black text-[10px] ${
                          stats.status === 'PASS' ? 'text-emerald-800' : 'text-rose-800'
                        }`}
                      >
                        {stats.status}
                      </td>
                      <td className="p-1.5 border border-slate-900 text-center font-bold text-slate-800">
                        {st.rank || '-'}
                      </td>
                    </tr>
                  );
                })}
              </tbody>
            </table>

            {/* Master Sheet Signatures */}
            <div className="pt-8 border-t border-slate-400 grid grid-cols-3 text-center text-xs font-bold text-slate-900 mt-6">
              <div>
                <div className="w-36 border-t-2 border-slate-800 mx-auto pt-1 font-black">
                  Class Incharge
                </div>
              </div>
              <div>
                <div className="w-40 border-t-2 border-slate-800 mx-auto pt-1 font-black">
                  Controller Examinations
                </div>
              </div>
              <div>
                <div className="w-36 border-t-2 border-slate-800 mx-auto pt-1 font-black">
                  Principal / Headmaster
                </div>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};
