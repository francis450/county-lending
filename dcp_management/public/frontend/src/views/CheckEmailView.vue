<template>
  <div class="min-h-screen bg-gradient-to-br from-blue-50 to-green-50 flex items-center justify-center p-4">
    <div class="max-w-md w-full">
      <!-- Success Card -->
      <div class="bg-white rounded-2xl shadow-xl p-8">
        <!-- Email Icon -->
        <div class="w-20 h-20 bg-green-100 rounded-full flex items-center justify-center mx-auto mb-6">
          <svg class="w-10 h-10 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path>
          </svg>
        </div>

        <div class="text-center">
          <h1 class="text-3xl font-bold text-gray-900 mb-3">Check Your Email</h1>
          <p class="text-gray-600 mb-6">
            We've sent a password setup link to <strong class="text-gray-900">{{ email }}</strong>
          </p>

          <div class="bg-blue-50 border border-blue-200 rounded-lg p-4 mb-6 text-left">
            <p class="text-sm text-blue-800 mb-3">
              <strong>Next Steps:</strong>
            </p>
            <ol class="text-sm text-blue-800 space-y-2 ml-4 list-decimal">
              <li>Check your email inbox (and spam folder)</li>
              <li>Click the "Set Password" link in the email</li>
              <li>Create a secure password for your account</li>
              <li>After setting password, navigate to <strong>/portal</strong> to access your account</li>
              <li>You'll be automatically redirected to complete your KYC verification</li>
            </ol>
          </div>

          <!-- Security Notice -->
          <div class="bg-yellow-50 border border-yellow-200 rounded-lg p-4 mb-6">
            <div class="flex items-start">
              <svg class="w-5 h-5 text-yellow-600 mr-2 mt-0.5" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M8.257 3.099c.765-1.36 2.722-1.36 3.486 0l5.58 9.92c.75 1.334-.213 2.98-1.742 2.98H4.42c-1.53 0-2.493-1.646-1.743-2.98l5.58-9.92zM11 13a1 1 0 11-2 0 1 1 0 012 0zm-1-8a1 1 0 00-1 1v3a1 1 0 002 0V6a1 1 0 00-1-1z" clip-rule="evenodd"></path>
              </svg>
              <p class="text-sm text-yellow-800">
                <strong>Important:</strong> The link will expire in 24 hours. You won't be able to access your account until you set a password.
              </p>
            </div>
          </div>

          <!-- Resend Email Button -->
          <button 
            v-if="showResend"
            @click="resendEmail"
            :disabled="resendLoading"
            class="w-full mb-4 bg-green-600 text-white font-semibold py-3 px-4 rounded-lg hover:bg-green-700 disabled:opacity-50 disabled:cursor-not-allowed transition">
            <span v-if="resendLoading">Sending...</span>
            <span v-else>Resend Email</span>
          </button>

          <!-- Countdown Timer -->
          <p v-if="!showResend" class="text-sm text-gray-500 mb-4">
            Didn't receive the email? You can resend it in {{ countdown }} seconds
          </p>

          <!-- Success Message -->
          <div v-if="resendSuccess" class="bg-green-50 border border-green-200 text-green-800 px-4 py-2 rounded-lg mb-4 text-sm">
            ✓ Email sent successfully!
          </div>

          <!-- Support Link -->
          <p class="text-sm text-gray-600">
            Need help? <a href="/portal#/about" class="text-green-600 hover:underline">Contact Support</a>
          </p>
        </div>
      </div>

      <!-- Back to Home -->
      <div class="text-center mt-6">
        <RouterLink to="/" class="text-gray-600 hover:text-gray-900 text-sm">
          ← Back to Home
        </RouterLink>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { RouterLink, useRoute } from 'vue-router'
import { api } from '@/api'

const route = useRoute()
const email = ref(route.query.email || 'your email')
const countdown = ref(60)
const showResend = ref(false)
const resendLoading = ref(false)
const resendSuccess = ref(false)

onMounted(() => {
  // Start countdown timer
  const timer = setInterval(() => {
    countdown.value--
    if (countdown.value <= 0) {
      showResend.value = true
      clearInterval(timer)
    }
  }, 1000)
})

const resendEmail = async () => {
  resendLoading.value = true
  resendSuccess.value = false
  
  try {
    // Call API to resend password reset email
    await api.post('/api/method/frappe.core.doctype.user.user.reset_password', {
      user: email.value
    })
    
    resendSuccess.value = true
    showResend.value = false
    countdown.value = 60
    
    // Restart countdown
    setTimeout(() => {
      resendSuccess.value = false
      const timer = setInterval(() => {
        countdown.value--
        if (countdown.value <= 0) {
          showResend.value = true
          clearInterval(timer)
        }
      }, 1000)
    }, 2000)
    
  } catch (error) {
    console.error('Resend failed:', error)
    alert('Failed to resend email. Please try again.')
  } finally {
    resendLoading.value = false
  }
}
</script>
