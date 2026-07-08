<script setup>
defineProps({
  status: String,
})

const classes = {
  pending:
    'bg-yellow-100 text-yellow-700',

  paid:
    'bg-green-100 text-green-700',

  processing:
    'bg-blue-100 text-blue-700',

  shipped:
    'bg-purple-100 text-purple-700',

  delivered:
    'bg-emerald-100 text-emerald-700',

  cancelled:
    'bg-red-100 text-red-700',

  refunded:
    'bg-slate-100 text-slate-700',
}
</script>

<template>
  <span
    class="rounded-full px-3 py-1 text-xs font-semibold"
    :class="
      classes[status]
    "
  >
    {{ status }}
  </span>
</template>
