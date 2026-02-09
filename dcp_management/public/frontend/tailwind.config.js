/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        // Jirani Credit v4.0 — Trust & Growth palette
        'clinical-white': '#FFFFFF',
        'vapor-grey': '#F4F6F8',
        'ink-black': '#000000',
        'watch-green': '#39FF14',
        'deepseek-blue': '#4D6BFE',
        'alert-magenta': '#FF00FF',
        // Trust colors — Kenyan fintech inspired
        'trust-green': '#0D9F61',
        'trust-green-light': '#E6F7EF',
        'trust-green-dark': '#087A4A',
        'trust-blue': '#1A56DB',
        'trust-blue-light': '#EBF0FE',
        'trust-blue-dark': '#0F3A94',
        'warm-gold': '#F59E0B',
        'warm-gold-light': '#FEF3C7',
        'soft-grey': '#6B7280',
        'light-grey': '#F9FAFB',
        // Legacy aliases
        'chronos-black': '#000000',
        'biolume-green': '#39FF14',
      },
      fontFamily: {
        'inter': ['Inter', 'Roboto', 'sans-serif'],
      },
      boxShadow: {
        'hard-sm': '3px 3px 0px 0px rgba(0,0,0,1)',
        'hard-md': '4px 4px 0px 0px rgba(0,0,0,1)',
        'hard-lg': '6px 6px 0px 0px rgba(0,0,0,1)',
        'green-glow': '0 0 20px rgba(57,255,20,0.4)',
        'soft': '0 2px 15px -3px rgba(0,0,0,0.07), 0 10px 20px -2px rgba(0,0,0,0.04)',
        'card': '0 4px 6px -1px rgba(0,0,0,0.05), 0 2px 4px -2px rgba(0,0,0,0.05)',
        'card-hover': '0 10px 25px -5px rgba(0,0,0,0.1), 0 8px 10px -6px rgba(0,0,0,0.05)',
      },
      animation: {
        'float': 'float 6s ease-in-out infinite',
        'pulse-slow': 'pulse 4s cubic-bezier(0.4, 0, 0.6, 1) infinite',
      },
      keyframes: {
        float: {
          '0%, 100%': { transform: 'translateY(0px)' },
          '50%': { transform: 'translateY(-10px)' },
        },
      },
    },
  },
  plugins: [],
}
