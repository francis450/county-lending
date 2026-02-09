<template>
  <div class="min-h-screen bg-white">

    <!-- HERO -->
    <section class="py-20 lg:py-28 bg-gradient-to-b from-trust-green-light to-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h1 class="trust-heading text-4xl md:text-5xl mb-6 fade-in-up">Frequently Asked Questions</h1>
        <p class="trust-subheading mx-auto fade-in-up delay-100">
          Find answers to common questions about our services, application process, and more.
        </p>
        <!-- Search Bar -->
        <div class="max-w-xl mx-auto mt-10 fade-in-up delay-200">
          <div class="relative">
            <svg class="w-5 h-5 absolute left-4 top-1/2 -translate-y-1/2 text-soft-grey" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z"/></svg>
            <input v-model="searchQuery" type="text" placeholder="Search questions..." class="w-full pl-12 pr-4 py-4 border-2 border-gray-200 rounded-xl focus:border-trust-green bg-white text-sm">
          </div>
        </div>
      </div>
    </section>

    <!-- CATEGORY TABS -->
    <section class="border-b border-gray-200 sticky top-20 bg-white z-40">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex gap-1 overflow-x-auto py-4">
          <button
            v-for="cat in categories"
            :key="cat.id"
            @click="activeCategory = cat.id"
            class="px-5 py-2 text-xs font-bold uppercase tracking-widest rounded-lg whitespace-nowrap transition-all"
            :class="activeCategory === cat.id ? 'bg-trust-green text-white' : 'text-soft-grey hover:bg-vapor-grey'"
          >
            {{ cat.label }}
          </button>
        </div>
      </div>
    </section>

    <!-- FAQ ACCORDION -->
    <section class="py-20">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <div v-if="filteredFaqs.length === 0" class="text-center py-12">
          <p class="text-soft-grey text-lg">No questions match your search. Try different keywords.</p>
        </div>
        <div class="space-y-4">
          <div v-for="(faq, i) in filteredFaqs" :key="i" class="accordion-item" :class="{'active': openIndex === i}">
            <button @click="toggleFaq(i)" class="accordion-trigger">
              <span>{{ faq.q }}</span>
              <svg class="w-5 h-5 flex-shrink-0 transition-transform" :class="{'rotate-180': openIndex === i}" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M19.5 8.25l-7.5 7.5-7.5-7.5"/></svg>
            </button>
            <transition name="slide">
              <div v-if="openIndex === i" class="accordion-content">
                <p>{{ faq.a }}</p>
              </div>
            </transition>
          </div>
        </div>
      </div>
    </section>

    <!-- STILL NEED HELP -->
    <section class="py-20 bg-vapor-grey border-t border-gray-200">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h2 class="trust-heading text-2xl mb-4">Still Need Help?</h2>
        <p class="text-soft-grey mb-8">Our support team is ready to assist you with any questions not covered here.</p>
        <div class="flex flex-col sm:flex-row gap-4 justify-center">
          <RouterLink to="/contact" class="btn-trust inline-block">Contact Us</RouterLink>
          <a href="tel:+254700000000" class="btn-trust-outline inline-block">Call +254 700 000 000</a>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import { RouterLink } from 'vue-router';

const searchQuery = ref('');
const activeCategory = ref('all');
const openIndex = ref(null);

const categories = [
  { id: 'all', label: 'All Questions' },
  { id: 'eligibility', label: 'Eligibility' },
  { id: 'application', label: 'Application' },
  { id: 'verification', label: 'Verification' },
  { id: 'repayment', label: 'Repayments' },
  { id: 'security', label: 'Security' },
];

const faqs = [
  // Eligibility
  { cat: 'eligibility', q: 'Who is eligible for a Jirani Credit loan?', a: 'You must be a Kenyan resident aged 18+, employed for at least 6 consecutive months, with a minimum net monthly salary of KSh 15,000. You also need an active M-Pesa account and bank account.' },
  { cat: 'eligibility', q: 'Can self-employed people apply?', a: 'Currently, our products are designed specifically for formally employed individuals. We are working on expanding our services to include self-employed Kenyans in the future.' },
  { cat: 'eligibility', q: 'What if I have a negative CRB listing?', a: 'A negative CRB listing does not automatically disqualify you. However, it may affect your loan amount or interest rate. Each application is reviewed individually by our AI system and admin team.' },
  { cat: 'eligibility', q: 'Is there a minimum salary requirement?', a: 'Yes, you need a minimum net monthly salary of KSh 15,000 to qualify for our loan products.' },

  // Application
  { cat: 'application', q: 'What documents do I need to apply?', a: 'You need 3 months of recent payslips, 2 months of M-Pesa statements, 2 months of bank statements, and a copy of your National ID. All documents should be in PDF or clear JPG format.' },
  { cat: 'application', q: 'How long does the application process take?', a: 'The online application takes about 10-15 minutes. AI verification is completed within 2-5 minutes. Admin review typically takes 24-48 hours. Total time from application to disbursement is usually under 48 hours.' },
  { cat: 'application', q: 'Can I apply for multiple loans?', a: 'You can only have one active loan at a time. Once your current loan is fully repaid, you can apply for a new one. Repeat borrowers with good repayment history may qualify for higher amounts.' },
  { cat: 'application', q: 'How much can I borrow?', a: 'Loan amounts depend on your product choice and income. Salary advances go up to 50% of your monthly salary. Emergency loans range from KSh 5,000 to 100,000. Business boosts can reach KSh 500,000 for qualified applicants.' },

  // Verification
  { cat: 'verification', q: 'What if DeepSeek AI rejects my documents?', a: 'If AI identifies issues with your documents (blurry images, expired dates, mismatched information), you can re-upload clearer or corrected versions. All applications are also reviewed by a human admin who can make final decisions.' },
  { cat: 'verification', q: 'How does AI verification work?', a: 'DeepSeek AI uses OCR technology to extract data from your payslips and statements. It verifies income amounts, checks for document authenticity, cross-references information across all documents, and flags any inconsistencies for admin review.' },
  { cat: 'verification', q: 'Is my data safe during verification?', a: 'Absolutely. All documents are encrypted with 256-bit encryption during upload and processing. We comply with the Kenya Data Protection Act and ODPC guidelines. Documents are securely deleted after verification is complete.' },
  { cat: 'verification', q: 'How long for approval after AI verification?', a: 'AI verification takes 2-5 minutes. After that, admin review typically takes 24-48 hours. You will receive email and SMS notifications at each stage of the process.' },

  // Repayment
  { cat: 'repayment', q: 'How do I repay my loan?', a: 'You can repay via M-Pesa (Paybill number provided after approval) or through automatic salary deduction if your employer is in our network. You can also make payments through your bank.' },
  { cat: 'repayment', q: 'What happens if I miss a payment?', a: 'Late payments incur a penalty fee as outlined in your loan agreement. We send reminders before due dates via SMS and email. Continuous defaults may be reported to CRB and could affect your future borrowing ability.' },
  { cat: 'repayment', q: 'Can I repay early?', a: 'Yes! You can repay your loan early without any prepayment penalties. Early repayment may even qualify you for better terms on future loans.' },
  { cat: 'repayment', q: 'What are the interest rates?', a: 'Interest rates vary by product: Salary Advance (5-10% monthly), Emergency Loans (8-15% monthly), Business Boost (10-15% monthly). Exact rates depend on your credit profile and loan amount.' },

  // Security
  { cat: 'security', q: 'How is my personal data protected?', a: 'We use 256-bit SSL encryption for all data transmission. Your documents are stored in encrypted servers. We comply with the Kenya Data Protection Act and ODPC regulations. We never share your data with third parties without your consent.' },
  { cat: 'security', q: 'Do you offer two-factor authentication?', a: 'Yes, we support 2FA via SMS. When you log in, a verification code is sent to your registered phone number. We highly recommend enabling 2FA for maximum security.' },
  { cat: 'security', q: 'What happens to my documents after verification?', a: 'After verification is complete and your loan is processed, documents are securely deleted from our active systems within 30 days. Anonymized data is retained for regulatory compliance as required by CBK.' },
];

const filteredFaqs = computed(() => {
  let result = faqs;
  if (activeCategory.value !== 'all') {
    result = result.filter(f => f.cat === activeCategory.value);
  }
  if (searchQuery.value.trim()) {
    const query = searchQuery.value.toLowerCase();
    result = result.filter(f =>
      f.q.toLowerCase().includes(query) || f.a.toLowerCase().includes(query)
    );
  }
  return result;
});

const toggleFaq = (index) => {
  openIndex.value = openIndex.value === index ? null : index;
};
</script>
