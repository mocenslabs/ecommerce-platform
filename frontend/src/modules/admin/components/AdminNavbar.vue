<script setup>
import { useRouter } from 'vue-router'

import {
  useAuthStore,
} from '@/stores/auth.store'

import {
  useUiStore,
} from '@/stores/ui.store'

const router = useRouter()

const authStore =
  useAuthStore()

const uiStore =
  useUiStore()

const logout =
  async () => {
    await authStore.logout()

    router.push('/login')
  }
</script>

<template>
  <header
    class="sticky top-0 z-40 flex h-16 items-center justify-between border-b border-slate-200 bg-white px-4 dark:border-slate-800 dark:bg-slate-950"
  >
    <div
      class="flex items-center gap-3"
    >
      <button
        class="rounded-lg p-2 hover:bg-slate-100 dark:hover:bg-slate-800 lg:hidden"
        @click="
          uiStore.toggleAdminSidebar()
        "
      >
        ☰
      </button>

      <h1
        class="text-lg font-semibold"
      >
        Admin
      </h1>
    </div>

    <div
      class="flex items-center gap-4"
    >
      <div
        class="hidden text-right md:block"
      >
        <p
          class="text-sm font-medium"
        >
          Administrator
        </p>

        <p
          class="text-xs text-slate-500"
        >
          Management Panel
        </p>
      </div>

      <button
        class="rounded-lg border px-4 py-2 text-sm hover:bg-slate-100 dark:hover:bg-slate-800"
        @click="logout"
      >
        Logout
      </button>
    </div>
  </header>
</template>
