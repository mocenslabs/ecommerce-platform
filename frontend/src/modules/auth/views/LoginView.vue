<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

import { useAuthStore } from '@/stores/auth.store'

const router = useRouter()

const authStore = useAuthStore()

const form = ref({
  email: '',
  password: '',
})

const error = ref('')

const handleSubmit = async () => {
  error.value = ''

  try {
    await authStore.login(
      form.value
    )

    router.push('/')
  } catch (err) {
    error.value =
      err.response?.data?.errors
        ?.non_field_errors?.[0] ??
      'Login failed'
  }
}
</script>

<template>
  <section
    class="mx-auto max-w-md px-4 py-12"
  >
    <h1
      class="mb-6 text-3xl font-bold"
    >
      Login
    </h1>

    <form
      class="space-y-4"
      @submit.prevent="handleSubmit"
    >
      <div>
        <label
          class="mb-1 block text-sm"
        >
          Email
        </label>

        <input
          v-model="form.email"
          type="email"
          class="w-full rounded-lg border p-3"
          required
        >
      </div>

      <div>
        <label
          class="mb-1 block text-sm"
        >
          Password
        </label>

        <input
          v-model="form.password"
          type="password"
          class="w-full rounded-lg border p-3"
          required
        >
      </div>

      <p
        v-if="error"
        class="text-red-500"
      >
        {{ error }}
      </p>

      <button
        type="submit"
        class="w-full rounded-lg bg-black p-3 text-white"
      >
        Login
      </button>
    </form>
  </section>
</template>
