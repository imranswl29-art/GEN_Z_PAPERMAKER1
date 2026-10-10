
import { MASTER_PTBB_SUBJECTS, getQuestionsForSubjectAndChapters } from './src/data/questionBankStore.ts';
const sub = MASTER_PTBB_SUBJECTS[0];
const res = getQuestionsForSubjectAndChapters(sub.id, [1]);
const unMcqs = res.mcqs.filter(m => !m.category);
console.log('Undefined MCQs count:', unMcqs.length);
if (unMcqs.length > 0) console.log('Sample undefined MCQ:', unMcqs[0]);
const unShorts = res.shortQuestions.filter(s => !s.category);
console.log('Undefined Shorts count:', unShorts.length);
if (unShorts.length > 0) console.log('Sample undefined Short:', unShorts[0]);
