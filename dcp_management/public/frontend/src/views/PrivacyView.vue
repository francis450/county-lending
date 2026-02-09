<template>
  <div class="min-h-screen bg-white">
    <!-- HERO -->
    <section class="py-16 bg-gradient-to-b from-vapor-grey to-white">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <h1 class="trust-heading text-3xl md:text-4xl mb-4">Privacy Policy</h1>
        <p class="text-soft-grey">Last updated: February 1, 2026</p>
      </div>
    </section>

    <section class="py-16">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="prose prose-lg max-w-none">

          <div class="mb-12">
            <h2 class="text-2xl font-black mb-4">1. Introduction</h2>
            <p class="text-soft-grey leading-relaxed mb-4">
              Jirani Credit Limited ("we," "our," or "us") is committed to protecting the privacy and security of your personal information. This Privacy Policy explains how we collect, use, share, and protect your data when you use our digital lending platform and services.
            </p>
            <p class="text-soft-grey leading-relaxed">
              We operate in compliance with the Kenya Data Protection Act, 2019 and the regulations set forth by the Office of the Data Protection Commissioner (ODPC). By using our services, you agree to the practices described in this policy.
            </p>
          </div>

          <div class="mb-12">
            <h2 class="text-2xl font-black mb-4">2. Data We Collect</h2>
            <p class="text-soft-grey leading-relaxed mb-4">We collect the following categories of personal data:</p>
            <div class="space-y-4">
              <div class="p-4 bg-vapor-grey rounded-xl">
                <h4 class="font-bold mb-2">Personal Identification</h4>
                <p class="text-soft-grey text-sm">Full name, National ID number, date of birth, phone number, email address, and physical address.</p>
              </div>
              <div class="p-4 bg-vapor-grey rounded-xl">
                <h4 class="font-bold mb-2">Employment Information</h4>
                <p class="text-soft-grey text-sm">Employer name and address, job title, employment duration, and monthly salary details.</p>
              </div>
              <div class="p-4 bg-vapor-grey rounded-xl">
                <h4 class="font-bold mb-2">Financial Documents</h4>
                <p class="text-soft-grey text-sm">Payslips, M-Pesa statements, bank statements, and any other documents you upload for verification.</p>
              </div>
              <div class="p-4 bg-vapor-grey rounded-xl">
                <h4 class="font-bold mb-2">Technical Data</h4>
                <p class="text-soft-grey text-sm">IP address, browser type, device information, and usage patterns on our platform.</p>
              </div>
            </div>
          </div>

          <div class="mb-12">
            <h2 class="text-2xl font-black mb-4">3. How We Use Your Data</h2>
            <ul class="space-y-3">
              <li v-for="(use, i) in dataUses" :key="i" class="flex items-start gap-3 text-soft-grey">
                <svg class="w-5 h-5 text-trust-green flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4.5 12.75l6 6 9-13.5"/></svg>
                <span>{{ use }}</span>
              </li>
            </ul>
          </div>

          <div class="mb-12">
            <h2 class="text-2xl font-black mb-4">4. AI Document Processing</h2>
            <div class="p-6 border-l-4 border-deepseek-blue bg-trust-blue-light rounded-r-xl mb-4">
              <h4 class="font-bold mb-2">DeepSeek AI Verification</h4>
              <p class="text-soft-grey text-sm leading-relaxed">
                We use DeepSeek AI technology to process and verify your uploaded documents. This includes OCR (Optical Character Recognition) to extract text from payslips, analysis of transaction patterns from M-Pesa and bank statements, and cross-verification of information across documents. All AI processing is performed on encrypted data.
              </p>
            </div>
            <p class="text-soft-grey leading-relaxed">
              AI analysis results are used to assist human administrators in making loan approval decisions. AI does not make final lending decisions autonomously — all applications undergo human admin review.
            </p>
          </div>

          <div class="mb-12">
            <h2 class="text-2xl font-black mb-4">5. Data Sharing</h2>
            <p class="text-soft-grey leading-relaxed mb-4">We may share your data with:</p>
            <ul class="space-y-2 text-soft-grey">
              <li class="flex items-start gap-2"><span class="text-ink-black font-bold">Credit Reference Bureaus (CRBs):</span> As required by CBK regulations for credit reporting.</li>
              <li class="flex items-start gap-2"><span class="text-ink-black font-bold">Safaricom (M-Pesa):</span> For loan disbursement and repayment processing.</li>
              <li class="flex items-start gap-2"><span class="text-ink-black font-bold">Regulatory Authorities:</span> When required by law or regulatory mandate.</li>
              <li class="flex items-start gap-2"><span class="text-ink-black font-bold">Employers:</span> Only for employment verification, with your consent.</li>
            </ul>
            <p class="text-soft-grey leading-relaxed mt-4">We do not sell your personal data to third parties for marketing purposes.</p>
          </div>

          <div class="mb-12">
            <h2 class="text-2xl font-black mb-4">6. Data Security</h2>
            <p class="text-soft-grey leading-relaxed mb-4">We implement industry-standard security measures including:</p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div class="flex items-center gap-3 p-4 bg-vapor-grey rounded-xl">
                <svg class="w-6 h-6 text-trust-green" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M16.5 10.5V6.75a4.5 4.5 0 10-9 0v3.75m-.75 11.25h10.5a2.25 2.25 0 002.25-2.25v-6.75a2.25 2.25 0 00-2.25-2.25H6.75a2.25 2.25 0 00-2.25 2.25v6.75a2.25 2.25 0 002.25 2.25z"/></svg>
                <span class="text-sm font-bold">256-bit SSL Encryption</span>
              </div>
              <div class="flex items-center gap-3 p-4 bg-vapor-grey rounded-xl">
                <svg class="w-6 h-6 text-trust-green" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75m-3-7.036A11.959 11.959 0 013.598 6 11.99 11.99 0 003 9.749c0 5.592 3.824 10.29 9 11.623 5.176-1.332 9-6.03 9-11.622 0-1.31-.21-2.571-.598-3.751h-.152c-3.196 0-6.1-1.248-8.25-3.285z"/></svg>
                <span class="text-sm font-bold">Two-Factor Authentication</span>
              </div>
              <div class="flex items-center gap-3 p-4 bg-vapor-grey rounded-xl">
                <svg class="w-6 h-6 text-trust-green" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5.25 14.25h13.5m-13.5 0a3 3 0 01-3-3m3 3a3 3 0 100 6h13.5a3 3 0 100-6m-16.5-3a3 3 0 013-3h13.5a3 3 0 013 3m-19.5 0a4.5 4.5 0 01.9-2.7L5.737 5.1a3.375 3.375 0 012.7-1.35h7.126c1.062 0 2.062.5 2.7 1.35l2.587 3.45a4.5 4.5 0 01.9 2.7m0 0a3 3 0 01-3 3m0 3h.008v.008h-.008v-.008zm0-6h.008v.008h-.008v-.008zm-3 6h.008v.008h-.008v-.008zm0-6h.008v.008h-.008v-.008z"/></svg>
                <span class="text-sm font-bold">Encrypted Server Storage</span>
              </div>
              <div class="flex items-center gap-3 p-4 bg-vapor-grey rounded-xl">
                <svg class="w-6 h-6 text-trust-green" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 6v6h4.5m4.5 0a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                <span class="text-sm font-bold">Regular Security Audits</span>
              </div>
            </div>
          </div>

          <div class="mb-12">
            <h2 class="text-2xl font-black mb-4">7. Your Rights</h2>
            <p class="text-soft-grey leading-relaxed mb-4">Under the Kenya Data Protection Act, you have the right to:</p>
            <ul class="space-y-2 text-soft-grey">
              <li>• Access your personal data held by us</li>
              <li>• Request correction of inaccurate data</li>
              <li>• Request deletion of your data (subject to legal requirements)</li>
              <li>• Object to certain processing activities</li>
              <li>• Data portability — receive your data in a structured format</li>
              <li>• Withdraw consent at any time</li>
            </ul>
            <p class="text-soft-grey leading-relaxed mt-4">To exercise these rights, contact our Data Protection Officer at <strong>dpo@jiranicredit.co.ke</strong>.</p>
          </div>

          <div class="mb-12">
            <h2 class="text-2xl font-black mb-4">8. Cookie Policy</h2>
            <p class="text-soft-grey leading-relaxed">
              We use essential cookies for platform functionality (login sessions, security tokens) and analytics cookies (Google Analytics) to improve our services. You can manage cookie preferences through your browser settings.
            </p>
          </div>

          <div class="mb-12">
            <h2 class="text-2xl font-black mb-4">9. Data Retention</h2>
            <p class="text-soft-grey leading-relaxed">
              Uploaded documents are securely deleted within 30 days of verification completion. Account data is retained for the duration of your relationship with us plus 7 years as required by CBK regulations. Anonymized data may be retained indefinitely for statistical analysis.
            </p>
          </div>

          <div>
            <h2 class="text-2xl font-black mb-4">10. Contact Us</h2>
            <p class="text-soft-grey leading-relaxed">
              For privacy-related inquiries, contact our Data Protection Officer:<br/>
              Email: <strong>dpo@jiranicredit.co.ke</strong><br/>
              Phone: <strong>+254 700 000 000</strong><br/>
              Address: Westlands Business Centre, Waiyaki Way, Nairobi, Kenya
            </p>
          </div>

        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
const dataUses = [
  'To verify your identity and assess loan eligibility',
  'To process your loan application and disburse funds',
  'To perform AI-powered document verification via DeepSeek',
  'To conduct credit checks through licensed Credit Reference Bureaus',
  'To communicate with you about your application status and account',
  'To comply with regulatory requirements (CBK, ODPC)',
  'To improve our services and user experience through analytics',
  'To prevent fraud and unauthorized access',
];
</script>
