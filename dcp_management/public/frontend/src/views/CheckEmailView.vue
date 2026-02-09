<template>
  <div class="min-h-screen bg-white flex items-center justify-center p-4 font-inter text-ink-black">
    <div class="max-w-md w-full">
      <!-- Card -->
      <div class="border-2 border-ink-black bg-white p-8 shadow-hard-lg">
        <!-- Icon -->
        <div class="w-20 h-20 bg-watch-green flex items-center justify-center mx-auto mb-6">
          <svg class="w-10 h-10 text-ink-black" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path>
          </svg>
        </div>

        <div class="text-center">
          <h1 class="text-3xl font-black uppercase tracking-tight mb-3">Check Your Email</h1>
          <p class="text-ink-black/60 mb-6 text-sm">
            We've sent a password setup link to <strong class="text-ink-black">{{ email }}</strong>
          </p>

          <div class="bg-vapor-grey border-2 border-ink-black/10 p-4 mb-6 text-left">
            <p class="text-[10px] font-black uppercase tracking-widest text-ink-black mb-3">Next Steps:</p>
            <ol class="text-sm text-ink-black/60 space-y-2 ml-4 list-decimal">
              <li>Check your email inbox (and spam folder)</li>
              <li>Click the "Set Password" link in the email</li>
              <li>Create a secure password for your account</li>
              <li>After setting password, navigate to <strong>/portal</strong></li>
              <li>Complete your KYC verification</li>
            </ol>
          </div>

          <!-- Warning -->
          <div class="border-2 border-alert-magenta/30 bg-alert-magenta/5 p-4 mb-6">
            <div class="flex items-start gap-2">
              <svg class="w-5 h-5 text-alert-magenta flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path>
              </svg>
              <p class="text-sm text-ink-black/70">
                <strong>Important:</strong> The link expires in 24 hours.
              </p>
            </div>
          </div>

          <!-- Resend -->
          <button
            v-if="showResend"
            @click="resendEmail"
            :disabled="resendLoading"
            class="btn-primary w-full text-center mb-4 disabled:opacity-50 disabled:shadow-none">
            <span v-if="resendLoading">Sending...</span>
            <span v-else>Resend Email</span>
          </button>

          <p v-else class="text-xs text-ink-black/30 mb-4">
            Didn't receive it? You can resend in <strong>{{ resendCountdown }}s</strong>
          </p>

          <RouterLink to="/login" class="text-[10px] font-black uppercase tracking-[0.2em] text-deepseek-blue hover:underline">
            Go to Login
          </RouterLink>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import { useRoute, RouterLink } from 'vue-router';

const route = useRoute();
const email = ref(route.query.email || 'your email');
const showResend = ref(false);
const resendLoading = ref(false);
const resendCountdown = ref(60);
let countdownTimer = null;

const startCountdown = () => {
  resendCountdown.value = 60;
  showResend.value = false;
  countdownTimer = setInterval(() => {
    resendCountdown.value--;
    if (resendCountdown.value <= 0) {
      clearInterval(countdownTimer);
      showResend.value = true;
    }
  }, 1000);
};

const resendEmail = async () => {
  resendLoading.value = true;
  // Simulate resend
  await new Promise(r => setTimeout(r, 1500));
  resendLoading.value = false;
  startCountdown();
};

onMounted(() => startCountdown());
onUnmounted(() => clearInterval(countdownTimer));
</script>
