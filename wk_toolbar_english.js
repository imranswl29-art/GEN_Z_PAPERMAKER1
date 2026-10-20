bold text-slate-500",children:"PTBB BISE Punjab Examination"})
        ]}),
        l.jsx("h2",{className:"text-base font-black text-slate-900 tracking-tight",children:"Multi-Functional Paper Control Suite"})
      ]})
    ]}),
    l.jsxs("div",{className:"flex items-center gap-2 flex-wrap",children:[
      l.jsxs("button",{type:"button",onClick:Z,className:"btn-print-preview flex items-center gap-2 px-4 py-2 bg-gradient-to-r from-emerald-600 to-teal-700 hover:from-emerald-500 hover:to-teal-600 text-white font-black text-xs rounded-xl shadow-md cursor-pointer transition-all",title:"Open browser print dialog for A4 Paper",children:[
        l.jsx(SAFE_od,{className:"w-4 h-4 text-emerald-100"}),
        l.jsx("span",{children:"Print & Preview"})
      ]}),
      l.jsxs("button",{type:"button",onClick:()=>ne(),disabled:C,className:"btn-3d btn-3d-red flex items-center gap-1.5 px-3.5 py-2 text-white rounded-xl text-xs font-black cursor-pointer shadow-xs",title:"Download High-Res PDF",children:[
        l.jsx(SAFE_ad,{className:"w-3.5 h-3.5 text-white"}),
        l.jsx("span",{children:C?"Exporting...":"PDF Download"})
      ]}),
      l.jsx("input",{ref:R,type:"file",accept:"image/*",className:"hidden",onChange:oe})
    ]})
  ]}),

  /* Master Hub Category Buttons */
  l.jsxs("div",{className:"space-y-1.5",children:[
    l.jsxs("div",{className:"flex items-center justify-between text-[11px] text-slate-600 font-bold px-1",children:[
      l.jsx("span",{children:"Select a tool to expand child buttons:"}),
      l.jsx("span",{className:"text-blue-700 font-bold",children:"Click any tool to access expanded controls ▾"})
    ]}),
    l.jsxs("div",{className:"flex items-center gap-2 overflow-x-auto pb-1 scrollbar-none",children:[
      l.jsxs("button",{type:"button",onClick:()=>setActiveHubTab(activeHubTab==="sections"?"":"sections"),className:"hub-btn " + (activeHubTab==="sections"?"hub-btn-active":""),children:[
        l.jsx(r8,{className:"w-3.5 h-3.5 " + (activeHubTab==="sections"?"text-blue-400":"text-blue-600")}),
        l.jsx("span",{children:"Paper Sections"}),
        l.jsx("span",{className:"hub-badge " + (activeHubTab==="sections"?"hub-badge-active":"hub-badge-inactive"),children:o==="all"?"All":o==="objective"?"MCQs":"Subjective"})
      ]}),
      l.jsxs("button",{type:"button",onClick:()=>setActiveHubTab(activeHubTab==="medium"?"":"medium"),className:"hub-btn " + (activeHubTab==="medium"?"hub-btn-active":""),children:[
        l.jsx("span",{children:"🌐"}),
        l.jsx("span",{children:"Language & Medium"}),
        l.jsx("span",{className:"hub-badge " + (activeHubTab==="medium"?"hub-badge-active":"hub-badge-inactive"),children:D==="bilingual"?"Bilingual":D==="english"?"English":"Urdu"})
      ]}),
      l.jsxs("button",{type:"button",onClick:()=>setActiveHubTab(activeHubTab==="sets"?"":"sets"),className:"hub-btn " + (activeHubTab==="sets"?"hub-btn-active":""),children:[
        l.jsx(SAFE_Ta,{className:"w-3.5 h-3.5 " + (activeHubTab==="sets"?"text-amber-400":"text-amber-600")}),
        l.jsx("span",{children:"Paper Sets & Shuffle"}),
        l.jsx("span",{className:"hub-badge " + (activeHubTab==="sets"?"hub-badge-active":"hub-badge-inactive"),children:"Set " + (n.header.paperSet||"A")})
      ]}),
      l.jsxs("button",{type:"button",onClick:()=>setActiveHubTab(activeHubTab==="bubble"?"":"bubble"),className:"hub-btn " + (activeHubTab==="bubble"?"hub-btn-active":""),children:[
        l.jsx(Ru,{className:"w-3.5 h-3.5 " + (activeHubTab==="bubble"?"text-emerald-400":"text-emerald-600")}),
        l.jsx("span",{children:"OMR Bubble Sheet"}),
        l.jsx("span",{className:"hub-badge " + (activeHubTab==="bubble"?"hub-badge-active":"hub-badge-inactive"),children:n.header.includeBubbleSheet!==!1?"ON":"OFF"})
      ]}),
      l.jsxs("button",{type:"button",onClick:()=>setActiveHubTab(activeHubTab==="layout"?"":"layout"),className:"hub-btn " + (activeHubTab==="layout"?"hub-btn-active":""),children:[
        l.jsx(J2,{className:"w-3.5 h-3.5 " + (activeHubTab==="layout"?"text-indigo-400":"text-indigo-600")}),
        l.jsx("span",{children:"Page & Layout"}),
        l.jsx("span",{className:"hub-badge " + (activeHubTab==="layout"?"hub-badge-active":"hub-badge-inactive"),children:paperOrientation==="portrait"?"Portrait":"Landscape"})
      ]}),
      l.jsxs("button",{type:"button",onClick:()=>setActiveHubTab(activeHubTab==="branding"?"":"branding"),className:"hub-btn " + (activeHubTab==="branding"?"hub-btn-active":""),children:[
        l.jsx("span",{children:"🛡️"}),
        l.jsx("span",{children:"Branding & Logo"}),
        l.jsx("span",{className:"hub-badge " + (activeHubTab==="branding"?"hub-badge-active":"hub-badge-inactive"),children:n.header.showWatermark?"ON":"OFF"})
      ]}),
      l.jsxs("button",{type:"button",onClick:()=>setActiveHubTab(activeHubTab==="editor"?"":"editor"),className:"hub-btn " + (activeHubTab==="editor"?"hub-btn-active":""),children:[
        l.jsx("span",{children:"✏️"}),
        l.jsx("span",{children:"Edit Questions"}),
        l.jsx("span",{className:"hub-badge " + (activeHubTab==="editor"?"hub-badge-active":"hub-badge-inactive"),children:u?"Active":"Off"})
      ]}),
      l.jsxs("button",{type:"button",onClick:()=>setActiveHubTab(activeHubTab==="downloads"?"":"downloads"),className:"hub-btn " + (activeHubTab==="downloads"?"hub-btn-active":""),children:[
        l.jsx(SAFE_ad,{className:"w-3.5 h-3.5 " + (activeHubTab==="downloads"?"text-rose-400":"text-rose-600")}),
        l.jsx("span",{children:"Downloads & Export"}),
        l.jsx("span",{className:"hub-badge " + (activeHubTab==="downloads"?"hub-badge-active":"hub-badge-inactive"),children:"PDF/Word"})
      ]}),
      l.jsxs("button",{type:"button",onClick:()=>setActiveHubTab(activeHubTab==="share"?"":"share"),className:"hub-btn " + (activeHubTab==="share"?"hub-btn-active":""),children:[
        l.jsx(K0,{className:"w-3.5 h-3.5 " + (activeHubTab==="share"?"text-emerald-400":"text-emerald-600")}),
        l.jsx("span",{children:"Share & Send"}),
        l.jsx("span",{className:"hub-badge " + (activeHubTab==="share"?"hub-badge-active":"hub-badge-inactive"),children:"WhatsApp"})
      ]})
    ]})
  ]}),

  /* Expanded Child Action Drawer */
  activeHubTab==="sections"&&l.jsxs("div",{className:"hub-child-drawer space-y-2.5",children:[
    l.jsxs("div",{className:"flex items-center justify-between border-b border-slate-200 pb-1.5",children:[
      l.jsxs("div",{className:"flex items-center gap-1.5 text-xs font-black text-slate-800",children:[
        l.jsx("span",{children:"📑"}),
        l.jsx("span",{children:"Select Section to View & Print:"})
      ]}),
      l.jsx("span",{className:"text-[10px] text-slate-500 font-bold",children:"Click any section to filter current view and print preview"})
    ]}),
    l.jsxs("div",{className:"flex flex-wrap items-center gap-2",children:[
      l.jsxs("button",{type:"button",onClick:()=>A("all"),className:"hub-child-btn " + (o==="all"?"hub-child-btn-active":""),children:[
        l.jsx(r8,{className:"w-4 h-4"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"Full Paper (All)"}),
          l.jsx("div",{className:"text-[10px] opacity-75 font-semibold",children:"Objective and Subjective sections"})
        ]}),
        o==="all"&&l.jsx("span",{className:"ml-2 text-xs font-black",children:"✓"})
      ]}),
      l.jsxs("button",{type:"button",onClick:()=>A("objective"),className:"hub-child-btn " + (o==="objective"?"hub-child-btn-active":""),children:[
        l.jsx(z3,{className:"w-4 h-4"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"Objective MCQs"}),
          l.jsx("div",{className:"text-[10px] opacity-75 font-semibold",children:"Multiple Choice Questions only"})
        ]}),
        o==="objective"&&l.jsx("span",{className:"ml-2 text-xs font-black",children:"✓"})
      ]}),
      l.jsxs("button",{type:"button",onClick:()=>A("subjective"),className:"hub-child-btn " + (o==="subjective"?"hub-child-btn-active":""),children:[
        l.jsx(i8,{className:"w-4 h-4"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"Subjective Questions"}),
          l.jsx("div",{className:"text-[10px] opacity-75 font-semibold",children:"Short and Long questions"})
        ]}),
        o==="subjective"&&l.jsx("span",{className:"ml-2 text-xs font-black",children:"✓"})
      ]}),
      a&&l.jsxs("button",{type:"button",onClick:a,className:"hub-child-btn border-emerald-300 text-emerald-800 hover:bg-emerald-50",children:[
        l.jsx(FC,{className:"w-4 h-4 text-emerald-600"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"Answer Key"}),
          l.jsx("div",{className:"text-[10px] text-emerald-600 font-semibold",children:"Complete solved answer guide"})
        ]})
      ]}),
      r&&l.jsxs("button",{type:"button",onClick:r,className:"hub-child-btn border-indigo-300 text-indigo-800 hover:bg-indigo-50",children:[
        l.jsx(Ru,{className:"w-4 h-4 text-indigo-600"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"OMR Response Grid"}),
          l.jsx("div",{className:"text-[10px] text-indigo-600 font-semibold",children:"Official bubble sheet for MCQs"})
        ]})
      ]})
    ]})
  ]}),

  activeHubTab==="medium"&&l.jsxs("div",{className:"hub-child-drawer space-y-2.5",children:[
    l.jsxs("div",{className:"flex items-center justify-between border-b border-slate-200 pb-1.5",children:[
      l.jsxs("div",{className:"flex items-center gap-1.5 text-xs font-black text-slate-800",children:[
        l.jsx("span",{children:"🌐"}),
        l.jsx("span",{children:"Select Language Medium:"})
      ]}),
      l.jsx("span",{className:"text-[10px] text-slate-500 font-bold",children:"Click any button to switch the paper language format immediately"})
    ]}),
    l.jsxs("div",{className:"flex flex-wrap items-center gap-2",children:[
      l.jsxs("button",{type:"button",onClick:()=>e({...n,languageMode:"bilingual"}),className:"hub-child-btn " + (D==="bilingual"?"hub-child-btn-active":""),children:[
        l.jsx("span",{className:"text-base",children:"🌐"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"Bilingual Mode"}),
          l.jsx("div",{className:"text-[10px] opacity-75 font-semibold",children:"English and Urdu side-by-side"})
        ]}),
        D==="bilingual"&&l.jsx("span",{className:"ml-2 text-xs font-black",children:"✓"})
      ]}),
      l.jsxs("button",{type:"button",onClick:()=>e({...n,languageMode:"english"}),className:"hub-child-btn " + (D==="english"?"hub-child-btn-active":""),children:[
        l.jsx("span",{className:"text-base",children:"🇬🇧"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"English Medium Only"}),
          l.jsx("div",{className:"text-[10px] opacity-75 font-semibold",children:"All questions in English only"})
        ]}),
        D==="english"&&l.jsx("span",{className:"ml-2 text-xs font-black",children:"✓"})
      ]}),
      l.jsxs("button",{type:"button",onClick:()=>e({...n,languageMode:"urdu"}),className:"hub-child-btn " + (D==="urdu"?"hub-child-btn-active":""),children:[
        l.jsx("span",{className:"text-base",children:"🇵🇰"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"Urdu Medium Only"}),
          l.jsx("div",{className:"text-[10px] opacity-75 font-semibold",children:"All questions in authentic Urdu Nastaliq"})
        ]}),
        D==="urdu"&&l.jsx("span",{className:"ml-2 text-xs font-black",children:"✓"})
      ]})
    ]})
  ]}),

  activeHubTab==="sets"&&l.jsxs("div",{className:"hub-child-drawer space-y-2.5",children:[
    l.jsxs("div",{className:"flex items-center justify-between border-b border-slate-200 pb-1.5",children:[
      l.jsxs("div",{className:"flex items-center gap-1.5 text-xs font-black text-slate-800",children:[
        l.jsx("span",{children:"🎲"}),
        l.jsx("span",{children:"Paper Codes, Sets & Question Shuffling:"})
      ]}),
      l.jsx("span",{className:"text-[10px] text-slate-500 font-bold",children:"Each set randomizes question and option sequences for exams"})
    ]}),
    l.jsxs("div",{className:"flex flex-wrap items-center gap-2",children:[
      l.jsxs("button",{type:"button",onClick:()=>Le("A"),className:"hub-child-btn " + ((n.header.paperSet||"A")==="A"?"hub-child-btn-active":""),children:[
        l.jsx("span",{className:"w-6 h-6 rounded-md bg-amber-500 text-white font-black text-xs flex items-center justify-center shrink-0",children:"A"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"Paper Set A"}),
          l.jsx("div",{className:"text-[10px] opacity-75 font-semibold",children:"Paper Code: 7105"})
        ]}),
        (n.header.paperSet||"A")==="A"&&l.jsx("span",{className:"ml-2 text-xs font-black",children:"✓"})
      ]}),
      l.jsxs("button",{type:"button",onClick:()=>Le("B"),className:"hub-child-btn " + (n.header.paperSet==="B"?"hub-child-btn-active":""),children:[
        l.jsx("span",{className:"w-6 h-6 rounded-md bg-indigo-500 text-white font-black text-xs flex items-center justify-center shrink-0",children:"B"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"Paper Set B"}),
          l.jsx("div",{className:"text-[10px] opacity-75 font-semibold",children:"Paper Code: 7284 (Shuffled)"})
        ]}),
        n.header.paperSet==="B"&&l.jsx("span",{className:"ml-2 text-xs font-black",children:"✓"})
      ]}),
      l.jsxs("button",{type:"button",onClick:()=>Le("C"),className:"hub-child-btn " + (n.header.paperSet==="C"?"hub-child-btn-active":""),children:[
        l.jsx("span",{className:"w-6 h-6 rounded-md bg-emerald-500 text-white font-black text-xs flex items-center justify-center shrink-0",children:"C"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"Paper Set C"}),
          l.jsx("div",{className:"text-[10px] opacity-75 font-semibold",children:"Paper Code: 7392 (Shuffled)"})
        ]}),
        n.header.paperSet==="C"&&l.jsx("span",{className:"ml-2 text-xs font-black",children:"✓"})
      ]}),
      l.jsxs("button",{type:"button",onClick:()=>{const s=n.header.paperSet==="A"?"B":n.header.paperSet==="B"?"C":"A";Le(s);},className:"hub-child-btn bg-purple-50 text-purple-900 border-purple-300 hover:bg-purple-100",children:[
        l.jsx(SAFE_Ta,{className:"w-4 h-4 text-purple-700"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"Shuffle Questions Now"}),
          l.jsx("div",{className:"text-[10px] text-purple-700 font-semibold",children:"Re-shuffle question sequences across paper"})
        ]})
      ]}),
      l.jsxs("button",{type:"button",onClick:()=>e({...n,header:{...n.header,hideRollNo:!n.header.hideRollNo}}),className:"hub-child-btn " + (!n.header.hideRollNo?"border-blue-400 bg-blue-50/50":"opacity-75"),children:[
        l.jsx("span",{children:"🔢"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"Roll No Grid Box"}),
          l.jsx("div",{className:"text-[10px] opacity-75 font-semibold",children:n.header.hideRollNo?"Roll No Box Hidden":"Roll No Box Visible"})
        ]}),
        !n.header.hideRollNo&&l.jsx("span",{className:"ml-2 text-xs font-black text-blue-600",children:"✓"})
      ]})
    ]})
  ]}),

  activeHubTab==="bubble"&&l.jsxs("div",{className:"hub-child-drawer space-y-2.5",children:[
    l.jsxs("div",{className:"flex items-center justify-between border-b border-slate-200 pb-1.5",children:[
      l.jsxs("div",{className:"flex items-center gap-1.5 text-xs font-black text-slate-800",children:[
        l.jsx("span",{children:"⭕"}),
        l.jsx("span",{children:"OMR Bubble Response Sheet Options:"})
      ]}),
      l.jsx("span",{className:"text-[10px] text-slate-500 font-bold",children:"Attach or detach official OMR bubble grid per board pattern"})
    ]}),
    l.jsxs("div",{className:"flex flex-wrap items-center gap-2",children:[
      l.jsxs("button",{type:"button",onClick:()=>e({...n,header:{...n.header,includeBubbleSheet:!0}}),className:"hub-child-btn " + (n.header.includeBubbleSheet!==!1?"hub-child-btn-active":""),children:[
        l.jsx(Ru,{className:"w-4 h-4"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"With Bubble Sheet"}),
          l.jsx("div",{className:"text-[10px] opacity-75 font-semibold",children:"Attached OMR bubble grid on the question paper"})
        ]}),
        n.header.includeBubbleSheet!==!1&&l.jsx("span",{className:"ml-2 text-xs font-black",children:"✓"})
      ]}),
      l.jsxs("button",{type:"button",onClick:()=>e({...n,header:{...n.header,includeBubbleSheet:!1}}),className:"hub-child-btn " + (n.header.includeBubbleSheet===!1?"hub-child-btn-active":""),children:[
        l.jsx("span",{className:"text-base",children:"✕"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"Without Bubble Sheet"}),
          l.jsx("div",{className:"text-[10px] opacity-75 font-semibold",children:"Standard question paper layout without bubble grid"})
        ]}),
        n.header.includeBubbleSheet===!1&&l.jsx("span",{className:"ml-2 text-xs font-black",children:"✓"})
      ]}),
      r&&l.jsxs("button",{type:"button",onClick:r,className:"hub-child-btn border-indigo-300 text-indigo-900 hover:bg-indigo-50",children:[
        l.jsx(SAFE_od,{className:"w-4 h-4 text-indigo-600"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"Print Standalone OMR Sheet"}),
          l.jsx("div",{className:"text-[10px] text-indigo-600 font-semibold",children:"Print dedicated standalone full-page OMR bubble sheet"})
        ]})
      ]})
    ]})
  ]}),

  activeHubTab==="layout"&&l.jsxs("div",{className:"hub-child-drawer space-y-2.5",children:[
    l.jsxs("div",{className:"flex items-center justify-between border-b border-slate-200 pb-1.5",children:[
      l.jsxs("div",{className:"flex items-center gap-1.5 text-xs font-black text-slate-800",children:[
        l.jsx("span",{children:"📐"}),
        l.jsx("span",{children:"Page Orientation, Font Size & Layout:"})
      ]}),
      l.jsx("span",{className:"text-[10px] text-slate-500 font-bold",children:"Optimize layout for single-page economy or readable large print"})
    ]}),
    l.jsxs("div",{className:"flex flex-wrap items-center gap-2",children:[
      l.jsxs("button",{type:"button",onClick:()=>setPaperOrientation("portrait"),className:"hub-child-btn " + (paperOrientation==="portrait"?"hub-child-btn-active":""),children:[
        l.jsx("span",{className:"text-base",children:"📄"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"Portrait Mode (Standard A4)"}),
          l.jsx("div",{className:"text-[10px] opacity-75 font-semibold",children:"Standard vertical single/multi-page layout"})
        ]}),
        paperOrientation==="portrait"&&l.jsx("span",{className:"ml-2 text-xs font-black",children:"✓"})
      ]}),
      l.jsxs("button",{type:"button",onClick:()=>setPaperOrientation("landscape"),className:"hub-child-btn " + (paperOrientation==="landscape"?"hub-child-btn-active":""),children:[
        l.jsx("span",{className:"text-base",children:"📑"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"Landscape Mode (2-Column A4)"}),
          l.jsx("div",{className:"text-[10px] opacity-75 font-semibold",children:"Dual-column landscape format for paper economy"})
        ]}),
        paperOrientation==="landscape"&&l.jsx("span",{className:"ml-2 text-xs font-black",children:"✓"})
      ]}),
      l.jsxs("button",{type:"button",onClick:()=>setFontSizeScale("compact"),className:"hub-child-btn " + (fontSizeScale==="compact"?"hub-child-btn-active":""),children:[
        l.jsx("span",{className:"text-base",children:"🔍"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"Compact Size (Fit 1 Page)"}),
          l.jsx("div",{className:"text-[10px] opacity-75 font-semibold",children:"Tight line spacing to economize paper printing"})
        ]}),
        fontSizeScale==="compact"&&l.jsx("span",{className:"ml-2 text-xs font-black",children:"✓"})
      ]}),
      l.jsxs("button",{type:"button",onClick:()=>setFontSizeScale("standard"),className:"hub-child-btn " + (fontSizeScale==="standard"?"hub-child-btn-active":""),children:[
        l.jsx("span",{className:"text-base",children:"📏"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"Standard BISE Size"}),
          l.jsx("div",{className:"text-[10px] opacity-75 font-semibold",children:"Balanced typography conforming to board standards"})
        ]}),
        fontSizeScale==="standard"&&l.jsx("span",{className:"ml-2 text-xs font-black",children:"✓"})
      ]}),
      l.jsxs("button",{type:"button",onClick:()=>setFontSizeScale("large"),className:"hub-child-btn " + (fontSizeScale==="large"?"hub-child-btn-active":""),children:[
        l.jsx("span",{className:"text-base",children:"🔎"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"Large Font Size"}),
          l.jsx("div",{className:"text-[10px] opacity-75 font-semibold",children:"Spacious high-legibility print formatting"})
        ]}),
        fontSizeScale==="large"&&l.jsx("span",{className:"ml-2 text-xs font-black",children:"✓"})
      ]}),
      l.jsxs("button",{type:"button",onClick:()=>setDoubleBorder(!doubleBorder),className:"hub-child-btn " + (doubleBorder?"border-slate-800 bg-slate-100":""),children:[
        l.jsx("span",{className:"text-base",children:"📦"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"Double Line Board Border"}),
          l.jsx("div",{className:"text-[10px] opacity-75 font-semibold",children:doubleBorder?"Double Border Enabled":"Simple Border Enabled"})
        ]}),
        doubleBorder&&l.jsx("span",{className:"ml-2 text-xs font-black text-blue-700",children:"✓"})
      ]})
    ]})
  ]}),

  activeHubTab==="branding"&&l.jsxs("div",{className:"hub-child-drawer space-y-2.5",children:[
    l.jsxs("div",{className:"flex items-center justify-between border-b border-slate-200 pb-1.5",children:[
      l.jsxs("div",{className:"flex items-center gap-1.5 text-xs font-black text-slate-800",children:[
        l.jsx("span",{children:"🛡️"}),
        l.jsx("span",{children:"Institutional Branding, Monogram & Watermark:"})
      ]}),
      l.jsx("span",{className:"text-[10px] text-slate-500 font-bold",children:"Configure official monogram, header crest, and background watermark"})
    ]}),
    l.jsxs("div",{className:"flex flex-wrap items-center gap-2",children:[
      l.jsxs("button",{type:"button",onClick:()=>e({...n,header:{...n.header,showWatermark:!0}}),className:"hub-child-btn " + (n.header.showWatermark?"hub-child-btn-active":""),children:[
        l.jsx("span",{className:"text-base",children:"💧"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"Watermark: ON"}),
          l.jsx("div",{className:"text-[10px] opacity-75 font-semibold",children:"Faint institutional watermark visible on paper background"})
        ]}),
        n.header.showWatermark&&l.jsx("span",{className:"ml-2 text-xs font-black",children:"✓"})
      ]}),
      l.jsxs("button",{type:"button",onClick:()=>e({...n,header:{...n.header,showWatermark:!1}}),className:"hub-child-btn " + (!n.header.showWatermark?"hub-child-btn-active":""),children:[
        l.jsx("span",{className:"text-base",children:"🚫"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"Watermark: OFF"}),
          l.jsx("div",{className:"text-[10px] opacity-75 font-semibold",children:"Clean background without watermark"})
        ]}),
        !n.header.showWatermark&&l.jsx("span",{className:"ml-2 text-xs font-black",children:"✓"})
      ]}),
      l.jsxs("button",{type:"button",onClick:()=>{var Ce;return(Ce=R.current)==null?void 0:Ce.click();},className:"hub-child-btn bg-amber-50 text-amber-950 border-amber-300 hover:bg-amber-100",children:[
        l.jsx("span",{className:"text-base",children:"📷"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"Upload School Monogram"}),
          l.jsx("div",{className:"text-[10px] text-amber-800 font-semibold",children:"Upload new school monogram / crest logo file"})
        ]})
      ]}),
      n.header.customLogoUrl&&l.jsxs("button",{type:"button",onClick:()=>e({...n,header:{...n.header,customLogoUrl:void 0}}),className:"hub-child-btn bg-rose-50 text-rose-800 border-rose-300 hover:bg-rose-100",children:[
        l.jsx("span",{className:"text-base",children:"✕"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"Remove Custom Logo"}),
          l.jsx("div",{className:"text-[10px] text-rose-600 font-semibold",children:"Remove custom monogram and restore default"})
        ]})
      ]})
    ]})
  ]}),

  activeHubTab==="editor"&&l.jsxs("div",{className:"hub-child-drawer space-y-2.5",children:[
    l.jsxs("div",{className:"flex items-center justify-between border-b border-slate-200 pb-1.5",children:[
      l.jsxs("div",{className:"flex items-center gap-1.5 text-xs font-black text-slate-800",children:[
        l.jsx("span",{children:"✏️"}),
        l.jsx("span",{children:"In-Place Question Editor & Customizer:"})
      ]}),
      l.jsx("span",{className:"text-[10px] text-slate-500 font-bold",children:"Edit question text directly on paper or add custom questions"})
    ]}),
    l.jsxs("div",{className:"flex flex-wrap items-center gap-2",children:[
      l.jsxs("button",{type:"button",onClick:()=>f(!u),className:"hub-child-btn " + (u?"hub-child-btn-active bg-amber-600 border-amber-600":""),children:[
        l.jsx("span",{className:"text-base",children:u?"✓":"✏️"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:u?"Finish Editing & Save Changes":"Edit Text Directly (Live Mode)"}),
          l.jsx("div",{className:"text-[10px] opacity-75 font-semibold",children:u?"All customized changes are saved to memory":"Click any question or option directly to edit text"})
        ]}),
        u&&l.jsx("span",{className:"ml-2 text-xs font-black",children:"✓"})
      ]}),
      l.jsxs("button",{type:"button",onClick:ce,className:"hub-child-btn bg-blue-50 text-blue-900 border-blue-300 hover:bg-blue-100",children:[
        l.jsx("span",{className:"text-base",children:"➕"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"+ Add New MCQ"}),
          l.jsx("div",{className:"text-[10px] text-blue-700 font-semibold",children:"Add New MCQ Question"})
        ]})
      ]}),
      l.jsxs("button",{type:"button",onClick:()=>{G.part1_shortQuestions[0]&&me(G.part1_shortQuestions[0].id)},className:"hub-child-btn bg-indigo-50 text-indigo-900 border-indigo-300 hover:bg-indigo-100",children:[
        l.jsx("span",{className:"text-base",children:"➕"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"+ Add Short Question"}),
          l.jsx("div",{className:"text-[10px] text-indigo-700 font-semibold",children:"Add New Short Question"})
        ]})
      ]}),
      l.jsxs("button",{type:"button",onClick:ue,className:"hub-child-btn bg-emerald-50 text-emerald-900 border-emerald-300 hover:bg-emerald-100",children:[
        l.jsx("span",{className:"text-base",children:"➕"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"+ Add Long Question"}),
          l.jsx("div",{className:"text-[10px] text-emerald-700 font-semibold",children:"Add New Long Question"})
        ]})
      ]})
    ]})
  ]}),

  activeHubTab==="downloads"&&l.jsxs("div",{className:"hub-child-drawer space-y-2.5",children:[
    l.jsxs("div",{className:"flex items-center justify-between border-b border-slate-200 pb-1.5",children:[
      l.jsxs("div",{className:"flex items-center gap-1.5 text-xs font-black text-slate-800",children:[
        l.jsx("span",{children:"📥"}),
        l.jsx("span",{children:"Download & Export Formats:"})
      ]}),
      l.jsx("span",{className:"text-[10px] text-slate-500 font-bold",children:"Save high-resolution PDF or editable Microsoft Word files"})
    ]}),
    l.jsxs("div",{className:"flex flex-wrap items-center gap-2",children:[
      l.jsxs("button",{type:"button",onClick:ne,disabled:C,className:"hub-child-btn hub-child-btn-active",children:[
        l.jsx(SAFE_ad,{className:"w-4 h-4 text-white"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:C?"Preparing PDF...":"Download High-Res PDF (.pdf)"}),
          l.jsx("div",{className:"text-[10px] opacity-75 font-semibold",children:"Print-ready vector PDF formatted for A4 paper"})
        ]})
      ]}),
      l.jsxs("button",{type:"button",onClick:()=>z0(n,o),className:"hub-child-btn border-blue-400 bg-blue-50 text-blue-900 hover:bg-blue-100",children:[
        l.jsx(Xu,{className:"w-4 h-4 text-blue-700"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"Download MS Word (.doc)"}),
          l.jsx("div",{className:"text-[10px] text-blue-700 font-semibold",children:"Fully editable Microsoft Word (.doc) document"})
        ]})
      ]}),
      a&&l.jsxs("button",{type:"button",onClick:a,className:"hub-child-btn border-emerald-400 bg-emerald-50 text-emerald-900 hover:bg-emerald-100",children:[
        l.jsx(FC,{className:"w-4 h-4 text-emerald-700"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"Download Solved Key"}),
          l.jsx("div",{className:"text-[10px] text-emerald-700 font-semibold",children:"Full answer key and grading guide PDF"})
        ]})
      ]}),
      r&&l.jsxs("button",{type:"button",onClick:r,className:"hub-child-btn border-indigo-400 bg-indigo-50 text-indigo-900 hover:bg-indigo-100",children:[
        l.jsx(Ru,{className:"w-4 h-4 text-indigo-700"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"Download Bubble Sheet PDF"}),
          l.jsx("div",{className:"text-[10px] text-indigo-700 font-semibold",children:"Blank printable OMR bubble response sheet PDF"})
        ]})
      ]})
    ]})
  ]}),

  activeHubTab==="share"&&l.jsxs("div",{className:"hub-child-drawer space-y-2.5",children:[
    l.jsxs("div",{className:"flex items-center justify-between border-b border-slate-200 pb-1.5",children:[
      l.jsxs("div",{className:"flex items-center gap-1.5 text-xs font-black text-slate-800",children:[
        l.jsx("span",{children:"📢"}),
        l.jsx("span",{children:"Share & Distribute Paper:"})
      ]}),
      l.jsx("span",{className:"text-[10px] text-slate-500 font-bold",children:"Instantly send to teachers or students via WhatsApp or web link"})
    ]}),
    l.jsxs("div",{className:"flex flex-wrap items-center gap-2",children:[
      l.jsxs("button",{type:"button",onClick:P,className:"hub-child-btn hub-child-btn-emerald",children:[
        l.jsx(K0,{className:"w-4 h-4 text-white"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"Share via WhatsApp"}),
          l.jsx("div",{className:"text-[10px] opacity-75 font-semibold",children:"Send formatted paper details directly via WhatsApp"})
        ]})
      ]}),
      l.jsxs("button",{type:"button",onClick:te,className:"hub-child-btn border-purple-400 bg-purple-50 text-purple-900 hover:bg-purple-100",children:[
        l.jsx($2,{className:"w-4 h-4 text-purple-700"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"Copy Paper Link"}),
          l.jsx("div",{className:"text-[10px] text-purple-700 font-semibold",children:"Copy direct shareable web link to clipboard"})
        ]})
      ]}),
      l.jsxs("button",{type:"button",onClick:te,className:"hub-child-btn border-slate-300 hover:bg-slate-50",children:[
        l.jsx("span",{className:"text-base",children:"📱"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"Device Share Dialog"}),
          l.jsx("div",{className:"text-[10px] text-slate-600 font-semibold",children:"Open native operating system sharing menu"})
        ]})
      ]})
    ]})
  ]})
]}),
C&&l.jsxs("div",{className:"no-print bg-gradient-to-r from-indigo-600 to-blue-600 text-white px-4 py-2 text-xs font-bold flex items-center justify-center gap-2 animate-pulse shadow-md",children:[l.jsx(Sc,{className:"w-4 h-4 animate-spin text-white"}),l.jsx("span",{children:v||"Generating High-Resolution PDF... Please wait a few seconds"})]}),
B&&l.jsxs("div",{className:"no-print bg-blue-50 border-b border-blue-200 px-4 py-2.5 text-xs text-blue-950 flex items-center justify-between",children:[l.jsxs("div",{className:"flex items-center gap-2",children:[l.jsx(G3,{className:"w-4 h-4 text-blue-600 shrink-0"}),l.jsxs("div",{children:[l.jsx("span",{className:"font-bold",children:"PDF Direct Download Note: "}),"If direct download was blocked by browser permissions, select ",l.jsx("strong",{children:'"Save as PDF"'})," in the print dialog."]})]}),l.jsx("button",{type:"button",onClick:()=>m(!1),className:"text-blue-800 font-bold ml-2 text-sm hover:text-blue-900 cursor-pointer",children:"✕"})]}),l.jsxs("div",{id:"