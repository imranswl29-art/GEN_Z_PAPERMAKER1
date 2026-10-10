import os
import json
import re

BASE_DIR = "src/data/notes"

# Read ptbbData.ts to get exact subjects and chapters
with open("src/data/ptbbData.ts", "r", encoding="utf-8") as f:
    text = f.read()

# Subject mappings for Science Group
science_subjects = [
    ("9th-physics", "class9", "physics", "Physics", "طبیعیات"),
    ("9th-chemistry", "class9", "chemistry", "Chemistry", "کیمسٹری"),
    ("9th-biology", "class9", "biology", "Biology", "حیاتیات"),
    ("9th-computer", "class9", "computer", "Computer Science", "کمپیوٹر سائنس"),
    ("9th-mathematics", "class9", "mathematics", "Mathematics", "ریاضی"),
    ("9th-english", "class9", "english", "English", "انگریزی لازمی"),
    ("9th-urdu", "class9", "urdu", "Urdu", "اردو لازمی"),
    ("9th-islamiyat", "class9", "islamiyat", "Islamiat Compulsory", "اسلامیات لازمی"),
    ("9th-tarjuma-quran", "class9", "tarjuma_quran", "Tarjuma-tul-Quran-ul-Majeed", "ترجمۃ القرآن المجید"),
    ("9th-pakstudies", "class9", "pakstudies", "Pakistan Studies", "مطالعہ پاکستان"),
    
    ("10th-physics", "class10", "physics", "Physics", "طبیعیات"),
    ("10th-chemistry", "class10", "chemistry", "Chemistry", "کیمسٹری"),
    ("10th-biology", "class10", "biology", "Biology", "حیاتیات"),
    ("10th-computer", "class10", "computer", "Computer Science", "کمپیوٹر سائنس"),
    ("10th-mathematics", "class10", "mathematics", "Mathematics", "ریاضی"),
    ("10th-english", "class10", "english", "English", "انگریزی لازمی"),
    ("10th-urdu", "class10", "urdu", "Urdu", "اردو لازمی"),
    ("10th-islamiyat", "class10", "islamiyat", "Islamiat Compulsory", "اسلامیات لازمی"),
    ("10th-tarjuma-quran", "class10", "tarjuma_quran", "Tarjuma-tul-Quran-ul-Majeed", "ترجمۃ القرآن المجید"),
    ("10th-pakstudies", "class10", "pakstudies", "Pakistan Studies", "مطالعہ پاکستان"),
]

print("Ready to process", len(science_subjects), "Science subjects across 9th and 10th.")
