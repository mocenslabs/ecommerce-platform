<script setup>
import {
  onMounted,
} from 'vue'

import {
  RouterLink,
} from 'vue-router'

import {
  storeToRefs,
} from 'pinia'

import {
  useCustomerDashboardStore,
} from '@/stores/customer-dashboard.store'

const dashboardStore =
  useCustomerDashboardStore()

const {
  dashboard,
  loading,
} = storeToRefs(
  dashboardStore,
)

onMounted(() => {
  dashboardStore.fetchDashboard()
})
</script>

<template>
  <section class="mx-auto max-w-6xl px-4 py-12">
    <h1 class="mb-8 text-4xl font-bold">
      My Account
    </h1>

    <div v-if="loading" class="py-20 text-center">
      Loading...
    </div>

    <template v-else-if="dashboard">
      <!-- Stats -->

      <div class="grid gap-4 sm:grid-cols-2 xl:grid-cols-4">
        <div class="rounded-xl border p-6">
          <p class="text-sm text-slate-500">
            Orders
          </p>

          <h3 class="mt-2 text-3xl font-bold">
            {{ dashboard.total_orders }}
          </h3>
        </div>

        <div class="rounded-xl border p-6">
          <p class="text-sm text-slate-500">
            Total Spent
          </p>

          <h3 class="mt-2 text-3xl font-bold">
            $
            {{ dashboard.total_spent }}
          </h3>
        </div>

        <div class="rounded-xl border p-6">
          <p class="text-sm text-slate-500">
            Wishlist
          </p>

          <h3 class="mt-2 text-3xl font-bold">
            {{ dashboard.wishlist_count }}
          </h3>
        </div>

        <div class="rounded-xl border p-6">
          <p class="text-sm text-slate-500">
            Addresses
          </p>

          <h3 class="mt-2 text-3xl font-bold">
            {{ dashboard.address_count }}
          </h3>
        </div>
      </div>

      <!-- Last Order -->

      <div class="mt-8 rounded-xl border p-6">
        <h2 class="mb-4 text-xl font-bold">
          Last Order
        </h2>

        <div v-if="dashboard.last_order">
          <p>
            Number:
            {{
              dashboard.last_order.order_number
            }}
          </p>

          <p>
            Status:
            {{
              dashboard.last_order.status
            }}
          </p>

          <p>
            Total:
            $
            {{
              dashboard.last_order.total_amount
            }}
          </p>
        </div>

        <div v-else class="text-slate-500">
          No orders yet.
        </div>
      </div>

      <!-- Quick Actions -->

      <div class="mt-8 grid gap-4 md:grid-cols-3">
        <RouterLink to="/account/orders"
          class="rounded-xl border p-6 transition hover:bg-slate-50 dark:hover:bg-slate-800">
          My Orders
        </RouterLink>

        <RouterLink to="/wishlist" class="rounded-xl border p-6 transition hover:bg-slate-50 dark:hover:bg-slate-800">
          Wishlist
        </RouterLink>

        <RouterLink to="/account/addresses"
          class="rounded-xl border p-6 transition hover:bg-slate-50 dark:hover:bg-slate-800">
          Addresses
        </RouterLink>

        <RouterLink to="/account/profile" class="rounded-xl border p-6">
          Profile
        </RouterLink>

        <RouterLink to="/account/security" class="rounded-xl border p-6">
          Security
        </RouterLink>
      </div>
    </template>
  </section>
</template>
