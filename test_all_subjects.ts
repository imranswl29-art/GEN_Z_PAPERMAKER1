import { MASTER_PTBB_SUBJECTS, getQuestionsForSubjectAndChapters } from './src/data/questionBankStore.ts';

console.log("Total PTBB Subjects in store:", MASTER_PTBB_SUBJECTS.length);
MASTER_PTBB_SUBJECTS.forEach((sub, i) => {
  const ch1 = sub.chapters[0] ? [sub.chapters[0].number] : [1];
  const res = getQuestionsForSubjectAndChapters(sub.id, ch1);
  const mcqCats = [...new Set(res.mcqs.map(m => m.category))];
  const sqCats = [...new Set(res.shortQuestions.map(s => s.category))];
  const allCats = [...new Set([...mcqCats, ...sqCats])];
  console.log(`[${i+1}] ${sub.id} (${sub.nameEn}) -> MCQs: ${res.mcqs.length}, SQs: ${res.shortQuestions.length}, LQs: ${res.longQuestions.length} | Cats: ${allCats.join(', ')}`);
});
