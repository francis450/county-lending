<template>
  <div class="border-2 border-ink-black p-6 bg-white shadow-hard-sm hover:shadow-hard-md transition-all font-inter">
    <div class="flex items-start justify-between">
      <div>
        <p class="text-[10px] font-black text-ink-black/40 uppercase tracking-[0.2em] mb-1">{{ label }}</p>
        <p class="text-3xl font-black">{{ formattedValue }}</p>
        <p v-if="subtitle" class="text-xs text-ink-black/40 mt-1">{{ subtitle }}</p>
      </div>
      <div :class="['w-12 h-12 flex items-center justify-center', iconBgClass]">
        <slot name="icon">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
          </svg>
        </slot>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  label: { type: String, required: true },
  value: { type: [Number, String], required: true },
  subtitle: { type: String, default: '' },
  type: { type: String, default: 'default' },
  isCurrency: { type: Boolean, default: false }
})

const formattedValue = computed(() => {
  if (props.isCurrency) {
    const num = typeof props.value === 'number' ? props.value : parseFloat(props.value) || 0
    return `KES ${num.toLocaleString()}`
  }
  return props.value
})

const iconBgClass = computed(() => {
  const colors = {
    default: 'bg-vapor-grey border-2 border-ink-black',
    success: 'bg-watch-green',
    warning: 'bg-alert-magenta/10 border-2 border-alert-magenta',
    danger: 'bg-alert-magenta/10 border-2 border-alert-magenta',
    info: 'bg-deepseek-blue text-white'
  }
  return colors[props.type] || colors.default
})
</script>
