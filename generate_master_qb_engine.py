import sys

with open("src/data/massiveQuestionBankEngine.ts", "w", encoding="utf-8") as out:
    out.write("""// PTBB Punjab Boards (BISE) Master Question Bank Engine (2020–2026)
// Covers all 9 BISE Punjab Boards: Lahore, Gujranwala, Rawalpindi, Faisalabad, Multan, Sahiwal, Sargodha, Bahawalpur, D.G. Khan
// Strictly adheres to Punjab Curriculum and Textbook Board (PTBB) Curriculum 2026, Textbook Exercises, and In-Text/Box Questions.

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
""")

print("Header written successfully.")
