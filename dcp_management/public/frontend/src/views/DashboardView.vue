<template>
  <div class="min-h-screen bg-gradient-to-br from-blue-50 to-green-50 pb-12">
    <!-- Header -->
    <div class="bg-white shadow-sm border-b">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
        <div class="flex items-center justify-between">
          <div class="flex items-center">
            <div class="w-16 h-16 bg-green-600 text-white rounded-full flex items-center justify-center text-2xl font-bold mr-4">
              {{ customerStore.initials || 'U' }}
            </div>
            <div>
              <h1 class="text-2xl font-bold text-gray-900">
                Welcome back, {{ firstName }}!
              </h1>
              <p class="text-gray-600">{{ customerStore.customer?.email || 'customer@example.com' }}</p>
            </div>
          </div>
          <button 
            @click="handleLogout"
            class="px-4 py-2 text-gray-700 hover:text-red-600 transition">
            <svg class="w-5 h-5 inline mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"></path>
            </svg>
            Logout
          </button>
        </div>
      </div>
    </div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <!-- Loading State -->
      <div v-if="loanStore.loading" class="text-center py-12">
        <div class="inline-block animate-spin rounded-full h-12 w-12 border-4 border-green-500 border-t-transparent"></div>
        <p class="mt-4 text-gray-600">Loading your dashboard...</p>
      </div>

      <!-- Main Content -->
      <div v-else>
        <!-- Stats Overview -->
        <div class="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
          <StatCard 
            label="Total Borrowed"
            :value="loanStore.totalBorrowed"
            :is-currency="true"
            type="info"
          >
            <template #icon>
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
              </svg>
            </template>
          </StatCard>

          <StatCard 
            label="Total Repaid"
            :value="loanStore.totalRepaid"
            :is-currency="true"
            type="success"
          >
            <template #icon>
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
              </svg>
            </template>
          </StatCard>

          <StatCard 
            label="Outstanding"
            :value="loanStore.totalOutstanding"
            :is-currency="true"
            :type="loanStore.totalOutstanding > 0 ? 'warning' : 'default'"
          >
            <template #icon>
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
              </svg>
            </template>
          </StatCard>

          <StatCard 
            label="Active Loans"
            :value="activeLoansCount"
            type="default"
          >
            <template #icon>
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path>
              </svg>
            </template>
          </StatCard>
        </div>

        <!-- Quick Actions -->
        <div class="bg-white rounded-xl shadow-lg border border-gray-200 p-6 mb-8">
          <h2 class="text-xl font-bold text-gray-900 mb-4">Quick Actions</h2>
          <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
            <button 
              @click="router.push('/apply')"
              class="flex items-center p-4 bg-green-50 border-2 border-green-200 rounded-lg hover:bg-green-100 transition group">
              <div class="w-12 h-12 bg-green-600 rounded-full flex items-center justify-center mr-4 group-hover:scale-110 transition">
                <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"></path>
                </svg>
              </div>
              <div class="text-left">
                <p class="font-semibold text-gray-900">Apply for Loan</p>
                <p class="text-sm text-gray-600">Get funds in minutes</p>
              </div>
            </button>

            <button 
              @click="showPaymentModal = true"
              :disabled="!loanStore.hasActiveLoan"
              class="flex items-center p-4 bg-blue-50 border-2 border-blue-200 rounded-lg hover:bg-blue-100 transition group disabled:opacity-50 disabled:cursor-not-allowed">
              <div class="w-12 h-12 bg-blue-600 rounded-full flex items-center justify-center mr-4 group-hover:scale-110 transition">
                <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 9V7a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2m2 4h10a2 2 0 002-2v-6a2 2 0 00-2-2H9a2 2 0 00-2 2v6a2 2 0 002 2zm7-5a2 2 0 11-4 0 2 2 0 014 0z"></path>
                </svg>
              </div>
              <div class="text-left">
                <p class="font-semibold text-gray-900">Make Payment</p>
                <p class="text-sm text-gray-600">Pay via M-Pesa</p>
              </div>
            </button>

            <button 
              @click="router.push('/kyc')"
              class="flex items-center p-4 bg-purple-50 border-2 border-purple-200 rounded-lg hover:bg-purple-100 transition group">
              <div class="w-12 h-12 bg-purple-600 rounded-full flex items-center justify-center mr-4 group-hover:scale-110 transition">
                <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path>
                </svg>
              </div>
              <div class="text-left">
                <p class="font-semibold text-gray-900">Update Profile</p>
                <p class="text-sm text-gray-600">Complete your KYC</p>
              </div>
            </button>
          </div>
        </div>

        <!-- Active Loan -->
        <div v-if="loanStore.activeLoan" class="mb-8">
          <h2 class="text-2xl font-bold text-gray-900 mb-4">Active Loan</h2>
          <LoanCard 
            :loan="loanStore.activeLoan" 
            @pay="handlePayment"
            @view="handleViewLoan"
          />
        </div>

        <!-- Pending Applications -->
        <div v-if="loanStore.pendingApplications.length > 0" class="mb-8">
          <h2 class="text-2xl font-bold text-gray-900 mb-4">Pending Applications</h2>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <LoanCard 
              v-for="loan in loanStore.pendingApplications" 
              :key="loan.name"
              :loan="loan"
              @view="handleViewLoan"
            />
          </div>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
          <!-- Transaction History -->
          <TransactionHistory 
            :transactions="mockTransactions"
            :loading="false"
          />

          <!-- Loan History -->
          <div class="bg-white rounded-xl shadow-lg border border-gray-200 p-6">
            <h3 class="text-lg font-bold text-gray-900 mb-4">Loan History</h3>
            <div v-if="loanStore.loans.length === 0" class="text-center py-8 text-gray-500">
              <svg class="w-12 h-12 mx-auto mb-2 opacity-50" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path>
              </svg>
              <p>No loan history yet</p>
              <RouterLink to="/apply" class="text-green-600 hover:underline mt-2 inline-block">Apply for your first loan</RouterLink>
            </div>
            <div v-else class="space-y-3">
              <div 
                v-for="loan in loanStore.loans.slice(0, 5)" 
                :key="loan.name"
                class="flex items-center justify-between py-3 border-b border-gray-100 last:border-0 cursor-pointer hover:bg-gray-50 rounded px-2 transition"
                @click="handleViewLoan(loan)">
                <div>
                  <p class="font-medium text-gray-900">{{ loan.name }}</p>
                  <p class="text-xs text-gray-500">KES {{ (loan.loan_amount || 0).toLocaleString() }}</p>
                </div>
                <span :class="['px-2 py-1 rounded-full text-xs font-semibold', getLoanStatusClass(loan.status)]">
                  {{ loan.status }}
                </span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter, RouterLink } from 'vue-router'
import { useCustomerStore } from '@/stores/customer'
import { useLoanStore } from '@/stores/loans'
import { auth } from '@/api'
import StatCard from '@/components/StatCard.vue'
import LoanCard from '@/components/LoanCard.vue'
import TransactionHistory from '@/components/TransactionHistory.vue'

const router = useRouter()
const customerStore = useCustomerStore()
const loanStore = useLoanStore()

const showPaymentModal = ref(false)
const showProfileModal = ref(false)

const firstName = computed(() => {
  return customerStore.customer?.first_name || 'Customer'
})

const activeLoansCount = computed(() => {
  return loanStore.loans.filter(l => l.status === 'Active' || l.status === 'Disbursed').length
})

// Mock data for demonstration
const mockTransactions = ref([
  { id: 1, type: 'disbursement', description: 'Loan Disbursement', amount: 10000, date: '2026-01-10', status: 'Completed' },
  { id: 2, type: 'payment', description: 'M-Pesa Payment', amount: 5000, date: '2026-01-08', status: 'Completed' },
  { id: 3, type: 'application', description: 'Loan Application Fee', amount: 100, date: '2026-01-05', status: 'Completed' }
])

onMounted(async () => {
  // For MVP, we'll use mock customer data
  // In production, this would fetch from the backend
  if (!customerStore.customer) {
    customerStore.setCustomer({
      name: 'DCP-CUST-001',
      first_name: 'John',
      last_name: 'Doe',
      email: 'john.doe@example.com',
      phone: '+254712345678',
      status: 'Active'
    })
  }

  // Fetch customer loans
  await loanStore.fetchLoans(customerStore.customer.name)
})

const handlePayment = (loan) => {
  showPaymentModal.value = true
  // TODO: Implement payment modal
  alert(`Payment for loan ${loan.name}\nAmount: KES ${loan.loan_amount}`)
}

const handleViewLoan = (loan) => {
  // TODO: Navigate to loan details page
  alert(`Viewing loan details for ${loan.name}`)
}

const handleLogout = async () => {
  try {
    // Call Frappe logout API
    await auth.logout()
    // Clear local stores
    customerStore.logout()
    loanStore.clearLoans()
    // Redirect to login page
    router.push('/login')
  } catch (error) {
    console.error('Logout failed:', error)
    // Still redirect to login even if API call fails
    customerStore.logout()
    loanStore.clearLoans()
    router.push('/login')
  }
}

const getLoanStatusClass = (status) => {
  if (status === 'Active' || status === 'Disbursed') return 'bg-green-100 text-green-800'
  if (status === 'Pending' || status === 'Open') return 'bg-yellow-100 text-yellow-800'
  if (status === 'Rejected') return 'bg-red-100 text-red-800'
  return 'bg-gray-100 text-gray-800'
}
</script>
