<template>
  <div class="bg-white rounded-xl shadow-lg border border-gray-200 overflow-hidden">
    <div :class="['p-6', statusColorClass]">
      <div class="flex items-start justify-between">
        <div class="flex-1">
          <div class="flex items-center mb-2">
            <span :class="['inline-flex items-center px-3 py-1 rounded-full text-xs font-semibold', statusBadgeClass]">
              {{ loan.status || 'Unknown' }}
            </span>
            <span class="ml-3 text-sm text-gray-600">{{ loan.name }}</span>
          </div>
          <h3 class="text-2xl font-bold text-gray-900 mb-1">
            KES {{ (loan.loan_amount || 0).toLocaleString() }}
          </h3>
          <p class="text-sm text-gray-600">
            Applied on {{ formatDate(loan.creation || loan.posting_date) }}
          </p>
        </div>
        <div class="text-right">
          <p class="text-sm text-gray-600 mb-1">Total Repayment</p>
          <p class="text-xl font-bold text-gray-900">
            KES {{ (loan.total_payable || loan.loan_amount || 0).toLocaleString() }}
          </p>
        </div>
      </div>
    </div>

    <div class="p-6 bg-gray-50">
      <div class="grid grid-cols-2 gap-4 mb-4">
        <div>
          <p class="text-xs text-gray-600 mb-1">Tenure</p>
          <p class="font-semibold">{{ loan.repayment_periods || loan.tenure || 1 }} months</p>
        </div>
        <div>
          <p class="text-xs text-gray-600 mb-1">Interest Rate</p>
          <p class="font-semibold">{{ loan.rate_of_interest || 5 }}% /month</p>
        </div>
        <div>
          <p class="text-xs text-gray-600 mb-1">Amount Paid</p>
          <p class="font-semibold text-green-600">KES {{ (loan.total_payment || 0).toLocaleString() }}</p>
        </div>
        <div>
          <p class="text-xs text-gray-600 mb-1">Outstanding</p>
          <p class="font-semibold text-red-600">
            KES {{ ((loan.total_payable || 0) - (loan.total_payment || 0)).toLocaleString() }}
          </p>
        </div>
      </div>

      <!-- Progress Bar -->
      <div v-if="loan.status === 'Active' || loan.status === 'Disbursed'" class="mb-4">
        <div class="flex justify-between text-xs text-gray-600 mb-1">
          <span>Repayment Progress</span>
          <span>{{ repaymentProgress }}%</span>
        </div>
        <div class="w-full bg-gray-200 rounded-full h-2">
          <div 
            :class="['h-2 rounded-full transition-all', progressColorClass]"
            :style="{ width: `${repaymentProgress}%` }"
          ></div>
        </div>
      </div>

      <!-- Actions -->
      <div class="flex gap-2">
        <button 
          v-if="loan.status === 'Active' || loan.status === 'Disbursed'"
          @click="$emit('pay', loan)"
          class="flex-1 bg-green-600 text-white py-2 px-4 rounded-lg font-medium hover:bg-green-700 transition">
          Make Payment
        </button>
        <button 
          @click="$emit('view', loan)"
          class="flex-1 bg-gray-100 text-gray-700 py-2 px-4 rounded-lg font-medium hover:bg-gray-200 transition">
          View Details
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  loan: { type: Object, required: true }
})

defineEmits(['pay', 'view'])

const formatDate = (dateStr) => {
  if (!dateStr) return 'N/A'
  return new Date(dateStr).toLocaleDateString('en-KE', { 
    year: 'numeric', 
    month: 'short', 
    day: 'numeric' 
  })
}

const repaymentProgress = computed(() => {
  const total = props.loan.total_payable || props.loan.loan_amount || 0
  const paid = props.loan.total_payment || 0
  if (total === 0) return 0
  return Math.min(Math.round((paid / total) * 100), 100)
})

const statusColorClass = computed(() => {
  const status = props.loan.status
  if (status === 'Active' || status === 'Disbursed') return 'bg-green-50'
  if (status === 'Pending' || status === 'Open') return 'bg-yellow-50'
  if (status === 'Rejected' || status === 'Closed') return 'bg-red-50'
  return 'bg-gray-50'
})

const statusBadgeClass = computed(() => {
  const status = props.loan.status
  if (status === 'Active' || status === 'Disbursed') return 'bg-green-100 text-green-800'
  if (status === 'Pending' || status === 'Open') return 'bg-yellow-100 text-yellow-800'
  if (status === 'Rejected') return 'bg-red-100 text-red-800'
  if (status === 'Closed' || status === 'Repaid') return 'bg-gray-100 text-gray-800'
  return 'bg-blue-100 text-blue-800'
})

const progressColorClass = computed(() => {
  const progress = repaymentProgress.value
  if (progress >= 75) return 'bg-green-500'
  if (progress >= 50) return 'bg-yellow-500'
  return 'bg-red-500'
})
</script>
