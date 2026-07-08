<script setup>
import {
  reactive,
  onMounted,
} from 'vue'

import {
  storeToRefs,
} from 'pinia'

import {
  useProfileStore,
} from '@/stores/profile.store'

const profileStore =
  useProfileStore()

const {
  profile,
  loading,
} = storeToRefs(
  profileStore,
)

const form =
  reactive({
    first_name: '',
    last_name: '',
  })

onMounted(async () => {
  await profileStore.fetchProfile()

  form.first_name =
    profile.value?.first_name || ''

  form.last_name =
    profile.value?.last_name || ''
})

async function submit() {
  await profileStore.updateProfile(
    form
  )
}
</script>

<template>
  <section
    class="mx-auto max-w-3xl px-4 py-12"
  >
    <h1
      class="mb-8 text-4xl font-bold"
    >
      Profile
    </h1>

    <div
      v-if="loading"
      class="text-center"
    >
      Loading...
    </div>

    <form
      v-else
      class="space-y-6 rounded-xl border p-6"
      @submit.prevent="submit"
    >
      <div>
        <label
          class="mb-2 block text-sm font-medium"
        >
          Email
        </label>

        <input
          :value="profile?.email"
          disabled
          class="w-full rounded-lg border px-4 py-3"
        >
      </div>

      <div>
        <label
          class="mb-2 block text-sm font-medium"
        >
          First Name
        </label>

        <input
          v-model="form.first_name"
          class="w-full rounded-lg border px-4 py-3"
        >
      </div>

      <div>
        <label
          class="mb-2 block text-sm font-medium"
        >
          Last Name
        </label>

        <input
          v-model="form.last_name"
          class="w-full rounded-lg border px-4 py-3"
        >
      </div>

      <button
        class="rounded-lg bg-slate-900 px-6 py-3 text-white"
      >
        Save Changes
      </button>
    </form>
  </section>
</template>
