<template>
  <div class="min-h-screen bg-white flex items-center justify-center p-4 font-inter text-ink-black">
    <div class="max-w-md w-full">
      <!-- Back Link -->
      <RouterLink to="/" class="text-ink-black/40 hover:text-ink-black flex items-center mb-10 transition-colors uppercase text-[10px] font-black tracking-[0.2em]">
        <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" d="M15 19l-7-7 7-7"></path>
        </svg>
        Back to Home
      </RouterLink>

      <!-- Signup Card -->
      <div class="border-2 border-ink-black bg-white p-10 shadow-hard-lg">
        <div class="text-center mb-10">
          <div class="w-16 h-16 border-2 border-ink-black bg-watch-green flex items-center justify-center mx-auto mb-6">
            <svg class="w-8 h-8 text-ink-black" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M18 9v3m0 0v3m0-3h3m-3 0h-3m-2-5a4 4 0 11-8 0 4 4 0 018 0zM3 20a6 6 0 0112 0v1H3v-1z"></path></svg>
          </div>
          <h1 class="text-3xl font-black mb-2 uppercase tracking-tight">Create Account</h1>
          <p class="text-xs text-ink-black/40 uppercase tracking-[0.2em]">Professional Identity Setup</p>
        </div>

        <!-- Success Message -->
        <div v-if="showSuccess" class="border-2 border-watch-green bg-watch-green/10 text-ink-black px-6 py-4 mb-8">
          <p class="font-black text-sm uppercase tracking-widest">&#10003; Profile Created</p>
          <p class="text-xs mt-1 text-ink-black/60">Redirecting to secure login...</p>
        </div>

        <!-- Error Message -->
        <div v-if="errorMessage" class="border-2 border-alert-magenta bg-alert-magenta/5 text-alert-magenta px-6 py-4 mb-8">
          <p class="text-xs font-black uppercase tracking-widest">{{ errorMessage }}</p>
        </div>

        <form @submit.prevent="submitSignup" class="space-y-6">
          <!-- Full Name -->
          <div>
            <label class="block text-[10px] font-black text-ink-black/40 mb-2 uppercase tracking-[0.2em]">Legal Full Name</label>
            <input
              v-model="form.full_name"
              type="text"
              placeholder="As per ID Card"
              class="w-full"
              required
            >
          </div>

          <!-- Email -->
          <div>
            <label class="block text-[10px] font-black text-ink-black/40 mb-2 uppercase tracking-[0.2em]">Email Address</label>
            <input
              v-model="form.email"
              type="email"
              placeholder="name@company.com"
              class="w-full"
              required
            >
          </div>

          <!-- Phone -->
          <div>
            <label class="block text-[10px] font-black text-ink-black/40 mb-2 uppercase tracking-[0.2em]">M-Pesa Number</label>
            <div class="flex items-end">
              <span class="inline-flex items-center px-4 py-3 border-b-2 border-ink-black text-ink-black/40 font-black text-xs mr-2">
                +254
              </span>
              <input
                v-model="form.phone"
                type="tel"
                placeholder="712345678"
                pattern="[0-9]{9}"
                maxlength="9"
                class="w-full"
                required
              >
            </div>
          </div>

          <!-- Consent -->
          <div class="flex items-start gap-3 p-3 border border-ink-black/20 bg-vapor-grey">
            <input
              v-model="form.agree_terms"
              type="checkbox"
              id="terms"
              class="mt-0.5"
              required
            >
            <label for="terms" class="text-[11px] text-ink-black/60 leading-relaxed">
              I consent to <strong class="text-ink-black">AI Analysis</strong> of my financial documents under the <strong class="text-watch-green">Data Protection Act</strong>.
            </label>
          </div>

          <!-- Submit Button -->
          <button
            type="submit"
            :disabled="loading"
            class="btn-primary w-full text-center disabled:opacity-50 disabled:cursor-not-allowed disabled:shadow-none">
            <span v-if="loading" class="flex items-center justify-center gap-2">
              <svg class="animate-spin h-4 w-4" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
              Creating...
            </span>
            <span v-else>Confirm Identity</span>
          </button>
        </form>

        <!-- Login Link -->
        <p class="mt-8 text-center text-[10px] text-ink-black/40 uppercase tracking-[0.2em]">
          Existing Account?
          <RouterLink to="/login" class="text-watch-green font-black hover:underline">Secure Login</RouterLink>
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue';
import { useRouter, RouterLink } from 'vue-router';
import { api } from '@/api';

const router = useRouter();
const loading = ref(false);
const showSuccess = ref(false);
const errorMessage = ref('');

const form = reactive({
  full_name: '',
  email: '',
  phone: '',
  agree_terms: false
});

const submitSignup = async () => {
  loading.value = true;
  errorMessage.value = '';

  try {
    const nameParts = form.full_name.trim().split(' ');
    const first_name = nameParts[0] || '';
    const last_name = nameParts.slice(1).join(' ') || nameParts[0];

    const res = await api.post('/api/method/dcp_management.api.onboard_customer', {
      first_name,
      last_name,
      email: form.email,
      phone: '+254' + form.phone
    });

    const data = res.message || res;

    if (data.customer_id) {
      showSuccess.value = true;
      setTimeout(() => {
        router.push({ name: 'login' });
      }, 2000);
    } else {
      throw new Error('Onboarding failed');
    }
  } catch (error) {
    errorMessage.value = error.message || 'Account creation failed.';
  } finally {
    loading.value = false;
  }
};
</script>
