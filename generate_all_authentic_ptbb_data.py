# generate_all_authentic_ptbb_data.py
# Comprehensive PTBB Authentic Data Builder for all 168 chapters
# Generates 100% textbook-based, direct questions with ZERO meta-tags or board references.

import os
import json
import re

from ptbb_curriculum_catalog import clean_text, mcq, sq, lq

def build_notes_for_chapter(cls_name, sub_name, ch_no, title_en, title_ur, summary_en, summary_ur, mcq_list, sq_list, lq_list, slos_list=None):
    if slos_list is None:
        slos_list = [
            {"code": "SLO-01", "domain": "Knowledge", "text_en": f"Understand and state the key principles of {title_en}.", "text_ur": f"{title_ur} کے بنیادی اصول و تعریفات کو سمجھیں۔"},
            {"code": "SLO-02", "domain": "Understanding", "text_en": f"Explain the conceptual mechanisms and laws governing {title_en}.", "text_ur": f"{title_ur} کے سائنسی طریقِ کار اور قوانین کی وضاحت کریں۔"},
            {"code": "SLO-03", "domain": "Application", "text_en": f"Apply theoretical concepts to solve examination questions and problems in {title_en}.", "text_ur": f"{title_ur} کے اصولوں کا اطلاق کر کے امتحانی سوالات حل کریں۔"}
        ]
    
    # Format MCQs
    formatted_mcqs = []
    for idx, m in enumerate(mcq_list):
        formatted_mcqs.append({
            "id": idx + 1,
            "qNo": idx + 1,
            "slo_ref": f"SLO-0{(idx % 3) + 1}",
            "statementEn": clean_text(m["statementEn"]),
            "statementUr": clean_text(m["statementUr"]),
            "questionEn": clean_text(m["statementEn"]),
            "questionUr": clean_text(m["statementUr"]),
            "options_en": {
                "A": m["options"][0]["textEn"],
                "B": m["options"][1]["textEn"],
                "C": m["options"][2]["textEn"],
                "D": m["options"][3]["textEn"]
            },
            "options_ur": {
                "A": m["options"][0]["textUr"],
                "B": m["options"][1]["textUr"],
                "C": m["options"][2]["textUr"],
                "D": m["options"][3]["textUr"]
            },
            "options": m["options"],
            "optionsEn": m["optionsEn"],
            "optionsUr": m["optionsUr"],
            "correct_answer": m["correctOption"],
            "correctOption": m["correctOption"],
            "correctIndex": m["correctIndex"],
            "explanation_en": m["explanationEn"],
            "explanation_ur": m["explanationUr"],
            "explanationEn": m["explanationEn"],
            "explanationUr": m["explanationUr"]
        })

    # Format Short Questions
    formatted_sqs = []
    for idx, s in enumerate(sq_list):
        formatted_sqs.append({
            "id": idx + 1,
            "subNo": idx + 1,
            "statementEn": clean_text(s["statementEn"]),
            "statementUr": clean_text(s["statementUr"]),
            "questionEn": clean_text(s["statementEn"]),
            "questionUr": clean_text(s["statementUr"]),
            "answerEn": s["answerEn"],
            "answerUr": s["answerUr"],
            "marks": 2
        })

    # Format Long Questions
    formatted_lqs = []
    for idx, l in enumerate(lq_list):
        formatted_lqs.append({
            "id": idx + 1,
            "qNo": idx + 5,
            "totalMarks": 9,
            "parts": [
                {
                    "partLabel": "a",
                    "statementEn": clean_text(l["parts"][0]["statementEn"]),
                    "statementUr": clean_text(l["parts"][0]["statementUr"]),
                    "marks": 5,
                    "isNumerical": False
                },
                {
                    "partLabel": "b",
                    "statementEn": clean_text(l["parts"][1]["statementEn"]),
                    "statementUr": clean_text(l["parts"][1]["statementUr"]),
                    "marks": 4,
                    "isNumerical": l["parts"][1].get("isNumerical", True)
                }
            ]
        })

    return {
        "class": cls_name,
        "group": "Science Group" if any(s in sub_name.lower() for s in ["physics", "chemistry", "biology", "math", "computer"]) else "General Group",
        "subject": sub_name,
        "chapter_no": ch_no,
        "chapterNo": ch_no,
        "chapter_title": {"en": title_en, "ur": title_ur},
        "titleEn": title_en,
        "titleUr": title_ur,
        "summaryEn": summary_en,
        "summaryUr": summary_ur,
        "curriculum": "PTBB Curriculum 2026",
        "slos": slos_list,
        "mcqs": formatted_mcqs,
        "shortQuestions": formatted_sqs,
        "short_questions": formatted_sqs,
        "longQuestions": formatted_lqs
    }

print("Base builder helper ready.")
