var __defProp=Object.defineProperty;var __name=(target,value)=>__defProp(target,"name",{value,configurable:true});import{PTBB_SUBJECTS}from"./ptbbData.ts";import{generateMassiveQuestionPoolForChapter}from"./massiveQuestionBankEngine.ts";import{PTBB_CHAPTER_QUESTIONS}from"./ptbbMasterQuestionBank.ts";const ADDITIONAL_PTBB_SUBJECTS=[{id:"10th-english",nameEn:"English Compulsory",nameUr:"English Compulsory",classLevel:"10th",group:"general",defaultMarks:75,mcqMarks:19,shortQMarks:10,longQMarks:46,timeAllowed:"2:30 Hours",chapters:[{id:1,number:1,titleEn:"Hazrat Muhammad (PBUH) An Embodiment of Justice",titleUr:"\u062D\u0636\u0631\u062A \u0645\u062D\u0645\u062F \uFDFA - \u067E\u06CC\u06A9\u0631\u0650 \u0639\u062F\u0644 \u0648 \u0627\u0646\u0635\u0627\u0641"},{id:2,number:2,titleEn:"Chinese New Year",titleUr:"\u0686\u06CC\u0646\u06CC \u0646\u06CC\u0627 \u0633\u0627\u0644"},{id:3,number:3,titleEn:"Try Again (Poem)",titleUr:"\u062F\u0648\u0628\u0627\u0631\u06C1 \u06A9\u0648\u0634\u0634 \u06A9\u0631\u0648 (\u0646\u0638\u0645)"},{id:4,number:4,titleEn:"First Aid",titleUr:"\u0627\u0628\u062A\u062F\u0627\u0626\u06CC \u0637\u0628\u06CC \u0627\u0645\u062F\u0627\u062F"},{id:5,number:5,titleEn:"The Rain (Poem)",titleUr:"\u0628\u0627\u0631\u0634 (\u0646\u0638\u0645)"},{id:6,number:6,titleEn:"Television vs Newspapers",titleUr:"\u0679\u06CC\u0644\u06CC \u0648\u06CC\u0698\u0646 \u0628\u0645\u0642\u0627\u0628\u0644\u06C1 \u0627\u062E\u0628\u0627\u0631\u0627\u062A"},{id:7,number:7,titleEn:"Little by Little One Walks Far",titleUr:"\u0631\u0641\u062A\u06C1 \u0631\u0641\u062A\u06C1 \u0645\u0646\u0632\u0644 \u062A\u06A9 \u0631\u0633\u0627\u0626\u06CC"},{id:8,number:8,titleEn:"Peace (Poem)",titleUr:"\u0627\u0645\u0646 \u0648 \u0633\u06A9\u0648\u0646 (\u0646\u0638\u0645)"},{id:9,number:9,titleEn:"Selecting the Right Career",titleUr:"\u0635\u062D\u06CC\u062D \u067E\u06CC\u0634\u06C1 \u06A9\u0627 \u0627\u0646\u062A\u062E\u0627\u0628"},{id:10,number:10,titleEn:"A World Without Books",titleUr:"\u06A9\u062A\u0627\u0628\u0648\u06BA \u06A9\u06D2 \u0628\u063A\u06CC\u0631 \u062F\u0646\u06CC\u0627"},{id:11,number:11,titleEn:"Great Expectations",titleUr:"\u0639\u0638\u06CC\u0645 \u062A\u0648\u0642\u0639\u0627\u062A"},{id:12,number:12,titleEn:"Population Growth and World Food Supplies",titleUr:"\u0622\u0628\u0627\u062F\u06CC \u0645\u06CC\u06BA \u0627\u0636\u0627\u0641\u06C1 \u0627\u0648\u0631 \u063A\u0630\u0627\u0626\u06CC \u0648\u0633\u0627\u0626\u0644"},{id:13,number:13,titleEn:"Faithfulness",titleUr:"\u0648\u0641\u0627\u062F\u0627\u0631\u06CC"}]},{id:"10th-urdu",nameEn:"Urdu Compulsory",nameUr:"\u0627\u0631\u062F\u0648 (\u062F\u0633\u0648\u06CC\u06BA \u062C\u0645\u0627\u0639\u062A)",classLevel:"10th",group:"general",defaultMarks:75,mcqMarks:15,shortQMarks:10,longQMarks:50,timeAllowed:"2:30 Hours",chapters:[{id:1,number:1,titleEn:"Hissa Nasar: Mirza Muhammad Saeed",titleUr:"\u062D\u0635\u06C1 \u0646\u062B\u0631: \u0645\u0631\u0632\u0627 \u0645\u062D\u0645\u062F \u0633\u0639\u06CC\u062F"},{id:2,number:2,titleEn:"Hissa Nasar: Nazria-e-Pakistan",titleUr:"\u062D\u0635\u06C1 \u0646\u062B\u0631: \u0646\u0638\u0631\u06CC\u06C1 \u067E\u0627\u06A9\u0633\u062A\u0627\u0646"},{id:3,number:3,titleEn:"Hissa Nasar: Paristan ki Gohar Bano",titleUr:"\u062D\u0635\u06C1 \u0646\u062B\u0631: \u067E\u0631\u0633\u062A\u0627\u0646 \u06A9\u06CC \u06AF\u0648\u06C1\u0631 \u0628\u0627\u0646\u0648"},{id:4,number:4,titleEn:"Hissa Nasar: Urdu Adab main Eid-ul-Fitr",titleUr:"\u062D\u0635\u06C1 \u0646\u062B\u0631: \u0627\u0631\u062F\u0648 \u0627\u062F\u0628 \u0645\u06CC\u06BA \u0639\u06CC\u062F \u0627\u0644\u0641\u0637\u0631"},{id:5,number:5,titleEn:"Hissa Nasar: Mujhe Mere Doston se Bachao",titleUr:"\u062D\u0635\u06C1 \u0646\u062B\u0631: \u0645\u062C\u06BE\u06D2 \u0645\u06CC\u0631\u06D2 \u062F\u0648\u0633\u062A\u0648\u06BA \u0633\u06D2 \u0628\u0686\u0627\u0624"},{id:6,number:6,titleEn:"Hissa Nasar: Malli",titleUr:"\u062D\u0635\u06C1 \u0646\u062B\u0631: \u0645\u0644\u0645\u0639"},{id:7,number:7,titleEn:"Hissa Nazm: Hamd, Naat, Maidan-e-Karbala",titleUr:"\u062D\u0635\u06C1 \u0646\u0638\u0645: \u062D\u0645\u062F\u060C \u0646\u0639\u062A\u060C \u0645\u06CC\u062F\u0627\u0646\u0650 \u06A9\u0631\u0628\u0644\u0627"},{id:8,number:8,titleEn:"Hissa Ghazal: Hasrat Mohani, Jigar Muradabadi",titleUr:"\u062D\u0635\u06C1 \u063A\u0632\u0644: \u062D\u0633\u0631\u062A \u0645\u0648\u06C1\u0627\u0646\u06CC\u060C \u062C\u06AF\u0631 \u0645\u0631\u0627\u062F \u0622\u0628\u0627\u062F\u06CC"}]},{id:"10th-islamiyat",nameEn:"Islamiat Compulsory",nameUr:"\u0627\u0633\u0644\u0627\u0645\u06CC\u0627\u062A (\u062F\u0633\u0648\u06CC\u06BA \u062C\u0645\u0627\u0639\u062A)",classLevel:"10th",group:"general",defaultMarks:50,mcqMarks:10,shortQMarks:24,longQMarks:16,timeAllowed:"2:00 Hours",chapters:[{id:1,number:1,titleEn:"Surah Al-Ahzab (Ayaat 1 - 73)",titleUr:"\u0633\u0648\u0631\u06C3 \u0627\u0644\u0627\u062D\u0632\u0627\u0628 (\u0622\u06CC\u0627\u062A 1 \u062A\u0627 73)"},{id:2,number:2,titleEn:"Surah Al-Mumtahanah",titleUr:"\u0633\u0648\u0631\u06C3 \u0627\u0644\u0645\u0645\u062A\u062D\u0646\u06C1"},{id:3,number:3,titleEn:"Ahadith-e-Nabaviyya (Hadith 11 - 20)",titleUr:"\u0627\u062D\u0627\u062F\u06CC\u062B\u0650 \u0645\u0628\u0627\u0631\u06A9\u06C1 (\u062D\u062F\u06CC\u062B 11 \u062A\u0627 20)"},{id:4,number:4,titleEn:"Mozooati Mutalia: Jihad fi Sabilillah",titleUr:"\u0645\u0648\u0636\u0648\u0639\u0627\u062A\u06CC \u0645\u0637\u0627\u0644\u0639\u06C1: \u062C\u06C1\u0627\u062F \u0641\u06CC \u0633\u0628\u06CC\u0644 \u0627\u0644\u0644\u06C1"},{id:5,number:5,titleEn:"Mozooati Mutalia: Farz Shanasi aur Dayanat Dari",titleUr:"\u0645\u0648\u0636\u0648\u0639\u0627\u062A\u06CC \u0645\u0637\u0627\u0644\u0639\u06C1: \u0641\u0631\u0636 \u0634\u0646\u0627\u0633\u06CC \u0648 \u062F\u06CC\u0627\u0646\u062A \u062F\u0627\u0631\u06CC"},{id:6,number:6,titleEn:"Mozooati Mutalia: Khulaq-e-Azeem (Husn-e-Khuluq)",titleUr:"\u0645\u0648\u0636\u0648\u0639\u0627\u062A\u06CC \u0645\u0637\u0627\u0644\u0639\u06C1: \u062D\u0633\u0646\u0650 \u062E\u0644\u0642"}]},{id:"10th-pakstudies",nameEn:"Pakistan Studies",nameUr:"\u0645\u0637\u0627\u0644\u0639\u06C1 \u067E\u0627\u06A9\u0633\u062A\u0627\u0646 (\u062F\u0633\u0648\u06CC\u06BA \u062C\u0645\u0627\u0639\u062A)",classLevel:"10th",group:"general",defaultMarks:50,mcqMarks:10,shortQMarks:24,longQMarks:16,timeAllowed:"2:00 Hours",chapters:[{id:5,number:5,titleEn:"History of Pakistan (Part-II 1971 to Present)",titleUr:"\u062A\u0627\u0631\u06CC\u062E\u0650 \u067E\u0627\u06A9\u0633\u062A\u0627\u0646 (\u062D\u0635\u06C1 \u062F\u0648\u0645: 1971 \u062A\u0627 \u062D\u0627\u0644)"},{id:6,number:6,titleEn:"Pakistan in World Affairs (Foreign Policy)",titleUr:"\u067E\u0627\u06A9\u0633\u062A\u0627\u0646 \u06A9\u06D2 \u062E\u0627\u0631\u062C\u06C1 \u062A\u0639\u0644\u0642\u0627\u062A"},{id:7,number:7,titleEn:"Economic Development of Pakistan",titleUr:"\u067E\u0627\u06A9\u0633\u062A\u0627\u0646 \u06A9\u06CC \u0645\u0639\u0627\u0634\u06CC \u062A\u0631\u0642\u06CC"},{id:8,number:8,titleEn:"Population, Society and Culture of Pakistan",titleUr:"\u0622\u0628\u0627\u062F\u06CC\u060C \u0645\u0639\u0627\u0634\u0631\u06C1 \u0627\u0648\u0631 \u067E\u0627\u06A9\u0633\u062A\u0627\u0646 \u06A9\u06CC \u062B\u0642\u0627\u0641\u062A"}]},{id:"10th-tarjuma-quran",nameEn:"Tarjuma-tul-Quran-ul-Majeed",nameUr:"\u062A\u0631\u062C\u0645\u06C3 \u0627\u0644\u0642\u0631\u0622\u0646 \u0627\u0644\u0645\u062C\u06CC\u062F (\u062F\u0633\u0648\u06CC\u06BA \u062C\u0645\u0627\u0639\u062A)",classLevel:"10th",group:"general",defaultMarks:50,mcqMarks:10,shortQMarks:24,longQMarks:16,timeAllowed:"2:00 Hours",chapters:[{id:1,number:1,titleEn:"Surah Al-Furqan",titleUr:"\u0633\u0648\u0631\u06C3 \u0627\u0644\u0641\u0631\u0642\u0627\u0646"},{id:2,number:2,titleEn:"Surah Ash-Shuara",titleUr:"\u0633\u0648\u0631\u06C3 \u0627\u0644\u0634\u0639\u0631\u0627\u0621"},{id:3,number:3,titleEn:"Surah An-Naml",titleUr:"\u0633\u0648\u0631\u06C3 \u0627\u0644\u0646\u0645\u0644"},{id:4,number:4,titleEn:"Surah Al-Qasas",titleUr:"\u0633\u0648\u0631\u06C3 \u0627\u0644\u0642\u0635\u0635"},{id:5,number:5,titleEn:"Surah Al-Ankabut",titleUr:"\u0633\u0648\u0631\u06C3 \u0627\u0644\u0639\u0646\u06A9\u0628\u0648\u062A"},{id:6,number:6,titleEn:"Surah Ar-Rum & Luqman",titleUr:"\u0633\u0648\u0631\u06C3 \u0627\u0644\u0631\u0648\u0645 \u0648 \u0633\u0648\u0631\u06C3 \u0644\u0642\u0645\u0627\u0646"},{id:7,number:7,titleEn:"Surah As-Sajdah & Al-Ahzab",titleUr:"\u0633\u0648\u0631\u06C3 \u0627\u0644\u0633\u062C\u062F\u06C1 \u0648 \u0627\u0644\u0627\u062D\u0632\u0627\u0628"}]}];const seenSubjectIds=new Set<string>();const MASTER_PTBB_SUBJECTS=[...PTBB_SUBJECTS,...ADDITIONAL_PTBB_SUBJECTS].filter(s=>{if(seenSubjectIds.has(s.id))return false;seenSubjectIds.add(s.id);return true;});function generateCuratedQuestionsForChapter(subject,chapter){const chNo=chapter.number;const chKey1=`${subject.id}_ch${chNo}`;const chKey2=`${subject.id}_ch${chapter.id}`;const master=PTBB_CHAPTER_QUESTIONS[chKey1]||PTBB_CHAPTER_QUESTIONS[chKey2];if(master&&master.mcqs&&master.mcqs.length>0){return{mcqs:master.mcqs,shortQuestions:master.shortQuestions,longQuestions:master.longQuestions}}return{mcqs:[],shortQuestions:[],longQuestions:[]}}__name(generateCuratedQuestionsForChapter,"generateCuratedQuestionsForChapter");const USER_CUSTOM_QUESTIONS_KEY="ptbb_user_custom_questions_v1";function getUserCustomQuestions(){try{const raw=localStorage.getItem(USER_CUSTOM_QUESTIONS_KEY);if(!raw)return[];return JSON.parse(raw)}catch{return[]}}__name(getUserCustomQuestions,"getUserCustomQuestions");function saveUserCustomQuestion(q){const existing=getUserCustomQuestions();const newItem={...q,id:`custom-${Date.now()}-${Math.random().toString(36).substring(2,6)}`};existing.unshift(newItem);localStorage.setItem(USER_CUSTOM_QUESTIONS_KEY,JSON.stringify(existing));return newItem}__name(saveUserCustomQuestion,"saveUserCustomQuestion");function getQuestionsForSubjectAndChapters(subjectId,chapterNumbers){const subject=MASTER_PTBB_SUBJECTS.find(s=>s.id===subjectId);if(!subject){return{mcqs:[],shortQuestions:[],longQuestions:[],totalAvailableMCQs:0,totalAvailableShorts:0,totalAvailableLongs:0}}const validChapters=subject.chapters.filter((c,idx)=>chapterNumbers.length===0||chapterNumbers.includes(c.number)||chapterNumbers.includes(c.id)||chapterNumbers.includes(idx+1));const customQuestions=getUserCustomQuestions().filter(q=>q.subjectId===subjectId);const allMCQs=[];const allShorts=[];const allLongs=[];const chaptersMCQsList: any[][] = [];
const chaptersShortsList: any[][] = [];
const chaptersLongsList: any[][] = [];

validChapters.forEach(chapter => {
  const chKey1 = `${subject.id}_ch${chapter.number}`;
  const chKey2 = `${subject.id}_ch${chapter.id}`;
  const chKey3 = `${subject.id}_ch${validChapters.indexOf(chapter) + 1}`;
  const master = PTBB_CHAPTER_QUESTIONS[chKey1] || PTBB_CHAPTER_QUESTIONS[chKey2] || PTBB_CHAPTER_QUESTIONS[chKey3];

  const masterMCQs = (master?.mcqs || []).map((m: any) => ({ ...m, chapterRef: chapter.number }));
  const masterShorts = (master?.shortQuestions || []).map((s: any) => ({ ...s, chapterRef: chapter.number }));
  const masterLongs = (master?.longQuestions || []).map((l: any) => ({ ...l, chapterRef: `Unit ${chapter.number}` }));

  const existingMCQs = (chapter.mcqs || []).map((m: any) => ({ ...m, chapterRef: chapter.number, category: m.category || "Textbook Exercises" }));
  const existingShorts = (chapter.shortQuestions || []).map((s: any) => ({ ...s, chapterRef: chapter.number, category: s.category || "Textbook Exercises" }));
  const existingLongs = (chapter.longQuestions || []).map((l: any) => ({ id: l.id, totalMarks: 9, parts: l.parts || [{ partLabel: "a", statementEn: l.statementEn || "", statementUr: l.statementUr || "", marks: 5 }], chapterRef: `Unit ${chapter.number}`, category: l.category || "Past Board Papers" }));
  
  const customForChapter = customQuestions.filter((cq: any) => cq.chapterNo === chapter.number);
  const customMCQs: any[] = [];
  const customShorts: any[] = [];
  const customLongs: any[] = [];
  customForChapter.forEach((cq: any) => {
    if (cq.type === "mcq" && cq.options && cq.correctOption) {
      customMCQs.push({ id: cq.id, statementEn: cq.statementEn, statementUr: cq.statementUr, options: cq.options, correctOption: cq.correctOption, chapterRef: chapter.number });
    } else if (cq.type === "short") {
      customShorts.push({ id: cq.id, statementEn: cq.statementEn, statementUr: cq.statementUr, marks: cq.marks || 2, chapterRef: chapter.number });
    } else if (cq.type === "long") {
      customLongs.push({ id: cq.id, totalMarks: cq.marks || 9, parts: [{ partLabel: "a", statementEn: cq.statementEn, statementUr: cq.statementUr, marks: cq.marks || 5 }], chapterRef: `Unit ${chapter.number}` });
    }
  });

  chaptersMCQsList.push([...masterMCQs, ...existingMCQs, ...customMCQs]);
  chaptersShortsList.push([...masterShorts, ...existingShorts, ...customShorts]);
  chaptersLongsList.push([...masterLongs, ...existingLongs, ...customLongs]);
});

// Strictly balance and interleave chapter questions evenly across all selected chapters
const maxM = Math.max(0, ...chaptersMCQsList.map(a => a.length));
for (let i = 0; i < maxM; i++) {
  for (const cList of chaptersMCQsList) {
    if (i < cList.length) allMCQs.push({ ...cList[i], qNo: allMCQs.length + 1 });
  }
}
const maxS = Math.max(0, ...chaptersShortsList.map(a => a.length));
for (let i = 0; i < maxS; i++) {
  for (const cList of chaptersShortsList) {
    if (i < cList.length) allShorts.push({ ...cList[i], subNo: allShorts.length + 1 });
  }
}
const maxL = Math.max(0, ...chaptersLongsList.map(a => a.length));
for (let i = 0; i < maxL; i++) {
  for (const cList of chaptersLongsList) {
    if (i < cList.length) allLongs.push({ ...cList[i], qNo: allLongs.length + 5 });
  }
}
const uniqueMCQs=[];const mcqSet=new Set;allMCQs.forEach(m=>{const key=(m.statementEn||m.statementUr||"").trim().toLowerCase();if(key&&!mcqSet.has(key)){mcqSet.add(key);uniqueMCQs.push({...m,qNo:uniqueMCQs.length+1})}});const uniqueShorts=[];const shortSet=new Set;allShorts.forEach(s=>{const key=(s.statementEn||s.statementUr||"").trim().toLowerCase();if(key&&!shortSet.has(key)){shortSet.add(key);uniqueShorts.push({...s,subNo:uniqueShorts.length+1})}});const uniqueLongs=[];const longSet=new Set;allLongs.forEach(l=>{const mainKey=(l.parts?.[0]?.statementEn||l.statementEn||"").trim().toLowerCase();if(mainKey&&!longSet.has(mainKey)){longSet.add(mainKey);uniqueLongs.push({...l,qNo:uniqueLongs.length+5})}});return{mcqs:uniqueMCQs,shortQuestions:uniqueShorts,longQuestions:uniqueLongs,totalAvailableMCQs:uniqueMCQs.length,totalAvailableShorts:uniqueShorts.length,totalAvailableLongs:uniqueLongs.length}}__name(getQuestionsForSubjectAndChapters,"getQuestionsForSubjectAndChapters");
const EN_STOPWORDS = new Set([
  'what','which','following','explain','define','definition','state','describe',
  'write','note','short','differentiate','distinguish','between','compare','examples',
  'practical','applications','uses','how','why','calculate','find','determine',
  'according','ptbb','curriculum','correct','standard','measure','associated',
  'that','this','have','were','been','their','will','would','about','into','some',
  'them','then','also','than','each','both','under','using','when','does','show',
  'give','true','name','list','draw','term','type','unit','units','case','more',
  'from','with','meant','mean','relates','regarding','briefly','diagram','example',
  'formulas','formula','problems','problem','solved','solve','statement','value',
  'values','derived','base','is','are','am','was','were','and','of','in','the',
  'to','for','on','at','as','or','not','it','its','an','a','do','can','by','all'
]);

const UR_STOPWORDS = new Set([
  'درج','ذیل','میں','سے','کوئی','سوال','سوالات','جواب','جوابات','لکھیں','کیجیے',
  'کریں','کرے','ہے','ہیں','تھا','تھی','تھے','اور','یا','کا','کی','کے','پر','تک',
  'اگر','مگر','لیکن','سب','ساتھ','بغیر','والا','والی','والے','کون','سا','کیا',
  'کس','طرح','مراد','تعریف','وضاحت','بیان','اہم','کل','نکات','استعمال','استعمالات',
  'فوائد','نقصانات','اہمیت','کلیہ','حسابی','عددی','قیمت','معلوم','مساوات','خاکے',
  'خاکہ','مختصر','تفصیلی','نوٹ','ہو','گی','گے','گا','دیں','دین','دی','دیئے'
]);

const UR_PUNCT_REGEX = /[،؛؟۔\.,!?;:()\[\]{}"'\-\/\_]/g;

function normalizeQuestionText(s: string): string {
  if (!s) return '';
  let res = s.toLowerCase();
  res = res.replace(/ي/g, 'ی').replace(/ك/g, 'ک').replace(/ة/g, 'ہ').replace(/ھ/g, 'ہ').replace(/آ/g, 'آ');
  res = res.replace(UR_PUNCT_REGEX, ' ');
  res = res.replace(/[^a-zA-Z0-9؀-ۿ\s]/g, ' ');
  return res.split(/\s+/).filter(Boolean).join(' ');
}

function stemWord(w: string): string {
  let s = w.toLowerCase().trim();
  if (s.length > 4) {
    for (const suffix of ['ing', 'ies', 'es', 'ed', 'ly', 's']) {
      if (s.endsWith(suffix) && s.length - suffix.length >= 3) {
        s = s.slice(0, -suffix.length);
        break;
      }
    }
  }
  if (s.length > 3) {
    for (const suffix of ['وں', 'یں', 'ئے', 'ے', 'ی', 'ا']) {
      if (s.endsWith(suffix) && s.length - suffix.length >= 2) {
        s = s.slice(0, -suffix.length);
        break;
      }
    }
  }
  return s;
}

function extractKeywords(en?: string, ur?: string): Set<string> {
  const combined = normalizeQuestionText(en || '') + ' ' + normalizeQuestionText(ur || '');
  const words = combined.split(/\s+/).filter(w => w.length >= 2);
  const result = new Set<string>();
  for (const w of words) {
    const st = stemWord(w);
    if (!EN_STOPWORDS.has(w) && !UR_STOPWORDS.has(w) && !EN_STOPWORDS.has(st) && !UR_STOPWORDS.has(st)) {
      result.add(st);
    }
  }
  return result;
}

const ORDINAL_MAP: Record<string, number> = {
  first: 1, '1st': 1, 'پہل': 1,
  second: 2, '2nd': 2, 'دوسر': 2,
  third: 3, '3rd': 3, 'تیسر': 3,
  fourth: 4, '4th': 4, 'چوتھ': 4
};

function areQuestionsDuplicateOrSimilar(q1: any, q2: any): boolean {
  if (!q1 || !q2) return false;
  const norm1En = normalizeQuestionText(q1.statementEn || '');
  const norm2En = normalizeQuestionText(q2.statementEn || '');
  const norm1Ur = normalizeQuestionText(q1.statementUr || '');
  const norm2Ur = normalizeQuestionText(q2.statementUr || '');

  if (norm1En && norm1En === norm2En) return true;
  if (norm1Ur && norm1Ur === norm2Ur) return true;

  const kw1 = extractKeywords(q1.statementEn, q1.statementUr);
  const kw2 = extractKeywords(q2.statementEn, q2.statementUr);

  if (kw1.size === 0 || kw2.size === 0) return false;

  const ord1 = new Set<number>();
  const ord2 = new Set<number>();
  for (const w of kw1) if (ORDINAL_MAP[w]) ord1.add(ORDINAL_MAP[w]);
  for (const w of kw2) if (ORDINAL_MAP[w]) ord2.add(ORDINAL_MAP[w]);
  if (ord1.size > 0 && ord2.size > 0) {
    let diff = false;
    for (const o of ord1) {
      if (!ord2.has(o)) { diff = true; break; }
    }
    if (diff) return false;
  }

  let interCount = 0;
  for (const w of kw1) {
    if (kw2.has(w)) interCount++;
  }
  const unionCount = kw1.size + kw2.size - interCount;
  const jaccard = unionCount > 0 ? interCount / unionCount : 0;
  const minLen = Math.min(kw1.size, kw2.size);
  const containment = minLen > 0 ? interCount / minLen : 0;

  if (interCount >= 4) return true;
  if (minLen <= 2 && containment >= 0.70 && interCount >= 1) return true;
  if (interCount >= 2 && containment >= 0.65) return true;
  if (jaccard >= 0.40 && interCount >= 2) return true;

  return false;
}

function dedupeAndReplenishPaper(paper: any, explicitSubjectId?: string, explicitChapters?: number[]): any {
  if (!paper) return paper;

  const classLevel = (paper.header?.classLevel || '9th').toLowerCase();
  const subjectName = (paper.header?.subjectName || 'Physics').toLowerCase();

  const subObj = explicitSubjectId 
    ? MASTER_PTBB_SUBJECTS.find(s => s.id === explicitSubjectId)
    : MASTER_PTBB_SUBJECTS.find(s => (classLevel.includes('10') ? s.id.startsWith('10th') : s.id.startsWith('9th')) && (s.nameEn.toLowerCase() === subjectName || s.id.includes(subjectName))) 
      || MASTER_PTBB_SUBJECTS[0];

  let chapterNos = explicitChapters && explicitChapters.length > 0 ? explicitChapters : [];
  if (chapterNos.length === 0 && paper.header?.syllabusCovered) {
    const matches = paper.header.syllabusCovered.match(/\d+/g);
    if (matches) chapterNos = Array.from(new Set(matches.map(Number)));
  }
  if (chapterNos.length === 0) chapterNos = [1, 2, 3];

  const pool = getQuestionsForSubjectAndChapters(subObj?.id || '9th-physics', chapterNos);
  const usedPoolIds = new Set<string>();
  const acceptedQuestions: Array<{ statementEn: string; statementUr: string }> = [];

  function isDuplicateWithAccepted(q: any): boolean {
    return acceptedQuestions.some(acc => areQuestionsDuplicateOrSimilar(acc, q));
  }

  if (paper.objectiveSection?.questions) {
    paper.objectiveSection.questions.forEach((q: any) => { if (q.id) usedPoolIds.add(q.id); });
  }
  if (paper.subjectiveSection?.part1_shortQuestions) {
    paper.subjectiveSection.part1_shortQuestions.forEach((g: any) => {
      (g.questions || []).forEach((q: any) => { if (q.id) usedPoolIds.add(q.id); });
    });
  }
  if (paper.subjectiveSection?.part2_longQuestions?.questions) {
    paper.subjectiveSection.part2_longQuestions.questions.forEach((q: any) => { if (q.id) usedPoolIds.add(q.id); });
  }

  // 1. Deduplicate & replenish MCQs
  if (paper.objectiveSection?.questions) {
    const cleanMcqs: any[] = [];
    const targetMcqs = Math.max(paper.objectiveSection.questions?.length || 0, subObj?.mcqMarks || 12);
    for (const m of paper.objectiveSection.questions) {
      if (!isDuplicateWithAccepted(m)) {
        cleanMcqs.push(m);
        acceptedQuestions.push({ statementEn: m.statementEn, statementUr: m.statementUr });
      } else {
        const cand = pool.mcqs.find(p => !usedPoolIds.has(p.id) && !isDuplicateWithAccepted(p));
        if (cand) {
          usedPoolIds.add(cand.id);
          cleanMcqs.push({ ...cand });
          acceptedQuestions.push({ statementEn: cand.statementEn, statementUr: cand.statementUr });
        }
      }
    }
    while (cleanMcqs.length < targetMcqs) {
      const cand = pool.mcqs.find(p => !usedPoolIds.has(p.id) && !isDuplicateWithAccepted(p));
      if (!cand) break;
      usedPoolIds.add(cand.id);
      cleanMcqs.push({ ...cand });
      acceptedQuestions.push({ statementEn: cand.statementEn, statementUr: cand.statementUr });
    }
    cleanMcqs.forEach((q, idx) => { q.qNo = idx + 1; });
    paper.objectiveSection.questions = cleanMcqs;
    paper.objectiveSection.totalMarks = cleanMcqs.length;
  }

  // 2. Deduplicate & replenish Short Questions
  if (paper.subjectiveSection?.part1_shortQuestions) {
    paper.subjectiveSection.part1_shortQuestions.forEach((grp: any) => {
      if (grp.questions) {
        const cleanShorts: any[] = [];
        const targetShorts = grp.questions.length;
        for (const q of grp.questions) {
          if (!isDuplicateWithAccepted(q)) {
            cleanShorts.push(q);
            acceptedQuestions.push({ statementEn: q.statementEn, statementUr: q.statementUr });
          } else {
            const cand = pool.shortQuestions.find(p => !usedPoolIds.has(p.id) && !isDuplicateWithAccepted(p));
            if (cand) {
              usedPoolIds.add(cand.id);
              cleanShorts.push({ ...cand, marks: grp.marksEach || 2 });
              acceptedQuestions.push({ statementEn: cand.statementEn, statementUr: cand.statementUr });
            }
          }
        }
        while (cleanShorts.length < targetShorts) {
          const cand = pool.shortQuestions.find(p => !usedPoolIds.has(p.id) && !isDuplicateWithAccepted(p));
          if (!cand) break;
          usedPoolIds.add(cand.id);
          cleanShorts.push({ ...cand, marks: grp.marksEach || 2 });
          acceptedQuestions.push({ statementEn: cand.statementEn, statementUr: cand.statementUr });
        }
        cleanShorts.forEach((q, idx) => { q.subNo = idx + 1; });
        grp.questions = cleanShorts;
        grp.totalCount = cleanShorts.length;
      }
    });
  }

  // 3. Deduplicate & replenish Long Questions
  if (paper.subjectiveSection?.part2_longQuestions?.questions) {
    const cleanLongs: any[] = [];
    const targetLongs = Math.max(paper.subjectiveSection.part2_longQuestions.questions?.length || 0, paper.subjectiveSection.part2_longQuestions.totalCount || 3);
    for (const lq of paper.subjectiveSection.part2_longQuestions.questions) {
      const parts = lq.parts || [];
      const hasDup = parts.some((p: any) => isDuplicateWithAccepted(p)) || isDuplicateWithAccepted(lq);
      if (!hasDup) {
        cleanLongs.push(lq);
        parts.forEach((p: any) => acceptedQuestions.push({ statementEn: p.statementEn, statementUr: p.statementUr }));
        acceptedQuestions.push({ statementEn: lq.statementEn, statementUr: lq.statementUr });
      } else {
        const cand = pool.longQuestions.find(p => {
          if (usedPoolIds.has(p.id)) return false;
          if (isDuplicateWithAccepted(p)) return false;
          return !(p.parts || []).some((pt: any) => isDuplicateWithAccepted(pt));
        });
        if (cand) {
          usedPoolIds.add(cand.id);
          cleanLongs.push({ ...cand });
          (cand.parts || []).forEach((pt: any) => acceptedQuestions.push({ statementEn: pt.statementEn, statementUr: pt.statementUr }));
          acceptedQuestions.push({ statementEn: cand.statementEn, statementUr: cand.statementUr });
        }
      }
    }
    while (cleanLongs.length < targetLongs) {
      const cand = pool.longQuestions.find(p => {
        if (usedPoolIds.has(p.id)) return false;
        if (isDuplicateWithAccepted(p)) return false;
        return !(p.parts || []).some((pt: any) => isDuplicateWithAccepted(pt));
      });
      if (!cand) break;
      usedPoolIds.add(cand.id);
      cleanLongs.push({ ...cand });
      (cand.parts || []).forEach((pt: any) => acceptedQuestions.push({ statementEn: pt.statementEn, statementUr: pt.statementUr }));
      acceptedQuestions.push({ statementEn: cand.statementEn, statementUr: cand.statementUr });
    }
    cleanLongs.forEach((lq, idx) => { lq.qNo = idx + 5; });
    paper.subjectiveSection.part2_longQuestions.questions = cleanLongs;
    paper.subjectiveSection.part2_longQuestions.totalCount = cleanLongs.length;
  }

  return paper;
}

export{ADDITIONAL_PTBB_SUBJECTS,MASTER_PTBB_SUBJECTS,generateCuratedQuestionsForChapter,getQuestionsForSubjectAndChapters,getUserCustomQuestions,saveUserCustomQuestion,dedupeAndReplenishPaper,areQuestionsDuplicateOrSimilar,normalizeQuestionText,extractKeywords};
