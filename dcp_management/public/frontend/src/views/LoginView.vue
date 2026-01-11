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

      <!-- Login Card -->
      <div class="bg-white rounded-2xl shadow-xl p-8">
        <div class="text-center mb-8">
          <h1 class="text-3xl font-bold text-gray-900 mb-2">Welcome Back</h1>
          <p class="text-gray-600">Sign in to your account</p>
        </div>

        <!-- Error Message -->
        <div v-if="errorMessage" class="bg-red-50 border border-red-200 text-red-800 px-4 py-3 rounded-lg mb-6">
          <p class="text-sm">{{ errorMessage }}</p>
        </div>

        <form @submit.prevent="submitLogin" class="space-y-5">
          <!-- Email -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">Email Address</label>
            <input 
              v-model="form.email" 
              type="email" 
              placeholder="john@example.com"
              class="w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-green-500 focus:border-transparent transition"
              required
            >
          </div>

          <!-- Password -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">Password</label>
            <input 
              v-model="form.password" 
              type="password" 
              placeholder="••••••••"
              class="w-full px-4 py-3 rounded-lg border border-gray-300 focus:ring-2 focus:ring-green-500 focus:border-transparent transition"
              required
            >
          </div>

          <!-- Forgot Password -->
          <div class="flex justify-end">
             <a href="/update-password" class="text-sm text-green-600 hover:underline">Forgot password?</a>
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
              Signing In...
            </span>
            <span v-else>Sign In</span>
          </button>
        </form>

        <div class="mt-6 text-center text-sm text-gray-600">
          Don't have an account? 
          <RouterLink to="/onboard" class="font-medium text-green-600 hover:text-green-500">
            Create one today
          </RouterLink>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive, ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { auth, call } from '../api'

const router = useRouter()
const loading = ref(false)
const errorMessage = ref('')

const form = reactive({
  email: '',
  password: ''
})

const checkUserAndRedirect = async (user) => {
    try {
        // Check User doctype to determine type
        const userDoc = await call.get('frappe.client.get_value', {
            doctype: 'User',
            filters: { name: user },
            fieldname: 'user_type'
        })

        if (userDoc.message && userDoc.message.user_type === 'System User') {
            window.location.href = '/app'
            return
        }
        router.push('/dashboard')
    } catch (e) {
        console.error("Role check failed", e)
        router.push('/dashboard')
    }
}

onMounted(async () => {
    try {
        const user = await auth.getLoggedInUser()
        if (user && user !== "Guest") {
            await checkUserAndRedirect(user)
        }
    } catch (e) {
        console.log("Not logged in")
    }
})

const submitLogin = async () => {
  loading.value = true
  errorMessage.value = ''

  try {
    const res = await auth.loginWithUsernamePassword({
        username: form.email,
        password: form.password
    })
    
    // "Logged In" = System User with Desk access
    // "No App" = Website User (Customer) without Desk access
    if (res.message === 'Logged In' || res.message === 'No App') {
        // Check if backend provided a home_page in the response
        if (res.home_page) {
            // Extract hash route from home_page (e.g., "/portal#/kyc" -> "/kyc")
            const hashRoute = res.home_page.split('#')[1]
            if (hashRoute) {
                router.push(hashRoute)
                return
            }
        }
        
        const user = await auth.getLoggedInUser()
        if (user) {
            await checkUserAndRedirect(user)
        } else {
            router.push('/dashboard')
        }
    } else {
        // Double check user session
        try {
            const user = await auth.getLoggedUser()
            if (user && user !== 'Guest') {
                 router.push('/dashboard')
            } else {
                throw new Error("Login failed")
            }
        } catch (e) {
            errorMessage.value = "Invalid email or password"
        }
    }
    
  } catch (error) {
    console.error(error)
    errorMessage.value = "Invalid email or password"
  } finally {
    loading.value = false
  }
}
</script>
