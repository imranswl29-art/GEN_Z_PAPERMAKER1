export interface DateSheetRow {
  id: string;
  date: string;
  day: string;
  subject: string;
  paperType: string;
  syllabus?: string;
  timings?: string;
}

export interface DateSheetData {
  id: string;
  examType: string;
  customExamTitle: string;
  classLevel: string;
  session: string;
  examTimings: string;
  startDate: string;
  shift: string;
  instructions: string[];
  rows: DateSheetRow[];
  updatedAt?: string;
}

export interface SubjectConfig {
  id: string;
  name: string;
  totalMarks: number;
  passingMarks: number;
}

export interface StudentMarksRecord {
  id: string;
  rollNo: string;
  name: string;
  fatherName: string;
  photoUrl?: string;
  marks: Record<string, number>;
  totalObtained?: number;
  percentage?: number;
  grade?: string;
  status?: 'PASS' | 'FAIL' | 'COMPARTMENT';
  rank?: string;
  attendance?: string;
  remarks?: string;
}

export interface MarksheetData {
  id: string;
  classLevel: string;
  session: string;
  examCategory: string;
  subjects: SubjectConfig[];
  students: StudentMarksRecord[];
  updatedAt?: string;
}

export interface UnifiedSchoolBranding {
  schoolName: string;
  campusName: string;
  address: string;
  phone: string;
  logoUrl?: string;
  boardPattern?: string;
  tagline?: string;
  watermarkText?: string;
  showWatermark?: boolean;
}
