<script setup>
import {
  storeToRefs,
} from 'pinia'

import {
  useAuthStore,
} from '@/stores/auth.store'

const authStore =
  useAuthStore()

const {
  isAuthenticated,
} = storeToRefs(
  authStore,
)

async function logout() {
  await authStore.logout()
}

defineProps({
  open: {
    type: Boolean,
    default: false,
  },
})
</script>

<template>
  <Transition name="fade">
    <div
      v-if="open"
      class="border-t border-slate-200 bg-white dark:border-slate-800 dark:bg-slate-950 md:hidden"
    >
      <nav
        class="flex flex-col gap-4 p-4"
      >
        <RouterLink to="/">
          Home
        </RouterLink>

        <RouterLink
          to="/products"
        >
          Products
        </RouterLink>

        <RouterLink
          to="/cart"
        >
          Cart
        </RouterLink>

        <RouterLink
          v-if="isAuthenticated"
          to="/wishlist"
        >
          Wishlist
        </RouterLink>

        <RouterLink
          v-if="isAuthenticated"
          to="/account"
        >
          My Account
        </RouterLink>

        <button
          v-if="isAuthenticated"
          @click="logout"
        >
          Logout
        </button>

        <template
          v-else
        >
          <RouterLink
            to="/login"
          >
            Login
          </RouterLink>

          <RouterLink
            to="/register"
          >
            Register
          </RouterLink>
        </template>
      </nav>
    </div>
  </Transition>
</template>
