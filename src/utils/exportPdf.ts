import { jsPDF } from 'jspdf';
import html2canvas from 'html2canvas';
import { GeneratedExamPaper } from '../types/paper';

interface SliceInfo {
  startY: number;
  height: number;
}

/**
 * Intelligently calculates page slice positions on a canvas so that no indivisible
 * element (MCQ, Short Question, Long Question, OMR Bubble Grid, Table row, Board Header)
 * is cut in half across A4 page boundaries.
 */
function calculateSmartPageSlices(
  canvas: HTMLCanvasElement,
  element: HTMLElement,
  maxCanvasPageHeight: number
): SliceInfo[] {
  const slices: SliceInfo[] = [];
  const totalCanvasHeight = canvas.height;

  // Select all atomic elements that MUST NEVER be sliced across pages
  const avoidSelector = [
    '.page-break-inside-avoid',
    '.mcq-item',
    '.short-question-item',
    '.long-question-item',
    '.omr-bubble-grid-container',
    '.paper-header',
    '.paper-footer',
    '.section-header',
    '.short-q-group',
    'table',
    'tr',
    '[data-avoid-break="true"]',
  ].join(', ');

  const avoidElements = Array.from(element.querySelectorAll(avoidSelector)) as HTMLElement[];
  const containerRect = element.getBoundingClientRect();
  const elHeight = element.scrollHeight || element.offsetHeight || containerRect.height;
  const scaleY = elHeight > 0 ? totalCanvasHeight / elHeight : 1;

  const intervals: Array<{ top: number; bottom: number; isBreakBefore: boolean }> = [];

  for (const el of avoidElements) {
    const rect = el.getBoundingClientRect();
    const topPx = rect.top - containerRect.top;
    const bottomPx = rect.bottom - containerRect.top;
    const isBreakBefore =
      el.classList.contains('page-break-before') ||
      el.hasAttribute('data-page-break-before') ||
      el.getAttribute('data-break-before') === 'true';

    const canvasTop = Math.max(0, Math.floor(topPx * scaleY));
    const canvasBottom = Math.min(totalCanvasHeight, Math.ceil(bottomPx * scaleY));

    if (canvasBottom > canvasTop + 4) {
      intervals.push({ top: canvasTop, bottom: canvasBottom, isBreakBefore });
    }
  }

  // Sort intervals by their top position ascending
  intervals.sort((a, b) => a.top - b.top);

  let currentY = 0;
  let safetyLoop = 0;
  const maxLoops = 50;

  while (currentY < totalCanvasHeight && safetyLoop < maxLoops) {
    safetyLoop++;
    const remaining = totalCanvasHeight - currentY;

    // If remaining content fits on one page, take it all and finish
    if (remaining <= maxCanvasPageHeight) {
      slices.push({ startY: currentY, height: remaining });
      break;
    }

    const theoreticalEnd = currentY + maxCanvasPageHeight;
    let chosenCut = theoreticalEnd;

    // 1. Check if an element requires page-break-before within this page window
    let foundBreakBefore = false;
    for (const item of intervals) {
      if (item.isBreakBefore && item.top > currentY + 60 && item.top <= theoreticalEnd) {
        chosenCut = item.top;
        foundBreakBefore = true;
        break;
      }
    }

    // 2. If no explicit break-before, avoid slicing through any atomic block
    if (!foundBreakBefore) {
      for (const item of intervals) {
        if (item.top >= theoreticalEnd) continue;

        // If a single item is taller than 95% of a full page, it cannot be avoided
        if (item.bottom - item.top >= maxCanvasPageHeight * 0.95) continue;

        // Straddling check: does this item cross our theoretical page cut?
        if (item.top < theoreticalEnd && item.bottom > theoreticalEnd) {
          // Cut cleanly BEFORE this item starts!
          // Leave 4px breathing room above the element
          const safeCut = Math.max(currentY + 60, item.top - 4);
          if (safeCut < chosenCut) {
            chosenCut = safeCut;
          }
        }
      }
    }

    // Safety guard: ensure we always advance by at least 80px to prevent infinite loop
    if (chosenCut <= currentY + 80) {
      chosenCut = theoreticalEnd;
    }

    slices.push({ startY: currentY, height: chosenCut - currentY });
    currentY = chosenCut;
  }

  return slices;
}

/**
 * Captures a DOM element and slices it intelligently into A4 pages in a jsPDF document.
 */
async function renderElementSlicesToPdf(
  element: HTMLElement,
  pdf: jsPDF,
  contentWidth: number,
  usablePageHeight: number,
  marginX: number,
  marginY: number,
  isFirstSheet: boolean
): Promise<void> {
  // 1. Ensure all web fonts are fully loaded
  if (typeof document !== 'undefined' && document.fonts) {
    try {
      await document.fonts.ready;
    } catch {}
  }

  // 2. Ensure all images inside target element are loaded and decoded before canvas rendering
  const images = Array.from(element.querySelectorAll('img')) as HTMLImageElement[];
  if (images.length > 0) {
    await Promise.all(
      images.map(async (img) => {
        if (img.complete && img.naturalHeight > 0) {
          if ('decode' in img) {
            try {
              await img.decode();
            } catch {}
          }
          return;
        }
        return new Promise<void>((resolve) => {
          img.onload = () => resolve();
          img.onerror = () => resolve();
          setTimeout(resolve, 800);
        });
      })
    );
  }

  // Settle time for layout & Urdu Nastaliq font shaping
  await new Promise((resolve) => setTimeout(resolve, 350));

  // Capture element at scale 2 for ultra-crisp print quality
  const targetId = element.id;
  const canvas = await html2canvas(element, {
    scale: 2,
    useCORS: true,
    allowTaint: true,
    logging: false,
    backgroundColor: '#ffffff',
    scrollY: 0,
    scrollX: 0,
    windowWidth: 1200,
    onclone: (clonedDoc) => {
      clonedDoc.body.style.margin = '0';
      clonedDoc.body.style.padding = '0';
      clonedDoc.body.style.width = '100%';

      // Hide only non-printable controls (DO NOT hide semantic paper headers!)
      const toHide = clonedDoc.querySelectorAll('.no-print, nav, aside');
      toHide.forEach((el) => {
        (el as HTMLElement).style.display = 'none';
      });

      const clonedTarget = (targetId ? clonedDoc.getElementById(targetId) : null) || clonedDoc.body;
      if (clonedTarget) {
        // Unhide clonedTarget and its ancestors
        let curr: HTMLElement | null = clonedTarget;
        while (curr && curr !== clonedDoc.body) {
          curr.style.display = 'block';
          curr.style.visibility = 'visible';
          curr.style.opacity = '1';
          curr.classList.remove('hidden');
          curr = curr.parentElement;
        }

        clonedTarget.style.display = 'block';
        clonedTarget.style.visibility = 'visible';
        clonedTarget.style.opacity = '1';
        clonedTarget.classList.remove('hidden');
        clonedTarget.style.width = '794px';
        clonedTarget.style.maxWidth = '794px';
        clonedTarget.style.minWidth = '794px';
        clonedTarget.style.padding = '10px 14px';
        clonedTarget.style.margin = '0 auto';
        clonedTarget.style.boxSizing = 'border-box';
        clonedTarget.style.background = '#ffffff';

        // Force all tables to full width and visible
        const tables = clonedTarget.querySelectorAll('table');
        tables.forEach((t) => {
          (t as HTMLElement).style.width = '100%';
          (t as HTMLElement).style.visibility = 'visible';
        });

        // Ensure OMR bubble grid is formatted cleanly with zero overlap
        const bubbleGrids = clonedTarget.querySelectorAll('.omr-bubble-grid-container');
        bubbleGrids.forEach((bg) => {
          const bgEl = bg as HTMLElement;
          bgEl.style.pageBreakInside = 'avoid';
          bgEl.style.breakInside = 'avoid';
          bgEl.style.overflow = 'hidden';
          bgEl.style.clear = 'both';
          bgEl.style.display = 'block';
          bgEl.style.margin = '8px 0';
        });
      }
    },
  });

  if (!canvas || canvas.height === 0 || canvas.width === 0) {
    throw new Error('Canvas render produced empty output');
  }

  const maxCanvasPageHeight = Math.floor((usablePageHeight / contentWidth) * canvas.width);
  let slices = calculateSmartPageSlices(canvas, element, maxCanvasPageHeight);

  // Filter out any zero or degenerate slices
  slices = slices.filter((s) => s.height > 10);

  if (!slices || slices.length === 0) {
    slices = [{ startY: 0, height: canvas.height }];
  }

  for (let i = 0; i < slices.length; i++) {
    const { startY, height } = slices[i];
    if (height <= 0) continue;

    // Add page for subsequent slices or if this is a subsequent sheet
    if (!isFirstSheet || i > 0) {
      pdf.addPage();
    }

    const pageCanvas = document.createElement('canvas');
    pageCanvas.width = canvas.width;
    pageCanvas.height = height;
    const ctx = pageCanvas.getContext('2d');
    if (ctx) {
      ctx.fillStyle = '#ffffff';
      ctx.fillRect(0, 0, pageCanvas.width, pageCanvas.height);
      ctx.drawImage(canvas, 0, startY, canvas.width, height, 0, 0, canvas.width, height);
    }

    const pageImgData = pageCanvas.toDataURL('image/jpeg', 0.96);
    const renderedHeightMm = (height * contentWidth) / canvas.width;
    pdf.addImage(pageImgData, 'JPEG', marginX, marginY, contentWidth, renderedHeightMm, undefined, 'FAST');
  }
}

/**
 * Direct 1-Click PDF Downloader for Exam Papers
 * Renders the exact DOM paper elements into standard multi-page A4 PDF
 * with smart pagination that NEVER cuts questions or overlaps bubble sheets.
 */
export async function exportPaperToPdf(
  paper: GeneratedExamPaper,
  targetElementId: string = 'exam-paper-container',
  onProgress?: (status: string) => void,
  sheetType: 'all' | 'objective' | 'subjective' = 'all'
): Promise<boolean> {
  const container = document.getElementById(targetElementId);
  if (!container) {
    console.error(`Target element with id "${targetElementId}" not found for PDF export.`);
    window.print();
    return false;
  }

  try {
    if (onProgress) onProgress('Preparing high-resolution exam sheet...');
    // Brief settle time for web fonts & layout
    await new Promise((resolve) => setTimeout(resolve, 150));

    // Standard A4 dimensions in mm: 210 x 297
    const pageWidth = 210;
    const pageHeight = 297;
    const marginX = 8; // 8mm printable margin
    const marginY = 8;
    const contentWidth = pageWidth - marginX * 2; // 194mm
    const usablePageHeight = pageHeight - marginY * 2; // 281mm

    const pdf = new jsPDF({
      orientation: 'portrait',
      unit: 'mm',
      format: 'a4',
      compress: true,
    });

    const objSheetEl = document.getElementById('exam-paper-objective-sheet');
    const subjSheetEl = document.getElementById('exam-paper-subjective-sheet');

    if (sheetType === 'objective' && objSheetEl) {
      if (onProgress) onProgress('Capturing Objective Exam Sheet (معروضی پرچہ)...');
      await renderElementSlicesToPdf(objSheetEl, pdf, contentWidth, usablePageHeight, marginX, marginY, true);
    } else if (sheetType === 'subjective' && subjSheetEl) {
      if (onProgress) onProgress('Capturing Subjective Exam Sheet (انشائیہ پرچہ)...');
      await renderElementSlicesToPdf(subjSheetEl, pdf, contentWidth, usablePageHeight, marginX, marginY, true);
    } else if (sheetType === 'all' && objSheetEl && subjSheetEl) {
      // Clean multi-sheet export: Objective Paper is Sheet 1, Subjective starts on fresh Page!
      if (onProgress) onProgress('Capturing Sheet 1: Objective Paper (معروضی)...');
      await renderElementSlicesToPdf(objSheetEl, pdf, contentWidth, usablePageHeight, marginX, marginY, true);

      if (onProgress) onProgress('Capturing Sheet 2: Subjective Paper (انشائیہ)...');
      await renderElementSlicesToPdf(subjSheetEl, pdf, contentWidth, usablePageHeight, marginX, marginY, false);
    } else {
      // Fallback: render the whole container with smart page slicing
      if (onProgress) onProgress('Capturing Complete Exam Paper...');
      await renderElementSlicesToPdf(container, pdf, contentWidth, usablePageHeight, marginX, marginY, true);
    }

    if (onProgress) onProgress('Downloading PDF file...');
    const cleanSubject = (paper.header.subjectName || 'Paper').replace(/[^a-zA-Z0-9_-]/g, '_');
    const cleanClass = paper.header.classLevel || '9th';
    const sheetSuffix = sheetType === 'objective' ? '_Objective' : sheetType === 'subjective' ? '_Subjective' : '';
    const fileName = `${cleanClass}_Class_${cleanSubject}${sheetSuffix}_Exam_Paper.pdf`;

    pdf.save(fileName);
    if (onProgress) onProgress('Download complete!');
    return true;
  } catch (error) {
    console.warn('Direct PDF export encountered an error, falling back to print dialog:', error);
    const prevTitle = document.title;
    const cleanSubject = (paper.header.subjectName || 'Paper').replace(/[^a-zA-Z0-9_-]/g, '_');
    const cleanClass = paper.header.classLevel || '9th';
    document.title = `${cleanClass}_Class_${cleanSubject}_Exam_Paper`;
    window.print();
    setTimeout(() => {
      document.title = prevTitle;
    }, 1500);
    return false;
  }
}

/**
 * Direct 1-Click PDF Downloader for Answer Key & Solution Rubrics
 * with smart pagination that prevents any question rubric cutting.
 */
export async function exportAnswerKeyToPdf(
  paper: GeneratedExamPaper,
  targetElementId: string = 'answer-key-print-content',
  onProgress?: (status: string) => void
): Promise<boolean> {
  const element = document.getElementById(targetElementId);
  if (!element) {
    console.error(`Target element with id "${targetElementId}" not found for Answer Key PDF export.`);
    window.print();
    return false;
  }

  try {
    if (onProgress) onProgress('Capturing Answer Key pages...');
    await new Promise((resolve) => setTimeout(resolve, 150));

    const pageWidth = 210;
    const pageHeight = 297;
    const marginX = 8;
    const marginY = 8;
    const contentWidth = pageWidth - marginX * 2;
    const usablePageHeight = pageHeight - marginY * 2;

    const pdf = new jsPDF({
      orientation: 'portrait',
      unit: 'mm',
      format: 'a4',
      compress: true,
    });

    await renderElementSlicesToPdf(element, pdf, contentWidth, usablePageHeight, marginX, marginY, true);

    const cleanSubject = (paper.header.subjectName || 'Paper').replace(/[^a-zA-Z0-9_-]/g, '_');
    const cleanClass = paper.header.classLevel || '9th';
    const fileName = `${cleanClass}_Class_${cleanSubject}_Answer_Key.pdf`;

    pdf.save(fileName);
    if (onProgress) onProgress('Download complete!');
    return true;
  } catch (err) {
    console.warn('PDF Answer Key export fallback to print:', err);
    window.print();
    return false;
  }
}

/**
 * Universal High-Resolution A4 PDF Exporter for any printable DOM element
 * Supports Date Sheets, Result Cards, Master Marksheets, and Full OMR Sheets.
 */
export async function exportElementToPdf(
  targetElementId: string,
  fileName: string,
  onProgress?: (status: string) => void
): Promise<boolean> {
  const element = document.getElementById(targetElementId);
  if (!element) {
    console.error(`Target element with id "${targetElementId}" not found for PDF export.`);
    window.print();
    return false;
  }

  try {
    if (onProgress) onProgress('Rendering high-resolution A4 document...');
    await new Promise((resolve) => setTimeout(resolve, 150));

    const pageWidth = 210;
    const pageHeight = 297;
    const marginX = 8;
    const marginY = 8;
    const contentWidth = pageWidth - marginX * 2;
    const usablePageHeight = pageHeight - marginY * 2;

    const pdf = new jsPDF({
      orientation: 'portrait',
      unit: 'mm',
      format: 'a4',
      compress: true,
    });

    await renderElementSlicesToPdf(element, pdf, contentWidth, usablePageHeight, marginX, marginY, true);

    const safeFileName = fileName.endsWith('.pdf') ? fileName : `${fileName}.pdf`;
    pdf.save(safeFileName);
    if (onProgress) onProgress('Downloaded successfully!');
    return true;
  } catch (err) {
    console.warn('PDF export error, falling back to print:', err);
    window.print();
    return false;
  }
}
