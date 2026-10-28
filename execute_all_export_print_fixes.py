#!/usr/bin/env python3
import sys

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add printable area IDs and anti-white-text styles in print
old_css_target = """        #printable-content,
        #exam-paper-container,
        #exam-paper-objective-sheet,
        #exam-paper-subjective-sheet,
        #datesheet-print-container,
        #resultcard-print-container,
        #mastersheet-print-container,
        #answer-key-print-content,
        #bubble-sheet-print-container,
        #notes-printable-container,"""

new_css_replacement = """        #printable-content,
        #exam-paper-container,
        #exam-paper-objective-sheet,
        #exam-paper-subjective-sheet,
        #datesheet-print-container,
        #resultcard-print-container,
        #mastersheet-print-container,
        #answer-key-print-content,
        #bubble-sheet-print-container,
        #bubble-sheet-printable-area,
        #notes-printable-container,"""

if old_css_target in html:
    html = html.replace(old_css_target, new_css_replacement, 1)
    print("Updated index.html printable IDs.")
else:
    print("Warning: old_css_target not found in index.html")

# Add enhanced print and OMR layout rules right before </style>
print_rules = """
      /* Enhanced Layout & Contrast Rules for Print & Exports: Zero Overlap, Perfect Visibility */
      @media print {
        /* Prevent white-on-white text in Answer Key, Result Card, Marksheet & Bubble Sheet */
        #answer-key-print-content,
        #answer-key-print-content *,
        #bubble-sheet-printable-area,
        #bubble-sheet-printable-area *,
        #resultcard-print-container,
        #resultcard-print-container *,
        #mastersheet-print-container,
        #mastersheet-print-container *,
        #datesheet-print-container,
        #datesheet-print-container * {
          -webkit-print-color-adjust: exact !important;
          print-color-adjust: exact !important;
        }

        #answer-key-print-content [class*="text-white"],
        #answer-key-print-content .text-white,
        #resultcard-print-container [class*="text-white"],
        #resultcard-print-container .text-white,
        #mastersheet-print-container [class*="text-white"],
        #mastersheet-print-container .text-white,
        #bubble-sheet-printable-area [class*="text-white"],
        #bubble-sheet-printable-area .text-white {
          color: #000000 !important;
        }

        #answer-key-print-content [class*="bg-slate-900"],
        #answer-key-print-content [class*="bg-blue-900"],
        #resultcard-print-container [class*="bg-blue-900"],
        #resultcard-print-container [class*="bg-slate-900"],
        #mastersheet-print-container [class*="bg-blue-900"],
        #mastersheet-print-container [class*="bg-slate-900"],
        #bubble-sheet-printable-area [class*="bg-slate-800"],
        #bubble-sheet-printable-area [class*="bg-slate-900"] {
          background-color: #f1f5f9 !important;
          color: #000000 !important;
          border: 1.5pt solid #000000 !important;
        }

        #answer-key-print-content .answer-key-solved-badge {
          background-color: #f1f5f9 !important;
          color: #000000 !important;
          border: 1.5pt solid #000000 !important;
        }

        /* OMR Bubbles Mathematically Centered with Absolute Zero Overlap */
        .omr-bubble,
        .bubble-circle,
        #bubble-sheet-printable-area .omr-bubble,
        .omr-bubble-grid-container .omr-bubble {
          display: inline-flex !important;
          align-items: center !important;
          justify-content: center !important;
          text-align: center !important;
          width: 19px !important;
          height: 19px !important;
          min-width: 19px !important;
          min-height: 19px !important;
          max-width: 19px !important;
          max-height: 19px !important;
          border-radius: 50% !important;
          border: 1.5pt solid #000000 !important;
          background-color: #ffffff !important;
          color: #000000 !important;
          font-size: 8.5pt !important;
          font-weight: 900 !important;
          line-height: 1 !important;
          box-sizing: border-box !important;
          margin: 0 1px !important;
          flex-shrink: 0 !important;
        }

        /* Bubble sheet grid and roll number layout protection in print */
        #bubble-sheet-printable-area .bubble-grid-print {
          display: grid !important;
          grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
          column-gap: 16pt !important;
          row-gap: 4pt !important;
          width: 100% !important;
        }
        #bubble-sheet-printable-area .roll-number-table {
          margin: 0 auto !important;
          border-collapse: separate !important;
          border-spacing: 2pt !important;
        }
      }
"""

if print_rules not in html:
    html = html.replace('</style>', print_rules + '\n</style>', 1)
    print("Added print rules to index.html.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("index.html successfully updated!")
