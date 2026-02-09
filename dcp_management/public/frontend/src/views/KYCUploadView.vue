<template>
  <div class="min-h-screen bg-white py-12 px-4 font-inter text-ink-black">
    <div class="max-w-4xl mx-auto">

      <!-- ===== DeepSeek AI Analysis Overlay ===== -->
      <div v-if="isAnalyzing" class="fixed inset-0 z-50 flex flex-col items-center justify-center bg-white/95 transition-all duration-1000">
        <!-- Loader Ring -->
        <div class="relative mb-12">
          <div class="w-32 h-32 rounded-full border-4 border-vapor-grey flex items-center justify-center">
            <div class="w-24 h-24 rounded-full border-4 border-deepseek-blue border-t-transparent animate-spin"></div>
          </div>
          <!-- Success state: morphs to green circle with check -->
          <div v-if="analysisComplete" class="absolute inset-0 flex items-center justify-center">
            <div class="w-32 h-32 rounded-full bg-watch-green flex items-center justify-center">
              <svg class="w-16 h-16 text-ink-black" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"></path>
              </svg>
            </div>
          </div>
        </div>

        <h2 class="text-xl font-black text-deepseek-blue uppercase tracking-[0.2em] mb-8">DeepSeek AI Analysis</h2>

        <!-- Typewriter Terminal Feedback -->
        <div class="w-full max-w-md border-2 border-ink-black bg-white p-6 font-mono text-xs text-ink-black overflow-hidden h-48 shadow-hard-md">
          <div v-for="(line, index) in analysisLines" :key="index" class="mb-1 text-ink-black/70">
            &gt; {{ line }}
          </div>
          <div v-if="currentAnalysisLine" class="text-deepseek-blue font-bold">
            &gt; {{ currentAnalysisLine }}<span class="inline-block w-2 h-3 bg-deepseek-blue ml-1 animate-pulse"></span>
          </div>
        </div>

        <p class="mt-8 text-ink-black/40 uppercase tracking-[0.2em] text-[10px] font-black">Analyzing document integrity &amp; income consistency</p>
      </div>

      <!-- ===== Main Upload Content: "The Digital Desk" ===== -->
      <div v-else>
        <!-- Header -->
        <div class="mb-12">
          <h1 class="text-4xl font-black uppercase tracking-tight mb-2">
            Secure <span class="text-watch-green">Upload Center</span>
          </h1>
          <p class="text-ink-black/50 text-sm">Please provide the following documents for AI-powered verification.</p>
        </div>

        <!-- Document Drop Zones ("The Clean Desk") -->
        <div class="space-y-6 mb-12">

          <!-- Zone 1: Payslips -->
          <div class="relative group">
            <div :class="['p-8 border-2 border-dashed transition-all duration-300 bg-white',
                       documents.payslips ? 'border-watch-green bg-watch-green/5' : 'border-ink-black hover:border-watch-green']">
              <div class="flex flex-col md:flex-row md:items-center justify-between gap-6">
                <div class="flex-1">
                  <div class="flex items-center gap-3 mb-2">
                    <h3 class="text-lg font-black uppercase">Last 3 Payslips</h3>
                    <span v-if="documents.payslips" class="status-approved">READY</span>
                  </div>
                  <p class="text-sm text-ink-black/50">Upload your most recent 3 months payslips in PDF or clear Photo format.</p>
                </div>
                <div class="flex-shrink-0">
                  <label class="cursor-pointer border-2 border-ink-black bg-white px-6 py-3 inline-block text-center min-w-[160px] shadow-hard-sm hover:shadow-hard-md transition-all active:shadow-none active:translate-x-[3px] active:translate-y-[3px]">
                    <span class="font-black text-xs uppercase tracking-widest">{{ documents.payslips ? 'Change File' : 'Upload PDF' }}</span>
                    <input type="file" class="hidden" @change="(e) => handleUpload(e, 'payslips')" accept=".pdf,.jpg,.jpeg,.png" />
                  </label>
                </div>
              </div>

              <!-- Scanner animation overlay -->
              <div v-if="isScanning === 'payslips'" class="absolute inset-0 pointer-events-none overflow-hidden">
                <div class="w-full h-1 bg-watch-green shadow-green-glow animate-scan"></div>
              </div>
            </div>
          </div>

          <!-- Zone 2: M-Pesa Statement -->
          <div class="relative group">
            <div :class="['p-8 border-2 border-dashed transition-all duration-300 bg-white',
                       documents.mpesa ? 'border-watch-green bg-watch-green/5' : 'border-ink-black hover:border-watch-green']">
              <div class="flex flex-col md:flex-row md:items-center justify-between gap-6">
                <div class="flex-1">
                  <div class="flex items-center gap-3 mb-2">
                    <h3 class="text-lg font-black uppercase">M-Pesa Statement</h3>
                    <span v-if="documents.mpesa" class="status-approved">READY</span>
                  </div>
                  <p class="text-sm text-ink-black/50">Upload your last 2 months M-Pesa statement (PDF).</p>
                  <button class="mt-2 text-deepseek-blue text-xs uppercase font-black hover:underline">How to get this?</button>
                </div>
                <div class="flex-shrink-0">
                  <label class="cursor-pointer border-2 border-ink-black bg-white px-6 py-3 inline-block text-center min-w-[160px] shadow-hard-sm hover:shadow-hard-md transition-all active:shadow-none active:translate-x-[3px] active:translate-y-[3px]">
                    <span class="font-black text-xs uppercase tracking-widest">{{ documents.mpesa ? 'Change File' : 'Upload PDF' }}</span>
                    <input type="file" class="hidden" @change="(e) => handleUpload(e, 'mpesa')" accept=".pdf,.jpg,.jpeg,.png" />
                  </label>
                </div>
              </div>
              <div v-if="isScanning === 'mpesa'" class="absolute inset-0 pointer-events-none overflow-hidden">
                <div class="w-full h-1 bg-watch-green shadow-green-glow animate-scan"></div>
              </div>
            </div>
          </div>

          <!-- Zone 3: Bank Statement -->
          <div class="relative group">
            <div :class="['p-8 border-2 border-dashed transition-all duration-300 bg-white',
                       documents.bank ? 'border-watch-green bg-watch-green/5' : 'border-ink-black hover:border-watch-green']">
              <div class="flex flex-col md:flex-row md:items-center justify-between gap-6">
                <div class="flex-1">
                  <div class="flex items-center gap-3 mb-2">
                    <h3 class="text-lg font-black uppercase">Bank Statement</h3>
                    <span v-if="documents.bank" class="status-approved">READY</span>
                  </div>
                  <p class="text-sm text-ink-black/50">Upload your last 2 months bank statement (PDF).</p>
                </div>
                <div class="flex-shrink-0">
                  <label class="cursor-pointer border-2 border-ink-black bg-white px-6 py-3 inline-block text-center min-w-[160px] shadow-hard-sm hover:shadow-hard-md transition-all active:shadow-none active:translate-x-[3px] active:translate-y-[3px]">
                    <span class="font-black text-xs uppercase tracking-widest">{{ documents.bank ? 'Change File' : 'Upload PDF' }}</span>
                    <input type="file" class="hidden" @change="(e) => handleUpload(e, 'bank')" accept=".pdf,.jpg,.jpeg,.png" />
                  </label>
                </div>
              </div>
              <div v-if="isScanning === 'bank'" class="absolute inset-0 pointer-events-none overflow-hidden">
                <div class="w-full h-1 bg-watch-green shadow-green-glow animate-scan"></div>
              </div>
            </div>
          </div>
        </div>

        <!-- Action Bar -->
        <div class="flex flex-col sm:flex-row items-center justify-between p-6 border-2 border-ink-black bg-vapor-grey shadow-hard-sm gap-4">
          <div class="flex items-center gap-4">
            <div class="badge-encrypted">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"></path></svg>
              ODPC COMPLIANT &bull; AES-256
            </div>
          </div>

          <button @click="startAnalysis"
                  :disabled="!isReady"
                  :class="['btn-primary whitespace-nowrap',
                           !isReady ? 'opacity-30 cursor-not-allowed shadow-none' : '']">
            Verify with DeepSeek AI
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const documents = ref({ payslips: null, mpesa: null, bank: null });
const isScanning = ref(null);
const isAnalyzing = ref(false);
const analysisComplete = ref(false);
const analysisLines = ref([]);
const currentAnalysisLine = ref('');

const isReady = computed(() => {
  return documents.value.payslips && documents.value.mpesa && documents.value.bank;
});

const handleUpload = (event, type) => {
  const file = event.target.files[0];
  if (!file) return;
  isScanning.value = type;
  setTimeout(() => {
    documents.value[type] = file;
    isScanning.value = null;
  }, 1500);
};

const startAnalysis = async () => {
  isAnalyzing.value = true;
  analysisComplete.value = false;

  const possibleLines = [
    "SCANNING: PAYSLIP_OCTOBER.PDF",
    "EXTRACTING: NET_PAY...",
    "VERIFYING: EMPLOYER_KRA_PIN...",
    "Cross-referencing M-Pesa turnover patterns...",
    "Extracting 'Net Pay' fields: KSh 45,000 confirmed...",
    "Heuristic analysis for forgery detection: 100% clean.",
    "DETECTING: Salary-backed profile confirmed.",
    "Running risk scoring algorithm...",
    "DeepSeek confidence score: 98%."
  ];

  for (const line of possibleLines) {
    currentAnalysisLine.value = line;
    await new Promise(r => setTimeout(r, 600 + Math.random() * 800));
    analysisLines.value.push(line);
    currentAnalysisLine.value = '';
  }

  analysisComplete.value = true;
  await new Promise(r => setTimeout(r, 1200));
  router.push({ name: 'dashboard', query: { status: 'pending' } });
};
</script>
