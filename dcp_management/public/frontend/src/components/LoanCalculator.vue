<template>
  <div class="p-8 border-2 border-ink-black bg-white shadow-hard-md font-inter relative">
    <h3 class="text-2xl font-black uppercase tracking-tight mb-8">Loan Calculator</h3>

    <div class="space-y-8">
      <!-- Amount Slider -->
      <div>
        <div class="flex justify-between mb-4">
          <label class="text-[10px] font-black text-ink-black/40 uppercase tracking-[0.2em]">Loan Amount</label>
          <span class="text-xl font-black">KES {{ amount.toLocaleString() }}</span>
        </div>
        <input
          v-model.number="amount"
          type="range" min="1000" max="100000" step="500"
          class="w-full h-2 bg-ink-black/10 appearance-none cursor-pointer accent-watch-green"
        >
        <div class="flex justify-between text-[10px] text-ink-black/30 font-black uppercase tracking-widest mt-2">
          <span>KES 1,000</span>
          <span>KES 100,000</span>
        </div>
      </div>

      <!-- Tenure Slider -->
      <div>
        <div class="flex justify-between mb-4">
          <label class="text-[10px] font-black text-ink-black/40 uppercase tracking-[0.2em]">Payment Period</label>
          <span class="text-xl font-black">{{ tenure }} Months</span>
        </div>
        <input
          v-model.number="tenure"
          type="range" min="1" max="6" step="1"
          class="w-full h-2 bg-ink-black/10 appearance-none cursor-pointer accent-watch-green"
        >
        <div class="flex justify-between text-[10px] text-ink-black/30 font-black uppercase tracking-widest mt-2">
          <span>1 Month</span>
          <span>6 Months</span>
        </div>
      </div>

      <!-- Breakdown -->
      <div class="bg-vapor-grey border-2 border-ink-black/10 p-6 space-y-3">
        <div class="flex justify-between text-sm">
          <span class="text-ink-black/50">Principal</span>
          <span class="font-black">KES {{ amount.toLocaleString() }}</span>
        </div>
        <div class="flex justify-between text-sm">
          <span class="text-ink-black/50">Interest ({{ interestRate }}% p.m.)</span>
          <span class="font-black">KES {{ interest.toLocaleString() }}</span>
        </div>
        <div class="border-t-2 border-ink-black pt-3 flex justify-between">
          <span class="font-black uppercase text-sm">Total Repayment</span>
          <span class="font-black text-lg text-watch-green">KES {{ totalRepayment.toLocaleString() }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';

const amount = ref(10000);
const tenure = ref(3);
const interestRate = 5;

const interest = computed(() => Math.round(amount.value * (interestRate / 100) * tenure.value));
const totalRepayment = computed(() => amount.value + interest.value);
</script>
