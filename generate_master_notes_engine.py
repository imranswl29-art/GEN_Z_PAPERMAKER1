import os
import json

BASE_DIR = "src/data/notes"
os.makedirs(BASE_DIR, exist_ok=True)

# Subjects metadata
SCIENCE_SUBJECTS_CLASS9 = [
    ("physics", "Physics", "طبیعیات", 9),
    ("chemistry", "Chemistry", "کیمسٹری", 8),
    ("biology", "Biology", "حیاتیات", 9),
    ("mathematics", "Mathematics", "ریاضی", 17),
    ("computer", "Computer Science", "کمپیوٹر سائنس", 5),
    ("english", "English Compulsory", "انگریزی لازمی", 12),
    ("urdu", "Urdu Compulsory", "اردو لازمی", 7),
    ("islamiyat", "Islamiat Compulsory", "اسلامیات لازمی", 6),
    ("tarjuma_quran", "Tarjuma-tul-Quran-ul-Majeed", "ترجمۃ القرآن المجید", 6),
    ("pakstudies", "Pakistan Studies", "مطالعہ پاکستان", 5),
]

SCIENCE_SUBJECTS_CLASS10 = [
    ("physics", "Physics", "طبیعیات", 9),
    ("chemistry", "Chemistry", "کیمسٹری", 8),
    ("biology", "Biology", "حیاتیات", 9),
    ("mathematics", "Mathematics", "ریاضی", 13),
    ("computer", "Computer Science", "کمپیوٹر سائنس", 5),
    ("english", "English Compulsory", "انگریزی لازمی", 13),
    ("urdu", "Urdu Compulsory", "اردو لازمی", 10),
    ("islamiyat", "Islamiat Compulsory", "اسلامیات لازمی", 6),
    ("tarjuma_quran", "Tarjuma-tul-Quran-ul-Majeed", "ترجمۃ القرآن المجید", 6),
    ("pakstudies", "Pakistan Studies", "مطالعہ پاکستان", 5),
]

print("Metadata configured for Science Group subjects only.")
