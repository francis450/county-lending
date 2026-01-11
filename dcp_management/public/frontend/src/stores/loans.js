import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { api } from '@/api'

export const useLoanStore = defineStore('loans', () => {
  // State
  const loans = ref([])
  const activeLoan = ref(null)
  const loanHistory = ref([])
  const loading = ref(false)
  const error = ref(null)

  // Computed
  const hasActiveLoan = computed(() => !!activeLoan.value)
  const totalBorrowed = computed(() => {
    return loans.value.reduce((sum, loan) => sum + (loan.loan_amount || 0), 0)
  })
  const totalRepaid = computed(() => {
    return loans.value.reduce((sum, loan) => sum + (loan.total_payment || 0), 0)
  })
  const totalOutstanding = computed(() => {
    return loans.value
      .filter(loan => loan.status === 'Active' || loan.status === 'Disbursed')
      .reduce((sum, loan) => sum + (loan.total_payable || 0) - (loan.total_payment || 0), 0)
  })
  const pendingApplications = computed(() => {
    return loans.value.filter(loan => loan.status === 'Pending' || loan.status === 'Open')
  })

  // Actions
  async function fetchLoans(customerId) {
    loading.value = true
    error.value = null
    try {
      const res = await api.post('/api/method/dcp_management.api.get_customer_loans', {
        customer_id: customerId
      })
      
      if (res.message) {
        loans.value = res.message.loans || []
        activeLoan.value = res.message.active_loan || null
        loanHistory.value = res.message.history || []
      }
    } catch (err) {
      error.value = err.message
      console.error('Failed to fetch loans:', err)
    } finally {
      loading.value = false
    }
  }

  async function applyForLoan(data) {
    loading.value = true
    error.value = null
    try {
      const res = await api.post('/api/method/dcp_management.api.apply_for_loan', data)
      return res
    } catch (err) {
      error.value = err.message
      throw err
    } finally {
      loading.value = false
    }
  }

  async function makePayment(loanId, amount) {
    loading.value = true
    error.value = null
    try {
      const res = await api.post('/api/method/dcp_management.api.make_payment', {
        loan_id: loanId,
        amount
      })
      return res
    } catch (err) {
      error.value = err.message
      throw err
    } finally {
      loading.value = false
    }
  }

  function clearLoans() {
    loans.value = []
    activeLoan.value = null
    loanHistory.value = []
    error.value = null
  }

  return {
    loans,
    activeLoan,
    loanHistory,
    loading,
    error,
    hasActiveLoan,
    totalBorrowed,
    totalRepaid,
    totalOutstanding,
    pendingApplications,
    fetchLoans,
    applyForLoan,
    makePayment,
    clearLoans
  }
})
