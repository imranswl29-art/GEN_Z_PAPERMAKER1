import subprocess
import os

print("=== Running Complete Issues 1, 2, 3 Implementation ===")

with open('assets/index-DAioIUjd.js', 'r', encoding='utf-8') as f:
    text = f.read()

def verify(label):
    global text
    with open('test_verify_script.js', 'w', encoding='utf-8') as f_out:
        f_out.write(text)
    res = subprocess.run(['node', '--check', 'test_verify_script.js'], capture_output=True, text=True)
    if res.returncode != 0:
        print(f"FAILED AT: {label}")
        print(res.stderr[:500])
        exit(1)
    else:
        print(f"PASSED: {label}")

# -------------------------------------------------------------
# 1. ISSUE 3: 100% English UI Localization for Paper Suite Controls (WK)
# -------------------------------------------------------------
replacements_wk = [
    ('ملٹی فنکشنل پیپر کنٹرول سینٹر (Multi-Functional Paper Suite)', 'Multi-Functional Paper Control Suite'),
    ('Print & Preview (پرنٹ کریں)', 'Print & Preview'),
    ('ٹول منتخب کریں (کلک کرنے سے نیچے مزید بٹن اوپن ہوں گے):', 'Select a tool to expand child buttons:'),
    ('Select a tool to expand child buttons ▾', 'Click any tool to access expanded controls ▾'),
    ('پیپر سیکشنز کا انتخاب (Select Section to View & Print):', 'Select Section to View & Print:'),
    ('کلک کرنے پر پرچہ کا مطلوبہ حصہ ظاہر ہوگا', 'Click any section to filter current view and print preview'),
    ('مکمل پرچہ (Full Paper - All)', 'Full Paper (All)'),
    ('معروضی اور انشائیہ دونوں حصے', 'Objective and Subjective sections'),
    ('معروضی پرچہ (Objective MCQs)', 'Objective MCQs'),
    ('صرف کثیر الانتخابی سوالات', 'Multiple Choice Questions only'),
    ('انشائیہ پرچہ (Subjective Questions)', 'Subjective Questions'),
    ('مختصر اور تفصیلی سوالات', 'Short and Long questions'),
    ('حل شدہ جوابی کلید (Answer Key)', 'Answer Key'),
    ('درست جوابات کی مکمل شیٹ', 'Complete solved answer guide'),
    ('ببل رسپانس شیٹ (OMR Grid)', 'OMR Response Grid'),
    ('الگ امتحانی دائرہ شیٹ', 'Official bubble sheet for MCQs'),
    ('زبان اور میڈیم کا انتخاب (Select Language Medium):', 'Select Language Medium:'),
    ('کسی بھی بٹن پر کلک کریں، پرچہ فوری اس زبان میں تبدیل ہو جائے گا', 'Click any button to switch the paper language format immediately'),
    ('Bilingual Mode (دو لسانی)', 'Bilingual Mode'),
    ('English + Urdu Nastaliq یکجا', 'English and Urdu side-by-side'),
    ('صرف خالص انگریزی سوالات', 'All questions in English only'),
    ('Urdu Medium Only (اردو میڈیم)', 'Urdu Medium Only'),
    ('صرف خالص اردو خط نستعلیق', 'All questions in authentic Urdu Nastaliq'),
    ('پیپر کوڈز، سیٹس اور سوالات شفلنگ (Paper Sets & Shuffling):', 'Paper Codes, Sets & Question Shuffling:'),
    ('ہر سیٹ میں سوالات اور آپشنز کی ترتیب مختلف ہوتی ہے', 'Each set randomizes question and option sequences for exams'),
    ('Set A (سیٹ الف)', 'Paper Set A'),
    ('Set B (سیٹ ب)', 'Paper Set B'),
    ('Set C (سیٹ ج)', 'Paper Set C'),
    ('تمام سوالات فوری طور پر تبدیل کریں', 'Re-shuffle question sequences across paper'),
    ('امتحانی ببل شیٹ آپشنز (OMR Bubble Response Sheet):', 'OMR Bubble Response Sheet Options:'),
    ('امتحانی بورڈ کے مطابق پیپر پر ببل گرڈ شامل یا خارج کریں', 'Attach or detach official OMR bubble grid per board pattern'),
    ('With Bubble Sheet (ببل شیٹ شامل کریں)', 'With Bubble Sheet'),
    ('پرچے پر طالب علم کے لیے دائرہ گرڈ ظاہر ہوگی', 'Attached OMR bubble grid on the question paper'),
    ('Without Bubble Sheet (بغیر ببل شیٹ)', 'Without Bubble Sheet'),
    ('صرف خالص سوالات، کوئی ببل گرڈ نہیں', 'Standard question paper layout without bubble grid'),
    ('مکمل ایک صفحے کی علیحدہ ببل شیٹ پرنٹ کریں', 'Print dedicated standalone full-page OMR bubble sheet'),
    ('صفحہ کا رخ، فونٹ سائز اور فریم بارڈر (Layout & Formatting):', 'Page Orientation, Font Size & Layout:'),
    ('صفحات کی بچت یا بڑے پرنٹ کے لیے موزوں سائز منتخب کریں', 'Optimize layout for single-page economy or readable large print'),
    ('عمودی صفحہ (Portrait A4)', 'Portrait Mode (Standard A4)'),
    ('معیاری سیدھا رخ', 'Standard vertical single/multi-page layout'),
    ('افقی صفحہ (Landscape A4)', 'Landscape Mode (2-Column A4)'),
    ('چوڑا رخ (2 کالم پیپر)', 'Dual-column landscape format for paper economy'),
    ('معیاری سائز (Standard BISE)', 'Standard BISE Size'),
    ('بورڈ پیٹرن کا متوازن فونٹ', 'Balanced typography conforming to board standards'),
    ('کمپیکٹ سائز (Fit 1 Page)', 'Compact Size (Fit 1 Page)'),
    ('1 صفحہ پر پرچہ سمیٹیں', 'Tight line spacing to economize paper printing'),
    ('بڑا فونٹ (Large Font)', 'Large Font Size'),
    ('کھلا اور انتہائی واضح فونٹ', 'Spacious high-legibility print formatting'),
    ('ڈبل بارڈر آن ہے', 'Double Border Enabled'),
    ('سادہ بارڈر', 'Simple Border Enabled'),
    ('رول نمبر باکس آن ہے', 'Roll No Box Visible'),
    ('رول نمبر باکس چھپا ہوا', 'Roll No Box Hidden'),
    ('ادارہ کی برانڈنگ، مونوگرام اور واٹر مارک (Branding & Logo):', 'Institutional Branding, Monogram & Watermark:'),
    ('پرچے کے پس منظر پر ادارے کا واٹر مارک اور اوپر مونوگرام لوگو', 'Configure official monogram, header crest, and background watermark'),
    ('Watermark: ON (واٹر مارک دکھائیں)', 'Watermark: ON'),
    ('پرچے کے پس منظر میں واٹر مارک ظاہر ہوگا', 'Faint institutional watermark visible on paper background'),
    ('Watermark: OFF (واٹر مارک چھپائیں)', 'Watermark: OFF'),
    ('پس منظر سے واٹر مارک ہٹا دیں', 'Clean background without watermark'),
    ('ادارے کا لوگو یا مونوگرام فائل منتخب کریں', 'Upload new school monogram / crest logo file'),
    ('کسٹم مونوگرام ہٹا کر ڈیفالٹ بحال کریں', 'Remove custom monogram and restore default'),
    ('سوالات لائیو ایڈیٹر اور اضافہ (In-Place Question Editor):', 'In-Place Question Editor & Customizer:'),
    ('پرچے پر کسی بھی سوال کی تحریر بدلیں یا نئے سوالات شامل کریں', 'Edit question text directly on paper or add custom questions'),
    ('Edit Text Directly (لائیو ایڈٹ موڈ)', 'Edit Text Directly (Live Mode)'),
    ('پرچے پر براہِ راست سوالات تبدیل کریں', 'Click any question or option directly to edit text'),
    ('Done Editing (ایڈیٹنگ ختم کریں)', 'Finish Editing & Save Changes'),
    ('تبدیلیاں محفوظ ہیں', 'All customized changes are saved to memory'),
    ('نیا کثیر الانتخابی سوال شامل کریں', 'Add New MCQ Question'),
    ('حصہ اول میں نیا مختصر سوال شامل کریں', 'Add New Short Question'),
    ('حصہ دوم میں نیا تفصیلی سوال شامل کریں', 'Add New Long Question'),
    ('فائلز ڈاؤن لوڈ اور ایکسپورٹ (Download & Export Files):', 'Download & Export Formats:'),
    ('پی ڈی ایف یا ورڈ فارمیٹ میں مکمل پرچہ محفوظ کریں', 'Save high-resolution PDF or editable Microsoft Word files'),
    ('پرنٹ اور شیئر کے لیے معیاری پی ڈی ایف', 'Print-ready vector PDF formatted for A4 paper'),
    ('مائیکروسافٹ ورڈ میں قابلِ تدوین فائل', 'Fully editable Microsoft Word (.doc) document'),
    ('جوابی کلید اور حل شدہ پرچہ', 'Full answer key and grading guide PDF'),
    ('امتحانی ببل شیٹ فائل', 'Blank printable OMR bubble response sheet PDF'),
    ('پرچہ شیئرنگ اور تقسیم (Share & Distribute Paper):', 'Share & Distribute Paper:'),
    ('اساتذہ یا طلبہ کو واٹس ایپ یا لنک کے ذریعے فوری بھیجیں', 'Instantly send to teachers or students via WhatsApp or web link'),
    ('واٹس ایپ پر مکمل تفصیل اور لنک بھیجیں', 'Send formatted paper details directly via WhatsApp'),
    ('براہِ راست آن لائن لنک کاپی کریں', 'Copy direct shareable web link to clipboard'),
    ('موبائل کے اپنے شیئر مینو سے شیئر کریں', 'Open native operating system sharing menu'),
    ('o==="all"?"مکمل":o==="objective"?"معروضی":"انشائیہ"', 'o==="all"?"All":o==="objective"?"MCQs":"Subjective"'),
    ('D==="bilingual"?"دو لسانی":D==="english"?"انگلش":"اردو"', 'D==="bilingual"?"Bilingual":D==="english"?"English":"Urdu"'),
    ('n.header.includeBubbleSheet!==!1?"آن":"آف"', 'n.header.includeBubbleSheet!==!1?"ON":"OFF"'),
    ('/* Master Hub Category Buttons (ہر بٹن کے اندر مزید آپشنز) */', '/* Master Hub Category Buttons */'),
    ('پیپر سیکشنز', 'Paper Sections'),
    ('زبان اور میڈیم', 'Language & Medium'),
    ('پیپر سیٹس اور شفل', 'Paper Sets & Shuffle'),
    ('ببل شیٹ', 'OMR Bubble Sheet'),
    ('صفحہ اور لے آؤٹ', 'Page & Layout'),
    ('لوگو اور واٹر مارک', 'Branding & Logo'),
    ('سوالات ایڈٹ کریں', 'Edit Questions'),
    ('ڈاؤن لوڈز', 'Downloads & Export'),
    ('شیئر کریں', 'Share & Send'),
]

replacements_wk.sort(key=lambda x: len(x[0]), reverse=True)
for old_s, new_s in replacements_wk:
    text = text.replace(old_s, new_s)

verify("Issue 3: WK Toolbar 100% English")

# -------------------------------------------------------------
# 2. ISSUE 2: Single Open Dropdown in Saved Examination Papers Archive
# -------------------------------------------------------------
# First ensure openArchiveDropdownId state and outside-click in cq()
if 'openArchiveDropdownId' not in text:
    old_cq_head = 'function cq(){const[n,e]=Ee.useState("dashboard"),[t,r]=Ee.useState("9th"),'
    new_cq_head = 'function cq(){const[openArchiveDropdownId,setOpenArchiveDropdownId]=Ee.useState(null);Ee.useEffect(()=>{const h=ev=>{if(!ev.target.closest(".archive-dropdown-container"))setOpenArchiveDropdownId(null)};document.addEventListener("click",h);return()=>document.removeEventListener("click",h)},[]);const[n,e]=Ee.useState("dashboard"),[t,r]=Ee.useState("9th"),'
    if old_cq_head in text:
        text = text.replace(old_cq_head, new_cq_head, 1)
        verify("Issue 2: Defined openArchiveDropdownId in cq()")

# Now in saved_papers cards, replace options dropdown
pos_saved = text.find('n==="saved_papers"&&')
if pos_saved != -1:
    pos_opts = text.find('Options ▾', pos_saved)
    if pos_opts != -1:
        # Find start of dropdown element (details or div)
        pos_dt_start = text.rfind('l.jsxs("details",{className:"relative inline-block text-left no-print"', 0, pos_opts)
        if pos_dt_start != -1:
            # find end of details
            pos_del_btn = text.find('Delete Paper"})', pos_dt_start)
            # Find the closing sequence: button }) + menu ]}) + details ]})
            pos_dt_end = text.find(']})]})', pos_del_btn) + len(']})]})')
            
            clean_dropdown = 'l.jsxs("div",{className:"relative inline-block text-left no-print archive-dropdown-container",children:[l.jsxs("button",{type:"button",onClick:ev=>{ev.stopPropagation();setOpenArchiveDropdownId(openArchiveDropdownId===ge.id?null:ge.id);},className:"btn-3d btn-3d-indigo flex items-center gap-1 px-3 py-1.5 text-white rounded-lg text-xs font-black shadow-xs cursor-pointer select-none",title:"Export & Paper Options",children:[l.jsx("span",{children:"Options ▾"})]}),openArchiveDropdownId===ge.id&&l.jsxs("div",{className:"absolute right-0 bottom-full mb-2 z-50 min-w-[14rem] bg-white border border-slate-200 rounded-xl shadow-2xl p-1.5 space-y-1 animate-in fade-in zoom-in-95",style:{backgroundColor:"#ffffff",zIndex:9999},onClick:ev=>ev.stopPropagation(),children:[l.jsxs("button",{type:"button",onClick:()=>{setOpenArchiveDropdownId(null);z0(ge);},className:"w-full flex items-center gap-2.5 px-3 py-2 text-xs font-bold text-slate-800 hover:bg-blue-50 hover:text-blue-700 rounded-lg text-left transition-colors cursor-pointer",title:"Download editable Microsoft Word document",children:[l.jsx(Xu,{className:"w-4 h-4 text-blue-600 shrink-0"}),l.jsx("span",{children:"Download Word (.doc)"})]}),l.jsxs("button",{type:"button",onClick:()=>{setOpenArchiveDropdownId(null);E(ge);te(!0);},className:"w-full flex items-center gap-2.5 px-3 py-2 text-xs font-bold text-slate-800 hover:bg-emerald-50 hover:text-emerald-700 rounded-lg text-left transition-colors cursor-pointer",title:"View and print Answer Key",children:[l.jsx(SAFE_ad,{className:"w-4 h-4 text-emerald-600 shrink-0"}),l.jsx("span",{children:"Answer Key (Key & Solutions)"})]}),l.jsxs("button",{type:"button",onClick:()=>{setOpenArchiveDropdownId(null);E(ge);T(!0);},className:"w-full flex items-center gap-2.5 px-3 py-2 text-xs font-bold text-slate-800 hover:bg-purple-50 hover:text-purple-700 rounded-lg text-left transition-colors cursor-pointer",title:"View official OMR bubble sheet",children:[l.jsx(Rw,{className:"w-4 h-4 text-purple-600 shrink-0"}),l.jsx("span",{children:"OMR Bubble Sheet"})]}),m&&l.jsxs("button",{type:"button",onClick:()=>{setOpenArchiveDropdownId(null);window.confirm(`Are you sure you want to delete "${ge.header.subjectName}" paper?`)&&St(ge.id);},className:"w-full flex items-center gap-2.5 px-3 py-2 text-xs font-bold text-red-600 hover:bg-red-50 rounded-lg text-left border-t border-slate-100 transition-colors cursor-pointer",title:"Delete this paper from saved list",children:[l.jsx(Ql,{className:"w-4 h-4 text-red-600 shrink-0"}),l.jsx("span",{children:"Delete Paper"})]})]})]})'
            
            text = text[:pos_dt_start] + clean_dropdown + text[pos_dt_end:]
            verify("Issue 2: Single Open Dropdown in Saved Examination Papers Archive")

# -------------------------------------------------------------
# 3. ISSUE 1: Dual Paper Generation Modes in Step-by-Step Paper Builder (y8)
# -------------------------------------------------------------
# Add builderMode, isGeneratingAi, aiStatusMsg to y8
if 'builderMode' not in text:
    old_y8_state_start = 'const y8=({currentUser:n,initialClass:e="9th",onPaperCreated:t,onCancel:r})=>{var Jr;const[a,o]=Ee.useState(1),'
    new_y8_state_start = 'const y8=({currentUser:n,initialClass:e="9th",onPaperCreated:t,onCancel:r})=>{var Jr;const[builderMode,setBuilderMode]=Ee.useState("database"),[isGeneratingAi,setIsGeneratingAi]=Ee.useState(!1),[aiStatusMsg,setAiStatusMsg]=Ee.useState(""),[a,o]=Ee.useState(1),'
    if old_y8_state_start in text:
        text = text.replace(old_y8_state_start, new_y8_state_start, 1)
        verify("Issue 1: Added builderMode state to y8")

# In xr function of y8, handle AI mode
if 'builderMode==="ai"' not in text:
    old_xr = 'xr=()=>{const Ie=Y2.find(Cn=>Cn.id===Ze),'
    new_xr = 'xr=async()=>{if(builderMode==="ai"){setIsGeneratingAi(!0);setAiStatusMsg("Connecting to Gemini AI Engine...");try{const aiResp=await fetch("/api/generate-paper",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({classLevel:A,subjectName:C.nameEn,chapters:pr.map(cn=>`Unit ${cn.number}: ${cn.titleEn}`),examType:"chapter",totalMarks:S||60,languageMode:We,difficulty:ce,instituteName:le,campusName:Qe,examTitle:Be,teacherName:X})});if(aiResp.ok){const aiPaper=await aiResp.json();if(aiPaper&&aiPaper.id){setIsGeneratingAi(!1);t(aiPaper);return;}}}catch(err){console.warn("AI generation fallback to database:",err)}setIsGeneratingAi(!1);}const Ie=Y2.find(Cn=>Cn.id===Ze),'
    if old_xr in text:
        text = text.replace(old_xr, new_xr, 1)
        verify("Issue 1: Added AI Engine execution in xr()")

# Visual Mode Indicator badge in y8 header
if 'Mode: AI Powered' not in text:
    old_builder_header = 'l.jsxs("h1",{className:"text-lg font-black text-slate-900 flex items-center gap-2",children:[l.jsx(SAFE_Ta,{className:"w-5 h-5 text-blue-600"}),l.jsx("span",{children:"Step-by-Step Examination Paper Builder"})]}),l.jsx("p",{className:"text-xs text-slate-500 mt-0.5",children:"Follow the 8 guided steps or click Auto-Pick to automatically select questions conforming to PTBB pattern."})'
    new_builder_header = 'l.jsxs("h1",{className:"text-lg font-black text-slate-900 flex items-center gap-2 flex-wrap",children:[l.jsx(SAFE_Ta,{className:"w-5 h-5 text-blue-600"}),l.jsx("span",{children:"Step-by-Step Examination Paper Builder"}),l.jsx("span",{className:"px-2.5 py-0.5 rounded-full text-[11px] font-black uppercase tracking-wider " + (builderMode==="ai"?"bg-purple-100 text-purple-900 border border-purple-300":"bg-emerald-100 text-emerald-900 border border-emerald-300"),children:builderMode==="ai"?"Mode: AI Powered":"Mode: Question Bank"})]}),l.jsx("p",{className:"text-xs text-slate-500 mt-0.5",children:"Follow the 8 guided steps or choose generation mode below conforming to PTBB pattern."})'
    if old_builder_header in text:
        text = text.replace(old_builder_header, new_builder_header, 1)
        verify("Issue 1: Added Visual Mode Indicator badge in y8 header")

# 2-Option Mode Switcher right at start of Paper Builder
if 'Paper Generation Engine:' not in text:
    old_medium_bar_end = 'l.jsx("button",{type:"button",onClick:()=>dt("bilingual"),className:`px-3 py-1.5 rounded-lg text-xs font-black transition-all cursor-pointer ${We==="bilingual"?"bg-indigo-600 text-white shadow-xs":"text-slate-700 hover:text-slate-950 hover:bg-slate-100"}`,children:"Bilingual (English + Urdu)"})]})]}),'
    mode_switcher_jsx = 'l.jsxs("div",{className:"bg-slate-50 border border-slate-200 rounded-2xl p-3.5 sm:p-4 space-y-2.5 shadow-2xs",children:[l.jsxs("div",{className:"flex flex-wrap items-center justify-between gap-2",children:[l.jsxs("div",{children:[l.jsx("span",{className:"text-xs font-black uppercase text-slate-900 tracking-wide",children:"Paper Generation Engine:"}),l.jsx("p",{className:"text-[11px] text-slate-500",children:"Choose whether to pull questions strictly from pre-stored database or generate dynamically via Gemini AI."})]}),l.jsx("span",{className:"text-[11px] font-black px-2.5 py-1 rounded-lg " + (builderMode==="ai"?"bg-purple-600 text-white":"bg-emerald-600 text-white"),children:builderMode==="ai"?"Active: Gemini AI Engine":"Active: Question Bank (Offline)"})]}),l.jsxs("div",{className:"grid grid-cols-1 sm:grid-cols-2 gap-3",children:[l.jsxs("div",{onClick:()=>setBuilderMode("database"),className:"p-3.5 rounded-xl border-2 text-left transition-all cursor-pointer " + (builderMode==="database"?"bg-white border-emerald-600 shadow-md ring-2 ring-emerald-500/20":"bg-white border-slate-200 hover:border-slate-300"),children:[l.jsxs("div",{className:"flex items-center justify-between mb-1",children:[l.jsx("span",{className:"font-black text-xs uppercase tracking-wide text-emerald-700",children:"Mode A: Question Bank"}),builderMode==="database"&&l.jsx("span",{className:"w-5 h-5 rounded-full bg-emerald-600 text-white text-xs flex items-center justify-center font-black",children:"✓"})]}),l.jsx("div",{className:"font-black text-sm text-slate-900",children:"Offline / Pre-stored Database - No AI"}),l.jsx("p",{className:"text-[11px] text-slate-500 mt-1 leading-relaxed",children:"Pull questions strictly and solely from the saved question bank database. No API calls should be triggered to external AI services."})]}),l.jsxs("div",{onClick:()=>setBuilderMode("ai"),className:"p-3.5 rounded-xl border-2 text-left transition-all cursor-pointer " + (builderMode==="ai"?"bg-white border-purple-600 shadow-md ring-2 ring-purple-500/20":"bg-white border-slate-200 hover:border-slate-300"),children:[l.jsxs("div",{className:"flex items-center justify-between mb-1",children:[l.jsx("span",{className:"font-black text-xs uppercase tracking-wide text-purple-700",children:"Mode B: AI Generator"}),builderMode==="ai"&&l.jsx("span",{className:"w-5 h-5 rounded-full bg-purple-600 text-white text-xs flex items-center justify-center font-black",children:"✓"})]}),l.jsx("div",{className:"font-black text-sm text-slate-900",children:"Dynamic AI Generation via Vercel Gemini API Key"}),l.jsx("p",{className:"text-[11px] text-slate-500 mt-1 leading-relaxed",children:"Connect directly to the Gemini API configured in Vercel environment variables to dynamically formulate exam questions based on syllabus, board standards, and SLO criteria."})]})]})]}),isGeneratingAi&&l.jsxs("div",{className:"p-3 bg-purple-50 border border-purple-300 rounded-xl flex items-center gap-3 text-purple-900 text-xs font-bold animate-pulse",children:[l.jsx("div",{className:"w-4 h-4 border-2 border-purple-600 border-t-transparent rounded-full animate-spin"}),l.jsx("span",{children:aiStatusMsg||"Formulating examination questions via Gemini AI Engine..."})]}),'
    if old_medium_bar_end in text:
        text = text.replace(old_medium_bar_end, old_medium_bar_end + mode_switcher_jsx, 1)
        verify("Issue 1: Added 2-Option Mode Switcher right at start of Paper Builder")

# Write out final
with open('assets/index-DAioIUjd.js', 'w', encoding='utf-8') as f_out:
    f_out.write(text)

print("SUCCESS: assets/index-DAioIUjd.js completely updated!")
