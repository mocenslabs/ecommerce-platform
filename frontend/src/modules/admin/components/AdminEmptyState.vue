<script setup>
defineProps({
  title: String,
  description: String,
})
</script>

<template>
  <div
    class="rounded-2xl border border-dashed border-slate-300 p-12 text-center"
  >
    <h3
      class="text-lg font-semibold"
    >
      {{ title }}
    </h3>

    <p
      class="mt-2 text-sm text-slate-500"
    >
      {{ description }}
    </p>
  </div>
</template>
