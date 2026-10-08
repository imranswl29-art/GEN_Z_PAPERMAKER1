import React from 'react';
import {
  FilePlus2,
  BookOpen,
  Printer,
  FileCheck2,
  CircleDot,
  GraduationCap,
  Sparkles,
  ArrowRight,
  Download,
  Building2,
  Calendar,
  Layers,
  CheckCircle2,
  Phone,
  Code2,
  CheckSquare,
  Trash2,
  FolderArchive,
  Award,
  ShieldCheck,
  LifeBuoy,
} from 'lucide-react';
import { UserAccount } from '../types/user';
import { GeneratedExamPaper, ClassLevel } from '../types/paper';
import { exportPaperToWord } from '../utils/exportWord';
import { ActiveNavTab } from './NavigationSidebar';

interface DashboardViewProps {
  currentUser: UserAccount | null;
  savedPapers: GeneratedExamPaper[];
  onOpenCreatePaper: (initialClass?: ClassLevel) => void;
  onOpenAiGenerator?: (initialClass?: ClassLevel) => void;
  onOpenManualSelector?: (initialClass?: ClassLevel) => void;
  onOpenQuestionBank: () => void;
  onViewPaper: (paper: GeneratedExamPaper) => void;
  onOpenSchoolProfile: () => void;
  onOpenBubbleSheet: (paper: GeneratedExamPaper) => void;
  onOpenAnswerKey: (paper: GeneratedExamPaper) => void;
  onDeletePaper?: (paperId: string) => void;
  onSelectTab?: (tab: ActiveNavTab) => void;
}

export const DashboardView: React.FC<DashboardViewProps> = ({
  currentUser,
  savedPapers,
  onOpenCreatePaper,
  onOpenAiGenerator,
  onOpenManualSelector,
  onOpenQuestionBank,
  onViewPaper,
  onOpenSchoolProfile,
  onOpenBubbleSheet,
  onOpenAnswerKey,
  onDeletePaper,
  onSelectTab,
}) => {
  return (
    <div className="space-y-6 max-w-7xl mx-auto font-sans text-slate-800">
      {/* Welcome Banner with 3D Depth and explicit background fallback */}
      <div
        className="rounded-2xl p-6 sm:p-8 text-white shadow-2xl relative overflow-hidden border border-slate-700/80"
        style={{
          background: 'linear-gradient(135deg, #090d16 0%, #0f172a 60%, #1e1b4b 100%)',
          boxShadow: '0 10px 25px -5px rgba(0, 0, 0, 0.4), 0 8px 10px -6px rgba(0, 0, 0, 0.3), inset 0 1px 0 rgba(255, 255, 255, 0.15)',
        }}
      >
        <div className="relative z-10 max-w-3xl space-y-3">
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-blue-500/20 text-blue-300 border border-blue-400/40 text-xs font-bold uppercase tracking-wider shadow-xs">
            <Sparkles className="w-3.5 h-3.5 text-blue-400" />
            <span>PAPER MAKER SOFTWARE</span>
          </div>

          <h1 className="text-2xl sm:text-3xl font-extrabold tracking-tight text-white drop-shadow-sm">
            {currentUser?.schoolName || 'Punjab Board Examination System'}
          </h1>

          <p className="text-sm text-slate-200 leading-relaxed font-medium">
            Generate authentic board pattern question papers for 9th and 10th Matric Science Group & Compulsory Subjects (English & Urdu) in English, Urdu Nastaliq, or Bilingual format. Complete with official pairing schemes, OMR bubble sheets, answer keys, and MS Word export.
          </p>

          <div className="flex flex-wrap items-center gap-3 pt-2">
            {onOpenAiGenerator && (
              <button
                type="button"
                onClick={() => onOpenAiGenerator()}
                className="btn-3d flex items-center gap-2 px-5 py-2.5 rounded-xl text-xs font-black text-white cursor-pointer shadow-lg"
                style={{ backgroundColor: '#7c3aed', border: '1px solid #6d28d9' }}
                title="Generate paper using Google Gemini AI"
              >
                <Sparkles className="w-4 h-4 text-purple-200" />
                <span>🤖 AI Smart Generation</span>
              </button>
            )}

            <button
              type="button"
              onClick={() => onOpenCreatePaper()}
              className="btn-3d flex items-center gap-2 px-5 py-2.5 rounded-xl text-xs font-black text-white cursor-pointer shadow-md"
              style={{ backgroundColor: '#059669', border: '1px solid #047857' }}
              title="Create paper step-by-step from verified PTBB Question Bank"
            >
              <FilePlus2 className="w-4 h-4 text-emerald-100" />
              <span>📚 Question Bank Builder</span>
            </button>

            {onOpenManualSelector && (
              <button
                type="button"
                onClick={() => onOpenManualSelector()}
                className="btn-3d flex items-center gap-2 px-4 py-2.5 rounded-xl text-xs font-black text-white cursor-pointer"
                style={{ backgroundColor: '#2563eb', border: '1px solid #1d4ed8' }}
                title="Handpick individual questions manually"
              >
                <CheckSquare className="w-4 h-4 text-blue-100" />
                <span>✍️ Manual Selection</span>
              </button>
            )}

            <button
              type="button"
              onClick={onOpenQuestionBank}
              className="btn-3d flex items-center gap-2 px-4 py-2.5 rounded-xl text-xs font-black text-white cursor-pointer"
              style={{ backgroundColor: '#4338ca', border: '1px solid #3730a3' }}
            >
              <BookOpen className="w-4 h-4 text-indigo-100" />
              <span>Browse Question Bank</span>
            </button>

            <button
              type="button"
              onClick={onOpenSchoolProfile}
              className="btn-3d btn-3d-amber flex items-center gap-2 px-4 py-2.5 rounded-xl text-xs font-black cursor-pointer shadow-md"
            >
              <Building2 className="w-4 h-4 text-slate-950" />
              <span>School Monogram & Profile</span>
            </button>

            {onSelectTab && (
              <>
                <button
                  type="button"
                  onClick={() => onSelectTab('date_sheet')}
                  className="btn-3d flex items-center gap-2 px-4 py-2.5 rounded-xl text-xs font-black text-white cursor-pointer shadow-md"
                  style={{ backgroundColor: '#7e22ce', border: '1px solid #6b21a8' }}
                  title="Generate Official Date Sheet"
                >
                  <Calendar className="w-4 h-4 text-purple-200" />
                  <span>📅 Date Sheet</span>
                </button>

                <button
                  type="button"
                  onClick={() => onSelectTab('result_card')}
                  className="btn-3d flex items-center gap-2 px-4 py-2.5 rounded-xl text-xs font-black text-white cursor-pointer shadow-md"
                  style={{ backgroundColor: '#1d4ed8', border: '1px solid #1e40af' }}
                  title="Generate Student Marksheet & Result Cards"
                >
                  <Award className="w-4 h-4 text-blue-200" />
                  <span>🏆 Result Cards</span>
                </button>

                <button
                  type="button"
                  onClick={() => onSelectTab('bubble_sheet')}
                  className="btn-3d flex items-center gap-2 px-4 py-2.5 rounded-xl text-xs font-black text-white cursor-pointer shadow-md"
                  style={{ backgroundColor: '#0891b2', border: '1px solid #0e7490' }}
                  title="Generate OMR Bubble Sheets"
                >
                  <CircleDot className="w-4 h-4 text-cyan-200" />
                  <span>⭕ OMR Bubble Sheets</span>
                </button>
              </>
            )}
          </div>
        </div>

        {/* Subtle decorative emblem */}
        <div className="absolute right-6 -bottom-8 opacity-10 pointer-events-none select-none">
          <GraduationCap className="w-64 h-64 text-white" />
        </div>
      </div>

      {/* Metrics Row (Interactive 1-Click Cards) */}
      <div className="grid grid-cols-2 sm:grid-cols-4 gap-4">
        <div
          onClick={() => onSelectTab && onSelectTab('saved_papers')}
          className="card-3d p-4 flex flex-col justify-between cursor-pointer hover:border-blue-400 hover:shadow-md transition-all group"
          title="Click to open Saved Papers Archive"
        >
          <div className="flex items-center justify-between mb-1">
            <span className="text-[11px] font-black uppercase tracking-wider text-slate-700 group-hover:text-blue-700 transition-colors">
              Total Papers Created
            </span>
            <div className="w-8 h-8 rounded-lg bg-blue-600 text-white flex items-center justify-center shadow-xs shrink-0 group-hover:scale-110 transition-transform">
              <FolderArchive className="w-4 h-4 text-white" />
            </div>
          </div>
          <div className="text-2xl font-black text-slate-950 mt-1">{savedPapers.length}</div>
          <span className="text-[11px] text-blue-700 font-bold mt-0.5 group-hover:underline">Click to view archive &rarr;</span>
        </div>

        <div
          onClick={onOpenSchoolProfile}
          className="card-3d p-4 flex flex-col justify-between cursor-pointer hover:border-indigo-400 hover:shadow-md transition-all group"
          title="Click to view Board Pattern and School Profile"
        >
          <div className="flex items-center justify-between mb-1">
            <span className="text-[11px] font-black uppercase tracking-wider text-slate-700 group-hover:text-indigo-700 transition-colors">
              Target Board Pattern
            </span>
            <div className="w-8 h-8 rounded-lg bg-indigo-600 text-white flex items-center justify-center shadow-xs shrink-0 group-hover:scale-110 transition-transform">
              <Award className="w-4 h-4 text-white" />
            </div>
          </div>
          <div className="text-base font-bold text-slate-950 truncate mt-1">
            {currentUser?.targetBoard ? currentUser.targetBoard.toUpperCase() + ' Board' : 'BISE Punjab'}
          </div>
          <span className="text-[11px] text-slate-700 font-semibold mt-0.5 group-hover:text-indigo-600">PTBB Scheme &bull; Edit branding &rarr;</span>
        </div>

        <div
          onClick={() => onOpenCreatePaper('9th')}
          className="card-3d p-4 flex flex-col justify-between cursor-pointer hover:border-emerald-400 hover:shadow-md transition-all group"
          title="Click to create a new paper"
        >
          <div className="flex items-center justify-between mb-1">
            <span className="text-[11px] font-black uppercase tracking-wider text-slate-700 group-hover:text-emerald-700 transition-colors">
              Active Classes
            </span>
            <div className="w-8 h-8 rounded-lg bg-emerald-600 text-white flex items-center justify-center shadow-xs shrink-0 group-hover:scale-110 transition-transform">
              <GraduationCap className="w-4 h-4 text-white" />
            </div>
          </div>
          <div className="text-base font-bold text-slate-950 mt-1">9th & 10th Class</div>
          <span className="text-[11px] text-emerald-700 font-bold mt-0.5 group-hover:underline">Launch builder &rarr;</span>
        </div>

        <div
          onClick={() => {
            if (currentUser?.role === 'admin' && onSelectTab) {
              onSelectTab('admin_portal');
            } else {
              onOpenSchoolProfile();
            }
          }}
          className="card-3d p-4 flex flex-col justify-between cursor-pointer hover:border-amber-400 hover:shadow-md transition-all group"
          title="Click to view subscription & license details"
        >
          <div className="flex items-center justify-between mb-1">
            <span className="text-[11px] font-black uppercase tracking-wider text-slate-700 group-hover:text-amber-800 transition-colors">
              System License
            </span>
            <div className="w-8 h-8 rounded-lg bg-amber-600 text-white flex items-center justify-center shadow-xs shrink-0 group-hover:scale-110 transition-transform">
              <ShieldCheck className="w-4 h-4 text-white" />
            </div>
          </div>
          <div className="text-base font-bold text-emerald-700 flex items-center gap-1 mt-1">
            <CheckCircle2 className="w-4 h-4 text-emerald-600" />
            <span>Active</span>
          </div>
          <span className="text-[11px] text-slate-700 font-semibold mt-0.5">
            Valid till {currentUser?.expiryDate || '2027-12-31'}
          </span>
        </div>
      </div>

      {/* Full Examination Modules Hub (All Icons Clickable on Laptops & Desktops) */}
      <div className="card-3d p-5 space-y-3">
        <div className="flex items-center justify-between border-b border-slate-200 pb-2.5">
          <div>
            <h2 className="text-sm font-extrabold uppercase tracking-wider text-slate-900 flex items-center gap-2">
              <Sparkles className="w-4 h-4 text-blue-600" />
              <span>Examination System Modules & Tools Hub</span>
            </h2>
            <p className="text-xs text-slate-500">1-click direct access to all paper generator tools, archives, and official document generators</p>
          </div>
        </div>

        <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 xl:grid-cols-6 gap-3 pt-1">
          {[
            {
              id: 'create_paper' as ActiveNavTab,
              label: 'Paper Builder',
              desc: '8-step paper wizard',
              icon: FilePlus2,
              color: 'from-emerald-600 to-teal-700',
              badge: 'Wizard',
            },
            {
              id: 'question_bank' as ActiveNavTab,
              label: 'Question Bank',
              desc: '9th & 10th verified pool',
              icon: BookOpen,
              color: 'from-indigo-600 to-blue-700',
              badge: 'Matric',
            },
            {
              id: 'date_sheet' as ActiveNavTab,
              label: 'Date Sheet',
              desc: 'Print official schedules',
              icon: Calendar,
              color: 'from-purple-600 to-indigo-700',
              badge: 'New',
            },
            {
              id: 'result_card' as ActiveNavTab,
              label: 'Result Cards',
              desc: 'Marksheets & grades',
              icon: Award,
              color: 'from-blue-700 to-cyan-700',
              badge: 'New',
            },
            {
              id: 'answer_key' as ActiveNavTab,
              label: 'Answer Keys',
              desc: 'Solved keys & solutions',
              icon: FileCheck2,
              color: 'from-teal-600 to-emerald-700',
              badge: 'Solved',
            },
            {
              id: 'bubble_sheet' as ActiveNavTab,
              label: 'Bubble Sheets',
              desc: 'OMR MCQ sheets',
              icon: CircleDot,
              color: 'from-cyan-600 to-blue-600',
              badge: 'OMR',
            },
            {
              id: 'school_profile' as ActiveNavTab,
              label: 'School Branding',
              desc: 'Logo, monogram & seals',
              icon: Building2,
              color: 'from-rose-600 to-pink-700',
              badge: 'Branding',
            },
            {
              id: 'saved_papers' as ActiveNavTab,
              label: 'Saved Archive',
              desc: 'Past examination papers',
              icon: FolderArchive,
              color: 'from-amber-600 to-orange-700',
              badge: `${savedPapers.length} Papers`,
            },
            {
              id: 'support_bug' as ActiveNavTab,
              label: 'Help & Support',
              desc: 'WhatsApp & bug report',
              icon: LifeBuoy,
              color: 'from-emerald-700 to-teal-800',
              badge: '24/7',
            },
            ...(currentUser?.role === 'admin'
              ? [
                  {
                    id: 'admin_portal' as ActiveNavTab,
                    label: 'Admin Portal',
                    desc: 'Manage school accounts',
                    icon: ShieldCheck,
                    color: 'from-amber-700 to-yellow-800',
                    badge: 'Master',
                  },
                ]
              : []),
          ].map((mod) => {
            const ModIcon = mod.icon;
            return (
              <button
                key={mod.id}
                type="button"
                onClick={() => {
                  if (onSelectTab) {
                    onSelectTab(mod.id);
                  } else if (mod.id === 'create_paper') {
                    onOpenCreatePaper();
                  } else if (mod.id === 'question_bank') {
                    onOpenQuestionBank();
                  } else if (mod.id === 'school_profile') {
                    onOpenSchoolProfile();
                  }
                }}
                className="btn-3d p-3 rounded-xl bg-white border border-slate-200 hover:border-blue-400 hover:shadow-md transition-all text-left flex flex-col justify-between space-y-2 cursor-pointer group"
                title={`Open ${mod.label}`}
              >
                <div className="flex items-center justify-between">
                  <div className={`w-8 h-8 rounded-lg bg-gradient-to-tr ${mod.color} text-white flex items-center justify-center shadow-xs group-hover:scale-110 transition-transform`}>
                    <ModIcon className="w-4 h-4 text-white" />
                  </div>
                  <span className="text-[9px] font-black font-mono px-1.5 py-0.5 rounded bg-slate-100 text-slate-700 border border-slate-200">
                    {mod.badge}
                  </span>
                </div>
                <div>
                  <div className="font-extrabold text-xs text-slate-900 group-hover:text-blue-700 transition-colors">
                    {mod.label}
                  </div>
                  <div className="text-[10px] text-slate-500 font-medium truncate">
                    {mod.desc}
                  </div>
                </div>
              </button>
            );
          })}
        </div>
      </div>

      {/* Quick Launch Cards by Class */}
      <div>
        <div className="flex items-center justify-between mb-3">
          <h2 className="text-sm font-extrabold uppercase tracking-wider text-slate-900">
            Fast Paper Generator by Class
          </h2>
          <span className="text-xs text-slate-700 font-bold">Select class to start builder</span>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 max-w-4xl">
          {[
            {
              level: '9th' as ClassLevel,
              name: '9th Class (Matric Part-I)',
              subTitle: 'Secondary School Certificate - Science Group',
              subjects: 'Physics, Chemistry, Biology, Math, Computer, English, Urdu, Islamiat, Tarjuma-tul-Quran, Pak Studies',
              color: 'from-blue-700 to-indigo-800',
              btnClass: 'btn-3d-blue',
            },
            {
              level: '10th' as ClassLevel,
              name: '10th Class (Matric Part-II)',
              subTitle: 'Secondary School Certificate - Science Group',
              subjects: 'Physics, Chemistry, Biology, Math, Computer, English, Urdu, Islamiat, Tarjuma-tul-Quran, Pak Studies',
              color: 'from-indigo-700 to-slate-800',
              btnClass: 'btn-3d-indigo',
            },
          ].map((c) => (
            <div
              key={c.level}
              className="card-3d overflow-hidden flex flex-col justify-between"
            >
              <div className={`p-4 bg-gradient-to-r ${c.color} text-white`}>
                <div className="text-xs font-mono font-bold uppercase opacity-90">{c.level} PTBB</div>
                <h3 className="font-extrabold text-base mt-0.5">{c.name}</h3>
                <div className="text-xs opacity-90 mt-1">{c.subTitle}</div>
              </div>
              <div className="p-4 space-y-3 flex-1 flex flex-col justify-between text-xs">
                <p className="text-slate-700 text-xs leading-relaxed font-medium">
                  <strong className="text-slate-900">Available Subjects: </strong>{c.subjects}
                </p>
                <button
                  onClick={() => onOpenCreatePaper(c.level)}
                  className={`btn-3d ${c.btnClass} w-full py-2.5 text-white font-black rounded-xl flex items-center justify-center gap-1.5 cursor-pointer`}
                >
                  <span>Build {c.level} Paper</span>
                  <ArrowRight className="w-3.5 h-3.5" />
                </button>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Recent Generated Papers Section */}
      <div className="card-3d p-5">
        <div className="flex items-center justify-between mb-4 border-b border-slate-200 pb-3">
          <div>
            <h3 className="font-black text-sm text-slate-950">Recent Generated Question Papers</h3>
            <p className="text-xs text-slate-700 font-medium">1-click Print, MS Word download, Answer Key & Bubble Sheet</p>
          </div>
          <button
            onClick={() => onOpenCreatePaper()}
            className="btn-3d btn-3d-blue text-xs font-black text-white px-3 py-1.5 rounded-lg cursor-pointer"
          >
            + Create Another Paper
          </button>
        </div>

        {savedPapers.length > 0 ? (
          <div className="divide-y divide-slate-200">
            {savedPapers.slice(0, 5).map((p) => (
              <div
                key={p.id}
                className="py-3 flex flex-wrap items-center justify-between gap-3 text-xs hover:bg-slate-50 p-2 rounded-lg transition-colors"
              >
                <div>
                  <div className="font-extrabold text-slate-950 flex items-center gap-2">
                    <span className="text-sm">{p.header.subjectName}</span>
                    <span className="px-2 py-0.5 rounded bg-blue-100 text-blue-900 text-[10px] font-mono font-bold">
                      {p.header.classLevel}
                    </span>
                    <span className="text-slate-500 font-normal">·</span>
                    <span className="text-slate-800 font-semibold">{p.header.examTitle}</span>
                  </div>
                  <div className="text-xs text-slate-700 font-medium mt-0.5">
                    {p.header.dateStr} · Total Marks: <strong className="text-slate-950">{p.header.totalMarks}</strong> · Syllabus: {p.header.syllabusCovered || 'All chapters'}
                  </div>
                </div>

                <div className="flex items-center gap-1.5 flex-wrap">
                  <button
                    onClick={() => onViewPaper(p)}
                    className="btn-3d btn-3d-blue px-3 py-1.5 text-white rounded-lg font-bold text-[11px] cursor-pointer"
                  >
                    View Paper
                  </button>
                  <button
                    onClick={() => exportPaperToWord(p)}
                    className="btn-3d btn-3d-navy flex items-center gap-1 px-3 py-1.5 text-white rounded-lg font-bold text-[11px] cursor-pointer"
                  >
                    <Download className="w-3 h-3 text-blue-200" />
                    <span>MS Word</span>
                  </button>
                  <button
                    onClick={() => onOpenAnswerKey(p)}
                    className="btn-3d btn-3d-emerald px-3 py-1.5 text-white rounded-lg font-bold text-[11px] cursor-pointer"
                  >
                    Answer Key
                  </button>
                  <button
                    onClick={() => onOpenBubbleSheet(p)}
                    className="btn-3d btn-3d-purple px-3 py-1.5 text-white rounded-lg font-bold text-[11px] cursor-pointer"
                  >
                    Bubble Sheet
                  </button>
                  {onDeletePaper && (
                    <button
                      type="button"
                      onClick={() => {
                        if (window.confirm(`Are you sure you want to delete "${p.header.subjectName}" paper?`)) {
                          onDeletePaper(p.id);
                        }
                      }}
                      className="btn-3d btn-3d-ruby flex items-center gap-1 px-2.5 py-1.5 text-white rounded-lg font-bold text-[11px] cursor-pointer"
                      title="Delete this paper from saved list"
                    >
                      <Trash2 className="w-3 h-3" />
                      <span>Delete</span>
                    </button>
                  )}
                </div>
              </div>
            ))}
          </div>
        ) : (
          <div className="text-center py-8 text-slate-400 text-xs">
            No papers generated yet. Click &quot;Create New Exam Paper&quot; above to start.
          </div>
        )}
      </div>

      {/* Developer Banner in Desktop / Website View (no-print: NEVER shows on printed paper) */}
      <footer className="no-print pt-4 border-t border-slate-200 flex flex-wrap items-center justify-between text-xs text-slate-500">
        <div className="flex items-center gap-2">
          <Code2 className="w-4 h-4 text-blue-600" />
          <span>Developed by: <strong className="text-slate-800">MUHAMMAD IMRAN KHAN</strong> (MSc Computer Science)</span>
        </div>
        <div className="flex items-center gap-4 text-slate-600 font-mono text-[11px]">
          <span className="flex items-center gap-1">
            <Phone className="w-3 h-3 text-blue-600" />
            03007603964
          </span>
          <span className="flex items-center gap-1">
            <Phone className="w-3 h-3 text-blue-600" />
            03147603964
          </span>
        </div>
      </footer>
    </div>
  );
};
