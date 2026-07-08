<script setup>
defineProps({
  columns: {
    type: Array,
    required: true,
  },
})
</script>

<template>
  <div
    class="overflow-hidden rounded-2xl border border-slate-200 bg-white shadow-sm dark:border-slate-800 dark:bg-slate-900"
  >
    <div
      class="overflow-x-auto"
    >
      <table
        class="min-w-full whitespace-nowrap"
      >
        <thead>
          <tr
            class="border-b border-slate-200 dark:border-slate-800"
          >
            <th
              v-for="column in columns"
              :key="column"
              class="px-4 py-4 text-left text-sm font-semibold text-slate-700 dark:text-slate-300"
            >
              {{ column }}
            </th>
          </tr>
        </thead>

        <tbody>
          <slot />
        </tbody>
      </table>
    </div>
  </div>
</template>
