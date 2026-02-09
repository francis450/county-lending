<template>
  <div class="min-h-screen bg-white">

    <!-- HERO -->
    <section class="py-20 lg:py-28 bg-gradient-to-b from-trust-green-light to-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h1 class="trust-heading text-4xl md:text-5xl mb-6 fade-in-up">Am I Eligible?<br/>Check Here.</h1>
        <p class="trust-subheading mx-auto fade-in-up delay-100">
          We keep it simple. Meet these requirements, upload your documents, and you could have funds in your M-Pesa within hours.
        </p>
      </div>
    </section>

    <!-- ELIGIBILITY CRITERIA -->
    <section class="py-20">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-16">
          <!-- Criteria List -->
          <div>
            <h2 class="section-heading mb-4 text-trust-green">Requirements</h2>
            <h3 class="trust-heading text-3xl mb-8">Basic Eligibility Criteria</h3>
            <div class="space-y-4">
              <div v-for="(c, i) in criteria" :key="i" class="flex items-start gap-4 p-5 bg-vapor-grey rounded-xl">
                <div class="w-10 h-10 bg-trust-green rounded-lg flex items-center justify-center flex-shrink-0">
                  <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5"/></svg>
                </div>
                <div>
                  <h4 class="font-bold mb-1">{{ c.title }}</h4>
                  <p class="text-soft-grey text-sm">{{ c.desc }}</p>
                </div>
              </div>
            </div>
          </div>

          <!-- Important Notes -->
          <div>
            <h2 class="section-heading mb-4 text-warm-gold">Important to Know</h2>
            <h3 class="trust-heading text-3xl mb-8">Before You Apply</h3>
            <div class="space-y-4">
              <div class="p-5 border-l-4 border-warm-gold bg-warm-gold-light rounded-r-xl">
                <h4 class="font-bold mb-1">CRB Check</h4>
                <p class="text-soft-grey text-sm">We perform a credit reference bureau check. A negative listing may affect your application but is not an automatic rejection.</p>
              </div>
              <div class="p-5 border-l-4 border-deepseek-blue bg-trust-blue-light rounded-r-xl">
                <h4 class="font-bold mb-1">AI Verification</h4>
                <p class="text-soft-grey text-sm">DeepSeek AI will analyze your documents for authenticity. Ensure documents are clear, recent, and unedited.</p>
              </div>
              <div class="p-5 border-l-4 border-trust-green bg-trust-green-light rounded-r-xl">
                <h4 class="font-bold mb-1">Employer Verification</h4>
                <p class="text-soft-grey text-sm">We may contact your employer to verify your employment status and salary details.</p>
              </div>
              <div class="p-5 border-l-4 border-alert-magenta bg-pink-50 rounded-r-xl">
                <h4 class="font-bold mb-1">Rejection Warning</h4>
                <p class="text-soft-grey text-sm">Applications with mismatched or fraudulent documents will be rejected. Consistent information across all documents is required.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- REQUIRED DOCUMENTS -->
    <section class="py-20 bg-vapor-grey border-t border-gray-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="trust-heading mb-4">Required Documents</h2>
          <p class="trust-subheading mx-auto">Have these ready before starting your application to speed up the process.</p>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
          <div v-for="(d, i) in documents" :key="i" class="trust-card text-center">
            <div class="w-16 h-16 mx-auto mb-4 rounded-2xl flex items-center justify-center" :class="d.bgColor">
              <svg class="w-8 h-8" :class="d.iconColor" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" :d="d.icon"/></svg>
            </div>
            <h3 class="font-black text-lg mb-2">{{ d.title }}</h3>
            <p class="text-soft-grey text-sm mb-3">{{ d.desc }}</p>
            <div class="text-xs text-trust-green font-bold">{{ d.format }}</div>
          </div>
        </div>
      </div>
    </section>

    <!-- VERIFICATION PROCESS -->
    <section class="py-20 bg-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="trust-heading mb-4">Verification Process</h2>
          <p class="trust-subheading mx-auto">Here's what happens after you upload your documents.</p>
        </div>
        <div class="max-w-4xl mx-auto">
          <div class="grid grid-cols-1 md:grid-cols-4 gap-6">
            <div v-for="(step, i) in verificationSteps" :key="i" class="text-center relative">
              <div class="w-16 h-16 mx-auto mb-4 rounded-full flex items-center justify-center" :class="step.bg">
                <svg class="w-8 h-8" :class="step.icon" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" :d="step.path"/></svg>
              </div>
              <div v-if="i < 3" class="hidden md:block absolute top-8 left-[calc(50%+40px)] w-[calc(100%-80px)] h-0.5 bg-gray-200">
                <div class="absolute right-0 top-[-3px] w-2 h-2 border-t-2 border-r-2 border-gray-300 rotate-45"></div>
              </div>
              <h4 class="font-bold mb-1">{{ step.title }}</h4>
              <p class="text-soft-grey text-xs">{{ step.desc }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- TIPS -->
    <section class="py-16 bg-vapor-grey border-t border-gray-200">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="bg-white border-2 border-ink-black p-8 shadow-hard-md">
          <h3 class="font-black text-xl mb-6 uppercase">Tips to Speed Up Your Approval</h3>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div v-for="(tip, i) in tips" :key="i" class="flex items-start gap-3">
              <svg class="w-5 h-5 text-watch-green flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9.813 15.904L9 18.75l-.813-2.846a4.5 4.5 0 00-3.09-3.09L2.25 12l2.846-.813a4.5 4.5 0 003.09-3.09L9 5.25l.813 2.846a4.5 4.5 0 003.09 3.09L15.75 12l-2.846.813a4.5 4.5 0 00-3.09 3.09z"/></svg>
              <p class="text-sm text-soft-grey">{{ tip }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA -->
    <section class="py-20 bg-trust-green">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h2 class="text-3xl md:text-4xl font-black text-white mb-6">Meet the Criteria?</h2>
        <p class="text-white/80 text-lg mb-10">Start your application now — it only takes a few minutes.</p>
        <RouterLink to="/apply" class="bg-white text-trust-green px-10 py-4 font-black text-sm uppercase tracking-widest hover:bg-ink-black hover:text-watch-green transition-all shadow-hard-md inline-block">
          Apply Now
        </RouterLink>
      </div>
    </section>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router';

const criteria = [
  { title: 'Kenyan Resident', desc: 'You must be a citizen or permanent resident of Kenya with a valid National ID.' },
  { title: 'Age 18 or Above', desc: 'Applicants must be at least 18 years old.' },
  { title: 'Employed for 6+ Months', desc: 'You must have been formally employed for at least 6 consecutive months.' },
  { title: 'Active M-Pesa Account', desc: 'An active Safaricom M-Pesa account is required for disbursement and repayments.' },
  { title: 'Active Bank Account', desc: 'A bank account in your name for additional verification purposes.' },
  { title: 'Net Monthly Salary KSh 15,000+', desc: 'Minimum net monthly salary of KSh 15,000 to qualify for our products.' },
];

const documents = [
  {
    title: '3 Months Payslips',
    desc: 'Recent payslips showing employer name, gross pay, deductions, and net salary.',
    format: 'PDF or JPG • Max 5MB each',
    icon: 'M19.5 14.25v-2.625a3.375 3.375 0 00-3.375-3.375h-1.5A1.125 1.125 0 0113.5 7.125v-1.5a3.375 3.375 0 00-3.375-3.375H8.25m2.25 0H5.625c-.621 0-1.125.504-1.125 1.125v17.25c0 .621.504 1.125 1.125 1.125h12.75c.621 0 1.125-.504 1.125-1.125V11.25a9 9 0 00-9-9z',
    bgColor: 'bg-trust-green/10',
    iconColor: 'text-trust-green',
  },
  {
    title: '2 Months M-Pesa',
    desc: 'Recent M-Pesa statement showing transaction history and regular activity.',
    format: 'PDF • Max 5MB',
    icon: 'M10.5 1.5H8.25A2.25 2.25 0 006 3.75v16.5a2.25 2.25 0 002.25 2.25h7.5A2.25 2.25 0 0018 20.25V3.75a2.25 2.25 0 00-2.25-2.25H13.5m-3 0V3h3V1.5m-3 0h3m-3 18.75h3',
    bgColor: 'bg-trust-green/10',
    iconColor: 'text-trust-green',
  },
  {
    title: '2 Months Bank Statement',
    desc: 'Bank statement to verify income deposits and additional financial activity.',
    format: 'PDF • Max 5MB',
    icon: 'M12 21v-8.25M15.75 21v-8.25M8.25 21v-8.25M3 9l9-6 9 6m-1.5 12V10.332A48.36 48.36 0 0012 9.75c-2.551 0-5.056.2-7.5.582V21M3 21h18M12 6.75h.008v.008H12V6.75z',
    bgColor: 'bg-deepseek-blue/10',
    iconColor: 'text-deepseek-blue',
  },
  {
    title: 'National ID Copy',
    desc: 'Clear photo or scan of your Kenya National ID (front and back).',
    format: 'JPG or PNG • Max 3MB',
    icon: 'M15 9h3.75M15 12h3.75M15 15h3.75M4.5 19.5h15a2.25 2.25 0 002.25-2.25V6.75A2.25 2.25 0 0019.5 4.5h-15a2.25 2.25 0 00-2.25 2.25v10.5A2.25 2.25 0 004.5 19.5zm6-10.125a1.875 1.875 0 11-3.75 0 1.875 1.875 0 013.75 0zm1.294 6.336a6.721 6.721 0 01-3.17.789 6.721 6.721 0 01-3.168-.789 3.376 3.376 0 016.338 0z',
    bgColor: 'bg-warm-gold/10',
    iconColor: 'text-warm-gold',
  },
];

const verificationSteps = [
  { title: 'Upload Docs', desc: 'Securely upload through our encrypted portal', bg: 'bg-trust-green/10', icon: 'text-trust-green', path: 'M3 16.5v2.25A2.25 2.25 0 005.25 21h13.5A2.25 2.25 0 0021 18.75V16.5m-13.5-9L12 3m0 0l4.5 4.5M12 3v13.5' },
  { title: 'AI Reviews', desc: 'DeepSeek AI checks authenticity & income match', bg: 'bg-deepseek-blue/10', icon: 'text-deepseek-blue', path: 'M9.813 15.904L9 18.75l-.813-2.846a4.5 4.5 0 00-3.09-3.09L2.25 12l2.846-.813a4.5 4.5 0 003.09-3.09L9 5.25l.813 2.846a4.5 4.5 0 003.09 3.09L15.75 12l-2.846.813a4.5 4.5 0 00-3.09 3.09z' },
  { title: 'Admin Approves', desc: 'Human review for final decision within 24–48hrs', bg: 'bg-warm-gold/10', icon: 'text-warm-gold', path: 'M9 12.75L11.25 15 15 9.75m-3-7.036A11.959 11.959 0 013.598 6 11.99 11.99 0 003 9.749c0 5.592 3.824 10.29 9 11.623 5.176-1.332 9-6.03 9-11.622 0-1.31-.21-2.571-.598-3.751h-.152c-3.196 0-6.1-1.248-8.25-3.285z' },
  { title: 'Funds Sent', desc: 'M-Pesa disbursement upon approval', bg: 'bg-trust-green/10', icon: 'text-trust-green', path: 'M2.25 18.75a60.07 60.07 0 0115.797 2.101c.727.198 1.453-.342 1.453-1.096V18.75M3.75 4.5v.75A.75.75 0 013 6h-.75m0 0v-.375c0-.621.504-1.125 1.125-1.125H20.25M2.25 6v9m18-10.5v.75c0 .414.336.75.75.75h.75m-1.5-1.5h.375c.621 0 1.125.504 1.125 1.125v9.75c0 .621-.504 1.125-1.125 1.125h-.375m1.5-1.5H21a.75.75 0 00-.75.75v.75m0 0H3.75m0 0h-.375a1.125 1.125 0 01-1.125-1.125V15m1.5 1.5v-.75A.75.75 0 003 15h-.75M15 10.5a3 3 0 11-6 0 3 3 0 016 0zm3 0h.008v.008H18V10.5zm-12 0h.008v.008H6V10.5z' },
];

const tips = [
  'Ensure all documents are recent (within the last 3 months)',
  'Upload clear, unblurred scans or photos of documents',
  'Make sure your name matches across all documents',
  'Use PDF format when possible for faster AI processing',
  'Ensure your M-Pesa statement shows regular salary deposits',
  'Double-check document dates before uploading',
];
</script>
