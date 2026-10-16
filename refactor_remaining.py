import os
import subprocess

js_path = "assets/index-DAioIUjd.js"
with open(js_path, "r", encoding="utf-8") as f:
    text = f.read()

print("Loaded bundle, length:", len(text))

# -------------------------------------------------------------------------
# 1. Result Card singleCard toolbar: from p1 to p2
# -------------------------------------------------------------------------
p1 = text.find('a==="singleCard"&&P&&')
p2 = text.find(',a==="masterSheet"', p1)

if p1 != -1 and p2 != -1:
    print("Found singleCard block at", p1, p2)
    single_new = '''a==="singleCard"&&P&&l.jsxs(l.Fragment,{children:[l.jsxs("div",{className:"flex items-center gap-1 bg-slate-100 p-1 rounded-xl border border-slate-200 no-print",children:[l.jsxs("button",{type:"button",onClick:()=>{setMsOrientation("portrait");setPrintOrientation("portrait");},className:`flex items-center gap-1 px-3 py-1.5 rounded-lg text-xs font-bold transition-all cursor-pointer ${msOrientation==="portrait"?"bg-white text-blue-700 shadow-xs font-black ring-1 ring-blue-300":"text-slate-600 hover:text-slate-900"}`,title:"Portrait (Vertical Orientation)",children:[l.jsx("span",{children:"📄"}),l.jsx("span",{children:"Portrait"})]}),l.jsxs("button",{type:"button",onClick:()=>{setMsOrientation("landscape");setPrintOrientation("landscape");},className:`flex items-center gap-1 px-3 py-1.5 rounded-lg text-xs font-bold transition-all cursor-pointer ${msOrientation==="landscape"?"bg-white text-blue-700 shadow-xs font-black ring-1 ring-blue-300":"text-slate-600 hover:text-slate-900"}`,title:"Landscape (Horizontal Orientation)",children:[l.jsx("span",{children:"📑"}),l.jsx("span",{children:"Landscape"})]})]}),l.jsxs("button",{type:"button",onClick:()=>ue(P),className:"btn-print-preview",title:"Print single student result card on standard A4",children:[l.jsx(SAFE_od,{className:"w-4 h-4 text-emerald-100"}),l.jsx("span",{children:"Print & Preview"})]}),l.jsxs("details",{className:"relative inline-block text-left no-print",children:[l.jsxs("summary",{className:"btn-3d btn-3d-red flex items-center gap-2 px-4 py-2 text-white rounded-xl text-xs font-black cursor-pointer shadow-md list-none select-none",title:"Export & Download Options",children:[f?l.jsx(Sc,{className:"w-4 h-4 animate-spin"}):l.jsx(SAFE_ad,{className:"w-4 h-4 text-white"}),l.jsx("span",{children:f?m||"Rendering...":"Downloads ▾"})]}),l.jsxs("div",{className:"dropdown-menu-panel",children:[l.jsxs("button",{type:"button",onClick:e=>{e.currentTarget.closest("details")?.removeAttribute("open");Ne(P);},disabled:f,className:"dropdown-menu-item text-rose-700 hover:bg-rose-50",title:"Download single student result card PDF",children:[l.jsx(SAFE_ad,{className:"w-3.5 h-3.5 text-rose-600"}),l.jsx("span",{children:"Download Card (PDF)"})]}),l.jsxs("button",{type:"button",onClick:e=>{e.currentTarget.closest("details")?.removeAttribute("open");Le(P);},className:"dropdown-menu-item text-blue-700 hover:bg-blue-50",title:"Download single student result card Word (.doc)",children:[l.jsx(Xu,{className:"w-3.5 h-3.5 text-blue-600"}),l.jsx("span",{children:"Download Card (.doc)"})]}),l.jsxs("button",{type:"button",onClick:e=>{e.currentTarget.closest("details")?.removeAttribute("open");printAllCardsAction();},className:"dropdown-menu-item text-purple-700 hover:bg-purple-50",title:"Print all students result cards in one go",children:[l.jsx(SAFE_od,{className:"w-3.5 h-3.5 text-purple-600"}),l.jsx("span",{children:"Print ALL Cards"})]})]})]})]})}'''
    text = text[:p1] + single_new + text[p2:]
    print("[✓] Replaced singleCard block")
else:
    print("[!] Failed to find singleCard block")

# -------------------------------------------------------------------------
# 2. Result card editor: from p3 to p4
# -------------------------------------------------------------------------
p3 = text.find('l.jsxs("button",{type:"button",onClick:()=>fileInputRef.current')
p4 = text.find(',l.jsxs("div",{className:"card-3d p-5 sm:p-6', p3)

if p3 != -1 and p4 != -1:
    print("Found editor action bar block at", p3, p4)
    # Also include the preceding "Data Controls:" container:
    data_ctrl_start = text.rfind('l.jsxs("div",{className:"flex items-center gap-2",children:[l.jsxs("div",{className:"flex items-center gap-1.5",children:[l.jsx(o8,{className:"w-4 h-4 text-emerald-600"}),l.jsx("span",{className:"font-black text-xs text-slate-800 uppercase tracking-wide",children:"Data Controls:"})]})', 0, p3)
    
    if data_ctrl_start != -1:
        replace_start = data_ctrl_start
    else:
        replace_start = p3
        
    editor_new = '''l.jsxs("div",{className:"flex items-center gap-2 flex-wrap",children:[l.jsxs("button",{type:"button",onClick:autoCalculateRanks,className:"btn-3d btn-3d-amber flex items-center gap-1.5 px-3.5 py-1.5 text-slate-950 rounded-xl text-xs font-black cursor-pointer shadow-sm hover:brightness-110",title:"Auto calculate student class positions (1st, 2nd, 3rd) based on total marks",children:[l.jsx("span",{children:"⚡"}),l.jsx("span",{children:"Auto-Calculate Positions"})]}),l.jsxs("details",{className:"relative inline-block text-left no-print",children:[l.jsxs("summary",{className:"btn-3d bg-slate-800 hover:bg-slate-700 border border-slate-600 flex items-center gap-1.5 px-3.5 py-1.5 text-white rounded-xl text-xs font-black cursor-pointer shadow-sm list-none select-none",title:"Data Import and Export Controls",children:[l.jsx("span",{children:"📊"}),l.jsx("span",{children:"Data & Export ▾"})]}),l.jsxs("div",{className:"dropdown-menu-panel",children:[l.jsxs("button",{type:"button",onClick:e=>{e.currentTarget.closest("details")?.removeAttribute("open");fileInputRef.current&&fileInputRef.current.click();},className:"dropdown-menu-item text-slate-700 hover:bg-slate-50",title:"Import student marks from Excel or CSV file",children:[l.jsx("span",{children:"📥"}),l.jsx("span",{children:"Import Marks (CSV/Excel)"})]}),l.jsxs("button",{type:"button",onClick:e=>{e.currentTarget.closest("details")?.removeAttribute("open");exportMasterGazetteToExcel(R,r,m_sec);},className:"dropdown-menu-item text-emerald-700 hover:bg-emerald-50",title:"Download complete class marksheet data in Excel (.xls) format",children:[l.jsx("span",{children:"📊"}),l.jsx("span",{children:"Class Excel (.xls)"})]}),l.jsxs("button",{type:"button",onClick:e=>{e.currentTarget.closest("details")?.removeAttribute("open");exportWholeSchoolConsolidatedGazette([R],r);},className:"dropdown-menu-item text-purple-700 hover:bg-purple-50",title:"Export Whole School Consolidated Gazette across multiple grades",children:[l.jsx("span",{children:"🏫"}),l.jsx("span",{children:"Whole School Gazette"})]})]})]})]})'''
    text = text[:replace_start] + editor_new + text[p4:]
    print("[✓] Replaced editor action bar")
else:
    print("[!] Failed to find editor action bar block")

# -------------------------------------------------------------------------
# 3. Notes Step 4 toolbar: from p5 to p6
# -------------------------------------------------------------------------
p5 = text.find('// Button 1: Direct PDF Download')
p6 = text.find('// Print Paper Viewport Styles', p5)

if p5 != -1 and p6 != -1:
    print("Found Notes Step 4 block at", p5, p6)
    # The block ends right before the closing tags of the Step 4 toolbar div
    # In the original code, the toolbar div ends with: ] }) ] })
    # Let's inspect the end of the buttons container
    end_btn_container = text.rfind(']                  })', p5, p6)
    if end_btn_container != -1:
        end_btn_container += len(']                  })')
        notes_new = '''l.jsxs("div", {
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
        text = text[:p5] + notes_new + text[end_btn_container:]
        print("[✓] Replaced Notes Step 4 toolbar")
else:
    print("[!] Failed to find Notes Step 4 block")

# Save refactored bundle
with open(js_path, "w", encoding="utf-8") as f:
    f.write(text)

print("Saved new bundle, testing syntax...")
res = subprocess.run(["node", "--check", js_path], capture_output=True, text=True)
if res.returncode == 0:
    print("[✓] node --check passed cleanly!")
else:
    print("[X] node --check failed:")
    print(res.stderr[:600])
    exit(1)
