<template>
  <div class="min-h-screen bg-white font-inter text-ink-black pb-12">
    <!-- Dashboard Header -->
    <div class="border-b-2 border-ink-black bg-white sticky top-0 z-40">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-4">
            <div class="w-14 h-14 bg-watch-green text-ink-black flex items-center justify-center text-xl font-black shadow-hard-sm">
              {{ customerStore.initials || 'J' }}
            </div>
            <div>
              <h1 class="text-xl font-black uppercase tracking-tight">{{ firstName }}</h1>
              <p class="text-xs text-ink-black/40 uppercase tracking-[0.2em]">{{ customerStore.customer?.email || 'customer@example.com' }}</p>
            </div>
          </div>
          <div class="badge-encrypted">
            Tier 1 &bull; Salary Profile
          </div>
        </div>
      </div>
    </div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">

      <!-- ===== Pending AI/Admin Review State ("The Waiting Room") ===== -->
      <div v-if="isReviewPending" class="max-w-3xl mx-auto mt-12 border-2 border-ink-black bg-white p-12 shadow-hard-lg relative">
        <h2 class="text-3xl font-black text-center mb-12 uppercase tracking-tight">Application Status</h2>

        <!-- Progress Tracker: thick black track, green fill -->
        <div class="relative flex items-center justify-between mb-16">
          <!-- Background Track -->
          <div class="absolute left-0 top-1/2 -translate-y-1/2 w-full h-2 bg-ink-black/10"></div>
          <!-- Green Fill (2/3 done) -->
          <div class="absolute left-0 top-1/2 -translate-y-1/2 w-2/3 h-2 bg-watch-green"></div>

          <!-- Node: Upload -->
          <div class="relative z-10 flex flex-col items-center">
            <div class="w-12 h-12 bg-watch-green text-ink-black flex items-center justify-center shadow-hard-sm">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"></path></svg>
            </div>
            <p class="mt-4 text-[10px] font-black uppercase tracking-[0.2em] text-watch-green">Upload</p>
          </div>

          <!-- Node: AI Scan -->
          <div class="relative z-10 flex flex-col items-center">
            <div class="w-12 h-12 bg-watch-green text-ink-black flex items-center justify-center shadow-hard-sm">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"></path></svg>
            </div>
            <p class="mt-4 text-[10px] font-black uppercase tracking-[0.2em] text-watch-green">AI Scan</p>
          </div>

          <!-- Node: Admin Approval (pending) -->
          <div class="relative z-10 flex flex-col items-center">
            <div class="w-12 h-12 border-2 border-deepseek-blue bg-white text-deepseek-blue flex items-center justify-center animate-pulse">
              <svg class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
            </div>
            <p class="mt-4 text-[10px] font-black uppercase tracking-[0.2em] text-deepseek-blue">Admin Review</p>
          </div>
        </div>

        <div class="bg-vapor-grey border-2 border-ink-black/10 p-6 text-center">
          <p class="text-sm text-ink-black/60 leading-relaxed max-w-md mx-auto">
            Our credit officers are reviewing your <strong class="text-deepseek-blue">AI-verified</strong> application. Expect a decision within <strong class="text-ink-black">2 hours</strong>.
          </p>
        </div>

        <div class="mt-10 flex justify-center gap-4">
          <button class="border-2 border-ink-black bg-white px-8 py-3 font-black uppercase text-xs tracking-widest shadow-hard-sm hover:shadow-hard-md transition-all">Support Chat</button>
          <button @click="isReviewPending = false" class="text-xs font-black uppercase tracking-[0.2em] text-ink-black/40 hover:text-ink-black transition-all">View Dashboard</button>
        </div>
      </div>

      <!-- ===== Main Dashboard Content ===== -->
      <div v-else>
        <!-- Stats Overview -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-12">
          <div class="border-2 border-ink-black p-8 bg-white shadow-hard-sm group hover:shadow-hard-md transition-all">
            <p class="text-[10px] font-black text-ink-black/40 uppercase tracking-[0.2em] mb-1">Total Limit</p>
            <p class="text-4xl font-black">KSh 100K</p>
          </div>
          <div class="border-2 border-ink-black p-8 bg-white shadow-hard-sm group hover:shadow-hard-md transition-all">
            <p class="text-[10px] font-black text-ink-black/40 uppercase tracking-[0.2em] mb-1">Active Debt</p>
            <p class="text-4xl font-black text-alert-magenta">KSh {{ loanStore.totalOutstanding?.toLocaleString() || 0 }}</p>
          </div>
          <div class="border-2 border-ink-black p-8 bg-white shadow-hard-sm group hover:shadow-hard-md transition-all">
            <p class="text-[10px] font-black text-ink-black/40 uppercase tracking-[0.2em] mb-1">AI Trust Score</p>
            <p class="text-4xl font-black text-deepseek-blue">98%</p>
          </div>
        </div>

        <!-- Eligible Solutions -->
        <h2 class="section-heading mb-6">Eligible Solutions</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-12">
          <!-- Salary Advance -->
          <div class="border-2 border-ink-black p-8 bg-white shadow-hard-sm hover:shadow-hard-md transition-all group">
            <h3 class="text-2xl font-black mb-2 uppercase">Salary Advance</h3>
            <p class="text-sm text-ink-black/50 mb-8">Up to 50% of your Net Salary. Instant M-Pesa disbursement.</p>
            <RouterLink to="/apply" class="btn-primary inline-block">Request Advance</RouterLink>
          </div>
          <!-- Check-off Loan -->
          <div class="border-2 border-ink-black/30 p-8 bg-vapor-grey shadow-hard-sm group">
            <h3 class="text-2xl font-black mb-2 uppercase text-ink-black/40">Check-off Loan</h3>
            <p class="text-sm text-ink-black/30 mb-8">Direct payroll deduction. Longer tenures and higher limits.</p>
            <button class="border-2 border-ink-black/20 px-8 py-3 font-black uppercase text-xs tracking-widest text-ink-black/30 cursor-not-allowed">Employer Search Needed</button>
          </div>
        </div>

        <!-- Recent Transactions -->
        <div class="border-2 border-ink-black overflow-hidden shadow-hard-sm">
          <div class="p-6 border-b-2 border-ink-black bg-vapor-grey">
            <h3 class="font-black text-xs uppercase tracking-[0.2em]">Transaction History</h3>
          </div>
          <div v-if="loanStore.loans?.length > 0">
            <div v-for="loan in loanStore.loans" :key="loan.name" class="p-6 flex items-center justify-between border-b border-ink-black/10 hover:bg-vapor-grey transition-colors">
              <div class="flex items-center gap-4">
                <div class="w-10 h-10 border-2 border-ink-black flex items-center justify-center">
                  <svg class="w-5 h-5 text-ink-black" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
                </div>
                <div>
                  <p class="font-black text-sm">{{ loan.loan_product }}</p>
                  <p class="text-[10px] text-ink-black/40 uppercase tracking-[0.2em]">{{ loan.creation }}</p>
                </div>
              </div>
              <div class="text-right">
                <p class="font-black text-sm">KSh {{ (loan.loan_amount || 0).toLocaleString() }}</p>
                <span :class="loan.status === 'Sanctioned' ? 'status-approved' : 'status-pending'">{{ loan.status }}</span>
              </div>
            </div>
          </div>
          <div v-else class="p-12 text-center">
            <p class="text-xs text-ink-black/30 uppercase tracking-[0.2em] font-black">No transaction history detected</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { useRoute, useRouter, RouterLink } from 'vue-router';
import { useCustomerStore } from '@/stores/customer';
import { useLoanStore } from '@/stores/loans';

const route = useRoute();
const router = useRouter();
const customerStore = useCustomerStore();
const loanStore = useLoanStore();

const isReviewPending = ref(route.query.status === 'pending');

const firstName = computed(() => {
  if (!customerStore.customer?.customer_name) return 'Professional';
  return customerStore.customer.customer_name.split(' ')[0];
});

onMounted(async () => {
  if (!customerStore.customer) {
    await customerStore.fetchCurrentUser();
  }
  if (customerStore.customer) {
    await loanStore.fetchLoans(customerStore.customer.name);
  }
});
</script>
