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

      <!-- Login Card -->
      <div class="border-2 border-ink-black bg-white p-10 shadow-hard-lg">
        <div class="text-center mb-10">
          <div class="w-16 h-16 border-2 border-ink-black flex items-center justify-center mx-auto mb-6">
            <svg class="w-8 h-8 text-deepseek-blue" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"></path></svg>
          </div>
          <h1 class="text-3xl font-black mb-2 uppercase tracking-tight">Secure Login</h1>
          <p class="text-xs text-ink-black/40 uppercase tracking-[0.2em]">Identity Authentication Required</p>
        </div>

        <div v-if="errorMessage" class="border-2 border-alert-magenta bg-alert-magenta/5 text-alert-magenta px-6 py-4 mb-8">
          <p class="text-xs font-black uppercase tracking-widest">{{ errorMessage }}</p>
        </div>

        <form @submit.prevent="handleLogin" class="space-y-6">
          <!-- Email -->
          <div>
            <label class="block text-[10px] font-black text-ink-black/40 mb-2 uppercase tracking-[0.2em]">Email Address</label>
            <input
              v-model="email"
              type="email"
              placeholder="name@company.com"
              class="w-full"
              required
            >
          </div>

          <!-- Password -->
          <div>
            <label class="block text-[10px] font-black text-ink-black/40 mb-2 uppercase tracking-[0.2em]">Password</label>
            <input
              v-model="password"
              type="password"
              placeholder="••••••••"
              class="w-full"
              required
            >
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
              Authenticating...
            </span>
            <span v-else>Authorize Session</span>
          </button>
        </form>

        <p class="mt-8 text-center text-[10px] text-ink-black/40 uppercase tracking-[0.2em]">
          New Professional?
          <RouterLink to="/onboard" class="text-watch-green font-black hover:underline">Get Started</RouterLink>
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter, RouterLink } from 'vue-router';
import { useCustomerStore } from '@/stores/customer';

const router = useRouter();
const customerStore = useCustomerStore();

const email = ref('');
const password = ref('');
const loading = ref(false);
const errorMessage = ref('');

const handleLogin = async () => {
  loading.value = true;
  errorMessage.value = '';

  try {
    const csrfToken = window.csrf_token || '';

    const res = await fetch('/api/method/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'X-Frappe-CSRF-Token': csrfToken,
      },
      credentials: 'include',
      body: JSON.stringify({ usr: email.value, pwd: password.value }),
    });

    const data = await res.json();

    if (!res.ok) {
      // Show the actual server message if available
      const msg = data?.message || data?.exc_type || `Login failed (HTTP ${res.status})`;
      errorMessage.value = msg;
      console.error('Login failed:', data);
      return;
    }

    // Login succeeded — load customer profile then redirect
    await customerStore.fetchCurrentUser();
    router.push({ name: 'dashboard' });
  } catch (error) {
    console.error('Login error:', error);
    errorMessage.value = error?.message || 'Network error. Please check your connection.';
  } finally {
    loading.value = false;
  }
};
</script>
