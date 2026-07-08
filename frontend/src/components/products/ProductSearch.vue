<script setup>
defineProps({
  modelValue: {
    type: String,
    default: '',
  },
})

defineEmits([
  'update:modelValue',
])
</script>

<template>
  <input
    :value="modelValue"
    type="text"
    placeholder="Search products..."
    class="w-full rounded-lg border px-4 py-3"
    @input="
      $emit(
        'update:modelValue',
        $event.target.value,
      )
    "
  >
</template>
