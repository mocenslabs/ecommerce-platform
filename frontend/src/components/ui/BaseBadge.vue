<script setup>
defineProps({
  text: {
    type: String,
    required: true,
  },
})
</script>

<template>
  <span
    class="rounded-full bg-slate-100 px-3 py-1 text-xs font-medium"
  >
    {{ text }}
  </span>
</template>
