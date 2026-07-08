<script setup>
import { onMounted } from 'vue'

import { RouterLink } from 'vue-router'

import {
  useAdminStore,
} from '@/stores/admin.store'

import AdminPageHeader from
  '@/modules/admin/components/AdminPageHeader.vue'

import AdminTable from
  '@/modules/admin/components/AdminTable.vue'

const adminStore =
  useAdminStore()

onMounted(() => {
  adminStore.fetchOrders()
})
</script>

<template>
  <section>
    <AdminPageHeader
      title="Orders"
      subtitle="Manage customer orders and order status."
    />

    <AdminTable
      :columns="[
        'Order',
        'Customer',
        'Status',
        'Total',
        'Actions',
      ]"
    >
      <tr
        v-for="order in adminStore.orders"
        :key="order.id"
        class="border-b border-slate-200 dark:border-slate-800"
      >
        <td
          class="px-4 py-4"
        >
          <span
            class="font-mono text-sm"
          >
            {{ order.order_number }}
          </span>
        </td>

        <td
          class="px-4 py-4"
        >
          {{ order.customer_email }}
        </td>

        <td
          class="px-4 py-4"
        >
          <span
            class="rounded-full bg-slate-100 px-3 py-1 text-xs font-medium dark:bg-slate-800"
          >
            {{ order.status }}
          </span>
        </td>

        <td
          class="px-4 py-4 font-semibold"
        >
          $
          {{ order.total_amount }}
        </td>

        <td
          class="px-4 py-4"
        >
          <RouterLink
            :to="`/admin/orders/${order.id}`"
            class="inline-flex rounded-lg bg-slate-900 px-4 py-2 text-sm font-medium text-white transition hover:opacity-90"
          >
            View Details
          </RouterLink>
        </td>
      </tr>
    </AdminTable>
  </section>
</template>
