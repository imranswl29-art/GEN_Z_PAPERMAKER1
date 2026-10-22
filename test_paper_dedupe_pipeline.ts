import { MASTER_PTBB_SUBJECTS, getQuestionsForSubjectAndChapters, dedupeAndReplenishPaper } from './src/data/questionBankStore.ts';

// 1. Test Physics 9th Ch 1
const sub9Phys = MASTER_PTBB_SUBJECTS.find(s => s.id === "9th-physics")!;
const pool1 = getQuestionsForSubjectAndChapters("9th-physics", [1]);

console.log("=== POOL CHECK: 9th-physics Chapter 1 ===");
console.log("MCQs available:", pool1.mcqs.length);
console.log("Short Questions available:", pool1.shortQuestions.length);
console.log("Long Questions available:", pool1.longQuestions.length);

// 2. Simulate a paper with deliberate duplicate questions
const mockPaper = {
  header: {
    classLevel: "9th",
    subjectName: "Physics",
    syllabusCovered: "Unit 1"
  },
  objectiveSection: {
    questions: [
      { id: "m1", statementEn: "The number of base quantities in SI is:", statementUr: "ایس آئی میں بنیادی مقداروں کی تعداد ہے:", options: [], correctOption: "C" },
      // Deliberate duplicate MCQ
      { id: "m2", statementEn: "The number of base quantities in SI is:", statementUr: "ایس آئی میں بنیادی مقداروں کی تعداد ہے:", options: [], correctOption: "C" },
      { id: "m3", statementEn: "The least count of Vernier Calipers is:", statementUr: "ورنیئر کیلیپرز کا لیسٹ کاؤنٹ کتنا ہوتا ہے:", options: [], correctOption: "B" },
    ]
  },
  subjectiveSection: {
    part1_shortQuestions: [
      {
        qNo: 2,
        instructionEn: "Answer questions:",
        instructionUr: "سوالات کے جواب دیں:",
        attemptCount: 2,
        marksEach: 2,
        questions: [
          // Deliberate cross-section collision with MCQ statement
          { id: "s1", statementEn: "The number of base quantities in SI is:", statementUr: "ایس آئی میں بنیادی مقداروں کی تعداد ہے:", marks: 2 },
          { id: "s2", statementEn: "Differentiate between base quantities and derived quantities.", statementUr: "بنیادی اور ماخوذ مقداروں میں فرق واضح کریں۔", marks: 2 },
          { id: "s3", statementEn: "What is zero error in Screw Gauge?", statementUr: "سکرو گیج میں زیرو ایرر کیا ہے؟", marks: 2 }
        ]
      }
    ],
    part2_longQuestions: {
      questions: [
        {
          qNo: 5,
          totalMarks: 9,
          parts: [
            { partLabel: "a", statementEn: "Explain Vernier Calipers with its construction.", statementUr: "ورنیئر کیلیپرز کی بناوٹ بیان کریں۔", marks: 5 },
            { partLabel: "b", statementEn: "Calculate the volume of a sphere.", statementUr: "کرے کا والیم معلوم کریں۔", marks: 4, isNumerical: true }
          ]
        }
      ]
    }
  }
};

const cleaned = dedupeAndReplenishPaper(mockPaper, "9th-physics", [1]);

console.log("\n=== DEDUPLICATION RESULT ===");
const cleanMcqStatements = cleaned.objectiveSection.questions.map((m: any) => m.statementEn);
const cleanSqStatements = cleaned.subjectiveSection.part1_shortQuestions[0].questions.map((s: any) => s.statementEn);

console.log("Cleaned MCQs count:", cleanMcqStatements.length);
console.log("MCQ statements:", cleanMcqStatements);
console.log("Cleaned SQs count:", cleanSqStatements.length);
console.log("SQ statements:", cleanSqStatements);

// Check if duplicate MCQ was removed
const m1EqualM2 = cleanMcqStatements[0] === cleanMcqStatements[1];
console.log("Did MCQ duplicate get removed and replenished?", !m1EqualM2);

// Check if cross-section collision was removed
const sqHasMcqStatement = cleanSqStatements.includes("The number of base quantities in SI is:");
console.log("Did cross-section collision get removed?", !sqHasMcqStatement);
