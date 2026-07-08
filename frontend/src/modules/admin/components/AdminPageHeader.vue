<script setup>
defineProps({
  title: {
    type: String,
    required: true,
  },

  subtitle: {
    type: String,
    default: '',
  },
})
</script>

<template>
  <div
    class="mb-8 flex flex-col gap-4 md:flex-row md:items-center md:justify-between"
  >
    <div>
      <h1
        class="text-3xl font-bold"
      >
        {{ title }}
      </h1>

      <p
        v-if="subtitle"
        class="mt-1 text-sm text-slate-500"
      >
        {{ subtitle }}
      </p>
    </div>

    <slot />
  </div>
</template>
