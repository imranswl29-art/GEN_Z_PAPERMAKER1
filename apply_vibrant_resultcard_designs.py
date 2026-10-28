import sys

print("Loading assets/index-DAioIUjd.js...")
with open("assets/index-DAioIUjd.js", "r", encoding="utf-8") as f:
    text = f.read()

start_marker = 'cardTemplate==="modern"&&l.jsxs("div",{className:"modern-certificate-template'
start_idx = text.find(start_marker)
assert start_idx != -1, "start_marker not found"

end_marker = ',a==="masterSheet"'
end_idx = text.find(end_marker, start_idx)
assert end_idx != -1, "end_marker not found"

print(f"Replacing templates from index {start_idx} to {end_idx}")

new_templates = '''cardTemplate==="modern"&&l.jsxs("div",{className:"modern-certificate-template p-5 sm:p-7 border-4 border-double rounded-3xl relative overflow-hidden",style:{borderColor:"#1d4ed8",boxShadow:"inset 0 0 0 3px #f59e0b, 0 12px 30px -5px rgba(29, 78, 216, 0.2)",backgroundColor:"#fffdfa"},children:[
          /* Ornamental Corner Stars */
          l.jsx("div",{className:"absolute top-2 left-2 text-amber-500 font-black text-xl select-none",children:"⚜️"}),
          l.jsx("div",{className:"absolute top-2 right-2 text-amber-500 font-black text-xl select-none",children:"⚜️"}),
          l.jsx("div",{className:"absolute bottom-2 left-2 text-amber-500 font-black text-xl select-none",children:"⚜️"}),
          l.jsx("div",{className:"absolute bottom-2 right-2 text-amber-500 font-black text-xl select-none",children:"⚜️"}),

          /* Modern Certificate Grand Header */
          l.jsxs("div",{className:"text-center pb-4 mb-4 border-b-2 relative",style:{borderColor:"#d97706"},children:[
            l.jsxs("div",{className:"flex items-center justify-between gap-4 mb-3",children:[
              /* Left Monogram with Golden Ring */
              l.jsx("div",{className:"shrink-0 p-1.5 rounded-2xl shadow-md",style:{border:"3px solid #f59e0b",backgroundColor:"#ffffff"},children:
                l.jsx(Rw,{logoUrl:r.logoUrl,schoolName:r.schoolName,size:76})
              }),
              /* Center School Typography */
              l.jsxs("div",{className:"flex-1 text-center px-2",children:[
                l.jsx("div",{className:"text-[10px] font-black tracking-widest uppercase mb-0.5",style:{color:"#b45309"},children:"★ PRESTIGIOUS ACADEMIC EXCELLENCE & HONOURS GAZETTE ★"}),
                l.jsx("h1",{className:"text-2xl sm:text-3xl font-black uppercase tracking-tight leading-tight",style:{color:"#1e3a8a"},children:r.schoolName}),
                l.jsxs("div",{className:"text-xs sm:text-sm font-extrabold tracking-wide mt-1",style:{color:"#0f172a"},children:[r.campusName," • ",r.address]}),
                l.jsxs("div",{className:"text-[11px] font-bold mt-0.5",style:{color:"#475569"},children:["Board Affiliation: ",r.boardPattern||"BISE Punjab"," • Official Helpline: ",r.phone]})
              ]}),
              /* Right Golden Honors Rosette Badge */
              l.jsxs("div",{className:"shrink-0 hidden sm:flex flex-col items-center justify-center w-24 h-24 rounded-full p-1 text-center shadow-lg",style:{background:"linear-gradient(135deg, #fef3c7, #fde68a)",border:"3px solid #d97706",color:"#78350f"},children:[
                l.jsx("span",{className:"text-2xl",children:"🏅"}),
                l.jsx("span",{className:"text-[8px] font-black uppercase tracking-wider leading-tight",children:"Academic Award"}),
                l.jsx("span",{className:"text-[11px] font-black mt-0.5",children:R.session}),
                l.jsx("span",{className:"text-[7px] font-extrabold uppercase text-emerald-800",children:"Verified"})
              ]})
            ]}),
            /* Certificate Title Ribbon */
            l.jsxs("div",{className:"py-2 px-6 rounded-xl shadow-md mt-2",style:{backgroundColor:"#1e3a8a",border:"2px solid #f59e0b"},children:[
              l.jsx("h2",{className:"text-sm sm:text-base font-black uppercase tracking-widest",style:{color:"#fef08a"},children:"Certificate of Academic Achievement & Report Card"}),
              l.jsxs("p",{className:"text-[11px] font-bold tracking-wide mt-0.5",style:{color:"#ffffff"},children:["Academic Session: ",R.session," • Examination: ",R.examCategory," • Class: ",R.classLevel]})
            ]})
          ]}),

          /* Modern Executive Candidate Card */
          l.jsxs("div",{className:"rounded-2xl p-4 mb-5 shadow-xs flex flex-col sm:flex-row items-center gap-5",style:{backgroundColor:"#f0fdf4",border:"2px solid #059669"},children:[
            /* Circular Portrait with Golden Laurel Ring */
            l.jsxs("div",{className:"shrink-0 flex flex-col items-center",children:[
              l.jsx("div",{className:"w-24 h-24 rounded-full overflow-hidden shadow-md p-0.5",style:{border:"4px solid #f59e0b",backgroundColor:"#ffffff"},children:
                st.photoUrl?l.jsx("img",{src:st.photoUrl,alt:st.name,className:"w-full h-full object-cover rounded-full",style:{imageRendering:"-webkit-optimize-contrast"}}):
                l.jsxs("div",{className:"w-full h-full rounded-full flex flex-col items-center justify-center text-center",style:{backgroundColor:"#eff6ff"},children:[
                  l.jsx("span",{className:"text-2xl",children:"🎓"}),
                  l.jsx("span",{className:"text-[8px] font-black uppercase",style:{color:"#1e40af"},children:"Candidate"})
                ]})
              }),
              l.jsxs("div",{className:"mt-2 px-3 py-0.5 rounded-full font-black text-[11px] tracking-wider shadow-xs",style:{backgroundColor:"#1e3a8a",color:"#ffffff"},children:["Roll # ",st.rollNo]})
            ]}),
            /* Candidate Metadata Grid with Vibrant Colored Cards */
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
              l.jsxs("div",{className:"p-2.5 rounded-xl shadow-2xs",style:{backgroundColor:"#fef3c7",border:"2px solid #f59e0b"},children:[
                l.jsx("span",{className:"text-[9px] font-black uppercase tracking-wider block",style:{color:"#92400e"},children:"Class Standing"}),
                l.jsxs("span",{className:"text-xs font-black flex items-center gap-1 mt-0.5",style:{color:"#78350f"},children:[l.jsx("span",{children:"🏆"}),l.jsx("span",{children:st.rank||"1st Class"})]})
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
                    /* Obtained Marks in Bright High-Contrast Badge */
                    l.jsx("td",{className:"p-2 text-center border-r",style:{borderColor:"#e2e8f0"},children:
                      l.jsx("span",{className:"px-2.5 py-1 rounded-lg font-black text-xs inline-block",style:{backgroundColor:isPass?"#dbeafe":"#ffe4e6",color:isPass?"#1e40af":"#b91c1c",border:isPass?"1.5px solid #3b82f6":"1.5px solid #f43f5e"},children:obt})
                    }),
                    l.jsxs("td",{className:"p-2 text-center font-extrabold border-r",style:{color:"#0f172a",borderColor:"#e2e8f0"},children:[pct,"%"]}),
                    /* Grade in Bright Colored Pill */
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

          /* 4 Executive Stat Metric Cards (Deep High-Contrast Text) */
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
            l.jsxs("div",{className:"p-3.5 rounded-2xl text-center shadow-xs",style:{backgroundColor:"#fffbeb",border:"2.5px solid #d97706"},children:[
              l.jsx("span",{className:"text-[10px] uppercase font-black tracking-wider block",style:{color:"#92400e"},children:"Final Letter Grade"}),
              l.jsx("div",{className:"text-2xl font-black mt-1",style:{color:"#78350f"},children:q_stat.grade})
            ]}),
            /* Card 4: Status */
            l.jsxs("div",{className:"p-3.5 rounded-2xl text-center shadow-xs",style:{backgroundColor:q_stat.status==="PASS"?"#f0fdf4":"#fff1f2",border:q_stat.status==="PASS"?"2.5px solid #059669":"2.5px solid #e11d48"},children:[
              l.jsx("span",{className:"text-[10px] uppercase font-black tracking-wider block",style:{color:q_stat.status==="PASS"?"#065f46":"#9f1239"},children:"Official Result Status"}),
              l.jsx("div",{className:"text-base font-black mt-1",style:{color:q_stat.status==="PASS"?"#064e3b":"#881337"},children:q_stat.status==="PASS"?"PASSED WITH MERIT":"NEEDS IMPROVEMENT"})
            ]})
          ]}),

          /* Modern Commendation & Certified Badge */
          l.jsxs("div",{className:"rounded-2xl p-3.5 mb-6 flex flex-col sm:flex-row items-center justify-between gap-3 text-xs shadow-xs",style:{backgroundColor:"#fffbeb",border:"2px solid #f59e0b"},children:[
            l.jsxs("div",{className:"flex-1",children:[
              l.jsx("span",{className:"text-[10px] font-black uppercase tracking-wider block mb-0.5",style:{color:"#92400e"},children:"Executive Commendation & Remarks:"}),
              l.jsxs("p",{className:"italic leading-relaxed font-bold text-sm",style:{color:"#451a03"},children:['"',st.remarks||"Exhibits commendable scholastic performance, exemplary character, and high learning aptitude.",'"']})
            ]}),
            l.jsxs("div",{className:"shrink-0 flex items-center gap-2 px-3 py-1.5 rounded-xl text-[11px] font-black shadow-xs",style:{backgroundColor:"#fef3c7",border:"2px solid #d97706",color:"#78350f"},children:[
              l.jsx("span",{className:"text-xl",children:"🛡️"}),
              l.jsx("span",{children:"Institutionally Certified Record"})
            ]})
          ]}),

          /* Modern 3 Executive Signatures */
          l.jsxs("div",{className:"pt-6 border-t-2 grid grid-cols-3 text-center text-xs font-bold",style:{borderColor:"#d97706",color:"#0f172a"},children:[
            l.jsx("div",{children:l.jsx("div",{className:"w-36 border-t-2 mx-auto pt-1 font-black",style:{borderColor:"#1e3a8a"},children:"Controller Examinations"})}),
            l.jsx("div",{children:l.jsx("div",{className:"w-40 border-t-2 mx-auto pt-1 font-black",style:{borderColor:"#1e3a8a"},children:"Principal / Executive Seal"})}),
            l.jsx("div",{children:l.jsx("div",{className:"w-36 border-t-2 mx-auto pt-1 font-black",style:{borderColor:"#1e3a8a"},children:"Parent / Guardian"})})
          ]}),
          l.jsx("div",{className:"text-center text-[10px] font-extrabold mt-6 border-t pt-2 tracking-wider uppercase",style:{color:"#64748b",borderColor:"#e2e8f0"},children:"Modern Executive Certificate Edition • Designed for High-Distinction Recognition"})
        ]}),

        /* -------------------------------------------------------------
           DESIGN 3: MODERN STEM & ANALYTICAL DIAGNOSTIC INFOGRAPHIC
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

          /* Candidate Infographic Profile (5 Colorful Stat Tiles) */
          l.jsxs("div",{className:"grid grid-cols-2 sm:grid-cols-5 gap-2.5 mb-5 text-xs",children:[
            /* Tile 1: Photo & Name */
            l.jsxs("div",{className:"p-2.5 rounded-xl shadow-2xs flex items-center gap-2.5",style:{backgroundColor:"#f0f9ff",border:"2px solid #0284c7"},children:[
              l.jsx("div",{className:"w-11 h-11 rounded-full overflow-hidden bg-white shrink-0 shadow-xs",style:{border:"2.5px solid #0284c7"},children:
                st.photoUrl?l.jsx("img",{src:st.photoUrl,alt:st.name,className:"w-full h-full object-cover"}):
                l.jsx("div",{className:"w-full h-full flex items-center justify-center font-black text-xs",style:{color:"#0284c7"},children:"ID"})
              }),
              l.jsxs("div",{className:"min-w-0 flex-1",children:[
                l.jsx("span",{className:"text-[8px] font-black uppercase block",style:{color:"#0284c7"},children:"Candidate Name"}),
                l.jsx("span",{className:"text-xs font-black truncate block",style:{color:"#0c4a6e"},children:st.name}),
                l.jsxs("span",{className:"text-[10px] font-bold block",style:{color:"#0369a1"},children:["Roll # ",st.rollNo]})
              ]})
            ]}),
            /* Tile 2: Father Name */
            l.jsxs("div",{className:"p-2.5 rounded-xl shadow-2xs flex flex-col justify-center",style:{backgroundColor:"#faf5ff",border:"2px solid #8b5cf6"},children:[
              l.jsx("span",{className:"text-[8px] font-black uppercase block",style:{color:"#7c3aed"},children:"Father's Name"}),
              l.jsx("span",{className:"text-xs font-black truncate block mt-0.5",style:{color:"#581c87"},children:st.fatherName||"-"}),
              l.jsxs("span",{className:"text-[10px] font-bold block",style:{color:"#6b21a8"},children:["Sec: ",st.section||"A"]})
            ]}),
            /* Tile 3: Attendance */
            l.jsxs("div",{className:"p-2.5 rounded-xl shadow-2xs flex flex-col justify-center",style:{backgroundColor:"#ecfdf5",border:"2px solid #10b981"},children:[
              l.jsx("span",{className:"text-[8px] font-black uppercase block",style:{color:"#059669"},children:"Attendance & Punctuality"}),
              l.jsx("span",{className:"text-sm font-black block mt-0.5",style:{color:"#064e3b"},children:st.attendance||"96%"}),
              l.jsx("span",{className:"text-[10px] font-bold block",style:{color:"#047857"},children:"Regular Status"})
            ]}),
            /* Tile 4: Position Rank */
            l.jsxs("div",{className:"p-2.5 rounded-xl shadow-2xs flex flex-col justify-center",style:{backgroundColor:"#fffbeb",border:"2px solid #f59e0b"},children:[
              l.jsx("span",{className:"text-[8px] font-black uppercase block",style:{color:"#d97706"},children:"Class Position Rank"}),
              l.jsxs("span",{className:"text-sm font-black flex items-center gap-1 mt-0.5",style:{color:"#78350f"},children:[l.jsx("span",{children:"🏆"}),l.jsx("span",{children:st.rank||"Top Tier"})]}),
              l.jsx("span",{className:"text-[10px] font-bold block",style:{color:"#92400e"},children:"Merit Category"})
            ]}),
            /* Tile 5: Session */
            l.jsxs("div",{className:"p-2.5 rounded-xl shadow-2xs flex flex-col justify-center",style:{backgroundColor:"#f8fafc",border:"2px solid #64748b"},children:[
              l.jsx("span",{className:"text-[8px] font-black uppercase block",style:{color:"#475569"},children:"Academic Session"}),
              l.jsx("span",{className:"text-xs font-black block mt-0.5",style:{color:"#0f172a"},children:R.session}),
              l.jsx("span",{className:"text-[10px] font-bold block",style:{color:"#334155"},children:R.examCategory})
            ]})
          ]}),

          /* Subject Mastery Breakdown with Thick, Colorful 3D Progress Bars */
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
                else if(pNum>=70){grd="B";level="Competent 📘";barColor="#2563eb";badgeBg="#dbeafe";badgeColor="#1e40af";badgeBorder="#60a5fa";}
                else if(pNum>=60){grd="C";level="Developing 💡";barColor="#7c3aed";badgeBg="#ede9fe";badgeColor="#5b21b6";badgeBorder="#a78bfa";}
                else if(pNum>=50){grd="D";level="Basic 📙";barColor="#d97706";badgeBg="#fef3c7";badgeColor="#92400e";badgeBorder="#fbbf24";}
                else if(pNum>=40){grd="E";level="Marginal ⚠️";barColor="#ea580c";badgeBg="#ffedd5";badgeColor="#9a3412";badgeBorder="#fb923c";}
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
                  /* Thick 3D Visual Progress Bar */
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
            /* Holistic Behavioral Scorecard */
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
                  l.jsx("span",{className:"font-black",style:{color:"#7c2d12"},children:"100% On-Time"})
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

text = text[:start_idx] + new_templates + text[end_idx:]
print(f"[✓] Successfully injected vibrant, colorful templates! New bundle length: {len(text)}")

with open("assets/index-DAioIUjd.js", "w", encoding="utf-8") as f:
    f.write(text)

print("Saved updated assets/index-DAioIUjd.js!")
