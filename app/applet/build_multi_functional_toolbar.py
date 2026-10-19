import subprocess
import re

print("Starting Multi-Functional Toolbar Construction...")

# 1. Update index.html with styles for Multi-Functional Hub & Child Buttons
with open('index.html', 'r', encoding='utf-8') as f:
    html_text = f.read()

hub_css = '''
      /* Multi-Functional Master Hub Buttons */
      .hub-btn {
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.55rem 0.85rem;
        border-radius: 0.875rem;
        font-size: 0.75rem;
        font-weight: 800;
        cursor: pointer;
        transition: all 0.15s ease-in-out;
        border: 2px solid #cbd5e1;
        background: #ffffff;
        color: #334155;
        box-shadow: 0 1px 3px rgba(0,0,0,0.06);
        white-space: nowrap;
        user-select: none;
      }
      .hub-btn:hover {
        background: #f8fafc;
        border-color: #94a3b8;
        transform: translateY(-1px);
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
      }
      .hub-btn-active {
        background: linear-gradient(135deg, #1e293b, #0f172a) !important;
        border-color: #3b82f6 !important;
        color: #ffffff !important;
        box-shadow: 0 4px 12px -2px rgba(15, 23, 42, 0.4), inset 0 1px 0 rgba(255,255,255,0.2) !important;
        transform: translateY(-1px);
      }
      .hub-badge {
        font-size: 0.65rem;
        padding: 0.15rem 0.45rem;
        border-radius: 0.5rem;
        font-weight: 900;
        letter-spacing: 0.02em;
      }
      .hub-badge-active {
        background: #3b82f6;
        color: #ffffff;
      }
      .hub-badge-inactive {
        background: #f1f5f9;
        color: #64748b;
      }

      /* Expanded Child Action Drawer */
      .hub-child-drawer {
        background: #f8fafc;
        border: 2px solid #cbd5e1;
        border-radius: 1.125rem;
        padding: 0.875rem 1rem;
        box-shadow: 0 8px 24px -4px rgba(15, 23, 42, 0.07), inset 0 2px 4px rgba(0,0,0,0.02);
        animation: hubSlideDown 0.18s cubic-bezier(0.16, 1, 0.3, 1);
      }
      @keyframes hubSlideDown {
        from { opacity: 0; transform: translateY(-4px); }
        to { opacity: 1; transform: translateY(0); }
      }
      .hub-child-btn {
        display: inline-flex;
        align-items: center;
        gap: 0.6rem;
        padding: 0.6rem 1rem;
        border-radius: 0.85rem;
        font-size: 0.78rem;
        font-weight: 800;
        cursor: pointer;
        transition: all 0.15s ease-in-out;
        border: 2px solid #cbd5e1;
        background: #ffffff;
        color: #1e293b;
        box-shadow: 0 2px 4px rgba(0,0,0,0.04);
        user-select: none;
        text-align: left;
      }
      .hub-child-btn:hover {
        border-color: #64748b;
        background: #f1f5f9;
        transform: translateY(-1px);
      }
      .hub-child-btn-active {
        background: linear-gradient(135deg, #2563eb, #1d4ed8) !important;
        border-color: #1d4ed8 !important;
        color: #ffffff !important;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.35) !important;
      }
      .hub-child-btn-emerald {
        background: linear-gradient(135deg, #059669, #047857) !important;
        border-color: #047857 !important;
        color: #ffffff !important;
        box-shadow: 0 4px 12px rgba(5, 150, 105, 0.35) !important;
      }
'''

if '.hub-btn' not in html_text:
    pos_style_end = html_text.find('</style>')
    if pos_style_end != -1:
        html_text = html_text[:pos_style_end] + hub_css + html_text[pos_style_end:]
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(html_text)
        print("Updated index.html with .hub-btn and child drawer styles!")

print("Step 1 done.")
