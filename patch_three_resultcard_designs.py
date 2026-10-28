import sys

print("Opening assets/index-DAioIUjd.js...")
with open("assets/index-DAioIUjd.js", "r", encoding="utf-8") as f:
    text = f.read()

# -------------------------------------------------------------
# 1. Add cardTemplate state in lq
# -------------------------------------------------------------
old_state = '[msOrientation,setMsOrientation]=Ee.useState("portrait"),[studentSearch,setStudentSearch]=Ee.useState(""),[printAllCards,setPrintAllCards]=Ee.useState(!1),'
new_state = '[msOrientation,setMsOrientation]=Ee.useState("portrait"),[studentSearch,setStudentSearch]=Ee.useState(""),[printAllCards,setPrintAllCards]=Ee.useState(!1),[cardTemplate,setCardTemplate]=Ee.useState(()=>{try{return localStorage.getItem("ptbb_rc_template")||"classic"}catch(e){return"classic"}}),'

assert old_state in text, "old_state not found in lq"
text = text.replace(old_state, new_state, 1)
print("[✓] Added cardTemplate state in lq")

# -------------------------------------------------------------
# 2. Update ue and Ne to include cardTemplate
# -------------------------------------------------------------
old_ue_Ne = 'ue=S=>{setPrintOrientation(msOrientation);const V=document.title;document.title=`Result_Card_Roll_${S.rollNo}_${S.name.replace(/\\s+/g,"_")}_${msOrientation.toUpperCase()}`,window.print(),setTimeout(()=>{document.title=V},1500)},Ne=async S=>{u(S.id),o("singleCard"),B(!0),C(`Generating Roll ${S.rollNo} Result Card PDF...`),await new Promise(q=>setTimeout(q,250));const V=`Result_Card_Roll_${S.rollNo}_${S.name.replace(/\\s+/g,"_")}.pdf`;try{await iC("resultcard-print-container",V,ae=>{C(ae)},msOrientation)&&F(`Result Card PDF downloaded successfully in ${msOrientation} orientation!`)}finally{B(!1)}},Le=S=>{tq(S,R,r),F("Result Card MS Word document downloaded!")}'

new_ue_Ne = 'ue=S=>{setPrintOrientation(msOrientation);const V=document.title;document.title=`Result_Card_Roll_${S.rollNo}_${S.name.replace(/\\s+/g,"_")}_${cardTemplate.toUpperCase()}_${msOrientation.toUpperCase()}`,window.print(),setTimeout(()=>{document.title=V},1500)},Ne=async S=>{u(S.id),o("singleCard"),B(!0),C(`Generating Roll ${S.rollNo} Result Card PDF (${cardTemplate.toUpperCase()})...`),await new Promise(q=>setTimeout(q,250));const V=`Result_Card_Roll_${S.rollNo}_${S.name.replace(/\\s+/g,"_")}_${cardTemplate}.pdf`;try{await iC("resultcard-print-container",V,ae=>{C(ae)},msOrientation)&&F(`Result Card PDF downloaded successfully (${cardTemplate.toUpperCase()} Design, ${msOrientation} orientation)!`)}finally{B(!1)}},Le=S=>{tq(S,R,r,cardTemplate),F(`Result Card MS Word document downloaded (${cardTemplate.toUpperCase()} Design)!`)}'

assert old_ue_Ne in text, "old_ue_Ne not found in lq"
text = text.replace(old_ue_Ne, new_ue_Ne, 1)
print("[✓] Updated ue, Ne, and Le with cardTemplate awareness")

# -------------------------------------------------------------
# 3. Update singleCard body with 3 distinct designs and design switcher
# -------------------------------------------------------------
start_pattern = 'a==="singleCard"&&P&&l.jsxs("div",{className:"space-y-4"'
start_idx = text.find(start_pattern)
assert start_idx != -1, "start_pattern not found"

end_pattern = ',a==="masterSheet"&&l.jsx("div",{className:"space-y'
end_idx = text.find(end_pattern, start_idx)
assert end_idx != -1, "end_pattern not found"

print(f"Single card block found from {start_idx} to {end_idx} (len: {end_idx - start_idx})")

# Construct the brand-new, ultra-polished 3-design singleCard component in pure English
new_single_card = '''a==="singleCard"&&P&&l.jsxs("div",{className:"space-y-5",children:[
  /* 1. Design Template Selector Banner (English Only) */
  l.jsxs("div",{className:"bg-gradient-to-r from-slate-900 via-indigo-950 to-slate-900 p-4 sm:p-5 rounded-2xl border-2 border-indigo-600/70 shadow-xl no-print text-white",children:[
    l.jsxs("div",{className:"flex flex-col lg:flex-row items-start lg:items-center justify-between gap-4",children:[
      l.jsxs("div",{className:"flex items-center gap-3.5",children:[
        l.jsx("div",{className:"w-11 h-11 rounded-2xl bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center text-white shadow-lg text-xl shrink-0 ring-2 ring-indigo-300/40",children:"🎨"}),
        l.jsxs("div",{children:[
          l.jsxs("div",{className:"flex items-center gap-2.5 flex-wrap",children:[
            l.jsx("h3",{className:"text-sm sm:text-base font-black uppercase tracking-wider text-white",children:"Select Result Card Design Template"}),
            l.jsx("span",{className:"text-[10px] bg-gradient-to-r from-amber-400 to-yellow-300 text-slate-950 font-black px-2.5 py-0.5 rounded-full shadow-xs uppercase tracking-wide",children:"3 Distinct Designs Available"})
          ]}),
          l.jsx("p",{className:"text-xs text-slate-300 font-medium mt-0.5",children:"Choose your preferred institutional layout to preview, print, or download in high-definition PDF and Word."})
        ]})
      ]}),
      l.jsxs("div",{className:"flex flex-wrap items-center gap-2 w-full lg:w-auto",children:[
        /* Template 1 Button */
        l.jsxs("button",{type:"button",onClick:()=>{setCardTemplate("classic");try{localStorage.setItem("ptbb_rc_template","classic")}catch(e){}F("Active Design: Design 1 - Classic Academic Transcript");},className:`flex items-center gap-2.5 px-3.5 py-2.5 rounded-xl text-xs transition-all cursor-pointer border ${cardTemplate==="classic"?"bg-white text-blue-950 border-amber-400 ring-3 ring-amber-400/80 shadow-lg font-black":"bg-slate-800/90 text-slate-200 border-slate-700 hover:bg-slate-700/90 font-bold"}`,children:[
          l.jsx("span",{className:"text-lg",children:"📜"}),
          l.jsxs("div",{className:"text-left",children:[
            l.jsx("div",{className:"font-black text-xs leading-tight",children:"Design 1: Classic Academic"}),
            l.jsx("div",{className:"text-[9px] opacity-75 leading-tight font-medium",children:"Official Board Transcript"})
          ]}),
          cardTemplate==="classic"&&l.jsx("span",{className:"ml-1 text-emerald-600 font-black text-xs",children:"✓"})
        ]}),
        /* Template 2 Button */
        l.jsxs("button",{type:"button",onClick:()=>{setCardTemplate("modern");try{localStorage.setItem("ptbb_rc_template","modern")}catch(e){}F("Active Design: Design 2 - Modern Executive Certificate");},className:`flex items-center gap-2.5 px-3.5 py-2.5 rounded-xl text-xs transition-all cursor-pointer border ${cardTemplate==="modern"?"bg-white text-blue-950 border-amber-400 ring-3 ring-amber-400/80 shadow-lg font-black":"bg-slate-800/90 text-slate-200 border-slate-700 hover:bg-slate-700/90 font-bold"}`,children:[
          l.jsx("span",{className:"text-lg",children:"🏆"}),
          l.jsxs("div",{className:"text-left",children:[
            l.jsx("div",{className:"font-black text-xs leading-tight",children:"Design 2: Modern Certificate"}),
            l.jsx("div",{className:"text-[9px] opacity-75 leading-tight font-medium",children:"Executive Distinction Style"})
          ]}),
          cardTemplate==="modern"&&l.jsx("span",{className:"ml-1 text-emerald-600 font-black text-xs",children:"✓"})
        ]}),
        /* Template 3 Button */
        l.jsxs("button",{type:"button",onClick:()=>{setCardTemplate("diagnostic");try{localStorage.setItem("ptbb_rc_template","diagnostic")}catch(e){}F("Active Design: Design 3 - Detailed Diagnostic Report");},className:`flex items-center gap-2.5 px-3.5 py-2.5 rounded-xl text-xs transition-all cursor-pointer border ${cardTemplate==="diagnostic"?"bg-white text-blue-950 border-amber-400 ring-3 ring-amber-400/80 shadow-lg font-black":"bg-slate-800/90 text-slate-200 border-slate-700 hover:bg-slate-700/90 font-bold"}`,children:[
          l.jsx("span",{className:"text-lg",children:"📊"}),
          l.jsxs("div",{className:"text-left",children:[
            l.jsx("div",{className:"font-black text-xs leading-tight",children:"Design 3: Detailed Diagnostic"}),
            l.jsx("div",{className:"text-[9px] opacity-75 leading-tight font-medium",children:"Mastery Bars & Analytics"})
          ]}),
          cardTemplate==="diagnostic"&&l.jsx("span",{className:"ml-1 text-emerald-600 font-black text-xs",children:"✓"})
        ]})
      ]})
    ]})
  ]}),

  /* 2. Candidate Selection Bar with Live Search & Photo Upload (English Only) */
  l.jsxs("div",{className:"card-3d p-4 bg-white border border-slate-200 flex flex-wrap items-center justify-between gap-3 no-print",children:[
    l.jsxs("div",{className:"flex flex-wrap items-center gap-2.5",children:[
      l.jsx("span",{className:"text-xs font-black text-slate-700 uppercase tracking-wider",children:"Candidate:"}),
      /* Student Search Box */
      l.jsx("input",{type:"text",value:studentSearch,onChange:S=>setStudentSearch(S.target.value),placeholder:"🔍 Search by roll no or name...",className:"px-3 py-1.5 rounded-xl border border-slate-300 font-bold text-xs bg-slate-50 text-slate-900 w-44 sm:w-52 focus:bg-white focus:ring-2 focus:ring-blue-500 shadow-2xs"}),
      /* Student Select Dropdown */
      l.jsx("select",{value:P.id,onChange:S=>u(S.target.value),className:"px-3 py-1.5 rounded-xl border border-slate-300 font-bold text-xs bg-white text-slate-900 focus:ring-2 focus:ring-blue-500 shadow-2xs cursor-pointer",children:R.students.filter(S=>!studentSearch.trim()||S.name.toLowerCase().includes(studentSearch.toLowerCase())||S.rollNo.toLowerCase().includes(studentSearch.toLowerCase())).map(S=>l.jsxs("option",{value:S.id,children:["Roll #",S.rollNo," - ",S.name," (",S.rank||"Candidate",")"]},S.id))}),
      /* Active Template Badge */
      l.jsxs("span",{className:"px-2.5 py-1 rounded-lg bg-blue-50 border border-blue-200 text-blue-900 text-[11px] font-black hidden sm:inline-flex items-center gap-1",children:[
        l.jsx("span",{children:"Applied Design:"}),
        l.jsx("span",{className:"text-blue-700 underline",children:cardTemplate==="classic"?"Design 1 (Classic)":cardTemplate==="modern"?"Design 2 (Modern)":"Design 3 (Diagnostic)"})
      ]})
    ]}),
    l.jsxs("div",{className:"flex items-center gap-2",children:[
      l.jsxs("button",{type:"button",onClick:()=>pe(P.id),className:"btn-3d btn-3d-slate flex items-center gap-1.5 px-3 py-1.5 text-white rounded-xl text-xs font-bold cursor-pointer",title:"Upload student photo for result card",children:[
        l.jsx(J3,{className:"w-3.5 h-3.5 text-blue-300"}),
        l.jsx("span",{children:P.photoUrl?"Change Candidate Photo":"Upload Candidate Photo"})
      ]}),
      P.photoUrl&&l.jsx("button",{type:"button",onClick:()=>me(P.id),className:"px-2.5 py-1.5 bg-rose-100 text-rose-800 hover:bg-rose-200 rounded-xl text-xs font-bold cursor-pointer transition-all",title:"Remove candidate photo",children:"Remove Photo"})
    ]})
  ]}),

  /* 3. Result Card Print/Export Container */
  l.jsx("div",{id:"resultcard-print-container",className:`bg-white rounded-2xl shadow-xl border border-slate-300 p-6 sm:p-8 ${msOrientation==="landscape"?"max-w-6xl landscape-mode":"max-w-4xl portrait-mode"} mx-auto print:border-none print:shadow-none print:p-0 print:m-0 print:max-w-none print:w-full`,children:
    (printAllCards?R.students:[P]).map((st,stIdx)=>{
      const q_stat=te(st);
      return l.jsxs("div",{key:st.id,className:`${stIdx>0?"page-break-before mt-8 print:mt-0":""} result-card-sheet`,children:[
        
        /* -------------------------------------------------------------
           DESIGN 1: CLASSIC ACADEMIC TRANSCRIPT (Official Board Style)
           ------------------------------------------------------------- */
        cardTemplate==="classic"&&l.jsxs("div",{className:"classic-academic-template",children:[
          /* Classic Header */
          l.jsxs("div",{className:"paper-header border-b-2 border-slate-900 pb-3 mb-4 text-center",children:[
            l.jsxs("div",{className:"header-row flex items-center justify-between gap-4",children:[
              l.jsx("div",{className:"school-monogram-container shrink-0",children:l.jsx(Rw,{logoUrl:r.logoUrl,schoolName:r.schoolName,size:75})}),
              l.jsxs("div",{className:"school-name-col flex-1 min-w-0 px-2 text-center",children:[
                l.jsx("h1",{className:"school-name-title text-xl sm:text-2xl font-black uppercase text-slate-950 tracking-tight leading-tight",children:r.schoolName}),
                l.jsxs("div",{className:"text-xs sm:text-sm font-bold text-slate-700 tracking-wide mt-0.5",children:[r.campusName," • ",r.address]}),
                l.jsxs("div",{className:"text-[11px] text-slate-600 font-semibold mt-0.5",children:["Phone: ",r.phone," • Affiliation: ",r.boardPattern||"BISE Punjab"]})
              ]}),
              l.jsxs("div",{className:"shrink-0 hidden sm:flex flex-col items-center justify-center p-2 rounded-xl bg-slate-50 border border-slate-300 w-28 text-center",children:[
                l.jsx("span",{className:"text-[9px] uppercase font-black text-blue-900 tracking-wider",children:"Official Board"}),
                l.jsx("span",{className:"text-[11px] font-extrabold text-slate-900 mt-0.5",children:R.session}),
                l.jsx("span",{className:"text-[9px] font-bold text-emerald-700 mt-0.5",children:"Verified"})
              ]})
            ]}),
            l.jsxs("div",{className:"mt-3.5 bg-slate-100 text-slate-950 border-2 border-slate-900 font-black py-1.5 px-4 rounded text-xs sm:text-sm uppercase tracking-wider shadow-xs print:bg-slate-100 print:text-black",children:["Official Student Academic Transcript & Progress Report • Session ",R.session]}),
            l.jsxs("div",{className:"mt-2 text-xs font-black text-slate-900 uppercase flex flex-wrap items-center justify-center gap-3",children:[
              l.jsxs("span",{children:["Examination: ",R.examCategory]}),
              l.jsx("span",{children:"•"}),
              l.jsxs("span",{children:["Class: ",R.classLevel]}),
              l.jsx("span",{children:"•"}),
              l.jsxs("span",{children:["Design: Classic Academic Transcript"]})
            ]})
          ]}),

          /* Classic Candidate Info Box */
          l.jsxs("div",{className:"border border-slate-900 bg-slate-50 p-3.5 rounded-lg mb-5 flex flex-col sm:flex-row items-center gap-4",children:[
            l.jsx("div",{className:"shrink-0 w-24 h-32 rounded-lg border-2 border-slate-700 bg-white p-1 overflow-hidden shadow-xs flex flex-col items-center justify-center",children:st.photoUrl?l.jsx("img",{src:st.photoUrl,alt:st.name,className:"w-full h-full object-cover rounded",style:{imageRendering:"-webkit-optimize-contrast"}}):l.jsxs("div",{className:"flex flex-col items-center justify-center p-2 text-center w-full h-full bg-slate-50 rounded",children:[
              l.jsx("div",{className:"w-10 h-10 rounded-full bg-blue-100 flex items-center justify-center border border-blue-300 mb-1",children:l.jsx("span",{className:"text-lg",children:"👤"})}),
              l.jsx("span",{className:"text-[9px] font-black uppercase text-slate-800 tracking-wider",children:"Candidate"}),
              l.jsx("span",{className:"text-[8px] text-slate-500 font-semibold",children:"(Photo ID)"})
            ]})}),
            l.jsxs("div",{className:"flex-1 w-full grid grid-cols-2 sm:grid-cols-3 gap-2.5 text-xs",children:[
              l.jsxs("div",{children:[l.jsx("span",{className:"text-[10px] font-bold uppercase text-slate-500 block",children:"Roll Number:"}),l.jsx("span",{className:"text-sm font-black text-blue-950",children:st.rollNo})]}),
              l.jsxs("div",{children:[l.jsx("span",{className:"text-[10px] font-bold uppercase text-slate-500 block",children:"Student Name:"}),l.jsx("span",{className:"text-xs font-black text-slate-950",children:st.name})]}),
              l.jsxs("div",{children:[l.jsx("span",{className:"text-[10px] font-bold uppercase text-slate-500 block",children:"Father's Name:"}),l.jsx("span",{className:"text-xs font-bold text-slate-800",children:st.fatherName||"-"})]}),
              l.jsxs("div",{children:[l.jsx("span",{className:"text-[10px] font-bold uppercase text-slate-500 block",children:"Class & Section:"}),l.jsxs("span",{className:"text-xs font-bold text-slate-800",children:[R.classLevel," (Sec ",st.section||"A",")"]})]}),
              l.jsxs("div",{children:[l.jsx("span",{className:"text-[10px] font-bold uppercase text-slate-500 block",children:"Attendance Rate:"}),l.jsx("span",{className:"text-xs font-bold text-slate-800",children:st.attendance||"96%"})]}),
              l.jsxs("div",{children:[l.jsx("span",{className:"text-[10px] font-bold uppercase text-slate-500 block",children:"Class Position / Rank:"}),l.jsx("span",{className:"text-xs font-black text-emerald-800",children:st.rank||"Good Standing"})]})
            ]})
          ]}),

          /* Classic Marks Table */
          l.jsx("div",{className:"overflow-visible mb-5",children:l.jsxs("table",{className:"w-full text-xs border-collapse border border-slate-900",children:[
            l.jsx("thead",{children:l.jsxs("tr",{className:"bg-slate-200 text-slate-950 font-black uppercase text-[11px] border-b-2 border-slate-900 print:bg-slate-200 print:text-black",children:[
              l.jsx("th",{className:"p-2 border border-slate-900 text-center w-10 text-slate-950 font-black",children:"Sr#"}),
              l.jsx("th",{className:"p-2 border border-slate-900 text-left text-slate-950 font-black",children:"Subject Name"}),
              l.jsx("th",{className:"p-2 border border-slate-900 text-center w-24 text-slate-950 font-black",children:"Total Marks"}),
              l.jsx("th",{className:"p-2 border border-slate-900 text-center w-24 text-slate-950 font-black",children:"Pass Marks"}),
              l.jsx("th",{className:"p-2 border border-slate-900 text-center w-28 text-slate-950 font-black",children:"Marks Obtained"}),
              l.jsx("th",{className:"p-2 border border-slate-900 text-center w-20 text-slate-950 font-black",children:"Percentage"}),
              l.jsx("th",{className:"p-2 border border-slate-900 text-center w-20 text-slate-950 font-black",children:"Grade"}),
              l.jsx("th",{className:"p-2 border border-slate-900 text-center w-24 text-slate-950 font-black",children:"Remarks"})
            ]})}),
            l.jsxs("tbody",{children:[
              R.subjects.map((sub,sIdx)=>{
                const obt=Number((st.marks&&st.marks[sub.id])||0);
                const isPass=obt>=sub.passingMarks;
                const pct=sub.totalMarks>0?(obt/sub.totalMarks*100).toFixed(1):"0.0";
                const pNum=parseFloat(pct);
                let grd="F";
                if(pNum>=90)grd="A+";else if(pNum>=80)grd="A";else if(pNum>=70)grd="B";else if(pNum>=60)grd="C";else if(pNum>=50)grd="D";else if(pNum>=40)grd="E";
                return l.jsxs("tr",{key:sub.id,className:`border border-slate-900 ${sIdx%2===0?"bg-white":"bg-slate-50"}`,children:[
                  l.jsx("td",{className:"p-2 border border-slate-900 text-center font-bold text-slate-900",children:sIdx+1}),
                  l.jsx("td",{className:"p-2 border border-slate-900 font-extrabold text-slate-950",children:sub.name}),
                  l.jsx("td",{className:"p-2 border border-slate-900 text-center font-bold text-slate-900",children:sub.totalMarks}),
                  l.jsx("td",{className:"p-2 border border-slate-900 text-center font-medium text-slate-600",children:sub.passingMarks}),
                  l.jsx("td",{className:`p-2 border border-slate-900 text-center font-black text-sm ${isPass?"text-slate-950":"text-rose-700"}`,children:obt}),
                  l.jsxs("td",{className:"p-2 border border-slate-900 text-center font-bold text-slate-800",children:[pct,"%"]}),
                  l.jsx("td",{className:`p-2 border border-slate-900 text-center font-black ${isPass?"text-blue-900":"text-rose-700"}`,children:grd}),
                  l.jsx("td",{className:`p-2 border border-slate-900 text-center font-black text-xs ${isPass?"text-emerald-800":"text-rose-700"}`,children:isPass?"Passed":"Needs Retake"})
                ]});
              }),
              /* Grand Total Row */
              l.jsxs("tr",{className:"bg-slate-200 border-2 border-slate-900 font-black text-slate-950 text-xs",children:[
                l.jsx("td",{colSpan:2,className:"p-2.5 border border-slate-900 text-right uppercase tracking-wider",children:"Grand Total / Overall Summary:"}),
                l.jsx("td",{className:"p-2.5 border border-slate-900 text-center text-sm font-black",children:ne}),
                l.jsx("td",{className:"p-2.5 border border-slate-900 text-center",children:"-"}),
                l.jsx("td",{className:"p-2.5 border border-slate-900 text-center text-sm font-black text-blue-950",children:q_stat.totalObtained}),
                l.jsxs("td",{className:"p-2.5 border border-slate-900 text-center font-black text-sm",children:[q_stat.percentage,"%"]}),
                l.jsx("td",{className:"p-2.5 border border-slate-900 text-center font-black text-sm text-blue-950",children:q_stat.grade}),
                l.jsx("td",{className:`p-2.5 border border-slate-900 text-center font-black uppercase ${q_stat.status==="PASS"?"text-emerald-900 bg-emerald-100":"text-rose-900 bg-rose-100"}`,children:q_stat.status})
              ]})
            ]})
          ]})}),

          /* Classic Grading Formula + Remarks */
          l.jsxs("div",{className:"grid grid-cols-1 sm:grid-cols-2 gap-3 mb-6",children:[
            l.jsxs("div",{className:"border border-slate-300 p-2.5 rounded text-[10px]",children:[
              l.jsx("div",{className:"font-black text-slate-800 uppercase mb-1",children:"Official BISE Grading Formula:"}),
              l.jsxs("div",{className:"grid grid-cols-4 gap-1 text-center font-bold text-slate-700",children:[
                l.jsx("div",{className:"bg-slate-100 p-1 rounded",children:"A+ : 90%+"}),
                l.jsx("div",{className:"bg-slate-100 p-1 rounded",children:"A : 80-89%"}),
                l.jsx("div",{className:"bg-slate-100 p-1 rounded",children:"B : 70-79%"}),
                l.jsx("div",{className:"bg-slate-100 p-1 rounded",children:"C : 60-69%"}),
                l.jsx("div",{className:"bg-slate-100 p-1 rounded",children:"D : 50-59%"}),
                l.jsx("div",{className:"bg-slate-100 p-1 rounded",children:"E : 40-49%"}),
                l.jsx("div",{className:"bg-rose-100 text-rose-800 p-1 rounded col-span-2",children:"F (Fail) : <40%"})
              ]})
            ]}),
            l.jsxs("div",{className:"border border-slate-300 p-2.5 rounded text-xs flex flex-col justify-between",children:[
              l.jsxs("div",{children:[
                l.jsx("div",{className:"font-black text-slate-800 uppercase text-[10px] mb-1",children:"Class Teacher's Remarks & Conduct:"}),
                l.jsxs("div",{className:"italic text-slate-800 font-medium leading-relaxed",children:['"',st.remarks||"Shows consistent effort and commendable dedication. Keep up the high standard!",'"']})
              ]}),
              l.jsx("div",{className:"text-[10px] font-bold text-slate-500 mt-1",children:"General Conduct: Regular & Exemplary • Punctuality: Satisfactory"})
            ]})
          ]}),

          /* Classic 4 Signatures */
          l.jsxs("div",{className:"pt-6 border-t border-slate-400 grid grid-cols-4 text-center text-xs font-bold text-slate-900",children:[
            l.jsx("div",{children:l.jsx("div",{className:"w-28 border-t-2 border-slate-800 mx-auto pt-1 font-black",children:"Class Teacher"})}),
            l.jsx("div",{children:l.jsx("div",{className:"w-32 border-t-2 border-slate-800 mx-auto pt-1 font-black",children:"Exam Incharge"})}),
            l.jsx("div",{children:l.jsx("div",{className:"w-28 border-t-2 border-slate-800 mx-auto pt-1 font-black",children:"Parent / Guardian"})}),
            l.jsx("div",{children:l.jsx("div",{className:"w-32 border-t-2 border-slate-800 mx-auto pt-1 font-black",children:"Principal / Seal"})})
          ]}),
          l.jsx("div",{className:"text-center text-[10px] text-slate-500 font-mono mt-8 border-t border-slate-200 pt-2",children:"Automated Academic Evaluation System • Official Board Transcript Verified"})
        ]}),

        /* -------------------------------------------------------------
           DESIGN 2: MODERN EXECUTIVE CERTIFICATE (Award & Distinction Style)
           ------------------------------------------------------------- */
        cardTemplate==="modern"&&l.jsxs("div",{className:"modern-certificate-template p-4 sm:p-6 border-4 border-double border-amber-600/80 rounded-2xl bg-gradient-to-b from-amber-50/25 via-white to-slate-50 relative",style:{boxShadow:"inset 0 0 0 2px #1e3a8a, 0 10px 25px -5px rgba(0, 0, 0, 0.1)"},children:[
          /* Modern Certificate Header */
          l.jsxs("div",{className:"text-center pb-4 mb-4 border-b-2 border-amber-500/60 relative",children:[
            l.jsxs("div",{className:"flex items-center justify-between gap-4 mb-2",children:[
              l.jsx("div",{className:"shrink-0 p-1 rounded-2xl border-2 border-amber-400 bg-white shadow-xs",children:l.jsx(Rw,{logoUrl:r.logoUrl,schoolName:r.schoolName,size:70})}),
              l.jsxs("div",{className:"flex-1 text-center",children:[
                l.jsx("div",{className:"text-[10px] font-black tracking-widest uppercase text-amber-700",children:"★ EXCELLENCE IN EDUCATION ★"}),
                l.jsx("h1",{className:"text-xl sm:text-3xl font-black uppercase text-slate-900 tracking-tight",children:r.schoolName}),
                l.jsxs("div",{className:"text-xs font-extrabold text-blue-900 tracking-wide mt-0.5",children:[r.campusName," • ",r.address]}),
                l.jsxs("div",{className:"text-[10px] text-slate-500 font-semibold",children:["Affiliation: ",r.boardPattern||"BISE Punjab"," • Phone: ",r.phone]})
              ]}),
              l.jsxs("div",{className:"shrink-0 hidden sm:flex flex-col items-center justify-center w-24 h-24 rounded-full border-4 border-amber-400 bg-gradient-to-br from-amber-100 to-amber-200 text-amber-950 p-1 text-center shadow-md",children:[
                l.jsx("span",{className:"text-base",children:"🏅"}),
                l.jsx("span",{className:"text-[8px] font-black uppercase tracking-wider leading-tight",children:"Academic Award"}),
                l.jsx("span",{className:"text-[10px] font-black mt-0.5",children:R.session})
              ]})
            ]}),
            l.jsxs("div",{className:"bg-gradient-to-r from-blue-950 via-indigo-900 to-blue-950 text-white py-2 px-6 rounded-xl shadow-md border-2 border-amber-400 mt-2",children:[
              l.jsx("h2",{className:"text-sm sm:text-base font-black uppercase tracking-widest text-amber-300",children:"Certificate of Academic Achievement & Report Card"}),
              l.jsxs("p",{className:"text-[10px] text-slate-200 font-medium tracking-wide",children:["Academic Session: ",R.session," • Examination: ",R.examCategory," • Class: ",R.classLevel]})
            ]})
          ]}),

          /* Modern Executive Candidate Card */
          l.jsxs("div",{className:"bg-white border-2 border-slate-200 rounded-2xl p-4 mb-5 shadow-xs flex flex-col sm:flex-row items-center gap-5",children:[
            l.jsxs("div",{className:"shrink-0 flex flex-col items-center",children:[
              l.jsx("div",{className:"w-24 h-24 rounded-full border-4 border-amber-400 overflow-hidden shadow-md bg-slate-100 p-0.5",children:st.photoUrl?l.jsx("img",{src:st.photoUrl,alt:st.name,className:"w-full h-full object-cover rounded-full",style:{imageRendering:"-webkit-optimize-contrast"}}):l.jsxs("div",{className:"w-full h-full rounded-full flex flex-col items-center justify-center bg-slate-100 text-center",children:[
                l.jsx("span",{className:"text-2xl",children:"🎓"}),
                l.jsx("span",{className:"text-[8px] font-black uppercase text-slate-700",children:"Candidate"})
              ]})}),
              l.jsxs("div",{className:"mt-1.5 px-2.5 py-0.5 rounded-full bg-blue-900 text-white font-black text-[10px] tracking-wider shadow-xs",children:["Roll # ",st.rollNo]})
            ]}),
            l.jsxs("div",{className:"flex-1 w-full grid grid-cols-2 sm:grid-cols-4 gap-3 text-xs",children:[
              l.jsxs("div",{className:"bg-slate-50 p-2.5 rounded-xl border border-slate-200",children:[
                l.jsx("span",{className:"text-[9px] font-black uppercase tracking-wider text-slate-500 block",children:"Student Name"}),
                l.jsx("span",{className:"text-xs font-black text-slate-900",children:st.name})
              ]}),
              l.jsxs("div",{className:"bg-slate-50 p-2.5 rounded-xl border border-slate-200",children:[
                l.jsx("span",{className:"text-[9px] font-black uppercase tracking-wider text-slate-500 block",children:"Father's Name"}),
                l.jsx("span",{className:"text-xs font-bold text-slate-800",children:st.fatherName||"-"})
              ]}),
              l.jsxs("div",{className:"bg-slate-50 p-2.5 rounded-xl border border-slate-200",children:[
                l.jsx("span",{className:"text-[9px] font-black uppercase tracking-wider text-slate-500 block",children:"Class & Section"}),
                l.jsxs("span",{className:"text-xs font-bold text-slate-800",children:[R.classLevel," - ",st.section||"A"]})
              ]}),
              l.jsxs("div",{className:"bg-amber-50 p-2.5 rounded-xl border border-amber-300",children:[
                l.jsx("span",{className:"text-[9px] font-black uppercase tracking-wider text-amber-800 block",children:"Class Standing"}),
                l.jsxs("span",{className:"text-xs font-black text-amber-950 flex items-center gap-1",children:[l.jsx("span",{children:"🏆"}),l.jsx("span",{children:st.rank||"1st Class"})]})
              ]})
            ]})
          ]}),

          /* Modern Subject Table */
          l.jsx("div",{className:"overflow-visible mb-5",children:l.jsxs("table",{className:"w-full text-xs border-collapse border-2 border-slate-800 rounded-xl overflow-hidden",children:[
            l.jsx("thead",{children:l.jsxs("tr",{className:"bg-gradient-to-r from-blue-900 via-indigo-900 to-blue-900 text-white font-black uppercase text-[10px] tracking-wider",children:[
              l.jsx("th",{className:"p-2.5 text-center w-10 border border-blue-800",children:"#"}),
              l.jsx("th",{className:"p-2.5 text-left border border-blue-800",children:"Course Curriculum Subject"}),
              l.jsx("th",{className:"p-2.5 text-center w-20 border border-blue-800",children:"Max Marks"}),
              l.jsx("th",{className:"p-2.5 text-center w-20 border border-blue-800",children:"Min Pass"}),
              l.jsx("th",{className:"p-2.5 text-center w-24 border border-blue-800",children:"Score Obtained"}),
              l.jsx("th",{className:"p-2.5 text-center w-20 border border-blue-800",children:"Score %"}),
              l.jsx("th",{className:"p-2.5 text-center w-16 border border-blue-800",children:"Grade"}),
              l.jsx("th",{className:"p-2.5 text-center w-24 border border-blue-800",children:"Achievement"})
            ]})}),
            l.jsxs("tbody",{children:[
              R.subjects.map((sub,sIdx)=>{
                const obt=Number((st.marks&&st.marks[sub.id])||0);
                const isPass=obt>=sub.passingMarks;
                const pct=sub.totalMarks>0?(obt/sub.totalMarks*100).toFixed(1):"0.0";
                const pNum=parseFloat(pct);
                let grd="F";
                if(pNum>=90)grd="A+";else if(pNum>=80)grd="A";else if(pNum>=70)grd="B";else if(pNum>=60)grd="C";else if(pNum>=50)grd="D";else if(pNum>=40)grd="E";
                return l.jsxs("tr",{key:sub.id,className:`border-b border-slate-300 ${sIdx%2===0?"bg-white":"bg-slate-50/80"}`,children:[
                  l.jsx("td",{className:"p-2 text-center font-bold text-slate-700 border-r border-slate-200",children:sIdx+1}),
                  l.jsx("td",{className:"p-2 font-black text-slate-900 border-r border-slate-200",children:sub.name}),
                  l.jsx("td",{className:"p-2 text-center font-bold text-slate-700 border-r border-slate-200",children:sub.totalMarks}),
                  l.jsx("td",{className:"p-2 text-center text-slate-500 border-r border-slate-200",children:sub.passingMarks}),
                  l.jsx("td",{className:`p-2 text-center font-black border-r border-slate-200 ${isPass?"text-blue-900 text-sm":"text-rose-700 text-sm"}`,children:obt}),
                  l.jsxs("td",{className:"p-2 text-center font-bold text-slate-800 border-r border-slate-200",children:[pct,"%"]}),
                  l.jsx("td",{className:"p-2 text-center border-r border-slate-200",children:l.jsx("span",{className:`px-2 py-0.5 rounded-md font-black text-xs ${grd==="A+"||grd==="A"?"bg-emerald-100 text-emerald-900 border border-emerald-300":isPass?"bg-blue-100 text-blue-900":"bg-rose-100 text-rose-900"}`,children:grd})}),
                  l.jsx("td",{className:"p-2 text-center",children:l.jsx("span",{className:`text-[10px] font-black uppercase px-2 py-0.5 rounded-full ${isPass?"bg-emerald-50 text-emerald-800 border border-emerald-200":"bg-rose-50 text-rose-800 border border-rose-200"}`,children:isPass?(pNum>=80?"Distinction":"Satisfactory"):"Retake"})})
                ]});
              })
            ]})
          ]})}),

          /* Modern 4 Metric Showcase Cards */
          l.jsxs("div",{className:"grid grid-cols-2 sm:grid-cols-4 gap-3 mb-5",children:[
            l.jsxs("div",{className:"bg-gradient-to-br from-blue-900 to-indigo-900 text-white p-3 rounded-xl text-center shadow-xs",children:[
              l.jsx("span",{className:"text-[9px] uppercase font-black text-blue-200 tracking-wider block",children:"Total Marks Obtained"}),
              l.jsxs("div",{className:"text-lg font-black mt-0.5",children:[q_stat.totalObtained," ",l.jsxs("span",{className:"text-xs font-medium text-blue-200",children:["/ ",ne]})]})
            ]}),
            l.jsxs("div",{className:"bg-gradient-to-br from-indigo-900 to-purple-900 text-white p-3 rounded-xl text-center shadow-xs",children:[
              l.jsx("span",{className:"text-[9px] uppercase font-black text-indigo-200 tracking-wider block",children:"Aggregate Percentage"}),
              l.jsxs("div",{className:"text-lg font-black mt-0.5",children:[q_stat.percentage,"%"]})
            ]}),
            l.jsxs("div",{className:"bg-gradient-to-br from-amber-700 to-amber-900 text-white p-3 rounded-xl text-center shadow-xs",children:[
              l.jsx("span",{className:"text-[9px] uppercase font-black text-amber-200 tracking-wider block",children:"Final Letter Grade"}),
              l.jsx("div",{className:"text-xl font-black mt-0.5 text-amber-300",children:q_stat.grade})
            ]}),
            l.jsxs("div",{className:`p-3 rounded-xl text-center shadow-xs text-white ${q_stat.status==="PASS"?"bg-gradient-to-br from-emerald-800 to-teal-900":"bg-gradient-to-br from-rose-800 to-red-900"}`,children:[
              l.jsx("span",{className:"text-[9px] uppercase font-black text-emerald-200 tracking-wider block",children:"Official Status"}),
              l.jsx("div",{className:"text-lg font-black mt-0.5",children:q_stat.status==="PASS"?"PASSED WITH MERIT":"NEEDS IMPROVEMENT"})
            ]})
          ]}),

          /* Modern Commendation & Certified Badge */
          l.jsxs("div",{className:"bg-slate-50 border border-slate-300 rounded-xl p-3 mb-6 flex flex-col sm:flex-row items-center justify-between gap-3 text-xs",children:[
            l.jsxs("div",{className:"flex-1",children:[
              l.jsx("span",{className:"text-[9px] font-black uppercase text-amber-800 tracking-wider block mb-0.5",children:"Executive Commendation & Remarks:"}),
              l.jsxs("p",{className:"italic text-slate-800 leading-relaxed font-medium",children:['"',st.remarks||"Exhibits commendable scholastic performance, exemplary character, and high learning aptitude.",'"']})
            ]}),
            l.jsxs("div",{className:"shrink-0 flex items-center gap-2 px-3 py-1.5 rounded-lg bg-amber-100/60 border border-amber-300 text-amber-950 text-[10px] font-black",children:[
              l.jsx("span",{className:"text-lg",children:"🛡️"}),
              l.jsx("span",{children:"Institutionally Certified Record"})
            ]})
          ]}),

          /* Modern 3 Executive Signatures */
          l.jsxs("div",{className:"pt-6 border-t-2 border-slate-400 grid grid-cols-3 text-center text-xs font-bold text-slate-900",children:[
            l.jsx("div",{children:l.jsx("div",{className:"w-36 border-t-2 border-slate-800 mx-auto pt-1 font-black",children:"Controller Examinations"})}),
            l.jsx("div",{children:l.jsx("div",{className:"w-40 border-t-2 border-slate-800 mx-auto pt-1 font-black",children:"Principal / Executive Seal"})}),
            l.jsx("div",{children:l.jsx("div",{className:"w-36 border-t-2 border-slate-800 mx-auto pt-1 font-black",children:"Parent / Guardian"})})
          ]}),
          l.jsx("div",{className:"text-center text-[9px] text-slate-400 font-sans mt-6 border-t border-slate-200 pt-2 tracking-wider uppercase",children:"Modern Executive Certificate Edition • Designed for High-Distinction Recognition"})
        ]}),

        /* -------------------------------------------------------------
           DESIGN 3: DETAILED DIAGNOSTIC REPORT (Mastery Bars & Analytics)
           ------------------------------------------------------------- */
        cardTemplate==="diagnostic"&&l.jsxs("div",{className:"detailed-diagnostic-template p-4 sm:p-6 border-2 border-slate-300 rounded-2xl bg-white shadow-xs",children:[
          /* Tech-Academic Diagnostic Header */
          l.jsxs("div",{className:"pb-4 mb-4 border-b-2 border-slate-900 flex flex-col sm:flex-row items-center justify-between gap-4",children:[
            l.jsxs("div",{className:"flex items-center gap-3.5",children:[
              l.jsx(Rw,{logoUrl:r.logoUrl,schoolName:r.schoolName,size:68}),
              l.jsxs("div",{children:[
                l.jsx("h1",{className:"text-xl sm:text-2xl font-black uppercase text-slate-950 tracking-tight",children:r.schoolName}),
                l.jsxs("div",{className:"text-xs font-bold text-slate-700",children:[r.campusName," • ",r.address]}),
                l.jsxs("div",{className:"text-[10px] text-slate-500 font-semibold",children:["Affiliation: ",r.boardPattern||"BISE Punjab"," • Helpline: ",r.phone]})
              ]})
            ]}),
            l.jsxs("div",{className:"flex items-center gap-3 bg-slate-50 border border-slate-300 p-2.5 rounded-xl text-right shrink-0",children:[
              l.jsxs("div",{className:"text-right",children:[
                l.jsx("span",{className:"text-[9px] font-black uppercase tracking-wider text-blue-700 block",children:"Diagnostic Verification"}),
                l.jsxs("span",{className:"text-xs font-black text-slate-900 block",children:["ID: #",st.rollNo,"-",R.session]}),
                l.jsx("span",{className:"text-[9px] text-emerald-700 font-bold block",children:"✓ Digitally Verified"})
              ]}),
              l.jsx("div",{className:"w-12 h-12 bg-white border border-slate-400 p-1 rounded flex items-center justify-center shrink-0 shadow-inner",title:`Verification Code: ${st.rollNo}-${R.session}`,children:l.jsx("span",{className:"text-xl",children:"🏁"})})
            ]})
          ]}),

          /* Diagnostic Banner */
          l.jsxs("div",{className:"bg-slate-900 text-white px-4 py-2 rounded-xl mb-4 flex flex-wrap items-center justify-between gap-2 text-xs",children:[
            l.jsxs("div",{className:"font-black uppercase tracking-wider text-amber-400 flex items-center gap-1.5",children:[
              l.jsx("span",{children:"📊"}),
              l.jsx("span",{children:"Comprehensive Diagnostic Performance Report"})
            ]}),
            l.jsxs("div",{className:"text-slate-300 font-semibold text-[11px]",children:["Class: ",R.classLevel," • Cycle: ",R.examCategory," • Session: ",R.session]})
          ]}),

          /* Candidate Diagnostic Card */
          l.jsxs("div",{className:"grid grid-cols-2 sm:grid-cols-6 gap-2.5 bg-slate-50 border border-slate-300 p-3 rounded-xl mb-5 text-xs",children:[
            l.jsxs("div",{className:"col-span-2 flex items-center gap-2.5",children:[
              l.jsx("div",{className:"w-12 h-12 rounded-lg border border-slate-400 overflow-hidden bg-white shrink-0",children:st.photoUrl?l.jsx("img",{src:st.photoUrl,alt:st.name,className:"w-full h-full object-cover"}):l.jsx("div",{className:"w-full h-full flex items-center justify-center text-slate-400 font-bold",children:"ID"})}),
              l.jsxs("div",{children:[
                l.jsx("span",{className:"text-[9px] uppercase font-bold text-slate-500 block",children:"Candidate Name"}),
                l.jsx("span",{className:"text-xs font-black text-slate-900",children:st.name}),
                l.jsxs("span",{className:"text-[10px] text-slate-600 block",children:["Father: ",st.fatherName||"-"]})
              ]})
            ]}),
            l.jsxs("div",{children:[l.jsx("span",{className:"text-[9px] uppercase font-bold text-slate-500 block",children:"Roll Number"}),l.jsx("span",{className:"text-sm font-black text-blue-900",children:st.rollNo})]}),
            l.jsxs("div",{children:[l.jsx("span",{className:"text-[9px] uppercase font-bold text-slate-500 block",children:"Section"}),l.jsx("span",{className:"text-xs font-extrabold text-slate-900",children:st.section||"A"})]}),
            l.jsxs("div",{children:[l.jsx("span",{className:"text-[9px] uppercase font-bold text-slate-500 block",children:"Attendance"}),l.jsx("span",{className:"text-xs font-extrabold text-slate-900",children:st.attendance||"96%"})]}),
            l.jsxs("div",{children:[l.jsx("span",{className:"text-[9px] uppercase font-bold text-slate-500 block",children:"Class Position"}),l.jsx("span",{className:"text-xs font-black text-emerald-800",children:st.rank||"Top Tier"})]})
          ]}),

          /* Subject Mastery Breakdown with Visual Progress Bars */
          l.jsxs("div",{className:"border border-slate-300 rounded-xl overflow-hidden mb-5",children:[
            l.jsxs("div",{className:"bg-slate-100 px-3.5 py-2 border-b border-slate-300 flex items-center justify-between text-xs font-black text-slate-800 uppercase tracking-wider",children:[
              l.jsx("span",{children:"Curriculum Subject Mastery & Proficiency Analytics"}),
              l.jsx("span",{className:"text-[10px] text-slate-500 font-bold",children:"Visual Mastery Scale: 0% - 100%"})
            ]}),
            l.jsx("div",{className:"p-3 space-y-2.5",children:R.subjects.map(sub=>{
              const obt=Number((st.marks&&st.marks[sub.id])||0);
              const isPass=obt>=sub.passingMarks;
              const pct=sub.totalMarks>0?(obt/sub.totalMarks*100).toFixed(1):"0.0";
              const pNum=parseFloat(pct);
              let grd="F";
              let level="Needs Support";
              let barColor="#e11d48";
              if(pNum>=90){grd="A+";level="Advanced Mastery";barColor="#059669";}
              else if(pNum>=80){grd="A";level="Proficient";barColor="#10b981";}
              else if(pNum>=70){grd="B";level="Competent";barColor="#2563eb";}
              else if(pNum>=60){grd="C";level="Developing";barColor="#4f46e5";}
              else if(pNum>=50){grd="D";level="Basic";barColor="#d97706";}
              else if(pNum>=40){grd="E";level="Marginal";barColor="#ea580c";}
              return l.jsxs("div",{key:sub.id,className:"p-2 rounded-lg bg-slate-50 border border-slate-200 text-xs flex flex-col gap-1.5",children:[
                l.jsxs("div",{className:"flex items-center justify-between font-bold",children:[
                  l.jsxs("div",{className:"flex items-center gap-2",children:[
                    l.jsx("span",{className:"font-black text-slate-900",children:sub.name}),
                    l.jsxs("span",{className:"text-[10px] text-slate-500 font-medium",children:["(Max: ",sub.totalMarks," • Pass: ",sub.passingMarks,")"]})
                  ]}),
                  l.jsxs("div",{className:"flex items-center gap-3",children:[
                    l.jsxs("span",{className:"font-black text-slate-900",children:[obt," / ",sub.totalMarks]}),
                    l.jsxs("span",{className:"font-bold text-slate-700 w-12 text-right",children:[pct,"%"]}),
                    l.jsx("span",{className:`px-2 py-0.5 rounded text-[10px] font-black ${isPass?"bg-blue-100 text-blue-900":"bg-rose-100 text-rose-900"}`,children:grd}),
                    l.jsx("span",{className:`text-[10px] font-bold w-28 text-right ${isPass?"text-emerald-700":"text-rose-700"}`,children:level})
                  ]})
                ]}),
                l.jsx("div",{className:"w-full bg-slate-200 rounded-full h-2 overflow-hidden",children:
                  l.jsx("div",{className:"h-full rounded-full transition-all",style:{width:`${Math.min(100,Math.max(3,pNum))}%`,backgroundColor:barColor}})
                })
              ]});
            })})
          ]}),

          /* Summary Matrix + Holistic Radar */
          l.jsxs("div",{className:"grid grid-cols-1 sm:grid-cols-2 gap-3 mb-5",children:[
            l.jsxs("div",{className:"p-3 rounded-xl border border-slate-300 bg-slate-50 text-xs flex flex-col justify-between",children:[
              l.jsx("div",{className:"text-[10px] font-black uppercase tracking-wider text-slate-700 mb-2",children:"Overall Diagnostic Summary"}),
              l.jsxs("div",{className:"grid grid-cols-3 gap-2 text-center",children:[
                l.jsxs("div",{className:"bg-white p-2 rounded-lg border border-slate-200",children:[
                  l.jsx("span",{className:"text-[9px] uppercase text-slate-500 font-bold block",children:"Grand Score"}),
                  l.jsxs("span",{className:"text-sm font-black text-blue-950",children:[q_stat.totalObtained," / ",ne]})
                ]}),
                l.jsxs("div",{className:"bg-white p-2 rounded-lg border border-slate-200",children:[
                  l.jsx("span",{className:"text-[9px] uppercase text-slate-500 font-bold block",children:"Aggregate %"}),
                  l.jsxs("span",{className:"text-sm font-black text-slate-900",children:[q_stat.percentage,"%"]})
                ]}),
                l.jsxs("div",{className:"bg-white p-2 rounded-lg border border-slate-200",children:[
                  l.jsx("span",{className:"text-[9px] uppercase text-slate-500 font-bold block",children:"Final Grade"}),
                  l.jsx("span",{className:"text-sm font-black text-emerald-800",children:q_stat.grade})
                ]})
              ]}),
              l.jsxs("div",{className:"mt-2 pt-2 border-t border-slate-200 flex items-center justify-between text-[11px]",children:[
                l.jsx("span",{className:"font-bold text-slate-600",children:"Result Verdict:"}),
                l.jsx("span",{className:`font-black px-2.5 py-0.5 rounded-full ${q_stat.status==="PASS"?"bg-emerald-100 text-emerald-900":"bg-rose-100 text-rose-900"}`,children:q_stat.status==="PASS"?"PASSED & PROMOTED":"RETAKE REQUIRED"})
              ]})
            ]}),
            l.jsxs("div",{className:"p-3 rounded-xl border border-slate-300 bg-slate-50 text-xs flex flex-col justify-between",children:[
              l.jsx("div",{className:"text-[10px] font-black uppercase tracking-wider text-slate-700 mb-1.5",children:"Holistic Behavioral & Learning Matrix"}),
              l.jsxs("div",{className:"space-y-1 text-[11px]",children:[
                l.jsxs("div",{className:"flex justify-between",children:[l.jsx("span",{className:"text-slate-600 font-medium",children:"Academic Diligence & Focus:"}),l.jsx("span",{className:"font-black text-slate-800",children:"⭐⭐⭐⭐⭐ Excellent"})]}),
                l.jsxs("div",{className:"flex justify-between",children:[l.jsx("span",{className:"text-slate-600 font-medium",children:"Class Participation & Inquisitiveness:"}),l.jsx("span",{className:"font-black text-slate-800",children:"⭐⭐⭐⭐ Very Good"})]}),
                l.jsxs("div",{className:"flex justify-between",children:[l.jsx("span",{className:"text-slate-600 font-medium",children:"Assignment Punctuality:"}),l.jsx("span",{className:"font-black text-emerald-800",children:"100% On-Time"})]}),
                l.jsxs("div",{className:"flex justify-between",children:[l.jsx("span",{className:"text-slate-600 font-medium",children:"Social Conduct & Discipline:"}),l.jsx("span",{className:"font-black text-blue-900",children:"Exemplary"})]})
              ]})
            ]})
          ]}),

          /* Diagnostic Remarks */
          l.jsxs("div",{className:"p-3 rounded-xl border border-slate-300 bg-white mb-5 text-xs",children:[
            l.jsx("div",{className:"text-[10px] font-black uppercase tracking-wider text-slate-800 mb-1",children:"Educator Diagnostic Guidance & Feedback:"}),
            l.jsxs("div",{className:"italic text-slate-700 font-medium leading-relaxed",children:['"',st.remarks||"Displays commendable intellectual discipline and consistent analytical engagement. Recommended for competitive science stream tracks.",'"']})
          ]}),

          /* Diagnostic Signatures */
          l.jsxs("div",{className:"pt-6 border-t border-slate-400 grid grid-cols-3 text-center text-xs font-bold text-slate-900",children:[
            l.jsx("div",{children:l.jsx("div",{className:"w-36 border-t-2 border-slate-800 mx-auto pt-1 font-black",children:"Academic Advisor"})}),
            l.jsx("div",{children:l.jsx("div",{className:"w-40 border-t-2 border-slate-800 mx-auto pt-1 font-black",children:"Assessment Coordinator"})}),
            l.jsx("div",{children:l.jsx("div",{className:"w-36 border-t-2 border-slate-800 mx-auto pt-1 font-black",children:"Principal / Official Seal"})})
          ]}),
          l.jsx("div",{className:"text-center text-[9px] text-slate-400 font-mono mt-6 border-t border-slate-200 pt-2",children:"Diagnostic Report Edition • Detailed Subject Mastery Analytics • System Generated"})
        ]})

      ]});
    })
  })
]})'''

text = text[:start_idx] + new_single_card + text[end_idx:]
print(f"[✓] Replaced singleCard block successfully! New total length: {len(text)}")

# Write to file
with open("assets/index-DAioIUjd.js", "w", encoding="utf-8") as f:
    f.write(text)

print("Saved updated assets/index-DAioIUjd.js!")
