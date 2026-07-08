<script setup>
import {
  reactive,
} from 'vue'

const emit =
  defineEmits([
    'submit',
  ])

const form = reactive({
  first_name: '',
  last_name: '',
  line_1: '',
  line_2: '',
  city: '',
  state: '',
  postal_code: '',
  country: 'AR',
  phone_number: '',
  is_default: true,
  is_billing: true,
  is_shipping: true,
})

function submitForm() {
  emit(
    'submit',
    {
      ...form,
    },
  )
}
</script>

<template>
  <form
    class="space-y-4"
    @submit.prevent="submitForm"
  >
    <input
      v-model="form.first_name"
      placeholder="First Name"
      class="w-full rounded-lg border p-3"
    >

    <input
      v-model="form.last_name"
      placeholder="Last Name"
      class="w-full rounded-lg border p-3"
    >

    <input
      v-model="form.line_1"
      placeholder="Address"
      class="w-full rounded-lg border p-3"
    >

    <input
      v-model="form.city"
      placeholder="City"
      class="w-full rounded-lg border p-3"
    >

    <input
      v-model="form.state"
      placeholder="State"
      class="w-full rounded-lg border p-3"
    >

    <input
      v-model="form.postal_code"
      placeholder="Postal Code"
      class="w-full rounded-lg border p-3"
    >

    <input
      v-model="form.phone_number"
      placeholder="Phone Number"
      class="w-full rounded-lg border p-3"
    >

    <button
      class="rounded-lg bg-black px-6 py-3 text-white"
    >
      Save Address
    </button>
  </form>
</template>
