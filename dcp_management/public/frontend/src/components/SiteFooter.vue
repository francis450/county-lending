<template>
  <footer class="bg-ink-black text-white">
    <!-- Main Footer -->
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12">
        <!-- Brand -->
        <div class="lg:col-span-1">
          <RouterLink to="/" class="flex items-center mb-4">
            <span class="text-2xl font-black uppercase tracking-tighter">Jirani</span>
            <span class="text-watch-green ml-1 text-2xl font-black uppercase tracking-tighter">Credit</span>
          </RouterLink>
          <p class="text-white/50 text-sm leading-relaxed mb-6">
            Your Neighbor in Financial Growth. Empowering Kenya's workforce with fast, transparent digital credit.
          </p>
          <!-- Social Links -->
          <div class="flex gap-4">
            <a href="https://twitter.com/jiranicredit" target="_blank" rel="noopener"
               class="w-10 h-10 border border-white/20 flex items-center justify-center hover:bg-watch-green hover:border-watch-green hover:text-ink-black transition-all">
              <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg>
            </a>
            <a href="https://facebook.com/jiranicredit" target="_blank" rel="noopener"
               class="w-10 h-10 border border-white/20 flex items-center justify-center hover:bg-watch-green hover:border-watch-green hover:text-ink-black transition-all">
              <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>
            </a>
            <a href="https://linkedin.com/company/jiranicredit" target="_blank" rel="noopener"
               class="w-10 h-10 border border-white/20 flex items-center justify-center hover:bg-watch-green hover:border-watch-green hover:text-ink-black transition-all">
              <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
            </a>
          </div>
        </div>

        <!-- Quick Links -->
        <div>
          <h4 class="text-xs font-black uppercase tracking-[0.2em] mb-6 text-watch-green">Quick Links</h4>
          <ul class="space-y-3">
            <li><RouterLink to="/about" class="text-white/60 hover:text-white text-sm transition-colors">About Us</RouterLink></li>
            <li><RouterLink to="/services" class="text-white/60 hover:text-white text-sm transition-colors">Our Services</RouterLink></li>
            <li><RouterLink to="/eligibility" class="text-white/60 hover:text-white text-sm transition-colors">Eligibility</RouterLink></li>
            <li><RouterLink to="/how-to-apply" class="text-white/60 hover:text-white text-sm transition-colors">How to Apply</RouterLink></li>
            <li><RouterLink to="/faq" class="text-white/60 hover:text-white text-sm transition-colors">FAQ</RouterLink></li>
            <li><RouterLink to="/blog" class="text-white/60 hover:text-white text-sm transition-colors">Blog</RouterLink></li>
          </ul>
        </div>

        <!-- Legal -->
        <div>
          <h4 class="text-xs font-black uppercase tracking-[0.2em] mb-6 text-watch-green">Legal</h4>
          <ul class="space-y-3">
            <li><RouterLink to="/privacy" class="text-white/60 hover:text-white text-sm transition-colors">Privacy Policy</RouterLink></li>
            <li><RouterLink to="/terms" class="text-white/60 hover:text-white text-sm transition-colors">Terms &amp; Conditions</RouterLink></li>
            <li><RouterLink to="/contact" class="text-white/60 hover:text-white text-sm transition-colors">Contact Us</RouterLink></li>
          </ul>
          <!-- Trust Badges -->
          <div class="mt-8 space-y-3">
            <div class="flex items-center gap-2 text-white/40 text-xs">
              <svg class="w-4 h-4 text-watch-green" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75m-3-7.036A11.959 11.959 0 013.598 6 11.99 11.99 0 003 9.749c0 5.592 3.824 10.29 9 11.623 5.176-1.332 9-6.03 9-11.622 0-1.31-.21-2.571-.598-3.751h-.152c-3.196 0-6.1-1.248-8.25-3.285z"/></svg>
              Licensed by CBK
            </div>
            <div class="flex items-center gap-2 text-white/40 text-xs">
              <svg class="w-4 h-4 text-watch-green" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M16.5 10.5V6.75a4.5 4.5 0 10-9 0v3.75m-.75 11.25h10.5a2.25 2.25 0 002.25-2.25v-6.75a2.25 2.25 0 00-2.25-2.25H6.75a2.25 2.25 0 00-2.25 2.25v6.75a2.25 2.25 0 002.25 2.25z"/></svg>
              256-bit Encryption
            </div>
            <div class="flex items-center gap-2 text-white/40 text-xs">
              <svg class="w-4 h-4 text-watch-green" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 21a9.004 9.004 0 008.716-6.747M12 21a9.004 9.004 0 01-8.716-6.747M12 21c2.485 0 4.5-4.03 4.5-9S14.485 3 12 3m0 18c-2.485 0-4.5-4.03-4.5-9S9.515 3 12 3m0 0a8.997 8.997 0 017.843 4.582M12 3a8.997 8.997 0 00-7.843 4.582"/></svg>
              ODPC Compliant
            </div>
          </div>
        </div>

        <!-- Contact Info -->
        <div>
          <h4 class="text-xs font-black uppercase tracking-[0.2em] mb-6 text-watch-green">Contact</h4>
          <ul class="space-y-4">
            <li class="flex items-start gap-3">
              <svg class="w-5 h-5 text-watch-green mt-0.5 flex-shrink-0" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M15 10.5a3 3 0 11-6 0 3 3 0 016 0z"/><path stroke-linecap="round" stroke-linejoin="round" d="M19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1115 0z"/></svg>
              <span class="text-white/60 text-sm">Westlands, Nairobi, Kenya</span>
            </li>
            <li class="flex items-start gap-3">
              <svg class="w-5 h-5 text-watch-green mt-0.5 flex-shrink-0" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M2.25 6.75c0 8.284 6.716 15 15 15h2.25a2.25 2.25 0 002.25-2.25v-1.372c0-.516-.351-.966-.852-1.091l-4.423-1.106c-.44-.11-.902.055-1.173.417l-.97 1.293c-.282.376-.769.542-1.21.38a12.035 12.035 0 01-7.143-7.143c-.162-.441.004-.928.38-1.21l1.293-.97c.363-.271.527-.734.417-1.173L6.963 3.102a1.125 1.125 0 00-1.091-.852H4.5A2.25 2.25 0 002.25 4.5v2.25z"/></svg>
              <span class="text-white/60 text-sm">+254 700 000 000</span>
            </li>
            <li class="flex items-start gap-3">
              <svg class="w-5 h-5 text-watch-green mt-0.5 flex-shrink-0" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M21.75 6.75v10.5a2.25 2.25 0 01-2.25 2.25h-15a2.25 2.25 0 01-2.25-2.25V6.75m19.5 0A2.25 2.25 0 0019.5 4.5h-15a2.25 2.25 0 00-2.25 2.25m19.5 0v.243a2.25 2.25 0 01-1.07 1.916l-7.5 4.615a2.25 2.25 0 01-2.36 0L3.32 8.91a2.25 2.25 0 01-1.07-1.916V6.75"/></svg>
              <span class="text-white/60 text-sm">info@jiranicredit.co.ke</span>
            </li>
            <li class="flex items-start gap-3">
              <svg class="w-5 h-5 text-watch-green mt-0.5 flex-shrink-0" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M12 6v6h4.5m4.5 0a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
              <span class="text-white/60 text-sm">Mon–Fri: 8AM – 6PM EAT</span>
            </li>
          </ul>
        </div>
      </div>
    </div>

    <!-- Bottom Bar -->
    <div class="border-t border-white/10">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6 flex flex-col md:flex-row justify-between items-center gap-4">
        <p class="text-white/30 text-xs">&copy; {{ currentYear }} Jirani Credit Limited. All rights reserved.</p>
        <p class="text-white/20 text-[10px] uppercase tracking-widest">
          Licensed by the Central Bank of Kenya &middot; DeepSeek AI Powered Verification
        </p>
      </div>
    </div>
  </footer>
</template>

<script setup>
import { RouterLink } from 'vue-router';

const currentYear = new Date().getFullYear();
</script>
