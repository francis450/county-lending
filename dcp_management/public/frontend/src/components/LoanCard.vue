<template>
  <div class="border-2 border-ink-black p-6 bg-white shadow-hard-sm hover:shadow-hard-md transition-all font-inter">
    <div class="flex items-center justify-between mb-4">
      <div>
        <p class="font-black text-sm uppercase">{{ loan.loan_product || 'Salary Advance' }}</p>
        <p class="text-[10px] text-ink-black/40 uppercase tracking-widest">{{ loan.name }}</p>
      </div>
      <span :class="statusClass">{{ loan.status }}</span>
    </div>
    <div class="flex items-end justify-between">
      <div>
        <p class="text-2xl font-black">KES {{ (loan.loan_amount || 0).toLocaleString() }}</p>
        <p class="text-[10px] text-ink-black/40 uppercase tracking-widest mt-1">{{ loan.creation }}</p>
      </div>
      <button class="text-[10px] font-black uppercase tracking-widest text-deepseek-blue hover:underline">Details</button>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  loan: { type: Object, required: true }
})

const statusClass = computed(() => {
  const s = props.loan.status;
  if (s === 'Sanctioned' || s === 'Approved') return 'status-approved';
  if (s === 'Rejected') return 'bg-alert-magenta text-white text-[10px] font-black uppercase px-3 py-1';
  return 'status-pending';
})
</script>
