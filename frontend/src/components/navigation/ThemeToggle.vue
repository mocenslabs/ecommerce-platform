<script setup>
import { useTheme } from '@/composables/useTheme'

const {
  isDark,
  toggleTheme,
} = useTheme()
</script>

<template>
  <button
    class="flex h-10 w-10 items-center justify-center rounded-xl border border-slate-200 transition hover:bg-slate-100 dark:border-slate-700 dark:hover:bg-slate-800"
    @click="toggleTheme"
  >
    <span v-if="isDark">
      ☀️
    </span>

    <span v-else>
      🌙
    </span>
  </button>
</template>
