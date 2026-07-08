<script setup>
defineProps({
  variant: {
    type: String,
    default: 'primary',
  },

  size: {
    type: String,
    default: 'md',
  },

  disabled: {
    type: Boolean,
    default: false,
  },
})
</script>

<template>
  <button
    :disabled="disabled"
    :class="[
      'inline-flex items-center justify-center rounded-xl font-medium transition-all',

      {
        'bg-slate-900 text-white hover:bg-slate-800':
          variant === 'primary',

        'border border-slate-300 bg-white hover:bg-slate-100':
          variant === 'secondary',

        'h-10 px-4 text-sm':
          size === 'sm',

        'h-12 px-6':
          size === 'md',

        'h-14 px-8 text-lg':
          size === 'lg',
      },
    ]"
  >
    <slot />
  </button>
</template>
