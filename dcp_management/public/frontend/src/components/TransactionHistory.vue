<template>
  <div class="border-2 border-ink-black bg-white shadow-hard-sm font-inter">
    <div class="flex items-center justify-between p-6 border-b-2 border-ink-black bg-vapor-grey">
      <h3 class="font-black text-xs uppercase tracking-[0.2em]">Recent Transactions</h3>
      <button class="text-[10px] font-black text-deepseek-blue uppercase tracking-widest hover:underline">View All</button>
    </div>

    <div v-if="loading" class="text-center py-8 text-ink-black/40 text-sm">
      Loading transactions...
    </div>

    <div v-else-if="transactions.length === 0" class="text-center py-8">
      <svg class="w-12 h-12 mx-auto mb-2 text-ink-black/10" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path>
      </svg>
      <p class="text-xs text-ink-black/30 uppercase tracking-widest font-black">No transactions yet</p>
    </div>

    <div v-else>
      <div
        v-for="transaction in displayedTransactions"
        :key="transaction.id"
        class="flex items-center justify-between p-5 border-b border-ink-black/10 last:border-0 hover:bg-vapor-grey transition-colors">
        <div class="flex items-center gap-3">
          <div :class="['w-10 h-10 flex items-center justify-center', getIconClass(transaction.type)]">
            <svg v-if="transaction.type === 'payment'" class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"></path>
            </svg>
            <svg v-else-if="transaction.type === 'disbursement'" class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
            </svg>
            <svg v-else class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"></path>
            </svg>
          </div>
          <div>
            <p class="font-black text-sm">{{ transaction.description }}</p>
            <p class="text-[10px] text-ink-black/40 uppercase tracking-widest">{{ formatDate(transaction.date) }}</p>
          </div>
        </div>
        <div class="text-right">
          <p :class="['font-black text-sm', getAmountClass(transaction.type)]">
            {{ transaction.type === 'payment' ? '-' : '+' }} KES {{ transaction.amount.toLocaleString() }}
          </p>
          <p class="text-[10px] text-ink-black/40 uppercase tracking-widest">{{ transaction.status }}</p>
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
  limit: { type: Number, default: 5 }
})

const displayedTransactions = computed(() => props.transactions.slice(0, props.limit))

const formatDate = (dateStr) => {
  if (!dateStr) return '';
  const d = new Date(dateStr);
  return d.toLocaleDateString('en-KE', { day: '2-digit', month: 'short', year: 'numeric' });
}

const getIconClass = (type) => {
  if (type === 'payment') return 'bg-watch-green text-ink-black';
  if (type === 'disbursement') return 'bg-deepseek-blue text-white';
  return 'border-2 border-ink-black bg-vapor-grey text-ink-black';
}

const getAmountClass = (type) => {
  if (type === 'payment') return 'text-watch-green';
  return 'text-ink-black';
}
</script>
