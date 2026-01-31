<template>
  <div class="min-h-screen bg-gradient-to-br from-blue-50 to-green-50 py-12 px-4">
    <div class="max-w-3xl mx-auto">
      <!-- Header -->
      <div class="text-center mb-8">
        <div class="w-20 h-20 bg-green-600 rounded-full flex items-center justify-center mx-auto mb-4">
          <svg class="w-10 h-10 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"></path>
          </svg>
        </div>
        
        <h1 v-if="currentUser?.kyc_status === 'Pending Verification'" class="text-3xl font-bold text-gray-900 mb-2">Complete Your KYC</h1>

        <p v-if="!isKYCSubmitted" class="text-gray-600">Step {{ currentStep }} of 3: {{ stepTitle }}</p>
      </div>

      <!-- KYC Status View -->
      <div v-if="isKYCSubmitted" class="bg-white rounded-2xl shadow-xl p-8">
         <h2 class="text-2xl font-bold text-gray-800 mb-6">KYC Status</h2>
         
         <div class="flex items-center space-x-4 mb-6">
            <span :class="['px-4 py-2 rounded-full font-semibold', statusBadgeClass]">
                {{ currentUser.kyc_status }}
            </span>
         </div>
         
         <div class="bg-blue-50 border border-blue-200 text-blue-800 px-4 py-3 rounded-lg mb-8">
             <p>{{ statusMessage }}</p>
         </div>

         <h3 class="text-lg font-semibold text-gray-700 mb-4">Uploaded Documents</h3>
         <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
             <!-- ID Front -->
             <div class="border rounded-lg p-4 bg-gray-50">
                <p class="text-sm font-medium text-gray-500 mb-2">National ID (Front)</p>
                <a v-if="currentUser.national_id_front" :href="currentUser.national_id_front" target="_blank" class="block">
                    <img v-if="currentUser.national_id_front.match(/\.(jpeg|jpg|gif|png)$/i)" :src="currentUser.national_id_front" class="h-32 w-full object-cover rounded" />
                    <div v-else class="h-32 flex items-center justify-center bg-gray-200 rounded text-gray-500">
                        View Document
                    </div>
                </a>
                <span v-else class="text-red-500 text-sm">Not Uploaded</span>
             </div>
             
             <!-- ID Back -->
             <div class="border rounded-lg p-4 bg-gray-50">
                <p class="text-sm font-medium text-gray-500 mb-2">National ID (Back)</p>
                <a v-if="currentUser.national_id_back" :href="currentUser.national_id_back" target="_blank" class="block">
                     <img v-if="currentUser.national_id_back.match(/\.(jpeg|jpg|gif|png)$/i)" :src="currentUser.national_id_back" class="h-32 w-full object-cover rounded" />
                    <div v-else class="h-32 flex items-center justify-center bg-gray-200 rounded text-gray-500">
                        View Document
                    </div>
                </a>
                 <span v-else class="text-red-500 text-sm">Not Uploaded</span>
             </div>

             <!-- KRA Pin -->
             <div class="border rounded-lg p-4 bg-gray-50">
                <p class="text-sm font-medium text-gray-500 mb-2">KRA PIN Certificate</p>
                <a v-if="currentUser.kra_pin_certificate" :href="currentUser.kra_pin_certificate" target="_blank" class="block">
                     <img v-if="currentUser.kra_pin_certificate.match(/\.(jpeg|jpg|gif|png)$/i)" :src="currentUser.kra_pin_certificate" class="h-32 w-full object-cover rounded" />
                    <div v-else class="h-32 flex items-center justify-center bg-gray-200 rounded text-gray-500">
                         View Document
                    </div>
                </a>
                 <span v-else class="text-red-500 text-sm">Not Uploaded</span>
             </div>

             <!-- Passport Photo -->
             <div class="border rounded-lg p-4 bg-gray-50">
                <p class="text-sm font-medium text-gray-500 mb-2">Passport Photo</p>
                <a v-if="currentUser.passport_photo" :href="currentUser.passport_photo" target="_blank" class="block">
                     <img v-if="currentUser.passport_photo.match(/\.(jpeg|jpg|gif|png)$/i)" :src="currentUser.passport_photo" class="h-32 w-full object-cover rounded" />
                    <div v-else class="h-32 flex items-center justify-center bg-gray-200 rounded text-gray-500">
                         View Document
                    </div>
                </a>
                 <span v-else class="text-red-500 text-sm">Not Uploaded</span>
             </div>
         </div>
         
         <div v-if="currentUser.kyc_status === 'Rejected'" class="mt-8">
             <div class="bg-red-50 p-4 rounded text-red-800 border border-red-200">
                 <p class="font-bold">Reason for Rejection:</p>
                 <p>{{ currentUser.kyc_rejection_reason || 'Please check your email for details or contact support.' }}</p>
             </div>
         </div>
      </div>

      <div v-else>
      <!-- Steps Indicator -->
      <div class="flex justify-between items-center mb-8 px-8">
        <div :class="['h-2 flex-1 rounded-l-full', currentStep >= 1 ? 'bg-green-500' : 'bg-gray-200']"></div>
        <div :class="['h-2 flex-1', currentStep >= 2 ? 'bg-green-500' : 'bg-gray-200']"></div>
        <div :class="['h-2 flex-1 rounded-r-full', currentStep >= 3 ? 'bg-green-500' : 'bg-gray-200']"></div>
      </div>

      <!-- KYC Form Card -->
      <div class="bg-white rounded-2xl shadow-xl p-8">
        <!-- Success Message -->
        <div v-if="uploadSuccess" class="bg-green-50 border border-green-200 text-green-800 px-4 py-3 rounded-lg mb-6">
          <p class="font-medium">✓ KYC Documents Submitted Successfully!</p>
          <p class="text-sm mt-1">Your documents are under verification. You'll be notified once approved.</p>
        </div>

        <!-- Error Message -->
        <div v-if="errorMessage" class="bg-red-50 border border-red-200 text-red-800 px-4 py-3 rounded-lg mb-6">
          <p class="text-sm">{{ errorMessage }}</p>
        </div>

        <form @submit.prevent="submitKYC" class="space-y-6">
          
          <!-- Step 1: Personal Details -->
          <div v-if="currentStep === 1" class="space-y-6">
             <h2 class="text-xl font-semibold mb-4">Personal Identifiers</h2>
             <!-- National ID -->
             <div>
               <label class="block text-sm font-medium text-gray-700 mb-2">National ID Number *</label>
               <input v-model="kycData.national_id" type="text" pattern="[0-9]{8}" maxlength="8" class="form-input w-full px-4 py-3 rounded-lg border border-gray-300" required>
             </div>
             <!-- KRA PIN -->
             <div>
               <label class="block text-sm font-medium text-gray-700 mb-2">KRA PIN *</label>
               <input v-model="kycData.kra_pin" type="text" maxlength="11" class="form-input w-full px-4 py-3 rounded-lg border border-gray-300" placeholder="A123456789Z" required>
             </div>
          </div>

          <!-- Step 2: Address Details -->
          <div v-if="currentStep === 2" class="space-y-6">
            <h2 class="text-xl font-semibold mb-4">Residential Address</h2>
             <!-- Address -->
             <div>
               <label class="block text-sm font-medium text-gray-700 mb-2">Address / Estate *</label>
               <input v-model="kycData.residential_address" type="text" class="form-input w-full px-4 py-3 rounded-lg border border-gray-300" required>
             </div>
             <!-- County -->
             <div>
               <label class="block text-sm font-medium text-gray-700 mb-2">County *</label>
               <input v-model="kycData.county" type="text" class="form-input w-full px-4 py-3 rounded-lg border border-gray-300" required>
             </div>
             <!-- City/Town -->
             <div>
               <label class="block text-sm font-medium text-gray-700 mb-2">City / Town *</label>
               <input v-model="kycData.city" type="text" class="form-input w-full px-4 py-3 rounded-lg border border-gray-300" required>
             </div>
              <!-- Postal Code -->
             <div>
               <label class="block text-sm font-medium text-gray-700 mb-2">Postal Code</label>
               <input v-model="kycData.postal_code" type="text" class="form-input w-full px-4 py-3 rounded-lg border border-gray-300">
             </div>
          </div>

          <!-- Step 3: Document Uploads -->
          <div v-if="currentStep === 3" class="space-y-6">
            <h2 class="text-xl font-semibold mb-4">Upload Documents</h2>
            
            <!-- National ID Front -->
            <FileUploadField label="National ID (Front) *" v-model="files.id_front" :refName="'idFrontInput'" />
            <!-- National ID Back -->
            <FileUploadField label="National ID (Back) *" v-model="files.id_back" :refName="'idBackInput'" />
            <!-- KRA Certificate -->
            <FileUploadField label="KRA PIN Certificate *" v-model="files.kra_certificate" :refName="'kraInput'" accept=".pdf,image/*" />
            <!-- Passport Photo -->
            <FileUploadField label="Passport Photo *" v-model="files.passport_photo" :refName="'ppInput'" />
            <!-- 3-Months Recent Payslip -->
            <FileUploadField label="3-Months Recent Payslip *" v-model="files.payslip" :refName="'payslipInput'" accept=".pdf,image/*" />
            <!-- 2-Months Recent MPesa Statement -->
            <FileUploadField label="2-Months Recent MPesa Statement *" v-model="files.mpesa_statement" :refName="'mpesaInput'" accept=".pdf,image/*" />
            <!-- 2-Months Recent Bank Statement -->
            <FileUploadField label="2-Months Recent Bank Statement *" v-model="files.bank_statement" :refName="'bankInput'" accept=".pdf,image/*" />
            
          </div>

          <!-- Navigation Buttons -->
          <div class="flex justify-between mt-8">
            <button v-if="currentStep > 1" type="button" @click="currentStep--" class="px-6 py-3 border border-gray-300 rounded-lg text-gray-700 hover:bg-gray-50">Back</button>
            <div v-else></div> <!-- Spacer -->
            
            <button v-if="currentStep < 3" type="button" @click="nextStep" class="px-6 py-3 bg-green-600 text-white rounded-lg hover:bg-green-700">Continue</button>
            <button v-else type="submit" :disabled="loading" class="px-6 py-3 bg-green-600 text-white rounded-lg hover:bg-green-700 disabled:opacity-50">
               <span v-if="loading">Submitting...</span>
               <span v-else>Submit Application</span>
            </button>
          </div>

        </form>
      </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { call, auth, api } from '../api'

const router = useRouter()
const currentStep = ref(1)
const loading = ref(false)
const errorMessage = ref('')
const uploadSuccess = ref(false)
const currentUser = ref(null)
const isNewUser = ref(false)

const kycData = reactive({
  national_id: '',
  kra_pin: '',
  residential_address: '',
  county: '',
  city: '',
  postal_code: ''
})

const files = reactive({
  id_front: null,
  id_back: null,
  kra_certificate: null,
  passport_photo: null,
  payslip: null,
  mpesa_statement: null,
  bank_statement: null
})

const stepTitle = computed(() => {
  switch (currentStep.value) {
    case 1: return 'Personal Details'
    case 2: return 'Address Information'
    case 3: return 'Documents'
    default: return ''
  }
})

const isKYCSubmitted = computed(() => {
  if (!currentUser.value) return false;
  const status = currentUser.value.kyc_status;
  // If status exists and is not 'Incomplete', we consider it submitted
  return status && status !== 'Incomplete';
})

const statusBadgeClass = computed(() => {
  if (!currentUser.value) return ''
  const status = currentUser.value.kyc_status
  switch (status) {
    case 'Verified':
      return 'bg-green-100 text-green-800'
    case 'Rejected':
      return 'bg-red-100 text-red-800'
    case 'Pending Verification':
      return 'bg-yellow-100 text-yellow-800'
    default:
      return 'bg-gray-100 text-gray-800'
  }
})

const statusMessage = computed(() => {
  if (!currentUser.value) return ''
  const status = currentUser.value.kyc_status
  switch (status) {
    case 'Verified':
      return 'Your KYC documents have been verified successfully.'
    case 'Rejected':
      return 'Your KYC documents were rejected. Please contact support or re-submit.'
    case 'Pending Verification':
      return 'Your documents are currently under review. This usually takes 24-48 hours.'
    default:
      return ''
  }
})

// File Handler Component Logic inline for simplicity or imported
const handleFileUpload = (event, key) => {
  const file = event.target.files[0]
  if (file) {
    // Basic validation
    if (file.size > 5 * 1024 * 1024) {
      alert('File is too large. Max 5MB allowed.')
      return
    }
    files[key] = file
  }
}

const nextStep = () => {
  // Validate current step
  if (currentStep.value === 1) {
    if (!kycData.national_id || !kycData.kra_pin) {
      errorMessage.value = "Please fill in all required fields."
      return
    }
  }
  if (currentStep.value === 2) {
    if (!kycData.residential_address || !kycData.county || !kycData.city) {
       errorMessage.value = "Please fill in all required fields."
       return
    }
  }
  errorMessage.value = ""
  currentStep.value++
}

const submitKYC = async () => {
    // Validate Step 3
    if (!files.id_front || !files.id_back || !files.kra_certificate || !files.passport_photo || !files.payslip || !files.mpesa_statement || !files.bank_statement) {
      errorMessage.value = "Please upload all required documents."
      return
    }

    if (!currentUser.value) {
        errorMessage.value = "User session expired. Please refresh or login again."
        return
    }
    
    loading.value = true
    errorMessage.value = ''

    try {
        // 1. Upload Files
        const fileUploads = {}
        const keys = ['id_front', 'id_back', 'kra_certificate', 'passport_photo', 'payslip', 'mpesa_statement', 'bank_statement']
        
        for (const key of keys) {
            const formData = new FormData()
            formData.append('file', files[key])
            formData.append('doctype', 'DCP Customer')
            formData.append('docname', currentUser.value.name) // Use .name as ID
            formData.append('fieldname', mapFieldToDocField(key))
            formData.append('is_private', 1)

            const res = await api.upload('/api/method/dcp_management.api.upload_kyc_file', formData)
            if (res.message && res.message.file_url) {
                 fileUploads[key] = res.message.file_url
            } else {
                 throw new Error(`Failed to upload ${key}`)
            }
        }

        // 2. Submit Data
        const payload = {
            customer_id: currentUser.value.name, // Use .name as ID
            national_id: kycData.national_id,
            kra_pin: kycData.kra_pin,
            residential_address: kycData.residential_address,
            county: kycData.county,
            city: kycData.city,
            postal_code: kycData.postal_code,
            files_data: fileUploads // Passing URLs
        }

        console.log('=== KYC Submission Debug ===');
        console.log('Payload:', payload);
        
        const res = await call.post('dcp_management.api.upload_kyc_documents', payload)
        
        if (res.message) {
            uploadSuccess.value = true
            // Reload user data to update view
            await loadUserData();
        } else if (res.error) {
            throw new Error(res.error)
        }
    } catch (e) {
        console.error(e)
        errorMessage.value = e.message || 'An error occurred during submission.'
    } finally {
        loading.value = false
    }
}

const mapFieldToDocField = (key) => {
    const map = {
        'id_front': 'national_id_front',
        'id_back': 'national_id_back',
        'kra_certificate': 'kra_pin_certificate',
        'passport_photo': 'passport_photo',
        'payslip': 'payslip',
        'mpesa_statement': 'mpesa_statement',
        'bank_statement': 'bank_statement'
    }
    return map[key]
}

const loadUserData = async () => {
    try {
        const user = await auth.getLoggedInUser()
        
        if (user && user !== 'Guest') {
            // Get customer record using whitelisted API
            const res = await call.get('dcp_management.api.get_current_user_customer');
            
            let customerName = null;
            if (res && res.customer) {
                 customerName = res.customer.name
            } else if (res?.message?.customer) {
                 customerName = res.message.customer.name
            } 
            
            if (customerName) {
                // Fetch full document using standard REST API
                const docRes = await fetch(`/api/resource/DCP Customer/${customerName}`);
                const docData = await docRes.json();
                
                if (docData && docData.data) {
                    currentUser.value = docData.data;
                } else {
                    errorMessage.value = "Failed to fetch full customer profile."
                }
            } else {
                errorMessage.value = res?.error || res?.message?.error || "Customer record not found"
            }
        }
    } catch (e) {
        console.error("Failed to load customer data", e)
        errorMessage.value = "Failed to load your profile. Please refresh the page."
    }
}

onMounted(async () => {
  // Check for new_user query param
  if (router.currentRoute.value.query.new_user) {
    isNewUser.value = true
  }
  await loadUserData();
})
</script>

<script>
// Simple child component for file input (can be extracted)
import { h } from 'vue'
const FileUploadField = {
  props: ['label', 'modelValue', 'refName', 'accept'],
  emits: ['update:modelValue'],
  render() {
    return h('div', [
      h('label', { class: 'block text-sm font-medium text-gray-700 mb-2' }, this.label),
      h('div', { class: 'border-2 border-dashed border-gray-300 rounded-lg p-6 text-center hover:border-green-500 transition' }, [
         h('input', {
            type: 'file',
            ref: 'input',
            class: 'hidden',
             accept: this.accept || 'image/*',
            onChange: (e) => this.$emit('update:modelValue', e.target.files[0])
         }),
         h('button', {
            type: 'button',
             class: 'text-green-600 hover:text-green-700',
             onClick: () => this.$refs.input.click()
         }, [
            this.modelValue ? `✓ ${this.modelValue.name}` : 'Click to Upload'
         ])
      ])
    ])
  }
}
export default {
    components: {FileUploadField}
}
</script>
