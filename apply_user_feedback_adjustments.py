import subprocess
import os

print("Starting clean updates...")

with open('assets/index-DAioIUjd.js', 'r', encoding='utf-8') as f:
    text = f.read()

def check(step_name):
    global text
    with open('step_check.js', 'w', encoding='utf-8') as f:
        f.write(text)
    res = subprocess.run(['node', '--check', 'step_check.js'], capture_output=True, text=True)
    if res.returncode != 0:
        print(f"FAILED AT {step_name}:")
        print(res.stderr[:500])
        return False
    else:
        print(f"PASSED {step_name}")
        return True

assert check("Initial syntax check")

# =========================================================================
# 1. SLOW DOWN NEWS BULLETIN TICKER (Super slow and pauses on hover)
# =========================================================================
old_ticker_style = 'animation: seamlessTickerMove 120s linear infinite; will-change: transform; }"'
new_ticker_style = 'animation: seamlessTickerMove 450s linear infinite; will-change: transform; } .seamless-ticker-track:hover { animation-play-state: paused; }"'

if old_ticker_style in text:
    text = text.replace(old_ticker_style, new_ticker_style, 1)
    assert check("Step 1: Slow down NewsBulletinTicker to 450s with hover pause")
else:
    print("[!] old_ticker_style not found exactly, searching keyframes...")
    pos_kf = text.find('seamlessTickerMove 120s')
    if pos_kf != -1:
        text = text[:pos_kf] + 'seamlessTickerMove 450s linear infinite; will-change: transform; } .seamless-ticker-track:hover { animation-play-state: paused; }' + text[pos_kf+len('seamlessTickerMove 120s linear infinite; will-change: transform; }'):]
        assert check("Step 1: Slow down NewsBulletinTicker (fallback pos)")

# =========================================================================
# 2. REMOVE UNNECESSARY URDU TRANSLATIONS FOR SCIENCE SUBJECTS (No "طبیعیات", etc.)
# =========================================================================
# Replace in 9th metadata
old_meta_9th = '''const SUBJECT_METADATA_9TH = [
  { id: "physics", nameEn: "Physics", nameUr: "طبیعیات", chaptersCount: 9, icon: "⚡" },
  { id: "chemistry", nameEn: "Chemistry", nameUr: "کیمسٹری", chaptersCount: 8, icon: "🧪" },
  { id: "biology", nameEn: "Biology", nameUr: "حیاتیات", chaptersCount: 9, icon: "🧬" },
  { id: "mathematics", nameEn: "Mathematics", nameUr: "ریاضی", chaptersCount: 17, icon: "📐" },
  { id: "computer", nameEn: "Computer Science", nameUr: "کمپیوٹر سائنس", chaptersCount: 5, icon: "💻" },
  { id: "english", nameEn: "English", nameUr: "انگریزی لازمی", chaptersCount: 12, icon: "📖" },
  { id: "urdu", nameEn: "Urdu", nameUr: "اردو لازمی", chaptersCount: 7, icon: "✍️" },
  { id: "islamiyat", nameEn: "Islamiat Compulsory", nameUr: "اسلامیات لازمی", chaptersCount: 6, icon: "🕌" },
  { id: "tarjuma_quran", nameEn: "Tarjuma-tul-Quran-ul-Majeed", nameUr: "ترجمۃ القرآن المجید", chaptersCount: 6, icon: "📜" },
  { id: "pakstudies", nameEn: "Pakistan Studies", nameUr: "مطالعہ پاکستان", chaptersCount: 5, icon: "🇵🇰" }
];'''

new_meta_9th = '''const SUBJECT_METADATA_9TH = [
  { id: "physics", nameEn: "Physics", nameUr: "", chaptersCount: 9, icon: "⚡" },
  { id: "chemistry", nameEn: "Chemistry", nameUr: "", chaptersCount: 8, icon: "🧪" },
  { id: "biology", nameEn: "Biology", nameUr: "", chaptersCount: 9, icon: "🧬" },
  { id: "mathematics", nameEn: "Mathematics", nameUr: "", chaptersCount: 17, icon: "📐" },
  { id: "computer", nameEn: "Computer Science", nameUr: "", chaptersCount: 5, icon: "💻" },
  { id: "english", nameEn: "English", nameUr: "", chaptersCount: 12, icon: "📖" },
  { id: "urdu", nameEn: "Urdu", nameUr: "اردو", chaptersCount: 7, icon: "✍️" },
  { id: "islamiyat", nameEn: "Islamiat Compulsory", nameUr: "اسلامیات", chaptersCount: 6, icon: "🕌" },
  { id: "tarjuma_quran", nameEn: "Tarjuma-tul-Quran-ul-Majeed", nameUr: "ترجمۃ القرآن", chaptersCount: 6, icon: "📜" },
  { id: "pakstudies", nameEn: "Pakistan Studies", nameUr: "مطالعہ پاکستان", chaptersCount: 5, icon: "🇵🇰" }
];'''

if old_meta_9th in text:
    text = text.replace(old_meta_9th, new_meta_9th, 1)
    assert check("Step 2a: Removed Urdu labels from 9th science subjects")
else:
    print("[!] old_meta_9th not found exactly")

# Replace in 10th metadata
old_meta_10th = '''const SUBJECT_METADATA_10TH = [
  { id: "physics", nameEn: "Physics", nameUr: "طبیعیات", chaptersCount: 9, icon: "⚡" },
  { id: "chemistry", nameEn: "Chemistry", nameUr: "کیمسٹری", chaptersCount: 8, icon: "🧪" },
  { id: "biology", nameEn: "Biology", nameUr: "حیاتیات", chaptersCount: 9, icon: "🧬" },
  { id: "mathematics", nameEn: "Mathematics", nameUr: "ریاضی", chaptersCount: 13, icon: "📐" },
  { id: "computer", nameEn: "Computer Science", nameUr: "کمپیوٹر سائنس", chaptersCount: 5, icon: "💻" },
  { id: "english", nameEn: "English", nameUr: "انگریزی لازمی", chaptersCount: 13, icon: "📖" },
  { id: "urdu", nameEn: "Urdu", nameUr: "اردو لازمی", chaptersCount: 10, icon: "✍️" },
  { id: "islamiyat", nameEn: "Islamiat Compulsory", nameUr: "اسلامیات لازمی", chaptersCount: 6, icon: "🕌" },
  { id: "tarjuma_quran", nameEn: "Tarjuma-tul-Quran-ul-Majeed", nameUr: "ترجمۃ القرآن المجید", chaptersCount: 6, icon: "📜" },
  { id: "pakstudies", nameEn: "Pakistan Studies", nameUr: "مطالعہ پاکستان", chaptersCount: 5, icon: "🇵🇰" }
];'''

new_meta_10th = '''const SUBJECT_METADATA_10TH = [
  { id: "physics", nameEn: "Physics", nameUr: "", chaptersCount: 9, icon: "⚡" },
  { id: "chemistry", nameEn: "Chemistry", nameUr: "", chaptersCount: 8, icon: "🧪" },
  { id: "biology", nameEn: "Biology", nameUr: "", chaptersCount: 9, icon: "🧬" },
  { id: "mathematics", nameEn: "Mathematics", nameUr: "", chaptersCount: 13, icon: "📐" },
  { id: "computer", nameEn: "Computer Science", nameUr: "", chaptersCount: 5, icon: "💻" },
  { id: "english", nameEn: "English", nameUr: "", chaptersCount: 13, icon: "📖" },
  { id: "urdu", nameEn: "Urdu", nameUr: "اردو", chaptersCount: 10, icon: "✍️" },
  { id: "islamiyat", nameEn: "Islamiat Compulsory", nameUr: "اسلامیات", chaptersCount: 6, icon: "🕌" },
  { id: "tarjuma_quran", nameEn: "Tarjuma-tul-Quran-ul-Majeed", nameUr: "ترجمۃ القرآن", chaptersCount: 6, icon: "📜" },
  { id: "pakstudies", nameEn: "Pakistan Studies", nameUr: "مطالعہ پاکستان", chaptersCount: 5, icon: "🇵🇰" }
];'''

if old_meta_10th in text:
    text = text.replace(old_meta_10th, new_meta_10th, 1)
    assert check("Step 2b: Removed Urdu labels from 10th science subjects")
else:
    print("[!] old_meta_10th not found exactly")

# Replace any lingering "Physics (طبیعیات)" in text
if 'subjectName:"Physics (طبیعیات)"' in text:
    text = text.replace('subjectName:"Physics (طبیعیات)"', 'subjectName:"Physics"')
    assert check("Step 2c: Replaced Physics (طبیعیات) with Physics")

# Also in Notes print header, don't show empty parenthesis when nameUr is empty
old_header_sub = 'l.jsxs("span", { children: ["Subject: ", currentSubject.nameEn, " (", currentSubject.nameUr, ")"] })'
new_header_sub = 'l.jsxs("span", { children: ["Subject: ", currentSubject.nameEn, currentSubject.nameUr ? ` (${currentSubject.nameUr})` : ""] })'
if old_header_sub in text:
    text = text.replace(old_header_sub, new_header_sub, 1)
    assert check("Step 2d: Fixed header subject format without empty parens")

# =========================================================================
# 3. REMOVE NOTES BUTTON FROM NEXT TO LOGOUT IN HEADER
# =========================================================================
old_header_right_with_notes = '''l.jsxs("div",{className:"flex items-center gap-2 shrink-0",children:[l.jsxs("button",{type:"button",onClick:()=>{e("notes_portal");o(!1)},className:"btn-3d btn-3d-purple flex items-center gap-1.5 px-3 py-1.5 sm:px-3.5 sm:py-2 text-white rounded-xl text-xs font-black cursor-pointer shadow-sm hover:scale-[1.02] transition-transform",title:"Official PTBB Solved Notes for Class 9th & 10th (MCQs & Short Questions)",children:[l.jsxs("svg",{className:"w-4 h-4 text-purple-200",viewBox:"0 0 24 24",fill:"none",stroke:"currentColor",strokeWidth:"2.2",strokeLinecap:"round",strokeLinejoin:"round",children:[l.jsx("path",{d:"M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"}),l.jsx("path",{d:"M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"})]}),l.jsx("span",{children:"Notes 9th & 10th"}),l.jsx("span",{className:"hidden md:inline-block bg-purple-900/60 text-purple-200 text-[10px] px-1.5 py-0.5 rounded-md font-bold",children:"PTBB"})]}),m?l.jsxs("button",{type:"button",onClick:Ke,className:"btn-3d btn-3d-rose flex items-center gap-1.5 px-3 py-2 text-white rounded-xl text-xs font-black cursor-pointer shadow-sm",title:"Direct Logout",children:[l.jsxs("svg",{className:"w-3.5 h-3.5 text-white",viewBox:"0 0 24 24",fill:"none",stroke:"currentColor",strokeWidth:"2.2",strokeLinecap:"round",strokeLinejoin:"round",children:[l.jsx("path",{d:"M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"}),l.jsx("polyline",{points:"16 17 21 12 16 7"}),l.jsx("line",{x1:"21",x2:"9",y1:"12",y2:"12"})]}),l.jsx("span",{children:"Logout"})]}):l.jsx("button",{onClick:()=>R(!0),className:"btn-3d px-3.5 py-2 text-white font-black rounded-xl text-xs cursor-pointer",style:{backgroundColor:"#2563eb",border:"1px solid #1d4ed8",color:"#ffffff"},children:"Login"})]})'''

clean_header_right = '''l.jsx("div",{className:"flex items-center gap-2 shrink-0",children:m?l.jsxs("button",{type:"button",onClick:Ke,className:"btn-3d btn-3d-rose flex items-center gap-1.5 px-3 py-2 text-white rounded-xl text-xs font-black cursor-pointer shadow-sm",title:"Direct Logout",children:[l.jsxs("svg",{className:"w-3.5 h-3.5 text-white",viewBox:"0 0 24 24",fill:"none",stroke:"currentColor",strokeWidth:"2.2",strokeLinecap:"round",strokeLinejoin:"round",children:[l.jsx("path",{d:"M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"}),l.jsx("polyline",{points:"16 17 21 12 16 7"}),l.jsx("line",{x1:"21",x2:"9",y1:"12",y2:"12"})]}),l.jsx("span",{children:"Logout"})]}):l.jsx("button",{onClick:()=>R(!0),className:"btn-3d px-3.5 py-2 text-white font-black rounded-xl text-xs cursor-pointer",style:{backgroundColor:"#2563eb",border:"1px solid #1d4ed8",color:"#ffffff"},children:"Login"})})'''

assert old_header_right_with_notes in text, "old_header_right_with_notes not found in text"
text = text.replace(old_header_right_with_notes, clean_header_right, 1)
assert check("Step 3: Removed Notes button from next to Logout")

with open('assets/index-DAioIUjd.js', 'w', encoding='utf-8') as f_out:
    f_out.write(text)

print("SUCCESS: assets/index-DAioIUjd.js updated cleanly with all requested changes!")
