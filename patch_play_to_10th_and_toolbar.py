import json, re

with open("assets/index-DAioIUjd.js", "r", encoding="utf-8") as f:
    bundle = f.read()

# 1. Eliminate horizontal button scrolling in WK Toolbar
old_toolbar_scroll = 'className:"flex items-center gap-2 overflow-x-auto pb-1 scrollbar-none"'
new_toolbar_scroll = 'className:"flex flex-wrap items-center gap-2.5 pb-1"'
assert bundle.count(old_toolbar_scroll) == 1, f"Found {bundle.count(old_toolbar_scroll)} matches for old_toolbar_scroll"
bundle = bundle.replace(old_toolbar_scroll, new_toolbar_scroll, 1)
print("1. Replaced WK toolbar overflow-x-auto with flex-wrap gap-2.5!")

# 2. Add Master Presets Dictionary for Play Group to 10th Class
# We insert MASTER_CLASS_PRESETS right before the DateSheet component definition
master_presets_js = '''
var MASTER_CLASS_PRESETS = {
  play: {
    name: "Play Group",
    datesheet: [
      { subject: "English (Alphabet & Phonics)", syllabus: "Oral Letter Recognition (A-Z), Sounds & Picture Reading" },
      { subject: "Urdu (Huroof-e-Tahajji)", syllabus: "Oral Huroof Pehchan (Alif se Yay) & Nazmain" },
      { subject: "Mathematics (Numbers 1-10)", syllabus: "Oral Counting (1-10), Shape Matching & Tracing" },
      { subject: "General Knowledge & Conversation", syllabus: "Basic Self Identity, Body Parts & Daily Courtesies" },
      { subject: "Art, Drawing & Coloring", syllabus: "Free Hand Coloring & Crayon Control" },
      { subject: "Nazra Quran & Islamiyat", syllabus: "First Kalimah Tayyibah & Daily Duas (Oral)" }
    ],
    subjects: [
      { id: "sub-p1", name: "English (Oral/Phonics)", totalMarks: 50, passingMarks: 20 },
      { id: "sub-p2", name: "Urdu (Oral/Nazm)", totalMarks: 50, passingMarks: 20 },
      { id: "sub-p3", name: "Mathematics (Counting)", totalMarks: 50, passingMarks: 20 },
      { id: "sub-p4", name: "General Knowledge", totalMarks: 50, passingMarks: 20 },
      { id: "sub-p5", name: "Art & Coloring", totalMarks: 50, passingMarks: 20 },
      { id: "sub-p6", name: "Nazra Quran / Islamiyat", totalMarks: 50, passingMarks: 20 }
    ],
    students: [
      { id: "st-1", rollNo: "01", name: "Zainab Fatima", fatherName: "Muhammad Usman", attendance: "98%", rank: "1st", remarks: "Brilliant participation and very active child!", marks: { "sub-p1": 48, "sub-p2": 49, "sub-p3": 47, "sub-p4": 50, "sub-p5": 48, "sub-p6": 50 } },
      { id: "st-2", rollNo: "02", name: "Muhammad Ibrahim", fatherName: "Ahmad Raza", attendance: "96%", rank: "2nd", remarks: "Great vocabulary and excellent coloring skills.", marks: { "sub-p1": 46, "sub-p2": 47, "sub-p3": 46, "sub-p4": 48, "sub-p5": 47, "sub-p6": 49 } },
      { id: "st-3", rollNo: "03", name: "Ayesha Bibi", fatherName: "Shahid Ali", attendance: "94%", rank: "3rd", remarks: "Very polite, attentive, and cooperative in class.", marks: { "sub-p1": 44, "sub-p2": 45, "sub-p3": 43, "sub-p4": 46, "sub-p5": 45, "sub-p6": 48 } }
    ]
  },
  nursery: {
    name: "Nursery Class",
    datesheet: [
      { subject: "English (Reading & Writing)", syllabus: "Capital & Small Letters (A-Z, a-z), Initial Phonics & Tracing" },
      { subject: "Urdu (Huroof & Chotay Alfaz)", syllabus: "Alif se Yay Likhna, Pehchan & Nazmain" },
      { subject: "Mathematics (Counting 1-50)", syllabus: "Missing Numbers, Shapes, Counting & Concept of Zero" },
      { subject: "General Knowledge & Science", syllabus: "Body Parts, Colors, Fruits, Vegetables & Animals" },
      { subject: "Drawing & Creative Art", syllabus: "Coloring inside boundaries & Basic object drawing" },
      { subject: "Nazra Quran & Islamiyat", syllabus: "Kalimah 1-2, Surah Ikhlas & Islamic Manners" }
    ],
    subjects: [
      { id: "sub-n1", name: "English (Writing & Phonics)", totalMarks: 50, passingMarks: 20 },
      { id: "sub-n2", name: "Urdu (Huroof-e-Tahajji)", totalMarks: 50, passingMarks: 20 },
      { id: "sub-n3", name: "Mathematics (1-50)", totalMarks: 50, passingMarks: 20 },
      { id: "sub-n4", name: "General Knowledge", totalMarks: 50, passingMarks: 20 },
      { id: "sub-n5", name: "Drawing & Coloring", totalMarks: 50, passingMarks: 20 },
      { id: "sub-n6", name: "Nazra Quran & Islamiyat", totalMarks: 50, passingMarks: 20 }
    ],
    students: [
      { id: "st-1", rollNo: "01", name: "Anaya Tariq", fatherName: "Tariq Mahmood", attendance: "98%", rank: "1st", remarks: "Exceptional writing and neat presentation.", marks: { "sub-n1": 49, "sub-n2": 48, "sub-n3": 50, "sub-n4": 48, "sub-n5": 49, "sub-n6": 50 } },
      { id: "st-2", rollNo: "02", name: "Hassan Ali", fatherName: "Ali Nawaz", attendance: "95%", rank: "2nd", remarks: "Very bright student, quick learner in Math.", marks: { "sub-n1": 46, "sub-n2": 47, "sub-n3": 48, "sub-n4": 47, "sub-n5": 46, "sub-n6": 48 } },
      { id: "st-3", rollNo: "03", name: "Mariam Khan", fatherName: "Faisal Khan", attendance: "92%", rank: "3rd", remarks: "Consistent effort and lovely recitation.", marks: { "sub-n1": 44, "sub-n2": 45, "sub-n3": 45, "sub-n4": 44, "sub-n5": 47, "sub-n6": 47 } }
    ]
  },
  prep: {
    name: "Prep Class (KG)",
    datesheet: [
      { subject: "English (Phonics & Sentences)", syllabus: "3-Letter Words, Rhyming Words, Vowels & Simple Sentences" },
      { subject: "Urdu (Jor Tor & Chotay Jumlay)", syllabus: "Do Harfi/Teen Harfi Alfaz, Jor Tor & Jumla Sazi" },
      { subject: "Mathematics (Numbers 1-100)", syllabus: "Addition, Subtraction, Shapes & Multiplication Tables 2-5" },
      { subject: "General Knowledge & Social Studies", syllabus: "Our Environment, Community Helpers, Science Basics & Seasons" },
      { subject: "Drawing & Art", syllabus: "Object Sketching, Shading & Creative Coloring" },
      { subject: "Nazra Quran & Islamiyat", syllabus: "Kalimat, Surah Kausar, Fatiha & Daily Masnoon Duas" }
    ],
    subjects: [
      { id: "sub-pr1", name: "English (Phonics & Grammar)", totalMarks: 75, passingMarks: 25 },
      { id: "sub-pr2", name: "Urdu (Jor Tor & Jumlay)", totalMarks: 75, passingMarks: 25 },
      { id: "sub-pr3", name: "Mathematics (1-100)", totalMarks: 75, passingMarks: 25 },
      { id: "sub-pr4", name: "General Knowledge", totalMarks: 50, passingMarks: 17 },
      { id: "sub-pr5", name: "Drawing & Arts", totalMarks: 50, passingMarks: 17 },
      { id: "sub-pr6", name: "Islamiyat & Nazra Quran", totalMarks: 50, passingMarks: 17 }
    ],
    students: [
      { id: "st-1", rollNo: "01", name: "Ayan Rasheed", fatherName: "Rasheed Ahmad", attendance: "97%", rank: "1st", remarks: "Outstanding grasping power and reading skills.", marks: { "sub-pr1": 73, "sub-pr2": 72, "sub-pr3": 75, "sub-pr4": 48, "sub-pr5": 47, "sub-pr6": 50 } },
      { id: "st-2", rollNo: "02", name: "Khadija Bibi", fatherName: "Muhammad Bilal", attendance: "96%", rank: "2nd", remarks: "Neat handwriting and great Math aptitude.", marks: { "sub-pr1": 70, "sub-pr2": 69, "sub-pr3": 72, "sub-pr4": 47, "sub-pr5": 48, "sub-pr6": 49 } }
    ]
  },
  class1: {
    name: "Class 1 (Grade 1)",
    datesheet: [
      { subject: "English", syllabus: "Textbook Units 1-8, Phonics, Spelling & Sentence Construction" },
      { subject: "Urdu", syllabus: "Hissa Nasr, Sabaq 1-8, Alfaz Maani & Imla" },
      { subject: "Mathematics", syllabus: "Addition, Subtraction, Place Values & Basic Geometry" },
      { subject: "General Knowledge", syllabus: "Science Concepts, Nature, Family & Cleanliness" },
      { subject: "Islamiyat / Ethics", syllabus: "Arkan-e-Islam, Seerat-un-Nabi & Basic Akhlaq" },
      { subject: "Nazra Quran & Tarjuma", syllabus: "Noorani Qaida & Short Surahs" }
    ],
    subjects: [
      { id: "sub-c1-1", name: "English", totalMarks: 100, passingMarks: 33 },
      { id: "sub-c1-2", name: "Urdu", totalMarks: 100, passingMarks: 33 },
      { id: "sub-c1-3", name: "Mathematics", totalMarks: 100, passingMarks: 33 },
      { id: "sub-c1-4", name: "General Knowledge", totalMarks: 75, passingMarks: 25 },
      { id: "sub-c1-5", name: "Islamiyat / Ethics", totalMarks: 50, passingMarks: 17 },
      { id: "sub-c1-6", name: "Nazra Quran", totalMarks: 50, passingMarks: 17 }
    ],
    students: [
      { id: "st-1", rollNo: "101", name: "Abdullah Tariq", fatherName: "Tariq Mehmood", attendance: "98%", rank: "1st", remarks: "Top academic achievement with neat work.", marks: { "sub-c1-1": 95, "sub-c1-2": 94, "sub-c1-3": 98, "sub-c1-4": 72, "sub-c1-5": 49, "sub-c1-6": 50 } },
      { id: "st-2", rollNo: "102", name: "Zoya Rehman", fatherName: "Abdul Rehman", attendance: "95%", rank: "2nd", remarks: "Very dedicated, excellent spelling and recitation.", marks: { "sub-c1-1": 92, "sub-c1-2": 91, "sub-c1-3": 95, "sub-c1-4": 70, "sub-c1-5": 48, "sub-c1-6": 49 } }
    ]
  },
  class2: {
    name: "Class 2 (Grade 2)",
    datesheet: [
      { subject: "English", syllabus: "Reading Comprehension, Parts of Speech & Creative Sentences" },
      { subject: "Urdu", syllabus: "Sabaq, Nazmain, Alfaz-Mutazad & Qawaid" },
      { subject: "Mathematics", syllabus: "Multiplication, Division, Word Problems & Measurement" },
      { subject: "General Knowledge & Science", syllabus: "Living Things, Matter, Weather & Seasons" },
      { subject: "Islamiyat / Ethics", syllabus: "Seerat-un-Nabi (PBUH) & Good Deeds" },
      { subject: "Computer Studies", syllabus: "Computer Parts, Mouse & Keyboard Skills" }
    ],
    subjects: [
      { id: "sub-c2-1", name: "English", totalMarks: 100, passingMarks: 33 },
      { id: "sub-c2-2", name: "Urdu", totalMarks: 100, passingMarks: 33 },
      { id: "sub-c2-3", name: "Mathematics", totalMarks: 100, passingMarks: 33 },
      { id: "sub-c2-4", name: "General Knowledge", totalMarks: 75, passingMarks: 25 },
      { id: "sub-c2-5", name: "Islamiyat", totalMarks: 50, passingMarks: 17 },
      { id: "sub-c2-6", name: "Computer Studies", totalMarks: 50, passingMarks: 17 }
    ],
    students: [
      { id: "st-1", rollNo: "201", name: "Hamza Shafiq", fatherName: "Shafiq Ahmad", attendance: "96%", rank: "1st", remarks: "Excellent grasp of Mathematics and English.", marks: { "sub-c2-1": 94, "sub-c2-2": 93, "sub-c2-3": 98, "sub-c2-4": 72, "sub-c2-5": 49, "sub-c2-6": 48 } }
    ]
  },
  class3: {
    name: "Class 3 (Grade 3)",
    datesheet: [
      { subject: "English", syllabus: "Textbook Units 1-10, Grammar, Creative Writing & Story" },
      { subject: "Urdu", syllabus: "Hissa Nasr, Nazam, Khulasa, Alfaz-Mutaradif" },
      { subject: "Mathematics", syllabus: "Fractions, Time, Money, Geometry & Tables" },
      { subject: "General Science", syllabus: "Ecosystems, Forces, Energy & Plant Life" },
      { subject: "Social Studies", syllabus: "Our Country Pakistan, Maps, Culture & Rules" },
      { subject: "Islamiyat / Ethics", syllabus: "Taharat, Wuzu, Namaz & Islamic History" },
      { subject: "Computer Studies", syllabus: "Windows Basics, MS Paint & Safe Computer Use" }
    ],
    subjects: [
      { id: "sub-c3-1", name: "English", totalMarks: 100, passingMarks: 33 },
      { id: "sub-c3-2", name: "Urdu", totalMarks: 100, passingMarks: 33 },
      { id: "sub-c3-3", name: "Mathematics", totalMarks: 100, passingMarks: 33 },
      { id: "sub-c3-4", name: "General Science", totalMarks: 75, passingMarks: 25 },
      { id: "sub-c3-5", name: "Social Studies", totalMarks: 75, passingMarks: 25 },
      { id: "sub-c3-6", name: "Islamiyat", totalMarks: 50, passingMarks: 17 },
      { id: "sub-c3-7", name: "Computer Studies", totalMarks: 50, passingMarks: 17 }
    ],
    students: [
      { id: "st-1", rollNo: "301", name: "Bilal Farooq", fatherName: "Farooq Azam", attendance: "97%", rank: "1st", remarks: "Consistently tops the class in all subjects.", marks: { "sub-c3-1": 93, "sub-c3-2": 92, "sub-c3-3": 96, "sub-c3-4": 71, "sub-c3-5": 70, "sub-c3-6": 48, "sub-c3-7": 49 } }
    ]
  },
  class4: {
    name: "Class 4 (Grade 4)",
    datesheet: [
      { subject: "English", syllabus: "Textbook Units 1-12, Tenses, Paragraph Writing & Comprehension" },
      { subject: "Urdu", syllabus: "Hissa Nasr, Nazm, Khat, Darkhwast & Qawaid-o-Insha" },
      { subject: "Mathematics", syllabus: "Decimals, Factors & Multiples, Angles & Data Handling" },
      { subject: "General Science", syllabus: "Human Body, States of Matter, Light & Sound" },
      { subject: "Social Studies", syllabus: "Provinces of Pakistan, Heritage, Government & Economy" },
      { subject: "Islamiyat / Ethics", syllabus: "Ahadith, Huqooq-ul-Ibad & Seerat-e-Tayyaba" },
      { subject: "Computer Education", syllabus: "MS Word Basics, Typing, Files & Folders" }
    ],
    subjects: [
      { id: "sub-c4-1", name: "English", totalMarks: 100, passingMarks: 33 },
      { id: "sub-c4-2", name: "Urdu", totalMarks: 100, passingMarks: 33 },
      { id: "sub-c4-3", name: "Mathematics", totalMarks: 100, passingMarks: 33 },
      { id: "sub-c4-4", name: "General Science", totalMarks: 75, passingMarks: 25 },
      { id: "sub-c4-5", name: "Social Studies", totalMarks: 75, passingMarks: 25 },
      { id: "sub-c4-6", name: "Islamiyat", totalMarks: 50, passingMarks: 17 },
      { id: "sub-c4-7", name: "Computer Education", totalMarks: 50, passingMarks: 17 }
    ],
    students: [
      { id: "st-1", rollNo: "401", name: "Mehak Noor", fatherName: "Noor Muhammad", attendance: "98%", rank: "1st", remarks: "Brilliant analytical mindset and neat writing.", marks: { "sub-c4-1": 94, "sub-c4-2": 93, "sub-c4-3": 97, "sub-c4-4": 73, "sub-c4-5": 71, "sub-c4-6": 49, "sub-c4-7": 48 } }
    ]
  },
  class5: {
    name: "Class 5 (Grade 5)",
    datesheet: [
      { subject: "English", syllabus: "Full Book (Reading, Formal Letters, Essays, Active/Passive)" },
      { subject: "Urdu", syllabus: "Full Book (Mazameen, Darkhwastat, Qawaid-o-Insha)" },
      { subject: "Mathematics", syllabus: "Full Book (LCM, HCF, Geometry, Fractions, Percentage)" },
      { subject: "General Science", syllabus: "Full Book (Human Organs, Microorganisms, Electricity & Heat)" },
      { subject: "Social Studies", syllabus: "Full Book (Geography, Pakistan Movement, Government & Civics)" },
      { subject: "Islamiyat (Compulsory)", syllabus: "Full Book & Seerat-e-Tayyaba" },
      { subject: "Tarjuma-tul-Quran", syllabus: "Parah 30 Prescribed Surahs with Translation" },
      { subject: "Computer Education", syllabus: "Word Processing, Formatting, Web Browsing & Safety" }
    ],
    subjects: [
      { id: "sub-c5-1", name: "English", totalMarks: 100, passingMarks: 33 },
      { id: "sub-c5-2", name: "Urdu", totalMarks: 100, passingMarks: 33 },
      { id: "sub-c5-3", name: "Mathematics", totalMarks: 100, passingMarks: 33 },
      { id: "sub-c5-4", name: "General Science", totalMarks: 100, passingMarks: 33 },
      { id: "sub-c5-5", name: "Social Studies", totalMarks: 100, passingMarks: 33 },
      { id: "sub-c5-6", name: "Islamiyat", totalMarks: 50, passingMarks: 17 },
      { id: "sub-c5-7", name: "Tarjuma-tul-Quran", totalMarks: 50, passingMarks: 17 },
      { id: "sub-c5-8", name: "Computer Education", totalMarks: 50, passingMarks: 17 }
    ],
    students: [
      { id: "st-1", rollNo: "501", name: "Saad Imran", fatherName: "Muhammad Imran", attendance: "99%", rank: "1st", remarks: "Distinction in all subjects! Top candidate for scholarship.", marks: { "sub-c5-1": 95, "sub-c5-2": 94, "sub-c5-3": 99, "sub-c5-4": 96, "sub-c5-5": 94, "sub-c5-6": 49, "sub-c5-7": 50, "sub-c5-8": 49 } }
    ]
  },
  class6: {
    name: "Class 6 (Middle)",
    datesheet: [
      { subject: "English (Compulsory)", syllabus: "Full Book (Units 1-10, Grammar, Direct/Indirect, Essays)" },
      { subject: "Urdu (Compulsory)", syllabus: "Full Book (Nasr, Nazm, Ghazal & Qawaid)" },
      { subject: "Mathematics", syllabus: "Full Book (Sets, Integers, Algebra, Ratio & Geometry)" },
      { subject: "General Science", syllabus: "Full Book (Cells, Tissues, Photosynthesis, Elements, Energy)" },
      { subject: "History & Geography", syllabus: "Full Book (Ancient Civilizations, Earth, Landforms)" },
      { subject: "Computer Science", syllabus: "Computer Systems, Hardware, Operating Systems & MS Office" },
      { subject: "Islamiyat (Compulsory)", syllabus: "Full Book & Prescribed Ahadith" },
      { subject: "Tarjuma-tul-Quran-ul-Majeed", syllabus: "Prescribed Parahs Translation & Vocabulary" }
    ],
    subjects: [
      { id: "sub-c6-1", name: "English", totalMarks: 100, passingMarks: 33 },
      { id: "sub-c6-2", name: "Urdu", totalMarks: 100, passingMarks: 33 },
      { id: "sub-c6-3", name: "Mathematics", totalMarks: 100, passingMarks: 33 },
      { id: "sub-c6-4", name: "General Science", totalMarks: 100, passingMarks: 33 },
      { id: "sub-c6-5", name: "History & Geography", totalMarks: 100, passingMarks: 33 },
      { id: "sub-c6-6", name: "Computer Science", totalMarks: 75, passingMarks: 25 },
      { id: "sub-c6-7", name: "Islamiyat", totalMarks: 50, passingMarks: 17 },
      { id: "sub-c6-8", name: "Tarjuma-tul-Quran", totalMarks: 50, passingMarks: 17 }
    ],
    students: [
      { id: "st-1", rollNo: "601", name: "Usman Ghani", fatherName: "Ghani ur Rehman", attendance: "98%", rank: "1st", remarks: "Exemplary performance and top tier diligence.", marks: { "sub-c6-1": 93, "sub-c6-2": 91, "sub-c6-3": 97, "sub-c6-4": 94, "sub-c6-5": 92, "sub-c6-6": 72, "sub-c6-7": 49, "sub-c6-8": 49 } }
    ]
  },
  class7: {
    name: "Class 7 (Middle)",
    datesheet: [
      { subject: "English (Compulsory)", syllabus: "Full Book (Units 1-12, Grammar, Comprehension & Letters)" },
      { subject: "Urdu (Compulsory)", syllabus: "Full Book (Hissa Nasr, Nazm, Mazameen & Insha-Pardazi)" },
      { subject: "Mathematics", syllabus: "Full Book (Rational Numbers, Linear Equations, Practical Geometry)" },
      { subject: "General Science", syllabus: "Full Book (Human Organ Systems, Circulation, Heat & Sound)" },
      { subject: "History & Geography", syllabus: "Full Book (Medieval Era, Mughal Empire & Climate)" },
      { subject: "Computer Science", syllabus: "Algorithms, Flowcharts, Excel & Word Processing" },
      { subject: "Islamiyat (Compulsory)", syllabus: "Full Book PTBB Board Standard" },
      { subject: "Tarjuma-tul-Quran-ul-Majeed", syllabus: "Prescribed Surahs Translation & Meanings" }
    ],
    subjects: [
      { id: "sub-c7-1", name: "English", totalMarks: 100, passingMarks: 33 },
      { id: "sub-c7-2", name: "Urdu", totalMarks: 100, passingMarks: 33 },
      { id: "sub-c7-3", name: "Mathematics", totalMarks: 100, passingMarks: 33 },
      { id: "sub-c7-4", name: "General Science", totalMarks: 100, passingMarks: 33 },
      { id: "sub-c7-5", name: "History & Geography", totalMarks: 100, passingMarks: 33 },
      { id: "sub-c7-6", name: "Computer Science", totalMarks: 75, passingMarks: 25 },
      { id: "sub-c7-7", name: "Islamiyat", totalMarks: 50, passingMarks: 17 },
      { id: "sub-c7-8", name: "Tarjuma-tul-Quran", totalMarks: 50, passingMarks: 17 }
    ],
    students: [
      { id: "st-1", rollNo: "701", name: "Daniyal Tariq", fatherName: "Tariq Mehmood", attendance: "97%", rank: "1st", remarks: "Great conceptual clarity and hardworking.", marks: { "sub-c7-1": 92, "sub-c7-2": 90, "sub-c7-3": 96, "sub-c7-4": 93, "sub-c7-5": 91, "sub-c7-6": 71, "sub-c7-7": 48, "sub-c7-8": 49 } }
    ]
  },
  class8: {
    name: "Class 8 (Middle)",
    datesheet: [
      { subject: "English (Compulsory)", syllabus: "Complete Board Syllabus (Units 1-12, Grammar & Composition)" },
      { subject: "Urdu (Compulsory)", syllabus: "Complete Board Syllabus (Nasr, Nazm, Ghazal & Mazameen)" },
      { subject: "Mathematics", syllabus: "Complete Board Syllabus (Real Numbers, Algebra, Polynomials, Geometry)" },
      { subject: "General Science", syllabus: "Complete Board Syllabus (Ecology, Heredity, Biotechnology, Force & Pressure)" },
      { subject: "History & Geography", syllabus: "Complete Board Syllabus (Subcontinent British Era, Pakistan Movement)" },
      { subject: "Computer Science", syllabus: "Computer Networks, Cybersecurity, Database & Spreadsheet" },
      { subject: "Islamiyat (Compulsory)", syllabus: "Complete Prescribed Middle Board Syllabus" },
      { subject: "Tarjuma-tul-Quran-ul-Majeed", syllabus: "Parah 1-5 Prescribed Surahs & Meanings" }
    ],
    subjects: [
      { id: "sub-c8-1", name: "English", totalMarks: 100, passingMarks: 33 },
      { id: "sub-c8-2", name: "Urdu", totalMarks: 100, passingMarks: 33 },
      { id: "sub-c8-3", name: "Mathematics", totalMarks: 100, passingMarks: 33 },
      { id: "sub-c8-4", name: "General Science", totalMarks: 100, passingMarks: 33 },
      { id: "sub-c8-5", name: "History & Geography", totalMarks: 100, passingMarks: 33 },
      { id: "sub-c8-6", name: "Computer Science", totalMarks: 75, passingMarks: 25 },
      { id: "sub-c8-7", name: "Islamiyat", totalMarks: 50, passingMarks: 17 },
      { id: "sub-c8-8", name: "Tarjuma-tul-Quran", totalMarks: 50, passingMarks: 17 }
    ],
    students: [
      { id: "st-1", rollNo: "801", name: "Maryam Siddique", fatherName: "Abu Bakr Siddique", attendance: "99%", rank: "1st", remarks: "Top position holder in Middle Section! Outstanding result.", marks: { "sub-c8-1": 96, "sub-c8-2": 95, "sub-c8-3": 99, "sub-c8-4": 97, "sub-c8-5": 95, "sub-c8-6": 74, "sub-c8-7": 50, "sub-c8-8": 50 } }
    ]
  },
  "9th": {
    name: "9th Class (Matric Part-I)",
    datesheet: [
      { subject: "English (Compulsory)", syllabus: "Full Book (Objective & Subjective)" },
      { subject: "Biology / Computer Science", syllabus: "Full Book - Chapters 1 to 9 (Theory)" },
      { subject: "Chemistry", syllabus: "Full Book - Chapters 1 to 8" },
      { subject: "Mathematics (Science)", syllabus: "Full Book - Units 1 to 17" },
      { subject: "Physics", syllabus: "Full Book - Units 1 to 9" },
      { subject: "Islamiat (Compulsory)", syllabus: "Full Book & Quranic Verses" },
      { subject: "Tarjuma-tul-Quran-ul-Majeed", syllabus: "Complete Prescribed Surahs" },
      { subject: "Urdu (Compulsory)", syllabus: "Full Book (Nazam, Ghazal & Sabaq)" },
      { subject: "Pakistan Studies", syllabus: "Full Book - Chapters 1 to 4" }
    ],
    subjects: [
      { id: "sub-1", name: "English", totalMarks: 75, passingMarks: 25 },
      { id: "sub-2", name: "Urdu", totalMarks: 75, passingMarks: 25 },
      { id: "sub-3", name: "Islamiat", totalMarks: 50, passingMarks: 17 },
      { id: "sub-4", name: "Pak Studies", totalMarks: 50, passingMarks: 17 },
      { id: "sub-5", name: "Mathematics", totalMarks: 75, passingMarks: 25 },
      { id: "sub-6", name: "Physics", totalMarks: 60, passingMarks: 20 },
      { id: "sub-7", name: "Chemistry", totalMarks: 60, passingMarks: 20 },
      { id: "sub-8", name: "Biology / CS", totalMarks: 60, passingMarks: 20 },
      { id: "sub-9", name: "Tarjuma Quran", totalMarks: 50, passingMarks: 17 }
    ],
    students: [
      { id: "st-1", rollNo: "101", name: "Muhammad Ali", fatherName: "Tariq Mehmood", attendance: "98%", rank: "1st", remarks: "Outstanding analytical skills and exemplary conduct. Keep it up!", marks: { "sub-1": 68, "sub-2": 70, "sub-3": 46, "sub-4": 45, "sub-5": 72, "sub-6": 56, "sub-7": 55, "sub-8": 58, "sub-9": 48 } },
      { id: "st-2", rollNo: "102", name: "Fatima Zahra", fatherName: "Rashid Khan", attendance: "96%", rank: "2nd", remarks: "Consistent academic excellence and brilliant presentation.", marks: { "sub-1": 65, "sub-2": 68, "sub-3": 44, "sub-4": 43, "sub-5": 69, "sub-6": 54, "sub-7": 52, "sub-8": 55, "sub-9": 47 } },
      { id: "st-3", rollNo: "103", name: "Ahmad Hassan", fatherName: "Muhammad Saeed", attendance: "94%", rank: "3rd", remarks: "Very hardworking and dedicated student. Great achievement!", marks: { "sub-1": 60, "sub-2": 63, "sub-3": 41, "sub-4": 40, "sub-5": 65, "sub-6": 50, "sub-7": 48, "sub-8": 51, "sub-9": 44 } },
      { id: "st-4", rollNo: "104", name: "Ayesha Noor", fatherName: "Abdul Rehman", attendance: "91%", rank: "4th", remarks: "Good progress; needs slight focus on Mathematics calculations.", marks: { "sub-1": 58, "sub-2": 61, "sub-3": 39, "sub-4": 38, "sub-5": 55, "sub-6": 46, "sub-7": 45, "sub-8": 48, "sub-9": 42 } }
    ]
  },
  "10th": {
    name: "10th Class (Matric Part-II)",
    datesheet: [
      { subject: "English (Compulsory)", syllabus: "Full Book (Lessons 1-13, Essays & Grammar)" },
      { subject: "Physics", syllabus: "Full Book - Units 10 to 18" },
      { subject: "Chemistry", syllabus: "Full Book - Units 9 to 16" },
      { subject: "Mathematics (Science)", syllabus: "Full Book - Units 1 to 13" },
      { subject: "Biology / Computer Science", syllabus: "Full Book - Theory & Practical Guidelines" },
      { subject: "Islamiat (Compulsory)", syllabus: "Full Book & Surah Ahzab" },
      { subject: "Tarjuma-tul-Quran-ul-Majeed", syllabus: "Prescribed Surahs & Translation" },
      { subject: "Pakistan Studies", syllabus: "Full Book - Chapters 5 to 8" },
      { subject: "Urdu (Compulsory)", syllabus: "Full Book (Hissa Nasr, Nazam & Mazameen)" }
    ],
    subjects: [
      { id: "sub-1", name: "English", totalMarks: 75, passingMarks: 25 },
      { id: "sub-2", name: "Urdu", totalMarks: 75, passingMarks: 25 },
      { id: "sub-3", name: "Islamiat", totalMarks: 50, passingMarks: 17 },
      { id: "sub-4", name: "Pak Studies", totalMarks: 50, passingMarks: 17 },
      { id: "sub-5", name: "Mathematics", totalMarks: 75, passingMarks: 25 },
      { id: "sub-6", name: "Physics", totalMarks: 60, passingMarks: 20 },
      { id: "sub-7", name: "Chemistry", totalMarks: 60, passingMarks: 20 },
      { id: "sub-8", name: "Biology / CS", totalMarks: 60, passingMarks: 20 },
      { id: "sub-9", name: "Tarjuma Quran", totalMarks: 50, passingMarks: 17 }
    ],
    students: [
      { id: "st-1", rollNo: "1001", name: "Muhammad Tayyab", fatherName: "Tariq Mehmood", attendance: "98%", rank: "1st", remarks: "Outstanding performance in Board Send-Up exams!", marks: { "sub-1": 71, "sub-2": 72, "sub-3": 48, "sub-4": 47, "sub-5": 74, "sub-6": 58, "sub-7": 57, "sub-8": 59, "sub-9": 49 } },
      { id: "st-2", rollNo: "1002", name: "Areeba Noor", fatherName: "Muhammad Aslam", attendance: "96%", rank: "2nd", remarks: "Brilliant presentation and solid theoretical grasp.", marks: { "sub-1": 69, "sub-2": 70, "sub-3": 46, "sub-4": 45, "sub-5": 71, "sub-6": 56, "sub-7": 55, "sub-8": 57, "sub-9": 48 } }
    ]
  }
};
'''

# Find insertion point right before aq=({currentUser
target_aq = "aq=({currentUser:n,activeHeader:e,onOpenSchoolProfile:t})=>"
assert bundle.count(target_aq) == 1
bundle = bundle.replace(target_aq, master_presets_js + "\n" + target_aq, 1)
print("2. Injected MASTER_CLASS_PRESETS successfully!")

# 3. Update DateSheet P function to use MASTER_CLASS_PRESETS
old_P = 'P=D=>{const U=D==="9th"?PS:sq,Q=new Date;Q.setDate(Q.getDate()+7);const se=U.map((pe,ce)=>{const me=new Date(Q);me.setDate(Q.getDate()+ce*2);const ue=me.toISOString().split("T")[0];return{id:`row-${D}-${ce+1}-${Date.now()}`,date:ue,day:me.toLocaleDateString("en-US",{weekday:"long"}),subject:pe.subject,paperType:pe.syllabus,timings:E.examTimings}});I(pe=>({...pe,classLevel:D==="9th"?"9th Class (Matric Part-I)":"10th Class (Matric Part-II)",rows:se})),y(`Loaded ${D} Class standard schedule!`)}'

new_P = 'P=D=>{const preset=MASTER_CLASS_PRESETS[D]||MASTER_CLASS_PRESETS["9th"];const U=preset.datesheet||preset.subjects||[];const Q=new Date;Q.setDate(Q.getDate()+7);const se=U.map((pe,ce)=>{const me=new Date(Q);me.setDate(Q.getDate()+ce*2);const ue=me.toISOString().split("T")[0];return{id:`row-${D}-${ce+1}-${Date.now()}`,date:ue,day:me.toLocaleDateString("en-US",{weekday:"long"}),subject:pe.subject||pe.name,paperType:pe.syllabus||pe.paperType||"Full Book (Objective & Subjective)",timings:E.examTimings}});I(pe=>({...pe,classLevel:preset.name,rows:se})),y(`Loaded ${preset.name} standard examination schedule!`)}'

assert bundle.count(old_P) == 1
bundle = bundle.replace(old_P, new_P, 1)
print("3. Updated DateSheet P function!")

# 4. Update DateSheet Quick Presets Dropdown to include all classes
old_ds_select = 'children:[l.jsx("option",{value:"",children:"📋 Quick Presets..."}),l.jsx("option",{value:"9th",children:"9th Science Preset"}),l.jsx("option",{value:"10th",children:"10th Science Preset"})]'

new_ds_select = 'children:[' + ','.join([
    'l.jsx("option",{value:"",children:"📋 Quick Class Presets (Play to 10th)..."})',
    'l.jsx("option",{value:"play",children:"Play Group"})',
    'l.jsx("option",{value:"nursery",children:"Nursery Class"})',
    'l.jsx("option",{value:"prep",children:"Prep Class (KG)"})',
    'l.jsx("option",{value:"class1",children:"Class 1 (Grade 1)"})',
    'l.jsx("option",{value:"class2",children:"Class 2 (Grade 2)"})',
    'l.jsx("option",{value:"class3",children:"Class 3 (Grade 3)"})',
    'l.jsx("option",{value:"class4",children:"Class 4 (Grade 4)"})',
    'l.jsx("option",{value:"class5",children:"Class 5 (Grade 5)"})',
    'l.jsx("option",{value:"class6",children:"Class 6 (Middle)"})',
    'l.jsx("option",{value:"class7",children:"Class 7 (Middle)"})',
    'l.jsx("option",{value:"class8",children:"Class 8 (Middle)"})',
    'l.jsx("option",{value:"9th",children:"9th Class (Matric-I)"})',
    'l.jsx("option",{value:"10th",children:"10th Class (Matric-II)"})'
]) + ']'

assert bundle.count(old_ds_select) == 1
bundle = bundle.replace(old_ds_select, new_ds_select, 1)
print("4. Updated DateSheet dropdown with all classes (Play to 10th)!")

# 5. Add loadMarksheetPreset function in lq (Marksheet component)
# In lq, right after const r=_T(n,e) or near F=S=>{...}
target_lq_f = 'F=S=>{v(S),setTimeout(()=>v(null),3e3)}'
assert bundle.count(target_lq_f) == 1
new_lq_helper = 'F=S=>{v(S),setTimeout(()=>v(null),3e3)};const loadMarksheetPreset=clsKey=>{const p=MASTER_CLASS_PRESETS[clsKey]||MASTER_CLASS_PRESETS["9th"];Z(curr=>({...curr,classLevel:p.name,subjects:p.subjects,students:p.students}));F(`Loaded ${p.name} subjects & student marks!`);}'
bundle = bundle.replace(target_lq_f, new_lq_helper, 1)
print("5. Added loadMarksheetPreset helper in Marksheet!")

# 6. Add Class Preset Dropdown to Marksheet's "Class, Exam & Session Configuration" header
old_ms_header = 'l.jsxs("div",{className:"text-xs font-bold text-slate-500",children:["Total Exam Marks: ",l.jsx("strong",{className:"text-blue-900 text-sm font-black",children:ne})]})'

new_ms_dropdown = 'children:[' + ','.join([
    'l.jsx("option",{value:"",children:"📋 Load Class Preset (Play to 10th)..."})',
    'l.jsx("option",{value:"play",children:"Play Group"})',
    'l.jsx("option",{value:"nursery",children:"Nursery Class"})',
    'l.jsx("option",{value:"prep",children:"Prep Class (KG)"})',
    'l.jsx("option",{value:"class1",children:"Class 1 (Grade 1)"})',
    'l.jsx("option",{value:"class2",children:"Class 2 (Grade 2)"})',
    'l.jsx("option",{value:"class3",children:"Class 3 (Grade 3)"})',
    'l.jsx("option",{value:"class4",children:"Class 4 (Grade 4)"})',
    'l.jsx("option",{value:"class5",children:"Class 5 (Grade 5)"})',
    'l.jsx("option",{value:"class6",children:"Class 6 (Middle)"})',
    'l.jsx("option",{value:"class7",children:"Class 7 (Middle)"})',
    'l.jsx("option",{value:"class8",children:"Class 8 (Middle)"})',
    'l.jsx("option",{value:"9th",children:"9th Class (Matric-I)"})',
    'l.jsx("option",{value:"10th",children:"10th Class (Matric-II)"})'
]) + ']'

new_ms_header = 'l.jsxs("div",{className:"flex flex-wrap items-center gap-3",children:[l.jsxs("select",{value:"",onChange:S=>{if(S.target.value){loadMarksheetPreset(S.target.value);S.target.value="";}},className:"form-select py-1 px-2.5 rounded-lg border border-slate-300 bg-white font-bold text-[11px] text-slate-700 shadow-xs cursor-pointer focus:ring-2 focus:ring-blue-500",' + new_ms_dropdown + '}),l.jsxs("div",{className:"text-xs font-bold text-slate-500",children:["Total Exam Marks: ",l.jsx("strong",{className:"text-blue-900 text-sm font-black",children:ne})]})]})'

assert bundle.count(old_ms_header) == 1
bundle = bundle.replace(old_ms_header, new_ms_header, 1)
print("6. Added Class Preset selector into Marksheet header!")

with open("assets/index-DAioIUjd.js", "w", encoding="utf-8") as f:
    f.write(bundle)

print("SUCCESS: assets/index-DAioIUjd.js fully updated!")
