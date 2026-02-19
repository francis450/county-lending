<template>
  <div class="min-h-screen bg-white py-12 px-4 font-inter text-ink-black">
    <div class="max-w-4xl mx-auto">

      <!-- Loading State -->
      <div v-if="loading" class="flex items-center justify-center py-20">
        <div class="w-16 h-16 rounded-full border-4 border-deepseek-blue border-t-transparent animate-spin"></div>
      </div>

      <!-- Main Profile Content -->
      <div v-else-if="customer">
        <!-- Header -->
        <div class="mb-12">
          <h1 class="text-4xl font-black uppercase tracking-tight mb-2">
            My <span class="text-deepseek-blue">Profile</span>
          </h1>
          <p class="text-ink-black/50 text-sm">View your KYC verification status and manage your information</p>
        </div>

        <!-- KYC Status Card -->
        <div class="mb-8 p-8 border-2 border-ink-black shadow-hard-md">
          <div class="flex flex-col md:flex-row md:items-center justify-between gap-6 mb-6">
            <div>
              <h2 class="text-2xl font-black uppercase mb-2">KYC Verification Status</h2>
              <p class="text-ink-black/60 text-sm">Your application status for digital lending services</p>
            </div>
            <div>
              <span :class="getStatusBadgeClass(customer.kyc_status)" class="inline-block px-6 py-3 text-sm font-black uppercase tracking-wider">
                {{ customer.kyc_status }}
              </span>
            </div>
          </div>

          <!-- Status Description -->
          <div class="p-4 bg-vapor-grey border-l-4" :class="getStatusBorderClass(customer.kyc_status)">
            <p class="text-sm">{{ getStatusDescription(customer.kyc_status) }}</p>
          </div>
        </div>

        <!-- Personal Information -->
        <div class="mb-8 p-8 border-2 border-ink-black bg-vapor-grey/30">
          <h2 class="text-2xl font-black uppercase mb-6 flex items-center gap-3">
            <span class="text-deepseek-blue">01</span> Personal Information
          </h2>
          
          <div class="grid md:grid-cols-2 gap-6">
            <div>
              <label class="block text-xs font-black uppercase text-ink-black/60 mb-1">First Name</label>
              <p class="text-lg font-bold">{{ customer.first_name }}</p>
            </div>
            <div>
              <label class="block text-xs font-black uppercase text-ink-black/60 mb-1">Last Name</label>
              <p class="text-lg font-bold">{{ customer.last_name }}</p>
            </div>
            <div>
              <label class="block text-xs font-black uppercase text-ink-black/60 mb-1">Email</label>
              <p class="text-lg">{{ customer.email }}</p>
            </div>
            <div>
              <label class="block text-xs font-black uppercase text-ink-black/60 mb-1">Phone</label>
              <p class="text-lg">{{ customer.phone }}</p>
            </div>
          </div>
        </div>

        <!-- KYC Documents Checklist -->
        <div class="mb-8 p-8 border-2 border-ink-black bg-vapor-grey/30">
          <h2 class="text-2xl font-black uppercase mb-6 flex items-center gap-3">
            <span class="text-deepseek-blue">02</span> KYC Documents
          </h2>

          <div class="space-y-4">
            <!-- Identity Documents -->
            <div>
              <h3 class="text-sm font-black uppercase mb-3 text-ink-black/80">Identity Documents</h3>
              <div class="space-y-2">
                <DocumentCheckItem label="National ID Number" :completed="!!customer.national_id" />
                <DocumentCheckItem label="National ID (Front)" :completed="!!customer.national_id_front" />
                <DocumentCheckItem label="National ID (Back)" :completed="!!customer.national_id_back" />
                <DocumentCheckItem label="Passport Photo" :completed="!!customer.passport_photo" />
              </div>
            </div>

            <!-- Tax Documents -->
            <div>
              <h3 class="text-sm font-black uppercase mb-3 text-ink-black/80">Tax Documents</h3>
              <div class="space-y-2">
                <DocumentCheckItem label="KRA PIN" :completed="!!customer.kra_pin" />
                <DocumentCheckItem label="KRA PIN Certificate" :completed="!!customer.kra_pin_certificate" />
              </div>
            </div>

            <!-- Financial Documents -->
            <div>
              <h3 class="text-sm font-black uppercase mb-3 text-ink-black/80">Financial Documents</h3>
              <div class="space-y-2">
                <DocumentCheckItem label="Payslips (3 Months)" :completed="!!customer.payslip" />
                <DocumentCheckItem label="M-Pesa Statement (2 Months)" :completed="!!customer.mpesa_statement" />
                <DocumentCheckItem label="Bank Statement (2 Months)" :completed="!!customer.bank_statement" />
              </div>
            </div>

            <!-- Address Information -->
            <div>
              <h3 class="text-sm font-black uppercase mb-3 text-ink-black/80">Address Information</h3>
              <div class="space-y-2">
                <DocumentCheckItem label="Residential Address" :completed="!!customer.residential_address" />
                <DocumentCheckItem label="County" :completed="!!customer.county" />
                <DocumentCheckItem label="City/Town" :completed="!!customer.city" />
                <DocumentCheckItem label="Postal Code" :completed="!!customer.postal_code" />
              </div>
            </div>
          </div>

          <!-- Completion Stats -->
          <div class="mt-8 p-4 border-2 border-ink-black bg-white">
            <div class="flex items-center justify-between mb-2">
              <span class="text-sm font-black uppercase">Completion</span>
              <span class="text-sm font-black">{{ completionPercentage }}%</span>
            </div>
            <div class="w-full h-3 bg-vapor-grey border border-ink-black/20">
              <div class="h-full bg-watch-green transition-all duration-500" :style="{ width: completionPercentage + '%' }"></div>
            </div>
          </div>
        </div>

        <!-- Address Details -->
        <div v-if="customer.residential_address" class="mb-8 p-8 border-2 border-ink-black bg-vapor-grey/30">
          <h2 class="text-2xl font-black uppercase mb-6 flex items-center gap-3">
            <span class="text-deepseek-blue">03</span> Residential Address
          </h2>
          
          <div class="space-y-4">
            <div>
              <label class="block text-xs font-black uppercase text-ink-black/60 mb-1">Address</label>
              <p class="text-base">{{ customer.residential_address }}</p>
            </div>
            <div class="grid md:grid-cols-3 gap-4">
              <div>
                <label class="block text-xs font-black uppercase text-ink-black/60 mb-1">County</label>
                <p class="text-base">{{ customer.county || 'Not provided' }}</p>
              </div>
              <div>
                <label class="block text-xs font-black uppercase text-ink-black/60 mb-1">City/Town</label>
                <p class="text-base">{{ customer.city || 'Not provided' }}</p>
              </div>
              <div>
                <label class="block text-xs font-black uppercase text-ink-black/60 mb-1">Postal Code</label>
                <p class="text-base">{{ customer.postal_code || 'Not provided' }}</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Verification Info -->
        <div v-if="customer.kyc_status === 'Verified' && customer.kyc_verified_date" class="mb-8 p-6 border-2 border-watch-green bg-watch-green/10">
          <div class="flex items-start gap-4">
            <svg class="w-8 h-8 text-watch-green flex-shrink-0" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
            </svg>
            <div>
              <h3 class="font-black uppercase mb-1">Verified Account</h3>
              <p class="text-sm text-ink-black/70">Your account was verified on {{ formatDate(customer.kyc_verified_date) }}</p>
              <p v-if="customer.verified_by" class="text-xs text-ink-black/50 mt-1">Verified by: {{ customer.verified_by }}</p>
            </div>
          </div>
        </div>

        <!-- Action Buttons -->
        <div class="flex flex-col sm:flex-row gap-4">
          <button 
            @click="goToKYCUpdate" 
            class="flex-1 px-8 py-4 border-2 border-ink-black bg-white font-black uppercase text-sm shadow-hard-sm hover:shadow-hard-md transition-all active:shadow-none active:translate-x-[3px] active:translate-y-[3px]"
          >
            Update KYC Documents
          </button>
          <button 
            @click="goToDashboard" 
            class="flex-1 px-8 py-4 border-2 border-ink-black bg-vapor-grey font-black uppercase text-sm shadow-hard-sm hover:shadow-hard-md transition-all active:shadow-none active:translate-x-[3px] active:translate-y-[3px]"
          >
            Back to Dashboard
          </button>
        </div>

        <!-- ODPC Notice -->
        <div class="mt-8 p-4 bg-vapor-grey border-l-4 border-deepseek-blue">
          <div class="flex items-start gap-3">
            <svg class="w-5 h-5 text-deepseek-blue flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"></path>
            </svg>
            <div class="text-xs text-ink-black/70">
              <p class="font-bold mb-1">Data Protection Notice</p>
              <p>Your personal information is encrypted and stored securely in compliance with the Kenya Data Protection Act, 2019. We only share your data with authorized credit reference bureaus and regulatory authorities as required by law.</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Error State -->
      <div v-else class="text-center py-20">
        <p class="text-ink-black/60">Unable to load profile. Please try again later.</p>
      </div>

    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const customer = ref(null);
const loading = ref(true);

// Fetch customer profile
onMounted(async () => {
  try {
    const response = await fetch('/api/method/dcp_management.api.get_customer_profile', {
      headers: {
        'Accept': 'application/json',
        'X-Frappe-CSRF-Token': window.csrf_token || ''
      }
    });
    const data = await response.json();
    if (data.message) {
      customer.value = data.message;
    }
  } catch (error) {
    console.error('Error fetching customer profile:', error);
  } finally {
    loading.value = false;
  }
});

// Computed properties
const completionPercentage = computed(() => {
  if (!customer.value) return 0;
  
  const fields = [
    customer.value.national_id,
    customer.value.national_id_front,
    customer.value.national_id_back,
    customer.value.passport_photo,
    customer.value.kra_pin,
    customer.value.kra_pin_certificate,
    customer.value.payslip,
    customer.value.mpesa_statement,
    customer.value.bank_statement,
    customer.value.residential_address,
    customer.value.county,
    customer.value.city,
    customer.value.postal_code
  ];
  
  const completed = fields.filter(f => f).length;
  return Math.round((completed / fields.length) * 100);
});

// Methods
const getStatusBadgeClass = (status) => {
  const baseClasses = 'border-2 shadow-hard-sm';
  switch (status) {
    case 'Verified':
      return `${baseClasses} border-watch-green bg-watch-green text-ink-black`;
    case 'Pending Verification':
      return `${baseClasses} border-deepseek-blue bg-deepseek-blue text-white`;
    case 'Incomplete':
      return `${baseClasses} border-ink-black/30 bg-vapor-grey text-ink-black`;
    case 'Rejected':
      return `${baseClasses} border-red-500 bg-red-500 text-white`;
    default:
      return `${baseClasses} border-ink-black bg-white text-ink-black`;
  }
};

const getStatusBorderClass = (status) => {
  switch (status) {
    case 'Verified':
      return 'border-watch-green';
    case 'Pending Verification':
      return 'border-deepseek-blue';
    case 'Incomplete':
      return 'border-ink-black/30';
    case 'Rejected':
      return 'border-red-500';
    default:
      return 'border-ink-black';
  }
};

const getStatusDescription = (status) => {
  switch (status) {
    case 'Verified':
      return 'Your KYC verification is complete. You can now apply for loans and access all services.';
    case 'Pending Verification':
      return 'Your documents have been submitted and are currently under review. This typically takes 24-48 hours.';
    case 'Incomplete':
      return 'Please complete all required KYC documents to proceed with loan applications.';
    case 'Rejected':
      return 'Your KYC submission was rejected. Please update your documents and resubmit.';
    default:
      return 'Unknown status';
  }
};

const formatDate = (dateString) => {
  if (!dateString) return '';
  const date = new Date(dateString);
  return date.toLocaleDateString('en-KE', { 
    year: 'numeric', 
    month: 'long', 
    day: 'numeric' 
  });
};

const goToKYCUpdate = () => {
  router.push({ name: 'kyc' });
};

const goToDashboard = () => {
  router.push({ name: 'dashboard' });
};
</script>

<script>
// DocumentCheckItem Component
export default {
  components: {
    DocumentCheckItem: {
      props: {
        label: String,
        completed: Boolean
      },
      template: `
        <div class="flex items-center gap-3 p-3 bg-white border border-ink-black/10">
          <div :class="['w-5 h-5 border-2 flex items-center justify-center flex-shrink-0', completed ? 'border-watch-green bg-watch-green' : 'border-ink-black/30']">
            <svg v-if="completed" class="w-3 h-3 text-ink-black" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"></path>
            </svg>
          </div>
          <span class="text-sm" :class="completed ? 'font-bold' : 'text-ink-black/60'">{{ label }}</span>
        </div>
      `
    }
  }
};
</script>
