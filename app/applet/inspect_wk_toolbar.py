with open('assets/index-DAioIUjd.js', 'r', encoding='utf-8') as f:
    text = f.read()

pos_wk = text.find('WK=({paper:n,onUpdatePaper:e,printSection:t,onOpenBubbleSheetModal:r,onOpenAnswerKeyModal:a})=>{')
print("pos_wk:", pos_wk)

pos_hub = text.find('Multi-Functional Paper Suite', pos_wk)
print("pos_hub:", pos_hub)

pos_container = text.find('exam-paper-container', pos_hub)
print("pos_container:", pos_container)

toolbar_code = text[pos_hub - 200 : pos_container]
print("Toolbar code length:", len(toolbar_code))

with open('wk_toolbar_snippet.js', 'w', encoding='utf-8') as f_out:
    f_out.write(toolbar_code)

print("Saved snippet to wk_toolbar_snippet.js")
