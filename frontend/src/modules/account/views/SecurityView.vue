<script setup>
import {
  reactive,
} from 'vue'

import {
  useProfileStore,
} from '@/stores/profile.store'

const profileStore =
  useProfileStore()

const form =
  reactive({
    current_password: '',
    new_password: '',
    confirm_password: '',
  })

async function submit() {
  await profileStore.changePassword(
    form
  )

  form.current_password =
    ''

  form.new_password =
    ''

  form.confirm_password =
    ''
}
</script>

<template>
  <section
    class="mx-auto max-w-3xl px-4 py-12"
  >
    <h1
      class="mb-8 text-4xl font-bold"
    >
      Security
    </h1>

    <form
      class="space-y-6 rounded-xl border p-6"
      @submit.prevent="submit"
    >
      <input
        v-model="form.current_password"
        type="password"
        placeholder="Current password"
        class="w-full rounded-lg border px-4 py-3"
      >

      <input
        v-model="form.new_password"
        type="password"
        placeholder="New password"
        class="w-full rounded-lg border px-4 py-3"
      >

      <input
        v-model="form.confirm_password"
        type="password"
        placeholder="Confirm password"
        class="w-full rounded-lg border px-4 py-3"
      >

      <button
        class="rounded-lg bg-slate-900 px-6 py-3 text-white"
      >
        Change Password
      </button>
    </form>
  </section>
</template>
