<script setup>
import { ref } from 'vue'

import {
  storeToRefs,
} from 'pinia'

import {
  useAuthStore,
} from '@/stores/auth.store'

import {
  useCartStore,
} from '@/stores/cart.store'

import ThemeToggle from './ThemeToggle.vue'
import MobileMenu from './MobileMenu.vue'

const authStore =
  useAuthStore()

const cartStore =
  useCartStore()

const {
  isAuthenticated,
} = storeToRefs(
  authStore,
)

const {
  itemCount,
} = storeToRefs(
  cartStore,
)

const mobileMenuOpen = ref(
  false,
)

const toggleMenu = () => {
  mobileMenuOpen.value =
    !mobileMenuOpen.value
}

async function logout() {
  await authStore.logout()
}
</script>

<template>
  <header
    class="sticky top-0 z-50 border-b border-slate-200 bg-white/90 backdrop-blur dark:border-slate-800 dark:bg-slate-950/90"
  >
    <div
      class="mx-auto flex h-16 max-w-7xl items-center justify-between px-4"
    >
      <RouterLink
        to="/"
        class="text-xl font-bold tracking-tight"
      >
        Black Eagle
      </RouterLink>

      <nav
        class="hidden items-center gap-8 md:flex"
      >
        <RouterLink
          to="/"
          class="hover:text-blue-600"
        >
          Home
        </RouterLink>

        <RouterLink
          to="/products"
          class="hover:text-blue-600"
        >
          Products
        </RouterLink>

        <RouterLink
          v-if="isAuthenticated"
          to="/wishlist"
          class="hover:text-blue-600"
        >
          Wishlist
        </RouterLink>

        <RouterLink
          v-if="isAuthenticated"
          to="/account"
          class="hover:text-blue-600"
        >
          My Account
        </RouterLink>
      </nav>

      <div
        class="flex items-center gap-4"
      >
        <ThemeToggle />

        <RouterLink
          to="/cart"
          class="hidden md:block"
        >
          Cart ({{ itemCount }})
        </RouterLink>

        <template
          v-if="isAuthenticated"
        >
          <button
            class="hidden md:block"
            @click="logout"
          >
            Logout
          </button>
        </template>

        <template
          v-else
        >
          <RouterLink
            to="/login"
            class="hidden md:block"
          >
            Login
          </RouterLink>

          <RouterLink
            to="/register"
            class="hidden md:block"
          >
            Register
          </RouterLink>
        </template>

        <button
          class="md:hidden"
          @click="toggleMenu"
        >
          ☰
        </button>
      </div>
    </div>

    <MobileMenu
      :open="mobileMenuOpen"
    />
  </header>
</template>
