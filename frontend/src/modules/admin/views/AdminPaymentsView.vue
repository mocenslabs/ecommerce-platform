<script setup>
import { onMounted } from 'vue'

import { useAdminStore } from '@/stores/admin.store'

import AdminTable from '@/modules/admin/components/AdminTable.vue'
import AdminEmptyState from '@/modules/admin/components/AdminEmptyState.vue'

const adminStore = useAdminStore()

onMounted(async () => {
  await adminStore.fetchPayments()
})

const columns = [
  'Order',
  'Provider',
  'Status',
  'Amount',
  'External ID',
  'Created',
]
</script>

<template>
  <section class="space-y-6">
    <div>
      <h1 class="text-3xl font-bold">
        Payments
      </h1>

      <p class="mt-1 text-slate-500">
        Payment transactions
      </p>
    </div>

    <AdminEmptyState
      v-if="!adminStore.payments.length"
      title="No payments found"
      description="Payments will appear here when orders are processed."
    />

    <AdminTable
      v-else
      :columns="columns"
    >
      <tr
        v-for="payment in adminStore.payments"
        :key="payment.id"
        class="border-b border-slate-200 dark:border-slate-800"
      >
        <td class="px-4 py-4">
          {{ payment.order_number }}
        </td>

        <td class="px-4 py-4">
          {{ payment.provider }}
        </td>

        <td class="px-4 py-4">
          {{ payment.status }}
        </td>

        <td class="px-4 py-4">
          $ {{ payment.amount }}
        </td>

        <td class="px-4 py-4">
          {{ payment.external_id }}
        </td>

        <td class="px-4 py-4">
          {{ payment.created_at }}
        </td>
      </tr>
    </AdminTable>
  </section>
</template>
