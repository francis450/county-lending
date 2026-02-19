import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import { auth } from '../api'

const router = createRouter({
  history: createWebHashHistory(),
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) return savedPosition
    return { top: 0 }
  },
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/services',
      name: 'services',
      component: () => import('../views/ServicesView.vue')
    },
    {
      path: '/eligibility',
      name: 'eligibility',
      component: () => import('../views/EligibilityView.vue')
    },
    {
      path: '/how-to-apply',
      name: 'how-to-apply',
      component: () => import('../views/HowToApplyView.vue')
    },
    {
      path: '/faq',
      name: 'faq',
      component: () => import('../views/FAQView.vue')
    },
    {
      path: '/blog',
      name: 'blog',
      component: () => import('../views/BlogView.vue')
    },
    {
      path: '/contact',
      name: 'contact',
      component: () => import('../views/ContactView.vue')
    },
    {
      path: '/privacy',
      name: 'privacy',
      component: () => import('../views/PrivacyView.vue')
    },
    {
      path: '/terms',
      name: 'terms',
      component: () => import('../views/TermsView.vue')
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      component: () => import('../views/DashboardView.vue'),
      meta: { requiresAuth: true }
    },
    {
      path: '/kyc',
      name: 'kyc',
      component: () => import('../views/KYCUploadView.vue'),
      meta: { requiresAuth: true }
    },
    {
      path: '/profile',
      name: 'profile',
      component: () => import('../views/CustomerProfileView.vue'),
      meta: { requiresAuth: true }
    },
    {
      path: '/apply',
      name: 'apply',
      component: () => import('../views/LoanApplicationView.vue'),
      meta: { requiresAuth: true }
    },
    {
      path: '/onboard',
      name: 'onboard',
      component: () => import('../views/OnboardingView.vue')
    },
    {
      path: '/check-email',
      name: 'check-email',
      component: () => import('../views/CheckEmailView.vue')
    },
    {
      path: '/admin',
      name: 'admin',
      component: () => import('../views/AdminReviewView.vue'),
      meta: { requiresAuth: true }
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/LoginView.vue')
    }
  ]
})

// Navigation guard to check authentication
router.beforeEach(async (to, from, next) => {
  // Check if route requires authentication
  if (to.meta.requiresAuth) {
    try {
      const user = await auth.getLoggedInUser()
      if (user && user !== 'Guest') {
        // User is authenticated
        next()
      } else {
        // User is not authenticated, redirect to login
        next('/login')
      }
    } catch (error) {
      // 403 or other auth errors mean user is not logged in
      // This is expected for unauthenticated users, not an error
      if (error.httpStatus === 403 || error.httpStatus === 401) {
        next('/login')
      } else {
        console.error('Auth check failed:', error)
        next('/login')
      }
    }
  } else {
    // Route doesn't require auth
    next()
  }
})

export default router
