import subprocess, tempfile

def process_file(filepath):
    print(f"Processing {filepath}...")
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    orig_len = len(text)

    # -------------------------------------------------------------------------
    # PART 1 (Image ending in 15): Remove redundant outer duplicate buttons bar
    # (Removes "Back to Portal", duplicate "Download PDF", "Download MS Word",
    # "Answer Key", and "Print & Preview", leaving the clean single PaperView toolbar)
    # -------------------------------------------------------------------------
    dup_bar_start = 'l.jsxs("div",{className:"flex flex-wrap items-center justify-between gap-2 no-print max-w-5xl mx-auto",'
    pos_dup_start = text.find(dup_bar_start)
    if pos_dup_start != -1:
        # Find where it ends right before l.jsx(WK,
        target_wk = ',l.jsx(WK,{paper:v,onUpdatePaper:Ye,printSection:"all"'
        pos_wk = text.find(target_wk, pos_dup_start)
        if pos_wk != -1:
            # We remove from pos_dup_start up to pos_wk + 1 (the comma)
            text = text[:pos_dup_start] + text[pos_wk + 1:]
            print("  [✓] Part 1: Removed duplicate buttons bar and duplicate 'Back to Portal'")
        else:
            print("  [!] Part 1: target_wk not found after pos_dup_start")
    else:
        print("  [!] Part 1: dup_bar_start not found")

    # -------------------------------------------------------------------------
    # PART 2 (Image ending in 46): Remove "Examination System Modules & Tools Hub"
    # (Removes the redundant grid of 9/10 cards because all modules are already
    # in the left sidebar menu bar on desktop)
    # -------------------------------------------------------------------------
    hub_start = 'l.jsxs("div",{className:"card-3d p-5 space-y-3",children:[l.jsx("div",{className:"flex items-center justify-between border-b border-slate-200 pb-2.5",children:l.jsxs("div",{children:[l.jsxs("h2",{className:"text-sm font-extrabold uppercase tracking-wider text-slate-900 flex items-center gap-2",children:[l.jsx(SAFE_Ta,{className:"w-4 h-4 text-blue-600"}),l.jsx("span",{children:"Examination System Modules & Tools Hub"'
    pos_hub_start = text.find(hub_start)
    if pos_hub_start != -1:
        # Find the next section: Recent Generated Question Papers card
        recent_card_marker = 'l.jsxs("div",{className:"card-3d p-5",children:[l.jsxs("div",{className:"flex items-center justify-between mb-4 border-b border-slate-200 pb-3",children:[l.jsxs("div",{children:[l.jsx("h3",{className:"font-black text-sm text-slate-950",children:"Recent Generated Question Papers"'
        pos_recent = text.find(recent_card_marker, pos_hub_start)
        if pos_recent != -1:
            # The hub ends right before pos_recent
            # Remove from pos_hub_start up to pos_recent
            text = text[:pos_hub_start] + text[pos_recent:]
            print("  [✓] Part 2: Removed 'Examination System Modules & Tools Hub' section")
        else:
            print("  [!] Part 2: recent_card_marker not found after pos_hub_start")
    else:
        print("  [!] Part 2: hub_start not found")

    # Validate syntax with node --check
    with tempfile.NamedTemporaryFile('w', suffix='.mjs', delete=False) as tf:
        tf.write(text)
        temp_name = tf.name

    res = subprocess.run(['node', '--check', temp_name], capture_output=True, text=True)
    if res.returncode != 0:
        print(f"Error checking {filepath}:\n", res.stderr[:500])
        return False

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)

    print(f"  [✓] Validated syntax and saved {filepath} (len: {orig_len} -> {len(text)})\n")
    return True

files = [
    '/app/applet/assets/index-DAioIUjd.js',
    '/app/applet/dist/assets/index-DAioIUjd.js',
    '/app/applet/assets/index-DAiG7xr8.js',
    '/app/applet/dist/assets/index-DAiG7xr8.js',
    '/app/applet/dist/assets/index-DPUomzbq.js',
    '/app/applet/assets/index-DPUomzbq.js',
    '/app/applet/dist/assets/index-OsVJ5uB7.js'
]

for fp in files:
    try:
        process_file(fp)
    except Exception as e:
        print(f"Error on {fp}: {e}")

