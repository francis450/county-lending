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
        <h1 class="text-3xl font-bold text-gray-900 mb-2">Complete Your KYC</h1>
        <p class="text-gray-600">Step {{ currentStep }} of 3: {{ stepTitle }}</p>
      </div>

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
  passport_photo: null
})

const stepTitle = computed(() => {
  switch (currentStep.value) {
    case 1: return 'Personal Details'
    case 2: return 'Address Information'
    case 3: return 'Documents'
    default: return ''
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
    if (!files.id_front || !files.id_back || !files.kra_certificate || !files.passport_photo) {
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
        const keys = ['id_front', 'id_back', 'kra_certificate', 'passport_photo']
        
        for (const key of keys) {
            const formData = new FormData()
            formData.append('file', files[key])
            formData.append('doctype', 'DCP Customer')
            formData.append('docname', currentUser.value.customer_id)
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
            customer_id: currentUser.value.customer_id,
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
        console.log('File Uploads:', fileUploads);
        
        const res = await call.post('dcp_management.api.upload_kyc_documents', payload)
        
        console.log('API Response:', res);
        console.log('res.message:', res?.message);
        console.log('res.error:', res?.error);
        console.log('==============================');
        
        if (res.message) {
            uploadSuccess.value = true
            setTimeout(() => {
                router.push('/')
            }, 2000)
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
        'passport_photo': 'passport_photo'
    }
    return map[key]
}

onMounted(async () => {
  // Check for new_user query param
  if (router.currentRoute.value.query.new_user) {
    isNewUser.value = true
  }

  // Auth is already checked by router guard, just get user data
  try {
    const user = await auth.getLoggedInUser()
    
    if (user && user !== 'Guest') {
        // Get customer record using whitelisted API
        const res = await call.get('dcp_management.api.get_current_user_customer');
        
        // DEBUG: Log the response structure
        console.log('=== KYC API Response Debug ===');
        console.log('Full response:', res);
        console.log('res.customer:', res?.customer);
        console.log('res.message:', res?.message);
        console.log('res.message?.customer:', res?.message?.customer);
        console.log('==============================');
        
        if (res && res.customer) {
             currentUser.value = { ...user, customer_id: res.customer.name }
        } else if (res?.message?.customer) {
             currentUser.value = { ...user, customer_id: res.message.customer.name }
        } else {
            errorMessage.value = res?.error || res?.message?.error || "Customer record not found"
        }
    }
  } catch (e) {
    console.error("Failed to load customer data", e)
    errorMessage.value = "Failed to load your profile. Please refresh the page."
  }
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
