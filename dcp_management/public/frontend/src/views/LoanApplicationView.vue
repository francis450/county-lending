<template>
  <div class="min-h-screen bg-vapor-grey p-4 py-12 font-inter text-ink-black">
    <div class="max-w-4xl mx-auto">
      <!-- Header -->
      <div class="mb-8">
        <RouterLink to="/dashboard" class="text-ink-black/40 hover:text-ink-black flex items-center mb-4 text-[10px] font-black uppercase tracking-[0.2em] transition">
          <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" d="M15 19l-7-7 7-7"></path>
          </svg>
          Back to Dashboard
        </RouterLink>
        <h1 class="text-4xl font-black uppercase tracking-tight">Apply for a Loan</h1>
        <p class="text-ink-black/50 text-sm mt-2">Complete your application in minutes.</p>
      </div>

      <!-- Steps Indicator -->
      <div class="flex gap-1 mb-8 max-w-2xl">
        <div :class="['h-2 flex-1', currentStep >= 1 ? 'bg-watch-green' : 'bg-ink-black/10']"></div>
        <div :class="['h-2 flex-1', currentStep >= 2 ? 'bg-watch-green' : 'bg-ink-black/10']"></div>
      </div>

      <div class="grid md:grid-cols-2 gap-8">
        <!-- Application Form -->
        <div class="border-2 border-ink-black bg-white p-8 shadow-hard-md">
          <h2 class="text-2xl font-black mb-6 uppercase">Loan Details</h2>

          <!-- Error Message -->
          <div v-if="errorMessage" class="border-2 border-alert-magenta bg-alert-magenta/5 text-alert-magenta px-4 py-3 mb-6">
            <p class="text-xs font-black uppercase">{{ errorMessage }}</p>
          </div>

          <form @submit.prevent="handleSubmit" class="space-y-6">
            <div v-if="currentStep === 1">
              <!-- Loan Amount -->
              <div class="mb-6">
                <label class="block text-[10px] font-black text-ink-black/40 mb-2 uppercase tracking-[0.2em]">
                  How much do you need?
                </label>
                <div class="relative">
                  <span class="absolute left-0 top-3 text-ink-black/40 font-black text-sm">KES</span>
                  <input
                    v-model.number="amount"
                    type="number"
                    min="1000" max="100000" step="1000"
                    class="w-full pl-12 text-2xl font-black"
                    required
                  />
                </div>
                <input
                  v-model.number="amount"
                  type="range"
                  min="1000" max="100000" step="1000"
                  class="w-full mt-3 accent-watch-green"
                >
                <div class="flex justify-between text-[10px] text-ink-black/30 font-black uppercase tracking-widest mt-1">
                  <span>KES 1,000</span>
                  <span>KES 100,000</span>
                </div>
              </div>

              <!-- Tenure -->
              <div class="mb-6">
                <label class="block text-[10px] font-black text-ink-black/40 mb-3 uppercase tracking-[0.2em]">
                  Repayment Period
                </label>
                <div class="grid grid-cols-3 gap-3">
                  <button
                    v-for="option in tenureOptions"
                    :key="option.value"
                    type="button"
                    @click="tenure = option.value"
                    :class="[
                      'py-3 px-4 border-2 font-black text-sm uppercase transition-all',
                      tenure === option.value
                        ? 'border-watch-green bg-watch-green text-ink-black shadow-hard-sm'
                        : 'border-ink-black bg-white hover:bg-vapor-grey'
                    ]">
                    {{ option.label }}
                  </button>
                </div>
              </div>

              <!-- Loan Purpose -->
              <div>
                <label class="block text-[10px] font-black text-ink-black/40 mb-2 uppercase tracking-[0.2em]">
                  Loan Purpose
                </label>
                <select v-model="purpose" class="w-full border-b-2 border-ink-black bg-white py-3 font-semibold" required>
                  <option value="" disabled>Select a purpose</option>
                  <option value="business">Business</option>
                  <option value="emergency">Emergency</option>
                  <option value="education">Education</option>
                  <option value="personal">Personal Use</option>
                  <option value="other">Other</option>
                </select>
              </div>
            </div>

            <div v-if="currentStep === 2">
              <h3 class="font-black text-lg mb-4 uppercase">Review Application</h3>
              <div class="bg-vapor-grey border-2 border-ink-black/10 p-4 space-y-3 mb-6">
                <div class="flex justify-between">
                  <span class="text-ink-black/50 text-sm">Amount:</span>
                  <span class="font-black">KES {{ amount.toLocaleString() }}</span>
                </div>
                <div class="flex justify-between">
                  <span class="text-ink-black/50 text-sm">Period:</span>
                  <span class="font-black">{{ tenure }} Months</span>
                </div>
                <div class="flex justify-between">
                  <span class="text-ink-black/50 text-sm">Purpose:</span>
                  <span class="font-black capitalize">{{ purpose }}</span>
                </div>
              </div>

              <!-- Consent (ODPC) -->
              <div class="flex items-start gap-3 p-3 border border-ink-black/20 bg-vapor-grey">
                <input type="checkbox" v-model="termsAccepted" id="terms" class="mt-0.5" required>
                <label for="terms" class="text-[11px] text-ink-black/60 leading-relaxed">
                  I agree to the Terms and Conditions and consent to checking of my credit status with CRB.
                </label>
              </div>
            </div>

            <!-- Navigation -->
            <div class="pt-4 flex gap-4">
              <button
                v-if="currentStep === 2"
                type="button"
                @click="currentStep = 1"
                class="flex-1 border-2 border-ink-black bg-white text-ink-black font-black py-4 px-4 uppercase text-xs tracking-widest shadow-hard-sm hover:shadow-hard-md transition-all">
                Back
              </button>
              <button
                type="submit"
                :disabled="loading"
                class="flex-1 btn-primary text-center disabled:opacity-50 disabled:shadow-none">
                <span v-if="loading">Processing...</span>
                <span v-else>{{ currentStep === 1 ? 'Continue' : 'Submit Application' }}</span>
              </button>
            </div>
          </form>
        </div>

        <!-- Info Column -->
        <div class="hidden md:block">
          <div class="border-2 border-ink-black bg-white p-8 shadow-hard-md">
            <h3 class="text-xl font-black mb-4 uppercase">Why Jirani Credit?</h3>
            <ul class="space-y-4">
              <li class="flex items-center gap-3">
                <div class="w-8 h-8 bg-watch-green flex items-center justify-center flex-shrink-0">
                  <svg class="w-5 h-5 text-ink-black" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
                </div>
                <span class="font-semibold text-sm">Instant approval &amp; disbursement</span>
              </li>
              <li class="flex items-center gap-3">
                <div class="w-8 h-8 bg-watch-green flex items-center justify-center flex-shrink-0">
                  <svg class="w-5 h-5 text-ink-black" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                </div>
                <span class="font-semibold text-sm">Competitive interest rates</span>
              </li>
              <li class="flex items-center gap-3">
                <div class="w-8 h-8 bg-watch-green flex items-center justify-center flex-shrink-0">
                  <svg class="w-5 h-5 text-ink-black" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path></svg>
                </div>
                <span class="font-semibold text-sm">AI-verified &amp; CBK licensed</span>
              </li>
            </ul>
          </div>

          <!-- Encryption Badge -->
          <div class="mt-6 p-4 border-2 border-ink-black bg-vapor-grey flex items-center gap-3">
            <svg class="w-5 h-5 text-ink-black" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"></path></svg>
            <span class="text-[10px] font-black uppercase tracking-widest">256-Bit Encrypted Submission</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter, RouterLink } from 'vue-router'
import { call, auth } from '../api'

const router = useRouter()
const amount = ref(5000)
const tenure = ref(1)
const purpose = ref('')
const loading = ref(false)
const currentStep = ref(1)
const termsAccepted = ref(false)
const errorMessage = ref('')
const currentUser = ref(null)

const tenureOptions = [
  { label: '1 Month', value: 1 },
  { label: '3 Months', value: 3 },
  { label: '6 Months', value: 6 }
]

const handleSubmit = async () => {
  if (currentStep.value === 1) {
    if (!amount.value || !tenure.value || !purpose.value) {
      errorMessage.value = "Please fill all details"
      return
    }
    errorMessage.value = ""
    currentStep.value = 2
  } else {
    if (!termsAccepted.value) {
      errorMessage.value = "Please accept terms"
      return
    }
    await submitApplication()
  }
}

const submitApplication = async () => {
  if (!currentUser.value) {
    errorMessage.value = "User session expired. Please refresh or login again."
    return
  }

  loading.value = true
  errorMessage.value = ''

  try {
    const payload = {
      customer_id: currentUser.value.customer_id,
      amount: amount.value,
      tenure: tenure.value,
      purpose: purpose.value,
      consent_data: {
        ip_address: '127.0.0.1',
        policy_version: '1.0'
      }
    }

    const res = await call.post('dcp_management.api.apply_for_loan', payload)

    if (res.message.status === 'Submitted') {
      alert('Application Submitted Successfully!')
      router.push('/')
    }
  } catch (e) {
    console.error(e)
    errorMessage.value = e.message || 'Submission failed'
  } finally {
    loading.value = false
  }
}

onMounted(async () => {
  try {
    const user = await auth.getLoggedInUser()
    if (user && user !== 'Guest') {
      const res = await call.get('dcp_management.api.get_current_user_customer');

      if (res && res.customer) {
        currentUser.value = { ...user, customer_id: res.customer.name }
      } else if (res?.message?.customer) {
        currentUser.value = { ...user, customer_id: res.message.customer.name }
      } else {
        errorMessage.value = res?.error || res?.message?.error || "Customer record not found"
      }
    }
  } catch (e) {
    console.error("Failed to load customer data", e)
    errorMessage.value = "Failed to load your profile. Please refresh the page."
  }
})
</script>
