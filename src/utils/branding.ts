import { UserAccount } from '../types/user';
import { PaperHeaderInfo } from '../types/paper';
import { UnifiedSchoolBranding } from '../types/extraDocs';

/**
 * Global Unified School Branding Resolver
 * Automatically fetches School Name, Monogram/Logo, Campus, Address, and Contact Details
 * configured under "School Branding" (Item #7) and applies them across ALL generated documents
 * (Question Papers, Date Sheets, and Result Cards).
 */
export function getSchoolBranding(
  currentUser: UserAccount | null,
  header?: PaperHeaderInfo
): UnifiedSchoolBranding {
  let cachedProfile: Record<string, any> = {};

  if (currentUser?.id) {
    try {
      const p = localStorage.getItem(`ptbb_profile_${currentUser.id}`);
      if (p) cachedProfile = { ...cachedProfile, ...JSON.parse(p) };
      const h = localStorage.getItem(`ptbb_header_settings_${currentUser.id}`);
      if (h) cachedProfile = { ...cachedProfile, ...JSON.parse(h) };
    } catch (e) {
      console.warn('Could not parse cached school profile:', e);
    }
  }

  // Also check active paper header cached in localStorage if any
  try {
    const activeRaw = localStorage.getItem('ptbb_active_paper');
    if (activeRaw) {
      const parsedActive = JSON.parse(activeRaw);
      if (parsedActive?.header) {
        cachedProfile = { ...parsedActive.header, ...cachedProfile };
      }
    }
  } catch (e) {}

  const schoolName =
    cachedProfile.instituteName ||
    cachedProfile.schoolName ||
    header?.instituteName ||
    currentUser?.schoolName ||
    'GOVERNMENT HIGHER SECONDARY SCHOOL';

  const campusName =
    cachedProfile.campusName ||
    header?.campusName ||
    currentUser?.campusName ||
    'MAIN CAMPUS';

  const phone =
    cachedProfile.phone ||
    header?.phone ||
    currentUser?.phone ||
    '0300-1234567';

  const address =
    cachedProfile.address ||
    currentUser?.address ||
    (currentUser?.city ? `${currentUser.city}, Punjab` : 'Punjab, Pakistan');

  const logoUrl =
    cachedProfile.customLogoUrl ||
    cachedProfile.logoUrl ||
    header?.customLogoUrl ||
    currentUser?.logoUrl ||
    undefined;

  const boardPattern =
    cachedProfile.boardPattern ||
    header?.boardPattern ||
    'BISE Lahore / Punjab Boards';

  return {
    schoolName,
    campusName,
    address,
    phone,
    logoUrl,
    boardPattern,
    tagline: 'Quality Education & Character Building',
    watermarkText: header?.watermarkText || cachedProfile.watermarkText || schoolName,
    showWatermark: header?.showWatermark ?? cachedProfile.showWatermark ?? false,
  };
}
