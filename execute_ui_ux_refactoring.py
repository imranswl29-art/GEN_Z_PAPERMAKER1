import os
import re
import subprocess

print("=== Starting Application-Wide UI/UX Refactoring ===")

# =========================================================================
# 1. Update index.html and dist/index.html with Dropdown Styling
# =========================================================================
dropdown_css = """
      /* Unified Dropdown & Multi-Option Popover Styling */
      details > summary {
        list-style: none !important;
      }
      details > summary::-webkit-details-marker {
        display: none !important;
      }
      details[open] > summary {
        filter: brightness(0.92);
      }
      .dropdown-menu-panel {
        position: absolute !important;
        right: 0 !important;
        top: 100% !important;
        margin-top: 4px !important;
        z-index: 100 !important;
        min-width: 14rem !important;
        background-color: #ffffff !important;
        border-radius: 0.75rem !important;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.18), 0 8px 10px -6px rgba(0, 0, 0, 0.1) !important;
        border: 1.5px solid #e2e8f0 !important;
        padding: 0.375rem !important;
      }
      .dropdown-menu-item {
        width: 100% !important;
        display: flex !important;
        align-items: center !important;
        gap: 0.6rem !important;
        padding: 0.5rem 0.75rem !important;
        font-size: 0.75rem !important;
        font-weight: 700 !important;
        color: #334155 !important;
        border-radius: 0.5rem !important;
        text-align: left !important;
        transition: all 0.15s ease !important;
        cursor: pointer !important;
      }
      .dropdown-menu-item:hover {
        background-color: #f1f5f9 !important;
        color: #0f172a !important;
      }
"""

for html_path in ["index.html", "dist/index.html"]:
    if os.path.exists(html_path):
        with open(html_path, "r", encoding="utf-8") as f:
            html = f.read()
        if "dropdown-menu-panel" not in html:
            html = html.replace("</style>", f"{dropdown_css}\n    </style>", 1)
            with open(html_path, "w", encoding="utf-8") as f:
                f.write(html)
            print(f"[✓] Added dropdown styles to {html_path}")
        else:
            print(f"[i] Dropdown styles already in {html_path}")

# =========================================================================
# 2. Refactor assets/index-DAioIUjd.js
# =========================================================================
js_path = "assets/index-DAioIUjd.js"
with open(js_path, "r", encoding="utf-8") as f:
    text = f.read()

orig_len = len(text)
print(f"Loaded {js_path} ({orig_len} chars)")

# -------------------------------------------------------------------------
# A. ZERO URDU IN UI CONTROLS (Complete English Standardization)
# -------------------------------------------------------------------------

# 1. Orientation buttons & titles
text = text.replace('title:"Portrait (Vertical Orientation) - عمودی انداز"', 'title:"Portrait (Vertical Orientation)"')
text = text.replace('title:"Landscape (Horizontal Orientation) - افقی انداز"', 'title:"Landscape (Horizontal Orientation)"')
text = text.replace('children: "Portrait (عمودی)"', 'children: "Portrait"')
text = text.replace('children: "Landscape (افقی)"', 'children: "Landscape"')
text = text.replace('children:"Portrait (عمودی)"', 'children:"Portrait"')
text = text.replace('children:"Landscape (افقی)"', 'children:"Landscape"')

# 2. Auto-calculate positions & toast
text = text.replace('children:"Auto-Calculate Positions (پوزیشنز)"', 'children:"Auto-Calculate Positions"')
text = text.replace('F("تمام طلباء کی پوزیشنز خودکار طور پر کیلکولیٹ ہو گئیں!");', 'F("All student class positions and ranks calculated successfully!");')

# 3. Question Bank Add Modal
text = text.replace('children: "Urdu Nastaliq Statement (اردو سوال):"', 'children: "Urdu Nastaliq Statement (Optional):"')
text = text.replace('placeholder: "مثلاً: یکساں اسراع کی تعریف کریں اور اس کا ایس آئی یونٹ لکھیں۔"', 'placeholder: "e.g. Enter optional Urdu translation or leave blank"')

print("[✓] Zero Urdu in UI controls replaced successfully")

# -------------------------------------------------------------------------
# B. PAPER STUDIO (WK) TOOLBAR REFACTORING
# -------------------------------------------------------------------------
# Find the button cluster in WK starting after input file and ending at Full OMR Sheet
wk_start_marker = 'l.jsx("input",{ref:R,type:"file",accept:"image/*",className:"hidden",onChange:oe}),'
wk_end_marker = 'r&&l.jsxs("button",{type:"button",onClick:r,className:"btn-3d btn-3d-indigo flex items-center gap-1.5 px-3.5 py-2 text-white rounded-xl text-xs font-black cursor-pointer shadow-md",children:[l.jsx(Ru,{className:"w-3.5 h-3.5 text-indigo-100"}),l.jsx("span",{children:"Full OMR Sheet"})]})'

pos_wk_start = text.find(wk_start_marker)
if pos_wk_start != -1:
    pos_wk_end = text.find(wk_end_marker, pos_wk_start)
    if pos_wk_end != -1:
        wk_old_block = text[pos_wk_start + len(wk_start_marker): pos_wk_end + len(wk_end_marker)]
        
        wk_new_block = '''l.jsxs("div",{className:"flex items-center gap-1 bg-slate-100 p-1 rounded-xl border border-slate-200 no-print",children:[l.jsxs("button",{type:"button",onClick:()=>{setPaperOrientation("portrait");setPrintOrientation("portrait");},className:`flex items-center gap-1 px-3 py-1.5 rounded-lg text-xs font-bold transition-all cursor-pointer ${paperOrientation==="portrait"?"bg-white text-blue-700 shadow-xs font-black ring-1 ring-blue-300":"text-slate-600 hover:text-slate-900"}`,title:"Portrait (Vertical Orientation)",children:[l.jsx("span",{children:"📄"}),l.jsx("span",{children:"Portrait"})]}),l.jsxs("button",{type:"button",onClick:()=>{setPaperOrientation("landscape");setPrintOrientation("landscape");},className:`flex items-center gap-1 px-3 py-1.5 rounded-lg text-xs font-bold transition-all cursor-pointer ${paperOrientation==="landscape"?"bg-white text-blue-700 shadow-xs font-black ring-1 ring-blue-300":"text-slate-600 hover:text-slate-900"}`,title:"Landscape (Horizontal Orientation)",children:[l.jsx("span",{children:"📑"}),l.jsx("span",{children:"Landscape"})]})]}),l.jsxs("button",{type:"button",onClick:Z,className:"btn-print-preview",title:"Print Full A4 Paper directly with print preview",children:[l.jsx(SAFE_od,{className:"w-4 h-4 text-emerald-100"}),l.jsx("span",{children:"Print & Preview"})]}),l.jsxs("details",{className:"relative inline-block text-left no-print",children:[l.jsxs("summary",{className:"btn-3d btn-3d-red flex items-center gap-1.5 px-3.5 py-2 text-white rounded-xl text-xs font-black cursor-pointer shadow-xs list-none select-none",title:"Export & Download Options",children:[l.jsx(SAFE_ad,{className:"w-3.5 h-3.5 text-white"}),l.jsx("span",{children:C?"Downloading PDF...":"Downloads ▾"})]}),l.jsxs("div",{className:"dropdown-menu-panel",children:[l.jsxs("button",{type:"button",onClick:e=>{e.currentTarget.closest("details")?.removeAttribute("open");ne();},disabled:C,className:"dropdown-menu-item text-rose-700 hover:bg-rose-50",title:"Download high-resolution PDF",children:[l.jsx(SAFE_ad,{className:"w-3.5 h-3.5 text-rose-600"}),l.jsx("span",{children:C?"Downloading PDF...":"Download PDF (.pdf)"})]}),l.jsxs("button",{type:"button",onClick:e=>{e.currentTarget.closest("details")?.removeAttribute("open");z0(n,o);},className:"dropdown-menu-item text-blue-700 hover:bg-blue-50",title:"Download editable Microsoft Word document",children:[l.jsx(Xu,{className:"w-3.5 h-3.5 text-blue-600"}),l.jsx("span",{children:"Download MS Word (.doc)"})]}),a&&l.jsxs("button",{type:"button",onClick:e=>{e.currentTarget.closest("details")?.removeAttribute("open");a();},className:"dropdown-menu-item text-emerald-700 hover:bg-emerald-50",title:"Answer Key & Solved Sheet",children:[l.jsx(FC,{className:"w-3.5 h-3.5 text-emerald-600"}),l.jsx("span",{children:"Solved Answer Key"})]}),r&&l.jsxs("button",{type:"button",onClick:e=>{e.currentTarget.closest("details")?.removeAttribute("open");r();},className:"dropdown-menu-item text-indigo-700 hover:bg-indigo-50",title:"OMR Bubble Sheet for Assessment",children:[l.jsx(Ru,{className:"w-3.5 h-3.5 text-indigo-600"}),l.jsx("span",{children:"OMR Bubble Sheet"})]})]})]}),l.jsxs("details",{className:"relative inline-block text-left no-print",children:[l.jsxs("summary",{className:"btn-3d btn-3d-whatsapp flex items-center gap-1.5 px-3.5 py-2 text-white rounded-xl text-xs font-black cursor-pointer shadow-xs list-none select-none",title:"Share Exam Paper",children:[l.jsx(K0,{className:"w-3.5 h-3.5 text-white"}),l.jsx("span",{children:"Share ▾"})]}),l.jsxs("div",{className:"dropdown-menu-panel",children:[l.jsxs("button",{type:"button",onClick:e=>{e.currentTarget.closest("details")?.removeAttribute("open");P();},className:"dropdown-menu-item text-emerald-700 hover:bg-emerald-50",title:"Share directly via WhatsApp",children:[l.jsx(K0,{className:"w-3.5 h-3.5 text-emerald-600"}),l.jsx("span",{children:"Share via WhatsApp"})]}),l.jsxs("button",{type:"button",onClick:e=>{e.currentTarget.closest("details")?.removeAttribute("open");te();},className:"dropdown-menu-item text-purple-700 hover:bg-purple-50",title:"Copy Link or Device Share",children:[l.jsx($2,{className:"w-3.5 h-3.5 text-purple-600"}),l.jsx("span",{children:"Copy Link / Share"})]})]})]}),l.jsxs("details",{className:"relative inline-block text-left no-print",children:[l.jsxs("summary",{className:`btn-3d flex items-center gap-1.5 px-3.5 py-2 rounded-xl text-xs font-black cursor-pointer shadow-md list-none select-none ${u?"btn-3d-amber":"btn-3d-indigo text-white"}`,title:"Paper Options & Settings",children:[l.jsx(J2,{className:"w-3.5 h-3.5"}),l.jsx("span",{children:"Settings ⚙"})]}),l.jsxs("div",{className:"dropdown-menu-panel",children:[l.jsxs("button",{type:"button",onClick:e=>{e.currentTarget.closest("details")?.removeAttribute("open");f(!u);},className:"dropdown-menu-item text-slate-800 hover:bg-slate-100",children:[l.jsx(J2,{className:"w-3.5 h-3.5 text-indigo-600"}),l.jsx("span",{children:u?"Done Editing":"Edit Questions & Layout"})]}),l.jsxs("button",{type:"button",onClick:e=>{e.currentTarget.closest("details")?.removeAttribute("open");var Ce;return(Ce=R.current)==null?void 0:Ce.click();},className:"dropdown-menu-item text-amber-800 hover:bg-amber-50",children:[l.jsx(UC,{className:"w-3.5 h-3.5 text-amber-600"}),l.jsx("span",{children:"Upload School Monogram"})]})]})]})'''
        
        text = text[:pos_wk_start + len(wk_start_marker)] + wk_new_block + text[pos_wk_end + len(wk_end_marker):]
        print("[✓] Paper Studio (WK) toolbar refactored into modern unified dropdowns")
    else:
        print("[!] pos_wk_end not found")
else:
    print("[!] pos_wk_start not found")

# -------------------------------------------------------------------------
# C. DATE SHEET GENERATOR (aq) TOOLBAR REFACTORING
# -------------------------------------------------------------------------
ds_old_block = 'l.jsxs("div",{className:"flex flex-wrap items-center gap-2",children:[l.jsxs("button",{type:"button",onClick:T,className:"btn-print-preview",title:"Open browser print dialog for A4 Date Sheet",children:[l.jsx(SAFE_od,{className:"w-4 h-4 text-emerald-100"}),l.jsx("span",{children:"Print & Preview"})]}),l.jsxs("button",{type:"button",onClick:H,disabled:A,className:"btn-3d btn-3d-red flex items-center gap-2 px-4 py-2.5 text-white rounded-xl text-xs font-black cursor-pointer shadow-md disabled:opacity-50",title:"Download high-resolution PDF",children:[A?l.jsx(Sc,{className:"w-4 h-4 animate-spin"}):l.jsx(SAFE_ad,{className:"w-4 h-4"}),l.jsx("span",{children:A?f||"Rendering PDF...":"Download PDF"})]}),l.jsxs("button",{type:"button",onClick:G,className:"btn-3d btn-3d-navy flex items-center gap-2 px-4 py-2.5 text-white rounded-xl text-xs font-black cursor-pointer shadow-md",title:"Download editable Microsoft Word .doc file",children:[l.jsx(Xu,{className:"w-4 h-4 text-blue-200"}),l.jsx("span",{children:"Download Word (.doc)"})]})]})'

ds_new_block = '''l.jsxs("div",{className:"flex flex-wrap items-center gap-2",children:[l.jsxs("button",{type:"button",onClick:T,className:"btn-print-preview",title:"Open browser print dialog for A4 Date Sheet",children:[l.jsx(SAFE_od,{className:"w-4 h-4 text-emerald-100"}),l.jsx("span",{children:"Print & Preview"})]}),l.jsxs("details",{className:"relative inline-block text-left no-print",children:[l.jsxs("summary",{className:"btn-3d btn-3d-red flex items-center gap-2 px-4 py-2 text-white rounded-xl text-xs font-black cursor-pointer shadow-md list-none select-none",title:"Export & Download Options",children:[A?l.jsx(Sc,{className:"w-4 h-4 animate-spin"}):l.jsx(SAFE_ad,{className:"w-4 h-4 text-white"}),l.jsx("span",{children:A?f||"Rendering...":"Downloads ▾"})]}),l.jsxs("div",{className:"dropdown-menu-panel",children:[l.jsxs("button",{type:"button",onClick:e=>{e.currentTarget.closest("details")?.removeAttribute("open");H();},disabled:A,className:"dropdown-menu-item text-rose-700 hover:bg-rose-50",children:[l.jsx(SAFE_ad,{className:"w-3.5 h-3.5 text-rose-600"}),l.jsx("span",{children:"Download PDF (.pdf)"})]}),l.jsxs("button",{type:"button",onClick:e=>{e.currentTarget.closest("details")?.removeAttribute("open");G();},className:"dropdown-menu-item text-blue-700 hover:bg-blue-50",children:[l.jsx(Xu,{className:"w-3.5 h-3.5 text-blue-600"}),l.jsx("span",{children:"Download Word (.doc)"})]})]})]})]})'''

if ds_old_block in text:
    text = text.replace(ds_old_block, ds_new_block, 1)
    print("[✓] Date Sheet Generator toolbar refactored into compact dropdown")
else:
    print("[!] ds_old_block not found")

# -------------------------------------------------------------------------
# D. RESULT CARD & MARKSHEET (lq) SINGLE CARD VIEW TOOLBAR
# -------------------------------------------------------------------------
rc_single_old = 'a==="singleCard"&&P&&l.jsxs(l.Fragment,{children:[l.jsxs("button",{type:"button",onClick:()=>ue(P),className:"btn-print-preview",title:"Print single student result card on standard A4",children:[l.jsx(SAFE_od,{className:"w-4 h-4 text-emerald-100"}),l.jsx("span",{children:"Print & Preview"})]}),l.jsxs("button",{type:"button",onClick:()=>Ne(P),disabled:f,className:"btn-3d btn-3d-red flex items-center gap-2 px-4 py-2.5 text-white rounded-xl text-xs font-black cursor-pointer shadow-md disabled:opacity-50",title:"Download single student result card PDF",children:[f?l.jsx(Sc,{className:"w-4 h-4 animate-spin"}):l.jsx(SAFE_ad,{className:"w-4 h-4"}),l.jsx("span",{children:f?m||"Rendering...":"Download Card (PDF)"})]}),l.jsxs("button",{type:"button",onClick:()=>Le(P),className:"btn-3d btn-3d-navy flex items-center gap-2 px-4 py-2.5 text-white rounded-xl text-xs font-black cursor-pointer shadow-md",title:"Download single student result card Word (.doc)",children:[l.jsx(Xu,{className:"w-4 h-4 text-blue-200"}),l.jsx("span",{children:"Download Card (.doc)"})]}),l.jsxs("button",{type:"button",onClick:printAllCardsAction,className:"btn-3d btn-3d-purple flex items-center gap-1.5 px-3.5 py-2.5 text-white rounded-xl text-xs font-black cursor-pointer shadow-md",title:"Print ALL students result cards in one go",children:[l.jsx(SAFE_od,{className:"w-4 h-4 text-purple-200"}),l.jsx("span",{children:"Print ALL Cards"})]}),l.jsxs("div",{className:"flex items-center gap-1 bg-slate-100 p-1 rounded-xl border border-slate-200 no-print",children:[  l.jsxs("button",{type:"button",onClick:()=>{setMsOrientation("portrait");setPrintOrientation("portrait");},className:`flex items-center gap-1 px-3 py-1.5 rounded-lg text-xs font-bold transition-all cursor-pointer ${msOrientation==="portrait"?"bg-white text-blue-700 shadow-xs font-black ring-1 ring-blue-300":"text-slate-600 hover:text-slate-900"}`,title:"Portrait (Vertical)",children:[l.jsx("span",{children:"📄"}),l.jsx("span",{children:"Portrait"})]}),  l.jsxs("button",{type:"button",onClick:()=>{setMsOrientation("landscape");setPrintOrientation("landscape");},className:`flex items-center gap-1 px-3 py-1.5 rounded-lg text-xs font-bold transition-all cursor-pointer ${msOrientation==="landscape"?"bg-white text-blue-700 shadow-xs font-black ring-1 ring-blue-300":"text-slate-600 hover:text-slate-900"}`,title:"Landscape (Horizontal)",children:[l.jsx("span",{children:"📑"}),l.jsx("span",{children:"Landscape"})]})]})]})'

rc_single_new = '''a==="singleCard"&&P&&l.jsxs(l.Fragment,{children:[l.jsxs("div",{className:"flex items-center gap-1 bg-slate-100 p-1 rounded-xl border border-slate-200 no-print",children:[l.jsxs("button",{type:"button",onClick:()=>{setMsOrientation("portrait");setPrintOrientation("portrait");},className:`flex items-center gap-1 px-3 py-1.5 rounded-lg text-xs font-bold transition-all cursor-pointer ${msOrientation==="portrait"?"bg-white text-blue-700 shadow-xs font-black ring-1 ring-blue-300":"text-slate-600 hover:text-slate-900"}`,title:"Portrait (Vertical Orientation)",children:[l.jsx("span",{children:"📄"}),l.jsx("span",{children:"Portrait"})]}),l.jsxs("button",{type:"button",onClick:()=>{setMsOrientation("landscape");setPrintOrientation("landscape");},className:`flex items-center gap-1 px-3 py-1.5 rounded-lg text-xs font-bold transition-all cursor-pointer ${msOrientation==="landscape"?"bg-white text-blue-700 shadow-xs font-black ring-1 ring-blue-300":"text-slate-600 hover:text-slate-900"}`,title:"Landscape (Horizontal Orientation)",children:[l.jsx("span",{children:"📑"}),l.jsx("span",{children:"Landscape"})]})]}),l.jsxs("button",{type:"button",onClick:()=>ue(P),className:"btn-print-preview",title:"Print single student result card on standard A4",children:[l.jsx(SAFE_od,{className:"w-4 h-4 text-emerald-100"}),l.jsx("span",{children:"Print & Preview"})]}),l.jsxs("details",{className:"relative inline-block text-left no-print",children:[l.jsxs("summary",{className:"btn-3d btn-3d-red flex items-center gap-2 px-4 py-2 text-white rounded-xl text-xs font-black cursor-pointer shadow-md list-none select-none",title:"Export & Download Options",children:[f?l.jsx(Sc,{className:"w-4 h-4 animate-spin"}):l.jsx(SAFE_ad,{className:"w-4 h-4 text-white"}),l.jsx("span",{children:f?m||"Rendering...":"Downloads ▾"})]}),l.jsxs("div",{className:"dropdown-menu-panel",children:[l.jsxs("button",{type:"button",onClick:e=>{e.currentTarget.closest("details")?.removeAttribute("open");Ne(P);},disabled:f,className:"dropdown-menu-item text-rose-700 hover:bg-rose-50",title:"Download single student result card PDF",children:[l.jsx(SAFE_ad,{className:"w-3.5 h-3.5 text-rose-600"}),l.jsx("span",{children:"Download Card (PDF)"})]}),l.jsxs("button",{type:"button",onClick:e=>{e.currentTarget.closest("details")?.removeAttribute("open");Le(P);},className:"dropdown-menu-item text-blue-700 hover:bg-blue-50",title:"Download single student result card Word (.doc)",children:[l.jsx(Xu,{className:"w-3.5 h-3.5 text-blue-600"}),l.jsx("span",{children:"Download Card (.doc)"})]}),l.jsxs("button",{type:"button",onClick:e=>{e.currentTarget.closest("details")?.removeAttribute("open");printAllCardsAction();},className:"dropdown-menu-item text-purple-700 hover:bg-purple-50",title:"Print all students result cards in one go",children:[l.jsx(SAFE_od,{className:"w-3.5 h-3.5 text-purple-600"}),l.jsx("span",{children:"Print ALL Cards"})]})]})]})]})'''

if rc_single_old in text:
    text = text.replace(rc_single_old, rc_single_new, 1)
    print("[✓] Result Card single card toolbar refactored into dropdown")
else:
    print("[!] rc_single_old not found")

# -------------------------------------------------------------------------
# E. RESULT CARD & MARKSHEET (lq) MASTER SHEET VIEW TOOLBAR
# -------------------------------------------------------------------------
rc_master_start = 'a==="masterSheet"&&l.jsxs(l.Fragment,{children:[l.jsxs("button",{type:"button",onClick:Ce,className:"btn-print-preview",title:"Print full class master sheet / broadsheet",children:[l.jsx(SAFE_od,{className:"w-4 h-4 text-emerald-100"}),l.jsx("span",{children:"Print & Preview"})]}),'
rc_master_end = 'l.jsxs("button",{type:"button",onClick:Y,className:"btn-3d btn-3d-navy flex items-center gap-2 px-4 py-2.5 text-white rounded-xl text-xs font-black cursor-pointer shadow-md",children:[l.jsx(Xu,{className:"w-4 h-4 text-blue-200"}),l.jsx("span",{children:"Export Master (.doc)"})]})]})'

pos_m_start = text.find(rc_master_start)
if pos_m_start != -1:
    pos_m_end = text.find(rc_master_end, pos_m_start)
    if pos_m_end != -1:
        rc_master_new = '''a==="masterSheet"&&l.jsxs(l.Fragment,{children:[l.jsxs("div",{className:"flex items-center gap-1 bg-slate-100 p-1 rounded-xl border border-slate-200 mr-1 no-print",children:[l.jsxs("button",{type:"button",onClick:()=>{setMsOrientation("portrait");setPrintOrientation("portrait");},className:`flex items-center gap-1 px-3 py-1.5 rounded-lg text-xs font-bold transition-all cursor-pointer ${msOrientation==="portrait"?"bg-white text-blue-700 shadow-xs font-black ring-1 ring-blue-300":"text-slate-600 hover:text-slate-900"}`,title:"Portrait (Vertical Orientation)",children:[l.jsx("span",{children:"📄"}),l.jsx("span",{children:"Portrait"})]}),l.jsxs("button",{type:"button",onClick:()=>{setMsOrientation("landscape");setPrintOrientation("landscape");},className:`flex items-center gap-1 px-3 py-1.5 rounded-lg text-xs font-bold transition-all cursor-pointer ${msOrientation==="landscape"?"bg-white text-blue-700 shadow-xs font-black ring-1 ring-blue-300":"text-slate-600 hover:text-slate-900"}`,title:"Landscape (Horizontal Orientation)",children:[l.jsx("span",{children:"📑"}),l.jsx("span",{children:"Landscape"})]})]}),l.jsxs("button",{type:"button",onClick:Ce,className:"btn-print-preview",title:"Print full class master sheet / broadsheet",children:[l.jsx(SAFE_od,{className:"w-4 h-4 text-emerald-100"}),l.jsx("span",{children:"Print & Preview"})]}),l.jsxs("div",{className:"flex items-center gap-2 bg-slate-50 px-3 py-1.5 rounded-xl border border-slate-200 shadow-2xs mr-1",children:[l.jsx("span",{className:"text-xs font-black text-slate-600 uppercase tracking-wide hidden sm:inline",children:"Filter Section:"}),l.jsxs("select",{value:m_sec,onChange:S=>setM_sec(S.target.value),className:"px-2.5 py-1 rounded-lg border border-slate-300 font-bold text-xs bg-white focus:outline-none focus:ring-2 focus:ring-blue-500 shadow-xs cursor-pointer",children:[l.jsx("option",{value:"all",children:"All Sections (A, B, C, D)"}),l.jsx("option",{value:"A",children:"Section A"}),l.jsx("option",{value:"B",children:"Section B"}),l.jsx("option",{value:"C",children:"Section C"}),l.jsx("option",{value:"D",children:"Section D"})]})]}),l.jsxs("details",{className:"relative inline-block text-left no-print",children:[l.jsxs("summary",{className:"btn-3d btn-3d-emerald flex items-center gap-2 px-4 py-2 text-white rounded-xl text-xs font-black cursor-pointer shadow-md list-none select-none",title:"Export Options",children:[f?l.jsx(Sc,{className:"w-4 h-4 animate-spin"}):l.jsx(SAFE_ad,{className:"w-4 h-4 text-emerald-100"}),l.jsx("span",{children:f?m||"Rendering...":"Export Options ▾"})]}),l.jsxs("div",{className:"dropdown-menu-panel",children:[l.jsxs("button",{type:"button",onClick:e=>{e.currentTarget.closest("details")?.removeAttribute("open");k();},disabled:f,className:"dropdown-menu-item text-rose-700 hover:bg-rose-50",title:"Export Master Marksheet PDF",children:[l.jsx(SAFE_ad,{className:"w-3.5 h-3.5 text-rose-600"}),l.jsx("span",{children:"Export Master (PDF)"})]}),l.jsxs("button",{type:"button",onClick:e=>{e.currentTarget.closest("details")?.removeAttribute("open");exportMasterGazetteToExcel(R,r,m_sec);},className:"dropdown-menu-item text-emerald-700 hover:bg-emerald-50",title:"Download Consolidated Master Marksheet in Excel (.xls)",children:[l.jsx(SAFE_sd,{className:"w-3.5 h-3.5 text-emerald-600"}),l.jsx("span",{children:"Download Excel (.xls)"})]}),l.jsxs("button",{type:"button",onClick:e=>{e.currentTarget.closest("details")?.removeAttribute("open");Y();},className:"dropdown-menu-item text-blue-700 hover:bg-blue-50",title:"Export Master Document in Word (.doc)",children:[l.jsx(Xu,{className:"w-3.5 h-3.5 text-blue-600"}),l.jsx("span",{children:"Export Master (.doc)"})]})]})]})]})'''
        text = text[:pos_m_start] + rc_master_new + text[pos_m_end + len(rc_master_end):]
        print("[✓] Result Card master sheet toolbar refactored into dropdown")
    else:
        print("[!] pos_m_end not found")
else:
    print("[!] pos_m_start not found")

# -------------------------------------------------------------------------
# F. RESULT CARD & MARKSHEET (lq) MARKS ENTRY SHEET ACTION BAR
# -------------------------------------------------------------------------
rc_editor_bar_start = 'l.jsxs("button",{type:"button",onClick:()=>fileInputRef.current&&fileInputRef.current.click(),className:"btn-3d bg-slate-800 hover:bg-slate-700 border border-slate-600 flex items-center gap-1.5 px-3 py-1.5 text-white rounded-xl text-xs font-black cursor-pointer shadow-sm",title:"Import student marks from Excel / CSV",children:[l.jsx("span",{children:"📥"}),l.jsx("span",{children:"Import Marks (CSV/Excel)"})]}),'
rc_editor_bar_end = 'l.jsxs("button",{type:"button",onClick:()=>exportWholeSchoolConsolidatedGazette([R],r),className:"btn-3d bg-purple-700 hover:bg-purple-600 flex items-center gap-1.5 px-3.5 py-1.5 text-white rounded-xl text-xs font-black cursor-pointer shadow-sm hover:brightness-110",title:"Export Whole School Consolidated Gazette across multiple grades",children:[l.jsx("span",{children:"🏫"}),l.jsx("span",{children:"Whole School Gazette"})]})  ]})'

pos_ed_start = text.find(rc_editor_bar_start)
if pos_ed_start != -1:
    pos_ed_end = text.find(rc_editor_bar_end, pos_ed_start)
    if pos_ed_end != -1:
        rc_editor_new = '''l.jsxs("button",{type:"button",onClick:autoCalculateRanks,className:"btn-3d btn-3d-amber flex items-center gap-1.5 px-3.5 py-1.5 text-slate-950 rounded-xl text-xs font-black cursor-pointer shadow-sm hover:brightness-110",title:"Auto calculate student class positions (1st, 2nd, 3rd) based on total marks",children:[l.jsx("span",{children:"⚡"}),l.jsx("span",{children:"Auto-Calculate Positions"})]}),  l.jsxs("details",{className:"relative inline-block text-left no-print",children:[l.jsxs("summary",{className:"btn-3d bg-slate-800 hover:bg-slate-700 border border-slate-600 flex items-center gap-1.5 px-3.5 py-1.5 text-white rounded-xl text-xs font-black cursor-pointer shadow-sm list-none select-none",title:"Data Import and Export Controls",children:[l.jsx("span",{children:"📊"}),l.jsx("span",{children:"Data & Export ▾"})]}),l.jsxs("div",{className:"dropdown-menu-panel",children:[l.jsxs("button",{type:"button",onClick:e=>{e.currentTarget.closest("details")?.removeAttribute("open");fileInputRef.current&&fileInputRef.current.click();},className:"dropdown-menu-item text-slate-700 hover:bg-slate-50",title:"Import student marks from Excel or CSV file",children:[l.jsx("span",{children:"📥"}),l.jsx("span",{children:"Import Marks (CSV/Excel)"})]}),l.jsxs("button",{type:"button",onClick:e=>{e.currentTarget.closest("details")?.removeAttribute("open");exportMasterGazetteToExcel(R,r,m_sec);},className:"dropdown-menu-item text-emerald-700 hover:bg-emerald-50",title:"Download complete class marksheet data in Excel (.xls) format",children:[l.jsx("span",{children:"📊"}),l.jsx("span",{children:"Class Excel (.xls)"})]}),l.jsxs("button",{type:"button",onClick:e=>{e.currentTarget.closest("details")?.removeAttribute("open");exportWholeSchoolConsolidatedGazette([R],r);},className:"dropdown-menu-item text-purple-700 hover:bg-purple-50",title:"Export Whole School Consolidated Gazette across multiple grades",children:[l.jsx("span",{children:"🏫"}),l.jsx("span",{children:"Whole School Gazette"})]})]})]})  ]})'''
        
        # Also clean up the preceding "Data Controls:" label if needed
        text = text[:pos_ed_start] + rc_editor_new + text[pos_ed_end + len(rc_editor_bar_end):]
        print("[✓] Result Card marks table actions refactored into compact Data & Export dropdown")
    else:
        print("[!] pos_ed_end not found")
else:
    print("[!] pos_ed_start not found")

# -------------------------------------------------------------------------
# G. NOTES (ClassNotesView) STEP 4 TOOLBAR REFACTORING
# -------------------------------------------------------------------------
notes_bar_start = '// Right: Three 3D Export Buttons (Direct PDF Download, Word .docx, Direct Print)'
pos_nt_comment = text.find(notes_bar_start)
if pos_nt_comment != -1:
    # Find button 1 start
    b1_marker = 'l.jsxs("button", {                    type: "button",                    disabled: isExportingPdf,                    onClick: handleDownloadPDF,'
    pos_b1 = text.find(b1_marker, pos_nt_comment)
    # Find end after handlePrintNotes
    print_marker = 'onClick: handlePrintNotes,                    className: "btn-print-preview",                    title: "Print Solved Notes directly or save via browser preview",'
    pos_pr = text.find(print_marker, pos_b1)
    if pos_b1 != -1 and pos_pr != -1:
        # Find end of print button: children: [ ... ] })
        end_pr = text.find('children: [                      l.jsx(SAFE_od, { className: "w-4 h-4 text-emerald-100" }),                      l.jsx("span", { children: "Print Notes" })                    ]                  })', pos_pr)
        if end_pr != -1:
            end_pr_total = end_pr + len('children: [                      l.jsx(SAFE_od, { className: "w-4 h-4 text-emerald-100" }),                      l.jsx("span", { children: "Print Notes" })                    ]                  })')
            
            notes_new_block = '''l.jsxs("div", {
                    className: "flex items-center gap-1 bg-slate-100 p-1 rounded-xl border border-slate-200 no-print",
                    children: [
                      l.jsxs("button", {
                        type: "button",
                        onClick: () => { setNotesOrientation("portrait"); setPrintOrientation("portrait"); },
                        className: `flex items-center gap-1 px-3 py-1.5 rounded-lg text-xs font-bold transition-all cursor-pointer ${notesOrientation === "portrait" ? "bg-white text-blue-700 shadow-xs font-black ring-1 ring-blue-300" : "text-slate-600 hover:text-slate-900"}`,
                        title: "Portrait (Vertical Orientation)",
                        children: [l.jsx("span", { children: "📄" }), l.jsx("span", { children: "Portrait" })]
                      }),
                      l.jsxs("button", {
                        type: "button",
                        onClick: () => { setNotesOrientation("landscape"); setPrintOrientation("landscape"); },
                        className: `flex items-center gap-1 px-3 py-1.5 rounded-lg text-xs font-bold transition-all cursor-pointer ${notesOrientation === "landscape" ? "bg-white text-blue-700 shadow-xs font-black ring-1 ring-blue-300" : "text-slate-600 hover:text-slate-900"}`,
                        title: "Landscape (Horizontal Orientation)",
                        children: [l.jsx("span", { children: "📑" }), l.jsx("span", { children: "Landscape" })]
                      })
                    ]
                  }),
                  l.jsxs("button", {
                    type: "button",
                    onClick: handlePrintNotes,
                    className: "btn-print-preview",
                    title: "Print Solved Notes directly or save via browser preview",
                    children: [
                      l.jsx(SAFE_od, { className: "w-4 h-4 text-emerald-100" }),
                      l.jsx("span", { children: "Print Notes" })
                    ]
                  }),
                  l.jsxs("details", {
                    className: "relative inline-block text-left no-print",
                    children: [
                      l.jsxs("summary", {
                        className: "min-h-[44px] max-h-[48px] inline-flex items-center gap-2 px-4 py-2.5 bg-gradient-to-r from-rose-600 to-red-600 hover:from-rose-500 hover:to-red-500 text-white rounded-xl text-xs font-bold cursor-pointer border-b-4 border-rose-800 shadow-md list-none select-none",
                        title: "Downloads & Exports",
                        children: [
                          isExportingPdf ? l.jsx(Sc, { className: "w-4 h-4 animate-spin text-white" }) : l.jsx(SAFE_ad, { className: "w-4 h-4 text-rose-100" }),
                          l.jsx("span", { children: isExportingPdf ? "Generating..." : "Downloads ▾" })
                        ]
                      }),
                      l.jsxs("div", {
                        className: "dropdown-menu-panel",
                        children: [
                          l.jsxs("button", {
                            type: "button",
                            disabled: isExportingPdf,
                            onClick: e => { e.currentTarget.closest("details")?.removeAttribute("open"); handleDownloadPDF(); },
                            className: "dropdown-menu-item text-rose-700 hover:bg-rose-50",
                            title: `Download Solved Notes as PDF Document (${effectiveLangMode.toUpperCase()})`,
                            children: [
                              l.jsx(SAFE_ad, { className: "w-3.5 h-3.5 text-rose-600" }),
                              l.jsx("span", { children: "Download PDF (.pdf)" })
                            ]
                          }),
                          l.jsxs("button", {
                            type: "button",
                            onClick: e => { e.currentTarget.closest("details")?.removeAttribute("open"); exportNotesToWordDoc(notesData, selectedClass, currentSubject.nameEn, currentSubject.nameUr, effectiveLangMode, currentUser && currentUser.branding); },
                            className: "dropdown-menu-item text-blue-700 hover:bg-blue-50",
                            title: `Download Solved Notes as MS Word Document (${effectiveLangMode.toUpperCase()})`,
                            children: [
                              l.jsx(Xu, { className: "w-3.5 h-3.5 text-blue-600" }),
                              l.jsx("span", { children: "Download Word (.docx)" })
                            ]
                          })
                        ]
                      })
                    ]
                  }),
                  l.jsxs("button", {
                    type: "button",
                    disabled: isAiGenerating,
                    onClick: handleGenerateAiNotes,
                    className: "min-h-[44px] max-h-[48px] inline-flex items-center gap-2 px-4 py-2.5 bg-gradient-to-r from-purple-700 via-indigo-700 to-blue-700 hover:from-purple-600 hover:to-indigo-600 text-white rounded-xl text-xs font-black cursor-pointer shadow-md hover:shadow-lg active:scale-95 transition-all disabled:opacity-60",
                    title: "Generate or refresh 100% comprehensive solved notes with Gemini AI",
                    children: [
                      isAiGenerating ? l.jsx(Sc, { className: "w-4 h-4 animate-spin text-purple-200" }) : l.jsx("span", { children: "✨" }),
                      l.jsx("span", { children: isAiGenerating ? "Generating..." : "AI Solved Notes (Gemini)" })
                    ]
                  })'''
            
            text = text[:pos_b1] + notes_new_block + text[end_pr_total:]
            print("[✓] Notes Step 4 toolbar refactored into compact dropdown & clean orientation pills")
        else:
            print("[!] end_pr not found")
    else:
        print("[!] pos_b1 or pos_pr not found")
else:
    print("[!] notes_bar_start not found")

# -------------------------------------------------------------------------
# H. SAVED PAPERS CARD ACTIONS REFACTORING
# -------------------------------------------------------------------------
saved_old = 'l.jsxs("div",{className:"flex flex-wrap items-center gap-2 pt-2.5 border-t border-slate-100",children:[l.jsxs("button",{onClick:()=>qe(ge),className:"btn-3d btn-3d-blue flex items-center justify-center gap-1.5 px-3.5 py-1.5 text-white rounded-lg text-xs font-black shadow-xs cursor-pointer shrink-0 whitespace-nowrap min-w-[100px]",title:"View, edit, and print question paper on A4 sheet",children:[l.jsx(SAFE_od,{className:"w-3.5 h-3.5 text-blue-100 shrink-0"}),l.jsx("span",{className:"whitespace-nowrap",children:"View & Print"})]}),l.jsxs("button",{onClick:()=>z0(ge),className:"btn-3d btn-3d-indigo flex items-center justify-center gap-1 px-2.5 py-1.5 text-white rounded-lg text-xs font-black shadow-xs cursor-pointer shrink-0 whitespace-nowrap",title:"Download MS Word (.doc)",children:[l.jsx(Xu,{className:"w-3.5 h-3.5 text-indigo-100"}),l.jsx("span",{children:"Word"})]}),l.jsx("button",{onClick:()=>{E(ge),te(!0)},className:"btn-3d btn-3d-emerald px-2.5 py-1.5 text-white rounded-lg text-xs font-black shadow-xs cursor-pointer shrink-0 whitespace-nowrap",title:"View Answer Key",children:"Answer Key"}),l.jsx("button",{onClick:()=>{E(ge),T(!0)},className:"btn-3d btn-3d-purple px-2.5 py-1.5 text-white rounded-lg text-xs font-black shadow-xs cursor-pointer shrink-0 whitespace-nowrap",title:"View OMR Bubble Sheet",children:"Bubble Sheet"}),l.jsxs("button",{type:"button",onClick:()=>{window.confirm(`Are you sure you want to delete "${ge.header.subjectName}" paper?`)&&St(ge.id)},className:"flex items-center gap-1 px-2.5 py-1.5 bg-rose-600 hover:bg-rose-700 text-white rounded-lg text-xs font-bold shadow-xs cursor-pointer transition-colors",title:"Delete this saved paper",children:[l.jsx(Ql,{className:"w-3.5 h-3.5"}),l.jsx("span",{children:"Delete"})]})]})'

saved_new = '''l.jsxs("div",{className:"flex items-center justify-between gap-2 pt-2.5 border-t border-slate-100",children:[l.jsxs("button",{onClick:()=>qe(ge),className:"btn-3d btn-3d-blue flex items-center justify-center gap-1.5 px-3.5 py-1.5 text-white rounded-lg text-xs font-black shadow-xs cursor-pointer flex-1",title:"View, edit, and print question paper on A4 sheet",children:[l.jsx(SAFE_od,{className:"w-3.5 h-3.5 text-blue-100 shrink-0"}),l.jsx("span",{className:"whitespace-nowrap",children:"View & Print"})]}),l.jsxs("details",{className:"relative inline-block text-left no-print",children:[l.jsxs("summary",{className:"btn-3d btn-3d-indigo flex items-center justify-center gap-1 px-3 py-1.5 text-white rounded-lg text-xs font-black shadow-xs cursor-pointer list-none select-none",title:"Export & Paper Options",children:[l.jsx("span",{children:"Options ▾"})]}),l.jsxs("div",{className:"dropdown-menu-panel",children:[l.jsxs("button",{type:"button",onClick:e=>{e.currentTarget.closest("details")?.removeAttribute("open");z0(ge);},className:"dropdown-menu-item text-blue-700 hover:bg-blue-50",title:"Download MS Word (.doc)",children:[l.jsx(Xu,{className:"w-3.5 h-3.5 text-blue-600"}),l.jsx("span",{children:"Download Word (.doc)"})]}),l.jsxs("button",{type:"button",onClick:e=>{e.currentTarget.closest("details")?.removeAttribute("open");E(ge);te(!0);},className:"dropdown-menu-item text-emerald-700 hover:bg-emerald-50",title:"View Answer Key",children:[l.jsx(FC,{className:"w-3.5 h-3.5 text-emerald-600"}),l.jsx("span",{children:"View Answer Key"})]}),l.jsxs("button",{type:"button",onClick:e=>{e.currentTarget.closest("details")?.removeAttribute("open");E(ge);T(!0);},className:"dropdown-menu-item text-purple-700 hover:bg-purple-50",title:"View OMR Bubble Sheet",children:[l.jsx(Ru,{className:"w-3.5 h-3.5 text-purple-600"}),l.jsx("span",{children:"View Bubble Sheet"})]}),l.jsxs("button",{type:"button",onClick:e=>{e.currentTarget.closest("details")?.removeAttribute("open");window.confirm(`Are you sure you want to delete "${ge.header.subjectName}" paper?`)&&St(ge.id);},className:"dropdown-menu-item text-rose-700 hover:bg-rose-50 border-t border-slate-100",title:"Delete this saved paper",children:[l.jsx(Ql,{className:"w-3.5 h-3.5 text-rose-600"}),l.jsx("span",{children:"Delete Paper"})]})]})]})]})'''

if saved_old in text:
    text = text.replace(saved_old, saved_new, 1)
    print("[✓] Saved papers cards refactored into clean View & Print + Options dropdown")
else:
    print("[!] saved_old not found")

# Save refactored bundle
with open(js_path, "w", encoding="utf-8") as f:
    f.write(text)

print(f"Saved {js_path} (new length: {len(text)})")

# Test syntax with node --check
res = subprocess.run(["node", "--check", js_path], capture_output=True, text=True)
if res.returncode == 0:
    print("[✓] node --check passed for assets/index-DAioIUjd.js")
else:
    print("[X] node --check failed:")
    print(res.stderr[:600])
    exit(1)

print("=== Refactoring Execution Complete ===")
