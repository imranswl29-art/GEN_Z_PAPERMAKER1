with open('assets/index-DAioIUjd.js', 'r', encoding='utf-8') as f:
    code = f.read()

bad = '  </html>\n  ``,r=new Blob'
good = '  </html>\n  `,r=new Blob'

if bad in code:
    code = code.replace(bad, good, 1)
    print('Fixed double backtick in ly!')
else:
    print('bad string not found!')

with open('assets/index-DAioIUjd.js', 'w', encoding='utf-8') as f:
    f.write(code)
