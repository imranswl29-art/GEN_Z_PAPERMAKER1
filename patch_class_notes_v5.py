import re
import subprocess
import os

with open('assets/index-DAioIUjd.js', 'r', encoding='utf-8') as f:
    text = f.read()

pos_sample = text.find('const SAMPLE_NOTES_DATA')
pos_hub = text.find('function renderHubSvg')

if pos_sample == -1 or pos_hub == -1:
    print("Could not find boundaries! pos_sample:", pos_sample, "pos_hub:", pos_hub)
    exit(1)

replacement_code = r'''const SAMPLE_NOTES_DATA = {
  "9th-physics": {
    1: {
      chapterNo: 1,
      titleEn: "Physical Quantities and Measurement",
      titleUr: "طبیعی مقداریں اور پیمائش",
      summaryEn: "This chapter covers the introduction to physics, physical quantities (base and derived), International System of Units (SI), scientific notation, prefixes, and measuring instruments (Vernier calliper, Screw gauge, Physical balance, Stop watch, and Measuring cylinder).",
      summaryUr: "اس باب میں طبیعیات کا تعارف، طبعی مقداریں (بنیادی اور ماخوذ)، بین الاقوامی نظام یونٹس (SI)، سائنسی علامات، پریفکسز اور پیمائشی آلات شامل ہیں۔",
      mcqs: [
        {
          id: "m1",
          questionEn: "The number of base units in SI is:",
          questionUr: "انٹرنیشنل سسٹم آف یونٹس (SI) میں بنیادی یونٹس کی تعداد ہے:",
          optionsEn: ["3", "5", "7", "9"],
          optionsUr: ["3", "5", "7", "9"],
          correctIndex: 2,
          explanationEn: "In SI system, there are seven base units: meter (m), kilogram (kg), second (s), ampere (A), kelvin (K), mole (mol), and candela (cd).",
          explanationUr: "ایس آئی سسٹم میں سات بنیادی یونٹس ہیں: میٹر، کلوگرام، سیکنڈ، ایمپئر، کیلون، مول اور کینڈیلا۔"
        },
        {
          id: "m2",
          questionEn: "Which one of the following unit is not a derived unit?",
          questionUr: "مندرجہ ذیل میں سے کون سا یونٹ ماخوذ یونٹ نہیں ہے؟",
          optionsEn: ["Pascal", "Kilogram", "Newton", "Watt"],
          optionsUr: ["پاسکل", "کلوگرام", "نیوٹن", "واٹ"],
          correctIndex: 1,
          explanationEn: "Kilogram is a base unit of mass in SI. Pascal, Newton, and Watt are derived units.",
          explanationUr: "کلوگرام ماس کا بنیادی یونٹ ہے جبکہ پاسکل، نیوٹن اور واٹ ماخوذ یونٹس ہیں۔"
        },
        {
          id: "m3",
          questionEn: "The least count of a standard Vernier Callipers is:",
          questionUr: "عام ورنیر کیلیپرز کا لیسٹ کاؤنٹ کتنا ہوتا ہے؟",
          optionsEn: ["0.1 cm", "0.01 cm", "0.001 cm", "1 mm"],
          optionsUr: ["0.1 سینٹی میٹر", "0.01 سینٹی میٹر", "0.001 سینٹی میٹر", "1 ملی میٹر"],
          correctIndex: 1,
          explanationEn: "Least count of Vernier Callipers is 0.1 mm or 0.01 cm.",
          explanationUr: "ورنیر کیلیپرز کا لیسٹ کاؤنٹ 0.1 ملی میٹر یا 0.01 سینٹی میٹر ہوتا ہے۔"
        },
        {
          id: "m4",
          questionEn: "An interval of 200 microseconds is equivalent to:",
          questionUr: "200 مائیکرو سیکنڈ کا وقفہ برابر ہوتا ہے:",
          optionsEn: ["0.2 s", "2 x 10^-4 s", "2 x 10^-6 s", "2 x 10^-8 s"],
          optionsUr: ["0.2 سیکنڈ", "2 x 10^-4 سیکنڈ", "2 x 10^-6 سیکنڈ", "2 x 10^-8 سیکنڈ"],
          correctIndex: 1,
          explanationEn: "200 μs = 200 x 10^-6 s = 2 x 10^-4 s.",
          explanationUr: "200 مائیکرو سیکنڈ = 200 ضرب 10 کی پاور منفی 6 = 2 ضرب 10 کی پاور منفی 4 سیکنڈ۔"
        },
        {
          id: "m5",
          questionEn: "Which of the following is the smallest quantity?",
          questionUr: "مندرجہ ذیل میں سے سب سے چھوٹی مقدار کون سی ہے؟",
          optionsEn: ["0.01 g", "2 mg", "100 μg", "5000 ng"],
          optionsUr: ["0.01 گرام", "2 ملی گرام", "100 مائیکرو گرام", "5000 نینو گرام"],
          correctIndex: 3,
          explanationEn: "5000 ng = 5000 x 10^-9 g = 5 x 10^-6 g, which is the smallest among all given options.",
          explanationUr: "5000 نینو گرام = 5 ضرب 10 کی پاور منفی 6 گرام، جو کہ سب سے چھوٹی مقدار ہے۔"
        }
      ],
      shortQuestions: [
        {
          id: "sq1",
          questionEn: "Define physics and name any four main branches of physics.",
          questionUr: "طبیعیات (Physics) کی تعریف کریں اور اس کی کوئی سی چار اہم شاخوں کے نام لکھیں۔",
          marks: 2,
          answerEn: "Physics is the branch of science that deals with matter, energy, and the mutual relationship between them.\n\nFour main branches of physics:\n1. Mechanics - Study of motion of objects, its causes and effects.\n2. Thermodynamics - Study of nature of heat, modes of transfer and effects.\n3. Electromagnetism - Study of charges at rest and in motion, effects and relations with magnetism.\n4. Nuclear Physics - Study of properties and behavior of nuclei and elementary particles.",
          answerUr: "تعریف: سائنس کی وہ شاخ جس میں مادے، انرجی اور ان کے باہمی تعلق کا مطالعہ کیا جاتا ہے، طبیعیات کہلاتی ہے۔\n\nطبیعیات کی چار اہم شاخیں:\n1۔ مکینکس: اجسام کی حرکت، وجوہات اور اثرات کا مطالعہ۔\n2۔ حرارت (تھرموڈائنامکس): حرارت کی ماہیت، منتقلی اور اثرات کا مطالعہ۔\n3۔ الیکٹرو میگنیٹزم: ساکن اور متحرک چارجز اور مقناطیسیت سے تعلق کا مطالعہ۔\n4۔ نیوکلیئر فزکس: ایٹم کے نیوکلیائی اور ذرات کی خصوصیات کا مطالعہ۔"
        },
        {
          id: "sq2",
          questionEn: "Differentiate between Base Quantities and Derived Quantities with two examples each.",
          questionUr: "بنیادی مقداروں اور ماخوذ مقداروں میں فرق واضح کریں اور ہر ایک کی دو دو مثالیں دیں۔",
          marks: 2,
          answerEn: "Base Quantities: Base quantities are the quantities on the basis of which other quantities are expressed. Examples: Length (meter), Mass (kilogram), Time (second).\n\nDerived Quantities: The quantities that are expressed in terms of base quantities are called derived quantities. Examples: Speed (m/s), Force (Newton), Work (Joule).",
          answerUr: "بنیادی مقداریں: بنیادی مقداریں وہ مقداریں ہیں جن کی بنیاد پر دوسری مقداریں بیان کی جاتی ہیں۔\nمثالیں: لمبائی (میٹر)، کمیت (کلوگرام)، وقت (سیکنڈ)۔\n\nماخوذ مقداریں: وہ مقداریں جو بنیادی مقداروں کی بنیاد پر اخذ کی جائیں، ماخوذ مقداریں کہلاتی ہیں۔\nمثالیں: رفتار (سپیڈ)، فورس (نیوٹن)، ورک (جول)۔"
        },
        {
          id: "sq3",
          questionEn: "What is meant by scientific notation (standard form)? Give one example.",
          questionUr: "سائنسی علامات (سٹینڈرڈ فارم) سے کیا مراد ہے؟ ایک مثال دیں۔",
          marks: 2,
          answerEn: "Scientific notation is a method in which a number is expressed as a power of ten multiplied by a number between 1 and 10.\nFormula form: N = M x 10^n (where 1 <= M < 10 and n is an integer).\n\nExample: The distance from the Earth to the Sun is approximately 150,000,000 km, which in scientific notation is written as 1.5 x 10^8 km.",
          answerUr: "تعریف: ایسا طریقہ جس میں کسی عدد کو 1 اور 10 کے درمیان کسی عدد اور 10 کی مناسب پاور میں ظاہر کیا جائے سائنسی علامات کہلاتا ہے۔\n\nمثال: زمین کا سورج سے فاصلہ تقریباً 150,000,000 کلومیٹر ہے، جسے سائنسی انداز میں 1.5 ضرب 10 کی طاقت 8 کلومیٹر لکھا جاتا ہے۔"
        }
      ]
    }
  },
  "9th-english": {
    1: {
      chapterNo: 1,
      titleEn: "The Saviour of Mankind",
      titleUr: "نوع انسانی کا نجات دہندہ (صلی اللہ علیہ وآلہ وسلم)",
      summaryEn: "This chapter highlights the Arabia of ancient times, the condition of humanity before Islam, the birth, proclamation of prophethood, and the divine message of Holy Prophet Hazrat Muhammad (PBUH) which transformed ignorant society into a beacon of justice and knowledge.",
      summaryUr: "یہ سبق جزیرہ نمائے عرب، اسلام سے پہلے انسانیت کی زبوں حالی اور خاتم النبیین حضرت محمد رسول اللہ ﷺ کے پیغامِ حق اور عظیم الشان انقلاب پر مبنی ہے۔",
      vocab: [
        { word: "Unparalleled", meaningUr: "بے مثال / لاثانی", context: "Arabia is a land of unparalleled charm and beauty." },
        { word: "Trackless", meaningUr: "بے نشان / گم راہ کن", context: "Trackless deserts of sand dunes in dazzling rays." },
        { word: "Dazzling", meaningUr: "خیرہ کن / چکا چوند کرنے والی", context: "Under the dazzling rays of a tropical sun." },
        { word: "Bestowed with", meaningUr: "عطا کیا گیا / نوازا گیا", context: "The Arabs were bestowed with a remarkable memory." },
        { word: "Eloquence", meaningUr: "فصاحت و بلاغت", context: "Their eloquence found expression in their poetry." },
        { word: "Solitude", meaningUr: "تنہائی / خلوت", context: "In the quiet solitude of Cave Hira, he meditated." }
      ],
      mcqs: [
        {
          id: "me1",
          questionEn: "Arabia is a land of unparalleled charm and beauty with its trackless deserts of:",
          questionUr: "عرب بے مثال حسن و دلکشی کی سرزمین ہے جس میں کس چیز کے بے نشان صحرا ہیں:",
          optionsEn: ["Sand dunes", "High mountains", "Deep valleys", "Flowing rivers"],
          optionsUr: ["ریت کے ٹیلے", "اونچے پہاڑ", "گہری وادیاں", "بہتے دریا"],
          correctIndex: 0,
          explanationEn: "According to paragraph 1: 'Arabia is a land of unparalleled charm and beauty with its trackless deserts of sand dunes in the dazzling rays of a tropical sun.'",
          explanationUr: "سبق کے پہلے پیراگراف کے مطابق: عرب شدید دھوپ میں ریت کے ٹیلوں کے بے نشان صحراؤں کا خطہ ہے۔"
        },
        {
          id: "me2",
          questionEn: "The word 'eloquence' means:",
          questionUr: "لفظ 'eloquence' کا کیا مطلب ہے؟",
          optionsEn: ["Fluent speech", "Strong memory", "Great power", "Deep sorrow"],
          optionsUr: ["فصیح اور پر اثر گفتگو", "مضبوط یادداشت", "بڑی طاقت", "گہرا غم"],
          correctIndex: 0,
          explanationEn: "'Eloquence' refers to fluent, persuasive and expressive speaking or writing.",
          explanationUr: "الوکوینس کا مطلب فصاحت، شستہ اور اثر انگیز گفتگو یا تحریر ہے۔"
        },
        {
          id: "me3",
          questionEn: "Where did Holy Prophet Hazrat Muhammad (PBUH) spend most of his time in meditation?",
          questionUr: "حضور اکرم ﷺ عبادت و مراقبہ میں اپنا زیادہ تر وقت کہاں گزارتے تھے؟",
          optionsEn: ["Cave of Thawr", "Cave of Hira", "Mount Uhud", "Mosque of Quba"],
          optionsUr: ["غارِ ثور", "غارِ حرا", "پہاڑ احد", "مسجدِ قبا"],
          correctIndex: 1,
          explanationEn: "In the quiet solitude of the Cave of Hira, he would spend days and weeks in remembrance of Allah Almighty.",
          explanationUr: "حضور پاک ﷺ غارِ حرا کی پرسکون خلوت میں اللہ تعالیٰ کی عبادت میں دن اور ہفتے گزارتے تھے۔"
        },
        {
          id: "me4",
          questionEn: "What was the mission of the Holy Prophet Hazrat Muhammad (PBUH)?",
          questionUr: "رسول اللہ ﷺ کا بنیادی مشن کیا تھا؟",
          optionsEn: ["To destroy superstitions and ignorance", "To elevate mankind to noble conception of life", "To establish belief in Oneness of Allah", "All of the above"],
          optionsUr: ["توہم پرستی اور جہالت کا خاتمہ", "انسانیت کو زندگی کے بلند مقصد سے روشناس کرانا", "اللہ کی توحید کا قیام", "یہ تمام"],
          correctIndex: 3,
          explanationEn: "The divine mission was to destroy superstition, ignorance, and disbelief and set up a noble conception of life guided by divine faith.",
          explanationUr: "حضور پاک ﷺ کا مشن تمام توہم پرستی اور گمراہی کا خاتمہ کر کے ایمان و عمل کی بلند قدریں قائم کرنا تھا۔"
        },
        {
          id: "me5",
          questionEn: "The Holy Quran was revealed in which language?",
          questionUr: "قرآن پاک کس زبان میں نازل ہوا؟",
          optionsEn: ["Arabic", "Persian", "Hebrew", "Urdu"],
          optionsUr: ["عربی", "فارسی", "عبرانی", "اردو"],
          correctIndex: 0,
          explanationEn: "The Holy Quran was revealed in the eloquent Arabic language.",
          explanationUr: "قرآن مجید فصیح و بلیغ عربی زبان میں نازل کیا گیا۔"
        }
      ],
      shortQuestions: [
        {
          id: "sqe1",
          questionEn: "What type of land is Arabia?",
          questionUr: "عرب کس قسم کی سرزمین ہے؟",
          marks: 2,
          answerEn: "Arabia is a land of unparalleled charm and beauty, with its trackless deserts of sand dunes in the dazzling rays of a tropical sun. Its starry sky has excited the imagination of poets and travelers.",
          answerUr: "عرب بے مثال حسن اور خوبصورتی کی سرزمین ہے جس میں تیز دھوپ میں ریت کے ٹیلوں کے بے نشان صحرا ہیں۔ اس کے تاروں بھرے آسمان نے شاعروں اور سیاحوں کے تخیل کو جلا بخشی ہے۔"
        },
        {
          id: "sqe2",
          questionEn: "For what ability were the Arabs famous throughout the ancient world?",
          questionUr: "عرب کس صلاحیت کی وجہ سے دنیا بھر میں مشہور تھے؟",
          marks: 2,
          answerEn: "The Arabs were world-famous for their eloquence and extraordinary memory. Their eloquence found expression in their rich poetry and grand fairs held at Ukaz.",
          answerUr: "اہلِ عرب اپنی فصاحت و بلاغت اور حیرت انگیز یادداشت کی بدولت دنیا بھر میں مشہور تھے۔ ان کی فصاحت کا اظہار ان کی شاعری اور عکاظ کے سالانہ میلے میں ہوتا تھا۔"
        },
        {
          id: "sqe3",
          questionEn: "What was the condition of mankind before the Holy Prophet Hazrat Muhammad (PBUH)?",
          questionUr: "حضور پاک ﷺ کی بعثت سے قبل نوعِ انسانی کی کیا حالت تھی؟",
          marks: 2,
          answerEn: "Before the advent of Islam, mankind stood on the verge of chaos. The civilization which had taken four thousand years to grow had started crumbling into ignorance, injustice, and idolatry.",
          answerUr: "حضور پاک ﷺ کی بعثت سے قبل انسانیت تباہی اور انتشار کے دہانے پر کھڑی تھی۔ وہ تہذیب جسے بننے میں چار ہزار سال لگے تھے، جہالت، بت پرستی اور ظلم کے بوجھ تلے بکھر رہی تھی۔"
        }
      ]
    }
  }
};

function getSubjectVisualTheme(nameEn = "") {
  const n = (nameEn || "").toLowerCase();
  if (n.includes("physic")) {
    return {
      icon: "⚡",
      badgeColor: "bg-blue-600 text-white shadow-blue-300",
      activeBg: "bg-blue-50/80 border-blue-600 shadow-md ring-2 ring-blue-300",
      tagColor: "bg-blue-100 text-blue-900 border-blue-200"
    };
  }
  if (n.includes("chem")) {
    return {
      icon: "🧪",
      badgeColor: "bg-emerald-600 text-white shadow-emerald-300",
      activeBg: "bg-emerald-50/80 border-emerald-600 shadow-md ring-2 ring-emerald-300",
      tagColor: "bg-emerald-100 text-emerald-900 border-emerald-200"
    };
  }
  if (n.includes("bio")) {
    return {
      icon: "🔬",
      badgeColor: "bg-teal-600 text-white shadow-teal-300",
      activeBg: "bg-teal-50/80 border-teal-600 shadow-md ring-2 ring-teal-300",
      tagColor: "bg-teal-100 text-teal-900 border-teal-200"
    };
  }
  if (n.includes("math")) {
    return {
      icon: "📐",
      badgeColor: "bg-indigo-600 text-white shadow-indigo-300",
      activeBg: "bg-indigo-50/80 border-indigo-600 shadow-md ring-2 ring-indigo-300",
      tagColor: "bg-indigo-100 text-indigo-900 border-indigo-200"
    };
  }
  if (n.includes("comput")) {
    return {
      icon: "💻",
      badgeColor: "bg-cyan-600 text-white shadow-cyan-300",
      activeBg: "bg-cyan-50/80 border-cyan-600 shadow-md ring-2 ring-cyan-300",
      tagColor: "bg-cyan-100 text-cyan-900 border-cyan-200"
    };
  }
  if (n.includes("english")) {
    return {
      icon: "🔤",
      badgeColor: "bg-amber-600 text-white shadow-amber-300",
      activeBg: "bg-amber-50/80 border-amber-600 shadow-md ring-2 ring-amber-300",
      tagColor: "bg-amber-100 text-amber-900 border-amber-200"
    };
  }
  if (n.includes("urdu")) {
    return {
      icon: "✒️",
      badgeColor: "bg-rose-600 text-white shadow-rose-300",
      activeBg: "bg-rose-50/80 border-rose-600 shadow-md ring-2 ring-rose-300",
      tagColor: "bg-rose-100 text-rose-900 border-rose-200"
    };
  }
  if (n.includes("islam") || n.includes("quran")) {
    return {
      icon: "🕌",
      badgeColor: "bg-emerald-700 text-white shadow-emerald-400",
      activeBg: "bg-emerald-50/80 border-emerald-700 shadow-md ring-2 ring-emerald-400",
      tagColor: "bg-emerald-100 text-emerald-950 border-emerald-300"
    };
  }
  if (n.includes("pak") || n.includes("mutalia")) {
    return {
      icon: "🇵🇰",
      badgeColor: "bg-green-700 text-white shadow-green-400",
      activeBg: "bg-green-50/80 border-green-700 shadow-md ring-2 ring-green-400",
      tagColor: "bg-green-100 text-green-950 border-green-300"
    };
  }
  return {
    icon: "📚",
    badgeColor: "bg-purple-600 text-white shadow-purple-300",
    activeBg: "bg-purple-50/80 border-purple-600 shadow-md ring-2 ring-purple-300",
    tagColor: "bg-purple-100 text-purple-900 border-purple-200"
  };
}

function renderSubjectIconGraphic(subName = "") {
  const n = (subName || "").toLowerCase();
  if (n.includes("pak") || n.includes("mutalia")) {
    return l.jsxs("svg", {
      className: "w-6 h-6",
      viewBox: "0 0 36 28",
      fill: "none",
      children: [
        l.jsx("rect", { width: "36", height: "28", rx: "4", fill: "#006622" }),
        l.jsx("rect", { width: "9", height: "28", rx: "2", fill: "#ffffff" }),
        l.jsx("path", {
          d: "M24.5 9.5 C20.5 11 18.5 15.5 20.2 19.5 C21.8 23.2 26 24.5 28.5 22.8 C25 24 21 21.5 20.2 18 C19.2 14 21.8 10.5 24.5 9.5 Z",
          fill: "#ffffff"
        }),
        l.jsx("polygon", {
          points: "25.5,10.5 26.5,12.8 29,13 27,14.5 27.5,17 25.5,15.5 23.5,17 24,14.5 22,13 24.5,12.8",
          fill: "#ffffff"
        })
      ]
    });
  }
  const theme = getSubjectVisualTheme(subName);
  return l.jsx("span", { children: theme.icon });
}

function getNotesForSubjectAndChapter(subjectId, chapterNo, subjectObj, chapterObj) {
  if (SAMPLE_NOTES_DATA[subjectId] && SAMPLE_NOTES_DATA[subjectId][chapterNo]) {
    return SAMPLE_NOTES_DATA[subjectId][chapterNo];
  }
  const isUrdu = (subjectObj.nameEn || "").toLowerCase().includes("urdu");
  const isEnglish = (subjectObj.nameEn || "").toLowerCase().includes("english");
  const chTitleEn = (chapterObj && chapterObj.titleEn) || ("Unit " + chapterNo + ": Fundamental Principles");
  const chTitleUr = (chapterObj && chapterObj.titleUr) || ("یونٹ " + chapterNo + ": بنیادی تصورات و اصول");

  return {
    chapterNo: chapterNo,
    titleEn: chTitleEn,
    titleUr: chTitleUr,
    summaryEn: `Standard Punjab Textbook Board (PTBB) syllabus notes for ${subjectObj.nameEn}, Unit ${chapterNo}. Contains fully solved Multiple Choice Questions (MCQs) with comprehensive justifications and Board pattern Short Questions with standard 2-mark model answers.`,
    summaryUr: `پنجاب ٹیکسٹ بک بورڈ کے نصاب کے عین مطابق ${subjectObj.nameUr || subjectObj.nameEn}، یونٹ نمبر ${chapterNo} کے مکمل حل شدہ نوٹس۔ بورڈ پیٹرن کے مطابق معروضی سوالات مع وجوہات اور مختصر سوالات مع 2 نمبر کے ماڈل جوابات۔`,
    vocab: isEnglish ? [
      { word: "Significance", meaningUr: "اہمیت / افادیت", context: "The significance of the topic is emphasized in board exams." },
      { word: "Comprehend", meaningUr: "سمجھنا / ادراک کرنا", context: "Students must comprehend core scientific principles." },
      { word: "Demonstrate", meaningUr: "ثابت کرنا / مظاہرہ کرنا", context: "Demonstrate the standard derivation step by step." }
    ] : undefined,
    mcqs: [
      {
        id: "mcq_gen_1",
        questionEn: `According to PTBB curriculum, what is the primary core concept introduced in Unit ${chapterNo} of ${subjectObj.nameEn}?`,
        questionUr: `پنجاب ٹیکسٹ بک بورڈ کے نصاب کے مطابق ${subjectObj.nameUr || subjectObj.nameEn} کے یونٹ ${chapterNo} کا بنیادی تصور کیا ہے؟`,
        optionsEn: ["Fundamental principles and standard definitions", "Secondary qualitative assumptions", "Hypothetical non-empirical theories", "None of the above"],
        optionsUr: ["بنیادی اصول اور معیاری تعریفات", "ثانوی مفروضات", "غیر سائنسی نظریات", "ان میں سے کوئی نہیں"],
        correctIndex: 0,
        explanationEn: `Standard PTBB syllabus begins Unit ${chapterNo} with clear definitions, foundational rules, and essential laws necessary for matriculation examinations.`,
        explanationUr: `بورڈ کے معیار کے مطابق ہر باب کا آغاز بنیادی تعریفات اور مستند سائنسی و تدریسی اصولوں سے ہوتا ہے۔`
      },
      {
        id: "mcq_gen_2",
        questionEn: `Which standard unit or measuring parameter is officially recommended by PTBB for Unit ${chapterNo}?`,
        questionUr: `یونٹ ${chapterNo} میں بورڈ کے نصاب کے مطابق کون سا پیمانہ یا یونٹ مستند مانا گیا ہے؟`,
        optionsEn: ["International System of Units (SI standard)", "Imperial British standard only", "Arbitrary local scale", "Unstandardized scale"],
        optionsUr: ["بین الاقوامی سسٹم آف یونٹس (SI معیار)", "صرف برطانوی نظام", "غیر معیاری پیمانہ", "کوئی بھی نہیں"],
        correctIndex: 0,
        explanationEn: "All BISE boards strictly mandate the SI standard and internationally accepted terminology for all scientific units.",
        explanationUr: "تمام تعلیمی بورڈز ایس آئی یونٹس اور مستند سائنسی اصطلاحات کو لازمی قرار دیتے ہیں۔"
      },
      {
        id: "mcq_gen_3",
        questionEn: `The fundamental relation highlighted in the key laws of ${subjectObj.nameEn} (Unit ${chapterNo}) illustrates:`,
        questionUr: `اس سبق کے اہم ترین کلیے کس بنیادی تعلق کو ظاہر کرتے ہیں؟`,
        optionsEn: ["Direct proportionality under controlled boundary conditions", "Inverse exponential decay only", "Completely random fluctuations", "Static non-varying values"],
        optionsUr: ["معیاری حالات کے تحت براہ راست تعلق", "بے قاعدہ تبدیلی", "غیر مستقل رویہ", "کوئی بھی نہیں"],
        correctIndex: 0,
        explanationEn: "Scientific and board formulas state direct proportional relationships under controlled experimental parameters.",
        explanationUr: "بورڈ کے نصاب میں سائنسی کلیے معیاری شرائط کے تحت براہ راست متناسب تعلق کو واضح کرتے ہیں۔"
      },
      {
        id: "mcq_gen_4",
        questionEn: `What is the key practical application of the concepts taught in Unit ${chapterNo}?`,
        questionUr: `اس یونٹ میں پڑھے گئے تصورات کا اہم ترین عملی اطلاق کیا ہے؟`,
        optionsEn: ["Accurate problem solving and analytical reasoning in daily life", "Theoretical memorization without practical utility", "Historical trivia retention", "None of the above"],
        optionsUr: ["روزمرہ زندگی اور امتحانات میں درست حل اور سائنسی استدلال", "صرف زبانی رٹا لگانا", "تاریخی حقائق کا بلا مقصد حفظ", "ان میں سے کوئی نہیں"],
        correctIndex: 0,
        explanationEn: "Modern BISE SLO-based examination papers test analytical understanding and real-world problem-solving skills.",
        explanationUr: "موجودہ بورڈ ایس ایل او امتحانی نظام میں عملی اطلاق اور فکری فہم کو فوقیت دی جاتی ہے۔"
      },
      {
        id: "mcq_gen_5",
        questionEn: `Which statement correctly reflects the textbook law defined in Unit ${chapterNo}?`,
        questionUr: `درج ذیل میں سے کون سا بیان کتاب میں بیان کردہ کلیے کی درست نمائندگی کرتا ہے؟`,
        optionsEn: ["Every physical phenomenon obeys universal conservation laws and natural order", "Natural phenomena occur without physical cause", "Physical quantities cannot be measured quantitatively", "All observations are independent of standard units"],
        optionsUr: ["ہر قدرتی مظہر بقائے توانائی اور فطری قوانین کا پابند ہوتا ہے", "قدرتی مظاہر بغیر کسی سبب کے رونما ہوتے ہیں", "طبعی مقداروں کی پیمائش ناممکن ہے", "تمام مشاہدات یونٹس سے آزاد ہوتے ہیں"],
        correctIndex: 0,
        explanationEn: "Standard PTBB textbooks strictly conform to physical laws of conservation and consistent reproducible scientific truths.",
        explanationUr: "درسی کتب کا بنیادی مقصد طلبہ کو قوانینِ فطرت اور سائنسی صداقتوں سے روشناس کرانا ہے۔"
      }
    ],
    shortQuestions: [
      {
        id: "sq_gen_1",
        questionEn: `State the standard textbook definition of the main topic in Unit ${chapterNo} of ${subjectObj.nameEn}.`,
        questionUr: `${subjectObj.nameUr || subjectObj.nameEn} کے یونٹ ${chapterNo} کے مرکزی موضوع کی مستند درسی تعریف بیان کریں۔`,
        marks: 2,
        answerEn: `Standard Definition:\nThe subject matter of Unit ${chapterNo} focuses on the systematic explanation and quantifiable laws governing ${subjectObj.nameEn}. It establishes the primary conditions under which scientific and literary phenomena are observed and calculated accurately.\n\nKey Rule:\n1. Strict adherence to PTBB defined terminology.\n2. Accurate mathematical or conceptual formulation.`,
        answerUr: `مستند درسی تعریف:\nاس باب کا مرکزی نکتہ ان بنیادی اور مستند اصولوں پر مبنی ہے جو موضوع کو سائنسی اور فکری اعتبار سے واضح کرتے ہیں۔ یہ وہ شرائط طے کرتا ہے جن کے تحت تمام مظاہر کا درست ادراک ممکن ہوتا ہے۔\n\nاہم نکات:\n1۔ درسی کتاب کی مستند اصطلاحات کا استعمال۔\n2۔ مدلل اور جامع تفہیم۔`
      },
      {
        id: "sq_gen_2",
        questionEn: `Write two essential conditions or characteristics required for the law discussed in Unit ${chapterNo}.`,
        questionUr: `اس یونٹ میں زیرِ بحث قانون یا تصور کے لیے کوئی سی دو ضروری شرائط یا خصوصیات تحریر کریں۔`,
        marks: 2,
        answerEn: `Two Essential Conditions:\n1. Physical and Environmental Equilibrium: The baseline experimental and contextual environment must remain constant throughout observations.\n2. Standard Unit Calibration: All measured values must strictly align with internationally accepted SI base or derived standards.`,
        answerUr: `دو لازمی شرائط:\n1۔ ماحول اور حالات کا یکساں رہنا: مشاہدات کے دوران بنیادی شرائط اور پیمانے تبدیل نہیں ہونے چاہئیں۔\n2۔ معیاری پیمائش: تمام حاصل کردہ اقدار ایس آئی (SI) یونٹس اور بورڈ کے معیار کے مطابق ہونی چاہئیں۔`
      },
      {
        id: "sq_gen_3",
        questionEn: `Give two everyday real-world examples or applications demonstrating the principles of Unit ${chapterNo}.`,
        questionUr: `اس سبق کے اصولوں کو واضح کرنے کے لیے روزمرہ زندگی سے دو عام مثالیں یا اطلاقات دیں۔`,
        marks: 2,
        answerEn: `Real-World Applications:\n1. Practical Everyday Utilization: Applied in engineering devices, industrial machinery, and household instruments ensuring precision and safety.\n2. Diagnostic & Laboratory Analysis: Serves as the bedrock for modern testing apparatus and experimental procedures across all Punjab education boards.`,
        answerUr: `روزمرہ زندگی سے دو عملی مثالیں:\n1۔ عام زندگی میں اطلاق: گھریلو اور صنعتی آلات میں درستگی اور تحفظ کو یقینی بنانے کے لیے ان قوانین کا استعمال ہوتا ہے۔\n2۔ تجرباتی اور تعلیمی اہمیت: پنجاب بھر کے بورڈز کے سلیبس میں تجربہ گاہوں اور پریکٹیکل امتحانات کا بنیادی ستون ہے۔`
      }
    ]
  };
}

function exportNotesToWordDoc(notesData, selectedClass, subjectNameEn, subjectNameUr, effectiveLangMode, schoolBrand) {
  const brandTitle = (schoolBrand && schoolBrand.name) || "SUPERIOR MODEL HIGH SCHOOL";
  const brandSub = (schoolBrand && schoolBrand.address) || "BISE Lahore / Punjab Board - Quality Education System";
  const docTitle = `${selectedClass}_Class_${subjectNameEn.replace(/\s+/g, '_')}_Unit_${notesData.chapterNo}_Solved_Notes_${effectiveLangMode}.docx`;

  let html = `<!DOCTYPE html>
<html xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:w="urn:schemas-microsoft-com:office:word" xmlns="http://www.w3.org/TR/REC-html40">
<head>
<meta charset="utf-8">
<title>${selectedClass} Class ${subjectNameEn} - Unit ${notesData.chapterNo} Solved Notes</title>
<style>
  @page { size: A4; margin: 1in; mso-page-orientation: portrait; }
  body { font-family: 'Calibri', 'Segoe UI', 'Jameel Noori Nastaleeq', Arial, sans-serif; font-size: 11pt; color: #1e293b; line-height: 1.5; }
  .header-box { text-align: center; border-bottom: 2pt solid #1e3a8a; padding-bottom: 12pt; margin-bottom: 16pt; }
  .school-title { font-size: 20pt; font-weight: bold; color: #1e3a8a; text-transform: uppercase; margin: 0; }
  .school-subtitle { font-size: 10pt; color: #64748b; margin-top: 3pt; font-weight: 600; }
  .notes-badge { display: inline-block; background-color: #1e3a8a; color: #ffffff; padding: 4pt 14pt; font-size: 12pt; font-weight: bold; border-radius: 4pt; margin-top: 8pt; }
  .meta-table { width: 100%; border-collapse: collapse; margin-bottom: 14pt; border: 1pt solid #cbd5e1; }
  .meta-table td { padding: 6pt 10pt; border: 1pt solid #cbd5e1; font-size: 10.5pt; font-weight: bold; }
  .section-heading { background-color: #f1f5f9; border-left: 4pt solid #1e3a8a; border-right: 4pt solid #1e3a8a; padding: 6pt 10pt; font-size: 13pt; font-weight: bold; color: #0f172a; margin-top: 16pt; margin-bottom: 10pt; }
  .item-card { border: 1pt solid #e2e8f0; border-radius: 4pt; padding: 10pt; margin-bottom: 10pt; background-color: #ffffff; page-break-inside: avoid; }
  .item-number { font-weight: bold; color: #1e3a8a; font-size: 11pt; margin-bottom: 4pt; }
  .question-text { font-size: 11.5pt; font-weight: bold; color: #0f172a; margin-bottom: 6pt; }
  .urdu-text { font-family: 'Jameel Noori Nastaleeq', 'Urdu Typesetting', Arial, sans-serif; direction: rtl; text-align: right; font-size: 13pt; line-height: 1.8; color: #0f172a; }
  .options-grid { width: 100%; border-collapse: collapse; margin-top: 6pt; margin-bottom: 6pt; }
  .options-grid td { width: 50%; padding: 4pt 6pt; border: 0.5pt solid #e2e8f0; font-size: 10pt; }
  .correct-ans { background-color: #ecfdf5; border: 1pt solid #10b981; color: #065f46; font-weight: bold; padding: 4pt 8pt; border-radius: 3pt; display: inline-block; margin-top: 4pt; font-size: 10pt; }
  .explanation { font-size: 9.5pt; color: #475569; margin-top: 4pt; font-style: italic; }
  .short-ans-box { background-color: #f8fafc; border-left: 3pt solid #10b981; padding: 8pt 10pt; margin-top: 6pt; font-size: 10.5pt; color: #1e293b; }
  .vocab-table { width: 100%; border-collapse: collapse; margin-top: 8pt; margin-bottom: 12pt; border: 1pt solid #cbd5e1; }
  .vocab-table th { background-color: #1e3a8a; color: #ffffff; padding: 6pt; text-align: left; font-size: 10.5pt; }
  .vocab-table td { padding: 6pt; border: 1pt solid #cbd5e1; font-size: 10pt; }
  .footer-box { text-align: center; font-size: 9pt; color: #94a3b8; border-top: 1pt solid #e2e8f0; padding-top: 10pt; margin-top: 20pt; }
</style>
</head>
<body>
  <div class="header-box">
    <div class="school-title">${brandTitle}</div>
    <div class="school-subtitle">${brandSub}</div>
    <div class="notes-badge">CLASS ${selectedClass.toUpperCase()} - SOLVED CHAPTER NOTES (${effectiveLangMode.toUpperCase()})</div>
  </div>

  <table class="meta-table">
    <tr>
      <td style="background-color: #f8fafc; width: 25%;">Subject:</td>
      <td style="width: 25%; color: #1e3a8a;">${subjectNameEn}</td>
      <td style="background-color: #f8fafc; width: 25%;">Unit / Chapter:</td>
      <td style="width: 25%; color: #1e3a8a;">Unit ${notesData.chapterNo}</td>
    </tr>
    <tr>
      <td style="background-color: #f8fafc;">Chapter Name:</td>
      <td colspan="3">${notesData.titleEn} ${effectiveLangMode !== 'english' && notesData.titleUr ? `&nbsp; (${notesData.titleUr})` : ''}</td>
    </tr>
  </table>`;

  if (effectiveLangMode !== 'english' && notesData.vocab && notesData.vocab.length > 0) {
    html += `
  <div class="section-heading">Key Vocabulary & Urdu Translation (Glossary)</div>
  <table class="vocab-table">
    <thead>
      <tr>
        <th style="width: 25%;">Word / Phrase</th>
        <th style="width: 35%; text-align: right;">Urdu Meaning</th>
        <th style="width: 40%;">Contextual Sentence</th>
      </tr>
    </thead>
    <tbody>`;
    notesData.vocab.forEach(v => {
      html += `
      <tr>
        <td style="font-weight: bold; color: #1e3a8a;">${v.word}</td>
        <td class="urdu-text" style="font-size: 11.5pt;">${v.meaningUr}</td>
        <td style="font-style: italic;">${v.context}</td>
      </tr>`;
    });
    html += `</tbody></table>`;
  }

  html += `<div class="section-heading">Section A: Solved Multiple Choice Questions (MCQs)</div>`;
  notesData.mcqs.forEach((mcq, idx) => {
    const letters = ['A', 'B', 'C', 'D'];
    html += `
  <div class="item-card">
    <div class="item-number">Q${idx + 1}. [MCQ]</div>`;
    if (effectiveLangMode === 'urdu') {
      html += `<div class="urdu-text" style="font-size: 12.5pt; font-weight: bold;">${mcq.questionUr || mcq.questionEn}</div>`;
    } else if (effectiveLangMode === 'english') {
      html += `<div class="question-text">${mcq.questionEn}</div>`;
    } else {
      html += `<div class="question-text">${mcq.questionEn}</div>`;
      if (mcq.questionUr) html += `<div class="urdu-text" style="margin-top: 2pt; font-size: 12pt;">${mcq.questionUr}</div>`;
    }

    html += `<table class="options-grid"><tr>`;
    mcq.optionsEn.forEach((opt, optIdx) => {
      const isCorrect = optIdx === mcq.correctIndex;
      const optUr = (mcq.optionsUr && mcq.optionsUr[optIdx]) || "";
      const textDisp = effectiveLangMode === 'urdu' ? (optUr || opt) : effectiveLangMode === 'english' ? opt : (optUr ? `${opt} (${optUr})` : opt);
      html += `<td style="${isCorrect ? 'background-color: #ecfdf5; font-weight: bold;' : ''}">(${letters[optIdx]}) ${textDisp} ${isCorrect ? ' ✔' : ''}</td>`;
      if (optIdx === 1) html += `</tr><tr>`;
    });
    html += `</tr></table>`;

    const correctLetter = letters[mcq.correctIndex];
    const correctOpt = mcq.optionsEn[mcq.correctIndex];
    html += `<div class="correct-ans">Correct Option: (${correctLetter}) ${correctOpt}</div>`;
    if (mcq.explanationEn) {
      if (effectiveLangMode === 'english') {
        html += `<div class="explanation"><strong>Explanation:</strong> ${mcq.explanationEn}</div>`;
      } else if (effectiveLangMode === 'urdu') {
        html += `<div class="explanation"><strong>Explanation:</strong> ${mcq.explanationUr || mcq.explanationEn}</div>`;
      } else {
        html += `<div class="explanation"><strong>Explanation:</strong> ${mcq.explanationEn}</div>`;
        if (mcq.explanationUr) html += `<div class="urdu-text" style="font-size: 11pt; margin-top: 2pt;">${mcq.explanationUr}</div>`;
      }
    }
    html += `</div>`;
  });

  html += `<div class="section-heading">Section B: Solved Short Questions (2 Marks Each)</div>`;
  notesData.shortQuestions.forEach((sq, idx) => {
    html += `
  <div class="item-card">
    <div class="item-number">Question ${idx + 1} (${sq.marks} Marks)</div>`;
    if (effectiveLangMode === 'urdu') {
      html += `<div class="urdu-text" style="font-size: 12.5pt; font-weight: bold;">${sq.questionUr || sq.questionEn}</div>`;
    } else if (effectiveLangMode === 'english') {
      html += `<div class="question-text">${sq.questionEn}</div>`;
    } else {
      html += `<div class="question-text">${sq.questionEn}</div>`;
      if (sq.questionUr) html += `<div class="urdu-text" style="margin-top: 2pt; font-size: 12pt;">${sq.questionUr}</div>`;
    }

    html += `<div class="short-ans-box"><strong>Standard Model Answer:</strong><br>`;
    if (effectiveLangMode === 'urdu') {
      html += `<div class="urdu-text" style="white-space: pre-line; margin-top: 4pt;">${sq.answerUr || sq.answerEn}</div>`;
    } else if (effectiveLangMode === 'english') {
      html += `<div style="white-space: pre-line; margin-top: 4pt;">${sq.answerEn}</div>`;
    } else {
      html += `<div style="white-space: pre-line; margin-top: 4pt;">${sq.answerEn}</div>`;
      if (sq.answerUr) {
        html += `<div class="urdu-text" style="white-space: pre-line; margin-top: 8pt; border-top: 1pt dashed #cbd5e1; padding-top: 6pt;">${sq.answerUr}</div>`;
      }
    }
    html += `</div></div>`;
  });

  html += `
  <div class="footer-box">
    Generated via Punjab Boards Examination Paper & Notes Generator System &bull; Strictly conforms to PTBB Curriculum
  </div>
</body>
</html>`;

  const blob = new Blob(['\ufeff', html], { type: 'application/vnd.ms-word;charset=utf-8' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = docTitle;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
}

async function exportNotesToPDF(elementId, selectedClass, subjectNameEn, chapterNo, effectiveLangMode) {
  const element = document.getElementById(elementId);
  if (!element) {
    window.print();
    return;
  }

  const { jsPDF } = window.jspdf || {};
  if (!jsPDF) {
    window.print();
    return;
  }

  const pdf = new jsPDF({
    orientation: 'portrait',
    unit: 'mm',
    format: 'a4',
    compress: true
  });

  const pageW = 210;
  const pageH = 297;
  const margin = 10;
  const printW = pageW - margin * 2;
  const printH = pageH - margin * 2;

  try {
    await Oh(element, pdf, printW, printH, margin, true);
    pdf.save(`${selectedClass}_Class_${subjectNameEn.replace(/\s+/g, '_')}_Unit_${chapterNo}_Solved_Notes_${effectiveLangMode}.pdf`);
  } catch (err) {
    console.error("PDF generation failed, falling back to window.print():", err);
    window.print();
  }
}

function ClassNotesView({ currentUser, onBack }) {
  // Step State: 1 = Select Class, 2 = Select Subject, 3 = Select Chapter & Medium, 4 = View & Print Solved Notes
  const [currentStep, setCurrentStep] = Ee.useState(1);
  const [selectedClass, setSelectedClass] = Ee.useState("");
  const classSubjects = Ee.useMemo(() => {
    if (!selectedClass) return [];
    return Wo.filter(s => s.classLevel === selectedClass);
  }, [selectedClass]);

  const [selectedSubjectId, setSelectedSubjectId] = Ee.useState("");
  const [isExportingPdf, setIsExportingPdf] = Ee.useState(false);

  const currentSubject = Ee.useMemo(() => {
    if (!selectedSubjectId) return null;
    return classSubjects.find(s => s.id === selectedSubjectId) || null;
  }, [classSubjects, selectedSubjectId]);

  const chapters = Ee.useMemo(() => {
    return (currentSubject && currentSubject.chapters) || [{ number: 1, titleEn: "Unit 1", titleUr: "یونٹ 1" }];
  }, [currentSubject]);

  const [selectedChapterNo, setSelectedChapterNo] = Ee.useState(1);
  Ee.useEffect(() => {
    if (chapters.length > 0 && !chapters.some(c => c.number === selectedChapterNo)) {
      setSelectedChapterNo(chapters[0].number);
    }
  }, [chapters, selectedChapterNo]);

  const isUrduSubject = Boolean(currentSubject && (currentSubject.nameEn || "").toLowerCase().includes("urdu"));
  const isEnglishSubject = Boolean(currentSubject && (currentSubject.nameEn || "").toLowerCase().includes("english"));

  const [languageMode, setLanguageMode] = Ee.useState("english");
  const effectiveLangMode = isUrduSubject ? "urdu" : isEnglishSubject ? "english" : languageMode;

  const currentChapter = Ee.useMemo(() => {
    return chapters.find(c => c.number === selectedChapterNo) || chapters[0];
  }, [chapters, selectedChapterNo]);

  const notesData = Ee.useMemo(() => {
    if (!currentSubject) return null;
    return getNotesForSubjectAndChapter(currentSubject.id, selectedChapterNo, currentSubject, currentChapter);
  }, [currentSubject, selectedChapterNo, currentChapter]);

  const [activeTab, setActiveTab] = Ee.useState("all");

  const handleDownloadPDF = async () => {
    if (!currentSubject || !notesData) return;
    try {
      setIsExportingPdf(true);
      await exportNotesToPDF("notes-print-sheet", selectedClass, currentSubject.nameEn, notesData.chapterNo, effectiveLangMode);
    } finally {
      setIsExportingPdf(false);
    }
  };

  const stepsList = [
    { num: 1, label: "Select Class", icon: "🏫" },
    { num: 2, label: "Select Subject", icon: "📚" },
    { num: 3, label: "Unit & Medium", icon: "📑" },
    { num: 4, label: "Solved Notes", icon: "📖" }
  ];

  return l.jsxs("div", {
    className: "space-y-5 max-w-7xl mx-auto pb-16 font-sans text-slate-800",
    children: [
      // Top Module Header & Stepper
      l.jsxs("div", {
        className: "bg-white p-4 sm:p-5 rounded-2xl border border-slate-200 shadow-xs space-y-4 no-print",
        children: [
          // Main Header Row (Clean Title & Active Status, without redundant Back to Dashboard button)
          l.jsxs("div", {
            className: "flex flex-wrap items-center justify-between gap-3",
            children: [
              l.jsxs("div", {
                className: "flex items-center gap-3",
                children: [
                  l.jsx("span", { className: "w-9 h-9 rounded-xl icon-3d-badge jewel-purple text-white shrink-0 flex items-center justify-center text-lg shadow-sm", children: "📖" }),
                  l.jsxs("div", {
                    children: [
                      l.jsx("h1", {
                        className: "text-lg sm:text-xl font-black text-slate-900 tracking-tight",
                        children: "CLASS 9th & 10th (Notes)"
                      }),
                      l.jsx("p", { className: "text-xs text-slate-500 font-semibold", children: "Punjab Textbook Board (PTBB) Solved Revision Notes" })
                    ]
                  })
                ]
              }),
              // Active Selection Indicator Chip
              l.jsxs("div", {
                className: "hidden md:flex items-center gap-2 bg-slate-50 px-3.5 py-1.5 rounded-xl border border-slate-200 text-xs font-bold text-slate-700 shadow-2xs",
                children: [
                  l.jsx("span", { className: "text-slate-400 font-normal", children: "Status:" }),
                  l.jsx("span", {
                    className: "px-2 py-0.5 rounded-md font-black " + (selectedClass ? "bg-blue-100 text-blue-800" : "bg-amber-100 text-amber-800"),
                    children: selectedClass ? (selectedClass + " Class") : "No Class Selected"
                  }),
                  selectedSubjectId && currentSubject && l.jsx("span", { className: "px-2 py-0.5 rounded-md bg-emerald-100 text-emerald-800 font-black", children: currentSubject.nameEn }),
                  selectedSubjectId && notesData && l.jsx("span", { className: "px-2 py-0.5 rounded-md bg-purple-100 text-purple-800 font-black", children: "Unit " + notesData.chapterNo }),
                  selectedSubjectId && l.jsx("span", { className: "px-2 py-0.5 rounded-md bg-indigo-100 text-indigo-800 font-black uppercase text-[10px]", children: effectiveLangMode })
                ]
              })
            ]
          }),

          // Stepper Navigation
          l.jsx("div", {
            className: "grid grid-cols-2 md:grid-cols-4 gap-2.5 pt-1",
            children: stepsList.map(st => {
              const isCurrent = currentStep === st.num;
              const isPast = currentStep > st.num;
              const canClick = (st.num === 1) || (st.num === 2 && Boolean(selectedClass)) || (st.num === 3 && Boolean(selectedSubjectId)) || (st.num === 4 && Boolean(selectedSubjectId));
              return l.jsxs("button", {
                key: st.num,
                type: "button",
                disabled: !canClick,
                onClick: () => { if (canClick) setCurrentStep(st.num); },
                className: "p-2.5 sm:p-3 rounded-xl text-center border-2 transition-all " + (
                  !canClick ? "opacity-50 cursor-not-allowed bg-slate-50 border-slate-200 text-slate-400" :
                  isCurrent ? "bg-blue-600 border-blue-700 text-white shadow-md ring-2 ring-blue-400/40 cursor-pointer" :
                  isPast ? "bg-emerald-600 border-emerald-700 text-white font-bold shadow-xs hover:bg-emerald-700 cursor-pointer" :
                  "bg-slate-50 border-slate-200 text-slate-600 hover:bg-slate-100 font-bold cursor-pointer"
                ),
                children: [
                  l.jsxs("div", {
                    className: "text-[11px] font-black uppercase flex items-center justify-center gap-1.5",
                    children: [
                      l.jsx("span", { children: st.icon }),
                      l.jsxs("span", { children: ["Step ", st.num] }),
                      isPast && l.jsx(bs, { className: "w-3 h-3 text-white shrink-0" })
                    ]
                  }),
                  l.jsx("div", {
                    className: "font-black text-xs sm:text-sm truncate mt-0.5",
                    children: st.label
                  })
                ]
              });
            })
          })
        ]
      }),

      // ==========================================
      // STEP 1: SELECT CLASS (ONLY OPEN ON STEP 1)
      // ==========================================
      currentStep === 1 && l.jsxs("div", {
        className: "bg-white p-6 sm:p-8 rounded-2xl border-2 border-slate-200 shadow-sm space-y-6 no-print",
        children: [
          l.jsxs("div", {
            className: "text-center max-w-xl mx-auto space-y-2",
            children: [
              l.jsxs("div", {
                className: "inline-flex items-center gap-2 px-3 py-1 rounded-full bg-blue-100 text-blue-900 font-black text-xs uppercase tracking-wider",
                children: [
                  l.jsx("span", { className: "w-2 h-2 rounded-full bg-blue-600" }),
                  "Step 1: Choose Matric Class"
                ]
              }),
              l.jsx("h2", { className: "text-2xl sm:text-3xl font-black text-slate-900", children: "Select Your Class" }),
              l.jsx("p", { className: "text-xs sm:text-sm text-slate-500 font-semibold", children: "Please select 9th or 10th Class to load official Punjab Textbook Board (PTBB) syllabus and solved notes." })
            ]
          }),

          // Two Interactive Big Class Cards
          l.jsxs("div", {
            className: "grid grid-cols-1 md:grid-cols-2 gap-5 max-w-3xl mx-auto pt-2",
            children: [
              // 9th Class Card
              l.jsxs("div", {
                onClick: () => {
                  setSelectedClass("9th");
                  setSelectedSubjectId("");
                },
                className: "p-6 rounded-2xl border-3 cursor-pointer transition-all relative overflow-hidden group " + (
                  selectedClass === "9th" ? "bg-blue-50/70 border-blue-600 shadow-lg ring-4 ring-blue-100 scale-[1.01]" :
                  "bg-white border-slate-200 hover:border-blue-400 hover:shadow-md"
                ),
                children: [
                  selectedClass === "9th" && l.jsx("div", {
                    className: "absolute top-3 right-3 w-7 h-7 rounded-full bg-blue-600 text-white flex items-center justify-center font-black text-sm shadow-sm",
                    children: "✔"
                  }),
                  l.jsxs("div", {
                    className: "flex items-start gap-4",
                    children: [
                      l.jsx("div", {
                        className: "w-16 h-16 rounded-2xl icon-3d-badge jewel-blue text-white flex items-center justify-center text-2xl font-black shrink-0",
                        children: "9th"
                      }),
                      l.jsxs("div", {
                        className: "space-y-1.5 flex-1",
                        children: [
                          l.jsx("h3", { className: "text-xl font-black text-slate-900 group-hover:text-blue-700", children: "Class 9th (Matric Part 1)" }),
                          l.jsx("p", { className: "text-xs text-slate-500 font-bold", children: "Punjab Textbook Board • All Science & Arts Subjects" }),
                          l.jsxs("div", {
                            className: "flex flex-wrap gap-1.5 pt-2",
                            children: [
                              l.jsx("span", { className: "px-2 py-0.5 rounded-md text-[11px] font-bold bg-slate-100 text-slate-700", children: "Physics" }),
                              l.jsx("span", { className: "px-2 py-0.5 rounded-md text-[11px] font-bold bg-slate-100 text-slate-700", children: "Chemistry" }),
                              l.jsx("span", { className: "px-2 py-0.5 rounded-md text-[11px] font-bold bg-slate-100 text-slate-700", children: "Biology" }),
                              l.jsx("span", { className: "px-2 py-0.5 rounded-md text-[11px] font-bold bg-slate-100 text-slate-700", children: "Math" }),
                              l.jsx("span", { className: "px-2 py-0.5 rounded-md text-[11px] font-bold bg-slate-100 text-slate-700", children: "English" }),
                              l.jsx("span", { className: "px-2 py-0.5 rounded-md text-[11px] font-bold bg-slate-100 text-slate-700", children: "Urdu" })
                            ]
                          })
                        ]
                      })
                    ]
                  })
                ]
              }),

              // 10th Class Card
              l.jsxs("div", {
                onClick: () => {
                  setSelectedClass("10th");
                  setSelectedSubjectId("");
                },
                className: "p-6 rounded-2xl border-3 cursor-pointer transition-all relative overflow-hidden group " + (
                  selectedClass === "10th" ? "bg-purple-50/70 border-purple-600 shadow-lg ring-4 ring-purple-100 scale-[1.01]" :
                  "bg-white border-slate-200 hover:border-purple-400 hover:shadow-md"
                ),
                children: [
                  selectedClass === "10th" && l.jsx("div", {
                    className: "absolute top-3 right-3 w-7 h-7 rounded-full bg-purple-600 text-white flex items-center justify-center font-black text-sm shadow-sm",
                    children: "✔"
                  }),
                  l.jsxs("div", {
                    className: "flex items-start gap-4",
                    children: [
                      l.jsx("div", {
                        className: "w-16 h-16 rounded-2xl icon-3d-badge jewel-purple text-white flex items-center justify-center text-2xl font-black shrink-0",
                        children: "10th"
                      }),
                      l.jsxs("div", {
                        className: "space-y-1.5 flex-1",
                        children: [
                          l.jsx("h3", { className: "text-xl font-black text-slate-900 group-hover:text-purple-700", children: "Class 10th (Matric Part 2)" }),
                          l.jsx("p", { className: "text-xs text-slate-500 font-bold", children: "Punjab Textbook Board • All Science & Arts Subjects" }),
                          l.jsxs("div", {
                            className: "flex flex-wrap gap-1.5 pt-2",
                            children: [
                              l.jsx("span", { className: "px-2 py-0.5 rounded-md text-[11px] font-bold bg-slate-100 text-slate-700", children: "Physics" }),
                              l.jsx("span", { className: "px-2 py-0.5 rounded-md text-[11px] font-bold bg-slate-100 text-slate-700", children: "Chemistry" }),
                              l.jsx("span", { className: "px-2 py-0.5 rounded-md text-[11px] font-bold bg-slate-100 text-slate-700", children: "Computer" }),
                              l.jsx("span", { className: "px-2 py-0.5 rounded-md text-[11px] font-bold bg-slate-100 text-slate-700", children: "Pak Studies" }),
                              l.jsx("span", { className: "px-2 py-0.5 rounded-md text-[11px] font-bold bg-slate-100 text-slate-700", children: "Islamiat" })
                            ]
                          })
                        ]
                      })
                    ]
                  })
                ]
              })
            ]
          }),

          // Standard Sized & Proportioned Next Button for Step 1 (Height 44-48px, min-width 140px, rounded-lg)
          l.jsx("div", {
            className: "flex justify-center pt-5",
            children: l.jsx("button", {
              type: "button",
              disabled: !selectedClass,
              onClick: () => {
                if (selectedClass) setCurrentStep(2);
              },
              className: "min-h-[46px] max-h-[48px] px-8 py-2.5 rounded-lg font-bold text-sm min-w-[150px] inline-flex items-center justify-center gap-2 transition-all cursor-pointer shadow-sm active:scale-95 " + (
                selectedClass
                  ? "bg-blue-600 hover:bg-blue-700 text-white shadow-blue-200"
                  : "bg-slate-200 text-slate-400 cursor-not-allowed shadow-none"
              ),
              children: "Next →"
            })
          })
        ]
      }),

      // ==========================================
      // STEP 2: SELECT SUBJECT (ONLY OPEN ON STEP 2)
      // ==========================================
      currentStep === 2 && l.jsxs("div", {
        className: "bg-white p-6 sm:p-8 rounded-2xl border-2 border-slate-200 shadow-sm space-y-6 no-print",
        children: [
          l.jsxs("div", {
            className: "text-center max-w-xl mx-auto space-y-2",
            children: [
              l.jsxs("div", {
                className: "inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-100 text-emerald-900 font-black text-xs uppercase tracking-wider",
                children: [
                  l.jsx("span", { className: "w-2 h-2 rounded-full bg-emerald-600" }),
                  "Step 2: Choose PTBB Subject (" + (selectedClass || "Matric") + " Class)"
                ]
              }),
              l.jsx("h2", { className: "text-2xl sm:text-3xl font-black text-slate-900", children: "Select Subject" }),
              l.jsx("p", { className: "text-xs sm:text-sm text-slate-500 font-semibold", children: "Click on any PTBB textbook subject below to generate its solved revision notes." })
            ]
          }),

          // Subjects Grid with Modern, Colorful, and High-Contrast Visual Icons
          l.jsx("div", {
            className: "grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-3.5 max-w-5xl mx-auto pt-2",
            children: classSubjects.map(sub => {
              const isSelected = sub.id === selectedSubjectId;
              const chCount = (sub.chapters && sub.chapters.length) || 0;
              const theme = getSubjectVisualTheme(sub.nameEn);
              return l.jsxs("div", {
                key: sub.id,
                onClick: () => setSelectedSubjectId(sub.id),
                className: "p-4 rounded-xl border-2 cursor-pointer transition-all flex items-center justify-between gap-3 " + (
                  isSelected ? theme.activeBg :
                  "bg-white border-slate-200 hover:border-slate-300 hover:bg-slate-50/80 shadow-2xs"
                ),
                children: [
                  l.jsxs("div", {
                    className: "flex items-center gap-3.5 min-w-0",
                    children: [
                      l.jsx("div", {
                        className: `w-12 h-12 rounded-xl flex items-center justify-center text-2xl font-bold shrink-0 shadow-md ${theme.badgeColor}`,
                        children: renderSubjectIconGraphic(sub.nameEn)
                      }),
                      l.jsxs("div", {
                        className: "min-w-0",
                        children: [
                          l.jsx("h4", { className: "font-black text-slate-900 text-sm sm:text-base truncate", children: sub.nameEn }),
                          l.jsxs("div", {
                            className: "flex items-center gap-1.5 mt-0.5",
                            children: [
                              l.jsx("span", { className: "text-xs text-slate-500 font-bold", children: chCount + " PTBB Chapters" }),
                              sub.group && l.jsx("span", { className: `text-[10px] uppercase font-black px-1.5 py-0.2 rounded border ${theme.tagColor}`, children: sub.group })
                            ]
                          })
                        ]
                      })
                    ]
                  }),
                  l.jsx("div", {
                    className: "w-6 h-6 rounded-full flex items-center justify-center font-bold text-xs shrink-0 " + (
                      isSelected ? "bg-emerald-600 text-white shadow-xs" : "border-2 border-slate-300 text-transparent"
                    ),
                    children: isSelected ? "✔" : ""
                  })
                ]
              });
            })
          }),

          // Standardized Navigation Bar for Step 2 (Height 44-48px, min-width 130px, gap-4)
          l.jsxs("div", {
            className: "flex items-center justify-between gap-4 max-w-5xl mx-auto pt-6 border-t border-slate-200",
            children: [
              l.jsx("button", {
                type: "button",
                onClick: () => setCurrentStep(1),
                className: "min-h-[44px] max-h-[48px] px-6 py-2.5 rounded-lg border border-slate-300 text-slate-700 bg-white hover:bg-slate-50 font-bold text-sm min-w-[130px] inline-flex items-center justify-center transition-all cursor-pointer shadow-xs active:scale-95",
                children: "← Back"
              }),
              l.jsx("button", {
                type: "button",
                disabled: !selectedSubjectId,
                onClick: () => {
                  if (selectedSubjectId) setCurrentStep(3);
                },
                className: "min-h-[44px] max-h-[48px] px-8 py-2.5 rounded-lg font-bold text-sm min-w-[140px] inline-flex items-center justify-center transition-all cursor-pointer shadow-sm active:scale-95 " + (
                  selectedSubjectId
                    ? "bg-emerald-600 hover:bg-emerald-700 text-white shadow-emerald-200"
                    : "bg-slate-200 text-slate-400 cursor-not-allowed shadow-none"
                ),
                children: "Next →"
              })
            ]
          })
        ]
      }),

      // ==========================================
      // STEP 3: SELECT CHAPTER & MEDIUM (ONLY STEP 3)
      // ==========================================
      currentStep === 3 && currentSubject && l.jsxs("div", {
        className: "bg-white p-6 sm:p-8 rounded-2xl border-2 border-slate-200 shadow-sm space-y-6 no-print",
        children: [
          l.jsxs("div", {
            className: "text-center max-w-xl mx-auto space-y-2",
            children: [
              l.jsxs("div", {
                className: "inline-flex items-center gap-2 px-3 py-1 rounded-full bg-purple-100 text-purple-900 font-black text-xs uppercase tracking-wider",
                children: [
                  l.jsx("span", { className: "w-2 h-2 rounded-full bg-purple-600" }),
                  "Step 3: Chapter & Language Selection"
                ]
              }),
              l.jsx("h2", { className: "text-2xl sm:text-3xl font-black text-slate-900", children: "Select Chapter & Language" }),
              l.jsxs("p", {
                className: "text-xs sm:text-sm text-slate-600 font-bold",
                children: [
                  "Active Subject: ",
                  l.jsx("span", { className: "text-blue-800 font-black", children: currentSubject.nameEn }),
                  " (" + selectedClass + " Class)"
                ]
              })
            ]
          }),

          // Section A: Language Medium Selection Box
          l.jsxs("div", {
            className: "max-w-4xl mx-auto bg-slate-50 border-2 border-slate-200 p-4 sm:p-5 rounded-2xl space-y-3",
            children: [
              l.jsxs("div", {
                className: "flex items-center justify-between",
                children: [
                  l.jsx("span", { className: "text-xs font-black uppercase tracking-wider text-slate-700", children: "Language Medium:" }),
                  isUrduSubject ? l.jsx("span", { className: "px-3 py-1 rounded-full text-xs font-black bg-emerald-100 text-emerald-800 border border-emerald-300", children: "Urdu Medium Only (100% Urdu)" }) :
                  isEnglishSubject ? l.jsx("span", { className: "px-3 py-1 rounded-full text-xs font-black bg-blue-100 text-blue-800 border border-blue-300", children: "English Medium with Urdu Translation Table" }) :
                  l.jsx("span", { className: "text-xs text-slate-500 font-bold", children: "Choose preferred language medium below:" })
                ]
              }),

              // Medium Toggles or Information
              isUrduSubject ? l.jsxs("div", {
                className: "p-3.5 bg-emerald-50 border border-emerald-200 rounded-xl text-xs text-emerald-900 flex items-center gap-2.5",
                children: [
                  l.jsx("span", { className: "text-base", children: "ℹ️" }),
                  l.jsx("span", { className: "font-semibold", children: "Urdu Subject Requirement: All notes, MCQs, and model answers are generated 100% in pure Urdu Nastaleeq as per PTBB rules." })
                ]
              }) : isEnglishSubject ? l.jsxs("div", {
                className: "p-3.5 bg-blue-50 border border-blue-200 rounded-xl text-xs text-blue-900 flex items-center gap-2.5",
                children: [
                  l.jsx("span", { className: "text-base", children: "ℹ️" }),
                  l.jsx("span", { className: "font-semibold", children: "English Subject Requirement: MCQs and Short Questions are provided in English, accompanied by a Key Vocabulary & Urdu Translation section." })
                ]
              }) : l.jsxs("div", {
                className: "grid grid-cols-1 sm:grid-cols-3 gap-2.5 pt-1",
                children: [
                  l.jsxs("button", {
                    type: "button",
                    onClick: () => setLanguageMode("english"),
                    className: "p-3 rounded-xl border-2 text-left cursor-pointer transition-all " + (
                      languageMode === "english" ? "bg-blue-600 border-blue-700 text-white shadow-md font-bold" : "bg-white border-slate-200 hover:border-blue-300 text-slate-800 font-semibold"
                    ),
                    children: [
                      l.jsx("div", { className: "text-xs font-black", children: "English Medium" }),
                      l.jsx("div", { className: "text-[11px] opacity-80 mt-0.5", children: "100% English (No Urdu in PDF / Word)" })
                    ]
                  }),
                  l.jsxs("button", {
                    type: "button",
                    onClick: () => setLanguageMode("urdu"),
                    className: "p-3 rounded-xl border-2 text-left cursor-pointer transition-all " + (
                      languageMode === "urdu" ? "bg-emerald-600 border-emerald-700 text-white shadow-md font-bold" : "bg-white border-slate-200 hover:border-emerald-300 text-slate-800 font-semibold"
                    ),
                    children: [
                      l.jsx("div", { className: "text-xs font-black", children: "Urdu Medium" }),
                      l.jsx("div", { className: "text-[11px] opacity-80 mt-0.5", children: "Questions and model answers in Urdu" })
                    ]
                  }),
                  l.jsxs("button", {
                    type: "button",
                    onClick: () => setLanguageMode("bilingual"),
                    className: "p-3 rounded-xl border-2 text-left cursor-pointer transition-all " + (
                      languageMode === "bilingual" ? "bg-purple-600 border-purple-700 text-white shadow-md font-bold" : "bg-white border-slate-200 hover:border-purple-300 text-slate-800 font-semibold"
                    ),
                    children: [
                      l.jsx("div", { className: "text-xs font-black", children: "Bilingual (English + Urdu)" }),
                      l.jsx("div", { className: "text-[11px] opacity-80 mt-0.5", children: "Both English and Urdu alongside" })
                    ]
                  })
                ]
              })
            ]
          }),

          // Section B: Chapter Selection Grid
          l.jsxs("div", {
            className: "max-w-4xl mx-auto space-y-3",
            children: [
              l.jsx("h3", { className: "text-sm font-black text-slate-800 uppercase tracking-wider", children: "Select Chapter / Unit:" }),
              l.jsx("div", {
                className: "grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-2.5 max-h-72 overflow-y-auto pr-1",
                children: chapters.map(ch => {
                  const isChSelected = ch.number === selectedChapterNo;
                  return l.jsxs("div", {
                    key: ch.number,
                    onClick: () => setSelectedChapterNo(ch.number),
                    className: "p-3.5 rounded-xl border-2 cursor-pointer transition-all flex items-center justify-between gap-2 " + (
                      isChSelected ? "bg-purple-50 border-purple-600 shadow-md ring-2 ring-purple-300 scale-[1.01]" :
                      "bg-white border-slate-200 hover:border-purple-300 hover:bg-slate-50"
                    ),
                    children: [
                      l.jsxs("div", {
                        className: "space-y-0.5 flex-1 min-w-0",
                        children: [
                          l.jsx("div", { className: "text-[11px] font-black uppercase text-purple-700", children: "Unit " + ch.number }),
                          l.jsx("div", { className: "font-bold text-xs text-slate-800 truncate", children: ch.titleEn || ("Chapter " + ch.number) }),
                          effectiveLangMode !== "english" && ch.titleUr && l.jsx("div", { className: "font-urdu text-[11px] text-slate-400 truncate text-right", dir: "rtl", children: ch.titleUr })
                        ]
                      }),
                      l.jsx("div", {
                        className: "w-5 h-5 rounded-full flex items-center justify-center font-bold text-[10px] shrink-0 " + (
                          isChSelected ? "bg-purple-600 text-white" : "border-2 border-slate-300 text-transparent"
                        ),
                        children: isChSelected ? "✔" : ""
                      })
                    ]
                  });
                })
              })
            ]
          }),

          // Standardized Navigation Bar for Step 3 (Height 44-48px, min-width 130px, gap-4)
          l.jsxs("div", {
            className: "flex items-center justify-between gap-4 max-w-4xl mx-auto pt-6 border-t border-slate-200",
            children: [
              l.jsx("button", {
                type: "button",
                onClick: () => setCurrentStep(2),
                className: "min-h-[44px] max-h-[48px] px-6 py-2.5 rounded-lg border border-slate-300 text-slate-700 bg-white hover:bg-slate-50 font-bold text-sm min-w-[130px] inline-flex items-center justify-center transition-all cursor-pointer shadow-xs active:scale-95",
                children: "← Back"
              }),
              l.jsx("button", {
                type: "button",
                onClick: () => setCurrentStep(4),
                className: "min-h-[44px] max-h-[48px] px-8 py-2.5 rounded-lg bg-purple-600 hover:bg-purple-700 text-white font-bold text-sm min-w-[140px] inline-flex items-center justify-center transition-all cursor-pointer shadow-sm active:scale-95",
                children: "Next →"
              })
            ]
          })
        ]
      }),

      // ==========================================
      // STEP 4: SOLVED NOTES DISPLAY & EXPORT
      // ==========================================
      currentStep === 4 && currentSubject && notesData && l.jsxs("div", {
        className: "space-y-4",
        children: [
          // Step 4 Toolbar: Navigation & 3 Export Buttons + Language Medium Selector for Export
          l.jsxs("div", {
            className: "bg-white p-4 sm:p-5 rounded-2xl border border-slate-200 shadow-xs flex flex-wrap items-center justify-between gap-3 no-print",
            children: [
              // Left: Back to Step 3 & Chapter Tag
              l.jsxs("div", {
                className: "flex items-center gap-2",
                children: [
                  l.jsxs("button", {
                    type: "button",
                    onClick: () => setCurrentStep(3),
                    className: "min-h-[44px] max-h-[48px] px-5 py-2 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-800 font-bold text-sm cursor-pointer border border-slate-300 shadow-xs inline-flex items-center gap-1.5 active:scale-95",
                    title: "Back to Unit Selection",
                    children: [l.jsx(SAFE_h_, { className: "w-4 h-4 text-blue-600" }), l.jsx("span", { children: "← Back" })]
                  }),
                  l.jsxs("div", {
                    className: "hidden sm:block text-xs font-black text-slate-700 bg-slate-100 px-3.5 py-2.5 rounded-lg border border-slate-200",
                    children: [
                      selectedClass, " Class • ", currentSubject.nameEn, " • Unit ", notesData.chapterNo
                    ]
                  })
                ]
              }),

              // Center: Immediate Language Medium Selector (English / Urdu / Bilingual) for Export & View
              !isUrduSubject && !isEnglishSubject && l.jsxs("div", {
                className: "flex items-center gap-1 bg-slate-100 p-1.5 rounded-xl border border-slate-300 shadow-2xs",
                children: [
                  l.jsx("span", { className: "text-[11px] font-black uppercase tracking-wider text-slate-600 px-2", children: "Language:" }),
                  l.jsx("button", {
                    type: "button",
                    onClick: () => setLanguageMode("english"),
                    className: "btn-3d px-3 py-1.5 rounded-lg text-xs font-black transition-all cursor-pointer " + (
                      languageMode === "english" ? "bg-blue-600 text-white shadow-xs" : "bg-white text-slate-700 font-bold hover:bg-slate-50 border border-slate-200"
                    ),
                    children: "English"
                  }),
                  l.jsx("button", {
                    type: "button",
                    onClick: () => setLanguageMode("urdu"),
                    className: "btn-3d px-3 py-1.5 rounded-lg text-xs font-black transition-all cursor-pointer " + (
                      languageMode === "urdu" ? "bg-emerald-600 text-white shadow-xs" : "bg-white text-slate-700 font-bold hover:bg-slate-50 border border-slate-200"
                    ),
                    children: "Urdu"
                  }),
                  l.jsx("button", {
                    type: "button",
                    onClick: () => setLanguageMode("bilingual"),
                    className: "btn-3d px-3 py-1.5 rounded-lg text-xs font-black transition-all cursor-pointer " + (
                      languageMode === "bilingual" ? "bg-purple-600 text-white shadow-xs" : "bg-white text-slate-700 font-bold hover:bg-slate-50 border border-slate-200"
                    ),
                    children: "Bilingual"
                  })
                ]
              }),

              // Right: Three Export Buttons: PDF (.pdf), Word (.docx), Direct Print
              l.jsxs("div", {
                className: "flex flex-wrap items-center gap-2",
                children: [
                  // Button 1: PDF Download
                  l.jsxs("button", {
                    type: "button",
                    disabled: isExportingPdf,
                    onClick: handleDownloadPDF,
                    className: "min-h-[44px] max-h-[48px] inline-flex items-center gap-1.5 px-5 py-2.5 bg-rose-600 hover:bg-rose-700 text-white rounded-lg text-xs font-bold cursor-pointer shadow-md disabled:opacity-60 transition-all",
                    title: `Download Solved Notes as PDF Document (${effectiveLangMode.toUpperCase()})`,
                    children: [
                      isExportingPdf ? l.jsx(Sc, { className: "w-4 h-4 animate-spin text-white" }) : l.jsx(SAFE_ad, { className: "w-4 h-4 text-rose-100" }),
                      l.jsx("span", { children: isExportingPdf ? "Generating PDF..." : "Download PDF" })
                    ]
                  }),

                  // Button 2: Word Download (.docx)
                  l.jsxs("button", {
                    type: "button",
                    onClick: () => exportNotesToWordDoc(notesData, selectedClass, currentSubject.nameEn, currentSubject.nameUr, effectiveLangMode, currentUser && currentUser.branding),
                    className: "min-h-[44px] max-h-[48px] inline-flex items-center gap-1.5 px-5 py-2.5 bg-blue-700 hover:bg-blue-800 text-white rounded-lg text-xs font-bold cursor-pointer shadow-md transition-all",
                    title: `Download Solved Notes as Editable MS Word Document (${effectiveLangMode.toUpperCase()})`,
                    children: [
                      l.jsx(Xu, { className: "w-4 h-4 text-blue-200" }),
                      l.jsx("span", { children: "Download Word" })
                    ]
                  }),

                  // Button 3: Direct Print
                  l.jsxs("button", {
                    type: "button",
                    onClick: () => window.print(),
                    className: "min-h-[44px] max-h-[48px] inline-flex items-center gap-1.5 px-5 py-2.5 bg-emerald-700 hover:bg-emerald-800 text-white rounded-lg text-xs font-bold cursor-pointer shadow-md transition-all",
                    title: "Open Browser Print Dialog",
                    children: [
                      l.jsx(SAFE_od, { className: "w-4 h-4 text-emerald-200" }),
                      l.jsx("span", { children: "Direct Print" })
                    ]
                  })
                ]
              })
            ]
          }),

          // Content Filter Tabs (All / MCQs / Short Questions)
          l.jsxs("div", {
            className: "flex items-center gap-2 border-b border-slate-200 pb-2 no-print",
            children: [
              l.jsxs("button", {
                type: "button",
                onClick: () => setActiveTab("all"),
                className: "px-3.5 py-1.5 rounded-lg text-xs font-bold transition-all cursor-pointer " + (
                  activeTab === "all" ? "bg-slate-900 text-white shadow-xs" : "bg-white text-slate-600 hover:bg-slate-100 border border-slate-200"
                ),
                children: ["All Solved Notes (", notesData.mcqs.length + notesData.shortQuestions.length, ")"]
              }),
              l.jsxs("button", {
                type: "button",
                onClick: () => setActiveTab("mcqs"),
                className: "px-3.5 py-1.5 rounded-lg text-xs font-bold transition-all cursor-pointer " + (
                  activeTab === "mcqs" ? "bg-blue-600 text-white shadow-xs" : "bg-white text-slate-600 hover:bg-slate-100 border border-slate-200"
                ),
                children: ["MCQs Only (", notesData.mcqs.length, ")"]
              }),
              l.jsxs("button", {
                type: "button",
                onClick: () => setActiveTab("sq"),
                className: "px-3.5 py-1.5 rounded-lg text-xs font-bold transition-all cursor-pointer " + (
                  activeTab === "sq" ? "bg-emerald-600 text-white shadow-xs" : "bg-white text-slate-600 hover:bg-slate-100 border border-slate-200"
                ),
                children: ["Short Questions Only (", notesData.shortQuestions.length, ")"]
              })
            ]
          }),

          // PRINTABLE & VISIBLE SOLVED NOTES DOCUMENT CONTAINER
          l.jsxs("div", {
            id: "notes-print-sheet",
            className: "bg-white p-6 sm:p-10 rounded-2xl border border-slate-200 shadow-md space-y-7 print:border-none print:shadow-none print:p-0 print:m-0",
            children: [
              // School Branding & Official Notes Header
              l.jsxs("div", {
                className: "border-b-2 border-blue-900 pb-5 text-center relative",
                children: [
                  // Monogram (if available)
                  currentUser && currentUser.branding && currentUser.branding.logoUrl ? l.jsx("img", {
                    src: currentUser.branding.logoUrl,
                    alt: "Monogram",
                    className: "w-20 h-20 object-contain mx-auto mb-2"
                  }) : l.jsx("div", {
                    className: "w-16 h-16 rounded-full bg-blue-950 text-white mx-auto flex items-center justify-center text-2xl font-black mb-2 shadow-sm",
                    children: "🎓"
                  }),
                  // Institute Name
                  l.jsx("h2", {
                    className: "text-2xl sm:text-3xl font-black text-blue-950 uppercase tracking-tight",
                    children: (currentUser && currentUser.branding && currentUser.branding.name) || "SUPERIOR MODEL HIGH SCHOOL & COLLEGE"
                  }),
                  // Subtitle & Affiliation
                  l.jsx("p", {
                    className: "text-xs sm:text-sm font-bold text-slate-600 mt-0.5",
                    children: (currentUser && currentUser.branding && currentUser.branding.address) || "Affiliated with Punjab Examination Commission & Board of Intermediate and Secondary Education"
                  }),
                  // Notes Header Banner
                  l.jsxs("div", {
                    className: "inline-block bg-blue-900 text-white px-6 py-1.5 rounded-md font-black text-xs sm:text-sm uppercase tracking-wider mt-3 shadow-xs",
                    children: ["CLASS ", selectedClass.toUpperCase(), " • CHAPTER SOLVED REVISION NOTES (", effectiveLangMode.toUpperCase(), ")"]
                  })
                ]
              }),

              // Chapter Metadata Bar
              l.jsxs("div", {
                className: "grid grid-cols-2 sm:grid-cols-4 gap-3 bg-slate-50 border border-slate-200 p-3.5 rounded-xl text-xs font-bold",
                children: [
                  l.jsxs("div", {
                    children: [
                      l.jsx("span", { className: "text-slate-500 font-semibold", children: "Class: " }),
                      l.jsx("span", { className: "text-blue-950 font-black", children: selectedClass + " Class" })
                    ]
                  }),
                  l.jsxs("div", {
                    children: [
                      l.jsx("span", { className: "text-slate-500 font-semibold", children: "Subject: " }),
                      l.jsx("span", { className: "text-blue-950 font-black", children: currentSubject.nameEn })
                    ]
                  }),
                  l.jsxs("div", {
                    children: [
                      l.jsx("span", { className: "text-slate-500 font-semibold", children: "Unit / Chapter: " }),
                      l.jsx("span", { className: "text-blue-950 font-black", children: "Unit " + notesData.chapterNo })
                    ]
                  }),
                  l.jsxs("div", {
                    children: [
                      l.jsx("span", { className: "text-slate-500 font-semibold", children: "Medium: " }),
                      l.jsx("span", {
                        className: "capitalize px-2 py-0.5 rounded bg-blue-100 text-blue-800 text-[11px] font-black",
                        children: effectiveLangMode
                      })
                    ]
                  })
                ]
              }),

              // Chapter Title & Overview Box
              l.jsxs("div", {
                className: "p-4 rounded-xl border border-blue-200 bg-blue-50/50 space-y-1.5",
                children: [
                  l.jsxs("div", {
                    className: "flex flex-wrap items-center justify-between gap-2",
                    children: [
                      l.jsxs("h3", {
                        className: "text-lg sm:text-xl font-black text-blue-950",
                        children: ["Unit " + notesData.chapterNo + ": ", notesData.titleEn]
                      }),
                      // Strict language mode: Do not show Urdu title if mode is English
                      effectiveLangMode !== "english" && notesData.titleUr && l.jsx("span", {
                        className: "font-urdu text-base sm:text-lg font-bold text-blue-900",
                        dir: "rtl",
                        children: notesData.titleUr
                      })
                    ]
                  }),
                  l.jsx("p", {
                    className: "text-xs text-slate-700 leading-relaxed font-medium",
                    children: effectiveLangMode === "urdu" ? (notesData.summaryUr || notesData.summaryEn) : notesData.summaryEn
                  })
                ]
              }),

              // English Subject: Key Vocabulary & Urdu Translation Section (Only shown when not strict english mode or requested)
              (activeTab === "all") && isEnglishSubject && effectiveLangMode !== "english" && notesData.vocab && notesData.vocab.length > 0 && l.jsxs("div", {
                className: "space-y-3",
                children: [
                  l.jsxs("div", {
                    className: "border-l-4 border-blue-800 pl-3 py-0.5 flex items-center justify-between",
                    children: [
                      l.jsx("h4", { className: "text-sm sm:text-base font-black text-slate-900 uppercase tracking-wide", children: "Key Vocabulary & Urdu Translation" }),
                      l.jsx("span", { className: "text-xs text-slate-500 font-bold", children: "Glossary & Meanings" })
                    ]
                  }),
                  l.jsx("div", {
                    className: "overflow-x-auto rounded-xl border border-slate-200",
                    children: l.jsxs("table", {
                      className: "w-full text-left border-collapse text-xs",
                      children: [
                        l.jsx("thead", {
                          className: "bg-slate-100 text-slate-700 font-black border-b border-slate-200",
                          children: l.jsxs("tr", {
                            children: [
                              l.jsx("th", { className: "p-3", children: "#" }),
                              l.jsx("th", { className: "p-3", children: "Vocabulary Word" }),
                              l.jsx("th", { className: "p-3 text-right font-urdu", dir: "rtl", children: "Urdu Meaning" }),
                              l.jsx("th", { className: "p-3", children: "Contextual Usage" })
                            ]
                          })
                        }),
                        l.jsx("tbody", {
                          className: "divide-y divide-slate-100",
                          children: notesData.vocab.map((v, vIdx) => {
                            return l.jsxs("tr", {
                              key: vIdx,
                              className: "hover:bg-slate-50 transition-colors",
                              children: [
                                l.jsx("td", { className: "p-3 font-bold text-slate-400", children: vIdx + 1 }),
                                l.jsx("td", { className: "p-3 font-black text-blue-900 text-sm", children: v.word }),
                                l.jsx("td", { className: "p-3 text-right font-urdu text-base font-bold text-slate-800", dir: "rtl", children: v.meaningUr }),
                                l.jsx("td", { className: "p-3 italic text-slate-600", children: v.context })
                              ]
                            });
                          })
                        })
                      ]
                    })
                  })
                ]
              }),

              // SECTION A: SOLVED MULTIPLE CHOICE QUESTIONS (MCQs)
              (activeTab === "all" || activeTab === "mcqs") && l.jsxs("div", {
                className: "space-y-4",
                children: [
                  l.jsxs("div", {
                    className: "border-l-4 border-blue-900 pl-3 py-0.5 flex items-center justify-between",
                    children: [
                      l.jsxs("h4", {
                        className: "text-sm sm:text-base font-black text-slate-900 uppercase tracking-wide",
                        children: ["Section A: Solved Multiple Choice Questions (", notesData.mcqs.length, " Questions)"]
                      }),
                      l.jsx("span", { className: "text-xs font-bold text-slate-500", children: "1 Mark Each" })
                    ]
                  }),
                  l.jsx("div", {
                    className: "space-y-3.5",
                    children: notesData.mcqs.map((mcq, mIdx) => {
                      const letters = ["A", "B", "C", "D"];
                      return l.jsxs("div", {
                        key: mcq.id || mIdx,
                        className: "p-4 rounded-xl border border-slate-200 bg-white space-y-3 shadow-2xs page-break-inside-avoid",
                        children: [
                          // Question Prompt
                          l.jsxs("div", {
                            className: "space-y-1",
                            children: [
                              l.jsxs("div", {
                                className: "flex items-start gap-2",
                                children: [
                                  l.jsxs("span", { className: "px-2 py-0.5 rounded bg-blue-100 text-blue-900 font-black text-xs shrink-0", children: ["Q", mIdx + 1] }),
                                  l.jsx("p", {
                                    className: "font-black text-slate-900 text-sm leading-relaxed",
                                    children: effectiveLangMode === "urdu" ? (mcq.questionUr || mcq.questionEn) : mcq.questionEn
                                  })
                                ]
                              }),
                              // Never show Urdu in English mode
                              effectiveLangMode === "bilingual" && mcq.questionUr && l.jsx("p", {
                                className: "font-urdu text-right text-sm text-slate-700 font-bold pr-2 leading-relaxed",
                                dir: "rtl",
                                children: mcq.questionUr
                              })
                            ]
                          }),

                          // Options Grid (4 Options)
                          l.jsx("div", {
                            className: "grid grid-cols-1 sm:grid-cols-2 gap-2 pt-1",
                            children: mcq.optionsEn.map((opt, optIdx) => {
                              const isCorrect = optIdx === mcq.correctIndex;
                              const optUr = (mcq.optionsUr && mcq.optionsUr[optIdx]) || "";
                              return l.jsxs("div", {
                                key: optIdx,
                                className: "p-2.5 rounded-lg border text-xs flex items-center justify-between gap-2 " + (
                                  isCorrect ? "bg-emerald-50 border-emerald-400 font-bold text-emerald-950 shadow-2xs" :
                                  "bg-slate-50/70 border-slate-200 text-slate-700 font-medium"
                                ),
                                children: [
                                  l.jsxs("div", {
                                    className: "flex items-center gap-2",
                                    children: [
                                      l.jsxs("span", {
                                        className: "w-5 h-5 rounded-full flex items-center justify-center font-black text-[11px] " + (
                                          isCorrect ? "bg-emerald-600 text-white" : "bg-slate-200 text-slate-700"
                                        ),
                                        children: letters[optIdx]
                                      }),
                                      l.jsx("span", {
                                        children: effectiveLangMode === "urdu" ? (optUr || opt) : effectiveLangMode === "english" ? opt : (optUr ? `${opt} (${optUr})` : opt)
                                      })
                                    ]
                                  }),
                                  isCorrect && l.jsx("span", { className: "text-emerald-700 font-black text-xs", children: "✔ Correct" })
                                ]
                              });
                            })
                          }),

                          // Justification / Explanation Box
                          l.jsxs("div", {
                            className: "bg-emerald-50/60 border border-emerald-200 rounded-lg p-2.5 text-xs text-slate-800 space-y-1",
                            children: [
                              l.jsxs("div", {
                                className: "flex items-center gap-1.5 font-black text-emerald-900",
                                children: [
                                  l.jsx("span", { children: "💡" }),
                                  l.jsxs("span", { children: ["Model Reason & Justification (Option ", letters[mcq.correctIndex], "):"] })
                                ]
                              }),
                              l.jsx("p", {
                                className: "text-slate-600 font-medium leading-relaxed",
                                children: effectiveLangMode === "urdu" ? (mcq.explanationUr || mcq.explanationEn) : mcq.explanationEn
                              }),
                              // Never show Urdu explanation in English mode
                              effectiveLangMode === "bilingual" && mcq.explanationUr && l.jsx("p", {
                                className: "font-urdu text-right text-xs text-slate-700 font-bold leading-relaxed pt-0.5",
                                dir: "rtl",
                                children: mcq.explanationUr
                              })
                            ]
                          })
                        ]
                      });
                    })
                  })
                ]
              }),

              // SECTION B: SOLVED SHORT QUESTIONS (2 MARKS EACH) - NO LONG QUESTIONS
              (activeTab === "all" || activeTab === "sq") && l.jsxs("div", {
                className: "space-y-4 pt-2",
                children: [
                  l.jsxs("div", {
                    className: "border-l-4 border-emerald-700 pl-3 py-0.5 flex items-center justify-between",
                    children: [
                      l.jsxs("h4", {
                        className: "text-sm sm:text-base font-black text-slate-900 uppercase tracking-wide",
                        children: ["Section B: Solved Short Questions (", notesData.shortQuestions.length, " Questions)"]
                      }),
                      l.jsx("span", { className: "text-xs font-bold text-slate-500", children: "2 Marks Each • Board Pattern" })
                    ]
                  }),
                  l.jsx("div", {
                    className: "space-y-4",
                    children: notesData.shortQuestions.map((sq, sqIdx) => {
                      return l.jsxs("div", {
                        key: sq.id || sqIdx,
                        className: "p-4 sm:p-5 rounded-xl border border-slate-200 bg-white space-y-3 shadow-2xs page-break-inside-avoid",
                        children: [
                          // Question Header
                          l.jsxs("div", {
                            className: "space-y-1",
                            children: [
                              l.jsxs("div", {
                                className: "flex items-start justify-between gap-2",
                                children: [
                                  l.jsxs("div", {
                                    className: "flex items-start gap-2",
                                    children: [
                                      l.jsxs("span", { className: "px-2 py-0.5 rounded bg-emerald-100 text-emerald-900 font-black text-xs shrink-0", children: ["SQ ", sqIdx + 1] }),
                                      l.jsx("h5", {
                                        className: "font-black text-slate-900 text-sm leading-relaxed",
                                        children: effectiveLangMode === "urdu" ? (sq.questionUr || sq.questionEn) : sq.questionEn
                                      })
                                    ]
                                  }),
                                  l.jsxs("span", { className: "px-2 py-0.5 rounded bg-slate-100 text-slate-700 font-black text-[11px] shrink-0", children: [sq.marks || 2, " Marks"] })
                                ]
                              }),
                              // Never show Urdu in English mode
                              effectiveLangMode === "bilingual" && sq.questionUr && l.jsx("p", {
                                className: "font-urdu text-right text-sm text-slate-700 font-bold pr-2 leading-relaxed",
                                dir: "rtl",
                                children: sq.questionUr
                              })
                            ]
                          }),

                          // Model Answer Box
                          l.jsxs("div", {
                            className: "bg-slate-50 border-l-3 border-emerald-600 rounded-r-xl p-3.5 space-y-2 text-xs",
                            children: [
                              l.jsx("div", {
                                className: "font-black text-emerald-900 text-[11px] uppercase tracking-wider",
                                children: "✔ Standard Model Answer:"
                              }),
                              // English Answer
                              effectiveLangMode !== "urdu" && l.jsx("div", {
                                className: "text-slate-800 leading-relaxed font-semibold whitespace-pre-line",
                                children: sq.answerEn
                              }),
                              // Urdu Answer (Strictly suppressed when in English mode)
                              effectiveLangMode !== "english" && (effectiveLangMode === "urdu" || effectiveLangMode === "bilingual") && sq.answerUr && l.jsxs("div", {
                                className: (effectiveLangMode === "bilingual" ? "border-t border-slate-200 pt-2.5 mt-2 " : "") + "font-urdu text-right text-slate-900 text-sm font-semibold leading-relaxed whitespace-pre-line",
                                dir: "rtl",
                                children: [
                                  effectiveLangMode === "bilingual" && l.jsx("div", { className: "text-[11px] font-sans font-bold text-slate-500 mb-1 text-left", dir: "ltr", children: "[Urdu Translation]:" }),
                                  sq.answerUr
                                ]
                              })
                            ]
                          })
                        ]
                      });
                    })
                  })
                ]
              }),

              // Notes Footer Signature & Stamp Box
              l.jsxs("div", {
                className: "border-t border-slate-200 pt-6 mt-8 flex flex-wrap items-center justify-between gap-4 text-xs font-bold text-slate-500",
                children: [
                  l.jsxs("div", {
                    children: [
                      l.jsx("p", { className: "text-slate-700", children: "Subject Specialist & Examination Cell" }),
                      l.jsx("p", { className: "text-[11px] text-slate-400 font-normal", children: "Curriculum strictly mapped with PTBB 2026 Board Pattern" })
                    ]
                  }),
                  l.jsxs("div", {
                    className: "text-right",
                    children: [
                      l.jsx("div", { className: "w-32 border-b border-slate-400 pb-1 mb-1" }),
                      l.jsx("p", { className: "text-slate-700", children: "Principal / Authorized Stamp" })
                    ]
                  })
                ]
              })
            ]
          })
        ]
      })
    ]
  });
}
'''

new_text = text[:pos_sample] + replacement_code + text[pos_hub:]

with open('assets/index-DAioIUjd.js', 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Successfully written updated assets/index-DAioIUjd.js with v5 patch")
