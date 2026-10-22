import sys
import re

print("Reading assets/index-DAioIUjd.js...")
with open("assets/index-DAioIUjd.js", "r", encoding="utf-8") as f:
    code = f.read()

orig_len = len(code)

# 1. Patch Oh onclone to remove all buttons, controls, action badges, and dropdowns before canvas rasterization
target_oh = 'y.querySelectorAll(".no-print, nav, aside").forEach(I=>{I.style.display="none"});'
replacement_oh = 'y.querySelectorAll(".no-print, button, .btn, .btn-3d, .btn-print-preview, .action-buttons, nav, aside, details, summary, input[type=\'file\'], input[type=\'button\'], input[type=\'submit\'], .dropdown-menu-panel, .segmented-control, .toast-notification, .hub-master-card, .floating-action-btn").forEach(I=>{try{I.remove();}catch(e){I.style.display="none";}});'

if target_oh in code:
    code = code.replace(target_oh, replacement_oh)
    print("SUCCESS: 1. Patched Oh onclone to physically strip all buttons and controls from PDF canvas rendering.")
else:
    print("WARNING: target_oh not found!")

# 2. Add class9 and class10 aliases in MASTER_CLASS_PRESETS
pos_presets = code.find('MASTER_CLASS_PRESETS = {')
if pos_presets != -1:
    # Find end of MASTER_CLASS_PRESETS definition
    # Let's see if we can attach aliases after MASTER_CLASS_PRESETS is initialized
    alias_code = '\nMASTER_CLASS_PRESETS.class9 = MASTER_CLASS_PRESETS["9th"];\nMASTER_CLASS_PRESETS.class10 = MASTER_CLASS_PRESETS["10th"];\n'
    # Or inject right after MASTER_CLASS_PRESETS declaration
    insert_pos = code.find(';', pos_presets + 500)
    # Let's check where the closing brace is for MASTER_CLASS_PRESETS
    end_preset = code.find('};', pos_presets)
    if end_preset != -1:
        code = code[:end_preset+2] + alias_code + code[end_preset+2:]
        print("SUCCESS: 2. Added class9 and class10 aliases to MASTER_CLASS_PRESETS.")
    else:
        print("WARNING: closing brace for MASTER_CLASS_PRESETS not found!")
else:
    print("WARNING: MASTER_CLASS_PRESETS not found!")

# 3. Enhance Date Sheet print function T to switch to preview mode first
# Old: T=()=>{const D=document.title,U=E.classLevel.replace(/\s+/g,"_"),Q=F.replace(/\s+/g,"_");document.title=`${U}_Date_Sheet_${Q}`,window.print(),setTimeout(()=>{document.title=D},1500)}
pattern_t = r'T=\(\)=>\{const D=document\.title,U=E\.classLevel\.replace\(/\\s\+/g,"_"\),Q=F\.replace\(/\\s\+/g,"_"\);document\.title=`\$\{U\}_Date_Sheet_\$\{Q\}`,window\.print\(\),setTimeout\(\(\)=>\{document\.title=D\},1500\)\}'
replacement_t = 'T=()=>{o("preview");const D=document.title,U=E.classLevel.replace(/\\s+/g,"_"),Q=F.replace(/\\s+/g,"_");document.title=`${U}_Date_Sheet_${Q}`;setTimeout(()=>{window.print();setTimeout(()=>{document.title=D},1500)},120)}'

m_t = re.search(pattern_t, code)
if m_t:
    code = code[:m_t.start()] + replacement_t + code[m_t.end():]
    print("SUCCESS: 3. Enhanced Date Sheet print function T to mount preview mode before printing.")
else:
    print("WARNING: pattern_t not matched!")

# 4. Enhance Result Card print function ue to switch to singleCard mode first
pattern_ue = r'ue=S=>\{const V=document\.title;document\.title=`Result_Card_Roll_\$\{S\.rollNo\}_\$\{S\.name\.replace\(/\\s\+/g,"_"\)\}`,window\.print\(\),setTimeout\(\(\)=>\{document\.title=V\},1500\)\}'
replacement_ue = 'ue=S=>{u(S.id);o("singleCard");const V=document.title;document.title=`Result_Card_Roll_${S.rollNo}_${S.name.replace(/\\s+/g,"_")}`;setTimeout(()=>{window.print();setTimeout(()=>{document.title=V},1500)},120)}'

m_ue = re.search(pattern_ue, code)
if m_ue:
    code = code[:m_ue.start()] + replacement_ue + code[m_ue.end():]
    print("SUCCESS: 4. Enhanced Result Card print function ue to mount singleCard view before printing.")
else:
    print("WARNING: pattern_ue not matched!")

# 5. Enhance Master Marksheet print function Ce to switch to masterSheet mode first
pattern_ce = r'Ce=\(\)=>\{o\("masterSheet"\);const S=document\.title;document\.title=`Master_Marksheet_\$\{R\.classLevel\.replace\(/\\s\+/g,"_"\)\}`,window\.print\(\),setTimeout\(\(\)=>\{document\.title=S\},1500\)\}'
replacement_ce = 'Ce=()=>{o("masterSheet");const S=document.title;document.title=`Master_Marksheet_${R.classLevel.replace(/\\s+/g,"_")}`;setTimeout(()=>{window.print();setTimeout(()=>{document.title=S},1500)},120)}'

m_ce = re.search(pattern_ce, code)
if m_ce:
    code = code[:m_ce.start()] + replacement_ce + code[m_ce.end():]
    print("SUCCESS: 5. Enhanced Master Marksheet print function Ce to ensure clean rendering before printing.")
else:
    print("WARNING: pattern_ce not matched!")

# Write back
with open("assets/index-DAioIUjd.js", "w", encoding="utf-8") as f:
    f.write(code)

print(f"Done! Original size: {orig_len}, New size: {len(code)}")
