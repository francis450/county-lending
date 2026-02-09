<template>
  <div class="min-h-screen bg-white">

    <!-- HERO -->
    <section class="py-20 lg:py-28 bg-gradient-to-b from-trust-green-light to-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h1 class="trust-heading text-4xl md:text-5xl mb-6 fade-in-up">Jirani Credit Blog</h1>
        <p class="trust-subheading mx-auto fade-in-up delay-100">
          Financial tips, success stories, and news for Kenya's employed professionals.
        </p>
      </div>
    </section>

    <!-- CATEGORIES -->
    <section class="border-b border-gray-200 sticky top-20 bg-white z-40">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex gap-1 overflow-x-auto py-4">
          <button
            v-for="cat in categories"
            :key="cat"
            @click="activeCategory = cat"
            class="px-5 py-2 text-xs font-bold uppercase tracking-widest rounded-lg whitespace-nowrap transition-all"
            :class="activeCategory === cat ? 'bg-trust-green text-white' : 'text-soft-grey hover:bg-vapor-grey'"
          >
            {{ cat }}
          </button>
        </div>
      </div>
    </section>

    <!-- FEATURED POST -->
    <section class="py-16">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
          <div class="bg-trust-green rounded-2xl p-8 flex flex-col justify-end min-h-[400px] relative overflow-hidden">
            <div class="absolute inset-0 bg-gradient-to-t from-ink-black/70 to-transparent"></div>
            <div class="relative z-10">
              <span class="inline-block bg-watch-green text-ink-black text-[10px] font-black uppercase px-3 py-1 mb-4">Featured</span>
              <h2 class="text-2xl md:text-3xl font-black text-white mb-3">{{ featuredPost.title }}</h2>
              <p class="text-white/70 mb-4">{{ featuredPost.excerpt }}</p>
              <div class="flex items-center gap-4 text-white/50 text-xs">
                <span>{{ featuredPost.author }}</span>
                <span>&middot;</span>
                <span>{{ featuredPost.date }}</span>
                <span>&middot;</span>
                <span>{{ featuredPost.readTime }}</span>
              </div>
            </div>
          </div>
          <!-- Side posts -->
          <div class="space-y-4">
            <div v-for="(post, i) in filteredPosts.slice(0, 3)" :key="i" class="trust-card flex gap-4 cursor-pointer hover:border-trust-green transition-colors">
              <div class="w-24 h-24 bg-vapor-grey rounded-xl flex-shrink-0 flex items-center justify-center">
                <span class="text-3xl">{{ post.emoji }}</span>
              </div>
              <div class="flex-1 min-w-0">
                <span class="text-[10px] font-bold uppercase tracking-widest text-trust-green">{{ post.category }}</span>
                <h3 class="font-bold text-sm mt-1 line-clamp-2">{{ post.title }}</h3>
                <div class="flex items-center gap-2 text-xs text-soft-grey mt-2">
                  <span>{{ post.date }}</span>
                  <span>&middot;</span>
                  <span>{{ post.readTime }}</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- ALL POSTS GRID -->
    <section class="py-16 bg-vapor-grey border-t border-gray-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <h2 class="trust-heading text-2xl mb-10">All Articles</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          <article v-for="(post, i) in filteredPosts" :key="i" class="trust-card group cursor-pointer">
            <div class="w-full h-48 bg-gradient-to-br rounded-xl mb-6 flex items-center justify-center" :class="post.gradient">
              <span class="text-5xl">{{ post.emoji }}</span>
            </div>
            <span class="text-[10px] font-bold uppercase tracking-widest text-trust-green">{{ post.category }}</span>
            <h3 class="font-black text-lg mt-2 mb-3 group-hover:text-trust-green transition-colors">{{ post.title }}</h3>
            <p class="text-soft-grey text-sm leading-relaxed mb-4">{{ post.excerpt }}</p>
            <div class="flex items-center justify-between text-xs text-soft-grey">
              <div class="flex items-center gap-2">
                <div class="w-6 h-6 bg-trust-green rounded-full flex items-center justify-center text-white text-[10px] font-bold">{{ post.author.charAt(0) }}</div>
                <span>{{ post.author }}</span>
              </div>
              <div class="flex items-center gap-2">
                <span>{{ post.date }}</span>
                <span>&middot;</span>
                <span>{{ post.readTime }}</span>
              </div>
            </div>
          </article>
        </div>
      </div>
    </section>

    <!-- NEWSLETTER -->
    <section class="py-20 bg-ink-black">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h2 class="text-3xl font-black text-white mb-4">Stay Informed</h2>
        <p class="text-white/50 mb-8">Subscribe to our newsletter for the latest financial tips and Jirani Credit updates.</p>
        <form @submit.prevent="subscribe" class="flex flex-col sm:flex-row gap-4 max-w-lg mx-auto">
          <input v-model="email" type="email" placeholder="Enter your email" class="flex-1 px-5 py-4 bg-white/10 border border-white/20 text-white rounded-xl placeholder-white/30 focus:border-watch-green focus:bg-white/5">
          <button type="submit" class="btn-primary whitespace-nowrap">Subscribe</button>
        </form>
        <p v-if="subscribed" class="text-watch-green text-sm mt-4">Thank you for subscribing!</p>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';

const activeCategory = ref('All');
const email = ref('');
const subscribed = ref(false);

const categories = ['All', 'Finance Tips', 'Success Stories', 'News', 'Guides'];

const featuredPost = {
  title: 'How to Manage Your Salary Advance Wisely',
  excerpt: 'Getting a salary advance can be a lifeline, but managing it well is key. Here are proven strategies for Kenyan employees to make the most of their advance without falling into a debt cycle.',
  author: 'Jirani Credit',
  date: 'Feb 5, 2026',
  readTime: '5 min read',
};

const posts = [
  { title: 'How to Manage Your Salary Advance Wisely', excerpt: 'Getting a salary advance can be a lifeline. Learn proven strategies for managing it well.', category: 'Finance Tips', author: 'Amina Hassan', date: 'Feb 5, 2026', readTime: '5 min', emoji: '💰', gradient: 'from-trust-green-light to-trust-blue-light' },
  { title: 'Financial Tips for Kenyan Employees in 2026', excerpt: 'The new year brings new opportunities. Here are 10 financial resolutions every Kenyan employee should adopt.', category: 'Finance Tips', author: 'James Omondi', date: 'Jan 28, 2026', readTime: '7 min', emoji: '📊', gradient: 'from-trust-blue-light to-vapor-grey' },
  { title: 'How AI is Transforming Lending in Kenya', excerpt: 'DeepSeek AI and other technologies are making loan approvals faster and fairer. Here\'s what you need to know.', category: 'News', author: 'Jirani Credit', date: 'Jan 20, 2026', readTime: '4 min', emoji: '🤖', gradient: 'from-vapor-grey to-trust-green-light' },
  { title: 'John\'s Story: From Emergency to Empowerment', excerpt: 'How a Nairobi teacher used Jirani Credit to handle a family emergency and build a better financial future.', category: 'Success Stories', author: 'Jirani Credit', date: 'Jan 15, 2026', readTime: '3 min', emoji: '⭐', gradient: 'from-warm-gold-light to-trust-green-light' },
  { title: 'Understanding CBK Regulations for Digital Lenders', excerpt: 'A simplified guide to the Central Bank of Kenya\'s regulations on digital lending and what they mean for borrowers.', category: 'News', author: 'Grace Njeri', date: 'Jan 10, 2026', readTime: '6 min', emoji: '📋', gradient: 'from-trust-green-light to-vapor-grey' },
  { title: 'M-Pesa Tips: Maximize Your Mobile Money', excerpt: 'Beyond sending money — discover M-Pesa features that can help you save, invest, and manage loans more effectively.', category: 'Guides', author: 'Peter Mwangi', date: 'Jan 5, 2026', readTime: '5 min', emoji: '📱', gradient: 'from-trust-blue-light to-warm-gold-light' },
  { title: 'Building an Emergency Fund on a Kenyan Salary', excerpt: 'Practical steps to building a financial safety net, even when money is tight.', category: 'Finance Tips', author: 'Amina Hassan', date: 'Dec 28, 2025', readTime: '6 min', emoji: '🏦', gradient: 'from-vapor-grey to-trust-blue-light' },
  { title: 'Mary\'s Journey: Education Financing with Jirani', excerpt: 'How a single mother from Mombasa financed her child\'s education using employee-based credit.', category: 'Success Stories', author: 'Jirani Credit', date: 'Dec 20, 2025', readTime: '4 min', emoji: '🎓', gradient: 'from-trust-green-light to-warm-gold-light' },
  { title: 'A Complete Guide to Your Jirani Credit Dashboard', excerpt: 'Step-by-step walkthrough of your Jirani Credit dashboard — track loans, payments, and documents.', category: 'Guides', author: 'Jirani Credit', date: 'Dec 15, 2025', readTime: '5 min', emoji: '📖', gradient: 'from-trust-blue-light to-trust-green-light' },
];

const filteredPosts = computed(() => {
  if (activeCategory.value === 'All') return posts;
  return posts.filter(p => p.category === activeCategory.value);
});

const subscribe = () => {
  if (email.value) {
    subscribed.value = true;
    email.value = '';
    setTimeout(() => { subscribed.value = false; }, 3000);
  }
};
</script>
