import { GoogleGenAI, Type } from "@google/genai";

const ai = new GoogleGenAI({
  apiKey: process.env.GEMINI_API_KEY || process.env.VITE_GEMINI_API_KEY,
  httpOptions: { headers: { "User-Agent": "aistudio-build" } }
});

async function testGen() {
  const systemInstruction = `You are the Senior Curriculum Specialist and Chief Textbook Author for the Punjab Textbook Board (PTBB / BISE Punjab).
Generate authentic, real, direct examination questions for 9th Class Physics, Unit 3: Dynamics (قوت اور حرکت).

CRITICAL CONSTRAINTS (STRICTLY ENFORCED):
1. NO META-REFERENCES OR BOARD TAGS:
   - Do NOT include any text like "[Past Board Paper]", "[Textbook Exercise]", "[In-Text Box]", "(BISE Lahore 2021)", "According to PTBB", "In Punjab board exams...", or "Option A (Fundamental Principle)".
   - State the direct question immediately (e.g. "State Newton's second law of motion and write its formula." or "نیوٹن کا موشن کا دوسرا قانون بیان کریں اور اس کا کلیہ لکھیں۔").
2. REAL TEXTBOOK TOPIC CONCEPTS:
   - Questions MUST cover the actual sub-topics of Unit 3: Force, Inertia, Momentum, Newton's 1st/2nd/3rd Laws of Motion, Mass vs Weight, Tension and Acceleration in a String (Atwood machine), Law of Conservation of Momentum, Friction (Rolling vs Sliding), Centripetal Force.
3. ZERO DUPLICATION OR OVERLAP:
   - Every MCQ, Short Question, and Long Question must test a completely unique concept. Never repeat any question.
4. BILINGUAL ACCURACY:
   - Clear, standard English alongside authentic, fluent PTBB Urdu Nastaliq scientific terminology.`;

  const prompt = `Generate:
- 15 authentic MCQs with 4 distinct options (optionsEn and optionsUr), correctOption (A/B/C/D), and brief explanation.
- 12 authentic Short Questions (2 marks each) with model answer.
- 3 authentic Long Questions (9 marks each: Part a Theory 5 marks + Part b Numerical 4 marks with given values and units).`;

  const resp = await ai.models.generateContent({
    model: "gemini-3.8-flash",
    contents: prompt,
    config: {
      systemInstruction,
      responseMimeType: "application/json",
      responseSchema: {
        type: Type.OBJECT,
        properties: {
          mcqs: {
            type: Type.ARRAY,
            items: {
              type: Type.OBJECT,
              properties: {
                statementEn: { type: Type.STRING },
                statementUr: { type: Type.STRING },
                optionsEn: { type: Type.ARRAY, items: { type: Type.STRING } },
                optionsUr: { type: Type.ARRAY, items: { type: Type.STRING } },
                correctOption: { type: Type.STRING },
                explanationEn: { type: Type.STRING },
                explanationUr: { type: Type.STRING }
              },
              required: ["statementEn", "statementUr", "optionsEn", "optionsUr", "correctOption"]
            }
          },
          shortQuestions: {
            type: Type.ARRAY,
            items: {
              type: Type.OBJECT,
              properties: {
                statementEn: { type: Type.STRING },
                statementUr: { type: Type.STRING },
                answerEn: { type: Type.STRING },
                answerUr: { type: Type.STRING },
                marks: { type: Type.INTEGER }
              },
              required: ["statementEn", "statementUr", "answerEn", "answerUr"]
            }
          },
          longQuestions: {
            type: Type.ARRAY,
            items: {
              type: Type.OBJECT,
              properties: {
                qNo: { type: Type.INTEGER },
                totalMarks: { type: Type.INTEGER },
                parts: {
                  type: Type.ARRAY,
                  items: {
                    type: Type.OBJECT,
                    properties: {
                      partLabel: { type: Type.STRING },
                      statementEn: { type: Type.STRING },
                      statementUr: { type: Type.STRING },
                      marks: { type: Type.INTEGER },
                      isNumerical: { type: Type.BOOLEAN }
                    },
                    required: ["partLabel", "statementEn", "statementUr", "marks", "isNumerical"]
                  }
                }
              },
              required: ["qNo", "totalMarks", "parts"]
            }
          }
        },
        required: ["mcqs", "shortQuestions", "longQuestions"]
      }
    }
  });

  const parsed = JSON.parse(resp.text || "{}");
  console.log("Generated MCQs:", parsed.mcqs.length);
  console.log("Sample MCQ 1:", parsed.mcqs[0]);
  console.log("Sample SQ 1:", parsed.shortQuestions[0]);
  console.log("Sample LQ 1:", parsed.longQuestions[0]);
}

testGen().catch(console.error);
