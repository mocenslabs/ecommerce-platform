<script setup>
import { useRoute } from 'vue-router'

import {
  useUiStore,
} from '@/stores/ui.store'

const route = useRoute()

const uiStore =
  useUiStore()

const menu = [
  {
    label: 'Dashboard',
    route: '/admin',
  },
  {
    label: 'Products',
    route: '/admin/products',
  },
  {
    label: 'Categories',
    route: '/admin/categories',
  },
  {
    label: 'Brands',
    route: '/admin/brands',
  },
  {
    label: 'Images',
    route: '/admin/product-images',
  },
  {
    label: 'Inventory',
    route: '/admin/inventory',
  },
  {
    label: 'Orders',
    route: '/admin/orders',
  },
  {
    label: 'Shipping',
    route: '/admin/shipping-methods',
  },
  {
    label: 'Payments',
    route: '/admin/payments',
  },
  {
  label: 'Discounts',
  route: '/admin/discounts',
  },
  {
    label: 'Customers',
    route: '/admin/customers',
  },
  {
    label: 'Reviews',
    route: '/admin/reviews',
  },

]

const isActive = (path) => {
  if (path === '/admin') {
    return route.path === '/admin'
  }

  return route.path.startsWith(path)
}

const navigate = () => {
  uiStore.closeAdminSidebar()
}
</script>

<template>
  <!-- Overlay -->

  <div
    v-if="uiStore.adminSidebarOpen"
    class="fixed inset-0 z-40 bg-black/50 lg:hidden"
    @click="
      uiStore.closeAdminSidebar()
    "
  />

  <aside
    :class="[
      'fixed left-0 top-0 z-50 flex h-screen w-64 flex-col border-r border-slate-200 bg-white transition-transform duration-300 dark:border-slate-800 dark:bg-slate-950 lg:static lg:translate-x-0',
      uiStore.adminSidebarOpen
        ? 'translate-x-0'
        : '-translate-x-full',
    ]"
  >
    <div
      class="border-b border-slate-200 p-6 dark:border-slate-800"
    >
      <h2
        class="text-xl font-bold"
      >
        Admin Panel
      </h2>

      <p
        class="mt-1 text-sm text-slate-500"
      >
        Premium E-commerce
      </p>
    </div>

    <nav
      class="flex-1 space-y-2 p-4"
    >
      <RouterLink
        v-for="item in menu"
        :key="item.route"
        :to="item.route"
        @click="navigate"
        :class="[
          'block rounded-lg px-4 py-3 text-sm font-medium transition',
          isActive(item.route)
            ? 'bg-slate-900 text-white'
            : 'hover:bg-slate-100 dark:hover:bg-slate-800',
        ]"
      >
        {{ item.label }}
      </RouterLink>
    </nav>
  </aside>
</template>
