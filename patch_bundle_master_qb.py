import re

with open("assets/index-DAioIUjd.js", "r", encoding="utf-8") as f:
    bundle = f.read()

# 1. Deduplicate Wo
target_wo = "Wo=[...g8,...b8];"
replacement_wo = "Wo=(()=>{const s=new Set();return[...g8,...b8].filter(x=>{if(s.has(x.id))return false;s.add(x.id);return true})})();"

if target_wo in bundle:
    bundle = bundle.replace(target_wo, replacement_wo)
    print("Patched Wo subject deduplication successfully.")
else:
    print("target_wo not found")

# 2. Update W2 to use window.__PTBB_MASTER_QB__
w2_target = """function W2(n,e){const t=Wo.find(E=>E.id===n);if(!t)return{mcqs:[],shortQuestions:[],longQuestions:[],totalAvailableMCQs:0,totalAvailableShorts:0,totalAvailableLongs:0};const r=t.chapters.filter(E=>e.length===0||e.includes(E.number)),a=Z3().filter(E=>E.subjectId===n),o=[],A=[],u=[];r.forEach(E=>{const I=(E.mcqs||[]).map((T,H)=>({...T,qNo:o.length+H+1,chapterRef:E.number})),O=(E.shortQuestions||[]).map((T,H)=>({...T,subNo:A.length+H+1,chapterRef:E.number})),F=(E.longQuestions||[]).map((T,H)=>({id:T.id,qNo:u.length+H+5,totalMarks:9,parts:T.parts||[{partLabel:"a",statementEn:T.statementEn||"",statementUr:T.statementUr||"",marks:5}],chapterRef:`Unit ${E.number}`})),R=x8(t,E),Z=C8(t,E),oe=[...I,...Z.mcqs,...R.mcqs],ne=[...O,...Z.shortQuestions,...R.shortQuestions],te=[...F,...Z.longQuestions,...R.longQuestions];oe.forEach((T,H)=>{T.qNo=o.length+H+1}),ne.forEach((T,H)=>{T.subNo=A.length+H+1}),te.forEach((T,H)=>{T.qNo=u.length+H+5}),o.push(...oe),A.push(...ne),u.push(...te),a.filter(T=>T.chapterNo===E.number).forEach(T=>{T.type==="mcq"&&T.options&&T.correctOption?o.push({id:T.id,qNo:o.length+1,statementEn:T.statementEn,statementUr:T.statementUr,options:T.options,correctOption:T.correctOption,chapterRef:E.number}):T.type==="short"?A.push({id:T.id,subNo:A.length+1,statementEn:T.statementEn,statementUr:T.statementUr,marks:T.marks||2,chapterRef:E.number}):T.type==="long"&&u.push({id:T.id,qNo:u.length+5,totalMarks:T.marks||9,parts:[{partLabel:"a",statementEn:T.statementEn,statementUr:T.statementUr,marks:T.marks||5}],chapterRef:`Unit ${E.number}`})})});const f=[],B=new Set;o.forEach(E=>{const I=(E.statementEn||E.statementUr||"").trim().toLowerCase();I&&!B.has(I)&&(B.add(I),f.push({...E,qNo:f.length+1}))});const m=[],C=new Set;A.forEach(E=>{const I=(E.statementEn||E.statementUr||"").trim().toLowerCase();I&&!C.has(I)&&(C.add(I),m.push({...E,subNo:m.length+1}))});const y=[],v=new Set;return u.forEach(E=>{var O,F;const I=(((F=(O=E.parts)==null?void 0:O[0])==null?void 0:F.statementEn)||E.statementEn||"").trim().toLowerCase();I&&!v.has(I)&&(v.add(I),y.push({...E,qNo:y.length+5}))}),{mcqs:f,shortQuestions:m,longQuestions:y,totalAvailableMCQs:f.length,totalAvailableShorts:m.length,totalAvailableLongs:y.length}}"""

w2_replacement = """function W2(n,e){const t=Wo.find(E=>E.id===n);if(!t)return{mcqs:[],shortQuestions:[],longQuestions:[],totalAvailableMCQs:0,totalAvailableShorts:0,totalAvailableLongs:0};const r=t.chapters.filter(E=>e.length===0||e.includes(E.number)),a=Z3().filter(E=>E.subjectId===n),o=[],A=[],u=[];const mqb=(typeof window!=="undefined"&&window.__PTBB_MASTER_QB__)||{};r.forEach((E,idx)=>{const k1=`${t.id}_ch${E.number}`,k2=`${t.id}_ch${E.id}`,k3=`${t.id}_ch${idx+1}`;const master=mqb[k1]||mqb[k2]||mqb[k3];const m_mcqs=master?master.mcqs.map(T=>({...T,chapterRef:E.number})):[];const m_sqs=master?master.shortQuestions.map(T=>({...T,chapterRef:E.number})):[];const m_lqs=master?master.longQuestions.map(T=>({...T,chapterRef:`Unit ${E.number}`})):[];const I=(E.mcqs||[]).map((T,H)=>({...T,chapterRef:E.number})),O=(E.shortQuestions||[]).map((T,H)=>({...T,chapterRef:E.number})),F=(E.longQuestions||[]).map((T,H)=>({id:T.id,totalMarks:9,parts:T.parts||[{partLabel:"a",statementEn:T.statementEn||"",statementUr:T.statementUr||"",marks:5}],chapterRef:`Unit ${E.number}`}));const R=master?{mcqs:[],shortQuestions:[],longQuestions:[]}:x8(t,E),Z=master?{mcqs:[],shortQuestions:[],longQuestions:[]}:C8(t,E);const oe=[...m_mcqs,...I,...Z.mcqs,...R.mcqs],ne=[...m_sqs,...O,...Z.shortQuestions,...R.shortQuestions],te=[...m_lqs,...F,...Z.longQuestions,...R.longQuestions];oe.forEach((T,H)=>{T.qNo=o.length+H+1}),ne.forEach((T,H)=>{T.subNo=A.length+H+1}),te.forEach((T,H)=>{T.qNo=u.length+H+5}),o.push(...oe),A.push(...ne),u.push(...te),a.filter(T=>T.chapterNo===E.number).forEach(T=>{T.type==="mcq"&&T.options&&T.correctOption?o.push({id:T.id,qNo:o.length+1,statementEn:T.statementEn,statementUr:T.statementUr,options:T.options,correctOption:T.correctOption,chapterRef:E.number}):T.type==="short"?A.push({id:T.id,subNo:A.length+1,statementEn:T.statementEn,statementUr:T.statementUr,marks:T.marks||2,chapterRef:E.number}):T.type==="long"&&u.push({id:T.id,qNo:u.length+5,totalMarks:T.marks||9,parts:[{partLabel:"a",statementEn:T.statementEn,statementUr:T.statementUr,marks:T.marks||5}],chapterRef:`Unit ${E.number}`})})});const f=[],B=new Set;o.forEach(E=>{const I=(E.statementEn||E.statementUr||"").trim().toLowerCase().replace(/[^a-z0-9؀-ۿ]/g,"");I&&!B.has(I)&&(B.add(I),f.push({...E,qNo:f.length+1}))});const m=[],C=new Set;A.forEach(E=>{const I=(E.statementEn||E.statementUr||"").trim().toLowerCase().replace(/[^a-z0-9؀-ۿ]/g,"");I&&!C.has(I)&&!B.has(I)&&(C.add(I),m.push({...E,subNo:m.length+1}))});const y=[],v=new Set;return u.forEach(E=>{var O,F;const I=(((F=(O=E.parts)==null?void 0:O[0])==null?void 0:F.statementEn)||E.statementEn||"").trim().toLowerCase().replace(/[^a-z0-9؀-ۿ]/g,"");I&&!v.has(I)&&(v.add(I),y.push({...E,qNo:y.length+5}))}),{mcqs:f,shortQuestions:m,longQuestions:y,totalAvailableMCQs:f.length,totalAvailableShorts:m.length,totalAvailableLongs:y.length}}"""

if w2_target in bundle:
    bundle = bundle.replace(w2_target, w2_replacement)
    print("Patched W2 to use window.__PTBB_MASTER_QB__ successfully.")
else:
    print("w2_target exact match failed, doing normalized replacement...")
    # fallback regex match
    pattern = r"function W2\(n,e\)\{const t=Wo\.find\(E=>E\.id===n\);.*?\btotalAvailableLongs:y\.length\}\}"
    m = re.search(pattern, bundle, re.DOTALL)
    if m:
        bundle = bundle[:m.start()] + w2_replacement + bundle[m.end():]
        print("Patched W2 via regex successfully.")
    else:
        print("Failed to patch W2 via regex")

with open("assets/index-DAioIUjd.js", "w", encoding="utf-8") as f:
    f.write(bundle)

print("Updated assets/index-DAioIUjd.js successfully.")
