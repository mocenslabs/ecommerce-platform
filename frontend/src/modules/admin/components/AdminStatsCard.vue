<script setup>
defineProps({
  title: String,
  value: [String, Number],
})
</script>

<template>
  <div
    class="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm dark:border-slate-800 dark:bg-slate-900"
  >
    <p
      class="text-sm text-slate-500"
    >
      {{ title }}
    </p>

    <h3
      class="mt-2 text-3xl font-bold"
    >
      {{ value }}
    </h3>
  </div>
</template>
