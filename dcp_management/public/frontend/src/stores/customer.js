import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { api } from '@/api'

export const useCustomerStore = defineStore('customer', () => {
  // State
  const customer = ref(null)
  const loading = ref(false)
  const error = ref(null)

  // Computed
  const isLoggedIn = computed(() => !!customer.value)
  const fullName = computed(() => {
    if (!customer.value) return ''
    return `${customer.value.first_name} ${customer.value.last_name}`
  })
  const initials = computed(() => {
    if (!customer.value) return ''
    return `${customer.value.first_name?.[0] || ''}${customer.value.last_name?.[0] || ''}`
  })

  // Actions
  async function fetchCustomer(customerId) {
    loading.value = true
    error.value = null
    try {
      const res = await api.get(`/api/resource/DCP Customer/${customerId}`)
      if (res.data) {
        customer.value = res.data
      }
    } catch (err) {
      error.value = err.message
      console.error('Failed to fetch customer:', err)
    } finally {
      loading.value = false
    }
  }

  async function fetchCurrentUser() {
    loading.value = true
    error.value = null
    try {
      const res = await api.get('/api/method/dcp_management.api.get_current_user_customer')
      if (res.message && res.message.customer) {
        customer.value = res.message.customer
      }
    } catch (err) {
      error.value = err.message
      console.error('Failed to fetch current user:', err)
    } finally {
      loading.value = false
    }
  }

  async function updateCustomer(data) {
    loading.value = true
    error.value = null
    try {
      const res = await api.post(`/api/method/dcp_management.api.update_customer`, {
        customer_id: customer.value.name,
        data
      })
      if (res.message) {
        customer.value = { ...customer.value, ...data }
      }
      return res
    } catch (err) {
      error.value = err.message
      throw err
    } finally {
      loading.value = false
    }
  }

  function setCustomer(data) {
    customer.value = data
  }

  function logout() {
    customer.value = null
    error.value = null
  }

  return {
    customer,
    loading,
    error,
    isLoggedIn,
    fullName,
    initials,
    fetchCustomer,
    fetchCurrentUser,
    updateCustomer,
    setCustomer,
    logout
  }
})
