import sys

with open('assets/index-DAioIUjd.js', 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Inspect DateSheet Excel
idx1 = code.find('function exportDateSheetToExcel(ds, brand)')
h1 = code.find('const html = `', idx1)
h1_end = code.find('downloadExcelFile(html,', h1)
print('DateSheet HTML length:', h1_end - h1)
ds_html_chunk = code[h1:h1_end]

# 2. Inspect ResultCard Excel
idx2 = code.find('function exportResultCardToExcel(st, marksheet, brand)')
h2 = code.find('const html = `', idx2)
h2_end = code.find('downloadExcelFile(html,', h2)
print('ResultCard HTML length:', h2_end - h2)
rc_html_chunk = code[h2:h2_end]

# 3. Inspect ly
idx3 = code.find('function ly(n,e){')
h3 = code.find('const t=`', idx3)
h3_end = code.find('`,r=new Blob([', h3)
print('ly HTML length:', h3_end - h3)
ly_html_chunk = code[h3:h3_end]

print("Found all 3 chunks successfully!")
