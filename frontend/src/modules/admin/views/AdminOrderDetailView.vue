<script setup>
import {
  onMounted,
  computed,
  ref,
} from 'vue'

import {
  useRoute,
  useRouter,
} from 'vue-router'

import {
  useAdminStore,
} from '@/stores/admin.store'

const route = useRoute()

const router = useRouter()

const adminStore =
  useAdminStore()

const status = ref('')

const order = computed(() =>
  adminStore.currentOrder
)

const saveStatus =
  async () => {
    await adminStore.updateOrder(
      order.value.id,
      {
        status: status.value,
      }
    )

    alert(
      'Order updated successfully'
    )
  }

const goBack = () => {
  router.push(
    '/admin/orders'
  )
}

onMounted(async () => {
  await adminStore.fetchOrder(
    route.params.id
  )

  status.value =
    adminStore.currentOrder?.status
})
</script>

<template>
  <section
    class="mx-auto max-w-6xl px-4 py-10"
  >
    <div
      class="mb-8 flex items-center justify-between"
    >
      <h1
        class="text-3xl font-bold"
      >
        Order Detail
      </h1>

      <button
        class="rounded-lg border px-4 py-2 hover:bg-slate-100"
        @click="goBack"
      >
        ← Back to Orders
      </button>
    </div>

    <div
      v-if="order"
      class="space-y-6"
    >
      <div
        class="rounded-xl border p-6"
      >
        <h2
          class="mb-4 text-xl font-semibold"
        >
          Order Information
        </h2>

        <div
          class="grid gap-4 md:grid-cols-2"
        >
          <div>
            <strong>
              Order Number:
            </strong>

            {{ order.order_number }}
          </div>

          <div>
            <strong>
              Customer:
            </strong>

            {{ order.customer_email }}
          </div>

          <div>
            <strong>
              Total:
            </strong>

            $
            {{ order.total_amount }}
          </div>

          <div>
            <strong>
              Created:
            </strong>

            {{ order.created_at }}
          </div>
        </div>
      </div>

      <div
        class="rounded-xl border p-6"
      >
        <h2
          class="mb-4 text-xl font-semibold"
        >
          Order Status
        </h2>

        <div
          class="flex flex-wrap items-center gap-4"
        >
          <select
            v-model="status"
            class="rounded border p-3"
          >
            <option value="pending">
              Pending
            </option>

            <option value="paid">
              Paid
            </option>

            <option value="processing">
              Processing
            </option>

            <option value="shipped">
              Shipped
            </option>

            <option value="delivered">
              Delivered
            </option>

            <option value="cancelled">
              Cancelled
            </option>

            <option value="refunded">
              Refunded
            </option>
          </select>

          <button
            class="rounded bg-green-600 px-5 py-3 text-white"
            @click="saveStatus"
          >
            Save Status
          </button>
        </div>
      </div>
    </div>
  </section>
</template>
