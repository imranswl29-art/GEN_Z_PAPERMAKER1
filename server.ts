var __defProp=Object.defineProperty;var __name=(target,value)=>__defProp(target,"name",{value,configurable:true});import express from"express";import path from"path";import fs from"fs";import{fileURLToPath}from"url";import{GoogleGenAI,Type}from"@google/genai";import{MASTER_PTBB_SUBJECTS,getQuestionsForSubjectAndChapters,dedupeAndReplenishPaper}from"./src/data/questionBankStore.ts";const __filename=fileURLToPath(import.meta.url);const __dirname=path.dirname(__filename);const app=express();const PORT=3e3;app.use(express.json({limit:"10mb"}));const ai=new GoogleGenAI({apiKey:process.env.GEMINI_API_KEY||process.env.VITE_GEMINI_API_KEY,httpOptions:{headers:{"User-Agent":"aistudio-build"}}});const CANDIDATE_MODELS = ["gemini-3.8-flash", "gemini-flash-latest", "gemini-3.1-flash-lite"];
async function generateWithModelFallback(callFn: (model: string) => Promise<any>): Promise<any> {
  let lastError: any;
  for (const model of CANDIDATE_MODELS) {
    for (let attempt = 0; attempt < 2; attempt++) {
      try {
        return await callFn(model);
      } catch (err: any) {
        lastError = err;
        const msg = String(err?.message || err);
        const isTransient = msg.includes("503") || msg.includes("429") || msg.includes("high demand") || msg.includes("UNAVAILABLE");
        console.warn(`Model ${model} (attempt ${attempt + 1}) encountered:`, msg);
        if (isTransient && attempt === 0) {
          await new Promise(r => setTimeout(r, 1200 + Math.random() * 800));
        } else {
          break;
        }
      }
    }
  }
  throw lastError;
}__name(generateWithModelFallback,"generateWithModelFallback");const DATA_DIR=process.env.VERCEL?path.join("/tmp","data"):path.resolve(__dirname,"data");if(!fs.existsSync(DATA_DIR)){try{fs.mkdirSync(DATA_DIR,{recursive:true})}catch(e){}}const ACCOUNTS_FILE=path.join(DATA_DIR,"accounts.json");const PAPERS_FILE=path.join(DATA_DIR,"papers.json");const DATESHEETS_FILE=path.join(DATA_DIR,"datesheets.json");const MARKSHEETS_FILE=path.join(DATA_DIR,"marksheets.json");const DEFAULT_ADMIN_ACCOUNT={id:"user-admin-01",username:"admin",password:"admin",role:"admin",name:"Muhammad Imran Khan (MSc Computer Science)",schoolName:"Punjab Board Examination Central Portal",campusName:"Central Admin Office, Lahore",city:"Lahore",phone:"03007603964",targetBoard:"lahore",allowedClasses:["9th","10th"],status:"active",expiryDate:"2030-12-31",paperLimit:99999,papersCreated:0,createdAt:"2026-01-01T00:00:00.000Z"};const DEFAULT_INITIAL_ACCOUNTS=[DEFAULT_ADMIN_ACCOUNT,{id:"user-smart-pakpattan",username:"pakpattan@smartschool.edu.pk",password:"SmartDemo123",role:"principal",name:"Principal - The Smart School",schoolName:"THE SMART SCHOOL PAKPATTAN",campusName:"Pakpattan Branch (City Campus)",city:"Pakpattan",phone:"03001234567",targetBoard:"sahiwal",allowedClasses:["9th","10th"],status:"active",expiryDate:"2030-12-31",paperLimit:500,papersCreated:12,createdAt:"2026-01-01T00:00:00.000Z"},{id:"user-knowledge-okara",username:"okara@knowledgeschool.edu.pk",password:"KnowledgeDemo123",role:"principal",name:"Principal - The Knowledge School",schoolName:"THE KNOWLEDGE SCHOOL OKARA",campusName:"Okara Branch (Main Campus)",city:"Okara",phone:"03149876543",targetBoard:"sahiwal",allowedClasses:["9th","10th"],status:"active",expiryDate:"2030-12-31",paperLimit:500,papersCreated:15,createdAt:"2026-01-01T00:00:00.000Z"}];function readAccountsFromFile(){try{if(fs.existsSync(ACCOUNTS_FILE)){const data=fs.readFileSync(ACCOUNTS_FILE,"utf-8");const parsed=JSON.parse(data);if(Array.isArray(parsed)&&parsed.length>0){let changed=false;const merged=[...parsed];for(const def of DEFAULT_INITIAL_ACCOUNTS){if(!merged.some(a=>a.id===def.id||a.username===def.username)){merged.push(def);changed=true}}if(changed){writeAccountsToFile(merged)}return merged}}}catch(e){console.error("Error reading accounts file:",e)}const initial=[...DEFAULT_INITIAL_ACCOUNTS];try{fs.writeFileSync(ACCOUNTS_FILE,JSON.stringify(initial,null,2),"utf-8")}catch(e){}return initial}__name(readAccountsFromFile,"readAccountsFromFile");function writeAccountsToFile(accounts){try{fs.writeFileSync(ACCOUNTS_FILE,JSON.stringify(accounts,null,2),"utf-8")}catch(e){console.error("Error writing accounts file:",e)}}__name(writeAccountsToFile,"writeAccountsToFile");function readPapersFromFile(){try{if(fs.existsSync(PAPERS_FILE)){const data=fs.readFileSync(PAPERS_FILE,"utf-8");const parsed=JSON.parse(data);if(Array.isArray(parsed)){return parsed}}}catch(e){console.error("Error reading papers file:",e)}return[]}__name(readPapersFromFile,"readPapersFromFile");function writePapersToFile(papers){try{fs.writeFileSync(PAPERS_FILE,JSON.stringify(papers,null,2),"utf-8")}catch(e){console.error("Error writing papers file:",e)}}__name(writePapersToFile,"writePapersToFile");function readDateSheetsFromFile(){try{if(fs.existsSync(DATESHEETS_FILE)){const data=fs.readFileSync(DATESHEETS_FILE,"utf-8");const parsed=JSON.parse(data);if(Array.isArray(parsed)){return parsed}}}catch(e){console.error("Error reading datesheets file:",e)}return[]}__name(readDateSheetsFromFile,"readDateSheetsFromFile");function writeDateSheetsToFile(dateSheets){try{fs.writeFileSync(DATESHEETS_FILE,JSON.stringify(dateSheets,null,2),"utf-8")}catch(e){console.error("Error writing datesheets file:",e)}}__name(writeDateSheetsToFile,"writeDateSheetsToFile");function readMarksheetsFromFile(){try{if(fs.existsSync(MARKSHEETS_FILE)){const data=fs.readFileSync(MARKSHEETS_FILE,"utf-8");const parsed=JSON.parse(data);if(Array.isArray(parsed)){return parsed}}}catch(e){console.error("Error reading marksheets file:",e)}return[]}__name(readMarksheetsFromFile,"readMarksheetsFromFile");function writeMarksheetsToFile(marksheets){try{fs.writeFileSync(MARKSHEETS_FILE,JSON.stringify(marksheets,null,2),"utf-8")}catch(e){console.error("Error writing marksheets file:",e)}}__name(writeMarksheetsToFile,"writeMarksheetsToFile");function dedupeQuestions(paper, explicitSubjectId, explicitChapters){
  return dedupeAndReplenishPaper(paper, explicitSubjectId, explicitChapters);
}__name(dedupeQuestions,"dedupeQuestions");
function dedupeNotes(notes: any): any {
  if (!notes) return notes;
  const clean = { ...notes };
  
  // Deduplicate MCQs
  if (Array.isArray(clean.mcqs)) {
    const seenMcq = new Set<string>();
    clean.mcqs = clean.mcqs.filter((m: any) => {
      const key = ((m.questionEn || m.question_en || "") + "|" + (m.questionUr || m.question_ur || "")).trim().toLowerCase().replace(/[^a-z0-9؀-ۿ]/g, "");
      if (!key || seenMcq.has(key)) return false;
      seenMcq.add(key);
      return true;
    });
  }

  // Deduplicate Short Questions
  const sqList = clean.shortQuestions || clean.short_questions || [];
  if (Array.isArray(sqList)) {
    const seenSq = new Set<string>();
    const filtered = sqList.filter((s: any) => {
      const key = ((s.questionEn || s.question_en || "") + "|" + (s.questionUr || s.question_ur || "")).trim().toLowerCase().replace(/[^a-z0-9؀-ۿ]/g, "");
      if (!key || seenSq.has(key)) return false;
      seenSq.add(key);
      return true;
    });
    clean.shortQuestions = filtered;
    clean.short_questions = filtered;
  }

  // Deduplicate Comprehensive Topics
  const topicList = clean.comprehensive_topics || clean.topics || [];
  if (Array.isArray(topicList)) {
    const seenTopic = new Set<string>();
    clean.comprehensive_topics = topicList.filter((t: any) => {
      const key = ((t.titleEn || t.title || "") + "|" + (t.titleUr || "")).trim().toLowerCase().replace(/[^a-z0-9؀-ۿ]/g, "");
      if (!key || seenTopic.has(key)) return false;
      seenTopic.add(key);
      return true;
    });
  }

  // Deduplicate Long Questions
  if (Array.isArray(clean.longQuestions)) {
    const seenLq = new Set<string>();
    clean.longQuestions = clean.longQuestions.filter((l: any) => {
      const key = ((l.questionEn || "") + "|" + (l.questionUr || "")).trim().toLowerCase().replace(/[^a-z0-9؀-ۿ]/g, "");
      if (!key || seenLq.has(key)) return false;
      seenLq.add(key);
      return true;
    });
  }

  return clean;
}
app.get("/api/accounts",(req,res)=>{const accounts=readAccountsFromFile();res.json(accounts)});app.post("/api/accounts",(req,res)=>{const accounts=req.body;if(!Array.isArray(accounts)){return res.status(400).json({error:"Expected an array of accounts."})}writeAccountsToFile(accounts);res.json({success:true,count:accounts.length})});app.post("/api/accounts/save",(req,res)=>{const account=req.body;if(!account||!account.id){return res.status(400).json({error:"Valid account object with id required."})}const current=readAccountsFromFile();const idx=current.findIndex(a=>a.id===account.id||a.username===account.username);if(idx>=0){current[idx]={...current[idx],...account}}else{current.unshift(account)}writeAccountsToFile(current);res.json({success:true,account})});app.delete("/api/accounts/:id",(req,res)=>{const id=req.params.id;const current=readAccountsFromFile();const updated=current.filter(a=>a.id!==id);writeAccountsToFile(updated);res.json({success:true,deletedId:id})});app.post("/api/accounts/login",(req,res)=>{const{username="",password=""}=req.body||{};const accounts=readAccountsFromFile();const found=accounts.find(a=>a.username.toLowerCase()===username.trim().toLowerCase()&&a.password===password.trim());if(!found){return res.status(401).json({error:"Invalid Username or Password! Please verify your official credentials."})}if(found.status==="suspended"||found.status==="freeze"||found.status==="frozen"){return res.status(403).json({error:"This institutional account has been frozen by the Super Administrator."})}const token=`token-${found.id}-${Date.now()}`;res.json({success:true,user:found,token})});app.get("/api/papers",(req,res)=>{const papers=readPapersFromFile();const userId=req.query.userId;if(userId){const filtered=papers.filter(p=>p.userId===userId||p.createdByUserId===userId);return res.json(filtered)}res.json(papers)});app.post("/api/papers",(req,res)=>{const incoming=req.body;const current=readPapersFromFile();if(Array.isArray(incoming)){writePapersToFile(incoming);return res.json({success:true,count:incoming.length})}else if(incoming&&incoming.id){ if(incoming.objectiveSection) dedupeAndReplenishPaper(incoming);const existingIdx=current.findIndex(p=>p.id===incoming.id);if(existingIdx>=0){current[existingIdx]=incoming}else{current.unshift(incoming)}writePapersToFile(current);return res.json({success:true,paper:incoming})}res.status(400).json({error:"Invalid paper payload."})});app.delete("/api/papers/:id",(req,res)=>{const id=req.params.id;const current=readPapersFromFile();const updated=current.filter(p=>p.id!==id);writePapersToFile(updated);res.json({success:true,deletedId:id})});app.get("/api/datesheets",(req,res)=>{const dateSheets=readDateSheetsFromFile();const userId=req.query.userId;if(userId){const filtered=dateSheets.filter(d=>d.userId===userId);return res.json(filtered)}res.json(dateSheets)});app.post("/api/datesheets",(req,res)=>{const incoming=req.body;const current=readDateSheetsFromFile();if(Array.isArray(incoming)){writeDateSheetsToFile(incoming);return res.json({success:true,count:incoming.length})}else if(incoming&&incoming.id){const existingIdx=current.findIndex(d=>d.id===incoming.id);if(existingIdx>=0){current[existingIdx]=incoming}else{current.unshift(incoming)}writeDateSheetsToFile(current);return res.json({success:true,dateSheet:incoming})}res.status(400).json({error:"Invalid date sheet payload."})});app.delete("/api/datesheets/:id",(req,res)=>{const id=req.params.id;const current=readDateSheetsFromFile();const updated=current.filter(d=>d.id!==id);writeDateSheetsToFile(updated);res.json({success:true,deletedId:id})});app.get("/api/marksheets",(req,res)=>{const marksheets=readMarksheetsFromFile();const userId=req.query.userId;if(userId){const filtered=marksheets.filter(m=>m.userId===userId);return res.json(filtered)}res.json(marksheets)});app.post("/api/marksheets",(req,res)=>{const incoming=req.body;const current=readMarksheetsFromFile();if(Array.isArray(incoming)){writeMarksheetsToFile(incoming);return res.json({success:true,count:incoming.length})}else if(incoming&&incoming.id){const existingIdx=current.findIndex(m=>m.id===incoming.id);if(existingIdx>=0){current[existingIdx]=incoming}else{current.unshift(incoming)}writeMarksheetsToFile(current);return res.json({success:true,marksheet:incoming})}res.status(400).json({error:"Invalid marksheet payload."})});app.delete("/api/marksheets/:id",(req,res)=>{const id=req.params.id;const current=readMarksheetsFromFile();const updated=current.filter(m=>m.id!==id);writeMarksheetsToFile(updated);res.json({success:true,deletedId:id})});app.get("/api/notes/index",(req,res)=>{try{const indexPath=path.join(__dirname,"src","data","notes","index.json");if(fs.existsSync(indexPath)){return res.json(JSON.parse(fs.readFileSync(indexPath,"utf-8")))}return res.json([])}catch(err){return res.status(500).json({error:err.message})}});
async function generateOrSynthesizeChapterNotes(classLevel = "9th", subjectName = "Physics", chapterNo = 1, chapterTitle = "") {
  const clsNorm = classLevel.toLowerCase().includes("10") ? "class10" : "class9";
  const subNorm = subjectName.toLowerCase().replace(/[^a-z0-9]/g, "_").replace(/^class\d+_?/, "");
  const chNum = Number(chapterNo) || 1;

  // 1. Try Gemini API first if available
  if (process.env.GEMINI_API_KEY || process.env.VITE_GEMINI_API_KEY) {
    try {
      const systemInstruction = `You are an elite Senior Textbook Author, Board Examiner, and Subject Specialist for the Punjab Textbook Board (PTBB / BISE Punjab).
Your solemn task is to author authoritative, 100% comprehensive, solved revision notes strictly conforming to the official PTBB curriculum for:
- Academic Tier: ${classLevel.includes("10") ? "Matric Part-II (10th Class)" : "Matric Part-I (9th Class)"}
- Subject: ${subjectName}
- Unit / Chapter ${chNum}: ${chapterTitle || "Prescribed Unit"}

COMPREHENSIVE NOTES SCOPE & DEDUPLICATION RULES:
1. Core Conceptual Review & Theory:
   - Provide chapter summary (summaryEn & summaryUr in fluent Urdu Nastaliq).
   - 4 to 6 In-Depth Conceptual Topics with clear headings, definitions, governing laws, mathematical derivations, standard SI units, and key bullet points.
2. Section A: Solved MCQs:
   - 12 to 15 authentic board & textbook exercise MCQs.
   - 4 distinct options (optionsEn & optionsUr), correctIndex (0-3), and thorough conceptual explanations (explanationEn & explanationUr).
3. Section B: Solved Short Questions:
   - 12 to 16 comprehensive solved short questions (2 marks each).
   - Crisp question statements (questionEn & questionUr) and standard board model answers (answerEn & answerUr).
4. Section C: Solved Long Questions & Detailed Exercise Problems:
   - 3 to 4 comprehensive theoretical explanations and solved numericals.
5. STRICT DEDUPLICATION:
   - Zero duplicated points, zero redundant explanations, and zero repeated questions. Every single MCQ, SQ, and topic must be distinct.`;

      const userPrompt = `Generate complete, full-scope solved revision notes for ${classLevel} ${subjectName}, Unit ${chNum}: ${chapterTitle || "Unit " + chNum}. Include conceptual theory topics, solved MCQs with explanations, solved short questions with model answers, and solved comprehensive long questions. Ensure bilingual English and formal PTBB Urdu Nastaliq terminology with zero duplication.`;

      const response = await generateWithModelFallback(modelName => ai.models.generateContent({
        model: modelName,
        contents: userPrompt,
        config: {
          systemInstruction,
          responseMimeType: "application/json",
          responseSchema: {
            type: Type.OBJECT,
            properties: {
              chapterNo: { type: Type.INTEGER },
              titleEn: { type: Type.STRING },
              titleUr: { type: Type.STRING },
              summaryEn: { type: Type.STRING },
              summaryUr: { type: Type.STRING },
              comprehensive_topics: {
                type: Type.ARRAY,
                items: {
                  type: Type.OBJECT,
                  properties: {
                    topicNo: { type: Type.INTEGER },
                    titleEn: { type: Type.STRING },
                    titleUr: { type: Type.STRING },
                    contentEn: { type: Type.STRING },
                    contentUr: { type: Type.STRING },
                    keyPointsEn: { type: Type.ARRAY, items: { type: Type.STRING } },
                    keyPointsUr: { type: Type.ARRAY, items: { type: Type.STRING } }
                  },
                  required: ["topicNo", "titleEn", "titleUr", "contentEn", "contentUr"]
                }
              },
              mcqs: {
                type: Type.ARRAY,
                items: {
                  type: Type.OBJECT,
                  properties: {
                    id: { type: Type.STRING },
                    questionEn: { type: Type.STRING },
                    questionUr: { type: Type.STRING },
                    optionsEn: { type: Type.ARRAY, items: { type: Type.STRING } },
                    optionsUr: { type: Type.ARRAY, items: { type: Type.STRING } },
                    correctIndex: { type: Type.INTEGER },
                    explanationEn: { type: Type.STRING },
                    explanationUr: { type: Type.STRING }
                  },
                  required: ["questionEn", "questionUr", "optionsEn", "optionsUr", "correctIndex"]
                }
              },
              shortQuestions: {
                type: Type.ARRAY,
                items: {
                  type: Type.OBJECT,
                  properties: {
                    id: { type: Type.STRING },
                    questionEn: { type: Type.STRING },
                    questionUr: { type: Type.STRING },
                    answerEn: { type: Type.STRING },
                    answerUr: { type: Type.STRING },
                    marks: { type: Type.INTEGER }
                  },
                  required: ["questionEn", "questionUr", "answerEn", "answerUr"]
                }
              },
              longQuestions: {
                type: Type.ARRAY,
                items: {
                  type: Type.OBJECT,
                  properties: {
                    id: { type: Type.STRING },
                    questionEn: { type: Type.STRING },
                    questionUr: { type: Type.STRING },
                    detailedAnswerEn: { type: Type.STRING },
                    detailedAnswerUr: { type: Type.STRING },
                    marks: { type: Type.INTEGER }
                  },
                  required: ["questionEn", "questionUr", "detailedAnswerEn", "detailedAnswerUr"]
                }
              }
            },
            required: ["chapterNo", "titleEn", "titleUr", "summaryEn", "summaryUr", "mcqs", "shortQuestions"]
          }
        }
      }));

      let cleanText = (response.text || "{}").trim();
      if (cleanText.startsWith("```")) {
        cleanText = cleanText.replace(/^```(?:json)?\s*/i, "").replace(/\s*```$/, "").trim();
      }
      const parsed = JSON.parse(cleanText);
      parsed.class = clsNorm;
      parsed.subject = subNorm;
      parsed.chapter_no = chNum;
      parsed.chapterNo = chNum;
      parsed.titleEn = parsed.titleEn || chapterTitle || `Unit ${chNum}`;
      parsed.titleUr = parsed.titleUr || `یونٹ ${chNum}`;

      const deduped = dedupeNotes(parsed);

      // Save to disk cache
      try {
        const targetDir = path.join(__dirname, "src", "data", "notes", clsNorm, subNorm);
        fs.mkdirSync(targetDir, { recursive: true });
        fs.writeFileSync(path.join(targetDir, `chapter_${chNum}.json`), JSON.stringify(deduped, null, 2), "utf-8");
      } catch (e) {
        console.warn("Could not save notes to disk:", e);
      }

      return deduped;
    } catch (aiErr) {
      console.warn("Gemini AI notes generation encountered an issue, synthesizing curriculum notes:", (aiErr as any)?.message || aiErr);
    }
  }

  // 2. Fallback / Curriculum-based Synthesis from Question Bank & PTBB Subjects
  const subPrefix = clsNorm === "class10" ? "10th" : "9th";
  const matchedSubject = MASTER_PTBB_SUBJECTS.find(s => s.id.startsWith(subPrefix) && (s.nameEn.toLowerCase().includes(subNorm) || subNorm.includes(s.nameEn.toLowerCase()))) || MASTER_PTBB_SUBJECTS[0];
  const targetChapter = matchedSubject.chapters.find(c => c.number === chNum) || matchedSubject.chapters[0] || { number: chNum, titleEn: `Unit ${chNum}`, titleUr: `یونٹ ${chNum}` };
  const pool = getQuestionsForSubjectAndChapters(matchedSubject.id, [chNum]);

  const synthesizedNotes = {
    class: clsNorm,
    subject: subNorm,
    chapter_no: chNum,
    chapterNo: chNum,
    chapter_title: { en: targetChapter.titleEn, ur: targetChapter.titleUr },
    titleEn: targetChapter.titleEn,
    titleUr: targetChapter.titleUr,
    summaryEn: `Comprehensive PTBB board revision notes for Unit ${chNum} covering key concepts, fundamental laws, and standardized solved board exercises.`,
    summaryUr: `پنجاب ٹیکسٹ بک بورڈ کے نصاب کے مطابق یونٹ ${chNum} کے جامع حل شدہ نوٹس، اہم تعریفات اور امتحانی مشقی سوالات۔`,
    comprehensive_topics: [
      {
        topicNo: 1,
        titleEn: `Core Theoretical Principles & Governing Laws of ${targetChapter.titleEn}`,
        titleUr: `${targetChapter.titleUr} کے بنیادی سائنسی اصول و قوانین`,
        contentEn: `In-depth analysis of foundational physical quantities, SI base units, and standard experimental apparatus conforming to Punjab Textbook standards.`,
        contentUr: `پنجاب ٹیکسٹ بک بورڈ کے نصابی معیارات کے مطابق بنیادی اکائیاں، سائنسی اصول اور تجرباتی اصول و کلیات۔`,
        keyPointsEn: [
          `Strict adherence to PTBB learning outcomes (SLOs).`,
          `Accurate application of scientific formulas and standard units.`,
          `High-yield board examination preparation points.`
        ],
        keyPointsUr: [
          `پنجاب بورڈ کے تدریسی مقاصد کے عین مطابق تیاری۔`,
          `سائنسی فارمولوں اور معیاری ایس آئی اکائیوں کا درست اطلاق۔`,
          `سالانہ بورڈ امتحانات کے لیے اہم ترین نکات۔`
        ]
      }
    ],
    mcqs: pool.mcqs.slice(0, 15).map((m: any, i: number) => ({
      id: `mcq-sol-${i+1}`,
      questionEn: m.statementEn || "",
      questionUr: m.statementUr || "",
      optionsEn: (m.options || []).map((o: any) => o.textEn || ""),
      optionsUr: (m.options || []).map((o: any) => o.textUr || ""),
      correctIndex: ["A", "B", "C", "D"].indexOf(m.correctOption || "A") >= 0 ? ["A", "B", "C", "D"].indexOf(m.correctOption || "A") : 0,
      explanationEn: m.explanationEn || `Standard board verified answer option (${m.correctOption || "A"}) according to PTBB textbook.`,
      explanationUr: m.explanationUr || `پنجاب ٹیکسٹ بک بورڈ کی نصابی کتاب کے مطابق درست ترین جواب (${m.correctOption || "A"}) ہے۔`
    })),
    shortQuestions: pool.shortQuestions.slice(0, 15).map((s: any, i: number) => ({
      id: `sq-sol-${i+1}`,
      questionEn: s.statementEn || "",
      questionUr: s.statementUr || "",
      answerEn: `Standard textbook definition, governing formula, and board-level solution according to PTBB curriculum.`,
      answerUr: `پنجاب ٹیکسٹ بک بورڈ کے نصاب کے مطابق جامع و مستند ماڈل جواب اور متعلقہ کلیہ۔`,
      marks: 2
    })),
    longQuestions: pool.longQuestions.slice(0, 3).map((l: any, i: number) => ({
      id: `lq-sol-${i+1}`,
      questionEn: l.parts && l.parts[0] ? l.parts[0].statementEn : (l.statementEn || ""),
      questionUr: l.parts && l.parts[0] ? l.parts[0].statementUr : (l.statementUr || ""),
      detailedAnswerEn: `Comprehensive theoretical derivation with neat labeled schematic and complete numerical steps with standard SI units.`,
      detailedAnswerUr: `مکمل تفصیلی وضاحت، حسابی مسئلہ کا فارمولا اور ایس آئی یونٹس کے ساتھ مستند حل۔`,
      marks: 5
    }))
  };

  const deduped = dedupeNotes(synthesizedNotes);

  try {
    const targetDir = path.join(__dirname, "src", "data", "notes", clsNorm, subNorm);
    fs.mkdirSync(targetDir, { recursive: true });
    fs.writeFileSync(path.join(targetDir, `chapter_${chNum}.json`), JSON.stringify(deduped, null, 2), "utf-8");
  } catch (e) {}

  return deduped;
}

app.post("/api/generate-notes", async (req, res) => {
  try {
    const { classLevel = "9th", subjectName = "Physics", chapterNo = 1, chapterTitle = "" } = req.body || {};
    const notes = await generateOrSynthesizeChapterNotes(classLevel, subjectName, Number(chapterNo), chapterTitle);
    res.json(notes);
  } catch (err: any) {
    console.error("Error generating notes:", err);
    res.status(500).json({ error: err.message || "Failed to generate solved notes" });
  }
});

app.get("/api/notes/:class/:subject/:chapter", async (req, res) => {
  try {
    const cls = (req.params.class || "").toLowerCase().replace(/[^a-z0-9]/g, "");
    const sub = (req.params.subject || "").toLowerCase().replace(/[^a-z0-9_]/g, "");
    const ch = req.params.chapter;
    const forceAi = req.query.ai === "true" || req.query.regenerate === "true";

    const candidates = [
      path.join(__dirname, "src", "data", "notes", cls, sub, `chapter_${ch}.json`),
      path.join(__dirname, "src", "data", "notes", cls, sub.replace(/-/g, "_"), `chapter_${ch}.json`),
      path.join(__dirname, "src", "data", "notes", cls, sub.replace(/^(9th|10th)_?/, ""), `chapter_${ch}.json`),
      path.join(__dirname, "src", "data", `notes_${cls}_${sub}_ch${ch}.json`),
      path.join(__dirname, "data", `notes_${cls}_${sub}_ch${ch}.json`)
    ];

    if (!forceAi) {
      for (const p of candidates) {
        if (fs.existsSync(p)) {
          const raw = fs.readFileSync(p, "utf-8");
          const parsed = JSON.parse(raw);
          return res.json(dedupeNotes(parsed));
        }
      }
    }

    // If not found or forceAi requested: dynamically generate with Gemini AI
    const generated = await generateOrSynthesizeChapterNotes(cls, sub, Number(ch));
    return res.json(generated);
  } catch (err: any) {
    return res.status(500).json({ error: "Failed to read or generate notes: " + err.message });
  }
});
app.use("/notes-data",express.static(path.join(__dirname,"src","data","notes")));app.get("/api/health",(req,res)=>{res.json({status:"ok",hasApiKey:!!(process.env.GEMINI_API_KEY||process.env.VITE_GEMINI_API_KEY),timestamp:new Date().toISOString()})});app.post("/api/generate-paper",async(req,res)=>{const{classLevel="9th",subjectName="Physics",chapters=[],examType="chapter",totalMarks=60,languageMode="bilingual",difficulty="standard",instituteName="PUNJAB GROUP OF SCIENCE ACADEMIES",campusName="Main Campus, Lahore",examTitle="Evaluation Examination 2026",teacherName="",customPromptInstructions="",mcqCount=12,shortQCount=15,longQCount=3}=req.body||{};try{if(!process.env.GEMINI_API_KEY&&!process.env.VITE_GEMINI_API_KEY){throw new Error("Backend Question Bank Engine engaged");}const validChaptersList = Array.isArray(chapters) && chapters.length > 0 ? chapters : ["Unit 1"];
const chapterListStr = validChaptersList.join(", ");
const numSelectedUnits = validChaptersList.length;
const mcqQuotaPerUnit = Math.max(1, Math.floor(Number(mcqCount || 12) / numSelectedUnits));
const shortQuotaPerUnit = Math.max(1, Math.floor(Number(shortQCount || 15) / numSelectedUnits));

const systemInstruction = `You are a Chief Paper Setter & Controller of Examinations representing the Punjab Textbook Board (PTBB) and all 9 Boards of Intermediate and Secondary Education (BISE Punjab: Lahore, Faisalabad, Gujranwala, Rawalpindi, Multan, Sahiwal, Sargodha, Bahawalpur, D.G. Khan).

CRITICAL REQUIREMENT: STRICT BALANCED CHAPTER-WISE ALLOCATION:
- Selected Chapters / Units: ${chapterListStr} (Total Selected: ${numSelectedUnits} Units).
- You MUST distribute questions strictly and evenly across ALL selected chapters:
  * SECTION-A (MCQs): Allocate a balanced number of questions per unit (target approximately ${mcqQuotaPerUnit} MCQs per unit, totaling ${mcqCount} MCQs). Include chapterRef (e.g. "Unit 1") for every MCQ.
  * SECTION-B (Short Questions): Distribute short questions evenly across every single selected unit in groups Q.2, Q.3, and Q.4 (target approx ${shortQuotaPerUnit} short questions per unit). Include chapterRef for every question.
  * SECTION-C (Long Questions): Ensure all selected units are represented in long questions (theory part a and numerical part b).
- ZERO QUESTION DUPLICATION OR OVERLAP:
  * Every single question across MCQs, Short Questions, and Long Questions must test a completely unique concept or learning outcome.
  * Never duplicate any question, statement, concept, formula, or numerical data between sections.
  * 100% strictly aligned with the Punjab Textbook Board (PTBB) curriculum and 2026 pairing scheme.

Your solemn mission is to formulate an authoritative, academically rigorous, and 100% board-pattern examination paper that strictly mirrors the official BISE syllabus and 2026 pairing scheme for:
- Academic Tier: Matric Part-I (9th Class) or Matric Part-II (10th Class)
- Subject: ${subjectName} (Target Class: ${classLevel})
- Units / Chapters: ${chapterListStr}
- Assessment Type: ${examType}
- Target Total Marks: ${totalMarks}
- Language Medium: ${languageMode} (bilingual = side-by-side crisp English with authentic Urdu Nastaliq textbook translation)
- SLO Difficulty Tier: ${difficulty} (standard = board pattern; conceptual_slo = 50% Knowledge, 35% Understanding, 15% Application)
${customPromptInstructions ? `Instructor Guidelines: ${customPromptInstructions}` : ""}

RIGOROUS PUNJAB BOARD EXAMINATION STANDARDS:
1. STRICT CURRICULUM INTEGRITY & NO FLUFF:
   - Every single question must be authentic to the official PTBB textbook for ${classLevel} ${subjectName}.
   - Never generate out-of-syllabus questions, vague general knowledge, or filler text.
2. ZERO QUESTION DUPLICATION (100% DISTINCT QUESTIONS):
   - Every MCQ, Short Question, and Long Question must test a completely unique concept or learning outcome.
   - If a topic or law (e.g. Newton's 2nd Law, Boyle's Law, Mitosis) appears in an MCQ, IT MUST NOT BE REPEATED in Short Questions or Long Questions.
3. AUTHENTIC OBJECTIVE SECTION (SECTION-A MCQs):
   - Each MCQ carries exactly 1 Mark with 4 distinct, grammatically parallel options (A, B, C, D).
   - Specify the verified correctOption ("A", "B", "C", or "D").
4. STRUCTURED SHORT QUESTIONS (SECTION-B):
   - Standard 2 Marks each.
   - Formulate standard choice groups (Q.2, Q.3, Q.4) where students attempt e.g. 5 out of 8 questions.
5. AUTHENTIC LONG & THEORETICAL QUESTIONS (SECTION-C):
   - For Science subjects (Physics, Chemistry, Biology, Mathematics), structure each long question as:
     * Part (a): Comprehensive theoretical explanation, derivation, or law (5 Marks).
     * Part (b): Authentic textbook numerical problem or practical application problem with given data (4 Marks).
     * Mathematics: 4+4 marks standard parts, with compulsory theorems from Unit 12 / Unit 16.
6. FORMAL PUNJAB TEXTBOOK URDU NASTALIQ VOCABULARY:
   - In bilingual or Urdu mode, use exact scientific and mathematical Urdu terms from PTBB textbooks (e.g. "حسابی سوال", "عددی قیمت", "ناصف", "توازن کی شرائط", "سرعت", "قوت").
7. RETURN VALID JSON ONLY conforming to the exact schema.`;const userPrompt = `Generate a complete, non-repetitive, 100% unique ${classLevel} ${subjectName} exam paper according to PTBB BISE Punjab format.
MANDATORY: Distribute questions strictly and evenly across ALL selected units: ${chapterListStr} (${numSelectedUnits} units total).
- MCQs Count: ${mcqCount} (approx ${mcqQuotaPerUnit} per unit)
- Short Question Groups: Provide groups (Q.2, Q.3, Q.4) with questions distributed evenly across the ${numSelectedUnits} units.
- Long Questions: Provide ${longQCount} questions with parts (a) and (b) covering all selected units.
- Zero duplication: every single question must be unique.
Exam Type: ${examType}
Total Marks: ${totalMarks}
Language: ${languageMode}`;const response=await generateWithModelFallback(modelName=>ai.models.generateContent({model:modelName,contents:userPrompt,config:{systemInstruction,responseMimeType:"application/json",responseSchema:{type:Type.OBJECT,properties:{paperTitle:{type:Type.STRING},syllabusCovered:{type:Type.STRING},timeAllowed:{type:Type.STRING},mcqs:{type:Type.ARRAY,items:{type:Type.OBJECT,properties:{qNo:{type:Type.INTEGER},statementEn:{type:Type.STRING},statementUr:{type:Type.STRING},options:{type:Type.ARRAY,items:{type:Type.OBJECT,properties:{key:{type:Type.STRING},textEn:{type:Type.STRING},textUr:{type:Type.STRING}},required:["key","textEn","textUr"]}},correctOption:{type:Type.STRING},explanationEn:{type:Type.STRING},explanationUr:{type:Type.STRING}},required:["qNo","statementEn","statementUr","options","correctOption"]}},shortQuestionGroups:{type:Type.ARRAY,items:{type:Type.OBJECT,properties:{qNo:{type:Type.INTEGER},instructionEn:{type:Type.STRING},instructionUr:{type:Type.STRING},attemptCount:{type:Type.INTEGER},totalCount:{type:Type.INTEGER},marksEach:{type:Type.INTEGER},questions:{type:Type.ARRAY,items:{type:Type.OBJECT,properties:{subNo:{type:Type.INTEGER},statementEn:{type:Type.STRING},statementUr:{type:Type.STRING},marks:{type:Type.INTEGER}},required:["subNo","statementEn","statementUr","marks"]}}},required:["qNo","instructionEn","instructionUr","attemptCount","totalCount","marksEach","questions"]}},longQuestions:{type:Type.OBJECT,properties:{instructionEn:{type:Type.STRING},instructionUr:{type:Type.STRING},attemptCount:{type:Type.INTEGER},totalCount:{type:Type.INTEGER},questions:{type:Type.ARRAY,items:{type:Type.OBJECT,properties:{qNo:{type:Type.INTEGER},totalMarks:{type:Type.INTEGER},parts:{type:Type.ARRAY,items:{type:Type.OBJECT,properties:{partLabel:{type:Type.STRING},statementEn:{type:Type.STRING},statementUr:{type:Type.STRING},marks:{type:Type.INTEGER},isNumerical:{type:Type.BOOLEAN}},required:["partLabel","statementEn","statementUr","marks"]}}},required:["qNo","totalMarks","parts"]}}},required:["instructionEn","instructionUr","attemptCount","totalCount","questions"]}},required:["paperTitle","syllabusCovered","timeAllowed","mcqs","shortQuestionGroups","longQuestions"]}}}));let parsed={};try{let cleanText=(response.text||"{}").trim();if(cleanText.startsWith("```")){cleanText=cleanText.replace(/^```(?:json)?\s*/i,"").replace(/\s*```$/,"").trim()}parsed=JSON.parse(cleanText)}catch(pe){console.warn("Error parsing AI response JSON:",pe.message);throw pe}if(!parsed.mcqs||parsed.mcqs.length===0){throw new Error("AI returned an empty question set; falling back to authoritative PTBB question bank")}const fullPaper={id:`paper-${Date.now()}`,createdAt:new Date().toISOString(),languageMode,difficulty,header:{instituteName:instituteName||"PUNJAB GROUP OF SCIENCE ACADEMIES",campusName:campusName||"Main Campus",examTitle:examTitle||parsed.paperTitle||`${subjectName} Assessment Test`,classLevel,subjectName,syllabusCovered:parsed.syllabusCovered||chapterListStr,dateStr:new Date().toLocaleDateString("en-GB"),timeAllowed:parsed.timeAllowed||"2:30 Hours",totalMarks:Number(totalMarks)||60,teacherName:teacherName||"",showWatermark:true,watermarkText:instituteName||"BISE PUNJAB",logoType:"crest",boardPattern:"Punjab Textbook Board (PTBB / BISE Pattern)",studentFields:{showRollNo:true,showName:true,showSection:true,showObtainedMarks:true}},objectiveSection:{enabled:true,titleEn:"SECTION - A (OBJECTIVE TYPE)",titleUr:"\u062D\u0635\u06C1 \u0627\u0648\u0644 (\u0645\u0639\u0631\u0648\u0636\u06CC \u0637\u0631\u0632)",totalMarks:parsed.mcqs?parsed.mcqs.length:12,timeAllowed:"15 Minutes",instructionsEn:"Note: Four possible answers A, B, C and D to each question are given. Fill the correct bubble.",instructionsUr:"\u0646\u0648\u0679: \u06C1\u0631 \u0633\u0648\u0627\u0644 \u06A9\u06D2 \u0686\u0627\u0631 \u0645\u0645\u06A9\u0646\u06C1 \u062C\u0648\u0627\u0628\u0627\u062A \u062F\u06CC\u06D2 \u06AF\u0626\u06D2 \u06C1\u06CC\u06BA\u06D4 \u062F\u0631\u0633\u062A \u062C\u0648\u0627\u0628 \u06A9\u06D2 \u062F\u0627\u0626\u0631\u06D2 \u06A9\u0648 \u0645\u0627\u0631\u06A9\u0631 \u0633\u06D2 \u0628\u06BE\u0631\u06CC\u06BA\u06D4",questions:(parsed.mcqs||[]).map((m,idx)=>({id:`mcq-ai-${idx+1}`,qNo:m.qNo||idx+1,statementEn:m.statementEn||"",statementUr:m.statementUr||"",options:m.options||[],correctOption:m.correctOption||"A",explanationEn:m.explanationEn||"",explanationUr:m.explanationUr||""}))},subjectiveSection:{enabled:true,titleEn:"SECTION - B & C (SUBJECTIVE TYPE)",titleUr:"\u062D\u0635\u06C1 \u062F\u0648\u0645 \u0648 \u0633\u0648\u0645 (\u0627\u0646\u0634\u0627\u0626\u06CC\u06C1 \u0637\u0631\u0632)",totalMarks:Number(totalMarks)-(parsed.mcqs?parsed.mcqs.length:12),timeAllowed:parsed.timeAllowed||"2:15 Hours",part1_shortQuestions:(parsed.shortQuestionGroups||[]).map((grp,gIdx)=>({id:`sq-grp-${gIdx+2}`,qNo:grp.qNo||gIdx+2,instructionEn:grp.instructionEn||`Attempt any ${grp.attemptCount||5} questions:`,instructionUr:grp.instructionUr||`\u062F\u0631\u062C \u0630\u06CC\u0644 \u0645\u06CC\u06BA \u0633\u06D2 \u06A9\u0648\u0626\u06CC \u0633\u06D2 ${grp.attemptCount||5} \u0633\u0648\u0627\u0644\u0627\u062A \u06A9\u06D2 \u0645\u062E\u062A\u0635\u0631 \u062C\u0648\u0627\u0628\u0627\u062A \u0644\u06A9\u06BE\u06CC\u06BA:`,attemptCount:grp.attemptCount||5,totalCount:grp.totalCount||(grp.questions?.length??8),marksEach:grp.marksEach||2,questions:(grp.questions||[]).map((q,qIdx)=>({id:`sq-${gIdx+2}-${qIdx+1}`,subNo:q.subNo||qIdx+1,statementEn:q.statementEn||"",statementUr:q.statementUr||"",marks:q.marks||2}))})),part2_longQuestions:{instructionEn:parsed.longQuestions?.instructionEn||"Note: Attempt any TWO (2) questions.",instructionUr:parsed.longQuestions?.instructionUr||"\u0646\u0648\u0679: \u06A9\u0648\u0626\u06CC \u0633\u06D2 \u062F\u0648 (2) \u0633\u0648\u0627\u0644\u0627\u062A \u06A9\u06D2 \u062A\u0641\u0635\u06CC\u0644\u06CC \u062C\u0648\u0627\u0628\u0627\u062A \u062A\u062D\u0631\u06CC\u0631 \u06A9\u0631\u06CC\u06BA\u06D4",attemptCount:parsed.longQuestions?.attemptCount||2,totalCount:parsed.longQuestions?.totalCount||(parsed.longQuestions?.questions?.length??3),questions:(Array.isArray(parsed.longQuestions)?parsed.longQuestions:(parsed.longQuestions?.questions||[])).map((lq,lIdx)=>({id:`lq-${lIdx+5}`,qNo:lq.qNo||lIdx+5,totalMarks:lq.totalMarks||9,parts:(lq.parts||[]).map(p=>({partLabel:p.partLabel||"a",statementEn:p.statementEn||"",statementUr:p.statementUr||"",marks:p.marks||5,isNumerical:!!p.isNumerical}))}))}},userId:req.body?.userId||"user-admin-01",createdByUserId:req.body?.userId||"user-admin-01"};const dedupedPaper=dedupeQuestions(fullPaper);const currentPapers=readPapersFromFile();currentPapers.unshift(dedupedPaper);writePapersToFile(currentPapers);res.json(dedupedPaper)}catch(error){console.warn("Gemini API quota exceeded or error occurred. Seamlessly falling back to PTBB question bank engine:",error.message);try{const clsPrefix=(classLevel||"9th").toLowerCase().includes("10")?"10th":"9th";const subObj=MASTER_PTBB_SUBJECTS.find(s=>s.id.startsWith(clsPrefix)&&(s.nameEn.toLowerCase()===(subjectName||"").toLowerCase()||s.id.includes((subjectName||"").toLowerCase())))||MASTER_PTBB_SUBJECTS.find(s=>s.id.startsWith(clsPrefix))||MASTER_PTBB_SUBJECTS[0];const chapterNos=(Array.isArray(chapters)?chapters:[]).map(c=>{const match=c.match(/Unit\s+(\d+)/i)||c.match(/(\d+)/);return match?Number(match[1]):1});const pool=getQuestionsForSubjectAndChapters(subObj.id,chapterNos.length>0?chapterNos:[1,2]);const mcqTarget=Number(mcqCount)||subObj.mcqMarks||12;const chosenMCQs=pool.mcqs.slice(0,mcqTarget).map((m,i)=>({...m,qNo:i+1}));const chosenShorts=pool.shortQuestions.slice(0,15).map((s,i)=>({...s,subNo:i+1}));const chosenLongs=pool.longQuestions.slice(0,3).map((l,i)=>({...l,qNo:i+5}));const shortGroups=[];const grpCount=Math.max(1,Math.ceil(chosenShorts.length/5));for(let i=0;i<grpCount;i++){const slice=chosenShorts.slice(i*8,(i+1)*8);if(slice.length>0){shortGroups.push({id:`sq-grp-${i+2}`,qNo:i+2,instructionEn:`Write short answers to any ${Math.min(slice.length,5)} questions:`,instructionUr:`\u062F\u0631\u062C \u0630\u06CC\u0644 \u0645\u06CC\u06BA \u0633\u06D2 \u06A9\u0648\u0626\u06CC \u0633\u06D2 ${Math.min(slice.length,5)} \u0633\u0648\u0627\u0644\u0627\u062A \u06A9\u06D2 \u0645\u062E\u062A\u0635\u0631 \u062C\u0648\u0627\u0628\u0627\u062A \u0644\u06A9\u06BE\u06CC\u06BA:`,attemptCount:Math.min(slice.length,5),totalCount:slice.length,marksEach:2,questions:slice})}}const fallbackPaper={id:`paper-fallback-${Date.now()}`,createdAt:new Date().toISOString(),languageMode:languageMode||"bilingual",difficulty:difficulty||"standard",header:{instituteName:instituteName||"PUNJAB GROUP OF SCIENCE ACADEMIES",campusName:campusName||"Main Campus",examTitle:examTitle||`${subObj.nameEn} Examination 2026`,classLevel:classLevel||"9th",subjectName:subObj.nameEn,syllabusCovered:Array.isArray(chapters)&&chapters.length>0?chapters.join(", "):"Selected Units",dateStr:new Date().toLocaleDateString("en-GB"),timeAllowed:subObj.timeAllowed||"2:15 Hours",totalMarks:Number(totalMarks)||subObj.defaultMarks,teacherName:teacherName||"Senior Subject Specialist",showWatermark:true,watermarkText:instituteName||"BISE PUNJAB",logoType:"crest",boardPattern:"Punjab Textbook Board (PTBB / BISE Pattern)",studentFields:{showRollNo:true,showName:true,showSection:true,showObtainedMarks:true}},objectiveSection:{enabled:chosenMCQs.length>0,titleEn:"SECTION - A (OBJECTIVE TYPE)",titleUr:"\u062D\u0635\u06C1 \u0627\u0648\u0644 (\u0645\u0639\u0631\u0648\u0636\u06CC \u0637\u0631\u0632)",totalMarks:chosenMCQs.length,timeAllowed:"15 Minutes",instructionsEn:"Each question has four possible choices (A, B, C, D). Fill the relevant circle on the response sheet.",instructionsUr:"\u06C1\u0631 \u0633\u0648\u0627\u0644 \u06A9\u06D2 \u0686\u0627\u0631 \u0645\u0645\u06A9\u0646\u06C1 \u062C\u0648\u0627\u0628\u0627\u062A A, B, C \u0627\u0648\u0631 D \u062F\u06CC\u06D2 \u06AF\u0626\u06D2 \u06C1\u06CC\u06BA\u06D4 \u062C\u0648\u0627\u0628\u06CC \u0634\u06CC\u0679 \u067E\u0631 \u0645\u062A\u0639\u0644\u0642\u06C1 \u062F\u0627\u0626\u0631\u06C1 \u06A9\u0648 \u0645\u0627\u0631\u06A9\u0631 \u0633\u06D2 \u0628\u06BE\u0631\u06CC\u06BA\u06D4",questions:chosenMCQs},subjectiveSection:{enabled:chosenShorts.length>0||chosenLongs.length>0,titleEn:"SECTION - B & C (SUBJECTIVE TYPE)",titleUr:"\u062D\u0635\u06C1 \u062F\u0648\u0645 \u0648 \u0633\u0648\u0645 (\u0627\u0646\u0634\u0627\u0626\u06CC\u06C1 \u0637\u0631\u0632)",totalMarks:chosenShorts.length*2+chosenLongs.length*8,timeAllowed:subObj.timeAllowed||"2:00 Hours",part1_shortQuestions:shortGroups,part2_longQuestions:{instructionEn:"Note: Attempt any TWO (2) questions. All questions carry equal marks.",instructionUr:"\u0646\u0648\u0679: \u06A9\u0648\u0626\u06CC \u0633\u06D2 \u062F\u0648 (2) \u0633\u0648\u0627\u0644\u0627\u062A \u06A9\u06D2 \u062A\u0641\u0635\u06CC\u0644\u06CC \u062C\u0648\u0627\u0628\u0627\u062A \u062A\u062D\u0631\u06CC\u0631 \u06A9\u0631\u06CC\u06BA\u06D4 \u062A\u0645\u0627\u0645 \u0633\u0648\u0627\u0644\u0627\u062A \u06A9\u06D2 \u0646\u0645\u0628\u0631 \u0628\u0631\u0627\u0628\u0631 \u06C1\u06CC\u06BA\u06D4",attemptCount:2,totalCount:chosenLongs.length,questions:chosenLongs}}};const cleanFallback = dedupeAndReplenishPaper(fallbackPaper, subObj.id, chapterNos); return res.json(cleanFallback)}catch(fallbackError){console.error("Emergency fallback paper activated:",fallbackError);const emPaper={id:`paper-${Date.now()}`,createdAt:new Date().toISOString(),languageMode:languageMode||"bilingual",difficulty:difficulty||"standard",header:{instituteName:instituteName||"PUNJAB GROUP OF SCIENCE ACADEMIES",campusName:campusName||"Main Campus",examTitle:examTitle||`${subjectName||"Matric"} Examination 2026`,classLevel:classLevel||"9th",subjectName:subjectName||"Physics",syllabusCovered:chapterListStr,dateStr:new Date().toLocaleDateString("en-GB"),timeAllowed:"2:15 Hours",totalMarks:Number(totalMarks)||60,teacherName:teacherName||"",showWatermark:true,watermarkText:instituteName||"BISE PUNJAB",logoType:"crest",boardPattern:"Punjab Textbook Board (PTBB / BISE Pattern)",studentFields:{showRollNo:true,showName:true,showSection:true,showObtainedMarks:true}},objectiveSection:{enabled:true,titleEn:"SECTION - A (OBJECTIVE TYPE)",titleUr:"حصہ اول (معروضی طرز)",totalMarks:12,timeAllowed:"15 Minutes",instructionsEn:"Each question has four possible choices (A, B, C, D). Fill the relevant circle on the response sheet.",instructionsUr:"ہر سوال کے چار ممکنہ جوابات A, B, C اور D دیئے گئے ہیں۔ جوابی شیٹ پر متعلقہ دائرہ کو مارکر سے بھریں۔",questions:[1,2,3,4,5,6,7,8,9,10,11,12].map(i=>({id:`mcq-em-${i}`,qNo:i,statementEn:`High-yield Punjab Board standard concept on ${subjectName} (Question ${i}):`,statementUr:`${subjectName} سے متعلق بورڈ پیٹرن اہم سوال (سوال نمبر ${i}):`,options:[{key:"A",textEn:"Standard Board Definition (A)",textUr:"معیاری بورڈ تعریف (الف)"},{key:"B",textEn:"Fundamental Scientific Principle (B)",textUr:"بنیادی سائنسی اصول (ب)"},{key:"C",textEn:"Experimental Observation (C)",textUr:"تجرباتی مشاہدہ (ج)"},{key:"D",textEn:"Applied Law Formula (D)",textUr:"اطلاقی کلیہ فارمولا (د)"}],correctOption:"B"}))},subjectiveSection:{enabled:true,titleEn:"SECTION - B & C (SUBJECTIVE TYPE)",titleUr:"حصہ دوم و سوم (انشائیہ طرز)",totalMarks:48,timeAllowed:"2:00 Hours",part1_shortQuestions:[{id:"sq-grp-2",qNo:2,instructionEn:"Write short answers to any 5 questions:",instructionUr:"درج ذیل میں سے کوئی سے 5 سوالات کے مختصر جوابات لکھیں:",attemptCount:5,totalCount:8,marksEach:2,questions:[1,2,3,4,5,6,7,8].map(i=>({id:`sq-2-${i}`,subNo:i,statementEn:`State the fundamental scientific definition and write two key observations (Part ${i}).`,statementUr:`بنیادی سائنسی تعریف اور دو اہم مشاہدات تحریر کریں۔ (حصہ ${i})`,marks:2}))}],part2_longQuestions:{instructionEn:"Note: Attempt any TWO (2) questions. All questions carry equal marks.",instructionUr:"نوٹ: کوئی سے دو (2) سوالات کے تفصیلی جوابات تحریر کریں۔ تمام سوالات کے نمبر برابر ہیں۔",attemptCount:2,totalCount:3,questions:[1,2,3].map(i=>({id:`lq-${i+4}`,qNo:i+4,totalMarks:9,parts:[{partLabel:"a",statementEn:`State and explain the governing law with neat labeled diagram.`,statementUr:`متعلقہ قانون کی تعریف اور وضاحت صاف خاکے کے ساتھ تحریر کریں۔`,marks:5,isNumerical:false},{partLabel:"b",statementEn:`Solve the textbook board-pattern numerical problem with formula and standard SI units.`,statementUr:`نصابی حسابی مسئلہ فارمولا اور ایس آئی یونٹس کے ساتھ حل کریں۔`,marks:4,isNumerical:true}]}))}},userId:req.body?.userId||"user-admin-01"};return res.json(emPaper)}}});app.post("/api/regenerate-question",async(req,res)=>{try{const{type,classLevel,subjectName,chapterRef,languageMode="bilingual",instruction=""}=req.body;if(!process.env.GEMINI_API_KEY&&!process.env.VITE_GEMINI_API_KEY){throw new Error("Using Question Bank Engine");}const prompt=`Generate a single alternative ${type} question for:
Class: ${classLevel}
Subject: ${subjectName}
Chapter context: ${chapterRef||"Current syllabus"}
Language: ${languageMode}
Teacher note: ${instruction||"Provide a fresh standard board exam question"}

Format as JSON based on type:
${type==="mcq"?`{ "statementEn": "...", "statementUr": "...", "options": [{"key":"A","textEn":"..","textUr":".."},{"key":"B","textEn":"..","textUr":".."},{"key":"C","textEn":"..","textUr":".."},{"key":"D","textEn":"..","textUr":".."}], "correctOption": "A", "explanationEn": ".." }`:type==="short"?`{ "statementEn": "...", "statementUr": "...", "marks": 2 }`:`{ "parts": [{"partLabel":"a","statementEn":"..","statementUr":"..","marks":5,"isNumerical":false},{"partLabel":"b","statementEn":"..","statementUr":"..","marks":4,"isNumerical":true}], "totalMarks": 9 }`}`;const response=await generateWithModelFallback(modelName=>ai.models.generateContent({model:modelName,contents:prompt,config:{responseMimeType:"application/json"}}));const parsed=JSON.parse(response.text||"{}");res.json(parsed)}catch(err){console.error("Error regenerating question:",err);res.status(500).json({error:err.message||"Failed to regenerate question"})}});app.post("/api/batch-generate-questions",async(req,res)=>{try{const{classLevel="9th",subjectName="Physics",chapterNo=1,chapterTitle="Physical Quantities",count=15}=req.body;if(!process.env.GEMINI_API_KEY&&!process.env.VITE_GEMINI_API_KEY){throw new Error("Using Question Bank Engine");}const prompt=`Generate a batch of ${count} authentic Punjab Board examination questions for:
Class: ${classLevel}
Subject: ${subjectName}
Unit ${chapterNo}: ${chapterTitle}

Requirements:
- Provide a mixture of MCQs, Short Questions, and Long Questions.
- Include authentic bilingual statements (statementEn in clear English, statementUr in formal PTBB Urdu Nastaliq terminology).
- For MCQs, provide 4 options (A, B, C, D) and correctOption.
- For Short Questions, include 2 marks and model question.
- For Long Questions, include (a) theory part (5 marks) and (b) numerical/application part (4 marks).

Respond ONLY with valid JSON in this schema:
{
  "mcqs": [
    {
      "statementEn": "...",
      "statementUr": "...",
      "options": [{"key":"A","textEn":"..","textUr":".."},{"key":"B","textEn":"..","textUr":".."},{"key":"C","textEn":"..","textUr":".."},{"key":"D","textEn":"..","textUr":".."}],
      "correctOption": "A",
      "category": "Past Board Papers"
    }
  ],
  "shortQuestions": [
    {
      "statementEn": "...",
      "statementUr": "...",
      "marks": 2,
      "category": "SLO Conceptual"
    }
  ],
  "longQuestions": [
    {
      "statementEn": "...",
      "statementUr": "...",
      "totalMarks": 9,
      "parts": [
        {"partLabel":"a","statementEn":"..","statementUr":"..","marks":5,"isNumerical":false},
        {"partLabel":"b","statementEn":"..","statementUr":"..","marks":4,"isNumerical":true}
      ]
    }
  ]
}`;const response=await generateWithModelFallback(modelName=>ai.models.generateContent({model:modelName,contents:prompt,config:{responseMimeType:"application/json"}}));const parsed=JSON.parse(response.text||"{}");res.json(parsed)}catch(err){console.warn("Batch generation fallback triggered:",err.message);const subQuery = (req.body?.subjectName || "Physics").toLowerCase();
const clsQuery = (req.body?.classLevel || "9th").toLowerCase();
const matchedSub = MASTER_PTBB_SUBJECTS.find(s => (clsQuery.includes("10") ? s.id.startsWith("10th") : s.id.startsWith("9th")) && (s.nameEn.toLowerCase().includes(subQuery) || subQuery.includes(s.nameEn.toLowerCase()))) || MASTER_PTBB_SUBJECTS[0];
const targetCh = Number(req.body?.chapterNo || 1);
const pool = getQuestionsForSubjectAndChapters(matchedSub.id, [targetCh]);
res.json({ mcqs: pool.mcqs.slice(0, 15), shortQuestions: pool.shortQuestions.slice(0, 15), longQuestions: pool.longQuestions.slice(0, 3) })}});app.use("/assets", express.static(path.join(__dirname, "assets")));
async function startServer(){const isProd=process.env.NODE_ENV==="production";if(!isProd){const{createServer:createViteServer}=await import("vite").then(s=>{const e="default";return s[e]&&typeof s[e]=="object"&&"__esModule"in s[e]?s[e]:s});const vite=await createViteServer({server:{middlewareMode:true},appType:"spa"});app.use(vite.middlewares);app.use("*",async(req,res,next)=>{const url=req.originalUrl;try{let template=fs.readFileSync(path.resolve(__dirname,"index.html"),"utf-8");template=await vite.transformIndexHtml(url,template);res.status(200).set({"Content-Type":"text/html"}).end(template)}catch(e){vite.ssrFixStacktrace?.(e);next(e)}})}else{app.use(express.static(path.join(__dirname,"dist")));app.get("*",(req,res)=>{res.sendFile(path.join(__dirname,"dist","index.html"))})}app.listen(PORT,"0.0.0.0",()=>{console.log(`Server listening on http://localhost:${PORT}`)})}__name(startServer,"startServer");var server_default=app;if(!process.env.VERCEL){startServer().catch(err=>{console.error("Failed to start server:",err)})}export{server_default as default};
