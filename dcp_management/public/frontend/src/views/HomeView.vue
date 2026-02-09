<template>
  <div class="min-h-screen bg-white">

    <!-- HERO SECTION -->
    <section class="relative pt-16 pb-20 lg:pt-24 lg:pb-28 bg-white overflow-hidden">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
          <div class="text-left z-10">
            <div class="badge-trust mb-6 fade-in-up">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75m-3-7.036A11.959 11.959 0 013.598 6 11.99 11.99 0 003 9.749c0 5.592 3.824 10.29 9 11.623 5.176-1.332 9-6.03 9-11.622 0-1.31-.21-2.571-.598-3.751h-.152c-3.196 0-6.1-1.248-8.25-3.285z"/></svg>
              Licensed by Central Bank of Kenya
            </div>
            <h1 class="text-4xl md:text-6xl lg:text-7xl font-black uppercase tracking-tight leading-[0.95] mb-6 fade-in-up">
              Get a Financial<br/>Boost for Your<br/>Goals &ndash; Up to<br/>
              <span class="text-watch-green">KSh 500K</span><br/>in Minutes!
            </h1>
            <p class="text-lg text-soft-grey mb-10 max-w-xl leading-relaxed fade-in-up delay-100">
              Employee-focused digital loans verified by
              <span class="text-deepseek-blue font-bold">DeepSeek AI</span>
              and disbursed directly to your M-Pesa. No collateral. No long queues.
            </p>
            <div class="flex flex-col sm:flex-row gap-4 fade-in-up delay-200">
              <RouterLink to="/apply" class="btn-primary text-center">Apply Now</RouterLink>
              <RouterLink to="/eligibility" class="btn-trust-outline text-center">Check Eligibility</RouterLink>
            </div>
            <div class="flex flex-wrap gap-6 mt-10 fade-in-up delay-300">
              <div class="flex items-center gap-2 text-xs text-soft-grey">
                <svg class="w-5 h-5 text-trust-green" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M16.5 10.5V6.75a4.5 4.5 0 10-9 0v3.75m-.75 11.25h10.5a2.25 2.25 0 002.25-2.25v-6.75a2.25 2.25 0 00-2.25-2.25H6.75a2.25 2.25 0 00-2.25 2.25v6.75a2.25 2.25 0 002.25 2.25z"/></svg>
                Data Protected
              </div>
              <div class="flex items-center gap-2 text-xs text-soft-grey">
                <svg class="w-5 h-5 text-trust-green" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 6v6h4.5m4.5 0a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                24hr Disbursement
              </div>
              <div class="flex items-center gap-2 text-xs text-soft-grey">
                <svg class="w-5 h-5 text-trust-green" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                CBK Licensed
              </div>
            </div>
          </div>
          <!-- Visual: Payslip Scanner -->
          <div class="relative hidden lg:block fade-in-up delay-300">
            <div class="w-full h-[480px] border-2 border-ink-black relative overflow-hidden bg-vapor-grey shadow-hard-lg">
              <div class="absolute inset-0 z-20 pointer-events-none overflow-hidden">
                <div class="w-full h-1 bg-watch-green shadow-green-glow animate-scan"></div>
              </div>
              <div class="absolute inset-8 border-2 border-ink-black/20 bg-white p-8">
                <div class="space-y-4">
                  <div class="flex justify-between items-center border-b-2 border-ink-black pb-3">
                    <div class="h-4 w-1/3 bg-ink-black/10"></div>
                    <div class="text-[10px] font-black uppercase tracking-widest text-ink-black/30">PAYSLIP</div>
                  </div>
                  <div class="h-6 w-2/3 bg-ink-black/5 border border-ink-black/10"></div>
                  <div class="grid grid-cols-2 gap-4 pt-4">
                    <div class="h-16 bg-vapor-grey border border-ink-black/10 p-3">
                      <div class="text-[8px] font-black uppercase text-ink-black/30 mb-1">GROSS PAY</div>
                      <div class="h-3 w-3/4 bg-ink-black/10"></div>
                    </div>
                    <div class="h-16 bg-watch-green/10 border-2 border-watch-green p-3">
                      <div class="text-[8px] font-black uppercase text-watch-green mb-1">NET PAY</div>
                      <div class="h-3 w-3/4 bg-watch-green/30"></div>
                    </div>
                  </div>
                  <div class="h-3 w-full bg-ink-black/5 mt-6"></div>
                  <div class="h-3 w-full bg-ink-black/5"></div>
                  <div class="h-3 w-2/3 bg-ink-black/5"></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- FEATURES SECTION -->
    <section class="py-20 bg-vapor-grey border-t border-gray-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="trust-heading mb-4">Why Choose Jirani Credit?</h2>
          <p class="trust-subheading mx-auto">Built for Kenya's workforce. Powered by AI. Trusted by thousands.</p>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div class="trust-card text-center group">
            <div class="w-16 h-16 mx-auto mb-6 bg-deepseek-blue/10 rounded-2xl flex items-center justify-center group-hover:bg-deepseek-blue/20 transition-colors">
              <svg class="w-8 h-8 text-deepseek-blue" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9.813 15.904L9 18.75l-.813-2.846a4.5 4.5 0 00-3.09-3.09L2.25 12l2.846-.813a4.5 4.5 0 003.09-3.09L9 5.25l.813 2.846a4.5 4.5 0 003.09 3.09L15.75 12l-2.846.813a4.5 4.5 0 00-3.09 3.09z"/></svg>
            </div>
            <h3 class="text-xl font-black mb-3">Quick Approval with AI</h3>
            <p class="text-soft-grey leading-relaxed">DeepSeek AI verifies your documents in minutes &mdash; payslip OCR, statement analysis, and authenticity checks.</p>
          </div>
          <div class="trust-card text-center group">
            <div class="w-16 h-16 mx-auto mb-6 bg-trust-green/10 rounded-2xl flex items-center justify-center group-hover:bg-trust-green/20 transition-colors">
              <svg class="w-8 h-8 text-trust-green" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M10.5 1.5H8.25A2.25 2.25 0 006 3.75v16.5a2.25 2.25 0 002.25 2.25h7.5A2.25 2.25 0 0018 20.25V3.75a2.25 2.25 0 00-2.25-2.25H13.5m-3 0V3h3V1.5m-3 0h3m-3 18.75h3"/></svg>
            </div>
            <h3 class="text-xl font-black mb-3">Flexible M-Pesa Repayments</h3>
            <p class="text-soft-grey leading-relaxed">Repay conveniently through M-Pesa or automatic salary deductions. Choose what works for you.</p>
          </div>
          <div class="trust-card text-center group">
            <div class="w-16 h-16 mx-auto mb-6 bg-warm-gold/10 rounded-2xl flex items-center justify-center group-hover:bg-warm-gold/20 transition-colors">
              <svg class="w-8 h-8 text-warm-gold" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 6v12m-3-2.818l.879.659c1.171.879 3.07.879 4.242 0 1.172-.879 1.172-2.303 0-3.182C13.536 12.219 12.768 12 12 12c-.725 0-1.45-.22-2.003-.659-1.106-.879-1.106-2.303 0-3.182s2.9-.879 4.006 0l.415.33M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
            </div>
            <h3 class="text-xl font-black mb-3">No Collateral Needed</h3>
            <p class="text-soft-grey leading-relaxed">Your employment is your guarantee. We lend based on your income, not your assets.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- HOW IT WORKS -->
    <section class="py-20 bg-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="trust-heading mb-4">How It Works</h2>
          <p class="trust-subheading mx-auto">From application to cash in your M-Pesa — four simple steps.</p>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-4 gap-8">
          <div v-for="(step, i) in howItWorks" :key="i" class="text-center relative">
            <div class="step-circle active mx-auto mb-6">{{ i + 1 }}</div>
            <div v-if="i < 3" class="hidden md:block absolute top-6 left-[calc(50%+28px)] w-[calc(100%-56px)] h-0.5 bg-trust-green/30"></div>
            <h3 class="font-black text-lg mb-2">{{ step.title }}</h3>
            <p class="text-soft-grey text-sm leading-relaxed">{{ step.desc }}</p>
          </div>
        </div>
        <div class="text-center mt-12">
          <RouterLink to="/how-to-apply" class="btn-trust inline-block">Learn More About the Process</RouterLink>
        </div>
      </div>
    </section>

    <!-- STATS -->
    <section class="py-16 bg-ink-black text-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-2 md:grid-cols-4 gap-8 text-center">
          <div>
            <div class="text-4xl md:text-5xl font-black text-watch-green mb-2">5K+</div>
            <div class="text-xs uppercase tracking-widest text-white/50">Loans Disbursed</div>
          </div>
          <div>
            <div class="text-4xl md:text-5xl font-black text-watch-green mb-2">KSh 200M+</div>
            <div class="text-xs uppercase tracking-widest text-white/50">Total Facilitated</div>
          </div>
          <div>
            <div class="text-4xl md:text-5xl font-black text-watch-green mb-2">98%</div>
            <div class="text-xs uppercase tracking-widest text-white/50">Satisfaction Rate</div>
          </div>
          <div>
            <div class="text-4xl md:text-5xl font-black text-watch-green mb-2">&lt;2hrs</div>
            <div class="text-xs uppercase tracking-widest text-white/50">Avg Disbursement</div>
          </div>
        </div>
      </div>
    </section>

    <!-- TESTIMONIALS -->
    <section class="py-20 bg-vapor-grey">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-16">
          <h2 class="trust-heading mb-4">What Our Customers Say</h2>
          <p class="trust-subheading mx-auto">Real stories from employees who boosted their finances with Jirani Credit.</p>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div v-for="(t, i) in testimonials" :key="i" class="trust-card">
            <div class="flex gap-1 mb-4">
              <svg v-for="s in 5" :key="s" class="w-5 h-5 text-warm-gold" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>
            </div>
            <p class="text-ink-black/70 leading-relaxed mb-6">"{{ t.quote }}"</p>
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 rounded-full bg-trust-green flex items-center justify-center text-white font-black text-sm">{{ t.name.charAt(0) }}</div>
              <div>
                <div class="font-bold text-sm">{{ t.name }}</div>
                <div class="text-xs text-soft-grey">{{ t.location }}</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- TRUST BADGES -->
    <section class="py-16 bg-white border-t border-gray-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex flex-wrap justify-center items-center gap-12">
          <div class="text-center">
            <svg class="w-10 h-10 mx-auto mb-2 text-trust-green" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75m-3-7.036A11.959 11.959 0 013.598 6 11.99 11.99 0 003 9.749c0 5.592 3.824 10.29 9 11.623 5.176-1.332 9-6.03 9-11.622 0-1.31-.21-2.571-.598-3.751h-.152c-3.196 0-6.1-1.248-8.25-3.285z"/></svg>
            <div class="text-xs font-bold uppercase tracking-widest">Licensed by CBK</div>
          </div>
          <div class="text-center">
            <svg class="w-10 h-10 mx-auto mb-2 text-deepseek-blue" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9.813 15.904L9 18.75l-.813-2.846a4.5 4.5 0 00-3.09-3.09L2.25 12l2.846-.813a4.5 4.5 0 003.09-3.09L9 5.25l.813 2.846a4.5 4.5 0 003.09 3.09L15.75 12l-2.846.813a4.5 4.5 0 00-3.09 3.09z"/></svg>
            <div class="text-xs font-bold uppercase tracking-widest">AI Verified</div>
          </div>
          <div class="text-center">
            <svg class="w-10 h-10 mx-auto mb-2 text-trust-green" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M16.5 10.5V6.75a4.5 4.5 0 10-9 0v3.75m-.75 11.25h10.5a2.25 2.25 0 002.25-2.25v-6.75a2.25 2.25 0 00-2.25-2.25H6.75a2.25 2.25 0 00-2.25 2.25v6.75a2.25 2.25 0 002.25 2.25z"/></svg>
            <div class="text-xs font-bold uppercase tracking-widest">Data Protected</div>
          </div>
          <div class="text-center">
            <svg class="w-10 h-10 mx-auto mb-2 text-trust-green" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M10.5 1.5H8.25A2.25 2.25 0 006 3.75v16.5a2.25 2.25 0 002.25 2.25h7.5A2.25 2.25 0 0018 20.25V3.75a2.25 2.25 0 00-2.25-2.25H13.5m-3 0V3h3V1.5m-3 0h3m-3 18.75h3"/></svg>
            <div class="text-xs font-bold uppercase tracking-widest">M-Pesa Integrated</div>
          </div>
        </div>
      </div>
    </section>

    <!-- BOTTOM CTA -->
    <section class="py-20 bg-trust-green">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h2 class="text-3xl md:text-5xl font-black text-white mb-6 uppercase tracking-tight">Ready for Your Financial Boost?</h2>
        <p class="text-white/80 text-lg mb-10 max-w-2xl mx-auto">Apply in minutes. Get approved fast. Receive funds directly to your M-Pesa.</p>
        <div class="flex flex-col sm:flex-row gap-4 justify-center">
          <RouterLink to="/apply" class="bg-white text-trust-green px-10 py-4 font-black text-sm uppercase tracking-widest hover:bg-ink-black hover:text-watch-green transition-all shadow-hard-md">
            Start Your Application
          </RouterLink>
          <RouterLink to="/contact" class="border-2 border-white text-white px-10 py-4 font-black text-sm uppercase tracking-widest hover:bg-white hover:text-trust-green transition-all">
            Talk to Us
          </RouterLink>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { RouterLink, useRouter } from 'vue-router';
import { onMounted } from 'vue';
import { api } from '@/api';

const router = useRouter();

const howItWorks = [
  { title: 'Check Eligibility', desc: 'Verify you meet our simple requirements — employed, Kenyan resident, with valid documents.' },
  { title: 'Upload Documents', desc: 'Securely upload your payslips, M-Pesa and bank statements through our encrypted portal.' },
  { title: 'Get AI Verified', desc: 'DeepSeek AI analyzes your documents instantly. Admin reviews for final approval.' },
  { title: 'Receive Funds', desc: 'Once approved, funds are disbursed directly to your M-Pesa within hours.' },
];

const testimonials = [
  { quote: 'Jirani Credit helped me cover my family\'s school fees without stress. The process was so fast, I had money in my M-Pesa the same day!', name: 'John Kamau', location: 'Nairobi' },
  { quote: 'I was skeptical about online loans, but Jirani\'s transparency and AI verification gave me confidence. Highly recommended for employees.', name: 'Mary Wanjiku', location: 'Mombasa' },
  { quote: 'The repayment through M-Pesa is so convenient. I just set it and forget it. Jirani understands the Kenyan worker.', name: 'Peter Ochieng', location: 'Kisumu' },
];

onMounted(async () => {
  try {
    const res = await api.get('/api/method/dcp_management.api.get_current_user_customer');
    if (res.message && res.message.customer && res.message.customer.kyc_status !== 'Incomplete') {
      router.push({ name: 'dashboard' });
    }
  } catch (error) {
    // Guest user — fine
  }
});
</script>
