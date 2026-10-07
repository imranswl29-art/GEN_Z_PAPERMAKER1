import React from 'react';
import {
  LayoutDashboard,
  FilePlus2,
  BookOpen,
  FolderArchive,
  FileCheck2,
  CircleDot,
  Building2,
  ShieldCheck,
  LogOut,
  ChevronRight,
  GraduationCap,
  Sparkles,
  Phone,
  Code2,
  Share2,
  PanelLeftClose,
  PanelLeftOpen,
  Calendar,
  Award,
  LifeBuoy,
} from 'lucide-react';
import { UserAccount } from '../types/user';

export type ActiveNavTab =
  | 'dashboard'
  | 'create_paper'
  | 'question_bank'
  | 'saved_papers'
  | 'answer_key'
  | 'bubble_sheet'
  | 'school_profile'
  | 'date_sheet'
  | 'result_card'
  | 'support_bug'
  | 'admin_portal';

interface NavigationSidebarProps {
  activeTab: ActiveNavTab;
  onSelectTab: (tab: ActiveNavTab) => void;
  currentUser: UserAccount | null;
  onOpenLogin: () => void;
  onLogout: () => void;
  isCollapsed?: boolean;
  onToggleCollapse?: () => void;
}

export const NavigationSidebar: React.FC<NavigationSidebarProps> = ({
  activeTab,
  onSelectTab,
  currentUser,
  onOpenLogin,
  onLogout,
  isCollapsed = false,
  onToggleCollapse,
}) => {
  const isAdmin = currentUser?.role === 'admin';

  const menuItems = [
    {
      id: 'dashboard',
      label: 'Dashboard',
      icon: LayoutDashboard,
      badge: 'Home',
    },
    {
      id: 'create_paper',
      label: 'Create Paper',
      icon: FilePlus2,
      badge: 'AI & Manual',
      highlight: true,
    },
    {
      id: 'question_bank',
      label: 'Question Bank',
      icon: BookOpen,
      badge: 'Matric 9-10',
    },
    {
      id: 'saved_papers',
      label: 'Saved Papers',
      icon: FolderArchive,
    },
    {
      id: 'answer_key',
      label: 'Answer Keys',
      icon: FileCheck2,
    },
    {
      id: 'bubble_sheet',
      label: 'OMR Bubble Sheets',
      icon: CircleDot,
    },
    {
      id: 'school_profile',
      label: 'School Branding',
      icon: Building2,
      badge: 'Monogram',
    },
    {
      id: 'date_sheet',
      label: 'Date Sheet Generator',
      icon: Calendar,
      badge: 'New',
    },
    {
      id: 'result_card',
      label: 'Result Card & Marksheet',
      icon: Award,
      badge: 'New',
    },
    {
      id: 'support_bug',
      label: 'Support & Report Bug',
      icon: LifeBuoy,
      badge: 'Help',
    },
  ];

  if (isAdmin) {
    menuItems.push({
      id: 'admin_portal',
      label: 'Admin Portal',
      icon: ShieldCheck,
      badge: 'Super Admin',
      highlight: false,
    });
  }

  return (
    <aside
      className={`${
        isCollapsed ? 'w-16' : 'w-64'
      } bg-white border-r border-slate-200 flex flex-col h-screen sticky top-0 shrink-0 select-none z-30 no-print text-slate-800 transition-all duration-200 shadow-sm`}
    >
      {/* Brand Header: Exact required heading "PAPER MAKER SOFTWARE" */}
      <div className="p-3.5 sm:p-4 border-b border-slate-200 bg-slate-50 flex items-center justify-between">
        <div className="flex items-center gap-2.5 min-w-0">
          <div className="w-9 h-9 rounded-xl bg-gradient-to-tr from-blue-700 to-indigo-600 flex items-center justify-center shadow-md text-white font-black text-lg shrink-0">
            <GraduationCap className="w-5 h-5 text-white" />
          </div>
          {!isCollapsed && (
            <div className="min-w-0">
              <h1 className="font-black text-xs tracking-tight text-slate-950 uppercase truncate">
                PAPER MAKER SOFTWARE
              </h1>
              <div className="text-[10px] text-blue-700 font-bold tracking-wider uppercase truncate">
                Matric Science (9th & 10th)
              </div>
            </div>
          )}
        </div>

        {onToggleCollapse && (
          <button
            type="button"
            onClick={onToggleCollapse}
            className="p-1 rounded-lg text-slate-500 hover:text-slate-900 hover:bg-slate-200 transition-colors cursor-pointer shrink-0 ml-1"
            title={isCollapsed ? 'Expand Sidebar (Space for Laptops)' : 'Collapse Sidebar (More Space for Laptops)'}
          >
            {isCollapsed ? (
              <PanelLeftOpen className="w-4 h-4 text-blue-600" />
            ) : (
              <PanelLeftClose className="w-4 h-4 text-slate-600" />
            )}
          </button>
        )}
      </div>

      {/* User Status Card */}
      {!isCollapsed ? (
        <div className="p-3 mx-3 my-2.5 bg-slate-50 rounded-xl border border-slate-200">
          {currentUser ? (
            <div>
              <div className="flex items-center justify-between mb-1">
                <span
                  className={`text-[9px] font-black px-2 py-0.5 rounded uppercase tracking-wider ${
                    isAdmin ? 'bg-amber-100 text-amber-900 border border-amber-300' : 'bg-blue-100 text-blue-900 border border-blue-300'
                  }`}
                >
                  {isAdmin ? 'Master Admin' : 'School Principal'}
                </span>
              </div>
              <div className="font-extrabold text-xs text-slate-950 truncate">{currentUser.name}</div>
              <div className="text-[11px] text-slate-600 font-semibold truncate">{currentUser.schoolName}</div>
            </div>
          ) : (
            <div className="flex items-center justify-between">
              <div>
                <div className="text-xs font-bold text-slate-800">Guest Teacher</div>
                <div className="text-[10px] text-slate-500 font-medium">Sign in for School Logo</div>
              </div>
              <button
                onClick={onOpenLogin}
                className="px-2.5 py-1 bg-blue-600 hover:bg-blue-500 text-white font-bold rounded-lg text-xs transition-colors cursor-pointer"
              >
                Login
              </button>
            </div>
          )}
        </div>
      ) : (
        <div className="p-2 text-center border-b border-slate-200">
          {currentUser ? (
            <div
              className="w-8 h-8 mx-auto rounded-full bg-blue-700 text-white flex items-center justify-center font-bold text-xs uppercase shadow-xs"
              title={`${currentUser.name} (${currentUser.schoolName})`}
            >
              {currentUser.username.slice(0, 2)}
            </div>
          ) : (
            <button
              onClick={onOpenLogin}
              className="w-8 h-8 mx-auto rounded-full bg-slate-200 hover:bg-slate-300 text-slate-800 flex items-center justify-center text-xs font-bold"
              title="Login"
            >
              IN
            </button>
          )}
        </div>
      )}

      {/* Navigation Links */}
      <nav className="flex-1 px-2 space-y-1 overflow-y-auto">
        {menuItems.map((item) => {
          const isActive = activeTab === item.id;
          const Icon = item.icon;
          return (
            <button
              key={item.id}
              onClick={() => onSelectTab(item.id as ActiveNavTab)}
              title={isCollapsed ? item.label : undefined}
              className={`w-full flex items-center ${
                isCollapsed ? 'justify-center p-2.5' : 'justify-between px-3 py-2'
              } rounded-xl text-xs transition-all cursor-pointer ${
                isActive
                  ? 'btn-3d btn-3d-blue text-white font-black shadow-md'
                  : 'text-slate-700 hover:text-slate-950 hover:bg-slate-100 font-bold border border-transparent hover:border-slate-200'
              }`}
            >
              <div className="flex items-center gap-2.5">
                <Icon className={`w-4 h-4 shrink-0 ${isActive ? 'text-white' : 'text-blue-700'}`} />
                {!isCollapsed && <span className="truncate">{item.label}</span>}
              </div>
              {!isCollapsed && item.badge && (
                <span
                  className={`text-[9px] px-1.5 py-0.5 rounded font-mono font-bold ${
                    isActive
                      ? 'bg-white text-blue-900 shadow-xs font-black'
                      : item.badge === 'New'
                      ? 'bg-emerald-100 text-emerald-900 font-black border border-emerald-300'
                      : item.badge === 'Help'
                      ? 'bg-cyan-100 text-cyan-900 font-black border border-cyan-300'
                      : item.badge === 'Super Admin'
                      ? 'bg-amber-100 text-amber-900 font-black border border-amber-300'
                      : 'bg-slate-100 text-slate-800 font-bold border border-slate-300'
                  }`}
                >
                  {item.badge}
                </span>
              )}
            </button>
          );
        })}
      </nav>

      {/* Developer Card (Web & Desktop ONLY - tagged with no-print so it NEVER prints on exam papers) */}
      {!isCollapsed && (
        <div className="p-2.5 mx-2.5 mb-2.5 bg-slate-50 rounded-xl border border-slate-200 text-slate-800 text-xs space-y-1 no-print shadow-2xs">
          <div className="flex items-center gap-1.5 text-[9px] font-black uppercase tracking-wider text-blue-700">
            <Code2 className="w-3 h-3 text-blue-700" />
            <span>Software Developer</span>
          </div>
          <div>
            <div className="font-extrabold text-slate-950 text-[11px] tracking-wide">
              MUHAMMAD IMRAN KHAN
            </div>
            <div className="text-[10px] text-slate-600 font-semibold">
              MSc Computer Science
            </div>
          </div>
          <div className="pt-1 border-t border-slate-200 flex flex-col gap-0.5 text-[10px] font-mono text-slate-800">
            <div className="flex items-center gap-1">
              <Phone className="w-2.5 h-2.5 text-emerald-600 shrink-0" />
              <a href="tel:03007603964" className="hover:text-blue-700 transition-colors font-bold">03007603964</a>
            </div>
            <div className="flex items-center gap-1">
              <Phone className="w-2.5 h-2.5 text-emerald-600 shrink-0" />
              <a href="tel:03147603964" className="hover:text-blue-700 transition-colors font-bold">03147603964</a>
            </div>
          </div>
        </div>
      )}
    </aside>
  );
};
