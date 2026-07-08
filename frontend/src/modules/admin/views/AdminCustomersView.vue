<script setup>
import {
  onMounted,
} from 'vue'

import {
  storeToRefs,
} from 'pinia'

import {
  useAdminStore,
} from '@/stores/admin.store'

import AdminCard from
  '@/modules/admin/components/AdminCard.vue'

import AdminEmptyState from
  '@/modules/admin/components/AdminEmptyState.vue'

const adminStore =
  useAdminStore()

const {
  customers,
} = storeToRefs(
  adminStore
)

onMounted(() => {
  adminStore.fetchCustomers()
})
</script>

<template>
  <section
    class="space-y-6"
  >
    <div>
      <h1
        class="text-3xl font-bold text-slate-900 dark:text-white"
      >
        Customers
      </h1>

      <p
        class="mt-1 text-slate-500"
      >
        Manage registered customers
      </p>
    </div>

    <div
      v-if="customers.length === 0"
    >
      <AdminEmptyState
        title="No customers found"
        description="Customers will appear here after registration."
      />
    </div>

    <div
      v-else
      class="grid gap-4 md:grid-cols-2 xl:grid-cols-3"
    >
      <AdminCard
        v-for="customer in customers"
        :key="customer.id"
      >
        <div
          class="space-y-3"
        >
          <div>
            <h3
              class="font-semibold text-slate-900 dark:text-white"
            >
              {{ customer.first_name }}
              {{ customer.last_name }}
            </h3>

            <p
              class="text-sm text-slate-500"
            >
              {{ customer.email }}
            </p>
          </div>

          <div
            class="grid grid-cols-2 gap-3 text-sm"
          >
            <div>
              <p
                class="text-slate-500"
              >
                Orders
              </p>

              <p
                class="font-semibold"
              >
                {{ customer.orders_count }}
              </p>
            </div>

            <div>
              <p
                class="text-slate-500"
              >
                Total Spent
              </p>

              <p
                class="font-semibold"
              >
                $
                {{ customer.total_spent || 0 }}
              </p>
            </div>
          </div>

          <div>
            <span
              :class="[
                'rounded-full px-3 py-1 text-xs font-medium',
                customer.is_verified
                  ? 'bg-green-100 text-green-700'
                  : 'bg-yellow-100 text-yellow-700',
              ]"
            >
              {{
                customer.is_verified
                  ? 'Verified'
                  : 'Pending Verification'
              }}
            </span>
          </div>
        </div>
      </AdminCard>
    </div>
  </section>
</template>
