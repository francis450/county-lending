<template>
  <div class="min-h-screen bg-gradient-to-br from-blue-50 to-green-50 p-4 py-12">
    <div class="max-w-4xl mx-auto">
      <!-- Header -->
      <div class="mb-8">
        <RouterLink to="/" class="text-green-600 hover:text-green-700 flex items-center mb-4">
          <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path>
          </svg>
          Back to Home
        </RouterLink>
        <h1 class="text-4xl font-bold text-gray-900">Apply for a Loan</h1>
        <p class="text-gray-600 mt-2">Complete your application in minutes</p>
      </div>

       <!-- Steps Indicator -->
      <div class="flex justify-between items-center mb-8 px-8 max-w-2xl mx-auto">
        <div :class="['h-2 flex-1 rounded-l-full', currentStep >= 1 ? 'bg-green-500' : 'bg-gray-200']"></div>
        <div :class="['h-2 flex-1 rounded-r-full', currentStep >= 2 ? 'bg-green-500' : 'bg-gray-200']"></div>
      </div>

      <div class="grid md:grid-cols-2 gap-8">
        <!-- Application Form -->
        <div class="bg-white rounded-2xl shadow-xl p-8">
          <h2 class="text-2xl font-bold mb-6">Loan Details</h2>
          
           <!-- Error Message -->
            <div v-if="errorMessage" class="bg-red-50 border border-red-200 text-red-800 px-4 py-3 rounded-lg mb-6">
            <p class="text-sm">{{ errorMessage }}</p>
            </div>

          <form @submit.prevent="handleSubmit" class="space-y-6">
            
            <div v-if="currentStep === 1">
                <!-- Loan Amount -->
                <div class="mb-6">
                <label class="block text-sm font-medium text-gray-700 mb-2">
                    How much do you need?
                </label>
                <div class="relative">
                    <span class="absolute left-4 top-3.5 text-gray-500 font-medium">KES</span>
                    <input 
                    v-model.number="amount" 
                    type="number" 
                    min="1000"
                    max="100000"
                    step="1000"
                    class="w-full pl-16 pr-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-green-500 focus:border-transparent text-lg font-semibold"
                    required 
                    />
                </div>
                <input 
                    v-model.number="amount" 
                    type="range" 
                    min="1000" 
                    max="100000" 
                    step="1000"
                    class="w-full mt-3"
                >
                <div class="flex justify-between text-xs text-gray-500 mt-1">
                    <span>KES 1,000</span>
                    <span>KES 100,000</span>
                </div>
                </div>

                <!-- Tenure -->
                <div class="mb-6">
                <label class="block text-sm font-medium text-gray-700 mb-2">
                    Repayment Period
                </label>
                <div class="grid grid-cols-3 gap-3">
                    <button 
                    v-for="option in tenureOptions" 
                    :key="option.value"
                    type="button"
                    @click="tenure = option.value"
                    :class="[
                        'py-3 px-4 rounded-lg border-2 font-medium transition',
                        tenure === option.value 
                        ? 'border-green-600 bg-green-50 text-green-700' 
                        : 'border-gray-200 hover:border-gray-300'
                    ]">
                    {{ option.label }}
                    </button>
                </div>
                </div>

                <!-- Loan Purpose -->
                <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">
                    Loan Purpose
                </label>
                <select 
                    v-model="purpose"
                    class="w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-green-500 focus:border-transparent" required>
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
                <h3 class="font-semibold text-lg mb-4">Review Application</h3>
                <div class="bg-gray-50 p-4 rounded-lg space-y-3 mb-6">
                    <div class="flex justify-between">
                        <span class="text-gray-600">Amount:</span>
                        <span class="font-bold">KES {{ amount.toLocaleString() }}</span>
                    </div>
                    <div class="flex justify-between">
                        <span class="text-gray-600">Period:</span>
                        <span class="font-bold">{{ tenure }} Months</span>
                    </div>
                    <div class="flex justify-between">
                        <span class="text-gray-600">Purpose:</span>
                        <span class="font-bold capitalize">{{ purpose }}</span>
                    </div>
                </div>
                
                <div class="flex items-start">
                    <input type="checkbox" v-model="termsAccepted" id="terms" class="mt-1 mr-2" required>
                    <label for="terms" class="text-sm text-gray-600">
                        I agree to the Terms and Conditions and checking of my credit status with CRB.
                    </label>
                </div>
            </div>

            <!-- Navigation -->
             <div class="pt-4 flex gap-4">
                 <button 
                  v-if="currentStep === 2"
                  type="button" 
                  @click="currentStep = 1"
                  class="flex-1 bg-gray-100 text-gray-700 font-semibold py-4 px-4 rounded-lg hover:bg-gray-200 transition">
                  Back
                 </button>

                <button 
                type="submit" 
                :disabled="loading"
                class="flex-1 bg-green-600 text-white font-semibold py-4 px-4 rounded-lg hover:bg-green-700 disabled:opacity-50 transition transform hover:scale-[1.02] active:scale-[0.98]">
                <span v-if="loading">Processing...</span>
                <span v-else>{{ currentStep === 1 ? 'Continue →' : 'Submit Application' }}</span>
                </button>
            </div>
          </form>
        </div>

        <!-- Info/Stats Column (Simplified from original) -->
        <div class="hidden md:block">
             <div class="bg-green-900 text-white rounded-2xl p-8 mb-8">
            <h3 class="text-xl font-bold mb-4">Why County Lending?</h3>
            <ul class="space-y-4">
              <li class="flex items-center">
                <svg class="w-6 h-6 mr-3 text-green-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
                <span>Instant approval & disbursement</span>
              </li>
              <li class="flex items-center">
                <svg class="w-6 h-6 mr-3 text-green-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                <span>Competitive interest rates</span>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue'
import { useRouter } from 'vue-router'
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
      customer_id: currentUser.value.customer_id, // We need to fetch this
      amount: amount.value,
      tenure: tenure.value,
      purpose: purpose.value,
      consent_data: {
        ip_address: '127.0.0.1', // Mock
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
  // Auth is already checked by router guard, just get user data
  try {
    const user = await auth.getLoggedInUser()
    if (user && user !== 'Guest') {
        // Get customer record using whitelisted API
        const res = await call.get('dcp_management.api.get_current_user_customer');
        
        // DEBUG: Log the response structure
        console.log('=== Loan Application API Response Debug ===');
        console.log('Full response:', res);
        console.log('res.customer:', res?.customer);
        console.log('res.message:', res?.message);
        console.log('res.message?.customer:', res?.message?.customer);
        console.log('==============================');
        
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
