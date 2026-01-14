<template>
  <div class="min-h-screen bg-gray-50">
    <!-- Skip navigation for routes that don't need it -->
    <header v-if="!isFullPageRoute" class="bg-white shadow-sm sticky top-0 z-50">
      <nav class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between items-center h-16">
          <!-- Logo -->
          <RouterLink to="/" class="flex items-center">
            <span class="text-2xl font-bold text-green-600">County</span>
            <span class="text-gray-700 ml-2 hidden sm:inline">Lending</span>
          </RouterLink>

          <!-- Desktop Navigation -->
          <div class="hidden md:flex items-center space-x-8">
            <template v-if="showNavLinks">
              <RouterLink to="/" class="text-gray-700 hover:text-green-600 font-medium transition">
                Home
              </RouterLink>
              <RouterLink to="/dashboard" class="text-gray-700 hover:text-green-600 font-medium transition">
                Dashboard
              </RouterLink>
                <RouterLink v-if="!customerStore.isLoggedIn" to="/apply" class="text-gray-700 hover:text-green-600 font-medium transition">
                Apply
                </RouterLink>
              <RouterLink to="/about" class="text-gray-700 hover:text-green-600 font-medium transition">
                About
              </RouterLink>
            </template>

            <button v-if="customerStore.isLoggedIn" @click="handleLogout" 
              class="text-gray-700 hover:text-green-600 font-medium transition">
              <svg class="w-5 h-5 inline mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"></path>
            </svg>
              Logout
            </button>
            <RouterLink v-else to="/onboard" 
              class="bg-green-600 text-white px-6 py-2 rounded-lg font-medium hover:bg-green-700 transition">
              Get Started
            </RouterLink>
          </div>

          <!-- Mobile Menu Button -->
          <button @click="mobileMenuOpen = !mobileMenuOpen" class="md:hidden p-2">
            <svg class="w-6 h-6 text-gray-700" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
            </svg>
          </button>
        </div>

        <!-- Mobile Menu -->
        <div v-if="mobileMenuOpen" class="md:hidden py-4 border-t">
          <div class="flex flex-col space-y-3">
            <template v-if="showNavLinks">
              <RouterLink @click="mobileMenuOpen = false" to="/" class="text-gray-700 hover:text-green-600 font-medium py-2">
                Home
              </RouterLink>
              <RouterLink @click="mobileMenuOpen = false" to="/dashboard" class="text-gray-700 hover:text-green-600 font-medium py-2">
                Dashboard
              </RouterLink>
              <RouterLink @click="mobileMenuOpen = false" to="/apply" class="text-gray-700 hover:text-green-600 font-medium py-2">
                Apply for Loan
              </RouterLink>
              <RouterLink @click="mobileMenuOpen = false" to="/about" class="text-gray-700 hover:text-green-600 font-medium py-2">
                About
              </RouterLink>
            </template>
            
            <button v-if="customerStore.isLoggedIn" @click="handleLogout(); mobileMenuOpen = false" 
              class="text-left text-gray-700 hover:text-green-600 font-medium py-2">
              Logout
            </button>
            <RouterLink v-else @click="mobileMenuOpen = false" to="/onboard" 
              class="bg-green-600 text-white px-6 py-2 rounded-lg font-medium text-center">
              Get Started
            </RouterLink>
          </div>
        </div>
      </nav>
    </header>

    <!-- Main Content -->
    <RouterView />
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { RouterLink, RouterView, useRoute, useRouter } from 'vue-router'
import { useCustomerStore } from './stores/customer'

const mobileMenuOpen = ref(false)
const route = useRoute()
const router = useRouter()
const customerStore = useCustomerStore()

// Hide navigation on certain full-page routes
const isFullPageRoute = computed(() => {
  return route.path === '/' || route.path === '/onboard'
})

const showNavLinks = computed(() => route.path !== '/dashboard')

const handleLogout = async () => {
  if (customerStore.logout) {
    await customerStore.logout()
  }
  router.push('/onboard')
}
</script>

<style scoped>
/* Add smooth transitions for route changes */
.router-link-active {
  color: #16a34a;
}
</style>
