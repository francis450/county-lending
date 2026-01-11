<template>
  <div :class="[
    'p-6 rounded-xl shadow-lg border-2 transition-all',
    colorClass
  ]">
    <div class="flex items-start justify-between">
      <div>
        <p class="text-sm font-medium opacity-80 mb-1">{{ label }}</p>
        <p class="text-3xl font-bold">{{ formattedValue }}</p>
        <p v-if="subtitle" class="text-sm opacity-70 mt-1">{{ subtitle }}</p>
      </div>
      <div :class="['w-12 h-12 rounded-full flex items-center justify-center', iconBgClass]">
        <slot name="icon">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
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
  type: { type: String, default: 'default' }, // default, success, warning, danger, info
  isCurrency: { type: Boolean, default: false }
})

const formattedValue = computed(() => {
  if (props.isCurrency) {
    const num = typeof props.value === 'number' ? props.value : parseFloat(props.value) || 0
    return `KES ${num.toLocaleString()}`
  }
  return props.value
})

const colorClass = computed(() => {
  const colors = {
    default: 'bg-white border-gray-200',
    success: 'bg-green-50 border-green-200 text-green-800',
    warning: 'bg-yellow-50 border-yellow-200 text-yellow-800',
    danger: 'bg-red-50 border-red-200 text-red-800',
    info: 'bg-blue-50 border-blue-200 text-blue-800'
  }
  return colors[props.type] || colors.default
})

const iconBgClass = computed(() => {
  const colors = {
    default: 'bg-gray-100 text-gray-600',
    success: 'bg-green-100 text-green-600',
    warning: 'bg-yellow-100 text-yellow-600',
    danger: 'bg-red-100 text-red-600',
    info: 'bg-blue-100 text-blue-600'
  }
  return colors[props.type] || colors.default
})
</script>
