import re

print("Reading assets/index-DAioIUjd.js...")
with open("assets/index-DAioIUjd.js", "r", encoding="utf-8") as f:
    bundle = f.read()

print("Reading src/data/massiveQuestionBankEngine.ts...")
with open("src/data/massiveQuestionBankEngine.ts", "r", encoding="utf-8") as f:
    engine_ts = f.read()

# Transpile engine_ts to JS suitable for injection
engine_js = engine_ts
engine_js = engine_js.replace("export const PUNJAB_BOARDS_LIST", "const PUNJAB_BOARDS_LIST")
engine_js = engine_js.replace("export const PUNJAB_BOARD_CODES", "const PUNJAB_BOARD_CODES")
engine_js = engine_js.replace("export const PAST_YEARS", "const PAST_YEARS")
engine_js = engine_js.replace("export const SESSIONS", "const SESSIONS")
engine_js = re.sub(r"export\s+function\s+generatePunjabBoardCitation\s*\([^)]*\)\s*:\s*string", "function generatePunjabBoardCitation(seed)", engine_js)
engine_js = re.sub(r"export\s+function\s+generateMassiveQuestionPoolForChapter\s*\([^)]*\)", "function C8(n, e)", engine_js)

# Inside C8, the parameters were subject, chapter. Let's make sure it handles both (n, e) or (subject, chapter):
engine_js = engine_js.replace("function C8(n, e) {\n  const chNo = chapter.number;", "function C8(n, e) {\n  const subject = n;\n  const chapter = e;\n  const chNo = chapter.number;")
engine_js = engine_js.replace("function C8(n, e) {\n  const chNo = e.number;", "function C8(n, e) {\n  const subject = n;\n  const chapter = e;\n  const chNo = chapter.number;")

# Strip TypeScript type annotations
engine_js = engine_js.replace("const mcqs: any[] = [];", "const mcqs = [];")
engine_js = engine_js.replace("const shortQuestions: any[] = [];", "const shortQuestions = [];")
engine_js = engine_js.replace("const longQuestions: any[] = [];", "const longQuestions = [];")
engine_js = engine_js.replace("let subjectMcqTemplates: any[] = [];", "let subjectMcqTemplates = [];")
engine_js = engine_js.replace("let subjectExerciseMcqs: any[] = [];", "let subjectExerciseMcqs = [];")
engine_js = engine_js.replace("let subjectInTextBoxMcqs: any[] = [];", "let subjectInTextBoxMcqs = [];")
engine_js = engine_js.replace("let subjectShortTemplates: any[] = [];", "let subjectShortTemplates = [];")
engine_js = engine_js.replace("let subjectLongTemplates: any[] = [];", "let subjectLongTemplates = [];")

# Locate C8 and x8 in bundle
c8_idx = bundle.find("function C8(")
x8_idx = bundle.find("function x8(")
z3_idx = bundle.find("const X3=\"ptbb_user_custom_questions_v1\";")

print(f"Indices: c8={c8_idx}, x8={x8_idx}, z3={z3_idx}")

# New x8 that returns empty arrays (eliminating placeholders!)
clean_x8 = "function x8(n,e){return{mcqs:[],shortQuestions:[],longQuestions:[]}}"

# Replace the block from c8_idx to z3_idx
new_block = engine_js + "\n" + clean_x8 + "\n"
new_bundle = bundle[:c8_idx] + new_block + bundle[z3_idx:]

with open("assets/index-DAioIUjd.js", "w", encoding="utf-8") as f:
    f.write(new_bundle)

print("Successfully replaced C8 and x8 in assets/index-DAioIUjd.js!")
