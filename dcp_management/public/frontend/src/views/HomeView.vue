<template>
  <div class="min-h-screen bg-gradient-to-br from-blue-50 to-green-50">
    <!-- Hero Section -->
    <section class="relative overflow-hidden">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20">
        <div class="text-center">
          <h1 class="text-5xl md:text-6xl font-extrabold text-gray-900 mb-6 fade-in-up">
            Fast, Fair &
            <span class="block text-green-600 mt-2">Reliable Loans</span>
          </h1>
          <p class="text-xl text-gray-600 mb-8 max-w-2xl mx-auto fade-in-up delay-100">
            Empowering employees and residents with instant access to credit. 
            From KES 1,000 to KES 100,000. 100% online. No paperwork.
          </p>
          <div class="flex flex-col sm:flex-row gap-4 justify-center fade-in-up delay-200">
            <RouterLink to="/onboard" 
              class="bg-green-600 text-white px-8 py-4 rounded-lg font-semibold text-lg hover:bg-green-700 transition shadow-lg hover:shadow-xl">
              Get Started Now
            </RouterLink>
            <RouterLink to="/login" 
              class="bg-white text-green-600 px-8 py-4 rounded-lg font-semibold text-lg hover:bg-gray-50 transition border-2 border-green-600">
              Client Login
            </RouterLink>
          </div>
        </div>
      </div>
    </section>

    <!-- Features Section -->
    <section class="py-16 bg-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 class="text-3xl font-bold text-center text-gray-900 mb-12">Why Choose Jirani Credit?</h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div class="text-center p-6">
            <div class="w-16 h-16 bg-green-100 rounded-full flex items-center justify-center mx-auto mb-4">
              <svg class="w-8 h-8 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path>
              </svg>
            </div>
            <h3 class="text-xl font-semibold mb-2">Instant Approval</h3>
            <p class="text-gray-600">Get loan decisions in minutes, not days. Our automated system works 24/7.</p>
          </div>
          
          <div class="text-center p-6">
            <div class="w-16 h-16 bg-blue-100 rounded-full flex items-center justify-center mx-auto mb-4">
              <svg class="w-8 h-8 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"></path>
              </svg>
            </div>
            <h3 class="text-xl font-semibold mb-2">Safe & Secure</h3>
            <p class="text-gray-600">CBK licensed and compliant. Your data is encrypted and protected.</p>
          </div>
          
          <div class="text-center p-6">
            <div class="w-16 h-16 bg-purple-100 rounded-full flex items-center justify-center mx-auto mb-4">
              <svg class="w-8 h-8 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
              </svg>
            </div>
            <h3 class="text-xl font-semibold mb-2">Flexible Repayment</h3>
            <p class="text-gray-600">Choose your repayment plan. Pay via M-Pesa, bank transfer, or direct debit.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- How It Works -->
    <section class="py-16 bg-gray-50">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 class="text-3xl font-bold text-center text-gray-900 mb-12">How It Works</h2>
        <div class="grid grid-cols-1 md:grid-cols-4 gap-8">
          <div class="text-center">
            <div class="w-12 h-12 bg-green-600 text-white rounded-full flex items-center justify-center mx-auto mb-4 text-xl font-bold">1</div>
            <h4 class="font-semibold mb-2">Sign Up</h4>
            <p class="text-sm text-gray-600">Create your account in 2 minutes</p>
          </div>
          <div class="text-center">
            <div class="w-12 h-12 bg-green-600 text-white rounded-full flex items-center justify-center mx-auto mb-4 text-xl font-bold">2</div>
            <h4 class="font-semibold mb-2">Verify KYC</h4>
            <p class="text-sm text-gray-600">Upload your National ID</p>
          </div>
          <div class="text-center">
            <div class="w-12 h-12 bg-green-600 text-white rounded-full flex items-center justify-center mx-auto mb-4 text-xl font-bold">3</div>
            <h4 class="font-semibold mb-2">Apply</h4>
            <p class="text-sm text-gray-600">Choose amount & tenure</p>
          </div>
          <div class="text-center">
            <div class="w-12 h-12 bg-green-600 text-white rounded-full flex items-center justify-center mx-auto mb-4 text-xl font-bold">4</div>
            <h4 class="font-semibold mb-2">Get Funded</h4>
            <p class="text-sm text-gray-600">Money in your M-Pesa instantly</p>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA Section -->
    <section class="py-16 bg-green-600 text-white">
      <div class="max-w-4xl mx-auto text-center px-4">
        <h2 class="text-3xl md:text-4xl font-bold mb-4">Ready to Get Started?</h2>
        <p class="text-xl mb-8 opacity-90">Join thousands of Kenyans who trust us for their financial needs</p>
        <RouterLink to="/onboard" 
          class="inline-block bg-white text-green-600 px-8 py-4 rounded-lg font-semibold text-lg hover:bg-gray-100 transition shadow-lg">
          Create Free Account
        </RouterLink>
      </div>
    </section>

    <!-- Footer -->
    <footer class="bg-gray-900 text-gray-400 py-8">
      <div class="max-w-7xl mx-auto px-4 text-center">
        <p class="text-sm">&copy; 2026 Jirani Credit. Licensed by Central Bank of Kenya.</p>
        <p class="text-xs mt-2">Terms & Conditions | Privacy Policy | Contact Support</p>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { RouterLink, useRouter } from 'vue-router'
import { api } from '@/api'

const router = useRouter()

onMounted(async () => {
  // Check if user is logged in and needs to complete KYC
  try {
    const res = await api.get('/api/method/dcp_management.api.get_current_user_customer')
    
    if (res.message && res.message.customer) {
      const customer = res.message.customer
      
      // If user has incomplete KYC, redirect to KYC page
      if (customer.kyc_status === 'Incomplete') {
        router.push({ name: 'kyc', query: { new_user: 1 } })
      } else {
        // If KYC is complete, redirect to dashboard
        router.push({ name: 'dashboard' })
      }
    }
  } catch (error) {
    // User not logged in or error - stay on home page
    console.log('User not authenticated or no customer record')
  }
})
</script>
