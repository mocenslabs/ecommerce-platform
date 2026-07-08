<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

import { authService } from '@/services/auth.service'

const router = useRouter()

const form = ref({
  email: '',
  password: '',
})

const error = ref('')
const success = ref('')

const handleSubmit = async () => {
  error.value = ''
  success.value = ''

  try {
    await authService.register(
      form.value
    )

    success.value =
      'Account created successfully.'

    setTimeout(() => {
      router.push('/login')
    }, 1500)
  } catch (err) {
    error.value =
      err.response?.data?.message ??
      'Registration failed'
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
      Register
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

      <p
        v-if="success"
        class="text-green-600"
      >
        {{ success }}
      </p>

      <button
        type="submit"
        class="w-full rounded-lg bg-black p-3 text-white"
      >
        Register
      </button>
    </form>
  </section>
</template>
