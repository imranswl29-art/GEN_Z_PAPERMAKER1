with open("assets/index-DAioIUjd.js", "r", encoding="utf-8") as f:
    bundle = f.read()

# 1. Objective Paper Monogram Fix
s1_old = 'l.jsx("div",{className:"school-monogram-container w-14 h-14 sm:w-20 sm:h-20 border-2 border-slate-900 rounded-full p-1 bg-white flex items-center justify-center overflow-hidden shrink-0 shadow-2xs",children:T.customLogoUrl?l.jsx("img",{src:T.customLogoUrl,alt:"School Monogram",className:"w-full h-full object-contain"}):l.jsxs("div",{className:"w-full h-full rounded-full bg-slate-900 text-white flex flex-col items-center justify-center p-1 text-center",children:[l.jsx(SAFE_id,{className:"w-7 h-7 text-amber-400"}),l.jsx("span",{className:"text-[7px] font-black uppercase tracking-tighter",children:"PTBB SEAL"})]})})'

s1_new = 'l.jsx("div",{className:"school-monogram-container w-14 h-14 sm:w-20 sm:h-20 border-2 border-black rounded-full p-1 bg-white flex items-center justify-center overflow-hidden shrink-0 shadow-2xs",children:T.customLogoUrl?l.jsx("img",{src:T.customLogoUrl,alt:"School Monogram",className:"w-full h-full object-contain"}):l.jsxs("div",{className:"paper-monogram-seal w-full h-full rounded-full border-2 border-black bg-white text-black flex flex-col items-center justify-center p-0.5 text-center",children:[l.jsx(SAFE_id,{className:"w-7 h-7 text-black stroke-black fill-black"}),l.jsx("span",{className:"text-[7px] font-black uppercase tracking-tighter text-black",children:"PTBB SEAL"})]})})'

assert bundle.count(s1_old) == 1, f"Expected 1 match for s1_old, found {bundle.count(s1_old)}"
bundle = bundle.replace(s1_old, s1_new, 1)

# 2. Subjective Paper Monogram Fix
s2_old = 'l.jsx("div",{className:"school-monogram-container w-14 h-14 sm:w-18 sm:h-18 border-2 border-slate-900 rounded-full p-1 bg-white flex items-center justify-center overflow-hidden shrink-0 shadow-2xs",children:T.customLogoUrl?l.jsx("img",{src:T.customLogoUrl,alt:"School Monogram",className:"w-full h-full object-contain"}):l.jsxs("div",{className:"w-full h-full rounded-full bg-slate-900 text-white flex flex-col items-center justify-center p-1 text-center",children:[l.jsx(SAFE_id,{className:"w-6 h-6 text-amber-400"}),l.jsx("span",{className:"text-[6.5px] font-black uppercase tracking-tighter",children:"PTBB SEAL"})]})})'

s2_new = 'l.jsx("div",{className:"school-monogram-container w-14 h-14 sm:w-18 sm:h-18 border-2 border-black rounded-full p-1 bg-white flex items-center justify-center overflow-hidden shrink-0 shadow-2xs",children:T.customLogoUrl?l.jsx("img",{src:T.customLogoUrl,alt:"School Monogram",className:"w-full h-full object-contain"}):l.jsxs("div",{className:"paper-monogram-seal w-full h-full rounded-full border-2 border-black bg-white text-black flex flex-col items-center justify-center p-0.5 text-center",children:[l.jsx(SAFE_id,{className:"w-6 h-6 text-black stroke-black fill-black"}),l.jsx("span",{className:"text-[6.5px] font-black uppercase tracking-tighter text-black",children:"PTBB SEAL"})]})})'

assert bundle.count(s2_old) == 1, f"Expected 1 match for s2_old, found {bundle.count(s2_old)}"
bundle = bundle.replace(s2_old, s2_new, 1)

# 3. Paper Set Boxes (both Objective and Subjective)
s3_old = 'l.jsxs("div",{className:"border border-slate-900 bg-slate-950 text-white px-2 py-0.5 text-center rounded-xs shadow-2xs",children:[l.jsx("span",{className:"block text-[7px] font-bold uppercase tracking-wider text-amber-300",children:"SET"}),l.jsx("span",{className:"text-xs sm:text-sm font-black text-white",children:T.paperSet||"A"})]})'

s3_new = 'l.jsxs("div",{className:"paper-set-box paper-set-badge border-2 border-black bg-white text-black px-2 py-0.5 text-center rounded-xs shadow-2xs",children:[l.jsx("span",{className:"block text-[7px] font-black uppercase tracking-wider text-black",children:"SET"}),l.jsx("span",{className:"text-xs sm:text-sm font-black text-black leading-none",children:T.paperSet||"A"})]})'

assert bundle.count(s3_old) == 2, f"Expected 2 matches for s3_old, found {bundle.count(s3_old)}"
bundle = bundle.replace(s3_old, s3_new)

# 4. Rw Institutional SVG Seal Colors (Crisp high-contrast monochromatic outlines)
old_rw = 'l.jsxs("svg",{viewBox:"0 0 100 100",className:"w-full h-full drop-shadow-xs",fill:"none",xmlns:"http://www.w3.org/2000/svg",children:[l.jsx("circle",{cx:"50",cy:"50",r:"47",stroke:"#1E3A8A",strokeWidth:"2.5",fill:"#FFFFFF"}),l.jsx("circle",{cx:"50",cy:"50",r:"43",stroke:"#D97706",strokeWidth:"1.2",strokeDasharray:"3 1.5"}),l.jsx("circle",{cx:"50",cy:"50",r:"38",fill:"#1E40AF"}),l.jsx("circle",{cx:"50",cy:"50",r:"37",stroke:"#F59E0B",strokeWidth:"1"}),l.jsx("path",{d:"M50 17 L51.2 20.5 L54.8 20.5 L51.9 22.6 L53 26 L50 24 L47 26 L48.1 22.6 L45.2 20.5 L48.8 20.5 Z",fill:"#FCD34D"}),l.jsx("path",{d:"M30 25 L30.9 27.5 L33.5 27.5 L31.4 29 L32.2 31.5 L30 30 L27.8 31.5 L28.6 29 L26.5 27.5 L29.1 27.5 Z",fill:"#FCD34D"}),l.jsx("path",{d:"M70 25 L70.9 27.5 L73.5 27.5 L71.4 29 L72.2 31.5 L70 30 L67.8 31.5 L68.6 29 L66.5 27.5 L69.1 27.5 Z",fill:"#FCD34D"})'

new_rw = 'l.jsxs("svg",{viewBox:"0 0 100 100",className:"w-full h-full drop-shadow-xs",fill:"none",xmlns:"http://www.w3.org/2000/svg",children:[l.jsx("circle",{cx:"50",cy:"50",r:"47",stroke:"#000000",strokeWidth:"2.5",fill:"#FFFFFF"}),l.jsx("circle",{cx:"50",cy:"50",r:"43",stroke:"#000000",strokeWidth:"1.2",strokeDasharray:"3 1.5"}),l.jsx("circle",{cx:"50",cy:"50",r:"38",fill:"#0f172a"}),l.jsx("circle",{cx:"50",cy:"50",r:"37",stroke:"#000000",strokeWidth:"1"}),l.jsx("path",{d:"M50 17 L51.2 20.5 L54.8 20.5 L51.9 22.6 L53 26 L50 24 L47 26 L48.1 22.6 L45.2 20.5 L48.8 20.5 Z",fill:"#000000"}),l.jsx("path",{d:"M30 25 L30.9 27.5 L33.5 27.5 L31.4 29 L32.2 31.5 L30 30 L27.8 31.5 L28.6 29 L26.5 27.5 L29.1 27.5 Z",fill:"#000000"}),l.jsx("path",{d:"M70 25 L70.9 27.5 L73.5 27.5 L71.4 29 L72.2 31.5 L70 30 L67.8 31.5 L68.6 29 L66.5 27.5 L69.1 27.5 Z",fill:"#000000"})'

if old_rw in bundle:
    bundle = bundle.replace(old_rw, new_rw, 1)
    print("Rw institutional SVG successfully updated to solid dark black!")
else:
    print("old_rw not matched or already updated")

with open("assets/index-DAioIUjd.js", "w", encoding="utf-8") as f:
    f.write(bundle)

print("SUCCESS: assets/index-DAioIUjd.js updated cleanly!")
