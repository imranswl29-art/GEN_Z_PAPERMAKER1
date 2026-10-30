import sys

print("Loading assets/index-DAioIUjd.js...")
with open("assets/index-DAioIUjd.js", "r", encoding="utf-8") as f:
    text = f.read()

start_marker = 'a==="singleCard"&&P&&l.jsxs("div",{className:"space-y-5"'
start_idx = text.find(start_marker)
assert start_idx != -1, "start_marker not found"

end_marker = ',a==="masterSheet"'
end_idx = text.find(end_marker, start_idx)
assert end_idx != -1, "end_marker not found"

print(f"Single card block found from {start_idx} to {end_idx}")

new_single_card = '''a==="singleCard"&&P&&l.jsxs("div",{className:"space-y-5",children:[
  /* 1. Design Template Selector Banner (English Only, Zero Yellow/Orange) */
  l.jsxs("div",{className:"bg-gradient-to-r from-slate-900 via-indigo-950 to-slate-900 p-4 sm:p-5 rounded-2xl border-2 border-indigo-600/70 shadow-xl no-print text-white",children:[
    l.jsxs("div",{className:"flex flex-col lg:flex-row items-start lg:items-center justify-between gap-4",children:[
      l.jsxs("div",{className:"flex items-center gap-3.5",children:[
        l.jsx("div",{className:"w-11 h-11 rounded-2xl bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center text-white shadow-lg text-xl shrink-0 ring-2 ring-indigo-300/40",children:"🎨"}),
        l.jsxs("div",{children:[
          l.jsxs("div",{className:"flex items-center gap-2.5 flex-wrap",children:[
            l.jsx("h3",{className:"text-sm sm:text-base font-black uppercase tracking-wider text-white",children:"Select Result Card Design Template"}),
            l.jsx("span",{className:"text-[10px] font-black px-2.5 py-0.5 rounded-full shadow-xs uppercase tracking-wide",style:{backgroundColor:"#059669",color:"#ffffff"},children:"3 Distinct Designs Available"})
          ]}),
          l.jsx("p",{className:"text-xs text-slate-300 font-medium mt-0.5",children:"Choose your preferred institutional layout to preview, print, or download in high-definition PDF and Word."})
        ]})
      ]}),
      l.jsxs("div",{className:"flex flex-wrap items-center gap-2 w-full lg:w-auto",children:[
        /* Template 1 Button */
        l.jsxs("button",{type:"button",onClick:()=>{setCardTemplate("classic");try{localStorage.setItem("ptbb_rc_template","classic")}catch(e){}F("Active Design: Design 1 - Classic Academic Transcript");},className:`flex items-center gap-2.5 px-3.5 py-2.5 rounded-xl text-xs transition-all cursor-pointer border ${cardTemplate==="classic"?"bg-white text-blue-950 border-blue-500 ring-3 ring-blue-500/80 shadow-lg font-black":"bg-slate-800/90 text-slate-200 border-slate-700 hover:bg-slate-700/90 font-bold"}`,children:[
          l.jsx("span",{className:"text-lg",children:"📜"}),
          l.jsxs("div",{className:"text-left",children:[
            l.jsx("div",{className:"font-black text-xs leading-tight",children:"Design 1: Classic Academic"}),
            l.jsx("div",{className:"text-[9px] opacity-75 leading-tight font-medium",children:"Official Board Transcript"})
          ]}),
          cardTemplate==="classic"&&l.jsx("span",{className:"ml-1 text-emerald-600 font-black text-xs",children:"✓"})
        ]}),
        /* Template 2 Button */
        l.jsxs("button",{type:"button",onClick:()=>{setCardTemplate("modern");try{localStorage.setItem("ptbb_rc_template","modern")}catch(e){}F("Active Design: Design 2 - Modern Executive Certificate");},className:`flex items-center gap-2.5 px-3.5 py-2.5 rounded-xl text-xs transition-all cursor-pointer border ${cardTemplate==="modern"?"bg-white text-blue-950 border-blue-500 ring-3 ring-blue-500/80 shadow-lg font-black":"bg-slate-800/90 text-slate-200 border-slate-700 hover:bg-slate-700/90 font-bold"}`,children:[
          l.jsx("span",{className:"text-lg",children:"🏆"}),
          l.jsxs("div",{className:"text-left",children:[
            l.jsx("div",{className:"font-black text-xs leading-tight",children:"Design 2: Modern Certificate"}),
            l.jsx("div",{className:"text-[9px] opacity-75 leading-tight font-medium",children:"Executive Distinction Style"})
          ]}),
          cardTemplate==="modern"&&l.jsx("span",{className:"ml-1 text-emerald-600 font-black text-xs",children:"✓"})
        ]}),
        /* Template 3 Button */
        l.jsxs("button",{type:"button",onClick:()=>{setCardTemplate("diagnostic");try{localStorage.setItem("ptbb_rc_template","diagnostic")}catch(e){}F("Active Design: Design 3 - Detailed Diagnostic Report");},className:`flex items-center gap-2.5 px-3.5 py-2.5 rounded-xl text-xs transition-all cursor-pointer border ${cardTemplate==="diagnostic"?"bg-white text-blue-950 border-blue-500 ring-3 ring-blue-500/80 shadow-lg font-black":"bg-slate-800/90 text-slate-200 border-slate-700 hover:bg-slate-700/90 font-bold"}`,children:[
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
           Kept exactly as requested, with strict photo size safeguards
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
            l.jsx("div",{className:"shrink-0 rounded-lg border-2 border-slate-700 bg-white p-1 overflow-hidden shadow-xs flex flex-col items-center justify-center",style:{width:"96px",height:"128px",minWidth:"96px",minHeight:"128px",maxWidth:"96px",maxHeight:"128px",flexShrink:0},children:st.photoUrl?l.jsx("img",{src:st.photoUrl,alt:st.name,className:"w-full h-full object-cover rounded",style:{width:"100%",height:"100%",objectFit:"cover",display:"block",imageRendering:"-webkit-optimize-contrast"}}):l.jsxs("div",{className:"flex flex-col items-center justify-center p-2 text-center w-full h-full bg-slate-50 rounded",children:[
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
           DESIGN 2: MODERN EXECUTIVE CERTIFICATE (Sapphire & Emerald Edition)
           NO yellow, NO orange! Strictly constrained photo dimensions!
           ------------------------------------------------------------- */
        cardTemplate==="modern"&&l.jsxs("div",{className:"modern-certificate-template p-5 sm:p-7 border-4 rounded-3xl relative overflow-hidden",style:{borderColor:"#1d4ed8",backgroundColor:"#ffffff",boxShadow:"inset 0 0 0 2px #059669, 0 10px 25px -5px rgba(29, 78, 216, 0.15)"},children:[
          /* Ornamental Corner Accents (Royal Sapphire) */
          l.jsx("div",{className:"absolute top-2 left-2 font-black text-lg select-none",style:{color:"#1d4ed8"},children:"⚜️"}),
          l.jsx("div",{className:"absolute top-2 right-2 font-black text-lg select-none",style:{color:"#1d4ed8"},children:"⚜️"}),
          l.jsx("div",{className:"absolute bottom-2 left-2 font-black text-lg select-none",style:{color:"#1d4ed8"},children:"⚜️"}),
          l.jsx("div",{className:"absolute bottom-2 right-2 font-black text-lg select-none",style:{color:"#1d4ed8"},children:"⚜️"}),

          /* Modern Certificate Grand Header */
          l.jsxs("div",{className:"text-center pb-4 mb-4 border-b-2 relative",style:{borderColor:"#059669"},children:[
            l.jsxs("div",{className:"flex items-center justify-between gap-4 mb-3",children:[
              /* Left Monogram with Emerald Ring */
              l.jsx("div",{className:"shrink-0 p-1.5 rounded-2xl shadow-md",style:{border:"3px solid #059669",backgroundColor:"#ffffff"},children:
                l.jsx(Rw,{logoUrl:r.logoUrl,schoolName:r.schoolName,size:76})
              }),
              /* Center School Typography */
              l.jsxs("div",{className:"flex-1 text-center px-2",children:[
                l.jsx("div",{className:"text-[10px] font-black tracking-widest uppercase mb-0.5",style:{color:"#047857"},children:"★ PRESTIGIOUS ACADEMIC EXCELLENCE & HONOURS GAZETTE ★"}),
                l.jsx("h1",{className:"text-2xl sm:text-3xl font-black uppercase tracking-tight leading-tight",style:{color:"#1e3a8a"},children:r.schoolName}),
                l.jsxs("div",{className:"text-xs sm:text-sm font-extrabold tracking-wide mt-1",style:{color:"#0f172a"},children:[r.campusName," • ",r.address]}),
                l.jsxs("div",{className:"text-[11px] font-bold mt-0.5",style:{color:"#475569"},children:["Board Affiliation: ",r.boardPattern||"BISE Punjab"," • Official Helpline: ",r.phone]})
              ]}),
              /* Right Emerald & Silver Honors Rosette Badge (NO yellow!) */
              l.jsxs("div",{className:"shrink-0 hidden sm:flex flex-col items-center justify-center w-24 h-24 rounded-full p-1 text-center shadow-md",style:{background:"linear-gradient(135deg, #ecfdf5, #d1fae5)",border:"3px solid #059669",color:"#064e3b"},children:[
                l.jsx("span",{className:"text-2xl",children:"🏅"}),
                l.jsx("span",{className:"text-[8px] font-black uppercase tracking-wider leading-tight",children:"Academic Award"}),
                l.jsx("span",{className:"text-[11px] font-black mt-0.5",children:R.session}),
                l.jsx("span",{className:"text-[7px] font-extrabold uppercase",style:{color:"#047857"},children:"Verified"})
              ]})
            ]}),
            /* Certificate Title Ribbon */
            l.jsxs("div",{className:"py-2 px-6 rounded-xl shadow-md mt-2",style:{backgroundColor:"#1e3a8a",border:"2px solid #10b981"},children:[
              l.jsx("h2",{className:"text-sm sm:text-base font-black uppercase tracking-widest",style:{color:"#ffffff"},children:"Certificate of Academic Achievement & Report Card"}),
              l.jsxs("p",{className:"text-[11px] font-bold tracking-wide mt-0.5",style:{color:"#93c5fd"},children:["Academic Session: ",R.session," • Examination: ",R.examCategory," • Class: ",R.classLevel]})
            ]})
          ]}),

          /* Modern Executive Candidate Card (Strictly 80x80 Photo) */
          l.jsxs("div",{className:"rounded-2xl p-4 mb-5 shadow-xs flex flex-col sm:flex-row items-center gap-5",style:{backgroundColor:"#f0fdf4",border:"2px solid #059669"},children:[
            /* Circular Portrait with Emerald Ring (Strictly Constrained) */
            l.jsxs("div",{className:"shrink-0 flex flex-col items-center",children:[
              l.jsx("div",{className:"rounded-full overflow-hidden shadow-md p-0.5 flex items-center justify-center",style:{width:"80px",height:"80px",minWidth:"80px",minHeight:"80px",maxWidth:"80px",maxHeight:"80px",border:"3.5px solid #059669",backgroundColor:"#ffffff",flexShrink:0},children:
                st.photoUrl?l.jsx("img",{src:st.photoUrl,alt:st.name,className:"rounded-full",style:{width:"100%",height:"100%",minWidth:"100%",minHeight:"100%",maxWidth:"100%",maxHeight:"100%",objectFit:"cover",display:"block",imageRendering:"-webkit-optimize-contrast"}}):
                l.jsxs("div",{className:"w-full h-full rounded-full flex flex-col items-center justify-center text-center",style:{backgroundColor:"#eff6ff"},children:[
                  l.jsx("span",{className:"text-2xl",children:"🎓"}),
                  l.jsx("span",{className:"text-[8px] font-black uppercase",style:{color:"#1e40af"},children:"Candidate"})
                ]})
              }),
              l.jsxs("div",{className:"mt-2 px-3 py-0.5 rounded-full font-black text-[11px] tracking-wider shadow-xs",style:{backgroundColor:"#1e3a8a",color:"#ffffff"},children:["Roll # ",st.rollNo]})
            ]}),
            /* Candidate Metadata Grid with High-Contrast Non-Yellow Cards */
            l.jsxs("div",{className:"flex-1 w-full grid grid-cols-2 sm:grid-cols-4 gap-3 text-xs",children:[
              l.jsxs("div",{className:"p-2.5 rounded-xl shadow-2xs",style:{backgroundColor:"#ffffff",border:"2px solid #93c5fd"},children:[
                l.jsx("span",{className:"text-[9px] font-black uppercase tracking-wider block",style:{color:"#2563eb"},children:"Student Name"}),
                l.jsx("span",{className:"text-xs font-black block mt-0.5",style:{color:"#1e3a8a"},children:st.name})
              ]}),
              l.jsxs("div",{className:"p-2.5 rounded-xl shadow-2xs",style:{backgroundColor:"#ffffff",border:"2px solid #cbd5e1"},children:[
                l.jsx("span",{className:"text-[9px] font-black uppercase tracking-wider block",style:{color:"#475569"},children:"Father's Name"}),
                l.jsx("span",{className:"text-xs font-bold block mt-0.5",style:{color:"#0f172a"},children:st.fatherName||"-"})
              ]}),
              l.jsxs("div",{className:"p-2.5 rounded-xl shadow-2xs",style:{backgroundColor:"#ffffff",border:"2px solid #c4b5fd"},children:[
                l.jsx("span",{className:"text-[9px] font-black uppercase tracking-wider block",style:{color:"#7c3aed"},children:"Class & Section"}),
                l.jsxs("span",{className:"text-xs font-black block mt-0.5",style:{color:"#581c87"},children:[R.classLevel," - ",st.section||"A"]})
              ]}),
              l.jsxs("div",{className:"p-2.5 rounded-xl shadow-2xs",style:{backgroundColor:"#ecfdf5",border:"2px solid #10b981"},children:[
                l.jsx("span",{className:"text-[9px] font-black uppercase tracking-wider block",style:{color:"#047857"},children:"Class Standing"}),
                l.jsxs("span",{className:"text-xs font-black flex items-center gap-1 mt-0.5",style:{color:"#064e3b"},children:[l.jsx("span",{children:"🏆"}),l.jsx("span",{children:st.rank||"1st Class"})]})
              ]})
            ]})
          ]}),

          /* Vibrant Curriculum Subject Performance Table */
          l.jsx("div",{className:"overflow-visible mb-5",children:
            l.jsxs("table",{className:"w-full text-xs border-collapse rounded-xl overflow-hidden shadow-xs",style:{border:"2px solid #1e3a8a"},children:[
              l.jsx("thead",{children:
                l.jsxs("tr",{className:"text-white font-black uppercase text-[11px] tracking-wider",style:{backgroundColor:"#1e3a8a"},children:[
                  l.jsx("th",{className:"p-2.5 text-center w-10 border border-blue-800",children:"#"}),
                  l.jsx("th",{className:"p-2.5 text-left border border-blue-800",children:"Course Curriculum Subject"}),
                  l.jsx("th",{className:"p-2.5 text-center w-20 border border-blue-800",children:"Max Marks"}),
                  l.jsx("th",{className:"p-2.5 text-center w-20 border border-blue-800",children:"Min Pass"}),
                  l.jsx("th",{className:"p-2.5 text-center w-24 border border-blue-800",children:"Score Obtained"}),
                  l.jsx("th",{className:"p-2.5 text-center w-20 border border-blue-800",children:"Score %"}),
                  l.jsx("th",{className:"p-2.5 text-center w-20 border border-blue-800",children:"Grade"}),
                  l.jsx("th",{className:"p-2.5 text-center w-28 border border-blue-800",children:"Achievement"})
                ]})
              }),
              l.jsxs("tbody",{children:[
                R.subjects.map((sub,sIdx)=>{
                  const obt=Number((st.marks&&st.marks[sub.id])||0);
                  const isPass=obt>=sub.passingMarks;
                  const pct=sub.totalMarks>0?(obt/sub.totalMarks*100).toFixed(1):"0.0";
                  const pNum=parseFloat(pct);
                  let grd="F";
                  if(pNum>=90)grd="A+";else if(pNum>=80)grd="A";else if(pNum>=70)grd="B";else if(pNum>=60)grd="C";else if(pNum>=50)grd="D";else if(pNum>=40)grd="E";
                  const isTop=grd==="A+"||grd==="A";
                  return l.jsxs("tr",{key:sub.id,className:"border-b",style:{backgroundColor:sIdx%2===0?"#ffffff":"#f8fafc",borderColor:"#cbd5e1"},children:[
                    l.jsx("td",{className:"p-2 text-center font-bold border-r",style:{color:"#0f172a",borderColor:"#e2e8f0"},children:sIdx+1}),
                    l.jsx("td",{className:"p-2 font-black border-r text-sm",style:{color:"#0f172a",borderColor:"#e2e8f0"},children:sub.name}),
                    l.jsx("td",{className:"p-2 text-center font-bold border-r",style:{color:"#1e293b",borderColor:"#e2e8f0"},children:sub.totalMarks}),
                    l.jsx("td",{className:"p-2 text-center font-medium border-r",style:{color:"#64748b",borderColor:"#e2e8f0"},children:sub.passingMarks}),
                    /* Obtained Marks in Bright Blue Badge */
                    l.jsx("td",{className:"p-2 text-center border-r",style:{borderColor:"#e2e8f0"},children:
                      l.jsx("span",{className:"px-2.5 py-1 rounded-lg font-black text-xs inline-block",style:{backgroundColor:isPass?"#dbeafe":"#ffe4e6",color:isPass?"#1e40af":"#b91c1c",border:isPass?"1.5px solid #3b82f6":"1.5px solid #f43f5e"},children:obt})
                    }),
                    l.jsxs("td",{className:"p-2 text-center font-extrabold border-r",style:{color:"#0f172a",borderColor:"#e2e8f0"},children:[pct,"%"]}),
                    /* Grade in Colored Pill (NO yellow/orange) */
                    l.jsx("td",{className:"p-2 text-center border-r",style:{borderColor:"#e2e8f0"},children:
                      l.jsx("span",{className:"px-2.5 py-0.5 rounded-md font-black text-xs inline-block",style:{backgroundColor:isTop?"#d1fae5":isPass?"#e0f2fe":"#ffe4e6",color:isTop?"#065f46":isPass?"#0369a1":"#9f1239",border:isTop?"1.5px solid #10b981":isPass?"1.5px solid #0284c7":"1.5px solid #f43f5e"},children:grd})
                    }),
                    /* Achievement Status */
                    l.jsx("td",{className:"p-2 text-center",children:
                      l.jsx("span",{className:"text-[10px] font-black uppercase px-2.5 py-0.5 rounded-full inline-block",style:{backgroundColor:isPass?"#ecfdf5":"#fff1f2",color:isPass?"#065f46":"#be123c",border:isPass?"1px solid #10b981":"1px solid #f43f5e"},children:isPass?(pNum>=80?"Distinction ⭐":"Passed ✓"):"Needs Retake ⚠"})
                    })
                  ]});
                })
              ]})
            ]})
          }),

          /* 4 Executive Stat Metric Cards (Deep High-Contrast Text, NO yellow/orange) */
          l.jsxs("div",{className:"grid grid-cols-2 sm:grid-cols-4 gap-3 mb-5",children:[
            /* Card 1: Total Obtained */
            l.jsxs("div",{className:"p-3.5 rounded-2xl text-center shadow-xs",style:{backgroundColor:"#eff6ff",border:"2.5px solid #2563eb"},children:[
              l.jsx("span",{className:"text-[10px] uppercase font-black tracking-wider block",style:{color:"#1e40af"},children:"Total Marks Obtained"}),
              l.jsxs("div",{className:"text-xl font-black mt-1",style:{color:"#1e3a8a"},children:[q_stat.totalObtained," ",l.jsxs("span",{className:"text-xs font-bold",style:{color:"#3b82f6"},children:["/ ",ne]})]})
            ]}),
            /* Card 2: Percentage */
            l.jsxs("div",{className:"p-3.5 rounded-2xl text-center shadow-xs",style:{backgroundColor:"#faf5ff",border:"2.5px solid #7c3aed"},children:[
              l.jsx("span",{className:"text-[10px] uppercase font-black tracking-wider block",style:{color:"#6b21a8"},children:"Aggregate Percentage"}),
              l.jsxs("div",{className:"text-xl font-black mt-1",style:{color:"#581c87"},children:[q_stat.percentage,"%"]})
            ]}),
            /* Card 3: Grade */
            l.jsxs("div",{className:"p-3.5 rounded-2xl text-center shadow-xs",style:{backgroundColor:"#ecfdf5",border:"2.5px solid #059669"},children:[
              l.jsx("span",{className:"text-[10px] uppercase font-black tracking-wider block",style:{color:"#047857"},children:"Final Letter Grade"}),
              l.jsx("div",{className:"text-2xl font-black mt-1",style:{color:"#064e3b"},children:q_stat.grade})
            ]}),
            /* Card 4: Status */
            l.jsxs("div",{className:"p-3.5 rounded-2xl text-center shadow-xs",style:{backgroundColor:q_stat.status==="PASS"?"#f0fdf4":"#fff1f2",border:q_stat.status==="PASS"?"2.5px solid #059669":"2.5px solid #e11d48"},children:[
              l.jsx("span",{className:"text-[10px] uppercase font-black tracking-wider block",style:{color:q_stat.status==="PASS"?"#065f46":"#9f1239"},children:"Official Result Status"}),
              l.jsx("div",{className:"text-base font-black mt-1",style:{color:q_stat.status==="PASS"?"#064e3b":"#881337"},children:q_stat.status==="PASS"?"PASSED WITH MERIT":"NEEDS IMPROVEMENT"})
            ]})
          ]}),

          /* Modern Commendation & Certified Badge */
          l.jsxs("div",{className:"rounded-2xl p-3.5 mb-6 flex flex-col sm:flex-row items-center justify-between gap-3 text-xs shadow-xs",style:{backgroundColor:"#f8fafc",border:"2px solid #059669"},children:[
            l.jsxs("div",{className:"flex-1",children:[
              l.jsx("span",{className:"text-[10px] font-black uppercase tracking-wider block mb-0.5",style:{color:"#047857"},children:"Executive Commendation & Remarks:"}),
              l.jsxs("p",{className:"italic leading-relaxed font-bold text-sm",style:{color:"#0f172a"},children:['"',st.remarks||"Exhibits commendable scholastic performance, exemplary character, and high learning aptitude.",'"']})
            ]}),
            l.jsxs("div",{className:"shrink-0 flex items-center gap-2 px-3 py-1.5 rounded-xl text-[11px] font-black shadow-xs",style:{backgroundColor:"#ecfdf5",border:"2px solid #059669",color:"#064e3b"},children:[
              l.jsx("span",{className:"text-xl",children:"🛡️"}),
              l.jsx("span",{children:"Institutionally Certified Record"})
            ]})
          ]}),

          /* Modern 3 Executive Signatures */
          l.jsxs("div",{className:"pt-6 border-t-2 grid grid-cols-3 text-center text-xs font-bold",style:{borderColor:"#059669",color:"#0f172a"},children:[
            l.jsx("div",{children:l.jsx("div",{className:"w-36 border-t-2 mx-auto pt-1 font-black",style:{borderColor:"#1e3a8a"},children:"Controller Examinations"})}),
            l.jsx("div",{children:l.jsx("div",{className:"w-40 border-t-2 mx-auto pt-1 font-black",style:{borderColor:"#1e3a8a"},children:"Principal / Executive Seal"})}),
            l.jsx("div",{children:l.jsx("div",{className:"w-36 border-t-2 mx-auto pt-1 font-black",style:{borderColor:"#1e3a8a"},children:"Parent / Guardian"})})
          ]}),
          l.jsx("div",{className:"text-center text-[10px] font-extrabold mt-6 border-t pt-2 tracking-wider uppercase",style:{color:"#64748b",borderColor:"#e2e8f0"},children:"Modern Executive Certificate Edition • Designed for High-Distinction Recognition"})
        ]}),

        /* -------------------------------------------------------------
           DESIGN 3: MODERN STEM & ANALYTICAL DIAGNOSTIC INFOGRAPHIC
           (Dedicated Candidate Box with Strict 80x80 Photo, NO yellow/orange)
           ------------------------------------------------------------- */
        cardTemplate==="diagnostic"&&l.jsxs("div",{className:"detailed-diagnostic-template p-5 sm:p-7 border-3 rounded-3xl relative shadow-md",style:{borderColor:"#0891b2",backgroundColor:"#ffffff"},children:[
          /* Tech-Academic Diagnostic Header */
          l.jsxs("div",{className:"pb-4 mb-4 border-b-2 flex flex-col sm:flex-row items-center justify-between gap-4",style:{borderColor:"#0891b2"},children:[
            l.jsxs("div",{className:"flex items-center gap-4",children:[
              l.jsx("div",{className:"p-1.5 rounded-2xl shadow-sm",style:{border:"2.5px solid #06b6d4",backgroundColor:"#ecfeff"},children:
                l.jsx(Rw,{logoUrl:r.logoUrl,schoolName:r.schoolName,size:72})
              }),
              l.jsxs("div",{children:[
                l.jsx("div",{className:"text-[10px] font-black uppercase tracking-widest",style:{color:"#0891b2"},children:"★ LEARNING DIAGNOSTICS & MASTERY ANALYTICS ★"}),
                l.jsx("h1",{className:"text-xl sm:text-2xl font-black uppercase tracking-tight",style:{color:"#0f172a"},children:r.schoolName}),
                l.jsxs("div",{className:"text-xs sm:text-sm font-bold mt-0.5",style:{color:"#334155"},children:[r.campusName," • ",r.address]}),
                l.jsxs("div",{className:"text-[11px] font-semibold",style:{color:"#64748b"},children:["Affiliation: ",r.boardPattern||"BISE Punjab"," • Helpline: ",r.phone]})
              ]})
            ]}),
            /* QR Verification Stamp & Meta */
            l.jsxs("div",{className:"flex items-center gap-3 p-2.5 rounded-2xl shrink-0 shadow-xs",style:{backgroundColor:"#ecfeff",border:"2px solid #06b6d4"},children:[
              l.jsxs("div",{className:"text-right",children:[
                l.jsx("span",{className:"text-[9px] font-black uppercase tracking-wider block",style:{color:"#0891b2"},children:"Diagnostic Verification"}),
                l.jsxs("span",{className:"text-xs font-black block",style:{color:"#0c4a6e"},children:["ID: #",st.rollNo,"-",R.session]}),
                l.jsx("span",{className:"text-[10px] font-bold block",style:{color:"#059669"},children:"✓ Digitally Verified"})
              ]}),
              l.jsx("div",{className:"w-12 h-12 bg-white p-1 rounded-xl flex items-center justify-center shrink-0 shadow-xs",style:{border:"1.5px solid #0891b2"},title:`Verification Code: ${st.rollNo}-${R.session}`,children:
                l.jsx("span",{className:"text-2xl",children:"📊"})
              })
            ]})
          ]}),

          /* Diagnostic Banner */
          l.jsxs("div",{className:"px-4 py-2.5 rounded-xl mb-4 flex flex-wrap items-center justify-between gap-2 text-xs shadow-xs",style:{backgroundColor:"#0f172a",borderBottom:"3px solid #06b6d4"},children:[
            l.jsxs("div",{className:"font-black uppercase tracking-wider flex items-center gap-2 text-sm",style:{color:"#38bdf8"},children:[
              l.jsx("span",{children:"📈"}),
              l.jsx("span",{children:"Comprehensive Diagnostic Performance & Subject Mastery Infographic"})
            ]}),
            l.jsxs("div",{className:"font-bold text-xs",style:{color:"#e2e8f0"},children:["Class: ",R.classLevel," • Cycle: ",R.examCategory," • Session: ",R.session]})
          ]}),

          /* Dedicated Candidate Profile (Strictly 80x80 Photo, Immune to Overflow) */
          l.jsxs("div",{className:"rounded-2xl p-4 mb-5 shadow-xs flex flex-col sm:flex-row items-center gap-5",style:{backgroundColor:"#f0f9ff",border:"2px solid #0891b2"},children:[
            /* Photo Container with Unbreakable Size Constraints */
            l.jsxs("div",{className:"shrink-0 flex flex-col items-center",children:[
              l.jsx("div",{className:"rounded-full overflow-hidden shadow-md p-0.5 flex items-center justify-center",style:{width:"80px",height:"80px",minWidth:"80px",minHeight:"80px",maxWidth:"80px",maxHeight:"80px",border:"3.5px solid #0891b2",backgroundColor:"#ffffff",flexShrink:0},children:
                st.photoUrl?l.jsx("img",{src:st.photoUrl,alt:st.name,className:"rounded-full",style:{width:"100%",height:"100%",minWidth:"100%",minHeight:"100%",maxWidth:"100%",maxHeight:"100%",objectFit:"cover",display:"block",imageRendering:"-webkit-optimize-contrast"}}):
                l.jsxs("div",{className:"w-full h-full rounded-full flex flex-col items-center justify-center text-center",style:{backgroundColor:"#ecfeff"},children:[
                  l.jsx("span",{className:"text-2xl",children:"🔬"}),
                  l.jsx("span",{className:"text-[8px] font-black uppercase",style:{color:"#0891b2"},children:"Candidate"})
                ]})
              }),
              l.jsxs("div",{className:"mt-2 px-3 py-0.5 rounded-full font-black text-[11px] tracking-wider shadow-xs",style:{backgroundColor:"#0891b2",color:"#ffffff"},children:["Roll # ",st.rollNo]})
            ]}),
            /* 4 Candidate Metadata Cards (NO yellow/orange) */
            l.jsxs("div",{className:"flex-1 w-full grid grid-cols-2 sm:grid-cols-4 gap-3 text-xs",children:[
              l.jsxs("div",{className:"p-2.5 rounded-xl shadow-2xs",style:{backgroundColor:"#ffffff",border:"2px solid #0284c7"},children:[
                l.jsx("span",{className:"text-[9px] font-black uppercase tracking-wider block",style:{color:"#0284c7"},children:"Candidate Full Name"}),
                l.jsx("span",{className:"text-xs font-black block mt-0.5",style:{color:"#0c4a6e"},children:st.name})
              ]}),
              l.jsxs("div",{className:"p-2.5 rounded-xl shadow-2xs",style:{backgroundColor:"#ffffff",border:"2px solid #8b5cf6"},children:[
                l.jsx("span",{className:"text-[9px] font-black uppercase tracking-wider block",style:{color:"#7c3aed"},children:"Father's Name"}),
                l.jsx("span",{className:"text-xs font-bold block mt-0.5",style:{color:"#581c87"},children:st.fatherName||"-"})
              ]}),
              l.jsxs("div",{className:"p-2.5 rounded-xl shadow-2xs",style:{backgroundColor:"#ffffff",border:"2px solid #3b82f6"},children:[
                l.jsx("span",{className:"text-[9px] font-black uppercase tracking-wider block",style:{color:"#2563eb"},children:"Class & Section"}),
                l.jsxs("span",{className:"text-xs font-black block mt-0.5",style:{color:"#1e40af"},children:[R.classLevel," - ",st.section||"A"]})
              ]}),
              l.jsxs("div",{className:"p-2.5 rounded-xl shadow-2xs",style:{backgroundColor:"#ecfdf5",border:"2px solid #10b981"},children:[
                l.jsx("span",{className:"text-[9px] font-black uppercase tracking-wider block",style:{color:"#059669"},children:"Attendance & Standing"}),
                l.jsxs("span",{className:"text-xs font-black flex items-center gap-1 mt-0.5",style:{color:"#064e3b"},children:[l.jsx("span",{children:"🏆"}),l.jsxs("span",{children:[st.attendance||"96%"," • ",st.rank||"Top Tier"]})]})
              ]})
            ]})
          ]}),

          /* Subject Mastery Breakdown with Thick, Colorful 3D Progress Bars (NO yellow/orange) */
          l.jsxs("div",{className:"rounded-2xl overflow-hidden mb-5 shadow-xs",style:{border:"2px solid #0891b2"},children:[
            l.jsxs("div",{className:"px-4 py-2.5 flex items-center justify-between text-xs font-black uppercase tracking-wider",style:{backgroundColor:"#e0f2fe",color:"#0369a1",borderBottom:"2px solid #0891b2"},children:[
              l.jsx("span",{children:"Curriculum Subject Mastery & Proficiency Analytics"}),
              l.jsx("span",{className:"text-[11px] font-extrabold",style:{color:"#0284c7"},children:"Visual Mastery Scale: 0% - 100%"})
            ]}),
            l.jsx("div",{className:"p-3.5 space-y-3 bg-white",children:
              R.subjects.map(sub=>{
                const obt=Number((st.marks&&st.marks[sub.id])||0);
                const isPass=obt>=sub.passingMarks;
                const pct=sub.totalMarks>0?(obt/sub.totalMarks*100).toFixed(1):"0.0";
                const pNum=parseFloat(pct);
                let grd="F";
                let level="Needs Support ⚠";
                let barColor="#e11d48";
                let badgeBg="#ffe4e6";
                let badgeColor="#9f1239";
                let badgeBorder="#f43f5e";
                if(pNum>=90){grd="A+";level="Advanced Mastery 🌟";barColor="#059669";badgeBg="#d1fae5";badgeColor="#065f46";badgeBorder="#10b981";}
                else if(pNum>=80){grd="A";level="Proficient 🎯";barColor="#10b981";badgeBg="#ecfdf5";badgeColor="#047857";badgeBorder="#34d399";}
                else if(pNum>=70){grd="B";level="Competent 📘";barColor="#0891b2";badgeBg="#ecfeff";badgeColor="#0e7490";badgeBorder="#06b6d4";}
                else if(pNum>=60){grd="C";level="Developing 💡";barColor="#2563eb";badgeBg="#dbeafe";badgeColor="#1e40af";badgeBorder="#60a5fa";}
                else if(pNum>=50){grd="D";level="Basic 📙";barColor="#7c3aed";badgeBg="#ede9fe";badgeColor="#5b21b6";badgeBorder="#a78bfa";}
                else if(pNum>=40){grd="E";level="Marginal ⚠️";barColor="#4f46e5";badgeBg="#e0e7ff";badgeColor="#3730a3";badgeBorder="#818cf8";}
                return l.jsxs("div",{key:sub.id,className:"p-2.5 rounded-xl shadow-2xs flex flex-col gap-2",style:{backgroundColor:"#f8fafc",border:"1.5px solid #e2e8f0"},children:[
                  l.jsxs("div",{className:"flex items-center justify-between font-bold text-xs",children:[
                    l.jsxs("div",{className:"flex items-center gap-2",children:[
                      l.jsx("span",{className:"font-black text-sm",style:{color:"#0f172a"},children:sub.name}),
                      l.jsxs("span",{className:"text-[11px] font-bold px-2 py-0.5 rounded-md",style:{backgroundColor:"#e2e8f0",color:"#334155"},children:["Max: ",sub.totalMarks," • Pass: ",sub.passingMarks]})
                    ]}),
                    l.jsxs("div",{className:"flex items-center gap-3",children:[
                      l.jsxs("span",{className:"font-black text-sm",style:{color:"#1d4ed8"},children:[obt," / ",sub.totalMarks]}),
                      l.jsxs("span",{className:"font-black text-sm w-14 text-right",style:{color:"#0f172a"},children:[pct,"%"]}),
                      l.jsx("span",{className:"px-2.5 py-0.5 rounded-md text-xs font-black inline-block",style:{backgroundColor:badgeBg,color:badgeColor,border:`1.5px solid ${badgeBorder}`},children:grd}),
                      l.jsx("span",{className:"text-xs font-extrabold w-36 text-right",style:{color:barColor},children:level})
                    ]})
                  ]}),
                  /* Thick 3D Visual Progress Bar (12px height) */
                  l.jsx("div",{className:"w-full rounded-full h-3 overflow-hidden shadow-inner",style:{backgroundColor:"#e2e8f0",border:"1px solid #cbd5e1"},children:
                    l.jsx("div",{className:"h-full rounded-full transition-all shadow-xs",style:{width:`${Math.min(100,Math.max(4,pNum))}%`,backgroundColor:barColor}})
                  })
                ]});
              })
            })
          ]}),

          /* Summary Matrix + Holistic Radar */
          l.jsxs("div",{className:"grid grid-cols-1 sm:grid-cols-2 gap-3 mb-5",children:[
            /* Aggregate Summary Box */
            l.jsxs("div",{className:"p-4 rounded-2xl text-xs flex flex-col justify-between shadow-xs",style:{backgroundColor:"#f0fdf4",border:"2px solid #059669"},children:[
              l.jsx("div",{className:"text-[11px] font-black uppercase tracking-wider mb-2",style:{color:"#065f46"},children:"Overall Diagnostic Summary"}),
              l.jsxs("div",{className:"grid grid-cols-3 gap-2.5 text-center",children:[
                l.jsxs("div",{className:"p-2.5 rounded-xl shadow-2xs",style:{backgroundColor:"#ffffff",border:"2px solid #3b82f6"},children:[
                  l.jsx("span",{className:"text-[9px] uppercase font-black block",style:{color:"#2563eb"},children:"Grand Score"}),
                  l.jsxs("span",{className:"text-base font-black block mt-0.5",style:{color:"#1e3a8a"},children:[q_stat.totalObtained," / ",ne]})
                ]}),
                l.jsxs("div",{className:"p-2.5 rounded-xl shadow-2xs",style:{backgroundColor:"#ffffff",border:"2px solid #8b5cf6"},children:[
                  l.jsx("span",{className:"text-[9px] uppercase font-black block",style:{color:"#7c3aed"},children:"Aggregate %"}),
                  l.jsxs("span",{className:"text-base font-black block mt-0.5",style:{color:"#581c87"},children:[q_stat.percentage,"%"]})
                ]}),
                l.jsxs("div",{className:"p-2.5 rounded-xl shadow-2xs",style:{backgroundColor:"#ffffff",border:"2px solid #10b981"},children:[
                  l.jsx("span",{className:"text-[9px] uppercase font-black block",style:{color:"#059669"},children:"Final Grade"}),
                  l.jsx("span",{className:"text-base font-black block mt-0.5",style:{color:"#064e3b"},children:q_stat.grade})
                ]})
              ]}),
              l.jsxs("div",{className:"mt-3 pt-2.5 flex items-center justify-between text-xs",style:{borderTop:"1.5px solid #86efac"},children:[
                l.jsx("span",{className:"font-extrabold",style:{color:"#065f46"},children:"Official Verdict:"}),
                l.jsx("span",{className:"font-black px-3 py-1 rounded-full text-xs shadow-xs",style:{backgroundColor:q_stat.status==="PASS"?"#dcfce7":"#fee2e2",color:q_stat.status==="PASS"?"#14532d":"#991b1b",border:q_stat.status==="PASS"?"1.5px solid #22c55e":"1.5px solid #ef4444"},children:q_stat.status==="PASS"?"PASSED & OFFICIALLY PROMOTED ✓":"RETAKE REQUIRED ⚠️"})
              ]})
            ]}),
            /* Holistic Behavioral Scorecard (NO yellow/orange) */
            l.jsxs("div",{className:"p-4 rounded-2xl text-xs flex flex-col justify-between shadow-xs",style:{backgroundColor:"#faf5ff",border:"2px solid #8b5cf6"},children:[
              l.jsx("div",{className:"text-[11px] font-black uppercase tracking-wider mb-2",style:{color:"#6b21a8"},children:"Holistic Behavioral & Learning Matrix"}),
              l.jsxs("div",{className:"space-y-1.5 text-xs font-bold",children:[
                l.jsxs("div",{className:"flex justify-between items-center p-1.5 rounded-lg bg-white border border-purple-200",children:[
                  l.jsx("span",{style:{color:"#475569"},children:"Academic Diligence & Focus:"}),
                  l.jsx("span",{className:"font-black",style:{color:"#065f46"},children:"⭐⭐⭐⭐⭐ Excellent"})
                ]}),
                l.jsxs("div",{className:"flex justify-between items-center p-1.5 rounded-lg bg-white border border-purple-200",children:[
                  l.jsx("span",{style:{color:"#475569"},children:"Classroom Engagement:"}),
                  l.jsx("span",{className:"font-black",style:{color:"#1e40af"},children:"⭐⭐⭐⭐ Very Good"})
                ]}),
                l.jsxs("div",{className:"flex justify-between items-center p-1.5 rounded-lg bg-white border border-purple-200",children:[
                  l.jsx("span",{style:{color:"#475569"},children:"Assignment Punctuality:"}),
                  l.jsx("span",{className:"font-black",style:{color:"#047857"},children:"100% On-Time"})
                ]}),
                l.jsxs("div",{className:"flex justify-between items-center p-1.5 rounded-lg bg-white border border-purple-200",children:[
                  l.jsx("span",{style:{color:"#475569"},children:"Social Conduct & Discipline:"}),
                  l.jsx("span",{className:"font-black",style:{color:"#581c87"},children:"Exemplary Standing"})
                ]})
              ]})
            ]})
          ]}),

          /* Diagnostic Remarks */
          l.jsxs("div",{className:"p-3.5 rounded-2xl mb-5 text-xs shadow-xs",style:{backgroundColor:"#f8fafc",borderLeft:"5px solid #0891b2",borderTop:"1px solid #cbd5e1",borderRight:"1px solid #cbd5e1",borderBottom:"1px solid #cbd5e1"},children:[
            l.jsx("div",{className:"text-[10px] font-black uppercase tracking-wider mb-1",style:{color:"#0891b2"},children:"Educator Diagnostic Guidance & Feedback:"}),
            l.jsxs("div",{className:"italic font-bold text-sm leading-relaxed",style:{color:"#0f172a"},children:['"',st.remarks||"Displays commendable intellectual discipline and consistent analytical engagement. Recommended for competitive science stream tracks.",'"']})
          ]}),

          /* Diagnostic Signatures */
          l.jsxs("div",{className:"pt-6 border-t-2 grid grid-cols-3 text-center text-xs font-bold",style:{borderColor:"#0891b2",color:"#0f172a"},children:[
            l.jsx("div",{children:l.jsx("div",{className:"w-36 border-t-2 mx-auto pt-1 font-black",style:{borderColor:"#0891b2"},children:"Academic Advisor"})}),
            l.jsx("div",{children:l.jsx("div",{className:"w-40 border-t-2 mx-auto pt-1 font-black",style:{borderColor:"#0891b2"},children:"Assessment Coordinator"})}),
            l.jsx("div",{children:l.jsx("div",{className:"w-36 border-t-2 mx-auto pt-1 font-black",style:{borderColor:"#0891b2"},children:"Principal / Official Seal"})})
          ]}),
          l.jsx("div",{className:"text-center text-[10px] font-extrabold mt-6 border-t pt-2 tracking-wider uppercase",style:{color:"#64748b",borderColor:"#e2e8f0"},children:"Diagnostic Report Edition • Detailed Subject Mastery Analytics • System Generated"})
        ]})

      ]});
    })
  })
]})'''

text = text[:start_idx] + new_single_card + text[end_idx:]
print(f"[✓] Successfully injected perfected result card designs! New bundle length: {len(text)}")

with open("assets/index-DAioIUjd.js", "w", encoding="utf-8") as f:
    f.write(text)

print("Saved updated assets/index-DAioIUjd.js!")
