<template>
  <div class="min-h-screen bg-gradient-to-br from-blue-50 to-green-50 flex items-center justify-center p-4">
    <div class="max-w-md w-full">
      <!-- Back Link -->
      <RouterLink to="/" class="text-green-600 hover:text-green-700 flex items-center mb-6">
        <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path>
        </svg>
        Back to Home
      </RouterLink>

      <!-- Signup Card -->
      <div class="bg-white rounded-2xl shadow-xl p-8">
        <div class="text-center mb-8">
          <h1 class="text-3xl font-bold text-gray-900 mb-2">Create Your Account</h1>
          <p class="text-gray-600">Get started in less than 2 minutes</p>
        </div>

        <!-- Success Message -->
        <div v-if="showSuccess" class="bg-green-50 border border-green-200 text-green-800 px-4 py-3 rounded-lg mb-6">
          <p class="font-medium">✓ Account created successfully!</p>
          <p class="text-sm mt-1">Redirecting to email verification...</p>
        </div>

        <!-- Error Message -->
        <div v-if="errorMessage" class="bg-red-50 border border-red-200 text-red-800 px-4 py-3 rounded-lg mb-6">
          <p class="text-sm">{{ errorMessage }}</p>
        </div>

        <form @submit.prevent="submitSignup" class="space-y-5">
          <!-- Full Name -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">Full Name *</label>
            <input 
              v-model="form.full_name" 
              type="text" 
              placeholder="John Doe"
              class="w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-green-500 focus:border-transparent transition"
              required
            >
          </div>

          <!-- Email -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">Email Address *</label>
            <input 
              v-model="form.email" 
              type="email" 
              placeholder="john@example.com"
              class="w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-green-500 focus:border-transparent transition"
              required
            >
          </div>

          <!-- Phone -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">Phone Number *</label>
            <div class="flex">
              <span class="inline-flex items-center px-3 rounded-l-lg border border-r-0 border-gray-300 bg-gray-50 text-gray-600">
                +254
              </span>
              <input 
                v-model="form.phone" 
                type="tel" 
                placeholder="712345678"
                pattern="[0-9]{9}"
                maxlength="9"
                class="w-full px-4 py-3 rounded-r-lg border border-gray-300 focus:ring-2 focus:ring-green-500 focus:border-transparent transition"
                required
              >
            </div>
            <p class="text-xs text-gray-500 mt-1">Enter your M-Pesa number without the leading zero</p>
          </div>

          <!-- Terms & Conditions -->
          <div class="flex items-start">
            <input 
              v-model="form.agree_terms" 
              type="checkbox" 
              id="terms" 
              class="mt-1 h-4 w-4 text-green-600 focus:ring-green-500 border-gray-300 rounded"
              required
            >
            <label for="terms" class="ml-2 text-sm text-gray-600">
              I agree to the <a href="#" class="text-green-600 hover:underline">Terms & Conditions</a> and <a href="#" class="text-green-600 hover:underline">Privacy Policy</a>
            </label>
          </div>

          <!-- Submit Button -->
          <button 
            type="submit" 
            :disabled="loading"
            class="w-full bg-green-600 text-white font-semibold py-3 px-4 rounded-lg hover:bg-green-700 disabled:opacity-50 disabled:cursor-not-allowed transition transform hover:scale-[1.02] active:scale-[0.98]">
            <span v-if="loading" class="flex items-center justify-center">
              <svg class="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
              Creating Account...
            </span>
            <span v-else>Create Account</span>
          </button>
        </form>

        <!-- KYC Notice -->
        <div class="mt-6 p-4 bg-blue-50 rounded-lg">
          <p class="text-sm text-blue-800">
            <strong>Next Step:</strong> After signup, you'll be redirected to complete your KYC verification 
            (National ID, KRA PIN & Photo) as required by the Central Bank of Kenya.
          </p>
        </div>

        <!-- Login Link -->
        <p class="mt-6 text-center text-sm text-gray-600">
          Already have an account? 
          <RouterLink to="/login" class="text-green-600 font-medium hover:underline">Sign In</RouterLink>
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'
import { api } from '@/api'
import { useRouter, RouterLink } from 'vue-router'

const router = useRouter()
const loading = ref(false)
const showSuccess = ref(false)
const errorMessage = ref('')

const form = reactive({
  full_name: '',
  email: '',
  phone: '',
  agree_terms: false
})

const submitSignup = async () => {
  loading.value = true
  errorMessage.value = ''
  
  try {
    // Split full name into first and last
    const nameParts = form.full_name.trim().split(' ')
    const first_name = nameParts[0] || ''
    const last_name = nameParts.slice(1).join(' ') || nameParts[0]

    const res = await api.post('/api/method/dcp_management.api.onboard_customer', {
      data: {
        first_name,
        last_name,
        email: form.email,
        phone: '+254' + form.phone
      }
    })

    if (res.message && res.message.customer_id) {
      showSuccess.value = true
      
      // Store customer data in localStorage (will be retrieved after password reset)
      localStorage.setItem('dcp_customer_id', res.message.customer_id)
      localStorage.setItem('pending_kyc_email', form.email)
      
      // Redirect to check email page after 2 seconds
      setTimeout(() => {
        router.push({ name: 'check-email', query: { email: form.email } })
      }, 2000)
    } else if (res.error) {
      throw new Error(res.error)
    } else {
      throw new Error('Registration failed')
    }
  } catch (error) {
    console.error(error)
    errorMessage.value = error.message || 'Failed to create account. Please try again.'
  } finally {
    loading.value = false
  }
}
</script>
