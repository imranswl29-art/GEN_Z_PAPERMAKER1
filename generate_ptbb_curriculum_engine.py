import os
import json
import re

BASE_DIR = "src/data/notes"
os.makedirs(BASE_DIR, exist_ok=True)

# Parse ptbbData.ts to extract accurate subject and chapter titles
with open("src/data/ptbbData.ts", "r", encoding="utf-8") as f:
    ptbb_text = f.read()

SUBJECT_CONFIGS = [
    # Class 9th Science Group
    { "id": "9th-physics", "class": "Class 9th", "class_dir": "class9", "subject_dir": "physics", "subject": "Physics", "subject_ur": "طبیعیات" },
    { "id": "9th-chemistry", "class": "Class 9th", "class_dir": "class9", "subject_dir": "chemistry", "subject": "Chemistry", "subject_ur": "کیمسٹری" },
    { "id": "9th-biology", "class": "Class 9th", "class_dir": "class9", "subject_dir": "biology", "subject": "Biology", "subject_ur": "حیاتیات" },
    { "id": "9th-computer", "class": "Class 9th", "class_dir": "class9", "subject_dir": "computer", "subject": "Computer Science", "subject_ur": "کمپیوٹر سائنس" },
    { "id": "9th-mathematics", "class": "Class 9th", "class_dir": "class9", "subject_dir": "mathematics", "subject": "Mathematics", "subject_ur": "ریاضی" },
    { "id": "9th-english", "class": "Class 9th", "class_dir": "class9", "subject_dir": "english", "subject": "English", "subject_ur": "انگریزی لازمی" },
    { "id": "9th-urdu", "class": "Class 9th", "class_dir": "class9", "subject_dir": "urdu", "subject": "Urdu", "subject_ur": "اردو لازمی" },
    { "id": "9th-islamiyat", "class": "Class 9th", "class_dir": "class9", "subject_dir": "islamiyat", "subject": "Islamiat Compulsory", "subject_ur": "اسلامیات لازمی" },
    { "id": "9th-tarjuma-quran", "class": "Class 9th", "class_dir": "class9", "subject_dir": "tarjuma_quran", "subject": "Tarjuma-tul-Quran-ul-Majeed", "subject_ur": "ترجمۃ القرآن المجید" },
    { "id": "9th-pakstudies", "class": "Class 9th", "class_dir": "class9", "subject_dir": "pakstudies", "subject": "Pakistan Studies", "subject_ur": "مطالعہ پاکستان" },

    # Class 10th Science Group
    { "id": "10th-physics", "class": "Class 10th", "class_dir": "class10", "subject_dir": "physics", "subject": "Physics", "subject_ur": "طبیعیات" },
    { "id": "10th-chemistry", "class": "Class 10th", "class_dir": "class10", "subject_dir": "chemistry", "subject": "Chemistry", "subject_ur": "کیمسٹری" },
    { "id": "10th-biology", "class": "Class 10th", "class_dir": "class10", "subject_dir": "biology", "subject": "Biology", "subject_ur": "حیاتیات" },
    { "id": "10th-computer", "class": "Class 10th", "class_dir": "class10", "subject_dir": "computer", "subject": "Computer Science", "subject_ur": "کمپیوٹر سائنس" },
    { "id": "10th-mathematics", "class": "Class 10th", "class_dir": "class10", "subject_dir": "mathematics", "subject": "Mathematics", "subject_ur": "ریاضی" },
    { "id": "10th-english", "class": "Class 10th", "class_dir": "class10", "subject_dir": "english", "subject": "English", "subject_ur": "انگریزی لازمی" },
    { "id": "10th-urdu", "class": "Class 10th", "class_dir": "class10", "subject_dir": "urdu", "subject": "Urdu", "subject_ur": "اردو لازمی" },
    { "id": "10th-islamiyat", "class": "Class 10th", "class_dir": "class10", "subject_dir": "islamiyat", "subject": "Islamiat Compulsory", "subject_ur": "اسلامیات لازمی" },
    { "id": "10th-tarjuma-quran", "class": "Class 10th", "class_dir": "class10", "subject_dir": "tarjuma_quran", "subject": "Tarjuma-tul-Quran-ul-Majeed", "subject_ur": "ترجمۃ القرآن المجید" },
    { "id": "10th-pakstudies", "class": "Class 10th", "class_dir": "class10", "subject_dir": "pakstudies", "subject": "Pakistan Studies", "subject_ur": "مطالعہ پاکستان" },
]

# Extract chapters for each subject
def get_chapters_for_subject(sub_id):
    pos = ptbb_text.find(f'id:"{sub_id}"')
    if pos == -1:
        pos = ptbb_text.find(f'id: "{sub_id}"')
    if pos == -1:
        return []
    next_pos = ptbb_text.find('id:"', pos + 10)
    if next_pos == -1:
        next_pos = ptbb_text.find('id: "', pos + 10)
    if next_pos == -1:
        next_pos = len(ptbb_text)
    block = ptbb_text[pos:next_pos]
    
    # regex to find chapter objects
    chapters = []
    # match each {id:..., number:N, titleEn:"...", titleUr:"..."}
    ch_matches = re.finditer(r'number:\s*(\d+),\s*titleEn:\s*\"([^\"]+)\",\s*titleUr:\s*\"([^\"]+)\"', block)
    for m in ch_matches:
        ch_no = int(m.group(1))
        t_en = m.group(2).encode().decode('unicode-escape')
        t_ur = m.group(3).encode().decode('unicode-escape')
        chapters.append({
            "number": ch_no,
            "title_en": t_en,
            "title_ur": t_ur
        })
    return chapters

for sc in SUBJECT_CONFIGS:
    sc["chapters"] = get_chapters_for_subject(sc["id"])
    print(f"{sc['class']} {sc['subject']}: found {len(sc['chapters'])} chapters")
