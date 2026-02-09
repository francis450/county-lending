<template>
  <div class="min-h-screen bg-white">

    <!-- HERO -->
    <section class="py-20 lg:py-28 bg-gradient-to-b from-trust-blue-light to-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h1 class="trust-heading text-4xl md:text-5xl mb-6 fade-in-up">We're Here to Help</h1>
        <p class="trust-subheading mx-auto fade-in-up delay-100">
          Have a question, concern, or feedback? Our team is ready to assist you. Reach out through any of the channels below.
        </p>
      </div>
    </section>

    <!-- CONTACT CONTENT -->
    <section class="py-20">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-16">

          <!-- Contact Form -->
          <div>
            <h2 class="trust-heading text-2xl mb-6">Send Us a Message</h2>
            <p class="text-soft-grey mb-8">Fill out the form below and we'll get back to you within 24 hours.</p>

            <form @submit.prevent="submitForm" class="space-y-6">
              <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
                <div>
                  <label class="block text-xs font-bold uppercase tracking-widest mb-2">Full Name *</label>
                  <input v-model="form.name" type="text" required placeholder="John Kamau" class="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:border-trust-green bg-white">
                </div>
                <div>
                  <label class="block text-xs font-bold uppercase tracking-widest mb-2">Email Address *</label>
                  <input v-model="form.email" type="email" required placeholder="john@example.com" class="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:border-trust-green bg-white">
                </div>
              </div>

              <div>
                <label class="block text-xs font-bold uppercase tracking-widest mb-2">Phone Number</label>
                <input v-model="form.phone" type="tel" placeholder="+254 700 000 000" class="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:border-trust-green bg-white">
              </div>

              <div>
                <label class="block text-xs font-bold uppercase tracking-widest mb-2">Subject *</label>
                <select v-model="form.subject" required class="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:border-trust-green bg-white">
                  <option value="">Select a topic...</option>
                  <option value="general">General Inquiry</option>
                  <option value="application">Loan Application</option>
                  <option value="repayment">Repayment Issues</option>
                  <option value="documents">Document Verification</option>
                  <option value="complaint">Complaint</option>
                  <option value="partnership">Partnership Inquiry</option>
                </select>
              </div>

              <div>
                <label class="block text-xs font-bold uppercase tracking-widest mb-2">Message *</label>
                <textarea v-model="form.message" required rows="5" placeholder="Tell us how we can help..." class="w-full px-4 py-3 border-2 border-gray-200 rounded-xl focus:border-trust-green bg-white resize-none"></textarea>
              </div>

              <!-- CAPTCHA placeholder -->
              <div class="flex items-center gap-3 p-4 bg-vapor-grey rounded-xl">
                <input type="checkbox" v-model="captchaVerified" class="w-5 h-5">
                <span class="text-sm text-soft-grey">I'm not a robot</span>
                <svg class="w-6 h-6 text-soft-grey ml-auto" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75m-3-7.036A11.959 11.959 0 013.598 6 11.99 11.99 0 003 9.749c0 5.592 3.824 10.29 9 11.623 5.176-1.332 9-6.03 9-11.622 0-1.31-.21-2.571-.598-3.751h-.152c-3.196 0-6.1-1.248-8.25-3.285z"/></svg>
              </div>

              <button type="submit" :disabled="!captchaVerified || submitting" class="btn-trust w-full disabled:opacity-50 disabled:cursor-not-allowed">
                {{ submitting ? 'Sending...' : 'Send Message' }}
              </button>

              <p v-if="submitted" class="text-trust-green text-sm font-bold text-center">
                Message sent successfully! We'll get back to you within 24 hours.
              </p>
            </form>
          </div>

          <!-- Contact Info & Map -->
          <div>
            <h2 class="trust-heading text-2xl mb-6">Contact Information</h2>
            <p class="text-soft-grey mb-8">Reach us through any of these channels. Our support team is available Monday to Friday, 8AM to 6PM EAT.</p>

            <div class="space-y-6 mb-10">
              <div class="flex items-start gap-4 p-5 bg-vapor-grey rounded-xl">
                <div class="w-12 h-12 bg-trust-green rounded-xl flex items-center justify-center flex-shrink-0">
                  <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M15 10.5a3 3 0 11-6 0 3 3 0 016 0z"/><path stroke-linecap="round" stroke-linejoin="round" d="M19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1115 0z"/></svg>
                </div>
                <div>
                  <h4 class="font-bold mb-1">Office Address</h4>
                  <p class="text-soft-grey text-sm">Jirani Credit Limited<br/>Westlands Business Centre<br/>Waiyaki Way, Nairobi, Kenya</p>
                </div>
              </div>

              <div class="flex items-start gap-4 p-5 bg-vapor-grey rounded-xl">
                <div class="w-12 h-12 bg-trust-green rounded-xl flex items-center justify-center flex-shrink-0">
                  <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M2.25 6.75c0 8.284 6.716 15 15 15h2.25a2.25 2.25 0 002.25-2.25v-1.372c0-.516-.351-.966-.852-1.091l-4.423-1.106c-.44-.11-.902.055-1.173.417l-.97 1.293c-.282.376-.769.542-1.21.38a12.035 12.035 0 01-7.143-7.143c-.162-.441.004-.928.38-1.21l1.293-.97c.363-.271.527-.734.417-1.173L6.963 3.102a1.125 1.125 0 00-1.091-.852H4.5A2.25 2.25 0 002.25 4.5v2.25z"/></svg>
                </div>
                <div>
                  <h4 class="font-bold mb-1">Phone</h4>
                  <p class="text-soft-grey text-sm">+254 700 000 000<br/>+254 20 000 0000</p>
                </div>
              </div>

              <div class="flex items-start gap-4 p-5 bg-vapor-grey rounded-xl">
                <div class="w-12 h-12 bg-trust-green rounded-xl flex items-center justify-center flex-shrink-0">
                  <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M21.75 6.75v10.5a2.25 2.25 0 01-2.25 2.25h-15a2.25 2.25 0 01-2.25-2.25V6.75m19.5 0A2.25 2.25 0 0019.5 4.5h-15a2.25 2.25 0 00-2.25 2.25m19.5 0v.243a2.25 2.25 0 01-1.07 1.916l-7.5 4.615a2.25 2.25 0 01-2.36 0L3.32 8.91a2.25 2.25 0 01-1.07-1.916V6.75"/></svg>
                </div>
                <div>
                  <h4 class="font-bold mb-1">Email</h4>
                  <p class="text-soft-grey text-sm">info@jiranicredit.co.ke<br/>support@jiranicredit.co.ke</p>
                </div>
              </div>

              <div class="flex items-start gap-4 p-5 bg-vapor-grey rounded-xl">
                <div class="w-12 h-12 bg-trust-green rounded-xl flex items-center justify-center flex-shrink-0">
                  <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 6v6h4.5m4.5 0a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                </div>
                <div>
                  <h4 class="font-bold mb-1">Business Hours</h4>
                  <p class="text-soft-grey text-sm">Monday – Friday: 8:00 AM – 6:00 PM EAT<br/>Saturday: 9:00 AM – 1:00 PM EAT<br/>Sunday &amp; Holidays: Closed</p>
                </div>
              </div>
            </div>

            <!-- Social Links -->
            <div>
              <h4 class="font-bold mb-4">Follow Us</h4>
              <div class="flex gap-3">
                <a href="https://twitter.com/jiranicredit" target="_blank" class="w-10 h-10 bg-ink-black text-white flex items-center justify-center rounded-lg hover:bg-trust-green transition-colors">
                  <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
                </a>
                <a href="https://facebook.com/jiranicredit" target="_blank" class="w-10 h-10 bg-ink-black text-white flex items-center justify-center rounded-lg hover:bg-trust-green transition-colors">
                  <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
                </a>
              </div>
            </div>

            <!-- Map Placeholder -->
            <div class="mt-10 bg-vapor-grey border-2 border-gray-200 rounded-2xl h-64 flex items-center justify-center">
              <div class="text-center text-soft-grey">
                <svg class="w-12 h-12 mx-auto mb-2 text-gray-300" fill="none" stroke="currentColor" stroke-width="1" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M15 10.5a3 3 0 11-6 0 3 3 0 016 0z"/><path stroke-linecap="round" stroke-linejoin="round" d="M19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1115 0z"/></svg>
                <p class="text-sm">Google Maps integration<br/>Westlands, Nairobi</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- RESPONSE TIMES -->
    <section class="py-16 bg-vapor-grey border-t border-gray-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 class="trust-heading text-2xl text-center mb-10">Expected Response Times</h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div class="trust-card text-center">
            <div class="text-3xl font-black text-trust-green mb-2">&lt; 24hrs</div>
            <h4 class="font-bold mb-1">Email Support</h4>
            <p class="text-soft-grey text-sm">For general inquiries and non-urgent matters</p>
          </div>
          <div class="trust-card text-center">
            <div class="text-3xl font-black text-trust-green mb-2">Instant</div>
            <h4 class="font-bold mb-1">Phone Support</h4>
            <p class="text-soft-grey text-sm">During business hours for urgent requests</p>
          </div>
          <div class="trust-card text-center">
            <div class="text-3xl font-black text-trust-green mb-2">&lt; 5 min</div>
            <h4 class="font-bold mb-1">Live Chat</h4>
            <p class="text-soft-grey text-sm">Available during business hours</p>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const form = ref({
  name: '',
  email: '',
  phone: '',
  subject: '',
  message: '',
});
const captchaVerified = ref(false);
const submitting = ref(false);
const submitted = ref(false);

const submitForm = async () => {
  if (!captchaVerified.value) return;
  submitting.value = true;
  // Simulate form submission
  await new Promise(resolve => setTimeout(resolve, 1500));
  submitting.value = false;
  submitted.value = true;
  form.value = { name: '', email: '', phone: '', subject: '', message: '' };
  captchaVerified.value = false;
  setTimeout(() => { submitted.value = false; }, 5000);
};
</script>
