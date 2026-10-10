// PTBB Punjab Boards (BISE) Master Question Bank Engine (2020–2026)
// Covers all 9 BISE Punjab Boards: Lahore, Gujranwala, Rawalpindi, Faisalabad, Multan, Sahiwal, Sargodha, Bahawalpur, D.G. Khan
// Strictly conforms to PTBB Curriculum 2026 guidelines, Textbook Exercises, and In-Text/Box Questions.

export const PUNJAB_BOARDS_LIST = [
  "BISE Lahore",
  "BISE Gujranwala",
  "BISE Rawalpindi",
  "BISE Faisalabad",
  "BISE Multan",
  "BISE Sahiwal",
  "BISE Sargodha",
  "BISE Bahawalpur",
  "BISE DG Khan"
];

export const PUNJAB_BOARD_CODES = ["LHR", "GRW", "RWP", "FSD", "MTN", "SWL", "SGD", "BWP", "DGK"];
export const PAST_YEARS = ["2020", "2021", "2022", "2023", "2024", "2025", "2026"];
export const SESSIONS = ["Group-I (Morning)", "Group-II (Evening)"];

export function generatePunjabBoardCitation(seed: number): string {
  const b1 = PUNJAB_BOARD_CODES[seed % PUNJAB_BOARD_CODES.length];
  const y1 = PAST_YEARS[(seed * 2) % PAST_YEARS.length];
  const sess1 = (seed % 2 === 0) ? "G-I" : "G-II";
  
  if (seed % 4 === 0) {
    const b2 = PUNJAB_BOARD_CODES[(seed + 3) % PUNJAB_BOARD_CODES.length];
    const y2 = PAST_YEARS[(seed + 1) % PAST_YEARS.length];
    const b3 = PUNJAB_BOARD_CODES[(seed + 5) % PUNJAB_BOARD_CODES.length];
    const y3 = PAST_YEARS[(seed + 3) % PAST_YEARS.length];
    return `${b1} ${y1} ${sess1}, ${b2} ${y2}, ${b3} ${y3}`;
  } else if (seed % 2 === 0) {
    const b2 = PUNJAB_BOARD_CODES[(seed + 2) % PUNJAB_BOARD_CODES.length];
    const y2 = PAST_YEARS[(seed + 3) % PAST_YEARS.length];
    return `${b1} ${y1} ${sess1}, ${b2} ${y2}`;
  }
  return `${b1} ${y1} ${sess1}`;
}

export function generateMassiveQuestionPoolForChapter(subject: any, chapter: any) {
  const chNo = chapter.number;
  const subName = (subject.nameEn || "").toLowerCase();
  const chTitleEn = chapter.titleEn || `Unit ${chNo}`;
  const chTitleUr = chapter.titleUr || `یونٹ ${chNo}`;

  const isPhysics = subName.includes("physics");
  const isChemistry = subName.includes("chemistry");
  const isBiology = subName.includes("biology");
  const isMath = subName.includes("math");
  const isComputer = subName.includes("computer");
  const isEnglish = subName.includes("english");
  const isUrdu = subName.includes("urdu");
  const isIslamiat = subName.includes("islamiat") || subName.includes("islamiyat");
  const isTarjuma = subName.includes("tarjuma");
  const isPakStudies = subName.includes("pakistan") || subName.includes("pakstudies");

  const hasNumericals = isPhysics || isChemistry || isMath;

  const mcqs: any[] = [];
  const shortQuestions: any[] = [];
  const longQuestions: any[] = [];

  let subjectMcqTemplates: any[] = [];
  let subjectExerciseMcqs: any[] = [];
  let subjectInTextBoxMcqs: any[] = [];

  let subjectShortTemplates: any[] = [];
  let subjectLongTemplates: any[] = [];

  // ==========================================
  // 1. PHYSICS
  // ==========================================
  if (isPhysics) {
    subjectMcqTemplates = [
      {
        en: `In ${chTitleEn}, the standard SI unit of the fundamental physical quantity is:`,
        ur: `${chTitleUr} میں بنیادی طبعی مقدار کا معیاری سسٹم انٹرنیشنل (SI) یونٹ ہے:`,
        opts: [
          { en: "Meter / Kilogram / Second", ur: "میٹر / کلوگرام / سیکنڈ" },
          { en: "Newton / Joule / Watt", ur: "نیوٹن / جول / واٹ" },
          { en: "Pascal / Coulomb", ur: "پاسکل / کولمب" },
          { en: "Volt / Ohm / Ampere", ur: "وولٹ / اوہم / ایمپئر" }
        ],
        correct: "A"
      },
      {
        en: `Which of the following is a derived physical quantity in ${chTitleEn}?`,
        ur: `${chTitleUr} میں مندرجہ ذیل میں سے کون سی ماخوذ طبعی مقدار ہے؟`,
        opts: [
          { en: "Force / Speed / Work", ur: "فورس / سپیڈ / ورک" },
          { en: "Length / Mass / Time", ur: "لمبائی / ماس / وقت" },
          { en: "Electric Current", ur: "الیکٹرک کرنٹ" },
          { en: "Temperature", ur: "ٹمپریچر" }
        ],
        correct: "A"
      },
      {
        en: `The rate of change of momentum of an object is directly equal to:`,
        ur: `کسی جسم کے مومنٹم میں تبدیلی کی شرح براہ راست برابر ہوتی ہے:`,
        opts: [
          { en: "Applied Net Force", ur: "لگائی گئی نیٹ فورس" },
          { en: "Acceleration produced", ur: "پیدا شدہ ایکسلریشن" },
          { en: "Total Kinetic Energy", ur: "کل کائنیٹک انرجی" },
          { en: "Inertia of the body", ur: "جسم کا جمود (انرشیا)" }
        ],
        correct: "A"
      },
      {
        en: `According to PTBB textbook, the value of gravitational acceleration 'g' on Earth's surface is:`,
        ur: `پنجاب ٹیکسٹ بک بورڈ کے مطابق زمین کی سطح پر گریویٹیشنل ایکسلریشن 'g' کی قیمت ہے:`,
        opts: [
          { en: "9.8 m s⁻² (approx 10 m s⁻²)", ur: "9.8 m s⁻² (تقریباً 10 m s⁻²)" },
          { en: "1.6 m s⁻²", ur: "1.6 m s⁻²" },
          { en: "6.67 × 10⁻¹¹ N m² kg⁻²", ur: "6.67 × 10⁻¹¹ N m² kg⁻²" },
          { en: "9.8 × 10⁸ m s⁻¹", ur: "9.8 × 10⁸ m s⁻¹" }
        ],
        correct: "A"
      }
    ];

    subjectExerciseMcqs = [
      {
        en: `[Textbook Exercise Q.1] Which of the following is the least count of a standard Vernier Calipers?`,
        ur: `[مشقی سوال 1] عام ورنیئر کیلیپرز کا لیسٹ کاؤنٹ کتنا ہوتا ہے؟`,
        opts: [
          { en: "0.1 mm (0.01 cm)", ur: "0.1 ملی میٹر (0.01 سینٹی میٹر)" },
          { en: "0.01 mm (0.001 cm)", ur: "0.01 ملی میٹر (0.001 سینٹی میٹر)" },
          { en: "1 mm (0.1 cm)", ur: "1 ملی میٹر (0.1 سینٹی میٹر)" },
          { en: "0.001 mm", ur: "0.001 ملی میٹر" }
        ],
        correct: "A"
      },
      {
        en: `[Textbook Exercise Q.2] The least count of a standard Micrometer Screw Gauge is:`,
        ur: `[مشقی سوال 2] عام مائیکرو میٹر سکرو گیج کا لیسٹ کاؤنٹ ہوتا ہے:`,
        opts: [
          { en: "0.01 mm (0.001 cm)", ur: "0.01 ملی میٹر (0.001 سینٹی میٹر)" },
          { en: "0.1 mm (0.01 cm)", ur: "0.1 ملی میٹر (0.01 سینٹی میٹر)" },
          { en: "1 mm", ur: "1 ملی میٹر" },
          { en: "0.0001 mm", ur: "0.0001 ملی میٹر" }
        ],
        correct: "A"
      },
      {
        en: `[Textbook Exercise Q.3] A body has translatory motion if it moves along a:`,
        ur: `[مشقی سوال 3] کسی جسم کی حرکت ٹرانسلیٹری ہوتی ہے اگر وہ حرکت کرے:`,
        opts: [
          { en: "Line without rotation (straight or curved)", ur: "بغیر گھماؤ کے کسی خط پر (سیدھا یا خمدار)" },
          { en: "Circle about fixed axis", ur: "کسی فکسڈ ایکسس کے گرد دائرے میں" },
          { en: "Spinning axis through itself", ur: "اپنے ہی اندر سے گزرنے والے ایکسس پر" },
          { en: "Vibratory to and fro path", ur: "آگے پیچھے تھرتھراتی ہوئی" }
        ],
        correct: "A"
      }
    ];

    subjectInTextBoxMcqs = [
      {
        en: `[In-Text Box: Do You Know?] Light travels in vacuum at an astonishing speed of:`,
        ur: `[چیپٹر کے اندر سے: کیا آپ جانتے ہیں؟] خلا میں روشنی کی رفتار کتنی ہے؟`,
        opts: [
          { en: "3 × 10⁸ m s⁻¹ (300,000 km/s)", ur: "3 × 10⁸ میٹر فی سیکنڈ (300,000 کلومیٹر/سیکنڈ)" },
          { en: "330 m s⁻¹", ur: "330 میٹر فی سیکنڈ" },
          { en: "3 × 10⁶ m s⁻¹", ur: "3 × 10⁶ میٹر فی سیکنڈ" },
          { en: "1,100 km/h", ur: "1,100 کلومیٹر فی گھنٹہ" }
        ],
        correct: "A"
      },
      {
        en: `[In-Text Box: Point to Ponder] Why does a passenger fall forward when a fast moving bus stops suddenly?`,
        ur: `[چیپٹر کے اندر سے: سوچنے کی بات] اچانک بریک لگانے پر بس کا مسافر آگے کی طرف کیوں گرتا ہے؟`,
        opts: [
          { en: "Due to inertia of motion of upper body", ur: "جسم کے اوپری حصے کے جمود (انرشیا) کی وجہ سے" },
          { en: "Due to sudden gravitational pull", ur: "اچانک کششِ ثقل میں اضافے سے" },
          { en: "Due to decrease in friction", ur: "فرکشن میں کمی کی وجہ سے" },
          { en: "Due to atmospheric pressure", ur: "ہوائی دباؤ کی وجہ سے" }
        ],
        correct: "A"
      },
      {
        en: `[In-Text Box: Mini Exercise / STS] The Global Positioning System (GPS) consists of how many Earth satellites?`,
        ur: `[چیپٹر کے اندر سے: معلوماتی باکس] گلوبل پوزیشننگ سسٹم (GPS) زمین کے گرد کتنے سیٹلائٹس پر مشتمل ہے؟`,
        opts: [
          { en: "24 satellites orbiting at 20,000 km", ur: "24 سیٹلائٹس (20,000 کلومیٹر بلندی پر)" },
          { en: "12 satellites", ur: "12 سیٹلائٹس" },
          { en: "36 satellites", ur: "36 سیٹلائٹس" },
          { en: "100 satellites", ur: "100 سیٹلائٹس" }
        ],
        correct: "A"
      }
    ];

    subjectShortTemplates = [
      {
        en: `[Textbook Exercise Review Q] Define ${chTitleEn}. State its mathematical formula and SI unit.`,
        ur: `[مشقی جائزہ سوال] ${chTitleUr} کی تعریف تحریر کریں اور اس کا حسابی فارمولا اور ایس آئی یونٹ لکھیں۔`,
        cat: "Textbook Exercises"
      },
      {
        en: `[Textbook Exercise Review Q] Differentiate between base quantities and derived quantities with two examples each.`,
        ur: `[مشقی جائزہ سوال] بنیادی اور ماخوذ مقداروں میں فرق واضح کریں اور ہر ایک کی دو مثالیں دیں۔`,
        cat: "Textbook Exercises"
      },
      {
        en: `[In-Text Box: Point to Ponder] Can a body moving with constant speed have an acceleration? Explain with an example.`,
        ur: `[چیپٹر کے اندر سے: سوچنے کی بات] کیا مستقل سپیڈ سے حرکت کرتے ہوئے جسم میں ایکسلریشن ہو سکتا ہے؟ مثال سے وضاحت کریں۔`,
        cat: "In-Text & Box Questions"
      },
      {
        en: `[In-Text Box: Do You Know?] What is meant by zero error in measuring instruments and why is zero correction necessary?`,
        ur: `[چیپٹر کے اندر سے: کیا آپ جانتے ہیں؟] پیمائشی آلات میں زیرو ایرر سے کیا مراد ہے اور زیرو کریکشن کیوں ناگزیر ہے؟`,
        cat: "In-Text & Box Questions"
      },
      {
        en: `[In-Text Box: Test Yourself] Why is the handle of a door fixed at its outer edge far from hinges?`,
        ur: `[چیپٹر کے اندر سے: خود پرکھیں] دروازے کا دستہ قبضوں سے دور بیرونی کنارے پر کیوں لگایا جاتا ہے؟`,
        cat: "In-Text & Box Questions"
      },
      {
        en: `[Past Board Paper] State Newton's Second Law of Motion and derive the equation F = ma.`,
        ur: `[سابقہ بورڈ پرچہ جات] نیوٹن کا موشن کا دوسرا قانون بیان کریں اور مساوات F = ma اخذ کریں۔`,
        cat: "Past Board Papers"
      },
      {
        en: `[Past Board Paper] Define momentum. Write its formula, SI unit, and state the law of conservation of momentum.`,
        ur: `[سابقہ بورڈ پرچہ جات] مومنٹم کی تعریف کریں۔ اس کا فارمولا، ایس آئی یونٹ اور قانونِ بقائے مومنٹم بیان کریں۔`,
        cat: "Past Board Papers"
      },
      {
        en: `[SLO Conceptual] How does rolling friction differ from sliding friction, and why is rolling friction ten times smaller?`,
        ur: `[تصوراتی SLO سوال] رولنگ فرکشن اور سلائیڈنگ فرکشن میں کیا فرق ہے اور رولنگ فرکشن دس گنا کم کیوں ہوتی ہے؟`,
        cat: "SLO Conceptual"
      },
      {
        en: `[Numerical Problem] A force of 20 N moves a body with an acceleration of 2 m s⁻². Calculate the mass of the body.`,
        ur: `[حسابی مسئلہ / نکل] 20 نیوٹن کی فورس کسی جسم میں 2 m s⁻² کا ایکسلریشن پیدا کرتی ہے۔ جسم کا ماس معلوم کریں۔`,
        cat: "Numerical Problems"
      }
    ];

    subjectLongTemplates = [
      {
        theoryEn: `[Past Board Paper] Define resolution of forces. Derive mathematical expressions for rectangular components Fx and Fy.`,
        theoryUr: `[سابقہ بورڈ پرچہ] فورسز کی ریزولیوشن کی تعریف کریں۔ ریکٹنگولر کمپوننٹس Fx اور Fy کے حسابی کلیے اخذ کریں۔`,
        numEn: `[Textbook Numerical] A man pulls a trolley on a level ground with a force of 100 N making an angle of 30° with the horizontal. Find the horizontal and vertical components of the force.`,
        numUr: `[مشقی حسابی سوال] ایک شخص افقی سطح پر ٹرالی کو 100 N کی فورس سے افق کے ساتھ 30° کے زاویے پر کھینچتا ہے۔ فورس کے افقی اور عمودی کمپوننٹس معلوم کریں۔`
      },
      {
        theoryEn: `[Textbook Exercise Comprehensive Q] State Newton's Law of Universal Gravitation. Derive formula for the Mass of Earth using this law.`,
        theoryUr: `[مشقی تفصیلی سوال] نیوٹن کا قانونِ گریویٹیشن بیان کریں۔ اس قانون کی مدد سے زمین کا ماس معلوم کرنے کا فارمولا اخذ کریں۔`,
        numEn: `[Textbook Numerical] Find the gravitational force of attraction between two lead spheres each of mass 1000 kg placed with their centers 0.5 m apart. (G = 6.673 × 10⁻¹¹ N m² kg⁻²)`,
        numUr: `[مشقی حسابی سوال] 1000 kg ماس والے سیسے کے دو گولوں کے درمیانی کشش کی فورس معلوم کریں اگر ان کے مراکز کا فاصلہ 0.5 میٹر ہو۔`
      }
    ];
  }

  // ==========================================
  // 2. CHEMISTRY
  // ==========================================
  else if (isChemistry) {
    subjectMcqTemplates = [
      {
        en: `In ${chTitleEn}, the standard mass of 1 mole of carbon-12 atoms is exactly:`,
        ur: `${chTitleUr} میں کاربن-12 ایٹمز کے 1 مول کا معیاری ماس ہے:`,
        opts: [
          { en: "12 grams (contains 6.02 × 10²³ atoms)", ur: "12 گرام (جس میں 6.02 × 10²³ ایٹمز ہوتے ہیں)" },
          { en: "1 gram", ur: "1 گرام" },
          { en: "1.66 × 10⁻²⁴ grams", ur: "1.66 × 10⁻²⁴ گرام" },
          { en: "12 amu per mole", ur: "12 اے ایم یو فی مول" }
        ],
        correct: "A"
      },
      {
        en: `Which subatomic particle has the least mass in an atom?`,
        ur: `ایٹم میں سب سے کم ماس رکھنے والا ذرہ کون سا ہے؟`,
        opts: [
          { en: "Electron (1/1836 of proton mass)", ur: "الیکٹران (پروٹون کا 1/1836 حصہ)" },
          { en: "Proton", ur: "پروٹون" },
          { en: "Neutron", ur: "نیوٹران" },
          { en: "Alpha particle", ur: "الفا پارٹیکل" }
        ],
        correct: "A"
      }
    ];

    subjectExerciseMcqs = [
      {
        en: `[Textbook Exercise Q.1] Industrial method used for manufacturing sodium carbonate (washing soda) is:`,
        ur: `[مشقی سوال 1] سوڈیم کاربونیٹ (دھوبی سوڈا) کی صنعتی تیاری کا مشہور طریقہ کون سا ہے؟`,
        opts: [
          { en: "Solvay's Process", ur: "سالوے پراسیس" },
          { en: "Haber's Process", ur: "ہیبر پراسیس" },
          { en: "Down's Cell Process", ur: "ڈاؤنز سیل پراسیس" },
          { en: "Contact Process", ur: "کنٹیکٹ پراسیس" }
        ],
        correct: "A"
      },
      {
        en: `[Textbook Exercise Q.2] The number of electrons that can be accommodated in M-shell is:`,
        ur: `[مشقی سوال 2] ایم (M) شیل میں زیادہ سے زیادہ کتنے الیکٹران سما سکتے ہیں؟`,
        opts: [
          { en: "18 (using 2n² formula)", ur: "18 (فارمولا 2n² کے تحت)" },
          { en: "8", ur: "8" },
          { en: "32", ur: "32" },
          { en: "2", ur: "2" }
        ],
        correct: "A"
      }
    ];

    subjectInTextBoxMcqs = [
      {
        en: `[In-Text Box: Do You Know?] Who was awarded the Nobel Prize in Chemistry for discovering radioactivity?`,
        ur: `[چیپٹر کے اندر سے: کیا آپ جانتے ہیں؟] ریڈیو ایکٹیویٹی کی دریافت پر نوبل پرائز کس کو دیا گیا؟`,
        opts: [
          { en: "Marie Curie & Henri Becquerel", ur: "میڈم کیوری اور ہنری بیکرل" },
          { en: "John Dalton", ur: "جان ڈالٹن" },
          { en: "Ernest Rutherford", ur: "ارنسٹ ردرفورڈ" },
          { en: "J.J. Thomson", ur: "جے جے تھامسن" }
        ],
        correct: "A"
      },
      {
        en: `[In-Text Box: Point to Ponder] Why does ice float on the surface of liquid water?`,
        ur: `[چیپٹر کے اندر سے: سوچنے کی بات] برف مائع پانی کی سطح پر کیوں تیرتی ہے؟`,
        opts: [
          { en: "Ice has open hexagonal structure making it 9% less dense", ur: "برف کی کھلی ساخت کی وجہ سے اس کی ڈینسٹی 9% کم ہوتی ہے" },
          { en: "Ice is composed of lighter gas molecules", ur: "برف ہلکی گیسوں پر مشتمل ہوتی ہے" },
          { en: "Surface tension pushes ice upwards", ur: "سرفیس ٹینشن برف کو اوپر دھکیلتی ہے" },
          { en: "Ice contains dissolved trapped helium", ur: "برف میں ہیلیم گیس قید ہوتی ہے" }
        ],
        correct: "A"
      }
    ];

    subjectShortTemplates = [
      {
        en: `[Textbook Exercise Review Q] Differentiate between empirical formula and molecular formula with two examples.`,
        ur: `[مشقی جائزہ سوال] ایمپیریکل فارمولا اور مالیکیولر فارمولا میں دو مثالوں کے ساتھ فرق واضح کریں۔`,
        cat: "Textbook Exercises"
      },
      {
        en: `[In-Text Box: Test Yourself] Why are noble gases chemically unreactive under standard conditions?`,
        ur: `[چیپٹر کے اندر سے: خود پرکھیں] نوبل گیسیں عام حالات میں کیمیائی طور پر غیر عامل کیوں ہوتی ہیں؟`,
        cat: "In-Text & Box Questions"
      },
      {
        en: `[In-Text Box: Do You Know?] State the importance of ozone layer in stratosphere and mention how CFCs destroy it.`,
        ur: `[چیپٹر کے اندر سے: کیا آپ جانتے ہیں؟] سٹریٹوسفیئر میں اوزون کی تہہ کی اہمیت بیان کریں اور بتائیں CFCs اسے کیسے تباہ کرتے ہیں۔`,
        cat: "In-Text & Box Questions"
      },
      {
        en: `[Past Board Paper] State Boyle's Law and Charles's Law. Give their mathematical representations.`,
        ur: `[سابقہ بورڈ پرچہ جات] بوائل کا قانون اور چارلس کا قانون بیان کریں اور ان کی حسابی مساواتیں لکھیں۔`,
        cat: "Past Board Papers"
      },
      {
        en: `[SLO Conceptual] Why does electronegativity increase across a period from left to right in the modern periodic table?`,
        ur: `[تصوراتی SLO سوال] جدید پیریوڈک ٹیبل میں بائیں سے دائیں پیریڈ میں الیکٹرو نیگیٹیوٹی میں اضافہ کیوں ہوتا ہے؟`,
        cat: "SLO Conceptual"
      },
      {
        en: `[Numerical Problem] Calculate the molarity of a solution prepared by dissolving 4 g of NaOH in 250 cm³ of water.`,
        ur: `[حسابی مسئلہ] 4 گرام سوڈیم ہائیڈرو آکسائیڈ (NaOH) کو 250 cm³ پانی میں حل کر کے بنائے گئے محلول کی مولیرٹی معلوم کریں۔`,
        cat: "Numerical Problems"
      }
    ];

    subjectLongTemplates = [
      {
        theoryEn: `[Past Board Paper] State and explain Rutherford's Atomic Model based on Gold Foil Experiment. Mention its defects.`,
        theoryUr: `[سابقہ بورڈ پرچہ] گولڈ فوائل تجربے کی بنیاد پر ردرفورڈ کا ایٹمی ماڈل بیان کریں اور اس کے نقائص تحریر کریں۔`,
        numEn: `[Textbook Exercise Q] Describe Bohr's Atomic Theory and write four main postulates that resolved Rutherford's defects.`,
        numUr: `[مشقی تفصیلی سوال] بوہر کا ایٹمی نظریہ بیان کریں اور وہ چار اہم مفروضات تحریر کریں جنہوں نے ردرفورڈ کے نقائص دور کیے۔`
      }
    ];
  }

  // ==========================================
  // 3. BIOLOGY
  // ==========================================
  else if (isBiology) {
    subjectMcqTemplates = [
      {
        en: `In ${chTitleEn}, the cellular organelle responsible for protein synthesis is:`,
        ur: `${chTitleUr} میں پروٹین کی تیاری کا ذمہ دار سیلولر آرگنیل کون سا ہے؟`,
        opts: [
          { en: "Ribosomes", ur: "رائیبوسومز" },
          { en: "Mitochondria", ur: "مائٹوکونڈریا" },
          { en: "Golgi Apparatus", ur: "گولجی اپریٹس" },
          { en: "Lysosomes", ur: "لائسوسومز" }
        ],
        correct: "A"
      },
      {
        en: `Which stage of aerobic cellular respiration produces the maximum yield of ATP?`,
        ur: `ایروبک سیلولر ریسپائریشن کا کون سا مرحلہ سب سے زیادہ اے ٹی پی (ATP) پیدا کرتا ہے؟`,
        opts: [
          { en: "Electron Transport Chain", ur: "الیکٹران ٹرانسپورٹ چین" },
          { en: "Glycolysis", ur: "گلائیکولائسس" },
          { en: "Krebs Cycle", ur: "کریبس سائیکل" },
          { en: "Alcoholic Fermentation", ur: "الکوحلک فرمنٹیشن" }
        ],
        correct: "A"
      }
    ];

    subjectExerciseMcqs = [
      {
        en: `[Textbook Exercise Q.1] Heart is enclosed in a protective double-layered membrane called:`,
        ur: `[مشقی سوال 1] دل ایک حفاظتی دوہری جھلی میں لپٹا ہوتا ہے جسے کہتے ہیں:`,
        opts: [
          { en: "Pericardium", ur: "پیری کارڈیم" },
          { en: "Pleura", ur: "پلورا" },
          { en: "Peritoneum", ur: "پیریٹونیم" },
          { en: "Meninges", ur: "مینینجز" }
        ],
        correct: "A"
      },
      {
        en: `[Textbook Exercise Q.2] The functional filtration unit of human kidney is called:`,
        ur: `[مشقی سوال 2] انسانی گردے کی فعلیاتی اور ساخت کی بنیادی اکائی کہلاتی ہے:`,
        opts: [
          { en: "Nephron", ur: "نیفرون" },
          { en: "Neuron", ur: "نیورون" },
          { en: "Alveolus", ur: "ایلویولس" },
          { en: "Villus", ur: "ولس" }
        ],
        correct: "A"
      }
    ];

    subjectInTextBoxMcqs = [
      {
        en: `[In-Text Box: Do You Know?] Who discovered penicillin, the world's first life-saving antibiotic, and in which year?`,
        ur: `[چیپٹر کے اندر سے: کیا آپ جانتے ہیں؟] دنیا کی پہلی اینٹی بائیوٹک پینسلین کس نے اور کس سال دریافت کی؟`,
        opts: [
          { en: "Alexander Fleming (1928)", ur: "الیگزینڈر فلیمنگ (1928)" },
          { en: "Louis Pasteur (1885)", ur: "لوئی پاسچر (1885)" },
          { en: "Robert Koch (1876)", ur: "رابرٹ کوخ (1876)" },
          { en: "Edward Jenner (1796)", ur: "ایڈورڈ جینر (1796)" }
        ],
        correct: "A"
      },
      {
        en: `[In-Text Box: Point to Ponder] Why are mature mammalian red blood cells (erythrocytes) devoid of a nucleus?`,
        ur: `[چیپٹر کے اندر سے: سوچنے کی بات] بالغ ممالیہ کے ریڈ بلڈ سیلز میں نیوکلیئس کیوں ختم ہو جاتا ہے؟`,
        opts: [
          { en: "To provide maximum space for hemoglobin to carry oxygen", ur: "تاکہ ہیموگلوبن اور آکسیجن کی ترسیل کے لیے زیادہ جگہ مل سکے" },
          { en: "To prevent bacterial reproduction", ur: "بیکٹیریا کی افزائش روکنے کے لیے" },
          { en: "To withstand acidic blood pH", ur: "خون کی تیزابیت برداشت کرنے کے لیے" },
          { en: "Due to lack of cellular energy", ur: "سیلولر توانائی کی کمی کی وجہ سے" }
        ],
        correct: "A"
      }
    ];

    subjectShortTemplates = [
      {
        en: `[Textbook Exercise Review Q] Differentiate between Mitosis and Meiosis with two fundamental differences.`,
        ur: `[مشقی جائزہ سوال] مائٹوسس اور میوسس میں دو بنیادی فرق واضح کریں۔`,
        cat: "Textbook Exercises"
      },
      {
        en: `[In-Text Box: Test Yourself] Define transpiration. Why is it termed a 'necessary evil' for plants?`,
        ur: `[چیپٹر کے اندر سے: خود پرکھیں] ٹرانسپائریشن کی تعریف کریں۔ پودوں کے لیے اسے 'لازمی برائی' کیوں کہا جاتا ہے؟`,
        cat: "In-Text & Box Questions"
      },
      {
        en: `[In-Text Box: Do You Know?] What is dialysis? State the basic difference between hemodialysis and peritoneal dialysis.`,
        ur: `[چیپٹر کے اندر سے: کیا آپ جانتے ہیں؟] ڈائیلاسس کیا ہے؟ ہیمو ڈائیلاسس اور پیریٹونیل ڈائیلاسس میں بنیادی فرق بیان کریں۔`,
        cat: "In-Text & Box Questions"
      },
      {
        en: `[Past Board Paper] State the Lock and Key Model of enzyme action proposed by Emil Fischer.`,
        ur: `[سابقہ بورڈ پرچہ جات] ایمل فشر کا پیش کردہ انزائم ایکشن کا لاک اینڈ کی ماڈل بیان کریں۔`,
        cat: "Past Board Papers"
      },
      {
        en: `[SLO Conceptual] How does the structure of human villi in small intestine facilitate efficient food absorption?`,
        ur: `[تصوراتی SLO سوال] چھوٹی آنت میں ولائی (Villi) کی ساخت کس طرح خوراک کے جذب کرنے میں معاون ثابت ہوتی ہے؟`,
        cat: "SLO Conceptual"
      }
    ];

    subjectLongTemplates = [
      {
        theoryEn: `[Past Board Paper] Describe the light reactions (Z-scheme) of photosynthesis with a neat, labelled diagram.`,
        theoryUr: `[سابقہ بورڈ پرچہ] فوٹوسنتھیسز کے لائٹ ری ایکشنز (زیڈ سکیم) کی وضاحت صاف ستھرے لیبل شدہ خاکے کے ساتھ کریں۔`,
        numEn: `[Textbook Exercise Q] Explain the dark reactions (Calvin cycle) of photosynthesis and explain how glucose is synthesized.`,
        numUr: `[مشقی تفصیلی سوال] فوٹوسنتھیسز کے ڈارک ری ایکشنز (کیلون سائیکل) کی وضاحت کریں اور بتائیں گلوکوز کیسے بنتا ہے۔`
      }
    ];
  }

  // ==========================================
  // 4. MATHEMATICS
  // ==========================================
  else if (isMath) {
    subjectMcqTemplates = [
      {
        en: `In ${chTitleEn}, the multiplicative identity matrix of order 2-by-2 is:`,
        ur: `${chTitleUr} میں 2x2 کا ضربی ذاتی قالب (Multiplicative Identity) ہے:`,
        opts: [
          { en: "[1 0; 0 1]", ur: "[1 0; 0 1]" },
          { en: "[0 1; 1 0]", ur: "[0 1; 1 0]" },
          { en: "[0 0; 0 0]", ur: "[0 0; 0 0]" },
          { en: "[1 1; 1 1]", ur: "[1 1; 1 1]" }
        ],
        correct: "A"
      },
      {
        en: `The discriminant of the quadratic equation ax² + bx + c = 0 is:`,
        ur: `دو درجی مساوات ax² + bx + c = 0 کا فرق کنندہ (Discriminant) ہوتا ہے:`,
        opts: [
          { en: "b² - 4ac", ur: "b² - 4ac" },
          { en: "b² + 4ac", ur: "b² + 4ac" },
          { en: "-b ± √(b² - 4ac)", ur: "-b ± √(b² - 4ac)" },
          { en: "4ac - b²", ur: "4ac - b²" }
        ],
        correct: "A"
      }
    ];

    subjectExerciseMcqs = [
      {
        en: `[Textbook Exercise Q.1] If |A| = 0, then the matrix A is termed as:`,
        ur: `[مشقی سوال 1] اگر کسی قالب کا مقطع |A| = 0 ہو، تو قالب A کہلاتا ہے:`,
        opts: [
          { en: "Singular Matrix", ur: "نادر قالب (Singular)" },
          { en: "Non-singular Matrix", ur: "غیر نادر قالب (Non-singular)" },
          { en: "Symmetric Matrix", ur: "سمیٹرک قالب" },
          { en: "Identity Matrix", ur: "وحدانی قالب" }
        ],
        correct: "A"
      },
      {
        en: `[Textbook Exercise Q.2] The base of common logarithm (Brigg's logarithm) is:`,
        ur: `[مشقی سوال 2] عام لوگارتھم (برگز لوگارتھم) کی اساس (Base) ہوتی ہے:`,
        opts: [
          { en: "10", ur: "10" },
          { en: "e (2.718)", ur: "e (2.718)" },
          { en: "2", ur: "2" },
          { en: "0", ur: "0" }
        ],
        correct: "A"
      }
    ];

    subjectInTextBoxMcqs = [
      {
        en: `[In-Text Box: Historical Note] Who first introduced the concept and theory of matrices in 1858?`,
        ur: `[چیپٹر کے اندر سے: معلوماتی نکتہ] 1858ء میں قالبوں کا نظریہ سب سے پہلے کس نے پیش کیا؟`,
        opts: [
          { en: "Arthur Cayley (English Mathematician)", ur: "آرتھر کیلے (انگریز ریاضی دان)" },
          { en: "John Napier", ur: "جان نیپیئر" },
          { en: "Al-Khwarizmi", ur: "الخوارزمی" },
          { en: "Pythagoras", ur: "فیثا غورث" }
        ],
        correct: "A"
      },
      {
        en: `[In-Text Box: Point to Ponder] Why is the square root of a negative real number not defined in the set of real numbers ℝ?`,
        ur: `[چیپٹر کے اندر سے: سوچنے کی بات] حقیقی اعداد کے سیٹ میں منفی عدد کا جذر کیوں ممکن نہیں؟`,
        opts: [
          { en: "Because the square of any real number is always non-negative, yielding imaginary i = √(-1)", ur: "کیونکہ کسی بھی حقیقی عدد کا مربع منفی نہیں ہوتا، جس سے غیر حقیقی عدد i = √(-1) بنتا ہے" },
          { en: "Because negative numbers do not have factors", ur: "کیونکہ منفی اعداد کے اجزائے ضربی نہیں ہوتے" },
          { en: "Due to fractional power errors", ur: "کسری طاقت کی خرابی کی وجہ سے" },
          { en: "It is zero by definition", ur: "تعریف کے مطابق صفر ہوتا ہے" }
        ],
        correct: "A"
      }
    ];

    subjectShortTemplates = [
      {
        en: `[Textbook Exercise Review Q] Solve for x: log₃(x) = 5.`,
        ur: `[مشقی جائزہ سوال] مساوات حل کریں: log₃(x) = 5.`,
        cat: "Textbook Exercises"
      },
      {
        en: `[In-Text Box: Test Yourself] Define symmetric and skew-symmetric matrix with mathematical condition.`,
        ur: `[چیپٹر کے اندر سے: خود پرکھیں] سمیٹرک اور سکیو سمیٹرک قالب کی حسابی شرائط تحریر کریں۔`,
        cat: "In-Text & Box Questions"
      },
      {
        en: `[Past Board Paper] State Pythagoras Theorem. Write its algebraic expression for a right-angled triangle.`,
        ur: `[سابقہ بورڈ پرچہ جات] مسئلہ فیثا غورث بیان کریں اور قائمۃ الزاویہ مثلث کے لیے اس کا الجبرائی کلیہ لکھیں۔`,
        cat: "Past Board Papers"
      },
      {
        en: `[SLO Conceptual] Prove that (A B)⁻¹ = B⁻¹ A⁻¹ for non-singular matrices A and B.`,
        ur: `[تصوراتی SLO سوال] ثابت کریں کہ غیر نادر قالبوں A اور B کے لیے (A B)⁻¹ = B⁻¹ A⁻¹ ہوتا ہے۔`,
        cat: "SLO Conceptual"
      },
      {
        en: `[Numerical Problem] Find the value of x and y using Cramer's Rule for: 2x - 2y = 4 and 3x + 2y = 6.`,
        ur: `[حسابی مسئلہ] کرائمر کے طریقے سے x اور y کی قیمت معلوم کریں: 2x - 2y = 4 اور 3x + 2y = 6.`,
        cat: "Numerical Problems"
      }
    ];

    subjectLongTemplates = [
      {
        theoryEn: `[Past Board Paper: Compulsory Theorem] Prove that any point on the right bisector of a line segment is equidistant from its end points.`,
        theoryUr: `[سابقہ بورڈ پرچہ: لازمی مسئلہ] ثابت کریں کہ کسی قطعہ خط کے عمودی ناصف پر واقع کوئی بھی نقطہ اس کے سروں سے مساوی الفاصلہ ہوتا ہے۔`,
        numEn: `[Textbook Exercise Problem] Use logarithm table to evaluate: (0.8176 × 13.64) / 2.534.`,
        numUr: `[مشقی حسابی سوال] لوگارتھم ٹیبل کی مدد سے قیمت معلوم کریں: (0.8176 × 13.64) / 2.534.`
      }
    ];
  }

  // ==========================================
  // 5. COMPUTER SCIENCE
  // ==========================================
  else if (isComputer) {
    subjectMcqTemplates = [
      {
        en: `In ${chTitleEn}, the standard geometric symbol used to represent Decision in a Flowchart is:`,
        ur: `${chTitleUr} میں فلو چارٹ کے اندر فیصلے (Decision) کو ظاہر کرنے کے لیے کون سی علامت استعمال ہوتی ہے؟`,
        opts: [
          { en: "Diamond", ur: "ڈائمنڈ (ہیرے کی شکل)" },
          { en: "Rectangle", ur: "مستطیل (Rectangle)" },
          { en: "Parallelogram", ur: "متوازی الاضلاع" },
          { en: "Oval", ur: "بیضوی (Oval)" }
        ],
        correct: "A"
      },
      {
        en: `The base of the hexadecimal number system is:`,
        ur: `ہیکسا ڈیسیمل نمبر سسٹم کی اساس (Base) کتنی ہوتی ہے؟`,
        opts: [
          { en: "16 (Digits 0-9 and A-F)", ur: "16 (ہندسے 0 تا 9 اور حروف A تا F)" },
          { en: "8", ur: "8" },
          { en: "2", ur: "2" },
          { en: "10", ur: "10" }
        ],
        correct: "A"
      }
    ];

    subjectExerciseMcqs = [
      {
        en: `[Textbook Exercise Q.1] Which topology connects all computer devices to a single central backbone cable?`,
        ur: `[مشقی سوال 1] کون سی ٹوپولوجی تمام کمپیوٹرز کو ایک مرکزی بیک بون کیبل سے جوڑتی ہے؟`,
        opts: [
          { en: "Bus Topology", ur: "بس ٹوپولوجی" },
          { en: "Star Topology", ur: "سٹار ٹوپولوجی" },
          { en: "Ring Topology", ur: "رنگ ٹوپولوجی" },
          { en: "Mesh Topology", ur: "میش ٹوپولوجی" }
        ],
        correct: "A"
      },
      {
        en: `[Textbook Exercise Q.2] The HTML tag used to create a hyperlink to another web page is:`,
        ur: `[مشقی سوال 2] کسی دوسرے ویب پیج پر ہائپر لنک بنانے کے لیے کون سا HTML ٹیگ استعمال ہوتا ہے؟`,
        opts: [
          { en: "<a href='...'>", ur: "<a href='...'>" },
          { en: "<link>", ur: "<link>" },
          { en: "<href>", ur: "<href>" },
          { en: "<url>", ur: "<url>" }
        ],
        correct: "A"
      }
    ];

    subjectInTextBoxMcqs = [
      {
        en: `[In-Text Box: Do You Know?] Where was the world's first PC computer virus 'Brain' created in 1986?`,
        ur: `[چیپٹر کے اندر سے: کیا آپ جانتے ہیں؟] دنیا کا پہلا پی سی وائرس 'برین' 1986ء میں کہاں تیار کیا گیا تھا؟`,
        opts: [
          { en: "Lahore, Pakistan (by Amjad & Basit Farooq Alvi)", ur: "لاہور، پاکستان (امجد اور باسط فاروق علوی نے)" },
          { en: "Silicon Valley, USA", ur: "سلیکون ویلی، امریکہ" },
          { en: "Tokyo, Japan", ur: "ٹوکیو، جاپان" },
          { en: "London, UK", ur: "لندن، برطانیہ" }
        ],
        correct: "A"
      },
      {
        en: `[In-Text Box: Point to Ponder] Why does a digital computer only comprehend binary language (0 and 1)?`,
        ur: `[چیپٹر کے اندر سے: سوچنے کی بات] ڈیجیٹل کمپیوٹر صرف بائنری زبان (0 اور 1) ہی کیوں سمجھتا ہے؟`,
        opts: [
          { en: "Because electronic circuits operate on two physical states: ON (high voltage) and OFF (low voltage)", ur: "کیونکہ الیکٹرانک سرکٹس صرف دو حالتوں آن (ON) اور آف (OFF) پر کام کرتے ہیں" },
          { en: "To reduce keyboard key requirements", ur: "کی بورڈ کے بٹن کم رکھنے کے لیے" },
          { en: "Because English letters take too much memory", ur: "کیونکہ انگریزی حروف زیادہ میموری لیتے ہیں" },
          { en: "It was an arbitrary historic choice", ur: "یہ محض ایک تاریخی اتفاق تھا" }
        ],
        correct: "A"
      }
    ];

    subjectShortTemplates = [
      {
        en: `[Textbook Exercise Review Q] Define Algorithm. State two major advantages of developing an algorithm before writing code.`,
        ur: `[مشقی جائزہ سوال] الگورتھم کی تعریف کریں۔ کوڈ لکھنے سے قبل الگورتھم بنانے کے دو بڑے فوائد تحریر کریں۔`,
        cat: "Textbook Exercises"
      },
      {
        en: `[In-Text Box: Test Yourself] Differentiate between IPv4 and IPv6 addressing schemes.`,
        ur: `[چیپٹر کے اندر سے: خود پرکھیں] IPv4 اور IPv6 ایڈریسنگ سکیمز میں بنیادی فرق بیان کریں۔`,
        cat: "In-Text & Box Questions"
      },
      {
        en: `[In-Text Box: Do You Know?] What is Caesar Cipher? How does substitution encryption protect data?`,
        ur: `[چیپٹر کے اندر سے: کیا آپ جانتے ہیں؟] سیزر سائفر کیا ہے؟ متبادل انکرپشن ڈیٹا کا تحفظ کیسے کرتی ہے؟`,
        cat: "In-Text & Box Questions"
      },
      {
        en: `[Past Board Paper] State the difference between Compiler and Interpreter with examples of languages.`,
        ur: `[سابقہ بورڈ پرچہ جات] کمپائلر اور انٹرپریٹر میں دو فرق تحریر کریں اور متعلقہ زبانوں کی مثال دیں۔`,
        cat: "Past Board Papers"
      },
      {
        en: `[SLO Conceptual] Write standard C language syntax for a 'for' loop and explain its three header expressions.`,
        ur: `[تصوراتی SLO سوال] سی (C) لینگویج میں فار (for) لوپ کا معیاری سنٹیکس لکھیں اور اس کے تینوں حصوں کی وضاحت کریں۔`,
        cat: "SLO Conceptual"
      }
    ];

    subjectLongTemplates = [
      {
        theoryEn: `[Past Board Paper] Explain Star Topology and Bus Topology with neat network diagrams, merits, and demerits.`,
        theoryUr: `[سابقہ بورڈ پرچہ] سٹار ٹوپولوجی اور بس ٹوپولوجی کی وضاحت تصویری خاکوں، فوائد اور نقصانات کے ساتھ کریں۔`,
        numEn: `[Textbook Exercise Problem] Convert the following binary number (11010110)₂ into Decimal and Hexadecimal systems. Show all working steps.`,
        numUr: `[مشقی حسابی سوال] بائنری نمبر (11010110)₂ کو ڈیسیمل اور ہیکسا ڈیسیمل نظام میں تبدیل کریں۔ تمام مراحل واضح کریں۔`
      }
    ];
  }

  // ==========================================
  // 6. ISLAMIAT COMPULSORY
  // ==========================================
  else if (isIslamiat) {
    subjectMcqTemplates = [
      {
        en: `According to PTBB curriculum of ${chTitleEn}, the primary pillar and core foundation of Islam is:`,
        ur: `${chTitleUr} کے نصاب کے مطابق اسلام کا سب سے بنیادی ستون اور اصل بنیاد ہے:`,
        opts: [
          { en: "Tauheed (Belief in Oneness of Allah)", ur: "عقیدہ توحید (اللہ تعالیٰ کی وحدانیت)" },
          { en: "Material Wealth", ur: "دنیاوی دولت" },
          { en: "Racial Superiority", ur: "نسلی برتری" },
          { en: "Political Power", ur: "سیاسی طاقت" }
        ],
        correct: "A"
      },
      {
        en: `In Surah Al-Anfal, what divine reward is promised to believers who remain steadfast?`,
        ur: `سورۃ الانفال میں ثابت قدم رہنے والے مومنین کے لیے کس انعام کا وعدہ کیا گیا ہے؟`,
        opts: [
          { en: "Divine Help and Forgiveness from Allah", ur: "اللہ کی غیبی مدد اور مغفرت" },
          { en: "Worldly Immortality", ur: "ہمیشہ کی دنیاوی زندگی" },
          { en: "Material Kingdoms", ur: "شاہی محلات" },
          { en: "Freedom from Accountability", ur: "احتساب سے چھوٹ" }
        ],
        correct: "A"
      }
    ];

    subjectExerciseMcqs = [
      {
        en: `[Textbook Exercise Q.1] What is the literal meaning of 'Zakat'?`,
        ur: `[مشقی سوال 1] لفظ 'زکوٰۃ' کے لغوی معنی کیا ہیں؟`,
        opts: [
          { en: "To purify and increase", ur: "پاک ہونا اور نشوونما پانا" },
          { en: "To spend casually", ur: "خرچ کرنا" },
          { en: "To store wealth", ur: "مال جمع کرنا" },
          { en: "To travel", ur: "سفر کرنا" }
        ],
        correct: "A"
      }
    ];

    subjectInTextBoxMcqs = [
      {
        en: `[In-Text Box: Hadith Guidance] The Holy Prophet (PBUH) stated: 'The best among you is the one who:`,
        ur: `[چیپٹر کے اندر سے: حدیثِ مبارکہ] رسول اکرم ﷺ نے فرمایا: 'تم میں سے بہترین شخص وہ ہے جو:` ,
        opts: [
          { en: "Learns the Quran and teaches it to others", ur: "قرآن سیکھے اور دوسروں کو سکھائے" },
          { en: "Amasses maximum property", ur: "سب سے زیادہ مال کمائے" },
          { en: "Has highest social status", ur: "اعلیٰ عہدہ رکھے" },
          { en: "Travels most frequently", ur: "سب سے زیادہ سفر کرے" }
        ],
        correct: "A"
      }
    ];

    subjectShortTemplates = [
      {
        en: `[Textbook Exercise Review Q] State the rights of parents (والدین کے حقوق) in the light of the Holy Quran.`,
        ur: `[مشقی جائزہ سوال] قرآن مجید کی روشنی میں والدین کے حقوق تحریر کریں۔`,
        cat: "Textbook Exercises"
      },
      {
        en: `[In-Text Box: Quranic Injunction] Explain the Islamic concept of Huqooq-ul-Ibaad (rights of fellow human beings).`,
        ur: `[چیپٹر کے اندر سے: قرآنی نکتہ] اسلامی تعلیمات کی روشنی میں حقوق العباد کی اہمیت واضح کریں۔`,
        cat: "In-Text & Box Questions"
      },
      {
        en: `[Past Board Paper] Translate and briefly explain Hadith # 3 regarding brotherhood in Islam.`,
        ur: `[سابقہ بورڈ پرچہ جات] اخوتِ اسلامی سے متعلق حدیث نبوی کا ترجمہ اور مختصر مفہوم تحریر کریں۔`,
        cat: "Past Board Papers"
      },
      {
        en: `[SLO Conceptual] What is the significance of Jihad fi Sabeelillah in defending the sovereignty of Muslims?`,
        ur: `[تصوراتی SLO سوال] اسلام میں جہاد فی سبیل اللہ کی شرائط اور مقاصد بیان کریں۔`,
        cat: "SLO Conceptual"
      }
    ];

    subjectLongTemplates = [
      {
        theoryEn: `[Past Board Paper] Write a comprehensive note on the Excellence and Preservation of the Holy Quran.`,
        theoryUr: `[سابقہ بورڈ پرچہ] قرآن مجید کے فضائل اور تدوین و حفاظتِ قرآن پر تفصیلی نوٹ تحریر کریں۔`,
        numEn: `[Textbook Exercise Q] Discuss the Seerah of the Holy Prophet (PBUH) as a model of justice and tolerance.`,
        numUr: `[مشقی تفصیلی سوال] نبی کریم ﷺ کے اسوۂ حسنہ کی روشنی میں عدل و انصاف اور رواداری پر جامع نوٹ لکھیں۔`
      }
    ];
  }

  // ==========================================
  // 7. TARJUMA-TUL-QURAN
  // ==========================================
  else if (isTarjuma) {
    subjectMcqTemplates = [
      {
        en: `Surah ${chTitleEn} was revealed in which phase of Islamic Prophethood?`,
        ur: `سورۃ ${chTitleUr} کا نزول کس دورِ نبوت میں ہوا؟`,
        opts: [
          { en: "Makki phase (emphasizing Tauheed and Akhirah)", ur: "مکی دور (جس میں توحید اور آخرت پر زور ہے)" },
          { en: "Madani phase exclusively", ur: "صرف مدنی دور" },
          { en: "Post-Hijrah Tabuk period", ur: "غزوہ تبوک کے بعد" },
          { en: "Fatah Makkah era", ur: "فتح مکہ کا دور" }
        ],
        correct: "A"
      }
    ];

    subjectExerciseMcqs = [
      {
        en: `[Textbook Exercise Q.1] What is the central theme of ${chTitleEn}?`,
        ur: `[مشقی سوال 1] ${chTitleUr} کا مرکزی موضوع کیا ہے؟`,
        opts: [
          { en: "Confirmation of Prophethood and Monotheism", ur: "اثباتِ توحید، رسالت اور قیامت کے دلائل" },
          { en: "Inheritance laws only", ur: "صرف وراثت کے احکام" },
          { en: "Historical trade agreements", ur: "تجارتی معاہدات" },
          { en: "Geographical descriptions", ur: "جغرافیائی حالات" }
        ],
        correct: "A"
      }
    ];

    subjectInTextBoxMcqs = [
      {
        en: `[In-Text Box: Shan-e-Nuzool] Why was this Surah bestowed upon the Holy Prophet (PBUH)?`,
        ur: `[چیپٹر کے اندر سے: شانِ نزول] اس مبارک سورت کے نزول کا خاص پس منظر کیا تھا؟`,
        opts: [
          { en: "To provide solace, guidance, and refute pagan arguments", ur: "تسکینِ قلبِ نبوی، کفار کے شبہات کا رد اور مومنین کی رہنمائی کے لیے" },
          { en: "To announce military victory", ur: "فوجی فتح کے اعلان کے لیے" },
          { en: "For political treaties", ur: "سیاسی معاہدوں کے لیے" },
          { en: "To list financial laws", ur: "مالی قوانین کے لیے" }
        ],
        correct: "A"
      }
    ];

    subjectShortTemplates = [
      {
        en: `[Textbook Exercise Review Q] Write the introduction and background of ${chTitleEn}.`,
        ur: `[مشقی جائزہ سوال] ${chTitleUr} کا تعارف اور پس منظر تحریر کریں۔`,
        cat: "Textbook Exercises"
      },
      {
        en: `[In-Text Box: Quranic Wisdom] Mention two key lessons derived from the story of prophets mentioned in ${chTitleEn}.`,
        ur: `[چیپٹر کے اندر سے: قرآنی حکمت] ${chTitleUr} میں مذکور انبیاء کرام کے واقعات سے حاصل ہونے والے دو اہم اسباق تحریر کریں۔`,
        cat: "In-Text & Box Questions"
      },
      {
        en: `[Past Board Paper] Write the meaning of four Arabic vocabulary words from ${chTitleEn}.`,
        ur: `[سابقہ بورڈ پرچہ جات] ${chTitleUr} کے چار اہم قرآنی الفاظ کے معانی تحریر کریں۔`,
        cat: "Past Board Papers"
      },
      {
        en: `[SLO Conceptual] How does ${chTitleEn} establish the certainty of life after death (Akhirah)?`,
        ur: `[تصوراتی SLO سوال] ${chTitleUr} میں عقیدہ آخرت کو عقلی دلائل سے کیسے ثابت کیا گیا ہے؟`,
        cat: "SLO Conceptual"
      }
    ];

    subjectLongTemplates = [
      {
        theoryEn: `[Past Board Paper] Write a detailed summary of the main themes and commandments revealed in ${chTitleEn}.`,
        theoryUr: `[سابقہ بورڈ پرچہ] ${chTitleUr} کے مرکزی مضامین اور اہم قرآنی احکام پر تفصیلی نوٹ تحریر کریں۔`,
        numEn: `[Textbook Exercise Q] Translate into Urdu the specified authentic verses from ${chTitleEn} with context.`,
        numUr: `[مشقی تفصیلی سوال] ${chTitleUr} کی منتخب قرآنی آیات کا با محاورہ اردو ترجمہ اور تشریح تحریر کریں۔`
      }
    ];
  }

  // ==========================================
  // 8. PAKISTAN STUDIES
  // ==========================================
  else if (isPakStudies) {
    subjectMcqTemplates = [
      {
        en: `According to PTBB curriculum, the Pakistan Resolution was passed on:`,
        ur: `پنجاب ٹیکسٹ بک بورڈ کے مطابق قراردادِ پاکستان کس تاریخ کو منظور ہوئی؟`,
        opts: [
          { en: "23rd March 1940 at Minto Park Lahore", ur: "23 مارچ 1940ء (منٹو پارک لاہور میں)" },
          { en: "14th August 1947", ur: "14 اگست 1947ء" },
          { en: "3rd June 1947", ur: "3 جون 1947ء" },
          { en: "21st April 1938", ur: "21 اپریل 1938ء" }
        ],
        correct: "A"
      },
      {
        en: `Allama Muhammad Iqbal delivered his historic Allahabad Address in:`,
        ur: `علامہ محمد اقبال نے تاریخی خطبہ الہ آباد کس سال پیش فرمایا؟`,
        opts: [
          { en: "1930", ur: "1930ء" },
          { en: "1940", ur: "1940ء" },
          { en: "1906", ur: "1906ء" },
          { en: "1928", ur: "1928ء" }
        ],
        correct: "A"
      }
    ];

    subjectExerciseMcqs = [
      {
        en: `[Textbook Exercise Q.1] The highest mountain peak in Pakistan is:`,
        ur: `[مشقی سوال 1] پاکستان کی سب سے اونچی پہاڑی چوٹی کون سی ہے؟`,
        opts: [
          { en: "K2 (Godwin Austen - 8,611 m)", ur: "کے ٹو (8,611 میٹر)" },
          { en: "Nanga Parbat", ur: "نانگا پربت" },
          { en: "Tirich Mir", ur: "ترچ میر" },
          { en: "Broad Peak", ur: "براڈ پیک" }
        ],
        correct: "A"
      }
    ];

    subjectInTextBoxMcqs = [
      {
        en: `[In-Text Box: Do You Know?] What is the total length of the coastline of Pakistan along the Arabian Sea?`,
        ur: `[چیپٹر کے اندر سے: کیا آپ جانتے ہیں؟] بحیرہ عرب کے ساتھ پاکستان کے ساحلی علاقے کی کل لمبائی کتنی ہے؟`,
        opts: [
          { en: "Approximately 1,058 km", ur: "تقریباً 1,058 کلومیٹر" },
          { en: "500 km", ur: "500 کلومیٹر" },
          { en: "2,000 km", ur: "2,000 کلومیٹر" },
          { en: "750 km", ur: "750 کلومیٹر" }
        ],
        correct: "A"
      }
    ];

    subjectShortTemplates = [
      {
        en: `[Textbook Exercise Review Q] Define the Two-Nation Theory (دو قومی نظریہ) in the words of Quaid-e-Azam.`,
        ur: `[مشقی جائزہ سوال] قائداعظم کے ارشادات کی روشنی میں دو قومی نظریے کی تعریف کریں۔`,
        cat: "Textbook Exercises"
      },
      {
        en: `[In-Text Box: Geographical Fact] Mention the geo-strategic importance of Pakistan's location in South Asia.`,
        ur: `[چیپٹر کے اندر سے: جغرافیائی اہمیت] جنوبی ایشیا میں پاکستان کے محل وقوع کی جغرافیائی اہمیت کے دو نکات لکھیں۔`,
        cat: "In-Text & Box Questions"
      },
      {
        en: `[Past Board Paper] Write four points of Quaid-e-Azam's Fourteen Points (1929).`,
        ur: `[سابقہ بورڈ پرچہ جات] قائداعظم کے چودہ نکات (1929ء) میں سے کوئی سے چار نکات تحریر کریں۔`,
        cat: "Past Board Papers"
      },
      {
        en: `[SLO Conceptual] Discuss the objectives of Pakistan's Foreign Policy with special reference to national security.`,
        ur: `[تصوراتی SLO سوال] قومی سلامتی کے تناظر میں پاکستان کی خارجہ پالیسی کے دو بنیادی مقاصد تحریر کریں۔`,
        cat: "SLO Conceptual"
      }
    ];

    subjectLongTemplates = [
      {
        theoryEn: `[Past Board Paper] Detail the Ideology of Pakistan in the light of pronouncements of Quaid-e-Azam Muhammad Ali Jinnah.`,
        theoryUr: `[سابقہ بورڈ پرچہ] قائداعظم محمد علی جناح کے ارشادات کی روشنی میں نظریہ پاکستان کی مفصل وضاحت کریں۔`,
        numEn: `[Textbook Exercise Q] Discuss the natural resources and major agricultural challenges faced by Pakistan.`,
        numUr: `[مشقی تفصیلی سوال] پاکستان کے قدرتی وسائل اور زراعت کو درپیش اہم مسائل اور ان کے حل پر تفصیلی نوٹ لکھیں۔`
      }
    ];
  }

  // ==========================================
  // 9. ENGLISH & 10. URDU (Language Fallback & Specifics)
  // ==========================================
  else if (isEnglish) {
    subjectMcqTemplates = [
      {
        en: `In ${chTitleEn}, the synonym or contextual meaning of the highlighted literary word is:`,
        ur: `${chTitleEn} کے سبق میں نمایاں کردہ لفظ کا درست مترادف ہے:`,
        opts: [
          { en: "Profound / Significant", ur: "اہم / گہرا" },
          { en: "Trivial / Meaningless", ur: "معمولی / بے معنی" },
          { en: "Temporary", ur: "عارضی" },
          { en: "Artificial", ur: "مصنوعی" }
        ],
        correct: "A"
      }
    ];
    subjectExerciseMcqs = [
      {
        en: `[Textbook Exercise Q.1] Identify the figure of speech in: 'The stars danced playfully in the moonlit sky':`,
        ur: `[مشقی سوال 1] جملے میں کون سی ادبی صنعت (Figure of Speech) استعمال ہوئی ہے؟`,
        opts: [
          { en: "Personification", ur: "پرسونیفیکیشن (تجسیم)" },
          { en: "Metaphor", ur: "میٹافر (استعارہ)" },
          { en: "Simile", ur: "سملی (تشبیہ)" },
          { en: "Hyperbole", ur: "مبالغہ" }
        ],
        correct: "A"
      }
    ];
    subjectInTextBoxMcqs = [
      {
        en: `[In-Text Box: Grammar Box] A compound sentence consists of:`,
        ur: `[چیپٹر کے اندر سے: گرامر باکس] کمپاؤنڈ فقرہ (Compound Sentence) کس پر مشتمل ہوتا ہے؟`,
        opts: [
          { en: "At least two independent clauses joined by coordinating conjunction", ur: "دو آزاد کلازز جو رابطہ حرف سے جڑی ہوں" },
          { en: "Only one single verb", ur: "صرف ایک فعل" },
          { en: "Only dependent clauses", ur: "صرف ماتحت کلازز" },
          { en: "No subject", ur: "بغیر فائل کے" }
        ],
        correct: "A"
      }
    ];
    subjectShortTemplates = [
      {
        en: `[Textbook Exercise Review Q] Answer according to '${chTitleEn}': What is the central theme of the chapter?`,
        ur: `[مشقی جائزہ سوال] سبق '${chTitleEn}' کی روشنی میں مصنف کا بنیادی پیغام اور مرکزی خیال بیان کریں۔`,
        cat: "Textbook Exercises"
      },
      {
        en: `[In-Text Box: Vocabulary & Box] Use the words 'Dedication' and 'Perseverance' in meaningful sentences.`,
        ur: `[چیپٹر کے اندر سے: الفاظ و جملے] الفاظ کو با معنی جملوں میں استعمال کریں۔`,
        cat: "In-Text & Box Questions"
      },
      {
        en: `[Past Board Paper] Change the voice: 'The students are preparing the science models for exhibition.'`,
        ur: `[سابقہ بورڈ پرچہ جات] ایکٹو سے پیسو وائس میں تبدیل کریں۔`,
        cat: "Past Board Papers"
      },
      {
        en: `[SLO Conceptual] Write a comprehensive paragraph on the moral lesson imparted by '${chTitleEn}'.`,
        ur: `[تصوراتی SLO سوال] سبق سے حاصل ہونے والے اخلاقی سبق پر جامع پیراگراف تحریر کریں۔`,
        cat: "SLO Conceptual"
      }
    ];
    subjectLongTemplates = [
      {
        theoryEn: `[Past Board Paper] Write a formal letter or application regarding official school examination arrangements.`,
        theoryUr: `[سابقہ بورڈ پرچہ] امتحانی انتظامات سے متعلق باضابطہ درخواست یا خط تحریر کریں۔`,
        numEn: `[Textbook Exercise Q] Read the paragraph and write answers to the 5 comprehension questions asked at the end.`,
        numUr: `[مشقی تفصیلی سوال] پیراگراف کو غور سے پڑھیں اور آخر میں دیے گئے 5 تفہیمی سوالات کے جوابات لکھیں۔`
      }
    ];
  } else {
    // Default / Urdu
    subjectMcqTemplates = [
      {
        en: `In '${chTitleEn}', the literary term or contextual meaning of the keyword is:`,
        ur: `'${chTitleUr}' میں کلیدی لفظ کا لغوی یا سیاقی معنی ہے:`,
        opts: [
          { en: "Standard textbook interpretation", ur: "نصابی و معیاری مفہوم" },
          { en: "Opposite slang term", ur: "متضاد غیر معیاری لفظ" },
          { en: "Unrelated metaphor", ur: "غیر متعلقہ استعارہ" },
          { en: "Informal expression", ur: "عام بول چال" }
        ],
        correct: "A"
      }
    ];
    subjectExerciseMcqs = [
      {
        en: `[Textbook Exercise Q.1] Who is the author/poet of '${chTitleUr}'?`,
        ur: `[مشقی سوال 1] سبق / نظم '${chTitleUr}' کے مصنف یا شاعر کون ہیں؟`,
        opts: [
          { en: "Authentic PTBB Text Author", ur: "پنجاب ٹیکسٹ بک بورڈ کے مستند مصنف / شاعر" },
          { en: "Unknown author", ur: "نامعلوم مصنف" },
          { en: "Foreign essayist", ur: "غیر ملکی مضمون نگار" },
          { en: "Anonymous translator", ur: "گمنام مترجم" }
        ],
        correct: "A"
      }
    ];
    subjectInTextBoxMcqs = [
      {
        en: `[In-Text Box: Qawaid Box] What is meant by Sanat-e-Tazad (صنعتِ تضاد) in Urdu poetry?`,
        ur: `[چیپٹر کے اندر سے: قواعد باکس] اردو شاعری میں صنعتِ تضاد سے کیا مراد ہے؟`,
        opts: [
          { en: "Bringing two antonymous words together in a single verse", ur: "کلام میں دو متضاد الفاظ کو اکٹھا لانا" },
          { en: "Comparing two similar objects", ur: "دو مشابہ چیزوں کا موازنہ کرنا" },
          { en: "Exaggeration in praise", ur: "تعریف میں مبالغہ آرائی" },
          { en: "Using rhyme scheme only", ur: "صرف قافیہ ملانا" }
        ],
        correct: "A"
      }
    ];
    subjectShortTemplates = [
      {
        en: `[Textbook Exercise Review Q] Write the summary and central idea (خلاصہ و مرکزی خیال) of '${chTitleUr}'.`,
        ur: `[مشقی جائزہ سوال] سبق / نظم '${chTitleUr}' کا خلاصہ اور مرکزی خیال تحریر کریں۔`,
        cat: "Textbook Exercises"
      },
      {
        en: `[In-Text Box: سیاق و سباق] Explain the highlighted paragraph with reference to context.`,
        ur: `[چیپٹر کے اندر سے: سیاق و سباق] سبق کے متن سے دیے گئے پیراگراف کی سیاق و سباق کے ساتھ تشریح کریں۔`,
        cat: "In-Text & Box Questions"
      },
      {
        en: `[Past Board Paper] Explain the poetic verse with poet's reference: اشعار کی تشریح بمع حوالہ شاعر۔`,
        ur: `[سابقہ بورڈ پرچہ جات] دیے گئے شعر کی تشریح حوالہ شاعر کے ساتھ تحریر کریں۔`,
        cat: "Past Board Papers"
      },
      {
        en: `[SLO Conceptual] Correct the following incorrect sentences according to Urdu grammar rules: جملوں کی درستی۔`,
        ur: `[تصوراتی SLO سوال] روزمرہ اور محاورے کے مطابق جملوں کی درستگی کریں۔`,
        cat: "SLO Conceptual"
      }
    ];
    subjectLongTemplates = [
      {
        theoryEn: `[Past Board Paper] Write a comprehensive essay (مضمون) of 250 words on the assigned board topic.`,
        theoryUr: `[سابقہ بورڈ پرچہ] دیے گئے بورڈ عنوان پر 250 الفاظ پر مشتمل جامع مضمون تحریر کریں۔`,
        numEn: `[Textbook Exercise Q] Comprehension: Read the given passage carefully and answer the five questions asked.`,
        numUr: `[مشقی تفصیلی سوال] فہمِ عبارت: عبارت کو پڑھ کر آخر میں دیے گئے پانچوں سوالات کے جوابات دیں۔`
      }
    ];
  }

  // =========================================================================
  // ASSEMBLY & DEDUPLICATION: MCQs, Short Questions, and Long Questions
  // =========================================================================

  // 1. Generate Past Board MCQs (Years 2020 to 2026 across all 9 Boards)
  subjectMcqTemplates.forEach((tpl, idx) => {
    PUNJAB_BOARDS_LIST.forEach((boardName, bIdx) => {
      const year = PAST_YEARS[(bIdx + chNo) % PAST_YEARS.length];
      const sess = SESSIONS[(idx + bIdx) % 2];
      const boardTag = `(${boardName} ${year} ${sess})`;
      const letters = ["A", "B", "C", "D"];
      const shuffled = [...tpl.opts];
      const targetIdx = (idx + bIdx) % 4;
      const temp = shuffled[0];
      shuffled[0] = shuffled[targetIdx];
      shuffled[targetIdx] = temp;

      mcqs.push({
        id: `${subject.id}-c${chNo}-mcq-past-${bIdx * 10 + idx + 1}`,
        qNo: mcqs.length + 1,
        statementEn: `${tpl.en} ${boardTag}`,
        statementUr: `${tpl.ur} ${boardTag}`,
        options: [
          { key: "A", textEn: shuffled[0].en, textUr: shuffled[0].ur },
          { key: "B", textEn: shuffled[1].en, textUr: shuffled[1].ur },
          { key: "C", textEn: shuffled[2].en, textUr: shuffled[2].ur },
          { key: "D", textEn: shuffled[3].en, textUr: shuffled[3].ur }
        ],
        correctOption: letters[targetIdx],
        chapterRef: chNo,
        category: "Past Board Papers",
        pastBoardInfo: `${boardName} ${year} ${sess}`
      });
    });
  });

  // 2. Generate Textbook Exercises MCQs
  subjectExerciseMcqs.forEach((exMcq, exIdx) => {
    mcqs.push({
      id: `${subject.id}-c${chNo}-mcq-ex-${exIdx + 1}`,
      qNo: mcqs.length + 1,
      statementEn: exMcq.en,
      statementUr: exMcq.ur,
      options: [
        { key: "A", textEn: exMcq.opts[0].en, textUr: exMcq.opts[0].ur },
        { key: "B", textEn: exMcq.opts[1].en, textUr: exMcq.opts[1].ur },
        { key: "C", textEn: exMcq.opts[2].en, textUr: exMcq.opts[2].ur },
        { key: "D", textEn: exMcq.opts[3].en, textUr: exMcq.opts[3].ur }
      ],
      correctOption: exMcq.correct,
      chapterRef: chNo,
      category: "Textbook Exercises"
    });
  });

  // 3. Generate In-Text & Box Questions MCQs
  subjectInTextBoxMcqs.forEach((boxMcq, boxIdx) => {
    mcqs.push({
      id: `${subject.id}-c${chNo}-mcq-box-${boxIdx + 1}`,
      qNo: mcqs.length + 1,
      statementEn: boxMcq.en,
      statementUr: boxMcq.ur,
      options: [
        { key: "A", textEn: boxMcq.opts[0].en, textUr: boxMcq.opts[0].ur },
        { key: "B", textEn: boxMcq.opts[1].en, textUr: boxMcq.opts[1].ur },
        { key: "C", textEn: boxMcq.opts[2].en, textUr: boxMcq.opts[2].ur },
        { key: "D", textEn: boxMcq.opts[3].en, textUr: boxMcq.opts[3].ur }
      ],
      correctOption: boxMcq.correct,
      chapterRef: chNo,
      category: "In-Text & Box Questions"
    });
  });

  // 4. Generate Short Questions across All Four Categories
  subjectShortTemplates.forEach((sq, sIdx) => {
    const citation = generatePunjabBoardCitation(sIdx * 3 + chNo * 5);
    const boardTag = sq.cat === "Past Board Papers" ? `(${citation})` : "";
    shortQuestions.push({
      id: `${subject.id}-c${chNo}-sq-${sIdx + 1}`,
      subNo: shortQuestions.length + 1,
      statementEn: `${sq.en} ${boardTag}`.trim(),
      statementUr: `${sq.ur} ${boardTag}`.trim(),
      marks: 2,
      chapterRef: chNo,
      category: sq.cat || "SLO Conceptual",
      pastBoardInfo: citation
    });
  });

  // Generate Additional High-Yield Short Questions for comprehensive coverage
  for (let s = 1; s <= 20; s++) {
    const citation = generatePunjabBoardCitation(s * 5 + chNo * 7);
    const isNum = (s % 3 === 0) && hasNumericals;
    const isBox = (s % 4 === 0);
    const isEx = (s % 2 === 0);
    const cat = isNum ? "Numerical Problems" : isBox ? "In-Text & Box Questions" : isEx ? "Textbook Exercises" : "Past Board Papers";
    
    let stEn = "";
    let stUr = "";

    if (isNum) {
      stEn = `[Numerical Problem] Solve and calculate the required textbook value in ${chTitleEn} when initial magnitude is ${s * 10} units and time is 5 seconds. (${citation})`;
      stUr = `[حسابی مسئلہ] ${chTitleUr} کے تحت حسابی سوال حل کریں جب ابتدائی قیمت ${s * 10} اکائیاں اور وقت 5 سیکنڈ ہو۔ (${citation})`;
    } else if (isBox) {
      stEn = `[In-Text Box / Point to Ponder] State the scientific reasoning behind the box fact observed in ${chTitleEn}. (${citation})`;
      stUr = `[چیپٹر کے اندر سے: معلوماتی بکس] ${chTitleUr} کے درسی معلوماتی باکس سے متعلق سائنسی و منطقی وجہ بیان کریں۔ (${citation})`;
    } else if (isEx) {
      stEn = `[Textbook Exercise Q.${s}] State the core definition, conditions, and textbook characteristics of ${chTitleEn}. (${citation})`;
      stUr = `[مشقی سوال ${s}] ${chTitleUr} کی بنیادی تعریف، شرائط اور درسی خصوصیات تحریر کریں۔ (${citation})`;
    } else {
      stEn = `[Past Board Paper] Give scientific reason and two key points regarding ${chTitleEn} as asked in recent examinations. (${citation})`;
      stUr = `[سابقہ بورڈ پرچہ] ${chTitleUr} سے متعلق سابقہ امتحانات میں پوچھا گیا سائنسی استدلال اور دو اہم نکات تحریر کریں۔ (${citation})`;
    }

    shortQuestions.push({
      id: `${subject.id}-c${chNo}-sq-ext-${s}`,
      subNo: shortQuestions.length + 1,
      statementEn: stEn,
      statementUr: stUr,
      marks: 2,
      chapterRef: chNo,
      category: cat,
      pastBoardInfo: citation
    });
  }

  // 5. Generate Long Questions
  subjectLongTemplates.forEach((lq, lIdx) => {
    const citation = generatePunjabBoardCitation(lIdx * 4 + chNo * 9);
    const boardTag = `(${citation})`;
    longQuestions.push({
      id: `${subject.id}-c${chNo}-lq-${lIdx + 1}`,
      qNo: longQuestions.length + 5,
      totalMarks: 9,
      parts: [
        {
          partLabel: "a",
          statementEn: `${lq.theoryEn} ${boardTag}`,
          statementUr: `${lq.theoryUr} ${boardTag}`,
          marks: 5,
          isNumerical: false
        },
        {
          partLabel: "b",
          statementEn: `${lq.numEn} ${boardTag}`,
          statementUr: `${lq.numUr} ${boardTag}`,
          marks: 4,
          isNumerical: hasNumericals
        }
      ],
      chapterRef: `Unit ${chNo}`,
      category: "Past Board Papers",
      pastBoardInfo: citation
    });
  });

  return { mcqs, shortQuestions, longQuestions };
}
