<template>
  <div class="bg-white rounded-xl shadow-lg border border-gray-200 p-6">
    <div class="flex items-center justify-between mb-4">
      <h3 class="text-lg font-bold text-gray-900">Recent Transactions</h3>
      <button class="text-sm text-green-600 hover:text-green-700 font-medium">View All</button>
    </div>

    <div v-if="loading" class="text-center py-8 text-gray-500">
      Loading transactions...
    </div>

    <div v-else-if="transactions.length === 0" class="text-center py-8 text-gray-500">
      <svg class="w-12 h-12 mx-auto mb-2 opacity-50" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path>
      </svg>
      <p>No transactions yet</p>
    </div>

    <div v-else class="space-y-3">
      <div 
        v-for="transaction in displayedTransactions" 
        :key="transaction.id"
        class="flex items-center justify-between py-3 border-b border-gray-100 last:border-0">
        <div class="flex items-center">
          <div :class="['w-10 h-10 rounded-full flex items-center justify-center mr-3', getIconClass(transaction.type)]">
            <svg v-if="transaction.type === 'payment'" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
            </svg>
            <svg v-else-if="transaction.type === 'disbursement'" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
            </svg>
            <svg v-else class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path>
            </svg>
          </div>
          <div>
            <p class="font-medium text-gray-900">{{ transaction.description }}</p>
            <p class="text-xs text-gray-500">{{ formatDate(transaction.date) }}</p>
          </div>
        </div>
        <div class="text-right">
          <p :class="['font-semibold', getAmountClass(transaction.type)]">
            {{ transaction.type === 'payment' ? '-' : '+' }} KES {{ transaction.amount.toLocaleString() }}
          </p>
          <p class="text-xs text-gray-500">{{ transaction.status }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  transactions: { type: Array, default: () => [] },
  loading: { type: Boolean, default: false },
  maxDisplay: { type: Number, default: 5 }
})

const displayedTransactions = computed(() => {
  return props.transactions.slice(0, props.maxDisplay)
})

const formatDate = (dateStr) => {
  if (!dateStr) return 'N/A'
  return new Date(dateStr).toLocaleDateString('en-KE', { 
    year: 'numeric', 
    month: 'short', 
    day: 'numeric',
    hour: '2-digit',
    minute: '2-digit'
  })
}

const getIconClass = (type) => {
  if (type === 'payment') return 'bg-red-100 text-red-600'
  if (type === 'disbursement') return 'bg-green-100 text-green-600'
  return 'bg-blue-100 text-blue-600'
}

const getAmountClass = (type) => {
  if (type === 'payment') return 'text-red-600'
  return 'text-green-600'
}
</script>
