with open('assets/index-DAioIUjd.js', 'r', encoding='utf-8') as f:
    text = f.read()

old_tq = 'function tq(n,e,t){const r=e.subjects.reduce((B,m)=>B+m.totalMarks,0),'
new_tq = 'function tq(n,e,t,template="classic"){const r=e.subjects.reduce((B,m)=>B+m.totalMarks,0),'
if old_tq in text:
    text = text.replace(old_tq, new_tq, 1)

old_tq_title = 'PROGRESS REPORT CARD / MARKSHEET (${e.session})'
new_tq_title = '${(template==="modern"?"CERTIFICATE OF ACADEMIC ACHIEVEMENT & REPORT CARD":template==="diagnostic"?"COMPREHENSIVE DIAGNOSTIC PERFORMANCE REPORT":"OFFICIAL STUDENT ACADEMIC TRANSCRIPT & PROGRESS REPORT")} (${e.session})'
if old_tq_title in text:
    text = text.replace(old_tq_title, new_tq_title, 1)

with open('assets/index-DAioIUjd.js', 'w', encoding='utf-8') as f:
    f.write(text)

print("[✓] Updated tq Word exporter successfully!")
