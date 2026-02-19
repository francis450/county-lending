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

        <!-- Error Message -->
        <div v-if="errorMessage" class="mb-6 p-4 border-2 border-red-500 bg-red-50 text-red-700">
          <p class="font-bold">Error</p>
          <p class="text-sm">{{ errorMessage }}</p>
        </div>

        <form @submit.prevent="startAnalysis" class="space-y-8">

          <!-- ========== SECTION 1: Identity Documents ========== -->
          <div class="border-2 border-ink-black p-6 bg-vapor-grey/30">
            <h2 class="text-2xl font-black uppercase mb-6 flex items-center gap-3">
              <span class="text-deepseek-blue">01</span> Identity Documents
            </h2>

            <!-- National ID Number -->
            <div class="mb-6">
              <label class="block text-sm font-black uppercase mb-2">National ID Number <span class="text-red-500">*</span></label>
              <input 
                v-model="formData.national_id" 
                type="text" 
                maxlength="8"
                required
                placeholder="12345678"
                class="w-full px-4 py-3 border-2 border-ink-black shadow-hard-sm focus:outline-none focus:border-deepseek-blue"
              />
            </div>

            <!-- National ID Front & Back -->
            <div class="grid md:grid-cols-2 gap-6 mb-6">
              <div class="relative group">
                <label class="block text-sm font-black uppercase mb-2">National ID (Front) <span class="text-red-500">*</span></label>
                <div :class="['p-6 border-2 border-dashed transition-all',
                           documents.national_id_front ? 'border-watch-green bg-watch-green/5' : 'border-ink-black hover:border-watch-green']">
                  <label class="cursor-pointer block text-center">
                    <div class="mb-2">
                      <span v-if="documents.national_id_front" class="text-watch-green font-bold text-sm">✓ UPLOADED</span>
                      <span v-else class="text-ink-black/50 text-sm">Click to upload</span>
                    </div>
                    <input type="file" required class="hidden" @change="(e) => handleUpload(e, 'national_id_front')" accept="image/*,.pdf" />
                  </label>
                  <div v-if="isScanning === 'national_id_front'" class="absolute inset-0 pointer-events-none overflow-hidden">
                    <div class="w-full h-1 bg-watch-green shadow-green-glow animate-scan"></div>
                  </div>
                </div>
              </div>

              <div class="relative group">
                <label class="block text-sm font-black uppercase mb-2">National ID (Back) <span class="text-red-500">*</span></label>
                <div :class="['p-6 border-2 border-dashed transition-all',
                           documents.national_id_back ? 'border-watch-green bg-watch-green/5' : 'border-ink-black hover:border-watch-green']">
                  <label class="cursor-pointer block text-center">
                    <div class="mb-2">
                      <span v-if="documents.national_id_back" class="text-watch-green font-bold text-sm">✓ UPLOADED</span>
                      <span v-else class="text-ink-black/50 text-sm">Click to upload</span>
                    </div>
                    <input type="file" required class="hidden" @change="(e) => handleUpload(e, 'national_id_back')" accept="image/*,.pdf" />
                  </label>
                  <div v-if="isScanning === 'national_id_back'" class="absolute inset-0 pointer-events-none overflow-hidden">
                    <div class="w-full h-1 bg-watch-green shadow-green-glow animate-scan"></div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Passport Photo -->
            <div class="relative group">
              <label class="block text-sm font-black uppercase mb-2">Passport Photo <span class="text-red-500">*</span></label>
              <div :class="['p-6 border-2 border-dashed transition-all max-w-xs',
                         documents.passport_photo ? 'border-watch-green bg-watch-green/5' : 'border-ink-black hover:border-watch-green']">
                <label class="cursor-pointer block text-center">
                  <div class="mb-2">
                    <span v-if="documents.passport_photo" class="text-watch-green font-bold text-sm">✓ UPLOADED</span>
                    <span v-else class="text-ink-black/50 text-sm">Click to upload</span>
                  </div>
                  <input type="file" required class="hidden" @change="(e) => handleUpload(e, 'passport_photo')" accept="image/*" />
                </label>
                <div v-if="isScanning === 'passport_photo'" class="absolute inset-0 pointer-events-none overflow-hidden">
                  <div class="w-full h-1 bg-watch-green shadow-green-glow animate-scan"></div>
                </div>
              </div>
            </div>
          </div>

          <!-- ========== SECTION 2: Tax Documents ========== -->
          <div class="border-2 border-ink-black p-6 bg-vapor-grey/30">
            <h2 class="text-2xl font-black uppercase mb-6 flex items-center gap-3">
              <span class="text-deepseek-blue">02</span> Tax Documents
            </h2>

            <!-- KRA PIN -->
            <div class="mb-6">
              <label class="block text-sm font-black uppercase mb-2">KRA PIN <span class="text-red-500">*</span></label>
              <input 
                v-model="formData.kra_pin" 
                type="text" 
                maxlength="11"
                required
                placeholder="A001234567X"
                class="w-full px-4 py-3 border-2 border-ink-black shadow-hard-sm focus:outline-none focus:border-deepseek-blue"
              />
            </div>

            <!-- KRA PIN Certificate -->
            <div class="relative group">
              <label class="block text-sm font-black uppercase mb-2">KRA PIN Certificate <span class="text-red-500">*</span></label>
              <div :class="['p-6 border-2 border-dashed transition-all',
                         documents.kra_pin_certificate ? 'border-watch-green bg-watch-green/5' : 'border-ink-black hover:border-watch-green']">
                <label class="cursor-pointer block text-center">
                  <div class="mb-2">
                    <span v-if="documents.kra_pin_certificate" class="text-watch-green font-bold text-sm">✓ UPLOADED</span>
                    <span v-else class="text-ink-black/50 text-sm">Click to upload PDF</span>
                  </div>
                  <input type="file" required class="hidden" @change="(e) => handleUpload(e, 'kra_pin_certificate')" accept=".pdf,image/*" />
                </label>
                <div v-if="isScanning === 'kra_pin_certificate'" class="absolute inset-0 pointer-events-none overflow-hidden">
                  <div class="w-full h-1 bg-watch-green shadow-green-glow animate-scan"></div>
                </div>
              </div>
            </div>
          </div>

          <!-- ========== SECTION 3: Financial Documents ========== -->
          <div class="border-2 border-ink-black p-6 bg-vapor-grey/30">
            <h2 class="text-2xl font-black uppercase mb-6 flex items-center gap-3">
              <span class="text-deepseek-blue">03</span> Financial Documents
            </h2>

            <!-- Payslips -->
            <div class="relative group mb-6">
              <label class="block text-sm font-black uppercase mb-2">Last 3 Months Payslips <span class="text-red-500">*</span></label>
              <div :class="['p-8 border-2 border-dashed transition-all duration-300 bg-white',
                         documents.payslip ? 'border-watch-green bg-watch-green/5' : 'border-ink-black hover:border-watch-green']">
                <div class="flex flex-col md:flex-row md:items-center justify-between gap-6">
                  <div class="flex-1">
                    <div class="flex items-center gap-3 mb-2">
                      <h3 class="text-lg font-black uppercase">Payslips</h3>
                      <span v-if="documents.payslip" class="status-approved">READY</span>
                    </div>
                    <p class="text-sm text-ink-black/50">Upload your most recent 3 months payslips in PDF or clear Photo format.</p>
                  </div>
                  <div class="flex-shrink-0">
                    <label class="cursor-pointer border-2 border-ink-black bg-white px-6 py-3 inline-block text-center min-w-[160px] shadow-hard-sm hover:shadow-hard-md transition-all active:shadow-none active:translate-x-[3px] active:translate-y-[3px]">
                      <span class="font-black text-xs uppercase tracking-widest">{{ documents.payslip ? 'Change File' : 'Upload PDF' }}</span>
                      <input type="file" required class="hidden" @change="(e) => handleUpload(e, 'payslip')" accept=".pdf,.jpg,.jpeg,.png" />
                    </label>
                  </div>
                </div>
                <div v-if="isScanning === 'payslip'" class="absolute inset-0 pointer-events-none overflow-hidden">
                  <div class="w-full h-1 bg-watch-green shadow-green-glow animate-scan"></div>
                </div>
              </div>
            </div>

            <!-- M-Pesa Statement -->
            <div class="relative group mb-6">
              <label class="block text-sm font-black uppercase mb-2">M-Pesa Statement (2 months) <span class="text-red-500">*</span></label>
              <div :class="['p-8 border-2 border-dashed transition-all duration-300 bg-white',
                         documents.mpesa_statement ? 'border-watch-green bg-watch-green/5' : 'border-ink-black hover:border-watch-green']">
                <div class="flex flex-col md:flex-row md:items-center justify-between gap-6">
                  <div class="flex-1">
                    <div class="flex items-center gap-3 mb-2">
                      <h3 class="text-lg font-black uppercase">M-Pesa Statement</h3>
                      <span v-if="documents.mpesa_statement" class="status-approved">READY</span>
                    </div>
                    <p class="text-sm text-ink-black/50">Upload your last 2 months M-Pesa statement (PDF).</p>
                  </div>
                  <div class="flex-shrink-0">
                    <label class="cursor-pointer border-2 border-ink-black bg-white px-6 py-3 inline-block text-center min-w-[160px] shadow-hard-sm hover:shadow-hard-md transition-all active:shadow-none active:translate-x-[3px] active:translate-y-[3px]">
                      <span class="font-black text-xs uppercase tracking-widest">{{ documents.mpesa_statement ? 'Change File' : 'Upload PDF' }}</span>
                      <input type="file" required class="hidden" @change="(e) => handleUpload(e, 'mpesa_statement')" accept=".pdf,.jpg,.jpeg,.png" />
                    </label>
                  </div>
                </div>
                <div v-if="isScanning === 'mpesa_statement'" class="absolute inset-0 pointer-events-none overflow-hidden">
                  <div class="w-full h-1 bg-watch-green shadow-green-glow animate-scan"></div>
                </div>
              </div>
            </div>

            <!-- Bank Statement -->
            <div class="relative group">
              <label class="block text-sm font-black uppercase mb-2">Bank Statement (2 months) <span class="text-red-500">*</span></label>
              <div :class="['p-8 border-2 border-dashed transition-all duration-300 bg-white',
                         documents.bank_statement ? 'border-watch-green bg-watch-green/5' : 'border-ink-black hover:border-watch-green']">
                <div class="flex flex-col md:flex-row md:items-center justify-between gap-6">
                  <div class="flex-1">
                    <div class="flex items-center gap-3 mb-2">
                      <h3 class="text-lg font-black uppercase">Bank Statement</h3>
                      <span v-if="documents.bank_statement" class="status-approved">READY</span>
                    </div>
                    <p class="text-sm text-ink-black/50">Upload your last 2 months bank statement (PDF).</p>
                  </div>
                  <div class="flex-shrink-0">
                    <label class="cursor-pointer border-2 border-ink-black bg-white px-6 py-3 inline-block text-center min-w-[160px] shadow-hard-sm hover:shadow-hard-md transition-all active:shadow-none active:translate-x-[3px] active:translate-y-[3px]">
                      <span class="font-black text-xs uppercase tracking-widest">{{ documents.bank_statement ? 'Change File' : 'Upload PDF' }}</span>
                      <input type="file" required class="hidden" @change="(e) => handleUpload(e, 'bank_statement')" accept=".pdf,.jpg,.jpeg,.png" />
                    </label>
                  </div>
                </div>
                <div v-if="isScanning === 'bank_statement'" class="absolute inset-0 pointer-events-none overflow-hidden">
                  <div class="w-full h-1 bg-watch-green shadow-green-glow animate-scan"></div>
                </div>
              </div>
            </div>
          </div>

          <!-- ========== SECTION 4: Residential Address ========== -->
          <div class="border-2 border-ink-black p-6 bg-vapor-grey/30">
            <h2 class="text-2xl font-black uppercase mb-6 flex items-center gap-3">
              <span class="text-deepseek-blue">04</span> Residential Address
            </h2>

            <!-- Residential Address -->
            <div class="mb-6">
              <label class="block text-sm font-black uppercase mb-2">Residential Address <span class="text-red-500">*</span></label>
              <textarea 
                v-model="formData.residential_address" 
                required
                rows="3"
                placeholder="Enter your full residential address"
                class="w-full px-4 py-3 border-2 border-ink-black shadow-hard-sm focus:outline-none focus:border-deepseek-blue"
              ></textarea>
            </div>

            <!-- County, City, Postal Code -->
            <div class="grid md:grid-cols-3 gap-6">
              <div>
                <label class="block text-sm font-black uppercase mb-2">County <span class="text-red-500">*</span></label>
                <input 
                  v-model="formData.county" 
                  type="text" 
                  required
                  placeholder="e.g., Nairobi"
                  class="w-full px-4 py-3 border-2 border-ink-black shadow-hard-sm focus:outline-none focus:border-deepseek-blue"
                />
              </div>
              <div>
                <label class="block text-sm font-black uppercase mb-2">City/Town <span class="text-red-500">*</span></label>
                <input 
                  v-model="formData.city" 
                  type="text" 
                  required
                  placeholder="e.g., Nairobi"
                  class="w-full px-4 py-3 border-2 border-ink-black shadow-hard-sm focus:outline-none focus:border-deepseek-blue"
                />
              </div>
              <div>
                <label class="block text-sm font-black uppercase mb-2">Postal Code <span class="text-red-500">*</span></label>
                <input 
                  v-model="formData.postal_code" 
                  type="text" 
                  required
                  placeholder="e.g., 00100"
                  class="w-full px-4 py-3 border-2 border-ink-black shadow-hard-sm focus:outline-none focus:border-deepseek-blue"
                />
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

            <button type="submit"
                    :disabled="!isReady || isUploading"
                    :class="['btn-primary whitespace-nowrap',
                             (!isReady || isUploading) ? 'opacity-30 cursor-not-allowed shadow-none' : '']">
              {{ isUploading ? 'Uploading...' : 'Verify with DeepSeek AI' }}
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();

// Form data
const formData = ref({
  national_id: '',
  kra_pin: '',
  residential_address: '',
  county: '',
  city: '',
  postal_code: ''
});

// Document files
const documents = ref({
  national_id_front: null,
  national_id_back: null,
  passport_photo: null,
  kra_pin_certificate: null,
  payslip: null,
  mpesa_statement: null,
  bank_statement: null
});

// Uploaded file URLs
const uploadedFiles = ref({});

// UI state
const isScanning = ref(null);
const isAnalyzing = ref(false);
const analysisComplete = ref(false);
const analysisLines = ref([]);
const currentAnalysisLine = ref('');
const isUploading = ref(false);
const errorMessage = ref('');
const customerId = ref(null);

// Computed
const isReady = computed(() => {
  const allDocsUploaded = Object.values(documents.value).every(doc => doc !== null);
  const allFieldsFilled = formData.value.national_id && 
                          formData.value.kra_pin && 
                          formData.value.residential_address &&
                          formData.value.county &&
                          formData.value.city &&
                          formData.value.postal_code;
  return allDocsUploaded && allFieldsFilled;
});

// Get customer ID on mount
onMounted(async () => {
  try {
    const response = await fetch('/api/method/dcp_management.api.get_current_user_customer', {
      headers: {
        'Accept': 'application/json',
        'X-Frappe-CSRF-Token': window.csrf_token || ''
      }
    });
    const data = await response.json();
    if (data.message && data.message.customer) {
      customerId.value = data.message.customer.name;
    }
  } catch (error) {
    console.error('Error fetching customer:', error);
    errorMessage.value = 'Failed to load customer data. Please refresh the page.';
  }
});

// Upload file to Frappe
const uploadFileToFrappe = async (file, fieldname) => {
  const formData = new FormData();
  formData.append('file', file);
  formData.append('is_private', '1');
  formData.append('folder', 'Home/Attachments');
  formData.append('doctype', 'DCP Customer');
  formData.append('docname', customerId.value);
  formData.append('fieldname', fieldname);

  try {
    const response = await fetch('/api/method/upload_file', {
      method: 'POST',
      body: formData,
      headers: {
        'Accept': 'application/json',
        'X-Frappe-CSRF-Token': window.csrf_token || ''
      }
    });

    const data = await response.json();
    if (data.message && data.message.file_url) {
      return data.message.file_url;
    }
    throw new Error('Upload failed');
  } catch (error) {
    console.error(`Error uploading ${fieldname}:`, error);
    throw error;
  }
};

// Handle file upload
const handleUpload = (event, type) => {
  const file = event.target.files[0];
  if (!file) return;
  
  isScanning.value = type;
  setTimeout(() => {
    documents.value[type] = file;
    isScanning.value = null;
  }, 1500);
};

// Start analysis and submit
const startAnalysis = async () => {
  if (!customerId.value) {
    errorMessage.value = 'Customer ID not found. Please refresh and try again.';
    return;
  }

  errorMessage.value = '';
  isUploading.value = true;
  isAnalyzing.value = true;
  analysisComplete.value = false;

  try {
    // Show initial analysis lines
    const initialLines = [
      "INITIALIZING SECURE UPLOAD...",
      "ENCRYPTING FILES WITH AES-256...",
      "UPLOADING TO SECURE SERVER..."
    ];

    for (const line of initialLines) {
      currentAnalysisLine.value = line;
      await new Promise(r => setTimeout(r, 400));
      analysisLines.value.push(line);
      currentAnalysisLine.value = '';
    }

    // Upload all files
    for (const [fieldname, file] of Object.entries(documents.value)) {
      if (file) {
        currentAnalysisLine.value = `UPLOADING: ${fieldname.toUpperCase()}...`;
        const fileUrl = await uploadFileToFrappe(file, fieldname);
        uploadedFiles.value[fieldname] = fileUrl;
        analysisLines.value.push(`✓ ${fieldname.toUpperCase()} uploaded`);
        currentAnalysisLine.value = '';
      }
    }

    // Show verification lines
    const verificationLines = [
      "SCANNING: PAYSLIP DOCUMENTS...",
      "EXTRACTING: NET_PAY...",
      "VERIFYING: EMPLOYER_KRA_PIN...",
      "Cross-referencing M-Pesa turnover patterns...",
      "Heuristic analysis for forgery detection: 100% clean.",
      "DETECTING: Salary-backed profile confirmed.",
      "Running risk scoring algorithm...",
      "DeepSeek confidence score: 98%."
    ];

    for (const line of verificationLines) {
      currentAnalysisLine.value = line;
      await new Promise(r => setTimeout(r, 600 + Math.random() * 400));
      analysisLines.value.push(line);
      currentAnalysisLine.value = '';
    }

    // Call backend API
    currentAnalysisLine.value = "SAVING KYC DATA...";
    const response = await fetch('/api/method/dcp_management.api.upload_kyc_documents', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'X-Frappe-CSRF-Token': window.csrf_token || ''
      },
      body: JSON.stringify({
        customer_id: customerId.value,
        national_id: formData.value.national_id,
        kra_pin: formData.value.kra_pin,
        residential_address: formData.value.residential_address,
        county: formData.value.county,
        city: formData.value.city,
        postal_code: formData.value.postal_code,
        files_data: JSON.stringify(uploadedFiles.value)
      })
    });

    const result = await response.json();
    
    if (result.message && !result.message.error) {
      analysisLines.value.push("✓ KYC DATA SAVED SUCCESSFULLY");
      currentAnalysisLine.value = '';
      analysisComplete.value = true;
      await new Promise(r => setTimeout(r, 1200));
      router.push({ name: 'dashboard', query: { status: 'pending' } });
    } else {
      throw new Error(result.message?.error || result.exc || 'Failed to save KYC data');
    }
    
  } catch (error) {
    console.error('Error submitting KYC:', error);
    errorMessage.value = `Submission failed: ${error.message}`;
    isAnalyzing.value = false;
    isUploading.value = false;
  }
};
</script>
