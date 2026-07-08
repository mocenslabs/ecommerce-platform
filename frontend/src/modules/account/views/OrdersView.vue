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
  useAccountStore,
} from '@/stores/account.store'

const accountStore =
  useAccountStore()

const {
  orders,
  loading,
} = storeToRefs(
  accountStore,
)

onMounted(() => {
  accountStore.fetchOrders()
})
</script>

<template>
  <section
    class="mx-auto max-w-6xl px-4 py-12"
  >
    <h1
      class="mb-8 text-4xl font-bold"
    >
      My Orders
    </h1>


<div
  v-if="loading"
  class="text-center"
>
  Loading...
</div>

<div
  v-else-if="orders.length"
  class="space-y-4"
>
  <RouterLink
    v-for="order in orders"
    :key="order.id"
    :to="`/account/orders/${order.order_number}`"
    class="block rounded-xl border p-6 transition hover:bg-slate-50 dark:hover:bg-slate-900"
  >
    <div
      class="flex items-center justify-between"
    >
      <span class="font-semibold">
        {{ order.order_number }}
      </span>

      <span>
        ${{ order.total_amount }}
      </span>
    </div>

    <div
      class="mt-2 text-sm text-slate-500"
    >
      {{ order.status }}
    </div>
  </RouterLink>
</div>

<div
  v-else
  class="rounded-xl border p-8 text-center"
>
  No orders found.
</div>


  </section>
</template>
