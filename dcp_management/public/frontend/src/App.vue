<template>
  <div class="min-h-screen bg-white font-inter text-ink-black flex flex-col">
    <!-- Header Navigation -->
    <header v-if="!isFullPageRoute" class="bg-white border-b border-gray-100 sticky top-0 z-50 shadow-sm">
      <nav class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between items-center h-20">
          <!-- Logo -->
          <RouterLink to="/" class="flex items-center group">
            <span class="text-2xl font-black text-ink-black uppercase tracking-tighter">Jirani</span>
            <span class="text-watch-green ml-1 text-2xl font-black uppercase tracking-tighter">Credit</span>
            <span class="hidden sm:block ml-3 text-[9px] text-soft-grey uppercase tracking-widest font-semibold border-l border-gray-200 pl-3">Your Neighbor in<br/>Financial Growth</span>
          </RouterLink>

          <!-- Desktop Navigation -->
          <div class="hidden lg:flex items-center space-x-8">
            <RouterLink to="/" class="nav-link" :class="{'nav-link-active': route.path === '/'}">Home</RouterLink>
            <RouterLink to="/about" class="nav-link" :class="{'nav-link-active': route.path === '/about'}">About</RouterLink>

            <!-- Services Dropdown -->
            <div class="relative" @mouseenter="servicesOpen = true" @mouseleave="servicesOpen = false">
              <RouterLink to="/services" class="nav-link flex items-center gap-1" :class="{'nav-link-active': route.path === '/services'}">
                Services
                <svg class="w-3 h-3 transition-transform" :class="{'rotate-180': servicesOpen}" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M19.5 8.25l-7.5 7.5-7.5-7.5"/></svg>
              </RouterLink>
              <transition name="fade">
                <div v-if="servicesOpen" class="absolute top-full left-0 mt-2 w-56 bg-white border border-gray-100 shadow-card-hover rounded-xl py-2 z-50">
                  <RouterLink to="/services" class="block px-4 py-3 text-sm hover:bg-trust-green-light hover:text-trust-green transition-colors">All Services</RouterLink>
                  <RouterLink to="/eligibility" class="block px-4 py-3 text-sm hover:bg-trust-green-light hover:text-trust-green transition-colors">Eligibility</RouterLink>
                  <RouterLink to="/how-to-apply" class="block px-4 py-3 text-sm hover:bg-trust-green-light hover:text-trust-green transition-colors">How to Apply</RouterLink>
                </div>
              </transition>
            </div>

            <RouterLink to="/faq" class="nav-link" :class="{'nav-link-active': route.path === '/faq'}">FAQ</RouterLink>
            <RouterLink to="/blog" class="nav-link" :class="{'nav-link-active': route.path === '/blog'}">Blog</RouterLink>
            <RouterLink to="/contact" class="nav-link" :class="{'nav-link-active': route.path === '/contact'}">Contact</RouterLink>
          </div>

          <!-- Right Actions -->
          <div class="hidden lg:flex items-center gap-4">
            <!-- Language Toggle -->
            <button @click="toggleLang" class="text-[10px] font-bold uppercase tracking-widest text-soft-grey hover:text-ink-black transition-colors px-2 py-1 border border-gray-200 rounded">
              {{ currentLang === 'en' ? 'SW' : 'EN' }}
            </button>

            <template v-if="customerStore.isLoggedIn">
              <RouterLink to="/dashboard" class="nav-link" :class="{'nav-link-active': route.path === '/dashboard'}">Dashboard</RouterLink>
              <RouterLink to="/profile" class="nav-link" :class="{'nav-link-active': route.path === '/profile'}">My Profile</RouterLink>
              <button @click="handleLogout"
                class="text-soft-grey hover:text-alert-magenta text-xs font-bold uppercase tracking-widest transition">
                Logout
              </button>
            </template>
            <template v-else>
              <RouterLink to="/login" class="text-ink-black hover:text-trust-green text-xs font-bold uppercase tracking-widest transition">
                Login
              </RouterLink>
              <RouterLink to="/apply"
                class="bg-watch-green text-ink-black px-6 py-3 font-black text-xs uppercase tracking-[0.15em] shadow-hard-sm hover:shadow-hard-md active:shadow-none active:translate-x-[3px] active:translate-y-[3px] transition-all duration-150">
                Apply Now
              </RouterLink>
            </template>
          </div>

          <!-- Mobile Menu Button -->
          <button @click="mobileMenuOpen = !mobileMenuOpen" class="lg:hidden p-2 text-ink-black">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24">
              <path v-if="!mobileMenuOpen" stroke-linecap="round" stroke-linejoin="round" d="M4 6h16M4 12h16M4 18h16"></path>
              <path v-else stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12"></path>
            </svg>
          </button>
        </div>

        <!-- Mobile Menu -->
        <transition name="fade">
          <div v-if="mobileMenuOpen" class="lg:hidden py-6 border-t border-gray-100 bg-white">
            <div class="flex flex-col space-y-1 px-2">
              <RouterLink @click="mobileMenuOpen = false" to="/" class="mobile-nav-link">Home</RouterLink>
              <RouterLink @click="mobileMenuOpen = false" to="/about" class="mobile-nav-link">About Us</RouterLink>
              <RouterLink @click="mobileMenuOpen = false" to="/services" class="mobile-nav-link">Services</RouterLink>
              <RouterLink @click="mobileMenuOpen = false" to="/eligibility" class="mobile-nav-link">Eligibility</RouterLink>
              <RouterLink @click="mobileMenuOpen = false" to="/how-to-apply" class="mobile-nav-link">How to Apply</RouterLink>
              <RouterLink @click="mobileMenuOpen = false" to="/faq" class="mobile-nav-link">FAQ</RouterLink>
              <RouterLink @click="mobileMenuOpen = false" to="/blog" class="mobile-nav-link">Blog</RouterLink>
              <RouterLink @click="mobileMenuOpen = false" to="/contact" class="mobile-nav-link">Contact Us</RouterLink>

              <div class="pt-4 mt-4 border-t border-gray-100">
                <template v-if="customerStore.isLoggedIn">
                  <RouterLink @click="mobileMenuOpen = false" to="/dashboard" class="mobile-nav-link font-bold">Dashboard</RouterLink>
                  <RouterLink @click="mobileMenuOpen = false" to="/profile" class="mobile-nav-link font-bold">My Profile</RouterLink>
                  <button @click="handleLogout(); mobileMenuOpen = false"
                    class="w-full text-left px-4 py-3 text-alert-magenta text-sm font-bold">
                    Logout
                  </button>
                </template>
                <template v-else>
                  <RouterLink @click="mobileMenuOpen = false" to="/login" class="mobile-nav-link">Login</RouterLink>
                  <RouterLink @click="mobileMenuOpen = false" to="/apply"
                    class="btn-primary text-center block mx-4 mt-3">
                    Apply Now
                  </RouterLink>
                </template>
              </div>

              <!-- Mobile Language Toggle -->
              <div class="px-4 pt-4">
                <button @click="toggleLang" class="text-xs font-bold uppercase tracking-widest text-soft-grey border border-gray-200 rounded px-3 py-2">
                  {{ currentLang === 'en' ? 'Swahili' : 'English' }}
                </button>
              </div>
            </div>
          </div>
        </transition>
      </nav>
    </header>

    <!-- Main Content -->
    <main class="flex-1">
      <RouterView v-slot="{ Component }">
        <transition name="fade" mode="out-in">
          <component :is="Component" />
        </transition>
      </RouterView>
    </main>

    <!-- Footer -->
    <SiteFooter v-if="!isFullPageRoute" />
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import { RouterLink, RouterView, useRoute, useRouter } from 'vue-router';
import { useCustomerStore } from './stores/customer';
import { auth } from './api';
import SiteFooter from './components/SiteFooter.vue';

const mobileMenuOpen = ref(false);
const servicesOpen = ref(false);
const currentLang = ref('en');
const route = useRoute();
const router = useRouter();
const customerStore = useCustomerStore();

const isFullPageRoute = computed(() => {
  const routes = ['/onboard', '/login', '/kyc', '/check-email'];
  return routes.includes(route.path);
});

const toggleLang = () => {
  currentLang.value = currentLang.value === 'en' ? 'sw' : 'en';
};

const handleLogout = async () => {
  try {
    await auth.logout();
  } catch (e) {
    console.error('Logout failed', e);
  }
  customerStore.logout();
  router.push('/');
};

// Close mobile menu on route change
router.afterEach(() => {
  mobileMenuOpen.value = false;
  servicesOpen.value = false;
});
</script>

<style>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

/* Nav link styles */
.nav-link {
  @apply text-soft-grey hover:text-ink-black text-xs font-bold uppercase tracking-[0.12em] transition-colors relative py-1;
}
.nav-link-active {
  @apply text-ink-black;
}
.nav-link-active::after {
  content: '';
  @apply absolute bottom-0 left-0 right-0 h-0.5 bg-watch-green;
}
.mobile-nav-link {
  @apply block px-4 py-3 text-ink-black/70 hover:text-ink-black hover:bg-light-grey text-sm font-semibold rounded-lg transition-colors;
}
</style>
