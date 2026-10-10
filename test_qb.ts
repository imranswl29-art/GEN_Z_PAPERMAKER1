
import { MASTER_PTBB_SUBJECTS, getQuestionsForSubjectAndChapters } from './src/data/questionBankStore.ts';
const sub = MASTER_PTBB_SUBJECTS[0];
const res = getQuestionsForSubjectAndChapters(sub.id, [1]);
console.log('Subject:', sub.nameEn, 'Ch 1 MCQs:', res.mcqs.length, 'Shorts:', res.shortQuestions.length, 'Longs:', res.longQuestions.length);
console.log('Sample MCQ categories:', [...new Set(res.mcqs.map(m => m.category))]);
console.log('Sample Short categories:', [...new Set(res.shortQuestions.map(s => s.category))]);
