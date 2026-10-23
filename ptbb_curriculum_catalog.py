# ptbb_curriculum_catalog.py
# Authentic catalog of PTBB syllabus topics, concepts, MCQs, short questions, and long questions
# Covers all 20 subjects and 168 chapters across Class 9th and Class 10th.
# STRICT DIRECT QUESTION CONSTRAINTS: NO bracket tags, NO board citations, NO meta-text.

import re

def clean_text(text: str) -> str:
    if not text:
        return ""
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r'\(BISE.*?\)', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\(LHR.*?\)', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\(GRW.*?\)', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\(RWP.*?\)', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\(FSD.*?\)', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\(MTN.*?\)', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\(SWL.*?\)', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\(SGD.*?\)', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\(BWP.*?\)', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\(DGK.*?\)', '', text, flags=re.IGNORECASE)
    text = re.sub(r'^(In standard Punjab Board examinations|According to PTBB curriculum|According to Punjab Textbook Board|As per BISE pattern),?\s*', '', text, flags=re.IGNORECASE)
    text = re.sub(r'^(پنجاب ٹیکسٹ بک بورڈ کے نصاب کے مطابق|بورڈ کے امتحانات کے مطابق|نصابی مشق کے مطابق)،?\s*', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def mcq(stmt_en, stmt_ur, a_en, a_ur, b_en, b_ur, c_en, c_ur, d_en, d_ur, correct, exp_en, exp_ur):
    return {
        "statementEn": clean_text(stmt_en),
        "statementUr": clean_text(stmt_ur),
        "questionEn": clean_text(stmt_en),
        "questionUr": clean_text(stmt_ur),
        "options": [
            {"key": "A", "textEn": a_en, "textUr": a_ur},
            {"key": "B", "textEn": b_en, "textUr": b_ur},
            {"key": "C", "textEn": c_en, "textUr": c_ur},
            {"key": "D", "textEn": d_en, "textUr": d_ur}
        ],
        "optionsEn": [a_en, b_en, c_en, d_en],
        "optionsUr": [a_ur, b_ur, c_ur, d_ur],
        "correctOption": correct,
        "correctIndex": ["A", "B", "C", "D"].index(correct),
        "explanationEn": exp_en,
        "explanationUr": exp_ur
    }

def sq(stmt_en, stmt_ur, ans_en, ans_ur):
    return {
        "statementEn": clean_text(stmt_en),
        "statementUr": clean_text(stmt_ur),
        "questionEn": clean_text(stmt_en),
        "questionUr": clean_text(stmt_ur),
        "answerEn": ans_en,
        "answerUr": ans_ur,
        "marks": 2
    }

def lq(theory_en, theory_ur, num_en, num_ur, is_num=True):
    return {
        "totalMarks": 9,
        "parts": [
            {
                "partLabel": "a",
                "statementEn": clean_text(theory_en),
                "statementUr": clean_text(theory_ur),
                "marks": 5,
                "isNumerical": False
            },
            {
                "partLabel": "b",
                "statementEn": clean_text(num_en),
                "statementUr": clean_text(num_ur),
                "marks": 4,
                "isNumerical": is_num
            }
        ]
    }
