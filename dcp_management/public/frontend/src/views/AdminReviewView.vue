<template>
  <div class="min-h-screen bg-white font-inter text-ink-black pb-20">
    <!-- Admin Header -->
    <div class="border-b-2 border-ink-black bg-white sticky top-0 z-40">
      <div class="max-w-[1400px] mx-auto px-6 py-5 flex items-center justify-between">
        <div class="flex items-center gap-6">
          <div class="w-12 h-12 bg-deepseek-blue text-white flex items-center justify-center shadow-hard-sm">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"></path></svg>
          </div>
          <h1 class="text-xl font-black uppercase tracking-tight">Admin <span class="text-deepseek-blue">Review Panel</span></h1>
        </div>

        <div class="flex items-center gap-8">
          <div class="flex items-center gap-2">
            <div class="w-2 h-2 bg-watch-green animate-pulse"></div>
            <span class="text-[10px] font-black uppercase tracking-[0.2em] text-ink-black/40">DeepSeek Active</span>
          </div>
          <div class="w-10 h-10 border-2 border-ink-black flex items-center justify-center text-xs font-black">
            AD
          </div>
        </div>
      </div>
    </div>

    <!-- Main Grid -->
    <div class="max-w-[1400px] mx-auto px-6 pt-8 grid grid-cols-1 lg:grid-cols-3 gap-8">

      <!-- Left Column: Processing Queue (spreadsheet/email-client dense) -->
      <div class="lg:col-span-1">
        <h2 class="section-heading mb-6">Processing Queue</h2>
        <div class="space-y-3">
          <div v-for="app in queue"
               :key="app.name"
               @click="selectedApp = app"
               :class="['p-5 border-2 cursor-pointer transition-all',
                        selectedApp?.name === app.name
                          ? 'border-deepseek-blue bg-deepseek-blue/5 border-l-4'
                          : 'border-ink-black/20 bg-white hover:border-ink-black',
                        app.ai_score >= 90 ? '' : '']">
            <!-- High match = green tint, Risk = red tint -->
            <div :class="['p-4 -m-5 mb-0',
                          app.ai_score >= 90 ? 'bg-watch-green/5' : 'bg-alert-magenta/5']">
              <div class="flex justify-between items-start mb-3">
                <div>
                  <p class="text-[10px] font-black text-ink-black/30 uppercase tracking-widest">{{ app.name }}</p>
                  <h3 class="text-lg font-black">{{ app.customer_name }}</h3>
                </div>
                <span :class="['text-[10px] font-black uppercase px-2 py-0.5',
                              app.ai_score >= 90 ? 'bg-watch-green text-ink-black' : 'bg-alert-magenta text-white']">
                  {{ app.ai_score }}% CONF
                </span>
              </div>

              <div class="flex items-center justify-between">
                <p class="text-[10px] font-black text-ink-black/40 uppercase tracking-widest">KSh {{ app.loan_amount.toLocaleString() }}</p>
                <p class="text-[10px] font-black text-ink-black/30 uppercase tracking-widest">{{ app.creation }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Right Column: Review Blade -->
      <div class="lg:col-span-2">
        <div v-if="selectedApp" class="border-2 border-ink-black bg-white shadow-hard-lg overflow-hidden sticky top-24">

          <!-- Review Header -->
          <div class="p-8 border-b-2 border-ink-black flex flex-col md:flex-row md:items-center justify-between gap-4 bg-vapor-grey">
            <div>
              <h2 class="text-2xl font-black uppercase tracking-tight">Application <span class="text-deepseek-blue">{{ selectedApp.name }}</span></h2>
              <p class="text-[10px] text-ink-black/40 mt-1 uppercase tracking-[0.2em]">Salaried Professional Verification</p>
            </div>
            <div class="flex gap-3">
              <button class="btn-outline-danger">Reject</button>
              <button class="btn-primary">Approve Disbursement</button>
            </div>
          </div>

          <div class="grid grid-cols-1 md:grid-cols-2">
            <!-- Document Viewer -->
            <div class="p-8 border-r-2 border-ink-black bg-white">
              <div class="flex items-center justify-between mb-6">
                <h3 class="section-heading">Raw Documents</h3>
                <div class="flex gap-2">
                  <span class="text-[10px] font-black uppercase px-2 py-0.5 border-2 border-ink-black bg-vapor-grey">Payslip</span>
                  <span class="text-[10px] font-black uppercase px-2 py-0.5 border-2 border-ink-black bg-vapor-grey">MPESA</span>
                </div>
              </div>
              <div class="aspect-[4/5] bg-vapor-grey border-2 border-ink-black flex items-center justify-center relative group">
                <div class="text-center p-8">
                  <svg class="w-12 h-12 text-ink-black/20 mx-auto mb-4" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M7 21h10a2 2 0 002-2V9.414a1 1 0 00-.293-.707l-5.414-5.414A1 1 0 0012.586 3H7a2 2 0 00-2 2v14a2 2 0 002 2z"></path></svg>
                  <p class="text-[10px] text-ink-black/30 uppercase tracking-widest font-black">DeepSeek Document Scanned</p>
                </div>
                <!-- Scan line on hover -->
                <div class="absolute inset-0 z-20 pointer-events-none overflow-hidden group-hover:opacity-100 opacity-0 transition-opacity">
                  <div class="w-full h-1 bg-watch-green shadow-green-glow animate-scan"></div>
                </div>
              </div>
            </div>

            <!-- DeepSeek AI Analysis Panel -->
            <div class="p-8">
              <h3 class="section-heading mb-6">DeepSeek AI Summary</h3>

              <!-- Confidence Score -->
              <div class="p-4 border-2 border-deepseek-blue bg-deepseek-blue/5 mb-6">
                <p class="text-[10px] font-black text-deepseek-blue uppercase tracking-[0.2em] mb-2">DeepSeek Confidence Score</p>
                <p class="text-4xl font-black text-watch-green">98%</p>
              </div>

              <!-- Income Verification -->
              <div class="p-4 border-2 border-ink-black/10 mb-6">
                <p class="text-[10px] font-black text-ink-black/40 uppercase tracking-[0.2em] mb-2">Income Verification</p>
                <div class="flex justify-between items-end">
                  <div>
                    <p class="text-2xl font-black">KSh {{ selectedApp.detected_salary.toLocaleString() }}</p>
                    <p class="text-[10px] text-ink-black/40 uppercase tracking-widest">Detected Net Salary</p>
                  </div>
                  <div class="text-right">
                    <p class="text-xl font-black text-watch-green">98%</p>
                    <p class="text-[10px] text-ink-black/40 uppercase tracking-widest">Consistency</p>
                  </div>
                </div>
              </div>

              <!-- Verified Items -->
              <div class="space-y-3 mb-6">
                <div class="flex items-center gap-3">
                  <div class="w-5 h-5 bg-watch-green flex items-center justify-center flex-shrink-0">
                    <svg class="w-3 h-3 text-ink-black" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"></path></svg>
                  </div>
                  <span class="text-xs text-ink-black/70 italic">"Company: Safaricom PLC confirmed via PDF Metadata"</span>
                </div>
                <div class="flex items-center gap-3">
                  <div class="w-5 h-5 bg-watch-green flex items-center justify-center flex-shrink-0">
                    <svg class="w-3 h-3 text-ink-black" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"></path></svg>
                  </div>
                  <span class="text-xs text-ink-black/70 italic">"M-Pesa entry 'Salary' matches payslip amount"</span>
                </div>
              </div>

              <!-- Risk Flags -->
              <div v-if="selectedApp.flags.length > 0" class="p-4 border-2 border-alert-magenta bg-alert-magenta/5">
                <p class="text-[10px] font-black text-alert-magenta uppercase tracking-[0.2em] mb-2">DeepSeek Risk Flags</p>
                <div v-for="flag in selectedApp.flags" :key="flag" class="flex items-start gap-3 mt-2">
                  <svg class="w-4 h-4 text-alert-magenta flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path></svg>
                  <span class="text-xs font-semibold text-alert-magenta">{{ flag }}</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Empty State -->
        <div v-else class="h-full flex items-center justify-center border-2 border-dashed border-ink-black/20 bg-vapor-grey p-20">
          <div class="text-center">
            <p class="text-xs font-black uppercase tracking-[0.2em] mb-4 text-ink-black/30">Awaiting Selection</p>
            <p class="text-[10px] max-w-xs text-ink-black/20 uppercase tracking-[0.2em] leading-loose">Choose an applicant from the processing queue to begin review.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { api } from '@/api';

const queue = ref([]);
const selectedApp = ref(null);

onMounted(async () => {
  try {
    const res = await api.get('/api/method/dcp_management.api.get_admin_application_queue');
    if (res.message) {
      queue.value = res.message;
      if (queue.value.length > 0) {
        selectedApp.value = queue.value[0];
      }
    }
  } catch (e) {
    console.error("Failed to load queue", e);
  }
});
</script>
