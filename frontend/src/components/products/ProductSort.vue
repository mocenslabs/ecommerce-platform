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
  <select
    :value="modelValue"
    class="rounded-lg border px-4 py-3"
    @change="
      $emit(
        'update:modelValue',
        $event.target.value,
      )
    "
  >
    <option value="">
      Sort By
    </option>

    <option value="-created_at">
      Newest
    </option>

    <option value="created_at">
      Oldest
    </option>

    <option value="name">
      Name A-Z
    </option>

    <option value="-name">
      Name Z-A
    </option>

    <option value="-rating">
      Highest Rated
    </option>
  </select>
</template>
