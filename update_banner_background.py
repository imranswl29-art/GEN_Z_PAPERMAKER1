import subprocess, tempfile

def update_banner():
    filepath = 'assets/index-DAioIUjd.js'
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    pos_m8 = text.find('const m8=')
    if pos_m8 == -1:
        print("const m8= not found")
        return False

    banner_start = text.find('l.jsxs("div",{className:"rounded-2xl', pos_m8)
    banner_end_marker = 'l.jsx("path",{d:"M6 12.5V16a6 3 0 0 0 12 0v-3.5"})]})})]}),'
    pos_end = text.find(banner_end_marker, banner_start)

    if banner_start == -1 or pos_end == -1:
        print("Markers not found:", banner_start, pos_end)
        return False

    end_index = pos_end + len(banner_end_marker)
    original_banner = text[banner_start:end_index]

    # Extract the exact foreground untouched
    fg_marker_start = 'l.jsxs("div",{className:"relative z-10 max-w-3xl space-y-3",'
    fg_marker_end = 'l.jsx(NewsBulletinTicker,{})]})'
    pos_fg_start = original_banner.find(fg_marker_start)
    pos_fg_end = original_banner.find(fg_marker_end)
    if pos_fg_start == -1 or pos_fg_end == -1:
        print("Foreground markers not found")
        return False

    foreground_code = original_banner[pos_fg_start:pos_fg_end + len(fg_marker_end)]

    new_banner = (
        'l.jsxs("div",{'
        'className:"rounded-2xl p-6 sm:p-8 text-white shadow-2xl relative overflow-hidden border border-blue-500/25",'
        'style:{background:"linear-gradient(135deg, #0b1a30 0%, #102140 45%, #142850 100%)",boxShadow:"0 16px 36px -6px rgba(11, 26, 48, 0.75), 0 4px 12px -2px rgba(0, 0, 0, 0.3)"},'
        'children:['
        'l.jsx("div",{className:"absolute -top-24 -right-24 w-96 h-96 rounded-full bg-blue-400/15 blur-3xl pointer-events-none select-none"}),'
        'l.jsx("div",{className:"absolute -bottom-24 right-1/4 w-80 h-80 rounded-full bg-indigo-500/15 blur-3xl pointer-events-none select-none"}),'
        'l.jsx("div",{className:"absolute top-1/2 -left-12 w-64 h-64 rounded-full bg-cyan-400/10 blur-2xl pointer-events-none select-none"}),'
        'l.jsx("div",{className:"absolute inset-0 pointer-events-none select-none overflow-hidden",children:'
        'l.jsxs("svg",{className:"w-full h-full",viewBox:"0 0 1000 320",fill:"none",xmlns:"http://www.w3.org/2000/svg",preserveAspectRatio:"xMaxYMid meet",children:['
        'l.jsxs("defs",{children:['
        'l.jsxs("linearGradient",{id:"heroSheetGrad1",x1:"0",y1:"0",x2:"1",y2:"1",children:['
        'l.jsx("stop",{offset:"0%",stopColor:"#ffffff",stopOpacity:"0.18"}),'
        'l.jsx("stop",{offset:"100%",stopColor:"#60a5fa",stopOpacity:"0.05"})'
        ']}),'
        'l.jsxs("linearGradient",{id:"heroSheetGrad2",x1:"0",y1:"0",x2:"1",y2:"1",children:['
        'l.jsx("stop",{offset:"0%",stopColor:"#93c5fd",stopOpacity:"0.22"}),'
        'l.jsx("stop",{offset:"100%",stopColor:"#1e3a8a",stopOpacity:"0.1"})'
        ']}),'
        'l.jsxs("linearGradient",{id:"heroCurveGrad1",x1:"0",y1:"0",x2:"1",y2:"0",children:['
        'l.jsx("stop",{offset:"0%",stopColor:"#38bdf8",stopOpacity:"0"}),'
        'l.jsx("stop",{offset:"50%",stopColor:"#60a5fa",stopOpacity:"0.35"}),'
        'l.jsx("stop",{offset:"100%",stopColor:"#818cf8",stopOpacity:"0"})'
        ']}),'
        'l.jsxs("linearGradient",{id:"heroCurveGrad2",x1:"0",y1:"0",x2:"1",y2:"0",children:['
        'l.jsx("stop",{offset:"0%",stopColor:"#818cf8",stopOpacity:"0"}),'
        'l.jsx("stop",{offset:"60%",stopColor:"#38bdf8",stopOpacity:"0.25"}),'
        'l.jsx("stop",{offset:"100%",stopColor:"#a78bfa",stopOpacity:"0"})'
        ']}),'
        'l.jsxs("linearGradient",{id:"heroPenGrad",x1:"0",y1:"0",x2:"1",y2:"1",children:['
        'l.jsx("stop",{offset:"0%",stopColor:"#93c5fd",stopOpacity:"0.6"}),'
        'l.jsx("stop",{offset:"100%",stopColor:"#2563eb",stopOpacity:"0.2"})'
        ']})'
        ']}),'
        'l.jsx("path",{d:"M 450,290 C 600,160 780,310 1020,110",stroke:"url(#heroCurveGrad1)",strokeWidth:"2",strokeDasharray:"6 4"}),'
        'l.jsx("path",{d:"M 400,310 C 650,220 820,340 1040,160",stroke:"url(#heroCurveGrad2)",strokeWidth:"1.5"}),'
        'l.jsx("path",{d:"M 520,330 C 720,260 860,190 1020,50",stroke:"url(#heroCurveGrad1)",strokeWidth:"1",strokeDasharray:"3 3"}),'
        'l.jsxs("g",{transform:"translate(810, 45) rotate(14)",children:['
        'l.jsx("rect",{x:"-40",y:"-55",width:"80",height:"110",rx:"6",fill:"url(#heroSheetGrad1)",stroke:"#93c5fd",strokeOpacity:"0.35",strokeWidth:"1.2"}),'
        'l.jsx("rect",{x:"-30",y:"-45",width:"40",height:"5",rx:"2.5",fill:"#93c5fd",fillOpacity:"0.5"}),'
        'l.jsx("circle",{cx:"28",cy:"-42",r:"3.5",fill:"#38bdf8",fillOpacity:"0.6"}),'
        'l.jsx("rect",{x:"-30",y:"-32",width:"60",height:"3",rx:"1.5",fill:"#ffffff",fillOpacity:"0.25"}),'
        'l.jsx("rect",{x:"-30",y:"-23",width:"52",height:"2.5",rx:"1.2",fill:"#ffffff",fillOpacity:"0.18"}),'
        'l.jsx("rect",{x:"-30",y:"-12",width:"58",height:"3",rx:"1.5",fill:"#ffffff",fillOpacity:"0.25"}),'
        'l.jsx("rect",{x:"-30",y:"-3",width:"45",height:"2.5",rx:"1.2",fill:"#ffffff",fillOpacity:"0.18"}),'
        'l.jsx("circle",{cx:"-25",cy:"12",r:"2.8",stroke:"#38bdf8",strokeWidth:"1",fill:"none",strokeOpacity:"0.5"}),'
        'l.jsx("circle",{cx:"-15",cy:"12",r:"2.8",fill:"#38bdf8",fillOpacity:"0.6"}),'
        'l.jsx("circle",{cx:"-5",cy:"12",r:"2.8",stroke:"#38bdf8",strokeWidth:"1",fill:"none",strokeOpacity:"0.5"}),'
        'l.jsx("circle",{cx:"5",cy:"12",r:"2.8",stroke:"#38bdf8",strokeWidth:"1",fill:"none",strokeOpacity:"0.5"}),'
        'l.jsx("rect",{x:"-30",y:"24",width:"60",height:"3",rx:"1.5",fill:"#ffffff",fillOpacity:"0.25"}),'
        'l.jsx("rect",{x:"-30",y:"33",width:"40",height:"2.5",rx:"1.2",fill:"#ffffff",fillOpacity:"0.18"}),'
        'l.jsx("circle",{cx:"22",cy:"38",r:"9",stroke:"#60a5fa",strokeWidth:"1.2",strokeOpacity:"0.4",strokeDasharray:"2 2",fill:"none"})'
        ']}),'
        'l.jsxs("g",{transform:"translate(680, 110) rotate(-12) scale(0.85)",children:['
        'l.jsx("rect",{x:"-40",y:"-55",width:"80",height:"110",rx:"6",fill:"url(#heroSheetGrad2)",stroke:"#818cf8",strokeOpacity:"0.3",strokeWidth:"1"}),'
        'l.jsx("rect",{x:"-30",y:"-45",width:"35",height:"4",rx:"2",fill:"#818cf8",fillOpacity:"0.4"}),'
        'l.jsx("rect",{x:"-30",y:"-33",width:"55",height:"2.5",rx:"1.2",fill:"#ffffff",fillOpacity:"0.2"}),'
        'l.jsx("rect",{x:"-30",y:"-24",width:"48",height:"2.5",rx:"1.2",fill:"#ffffff",fillOpacity:"0.15"}),'
        'l.jsx("rect",{x:"-30",y:"-12",width:"58",height:"2.5",rx:"1.2",fill:"#ffffff",fillOpacity:"0.2"}),'
        'l.jsx("rect",{x:"-30",y:"-3",width:"42",height:"2.5",rx:"1.2",fill:"#ffffff",fillOpacity:"0.15"}),'
        'l.jsx("rect",{x:"-30",y:"9",width:"52",height:"2.5",rx:"1.2",fill:"#ffffff",fillOpacity:"0.2"}),'
        'l.jsx("rect",{x:"-30",y:"18",width:"36",height:"2.5",rx:"1.2",fill:"#ffffff",fillOpacity:"0.15"})'
        ']}),'
        'l.jsxs("g",{transform:"translate(930, 145) rotate(-8) scale(0.9)",children:['
        'l.jsx("path",{d:"M 0,-22 L 40,0 L 0,22 L -40,0 Z",fill:"#1e3a8a",fillOpacity:"0.45",stroke:"#93c5fd",strokeOpacity:"0.5",strokeWidth:"1.5"}),'
        'l.jsx("path",{d:"M 0,-22 L 40,0 L 0,3 L -40,0 Z",fill:"#60a5fa",fillOpacity:"0.25"}),'
        'l.jsx("path",{d:"M -22,7 C -22,20 22,20 22,7 L 22,2 C 22,14 -22,14 -22,2 Z",fill:"#0f2b5c",fillOpacity:"0.6",stroke:"#60a5fa",strokeOpacity:"0.3",strokeWidth:"1"}),'
        'l.jsx("circle",{cx:"0",cy:"0",r:"3",fill:"#38bdf8",fillOpacity:"0.8"}),'
        'l.jsx("path",{d:"M 0,0 C 12,4 24,14 26,26 L 27,38",stroke:"#38bdf8",strokeWidth:"1.5",strokeOpacity:"0.7"}),'
        'l.jsx("polygon",{points:"24,38 30,38 29,48 25,48",fill:"#38bdf8",fillOpacity:"0.75"})'
        ']}),'
        'l.jsxs("g",{transform:"translate(745, 230) rotate(-35) scale(0.8)",children:['
        'l.jsx("rect",{x:"-5",y:"-35",width:"10",height:"60",rx:"3",fill:"url(#heroPenGrad)",stroke:"#93c5fd",strokeOpacity:"0.4",strokeWidth:"1"}),'
        'l.jsx("polygon",{points:"-5,-35 5,-35 0,-50",fill:"#60a5fa",fillOpacity:"0.7"}),'
        'l.jsx("circle",{cx:"0",cy:"-50",r:"1.2",fill:"#ffffff"}),'
        'l.jsx("rect",{x:"-3",y:"15",width:"6",height:"7",rx:"1",fill:"#38bdf8",fillOpacity:"0.5"})'
        ']}),'
        'l.jsxs("g",{opacity:"0.25",fill:"#93c5fd",children:['
        'l.jsx("text",{x:"610",y:"60",fontFamily:"sans-serif",fontWeight:"900",fontSize:"22",children:"∑"}),'
        'l.jsx("text",{x:"760",y:"40",fontFamily:"sans-serif",fontWeight:"900",fontSize:"18",children:"Δ"}),'
        'l.jsx("text",{x:"890",y:"270",fontFamily:"sans-serif",fontWeight:"900",fontSize:"20",children:"π"}),'
        'l.jsx("circle",{cx:"640",cy:"240",r:"14",stroke:"#38bdf8",strokeWidth:"1.5",opacity:"0.4"}),'
        'l.jsx("path",{d:"M 634,240 L 638,244 L 646,235",stroke:"#38bdf8",strokeWidth:"2",strokeLinecap:"round",strokeLinejoin:"round",opacity:"0.6"})'
        ']})'
        ']})}),'
        + foreground_code +
        ']}),'
    )

    new_text = text[:banner_start] + new_banner + text[end_index:]

    # Validate with node --check
    with tempfile.NamedTemporaryFile('w', suffix='.mjs', delete=False) as tf:
        tf.write(new_text)
        temp_name = tf.name

    res = subprocess.run(['node', '--check', temp_name], capture_output=True, text=True)
    if res.returncode != 0:
        print("Syntax check failed:\n", res.stderr[:500])
        return False

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_text)

    print(f"Successfully updated banner in {filepath}!")
    return True

if __name__ == '__main__':
    update_banner()
