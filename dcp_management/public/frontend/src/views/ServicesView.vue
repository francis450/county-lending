<template>
  <div class="min-h-screen bg-white">

    <!-- HERO -->
    <section class="py-20 lg:py-28 bg-gradient-to-b from-trust-blue-light to-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h1 class="trust-heading text-4xl md:text-5xl mb-6 fade-in-up">Tailored Financial Boosts<br/>for Employees</h1>
        <p class="trust-subheading mx-auto fade-in-up delay-100">
          Transparent, fast, and designed for Kenya's working professionals. Choose the loan product that fits your needs.
        </p>
      </div>
    </section>

    <!-- PRODUCT CARDS -->
    <section class="py-20">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">

          <!-- Salary Advance -->
          <div class="trust-card border-2 border-trust-green relative overflow-hidden">
            <div class="absolute top-0 left-0 right-0 h-1 bg-trust-green"></div>
            <div class="badge-trust mb-4">Most Popular</div>
            <h3 class="text-2xl font-black mb-2">Salary Advance</h3>
            <p class="text-soft-grey mb-6">Short-term loans based on your monthly salary. Perfect for bridging the gap before payday.</p>
            <div class="space-y-3 mb-8">
              <div class="flex justify-between py-2 border-b border-gray-100">
                <span class="text-sm text-soft-grey">Loan Amount</span>
                <span class="font-bold text-sm">Up to 50% of salary</span>
              </div>
              <div class="flex justify-between py-2 border-b border-gray-100">
                <span class="text-sm text-soft-grey">Interest Rate</span>
                <span class="font-bold text-sm">5–10% monthly</span>
              </div>
              <div class="flex justify-between py-2 border-b border-gray-100">
                <span class="text-sm text-soft-grey">Repayment</span>
                <span class="font-bold text-sm">1–3 months</span>
              </div>
              <div class="flex justify-between py-2 border-b border-gray-100">
                <span class="text-sm text-soft-grey">Disbursement</span>
                <span class="font-bold text-sm">Same day via M-Pesa</span>
              </div>
            </div>
            <RouterLink to="/apply" class="btn-trust w-full text-center block">Apply for Salary Advance</RouterLink>
          </div>

          <!-- Emergency Loan -->
          <div class="trust-card relative overflow-hidden">
            <div class="absolute top-0 left-0 right-0 h-1 bg-warm-gold"></div>
            <div class="inline-flex items-center gap-2 bg-warm-gold-light text-warm-gold text-xs font-bold px-4 py-2 rounded-full mb-4">Quick Access</div>
            <h3 class="text-2xl font-black mb-2">Emergency Loan</h3>
            <p class="text-soft-grey mb-6">For urgent financial needs — medical, family emergencies, or unexpected expenses.</p>
            <div class="space-y-3 mb-8">
              <div class="flex justify-between py-2 border-b border-gray-100">
                <span class="text-sm text-soft-grey">Loan Amount</span>
                <span class="font-bold text-sm">KSh 5,000 – 100,000</span>
              </div>
              <div class="flex justify-between py-2 border-b border-gray-100">
                <span class="text-sm text-soft-grey">Interest Rate</span>
                <span class="font-bold text-sm">8–15% monthly</span>
              </div>
              <div class="flex justify-between py-2 border-b border-gray-100">
                <span class="text-sm text-soft-grey">Repayment</span>
                <span class="font-bold text-sm">1–6 months</span>
              </div>
              <div class="flex justify-between py-2 border-b border-gray-100">
                <span class="text-sm text-soft-grey">Disbursement</span>
                <span class="font-bold text-sm">Within 2 hours</span>
              </div>
            </div>
            <RouterLink to="/apply" class="btn-trust-outline w-full text-center block">Apply for Emergency Loan</RouterLink>
          </div>

          <!-- Business Boost -->
          <div class="trust-card relative overflow-hidden">
            <div class="absolute top-0 left-0 right-0 h-1 bg-deepseek-blue"></div>
            <div class="inline-flex items-center gap-2 bg-trust-blue-light text-trust-blue text-xs font-bold px-4 py-2 rounded-full mb-4">Growth</div>
            <h3 class="text-2xl font-black mb-2">Business Boost</h3>
            <p class="text-soft-grey mb-6">For employed Kenyans with side businesses. Invest in your growth without risking your salary.</p>
            <div class="space-y-3 mb-8">
              <div class="flex justify-between py-2 border-b border-gray-100">
                <span class="text-sm text-soft-grey">Loan Amount</span>
                <span class="font-bold text-sm">KSh 50,000 – 500,000</span>
              </div>
              <div class="flex justify-between py-2 border-b border-gray-100">
                <span class="text-sm text-soft-grey">Interest Rate</span>
                <span class="font-bold text-sm">10–15% monthly</span>
              </div>
              <div class="flex justify-between py-2 border-b border-gray-100">
                <span class="text-sm text-soft-grey">Repayment</span>
                <span class="font-bold text-sm">3–12 months</span>
              </div>
              <div class="flex justify-between py-2 border-b border-gray-100">
                <span class="text-sm text-soft-grey">Disbursement</span>
                <span class="font-bold text-sm">24–48 hours</span>
              </div>
            </div>
            <RouterLink to="/apply" class="btn-trust-outline w-full text-center block">Apply for Business Boost</RouterLink>
          </div>
        </div>
      </div>
    </section>

    <!-- COMPARISON TABLE -->
    <section class="py-20 bg-vapor-grey border-t border-gray-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-12">
          <h2 class="trust-heading mb-4">Compare Our Products</h2>
          <p class="trust-subheading mx-auto">Find the right loan for your situation.</p>
        </div>
        <div class="overflow-x-auto">
          <table class="w-full bg-white border-2 border-ink-black">
            <thead>
              <tr class="bg-ink-black text-white">
                <th class="px-6 py-4 text-left text-xs font-black uppercase tracking-widest">Feature</th>
                <th class="px-6 py-4 text-center text-xs font-black uppercase tracking-widest">Salary Advance</th>
                <th class="px-6 py-4 text-center text-xs font-black uppercase tracking-widest">Emergency</th>
                <th class="px-6 py-4 text-center text-xs font-black uppercase tracking-widest">Business Boost</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(row, i) in comparisonRows" :key="i" :class="i % 2 === 0 ? 'bg-white' : 'bg-vapor-grey'">
                <td class="px-6 py-4 font-bold text-sm">{{ row.feature }}</td>
                <td class="px-6 py-4 text-center text-sm">{{ row.salary }}</td>
                <td class="px-6 py-4 text-center text-sm">{{ row.emergency }}</td>
                <td class="px-6 py-4 text-center text-sm">{{ row.business }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>

    <!-- BENEFITS -->
    <section class="py-20 bg-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="trust-heading mb-4">Why Jirani Credit Stands Out</h2>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <div v-for="(b, i) in benefits" :key="i" class="flex items-start gap-4 p-6 rounded-xl hover:bg-vapor-grey transition-colors">
            <svg class="w-6 h-6 text-trust-green flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
            <div>
              <h4 class="font-bold mb-1">{{ b.title }}</h4>
              <p class="text-soft-grey text-sm">{{ b.desc }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- FAQ TEASER -->
    <section class="py-16 bg-vapor-grey border-t border-gray-200">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h2 class="trust-heading text-2xl mb-4">Have Questions?</h2>
        <p class="text-soft-grey mb-8">Check our comprehensive FAQ section for answers about eligibility, application process, and more.</p>
        <RouterLink to="/faq" class="btn-trust-outline inline-block">View FAQ</RouterLink>
      </div>
    </section>

    <!-- CTA -->
    <section class="py-20 bg-trust-green">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h2 class="text-3xl md:text-4xl font-black text-white mb-6">Find the Right Loan for You</h2>
        <p class="text-white/80 text-lg mb-10">Start your application today — our AI-powered system will guide you to the best product.</p>
        <RouterLink to="/apply" class="bg-white text-trust-green px-10 py-4 font-black text-sm uppercase tracking-widest hover:bg-ink-black hover:text-watch-green transition-all shadow-hard-md inline-block">
          Start Application
        </RouterLink>
      </div>
    </section>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router';

const comparisonRows = [
  { feature: 'Loan Amount', salary: 'Up to 50% salary', emergency: 'KSh 5K – 100K', business: 'KSh 50K – 500K' },
  { feature: 'Interest Rate', salary: '5–10%/month', emergency: '8–15%/month', business: '10–15%/month' },
  { feature: 'Repayment Term', salary: '1–3 months', emergency: '1–6 months', business: '3–12 months' },
  { feature: 'Collateral', salary: 'None', emergency: 'None', business: 'None' },
  { feature: 'Eligibility', salary: '6+ months employed', emergency: '3+ months employed', business: '12+ months employed' },
  { feature: 'Disbursement Speed', salary: 'Same day', emergency: 'Within 2 hours', business: '24–48 hours' },
  { feature: 'AI Verification', salary: '✓', emergency: '✓', business: '✓' },
  { feature: 'M-Pesa Repayment', salary: '✓', emergency: '✓', business: '✓' },
];

const benefits = [
  { title: 'AI-Powered Verification', desc: 'DeepSeek AI verifies your documents instantly for faster approvals.' },
  { title: 'Admin Oversight', desc: 'Every application gets a human review for fairness and accuracy.' },
  { title: 'No Hidden Fees', desc: 'Our interest rates and fees are clearly stated upfront — no surprises.' },
  { title: 'M-Pesa Integration', desc: 'Receive and repay your loan directly through M-Pesa.' },
  { title: 'Employee-Focused', desc: 'Designed specifically for salaried workers in Kenya.' },
  { title: 'Secure & Compliant', desc: '256-bit encryption and full compliance with Kenya Data Protection Act.' },
];
</script>
