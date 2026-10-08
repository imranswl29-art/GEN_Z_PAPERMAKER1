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
      badgeColor: 'bg-blue-600 text-white',
    },
    {
      id: 'create_paper',
      label: 'Create Paper',
      icon: FilePlus2,
      badge: 'AI & Manual',
      badgeColor: 'bg-emerald-600 text-white',
    },
    {
      id: 'question_bank',
      label: 'Question Bank',
      icon: BookOpen,
      badge: 'Matric 9-10',
      badgeColor: 'bg-indigo-600 text-white',
    },
    {
      id: 'saved_papers',
      label: 'Saved Papers',
      icon: FolderArchive,
      badgeColor: 'bg-amber-600 text-white',
    },
    {
      id: 'answer_key',
      label: 'Answer Keys',
      icon: FileCheck2,
      badgeColor: 'bg-teal-600 text-white',
    },
    {
      id: 'bubble_sheet',
      label: 'OMR Bubble Sheets',
      icon: CircleDot,
      badgeColor: 'bg-cyan-600 text-white',
    },
    {
      id: 'school_profile',
      label: 'School Branding',
      icon: Building2,
      badge: 'Monogram',
      badgeColor: 'bg-rose-600 text-white',
    },
    {
      id: 'date_sheet',
      label: 'Date Sheet Generator',
      icon: Calendar,
      badge: 'New',
      badgeColor: 'bg-purple-600 text-white',
    },
    {
      id: 'result_card',
      label: 'Result Card & Marksheet',
      icon: Award,
      badge: 'New',
      badgeColor: 'bg-blue-700 text-white',
    },
    {
      id: 'support_bug',
      label: 'Support & Report Bug',
      icon: LifeBuoy,
      badge: 'Help',
      badgeColor: 'bg-emerald-700 text-white',
    },
  ];

  if (isAdmin) {
    menuItems.push({
      id: 'admin_portal',
      label: 'Admin Portal',
      icon: ShieldCheck,
      badge: 'Super Admin',
      badgeColor: 'bg-amber-700 text-white',
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
        <div className="p-2.5 mx-2.5 my-1.5 bg-slate-50 rounded-xl border border-slate-200 shrink-0">
          {currentUser ? (
            <div>
              <div className="flex items-center justify-between mb-0.5">
                <span
                  className={`text-[9px] font-black px-1.5 py-0.5 rounded uppercase tracking-wider ${
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
        <div className="p-2 text-center border-b border-slate-200 shrink-0">
          {currentUser ? (
            <div
              className="w-8 h-8 mx-auto rounded-full bg-blue-700 text-white flex items-center justify-center font-bold text-xs uppercase shadow-xs cursor-pointer"
              title={`${currentUser.name} (${currentUser.schoolName})`}
              onClick={() => onSelectTab('school_profile')}
            >
              {currentUser.username.slice(0, 2)}
            </div>
          ) : (
            <button
              onClick={onOpenLogin}
              className="w-8 h-8 mx-auto rounded-full bg-slate-200 hover:bg-slate-300 text-slate-800 flex items-center justify-center text-xs font-bold cursor-pointer"
              title="Login"
            >
              IN
            </button>
          )}
        </div>
      )}

      {/* Navigation Links - Scrollable on Laptops */}
      <nav className="flex-1 px-2 py-1 space-y-1 overflow-y-auto min-h-0">
        {menuItems.map((item) => {
          const isActive = activeTab === item.id;
          const Icon = item.icon;
          return (
            <button
              key={item.id}
              type="button"
              onClick={() => onSelectTab(item.id as ActiveNavTab)}
              title={item.label}
              className={`w-full flex items-center ${
                isCollapsed ? 'justify-center p-2' : 'justify-between px-2.5 py-1.5'
              } rounded-xl text-xs transition-all cursor-pointer ${
                isActive
                  ? 'btn-3d btn-3d-blue text-white font-black shadow-md'
                  : 'text-slate-800 hover:text-slate-950 hover:bg-slate-100 font-bold border border-transparent hover:border-slate-200'
              }`}
            >
              <div className="flex items-center gap-2 min-w-0">
                <div
                  className={`w-7 h-7 rounded-lg flex items-center justify-center shrink-0 shadow-xs transition-all ${
                    isActive
                      ? 'bg-white text-blue-900 shadow-sm ring-2 ring-white/50'
                      : `${item.badgeColor} ring-1 ring-black/5`
                  }`}
                >
                  <Icon className="w-4 h-4 shrink-0 text-current" strokeWidth={2.4} />
                </div>
                {!isCollapsed && <span className="truncate font-bold text-left">{item.label}</span>}
              </div>
              {!isCollapsed && item.badge && (
                <span
                  className={`text-[9px] px-1.5 py-0.5 rounded font-mono font-bold shrink-0 ${
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
        <div className="p-2 mx-2 mb-1.5 bg-slate-50 rounded-xl border border-slate-200 text-slate-800 text-[10px] space-y-0.5 no-print shadow-2xs shrink-0">
          <div className="flex items-center justify-between text-[9px] font-black uppercase tracking-wider text-blue-700">
            <span className="flex items-center gap-1">
              <Code2 className="w-3 h-3 text-blue-700" />
              <span>Developer</span>
            </span>
            <span className="font-extrabold text-slate-900">M. IMRAN KHAN</span>
          </div>
          <div className="pt-0.5 border-t border-slate-200 flex items-center justify-between text-[10px] font-mono text-slate-800">
            <a href="tel:03007603964" className="hover:text-blue-700 font-bold flex items-center gap-0.5">
              <Phone className="w-2.5 h-2.5 text-emerald-600" />
              03007603964
            </a>
            <a href="tel:03147603964" className="hover:text-blue-700 font-bold flex items-center gap-0.5">
              <Phone className="w-2.5 h-2.5 text-emerald-600" />
              03147603964
            </a>
          </div>
        </div>
      )}
    </aside>
  );
};
