<script setup>
import { onMounted } from 'vue'

import {
  useAdminStore,
} from '@/stores/admin.store'

import AdminPageHeader from
  '@/modules/admin/components/AdminPageHeader.vue'

import AdminTable from
  '@/modules/admin/components/AdminTable.vue'

const adminStore =
  useAdminStore()

const saveInventory =
  async (item) => {
    await adminStore.updateInventory(
      item.id,
      {
        quantity:
          item.quantity,
      },
    )
  }

const stockStatus =
  (available) => {
    if (available <= 0) {
      return 'out'
    }

    if (available <= 20) {
      return 'low'
    }

    return 'ok'
  }

onMounted(async () => {
  await adminStore.fetchInventory()
})
</script>

<template>
  <section>
    <AdminPageHeader
      title="Inventory"
      subtitle="Manage stock levels and product availability."
    />

    <!-- KPI Cards -->

    <div
      class="mb-8 grid gap-4 sm:grid-cols-2 xl:grid-cols-4"
    >
      <div
        class="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm dark:border-slate-800 dark:bg-slate-900"
      >
        <p
          class="text-sm text-slate-500"
        >
          Total SKUs
        </p>

        <h3
          class="mt-2 text-3xl font-bold"
        >
          {{
            adminStore.inventory.length
          }}
        </h3>
      </div>

      <div
        class="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm dark:border-slate-800 dark:bg-slate-900"
      >
        <p
          class="text-sm text-slate-500"
        >
          Low Stock
        </p>

        <h3
          class="mt-2 text-3xl font-bold"
        >
          {{
            adminStore.inventory.filter(
              item =>
                item.available_quantity > 0 &&
                item.available_quantity <= 20,
            ).length
          }}
        </h3>
      </div>

      <div
        class="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm dark:border-slate-800 dark:bg-slate-900"
      >
        <p
          class="text-sm text-slate-500"
        >
          Out of Stock
        </p>

        <h3
          class="mt-2 text-3xl font-bold"
        >
          {{
            adminStore.inventory.filter(
              item =>
                item.available_quantity === 0,
            ).length
          }}
        </h3>
      </div>

      <div
        class="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm dark:border-slate-800 dark:bg-slate-900"
      >
        <p
          class="text-sm text-slate-500"
        >
          Total Units
        </p>

        <h3
          class="mt-2 text-3xl font-bold"
        >
          {{
            adminStore.inventory.reduce(
              (total, item) =>
                total + item.quantity,
              0,
            )
          }}
        </h3>
      </div>
    </div>

    <!-- Inventory Table -->

    <AdminTable
      :columns="[
        'SKU',
        'Quantity',
        'Reserved',
        'Available',
        'Status',
        'Actions',
      ]"
    >
      <tr
        v-for="item in adminStore.inventory"
        :key="item.id"
        class="border-b border-slate-200 dark:border-slate-800"
      >
        <td
          class="px-4 py-4 font-mono text-sm"
        >
          {{ item.sku }}
        </td>

        <td
          class="px-4 py-4"
        >
          <input
            v-model.number="item.quantity"
            type="number"
            min="0"
            class="w-24 rounded-lg border border-slate-300 bg-transparent p-2"
          />
        </td>

        <td
          class="px-4 py-4"
        >
          {{ item.reserved_quantity }}
        </td>

        <td
          class="px-4 py-4 font-medium"
        >
          {{ item.available_quantity }}
        </td>

        <td
          class="px-4 py-4"
        >
          <span
            v-if="stockStatus(item.available_quantity) === 'ok'"
            class="rounded-full bg-green-100 px-3 py-1 text-xs font-medium text-green-700"
          >
            Healthy
          </span>

          <span
            v-else-if="stockStatus(item.available_quantity) === 'low'"
            class="rounded-full bg-yellow-100 px-3 py-1 text-xs font-medium text-yellow-700"
          >
            Low Stock
          </span>

          <span
            v-else
            class="rounded-full bg-red-100 px-3 py-1 text-xs font-medium text-red-700"
          >
            Out of Stock
          </span>
        </td>

        <td
          class="px-4 py-4"
        >
          <button
            class="rounded-lg bg-slate-900 px-4 py-2 text-sm font-medium text-white transition hover:opacity-90"
            @click="saveInventory(item)"
          >
            Save
          </button>
        </td>
      </tr>
    </AdminTable>
  </section>
</template>
