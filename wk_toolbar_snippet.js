bold text-slate-500",children:"PTBB BISE Punjab Examination"})
        ]}),
        l.jsx("h2",{className:"text-base font-black text-slate-900 tracking-tight",children:"ملٹی فنکشنل پیپر کنٹرول سینٹر (Multi-Functional Paper Suite)"})
      ]})
    ]}),
    l.jsxs("div",{className:"flex items-center gap-2 flex-wrap",children:[
      l.jsxs("button",{type:"button",onClick:Z,className:"btn-print-preview flex items-center gap-2 px-4 py-2 bg-gradient-to-r from-emerald-600 to-teal-700 hover:from-emerald-500 hover:to-teal-600 text-white font-black text-xs rounded-xl shadow-md cursor-pointer transition-all",title:"Open browser print dialog for A4 Paper",children:[
        l.jsx(SAFE_od,{className:"w-4 h-4 text-emerald-100"}),
        l.jsx("span",{children:"Print & Preview (پرنٹ کریں)"})
      ]}),
      l.jsxs("button",{type:"button",onClick:()=>ne(),disabled:C,className:"btn-3d btn-3d-red flex items-center gap-1.5 px-3.5 py-2 text-white rounded-xl text-xs font-black cursor-pointer shadow-xs",title:"Download High-Res PDF",children:[
        l.jsx(SAFE_ad,{className:"w-3.5 h-3.5 text-white"}),
        l.jsx("span",{children:C?"Exporting...":"PDF Download"})
      ]}),
      l.jsx("input",{ref:R,type:"file",accept:"image/*",className:"hidden",onChange:oe})
    ]})
  ]}),

  /* Master Hub Category Buttons (ہر بٹن کے اندر مزید آپشنز) */
  l.jsxs("div",{className:"space-y-1.5",children:[
    l.jsxs("div",{className:"flex items-center justify-between text-[11px] text-slate-600 font-bold px-1",children:[
      l.jsx("span",{children:"ٹول منتخب کریں (کلک کرنے سے نیچے مزید بٹن اوپن ہوں گے):"}),
      l.jsx("span",{className:"text-blue-700 font-bold",children:"Select a tool to expand child buttons ▾"})
    ]}),
    l.jsxs("div",{className:"flex items-center gap-2 overflow-x-auto pb-1 scrollbar-none",children:[
      l.jsxs("button",{type:"button",onClick:()=>setActiveHubTab(activeHubTab==="sections"?"":"sections"),className:"hub-btn " + (activeHubTab==="sections"?"hub-btn-active":""),children:[
        l.jsx(r8,{className:"w-3.5 h-3.5 " + (activeHubTab==="sections"?"text-blue-400":"text-blue-600")}),
        l.jsx("span",{children:"پیپر سیکشنز"}),
        l.jsx("span",{className:"hub-badge " + (activeHubTab==="sections"?"hub-badge-active":"hub-badge-inactive"),children:o==="all"?"مکمل":o==="objective"?"معروضی":"انشائیہ"})
      ]}),
      l.jsxs("button",{type:"button",onClick:()=>setActiveHubTab(activeHubTab==="medium"?"":"medium"),className:"hub-btn " + (activeHubTab==="medium"?"hub-btn-active":""),children:[
        l.jsx("span",{children:"🌐"}),
        l.jsx("span",{children:"زبان اور میڈیم"}),
        l.jsx("span",{className:"hub-badge " + (activeHubTab==="medium"?"hub-badge-active":"hub-badge-inactive"),children:D==="bilingual"?"دو لسانی":D==="english"?"انگلش":"اردو"})
      ]}),
      l.jsxs("button",{type:"button",onClick:()=>setActiveHubTab(activeHubTab==="sets"?"":"sets"),className:"hub-btn " + (activeHubTab==="sets"?"hub-btn-active":""),children:[
        l.jsx(SAFE_Ta,{className:"w-3.5 h-3.5 " + (activeHubTab==="sets"?"text-amber-400":"text-amber-600")}),
        l.jsx("span",{children:"پیپر سیٹس اور شفل"}),
        l.jsx("span",{className:"hub-badge " + (activeHubTab==="sets"?"hub-badge-active":"hub-badge-inactive"),children:"Set " + (n.header.paperSet||"A")})
      ]}),
      l.jsxs("button",{type:"button",onClick:()=>setActiveHubTab(activeHubTab==="bubble"?"":"bubble"),className:"hub-btn " + (activeHubTab==="bubble"?"hub-btn-active":""),children:[
        l.jsx(Ru,{className:"w-3.5 h-3.5 " + (activeHubTab==="bubble"?"text-emerald-400":"text-emerald-600")}),
        l.jsx("span",{children:"ببل شیٹ"}),
        l.jsx("span",{className:"hub-badge " + (activeHubTab==="bubble"?"hub-badge-active":"hub-badge-inactive"),children:n.header.includeBubbleSheet!==!1?"آن":"آف"})
      ]}),
      l.jsxs("button",{type:"button",onClick:()=>setActiveHubTab(activeHubTab==="layout"?"":"layout"),className:"hub-btn " + (activeHubTab==="layout"?"hub-btn-active":""),children:[
        l.jsx(J2,{className:"w-3.5 h-3.5 " + (activeHubTab==="layout"?"text-indigo-400":"text-indigo-600")}),
        l.jsx("span",{children:"صفحہ اور لے آؤٹ"}),
        l.jsx("span",{className:"hub-badge " + (activeHubTab==="layout"?"hub-badge-active":"hub-badge-inactive"),children:paperOrientation==="portrait"?"Portrait":"Landscape"})
      ]}),
      l.jsxs("button",{type:"button",onClick:()=>setActiveHubTab(activeHubTab==="branding"?"":"branding"),className:"hub-btn " + (activeHubTab==="branding"?"hub-btn-active":""),children:[
        l.jsx("span",{children:"🛡️"}),
        l.jsx("span",{children:"لوگو اور واٹر مارک"}),
        l.jsx("span",{className:"hub-badge " + (activeHubTab==="branding"?"hub-badge-active":"hub-badge-inactive"),children:n.header.showWatermark?"ON":"OFF"})
      ]}),
      l.jsxs("button",{type:"button",onClick:()=>setActiveHubTab(activeHubTab==="editor"?"":"editor"),className:"hub-btn " + (activeHubTab==="editor"?"hub-btn-active":""),children:[
        l.jsx("span",{children:"✏️"}),
        l.jsx("span",{children:"سوالات ایڈٹ کریں"}),
        l.jsx("span",{className:"hub-badge " + (activeHubTab==="editor"?"hub-badge-active":"hub-badge-inactive"),children:u?"Active":"Off"})
      ]}),
      l.jsxs("button",{type:"button",onClick:()=>setActiveHubTab(activeHubTab==="downloads"?"":"downloads"),className:"hub-btn " + (activeHubTab==="downloads"?"hub-btn-active":""),children:[
        l.jsx(SAFE_ad,{className:"w-3.5 h-3.5 " + (activeHubTab==="downloads"?"text-rose-400":"text-rose-600")}),
        l.jsx("span",{children:"ڈاؤن لوڈز"}),
        l.jsx("span",{className:"hub-badge " + (activeHubTab==="downloads"?"hub-badge-active":"hub-badge-inactive"),children:"PDF/Word"})
      ]}),
      l.jsxs("button",{type:"button",onClick:()=>setActiveHubTab(activeHubTab==="share"?"":"share"),className:"hub-btn " + (activeHubTab==="share"?"hub-btn-active":""),children:[
        l.jsx(K0,{className:"w-3.5 h-3.5 " + (activeHubTab==="share"?"text-emerald-400":"text-emerald-600")}),
        l.jsx("span",{children:"شیئر کریں"}),
        l.jsx("span",{className:"hub-badge " + (activeHubTab==="share"?"hub-badge-active":"hub-badge-inactive"),children:"WhatsApp"})
      ]})
    ]})
  ]}),

  /* Expanded Child Action Drawer */
  activeHubTab==="sections"&&l.jsxs("div",{className:"hub-child-drawer space-y-2.5",children:[
    l.jsxs("div",{className:"flex items-center justify-between border-b border-slate-200 pb-1.5",children:[
      l.jsxs("div",{className:"flex items-center gap-1.5 text-xs font-black text-slate-800",children:[
        l.jsx("span",{children:"📑"}),
        l.jsx("span",{children:"پیپر سیکشنز کا انتخاب (Select Section to View & Print):"})
      ]}),
      l.jsx("span",{className:"text-[10px] text-slate-500 font-bold",children:"کلک کرنے پر پرچہ کا مطلوبہ حصہ ظاہر ہوگا"})
    ]}),
    l.jsxs("div",{className:"flex flex-wrap items-center gap-2",children:[
      l.jsxs("button",{type:"button",onClick:()=>A("all"),className:"hub-child-btn " + (o==="all"?"hub-child-btn-active":""),children:[
        l.jsx(r8,{className:"w-4 h-4"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"مکمل پرچہ (Full Paper - All)"}),
          l.jsx("div",{className:"text-[10px] opacity-75 font-semibold",children:"معروضی اور انشائیہ دونوں حصے"})
        ]}),
        o==="all"&&l.jsx("span",{className:"ml-2 text-xs font-black",children:"✓"})
      ]}),
      l.jsxs("button",{type:"button",onClick:()=>A("objective"),className:"hub-child-btn " + (o==="objective"?"hub-child-btn-active":""),children:[
        l.jsx(z3,{className:"w-4 h-4"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"معروضی پرچہ (Objective MCQs)"}),
          l.jsx("div",{className:"text-[10px] opacity-75 font-semibold",children:"صرف کثیر الانتخابی سوالات"})
        ]}),
        o==="objective"&&l.jsx("span",{className:"ml-2 text-xs font-black",children:"✓"})
      ]}),
      l.jsxs("button",{type:"button",onClick:()=>A("subjective"),className:"hub-child-btn " + (o==="subjective"?"hub-child-btn-active":""),children:[
        l.jsx(i8,{className:"w-4 h-4"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"انشائیہ پرچہ (Subjective Questions)"}),
          l.jsx("div",{className:"text-[10px] opacity-75 font-semibold",children:"مختصر اور تفصیلی سوالات"})
        ]}),
        o==="subjective"&&l.jsx("span",{className:"ml-2 text-xs font-black",children:"✓"})
      ]}),
      a&&l.jsxs("button",{type:"button",onClick:a,className:"hub-child-btn border-emerald-300 text-emerald-800 hover:bg-emerald-50",children:[
        l.jsx(FC,{className:"w-4 h-4 text-emerald-600"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"حل شدہ جوابی کلید (Answer Key)"}),
          l.jsx("div",{className:"text-[10px] text-emerald-600 font-semibold",children:"درست جوابات کی مکمل شیٹ"})
        ]})
      ]}),
      r&&l.jsxs("button",{type:"button",onClick:r,className:"hub-child-btn border-indigo-300 text-indigo-800 hover:bg-indigo-50",children:[
        l.jsx(Ru,{className:"w-4 h-4 text-indigo-600"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"ببل رسپانس شیٹ (OMR Grid)"}),
          l.jsx("div",{className:"text-[10px] text-indigo-600 font-semibold",children:"الگ امتحانی دائرہ شیٹ"})
        ]})
      ]})
    ]})
  ]}),

  activeHubTab==="medium"&&l.jsxs("div",{className:"hub-child-drawer space-y-2.5",children:[
    l.jsxs("div",{className:"flex items-center justify-between border-b border-slate-200 pb-1.5",children:[
      l.jsxs("div",{className:"flex items-center gap-1.5 text-xs font-black text-slate-800",children:[
        l.jsx("span",{children:"🌐"}),
        l.jsx("span",{children:"زبان اور میڈیم کا انتخاب (Select Language Medium):"})
      ]}),
      l.jsx("span",{className:"text-[10px] text-slate-500 font-bold",children:"کسی بھی بٹن پر کلک کریں، پرچہ فوری اس زبان میں تبدیل ہو جائے گا"})
    ]}),
    l.jsxs("div",{className:"flex flex-wrap items-center gap-2",children:[
      l.jsxs("button",{type:"button",onClick:()=>e({...n,languageMode:"bilingual"}),className:"hub-child-btn " + (D==="bilingual"?"hub-child-btn-active":""),children:[
        l.jsx("span",{className:"text-base",children:"🌐"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"Bilingual Mode (دو لسانی)"}),
          l.jsx("div",{className:"text-[10px] opacity-75 font-semibold",children:"English + Urdu Nastaliq یکجا"})
        ]}),
        D==="bilingual"&&l.jsx("span",{className:"ml-2 text-xs font-black",children:"✓"})
      ]}),
      l.jsxs("button",{type:"button",onClick:()=>e({...n,languageMode:"english"}),className:"hub-child-btn " + (D==="english"?"hub-child-btn-active":""),children:[
        l.jsx("span",{className:"text-base",children:"🇬🇧"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"English Medium Only"}),
          l.jsx("div",{className:"text-[10px] opacity-75 font-semibold",children:"صرف خالص انگریزی سوالات"})
        ]}),
        D==="english"&&l.jsx("span",{className:"ml-2 text-xs font-black",children:"✓"})
      ]}),
      l.jsxs("button",{type:"button",onClick:()=>e({...n,languageMode:"urdu"}),className:"hub-child-btn " + (D==="urdu"?"hub-child-btn-active":""),children:[
        l.jsx("span",{className:"text-base",children:"🇵🇰"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"Urdu Medium Only (اردو میڈیم)"}),
          l.jsx("div",{className:"text-[10px] opacity-75 font-semibold",children:"صرف خالص اردو خط نستعلیق"})
        ]}),
        D==="urdu"&&l.jsx("span",{className:"ml-2 text-xs font-black",children:"✓"})
      ]})
    ]})
  ]}),

  activeHubTab==="sets"&&l.jsxs("div",{className:"hub-child-drawer space-y-2.5",children:[
    l.jsxs("div",{className:"flex items-center justify-between border-b border-slate-200 pb-1.5",children:[
      l.jsxs("div",{className:"flex items-center gap-1.5 text-xs font-black text-slate-800",children:[
        l.jsx("span",{children:"🎲"}),
        l.jsx("span",{children:"پیپر کوڈز، سیٹس اور سوالات شفلنگ (Paper Sets & Shuffling):"})
      ]}),
      l.jsx("span",{className:"text-[10px] text-slate-500 font-bold",children:"ہر سیٹ میں سوالات اور آپشنز کی ترتیب مختلف ہوتی ہے"})
    ]}),
    l.jsxs("div",{className:"flex flex-wrap items-center gap-2",children:[
      l.jsxs("button",{type:"button",onClick:()=>Le("A"),className:"hub-child-btn " + ((n.header.paperSet||"A")==="A"?"hub-child-btn-active":""),children:[
        l.jsx("span",{className:"w-6 h-6 rounded-md bg-amber-500 text-white font-black text-xs flex items-center justify-center shrink-0",children:"A"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"Set A (سیٹ الف)"}),
          l.jsx("div",{className:"text-[10px] opacity-75 font-semibold",children:"Paper Code: 7105"})
        ]}),
        (n.header.paperSet||"A")==="A"&&l.jsx("span",{className:"ml-2 text-xs font-black",children:"✓"})
      ]}),
      l.jsxs("button",{type:"button",onClick:()=>Le("B"),className:"hub-child-btn " + (n.header.paperSet==="B"?"hub-child-btn-active":""),children:[
        l.jsx("span",{className:"w-6 h-6 rounded-md bg-indigo-500 text-white font-black text-xs flex items-center justify-center shrink-0",children:"B"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"Set B (سیٹ ب)"}),
          l.jsx("div",{className:"text-[10px] opacity-75 font-semibold",children:"Paper Code: 7284 (Shuffled)"})
        ]}),
        n.header.paperSet==="B"&&l.jsx("span",{className:"ml-2 text-xs font-black",children:"✓"})
      ]}),
      l.jsxs("button",{type:"button",onClick:()=>Le("C"),className:"hub-child-btn " + (n.header.paperSet==="C"?"hub-child-btn-active":""),children:[
        l.jsx("span",{className:"w-6 h-6 rounded-md bg-emerald-500 text-white font-black text-xs flex items-center justify-center shrink-0",children:"C"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"Set C (سیٹ ج)"}),
          l.jsx("div",{className:"text-[10px] opacity-75 font-semibold",children:"Paper Code: 7392 (Shuffled)"})
        ]}),
        n.header.paperSet==="C"&&l.jsx("span",{className:"ml-2 text-xs font-black",children:"✓"})
      ]}),
      l.jsxs("button",{type:"button",onClick:()=>{const s=n.header.paperSet==="A"?"B":n.header.paperSet==="B"?"C":"A";Le(s);},className:"hub-child-btn bg-purple-50 text-purple-900 border-purple-300 hover:bg-purple-100",children:[
        l.jsx(SAFE_Ta,{className:"w-4 h-4 text-purple-700"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"Shuffle Questions Now"}),
          l.jsx("div",{className:"text-[10px] text-purple-700 font-semibold",children:"تمام سوالات فوری طور پر تبدیل کریں"})
        ]})
      ]}),
      l.jsxs("button",{type:"button",onClick:()=>e({...n,header:{...n.header,hideRollNo:!n.header.hideRollNo}}),className:"hub-child-btn " + (!n.header.hideRollNo?"border-blue-400 bg-blue-50/50":"opacity-75"),children:[
        l.jsx("span",{children:"🔢"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"Roll No Grid Box"}),
          l.jsx("div",{className:"text-[10px] opacity-75 font-semibold",children:n.header.hideRollNo?"رول نمبر باکس چھپا ہوا":"رول نمبر باکس آن ہے"})
        ]}),
        !n.header.hideRollNo&&l.jsx("span",{className:"ml-2 text-xs font-black text-blue-600",children:"✓"})
      ]})
    ]})
  ]}),

  activeHubTab==="bubble"&&l.jsxs("div",{className:"hub-child-drawer space-y-2.5",children:[
    l.jsxs("div",{className:"flex items-center justify-between border-b border-slate-200 pb-1.5",children:[
      l.jsxs("div",{className:"flex items-center gap-1.5 text-xs font-black text-slate-800",children:[
        l.jsx("span",{children:"⭕"}),
        l.jsx("span",{children:"امتحانی ببل شیٹ آپشنز (OMR Bubble Response Sheet):"})
      ]}),
      l.jsx("span",{className:"text-[10px] text-slate-500 font-bold",children:"امتحانی بورڈ کے مطابق پیپر پر ببل گرڈ شامل یا خارج کریں"})
    ]}),
    l.jsxs("div",{className:"flex flex-wrap items-center gap-2",children:[
      l.jsxs("button",{type:"button",onClick:()=>e({...n,header:{...n.header,includeBubbleSheet:!0}}),className:"hub-child-btn " + (n.header.includeBubbleSheet!==!1?"hub-child-btn-active":""),children:[
        l.jsx(Ru,{className:"w-4 h-4"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"With Bubble Sheet (ببل شیٹ شامل کریں)"}),
          l.jsx("div",{className:"text-[10px] opacity-75 font-semibold",children:"پرچے پر طالب علم کے لیے دائرہ گرڈ ظاہر ہوگی"})
        ]}),
        n.header.includeBubbleSheet!==!1&&l.jsx("span",{className:"ml-2 text-xs font-black",children:"✓"})
      ]}),
      l.jsxs("button",{type:"button",onClick:()=>e({...n,header:{...n.header,includeBubbleSheet:!1}}),className:"hub-child-btn " + (n.header.includeBubbleSheet===!1?"hub-child-btn-active":""),children:[
        l.jsx("span",{className:"text-base",children:"✕"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"Without Bubble Sheet (بغیر ببل شیٹ)"}),
          l.jsx("div",{className:"text-[10px] opacity-75 font-semibold",children:"صرف خالص سوالات، کوئی ببل گرڈ نہیں"})
        ]}),
        n.header.includeBubbleSheet===!1&&l.jsx("span",{className:"ml-2 text-xs font-black",children:"✓"})
      ]}),
      r&&l.jsxs("button",{type:"button",onClick:r,className:"hub-child-btn border-indigo-300 text-indigo-900 hover:bg-indigo-50",children:[
        l.jsx(SAFE_od,{className:"w-4 h-4 text-indigo-600"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"Print Standalone OMR Sheet"}),
          l.jsx("div",{className:"text-[10px] text-indigo-600 font-semibold",children:"مکمل ایک صفحے کی علیحدہ ببل شیٹ پرنٹ کریں"})
        ]})
      ]})
    ]})
  ]}),

  activeHubTab==="layout"&&l.jsxs("div",{className:"hub-child-drawer space-y-2.5",children:[
    l.jsxs("div",{className:"flex items-center justify-between border-b border-slate-200 pb-1.5",children:[
      l.jsxs("div",{className:"flex items-center gap-1.5 text-xs font-black text-slate-800",children:[
        l.jsx("span",{children:"📐"}),
        l.jsx("span",{children:"صفحہ کا رخ، فونٹ سائز اور فریم بارڈر (Layout & Formatting):"})
      ]}),
      l.jsx("span",{className:"text-[10px] text-slate-500 font-bold",children:"صفحات کی بچت یا بڑے پرنٹ کے لیے موزوں سائز منتخب کریں"})
    ]}),
    l.jsxs("div",{className:"flex flex-wrap items-center gap-2",children:[
      l.jsxs("button",{type:"button",onClick:()=>setPaperOrientation("portrait"),className:"hub-child-btn " + (paperOrientation==="portrait"?"hub-child-btn-active":""),children:[
        l.jsx("span",{className:"text-base",children:"📄"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"عمودی صفحہ (Portrait A4)"}),
          l.jsx("div",{className:"text-[10px] opacity-75 font-semibold",children:"معیاری سیدھا رخ"})
        ]}),
        paperOrientation==="portrait"&&l.jsx("span",{className:"ml-2 text-xs font-black",children:"✓"})
      ]}),
      l.jsxs("button",{type:"button",onClick:()=>setPaperOrientation("landscape"),className:"hub-child-btn " + (paperOrientation==="landscape"?"hub-child-btn-active":""),children:[
        l.jsx("span",{className:"text-base",children:"📑"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"افقی صفحہ (Landscape A4)"}),
          l.jsx("div",{className:"text-[10px] opacity-75 font-semibold",children:"چوڑا رخ (2 کالم پیپر)"})
        ]}),
        paperOrientation==="landscape"&&l.jsx("span",{className:"ml-2 text-xs font-black",children:"✓"})
      ]}),
      l.jsxs("button",{type:"button",onClick:()=>setFontSizeScale("compact"),className:"hub-child-btn " + (fontSizeScale==="compact"?"hub-child-btn-active":""),children:[
        l.jsx("span",{className:"text-base",children:"🔍"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"کمپیکٹ سائز (Fit 1 Page)"}),
          l.jsx("div",{className:"text-[10px] opacity-75 font-semibold",children:"1 صفحہ پر پرچہ سمیٹیں"})
        ]}),
        fontSizeScale==="compact"&&l.jsx("span",{className:"ml-2 text-xs font-black",children:"✓"})
      ]}),
      l.jsxs("button",{type:"button",onClick:()=>setFontSizeScale("standard"),className:"hub-child-btn " + (fontSizeScale==="standard"?"hub-child-btn-active":""),children:[
        l.jsx("span",{className:"text-base",children:"📏"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"معیاری سائز (Standard BISE)"}),
          l.jsx("div",{className:"text-[10px] opacity-75 font-semibold",children:"بورڈ پیٹرن کا متوازن فونٹ"})
        ]}),
        fontSizeScale==="standard"&&l.jsx("span",{className:"ml-2 text-xs font-black",children:"✓"})
      ]}),
      l.jsxs("button",{type:"button",onClick:()=>setFontSizeScale("large"),className:"hub-child-btn " + (fontSizeScale==="large"?"hub-child-btn-active":""),children:[
        l.jsx("span",{className:"text-base",children:"🔎"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"بڑا فونٹ (Large Font)"}),
          l.jsx("div",{className:"text-[10px] opacity-75 font-semibold",children:"کھلا اور انتہائی واضح فونٹ"})
        ]}),
        fontSizeScale==="large"&&l.jsx("span",{className:"ml-2 text-xs font-black",children:"✓"})
      ]}),
      l.jsxs("button",{type:"button",onClick:()=>setDoubleBorder(!doubleBorder),className:"hub-child-btn " + (doubleBorder?"border-slate-800 bg-slate-100":""),children:[
        l.jsx("span",{className:"text-base",children:"📦"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"Double Line Board Border"}),
          l.jsx("div",{className:"text-[10px] opacity-75 font-semibold",children:doubleBorder?"ڈبل بارڈر آن ہے":"سادہ بارڈر"})
        ]}),
        doubleBorder&&l.jsx("span",{className:"ml-2 text-xs font-black text-blue-700",children:"✓"})
      ]})
    ]})
  ]}),

  activeHubTab==="branding"&&l.jsxs("div",{className:"hub-child-drawer space-y-2.5",children:[
    l.jsxs("div",{className:"flex items-center justify-between border-b border-slate-200 pb-1.5",children:[
      l.jsxs("div",{className:"flex items-center gap-1.5 text-xs font-black text-slate-800",children:[
        l.jsx("span",{children:"🛡️"}),
        l.jsx("span",{children:"ادارہ کی برانڈنگ، مونوگرام اور واٹر مارک (Branding & Logo):"})
      ]}),
      l.jsx("span",{className:"text-[10px] text-slate-500 font-bold",children:"پرچے کے پس منظر پر ادارے کا واٹر مارک اور اوپر مونوگرام لوگو"})
    ]}),
    l.jsxs("div",{className:"flex flex-wrap items-center gap-2",children:[
      l.jsxs("button",{type:"button",onClick:()=>e({...n,header:{...n.header,showWatermark:!0}}),className:"hub-child-btn " + (n.header.showWatermark?"hub-child-btn-active":""),children:[
        l.jsx("span",{className:"text-base",children:"💧"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"Watermark: ON (واٹر مارک دکھائیں)"}),
          l.jsx("div",{className:"text-[10px] opacity-75 font-semibold",children:"پرچے کے پس منظر میں واٹر مارک ظاہر ہوگا"})
        ]}),
        n.header.showWatermark&&l.jsx("span",{className:"ml-2 text-xs font-black",children:"✓"})
      ]}),
      l.jsxs("button",{type:"button",onClick:()=>e({...n,header:{...n.header,showWatermark:!1}}),className:"hub-child-btn " + (!n.header.showWatermark?"hub-child-btn-active":""),children:[
        l.jsx("span",{className:"text-base",children:"🚫"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"Watermark: OFF (واٹر مارک چھپائیں)"}),
          l.jsx("div",{className:"text-[10px] opacity-75 font-semibold",children:"پس منظر سے واٹر مارک ہٹا دیں"})
        ]}),
        !n.header.showWatermark&&l.jsx("span",{className:"ml-2 text-xs font-black",children:"✓"})
      ]}),
      l.jsxs("button",{type:"button",onClick:()=>{var Ce;return(Ce=R.current)==null?void 0:Ce.click();},className:"hub-child-btn bg-amber-50 text-amber-950 border-amber-300 hover:bg-amber-100",children:[
        l.jsx("span",{className:"text-base",children:"📷"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"Upload School Monogram"}),
          l.jsx("div",{className:"text-[10px] text-amber-800 font-semibold",children:"ادارے کا لوگو یا مونوگرام فائل منتخب کریں"})
        ]})
      ]}),
      n.header.customLogoUrl&&l.jsxs("button",{type:"button",onClick:()=>e({...n,header:{...n.header,customLogoUrl:void 0}}),className:"hub-child-btn bg-rose-50 text-rose-800 border-rose-300 hover:bg-rose-100",children:[
        l.jsx("span",{className:"text-base",children:"✕"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"Remove Custom Logo"}),
          l.jsx("div",{className:"text-[10px] text-rose-600 font-semibold",children:"کسٹم مونوگرام ہٹا کر ڈیفالٹ بحال کریں"})
        ]})
      ]})
    ]})
  ]}),

  activeHubTab==="editor"&&l.jsxs("div",{className:"hub-child-drawer space-y-2.5",children:[
    l.jsxs("div",{className:"flex items-center justify-between border-b border-slate-200 pb-1.5",children:[
      l.jsxs("div",{className:"flex items-center gap-1.5 text-xs font-black text-slate-800",children:[
        l.jsx("span",{children:"✏️"}),
        l.jsx("span",{children:"سوالات لائیو ایڈیٹر اور اضافہ (In-Place Question Editor):"})
      ]}),
      l.jsx("span",{className:"text-[10px] text-slate-500 font-bold",children:"پرچے پر کسی بھی سوال کی تحریر بدلیں یا نئے سوالات شامل کریں"})
    ]}),
    l.jsxs("div",{className:"flex flex-wrap items-center gap-2",children:[
      l.jsxs("button",{type:"button",onClick:()=>f(!u),className:"hub-child-btn " + (u?"hub-child-btn-active bg-amber-600 border-amber-600":""),children:[
        l.jsx("span",{className:"text-base",children:u?"✓":"✏️"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:u?"Done Editing (ایڈیٹنگ ختم کریں)":"Edit Text Directly (لائیو ایڈٹ موڈ)"}),
          l.jsx("div",{className:"text-[10px] opacity-75 font-semibold",children:u?"تبدیلیاں محفوظ ہیں":"پرچے پر براہِ راست سوالات تبدیل کریں"})
        ]}),
        u&&l.jsx("span",{className:"ml-2 text-xs font-black",children:"✓"})
      ]}),
      l.jsxs("button",{type:"button",onClick:ce,className:"hub-child-btn bg-blue-50 text-blue-900 border-blue-300 hover:bg-blue-100",children:[
        l.jsx("span",{className:"text-base",children:"➕"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"+ Add New MCQ"}),
          l.jsx("div",{className:"text-[10px] text-blue-700 font-semibold",children:"نیا کثیر الانتخابی سوال شامل کریں"})
        ]})
      ]}),
      l.jsxs("button",{type:"button",onClick:()=>{G.part1_shortQuestions[0]&&me(G.part1_shortQuestions[0].id)},className:"hub-child-btn bg-indigo-50 text-indigo-900 border-indigo-300 hover:bg-indigo-100",children:[
        l.jsx("span",{className:"text-base",children:"➕"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"+ Add Short Question"}),
          l.jsx("div",{className:"text-[10px] text-indigo-700 font-semibold",children:"حصہ اول میں نیا مختصر سوال شامل کریں"})
        ]})
      ]}),
      l.jsxs("button",{type:"button",onClick:ue,className:"hub-child-btn bg-emerald-50 text-emerald-900 border-emerald-300 hover:bg-emerald-100",children:[
        l.jsx("span",{className:"text-base",children:"➕"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"+ Add Long Question"}),
          l.jsx("div",{className:"text-[10px] text-emerald-700 font-semibold",children:"حصہ دوم میں نیا تفصیلی سوال شامل کریں"})
        ]})
      ]})
    ]})
  ]}),

  activeHubTab==="downloads"&&l.jsxs("div",{className:"hub-child-drawer space-y-2.5",children:[
    l.jsxs("div",{className:"flex items-center justify-between border-b border-slate-200 pb-1.5",children:[
      l.jsxs("div",{className:"flex items-center gap-1.5 text-xs font-black text-slate-800",children:[
        l.jsx("span",{children:"📥"}),
        l.jsx("span",{children:"فائلز ڈاؤن لوڈ اور ایکسپورٹ (Download & Export Files):"})
      ]}),
      l.jsx("span",{className:"text-[10px] text-slate-500 font-bold",children:"پی ڈی ایف یا ورڈ فارمیٹ میں مکمل پرچہ محفوظ کریں"})
    ]}),
    l.jsxs("div",{className:"flex flex-wrap items-center gap-2",children:[
      l.jsxs("button",{type:"button",onClick:ne,disabled:C,className:"hub-child-btn hub-child-btn-active",children:[
        l.jsx(SAFE_ad,{className:"w-4 h-4 text-white"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:C?"Preparing PDF...":"Download High-Res PDF (.pdf)"}),
          l.jsx("div",{className:"text-[10px] opacity-75 font-semibold",children:"پرنٹ اور شیئر کے لیے معیاری پی ڈی ایف"})
        ]})
      ]}),
      l.jsxs("button",{type:"button",onClick:()=>z0(n,o),className:"hub-child-btn border-blue-400 bg-blue-50 text-blue-900 hover:bg-blue-100",children:[
        l.jsx(Xu,{className:"w-4 h-4 text-blue-700"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"Download MS Word (.doc)"}),
          l.jsx("div",{className:"text-[10px] text-blue-700 font-semibold",children:"مائیکروسافٹ ورڈ میں قابلِ تدوین فائل"})
        ]})
      ]}),
      a&&l.jsxs("button",{type:"button",onClick:a,className:"hub-child-btn border-emerald-400 bg-emerald-50 text-emerald-900 hover:bg-emerald-100",children:[
        l.jsx(FC,{className:"w-4 h-4 text-emerald-700"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"Download Solved Key"}),
          l.jsx("div",{className:"text-[10px] text-emerald-700 font-semibold",children:"جوابی کلید اور حل شدہ پرچہ"})
        ]})
      ]}),
      r&&l.jsxs("button",{type:"button",onClick:r,className:"hub-child-btn border-indigo-400 bg-indigo-50 text-indigo-900 hover:bg-indigo-100",children:[
        l.jsx(Ru,{className:"w-4 h-4 text-indigo-700"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"Download Bubble Sheet PDF"}),
          l.jsx("div",{className:"text-[10px] text-indigo-700 font-semibold",children:"امتحانی ببل شیٹ فائل"})
        ]})
      ]})
    ]})
  ]}),

  activeHubTab==="share"&&l.jsxs("div",{className:"hub-child-drawer space-y-2.5",children:[
    l.jsxs("div",{className:"flex items-center justify-between border-b border-slate-200 pb-1.5",children:[
      l.jsxs("div",{className:"flex items-center gap-1.5 text-xs font-black text-slate-800",children:[
        l.jsx("span",{children:"📢"}),
        l.jsx("span",{children:"پرچہ شیئرنگ اور تقسیم (Share & Distribute Paper):"})
      ]}),
      l.jsx("span",{className:"text-[10px] text-slate-500 font-bold",children:"اساتذہ یا طلبہ کو واٹس ایپ یا لنک کے ذریعے فوری بھیجیں"})
    ]}),
    l.jsxs("div",{className:"flex flex-wrap items-center gap-2",children:[
      l.jsxs("button",{type:"button",onClick:P,className:"hub-child-btn hub-child-btn-emerald",children:[
        l.jsx(K0,{className:"w-4 h-4 text-white"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"Share via WhatsApp"}),
          l.jsx("div",{className:"text-[10px] opacity-75 font-semibold",children:"واٹس ایپ پر مکمل تفصیل اور لنک بھیجیں"})
        ]})
      ]}),
      l.jsxs("button",{type:"button",onClick:te,className:"hub-child-btn border-purple-400 bg-purple-50 text-purple-900 hover:bg-purple-100",children:[
        l.jsx($2,{className:"w-4 h-4 text-purple-700"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"Copy Paper Link"}),
          l.jsx("div",{className:"text-[10px] text-purple-700 font-semibold",children:"براہِ راست آن لائن لنک کاپی کریں"})
        ]})
      ]}),
      l.jsxs("button",{type:"button",onClick:te,className:"hub-child-btn border-slate-300 hover:bg-slate-50",children:[
        l.jsx("span",{className:"text-base",children:"📱"}),
        l.jsxs("div",{children:[
          l.jsx("div",{className:"font-black",children:"Device Share Dialog"}),
          l.jsx("div",{className:"text-[10px] text-slate-600 font-semibold",children:"موبائل کے اپنے شیئر مینو سے شیئر کریں"})
        ]})
      ]})
    ]})
  ]})
]}),
C&&l.jsxs("div",{className:"no-print bg-gradient-to-r from-indigo-600 to-blue-600 text-white px-4 py-2 text-xs font-bold flex items-center justify-center gap-2 animate-pulse shadow-md",children:[l.jsx(Sc,{className:"w-4 h-4 animate-spin text-white"}),l.jsx("span",{children:v||"Generating High-Resolution PDF... Please wait a few seconds"})]}),
B&&l.jsxs("div",{className:"no-print bg-blue-50 border-b border-blue-200 px-4 py-2.5 text-xs text-blue-950 flex items-center justify-between",children:[l.jsxs("div",{className:"flex items-center gap-2",children:[l.jsx(G3,{className:"w-4 h-4 text-blue-600 shrink-0"}),l.jsxs("div",{children:[l.jsx("span",{className:"font-bold",children:"PDF Direct Download Note: "}),"If direct download was blocked by browser permissions, select ",l.jsx("strong",{children:'"Save as PDF"'})," in the print dialog."]})]}),l.jsx("button",{type:"button",onClick:()=>m(!1),className:"text-blue-800 font-bold ml-2 text-sm hover:text-blue-900 cursor-pointer",children:"✕"})]}),l.jsxs("div",{id:"