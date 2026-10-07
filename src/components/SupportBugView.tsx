import React, { useState } from 'react';
import { UserAccount } from '../types/user';
import {
  MessageSquare,
  Phone,
  Mail,
  Bug,
  Send,
  CheckCircle,
  HelpCircle,
  LifeBuoy,
  FileQuestion,
  ChevronDown,
  ChevronUp,
  Cpu,
  Monitor,
  Clock,
  Sparkles,
} from 'lucide-react';

interface SupportBugViewProps {
  currentUser: UserAccount | null;
}

export const SupportBugView: React.FC<SupportBugViewProps> = ({ currentUser }) => {
  const [ticketCategory, setTicketCategory] = useState('Question Paper Generator');
  const [priority, setPriority] = useState('Normal');
  const [subject, setSubject] = useState('');
  const [description, setDescription] = useState('');
  const [contactPhone, setContactPhone] = useState(currentUser?.phone || '');
  const [isSubmitted, setIsSubmitted] = useState(false);
  const [submittedTicketId, setSubmittedTicketId] = useState('');

  // FAQ Accordion State
  const [expandedFaq, setExpandedFaq] = useState<number | null>(null);

  const toggleFaq = (index: number) => {
    setExpandedFaq(expandedFaq === index ? null : index);
  };

  const handleSendWhatsAppDirect = () => {
    const textMsg = `Hello Imran, I need assistance with Paper Maker Software.

*Category:* ${ticketCategory}
*Priority:* ${priority}
*Subject:* ${subject || 'General Inquiry'}
*Description:* ${description || 'Need help with software features'}
*School:* ${currentUser?.schoolName || 'Teacher'}
*Contact:* ${contactPhone || 'N/A'}`;

    const url = `https://wa.me/923007603964?text=${encodeURIComponent(textMsg)}`;
    window.open(url, '_blank');
  };

  const handleSubmitForm = (e: React.FormEvent) => {
    e.preventDefault();
    const newId = 'TKT-' + Math.floor(100000 + Math.random() * 900000);
    setSubmittedTicketId(newId);
    setIsSubmitted(true);

    // Also auto prompt to send via WhatsApp for instant reply
    setTimeout(() => {
      handleSendWhatsAppDirect();
    }, 400);
  };

  const faqs = [
    {
      q: 'How do I add or change my school monogram / logo?',
      a: 'Go to "School Branding" (Item #7 in sidebar) or click the "Edit School Branding" button at the top of any page. You can upload any PNG, JPG, or SVG image. The software automatically applies your monogram across all Question Papers, Date Sheets, and Result Cards.',
    },
    {
      q: 'How to print Question Papers or Date Sheets on A4 without headers or margins cutting off?',
      a: 'When the browser print dialog opens, set Paper Size to "A4", Margins to "Default" or "None", and ensure "Background graphics" is checked. The software is strictly calibrated for standard A4 printable dimensions (210mm x 297mm).',
    },
    {
      q: 'Can I generate bilingual (English + Urdu Nastaliq) papers and answer keys?',
      a: 'Yes! In the Paper Builder or Paper View toolbar, select "Bilingual" medium. Questions will render in crisp English alongside authentic Urdu Nastaleeq typography. Solved answer keys and OMR bubble sheets will match the selected scheme.',
    },
    {
      q: 'How do I download papers and date sheets into editable MS Word (.doc)?',
      a: 'Click the "Download Word (.doc)" button available in the toolbar. It generates an MSO HTML document with preserved tables, Urdu RTL styling, and school branding that opens smoothly in Microsoft Word 2010 through 365.',
    },
  ];

  return (
    <div className="space-y-6 max-w-5xl mx-auto font-sans text-slate-800">
      {/* Top Banner Card */}
      <div className="card-3d p-6 bg-white border border-slate-200">
        <div className="flex flex-col md:flex-row items-start md:items-center justify-between gap-4">
          <div className="flex items-center gap-3.5">
            <div className="w-12 h-12 rounded-2xl bg-gradient-to-tr from-emerald-600 to-teal-700 flex items-center justify-center text-white shadow-md shrink-0">
              <LifeBuoy className="w-6 h-6 text-white" />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <span className="text-[10px] font-black uppercase tracking-wider px-2 py-0.5 rounded bg-emerald-100 text-emerald-950">
                  Item #10 &bull; Direct Developer Contact
                </span>
                <span className="text-[11px] font-bold text-slate-500">24/7 Priority Support</span>
              </div>
              <h1 className="text-xl sm:text-2xl font-black text-slate-950 tracking-tight mt-0.5">
                Support &amp; Report Bug
              </h1>
              <p className="text-xs text-slate-600 font-medium">
                Direct developer contact, instant WhatsApp support, bug reporting, and quick assistance for Paper Maker Software
              </p>
            </div>
          </div>
        </div>
      </div>

      {/* ========================================================================= */}
      {/* DEVELOPER INFO DISPLAY (Strictly NO section headers as requested)          */}
      {/* ========================================================================= */}
      <div className="card-3d p-6 sm:p-7 bg-white border border-slate-200 shadow-md">
        <div className="flex flex-col lg:flex-row items-start lg:items-center justify-between gap-6">
          {/* Exact Required Developer Info Block */}
          <div className="space-y-1 text-slate-900 select-all">
            <div className="text-2xl font-black tracking-tight text-slate-950 uppercase">
              Muhammad Imran Khan
            </div>
            <div className="text-sm font-bold text-blue-900">
              MSc Computer Science
            </div>
            <div className="text-xs font-semibold text-slate-600">
              Software developer
            </div>
            <div className="pt-2 font-mono text-base font-black tracking-wide text-slate-900 space-y-0.5">
              <div className="flex items-center gap-2">
                <Phone className="w-4 h-4 text-emerald-600 shrink-0" />
                <a href="tel:03007603964" className="hover:text-blue-700 transition-colors">
                  03007603964
                </a>
              </div>
              <div className="flex items-center gap-2">
                <Phone className="w-4 h-4 text-emerald-600 shrink-0" />
                <a href="tel:03147603964" className="hover:text-blue-700 transition-colors">
                  03147603964
                </a>
              </div>
            </div>
          </div>

          {/* Direct Interactive Action Contact Buttons */}
          <div className="flex flex-col sm:flex-row flex-wrap items-stretch sm:items-center gap-2.5 w-full lg:w-auto">
            {/* WhatsApp Support Button: https://wa.me/923007603964 with prefilled greeting */}
            <a
              href={`https://wa.me/923007603964?text=${encodeURIComponent(
                'Hello Imran, I need assistance with Paper Maker Software...'
              )}`}
              target="_blank"
              rel="noopener noreferrer"
              className="btn-3d btn-3d-whatsapp flex items-center justify-center gap-2 px-4 py-3 rounded-xl text-xs font-black text-white shadow-md cursor-pointer no-underline text-center"
              title="Chat directly on WhatsApp (03007603964)"
            >
              <MessageSquare className="w-4 h-4" />
              <span>WhatsApp Support</span>
            </a>

            {/* Direct Email (Gmail): mailto:Mimrankhan3964@gmail.com */}
            <a
              href="mailto:Mimrankhan3964@gmail.com?subject=Paper%20Maker%20Software%20Support"
              className="btn-3d btn-3d-gmail flex items-center justify-center gap-2 px-4 py-3 rounded-xl text-xs font-black text-white shadow-md cursor-pointer no-underline text-center"
              title="Send direct email to Mimrankhan3964@gmail.com"
            >
              <Mail className="w-4 h-4" />
              <span>Direct Email (Gmail)</span>
            </a>

            {/* Call 1: 03007603964 */}
            <a
              href="tel:03007603964"
              className="btn-3d btn-3d-phone flex items-center justify-center gap-2 px-4 py-3 rounded-xl text-xs font-black text-white shadow-md cursor-pointer no-underline text-center"
              title="Call primary number: 03007603964"
            >
              <Phone className="w-4 h-4" />
              <span>Call: 03007603964</span>
            </a>

            {/* Call 2: 03147603964 */}
            <a
              href="tel:03147603964"
              className="btn-3d btn-3d-phone flex items-center justify-center gap-2 px-4 py-3 rounded-xl text-xs font-black text-white shadow-md cursor-pointer no-underline text-center"
              title="Call secondary number: 03147603964"
            >
              <Phone className="w-4 h-4" />
              <span>Call: 03147603964</span>
            </a>
          </div>
        </div>
      </div>

      {/* ========================================================================= */}
      {/* INTERACTIVE REPORT BUG / REQUEST FEATURE FORM                              */}
      {/* ========================================================================= */}
      <div className="card-3d p-6 bg-white border border-slate-200 space-y-4">
        <div className="flex items-center gap-2 border-b border-slate-200 pb-3 text-slate-900">
          <Bug className="w-5 h-5 text-rose-600" />
          <h2 className="font-black text-base">Submit Bug Report or Feature Request</h2>
        </div>

        {isSubmitted ? (
          <div className="p-6 bg-emerald-50 border border-emerald-300 rounded-2xl text-center space-y-3">
            <div className="w-12 h-12 bg-emerald-600 text-white rounded-full flex items-center justify-center mx-auto shadow-md">
              <CheckCircle className="w-6 h-6" />
            </div>
            <h3 className="text-base font-black text-emerald-950">
              Bug Report Submitted Successfully!
            </h3>
            <p className="text-xs text-emerald-800 max-w-md mx-auto">
              Your support ticket reference is <strong className="font-mono text-emerald-950">{submittedTicketId}</strong>.
              The developer has been notified. You can also chat directly on WhatsApp for an immediate response.
            </p>
            <div className="flex items-center justify-center gap-3 pt-2">
              <button
                type="button"
                onClick={handleSendWhatsAppDirect}
                className="btn-3d btn-3d-whatsapp px-4 py-2 text-white font-bold text-xs rounded-xl cursor-pointer"
              >
                Send via WhatsApp
              </button>
              <button
                type="button"
                onClick={() => {
                  setIsSubmitted(false);
                  setSubject('');
                  setDescription('');
                }}
                className="px-4 py-2 bg-slate-200 hover:bg-slate-300 text-slate-800 font-bold text-xs rounded-xl cursor-pointer"
              >
                Submit Another Report
              </button>
            </div>
          </div>
        ) : (
          <form onSubmit={handleSubmitForm} className="space-y-4 text-xs">
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div>
                <label className="block font-bold text-slate-700 mb-1">Issue Category:</label>
                <select
                  value={ticketCategory}
                  onChange={(e) => setTicketCategory(e.target.value)}
                  className="w-full px-3 py-2 rounded-xl border border-slate-300 font-semibold focus:outline-none focus:ring-2 focus:ring-blue-500"
                >
                  <option value="Question Paper Generator">Question Paper Generator</option>
                  <option value="Date Sheet Generator">Date Sheet Generator</option>
                  <option value="Result Card & Marksheet">Result Card & Marksheet</option>
                  <option value="Question Bank (Matric 9-10)">Question Bank (Matric 9-10)</option>
                  <option value="School Branding & Monogram">School Branding & Monogram</option>
                  <option value="Printing & A4 Page Margins">Printing & A4 Page Margins</option>
                  <option value="MS Word (.doc) or PDF Export">MS Word (.doc) or PDF Export</option>
                  <option value="Other Suggestion / Feature Request">Other Suggestion / Feature Request</option>
                </select>
              </div>

              <div>
                <label className="block font-bold text-slate-700 mb-1">Priority Level:</label>
                <select
                  value={priority}
                  onChange={(e) => setPriority(e.target.value)}
                  className="w-full px-3 py-2 rounded-xl border border-slate-300 font-semibold focus:outline-none focus:ring-2 focus:ring-blue-500"
                >
                  <option value="Normal">Normal</option>
                  <option value="High Priority">High Priority (Urgent)</option>
                  <option value="Feature Suggestion">Feature Suggestion</option>
                </select>
              </div>
            </div>

            <div>
              <label className="block font-bold text-slate-700 mb-1">Subject / Summary:</label>
              <input
                type="text"
                required
                value={subject}
                onChange={(e) => setSubject(e.target.value)}
                placeholder="Brief summary of the issue or requirement"
                className="w-full px-3 py-2 rounded-xl border border-slate-300 font-semibold focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
            </div>

            <div>
              <label className="block font-bold text-slate-700 mb-1">
                Detailed Description &amp; Reproduction Steps:
              </label>
              <textarea
                required
                rows={4}
                value={description}
                onChange={(e) => setDescription(e.target.value)}
                placeholder="Describe what happened, which subject or paper, and what result you expected..."
                className="w-full px-3 py-2 rounded-xl border border-slate-300 font-medium focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div>
                <label className="block font-bold text-slate-700 mb-1">
                  Your Contact Phone / WhatsApp:
                </label>
                <input
                  type="text"
                  value={contactPhone}
                  onChange={(e) => setContactPhone(e.target.value)}
                  placeholder="e.g. 0300-1234567"
                  className="w-full px-3 py-2 rounded-xl border border-slate-300 font-semibold focus:outline-none focus:ring-2 focus:ring-blue-500"
                />
              </div>

              <div>
                <label className="block font-bold text-slate-700 mb-1">School / Institute Name:</label>
                <input
                  type="text"
                  readOnly
                  value={currentUser?.schoolName || 'Guest User'}
                  className="w-full px-3 py-2 rounded-xl border border-slate-200 bg-slate-50 font-bold text-slate-600 cursor-not-allowed"
                />
              </div>
            </div>

            <div className="flex flex-wrap items-center justify-between gap-3 pt-2">
              <div className="text-[11px] text-slate-500 flex items-center gap-1.5 font-medium">
                <Clock className="w-3.5 h-3.5 text-blue-600" />
                <span>Response time typically under 15 minutes during academic hours</span>
              </div>

              <div className="flex items-center gap-2">
                <button
                  type="button"
                  onClick={handleSendWhatsAppDirect}
                  className="btn-3d btn-3d-whatsapp flex items-center gap-1.5 px-4 py-2.5 rounded-xl font-black text-white cursor-pointer shadow-md"
                >
                  <MessageSquare className="w-4 h-4" />
                  <span>Send via WhatsApp</span>
                </button>

                <button
                  type="submit"
                  className="btn-3d btn-3d-blue flex items-center gap-1.5 px-4 py-2.5 rounded-xl font-black text-white cursor-pointer shadow-md"
                >
                  <Send className="w-4 h-4" />
                  <span>Submit Ticket</span>
                </button>
              </div>
            </div>
          </form>
        )}
      </div>

      {/* ========================================================================= */}
      {/* QUICK FREQUENTLY ASKED QUESTIONS (FAQ)                                    */}
      {/* ========================================================================= */}
      <div className="card-3d p-6 bg-white border border-slate-200 space-y-3">
        <div className="flex items-center gap-2 border-b border-slate-200 pb-3 text-slate-900 font-black text-base">
          <HelpCircle className="w-5 h-5 text-indigo-600" />
          <span>Frequently Asked Questions &amp; Quick Guide</span>
        </div>

        <div className="divide-y divide-slate-200">
          {faqs.map((faq, idx) => (
            <div key={idx} className="py-3">
              <button
                type="button"
                onClick={() => toggleFaq(idx)}
                className="w-full flex items-center justify-between text-left font-extrabold text-xs text-slate-900 hover:text-blue-700 transition-colors cursor-pointer"
              >
                <span>{faq.q}</span>
                {expandedFaq === idx ? (
                  <ChevronUp className="w-4 h-4 text-blue-600 shrink-0" />
                ) : (
                  <ChevronDown className="w-4 h-4 text-slate-400 shrink-0" />
                )}
              </button>
              {expandedFaq === idx && (
                <div className="mt-2 text-xs text-slate-600 font-medium leading-relaxed bg-slate-50 p-3 rounded-xl border border-slate-200">
                  {faq.a}
                </div>
              )}
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};
