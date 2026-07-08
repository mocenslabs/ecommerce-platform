<script setup>
import {
  onMounted,
} from 'vue'

import {
  useRoute,
} from 'vue-router'

import {
  storeToRefs,
} from 'pinia'

import {
  useAccountStore,
} from '@/stores/account.store'

const route =
  useRoute()

const accountStore =
  useAccountStore()

const {
  currentOrder,
  loading,
} = storeToRefs(
  accountStore,
)

onMounted(() => {
  accountStore.fetchOrder(
    route.params.orderNumber,
  )
})
</script>

<template>
  <section
    class="mx-auto max-w-6xl px-4 py-12"
  >
    <div
      v-if="loading"
      class="text-center"
    >
      Loading...
    </div>


<div
  v-else-if="currentOrder"
>
  <h1
    class="mb-6 text-4xl font-bold"
  >
    Order Details
  </h1>

  <div
    class="rounded-xl border p-6"
  >
    <p>
      Number:
      {{ currentOrder.order_number }}
    </p>

    <p>
      Status:
      {{ currentOrder.status }}
    </p>

    <p>
      Subtotal:
      ${{ currentOrder.subtotal_amount }}
    </p>

    <p>
      Shipping:
      ${{ currentOrder.shipping_amount }}
    </p>

    <p>
      Tax:
      ${{ currentOrder.tax_amount }}
    </p>

    <p>
      Discount:
      ${{ currentOrder.discount_amount }}
    </p>

    <p class="mt-2 font-bold">
      Total:
      ${{ currentOrder.total_amount }}
    </p>
  </div>

  <div
    class="mt-8 space-y-4"
  >
    <div
      v-for="item in currentOrder.items"
      :key="item.id"
      class="rounded-xl border p-4"
    >
      <h3
        class="font-semibold"
      >
        {{ item.product_name }}
      </h3>

      <p>
        SKU:
        {{ item.sku }}
      </p>

      <p>
        Quantity:
        {{ item.quantity }}
      </p>

      <p>
        Unit Price:
        ${{ item.unit_price }}
      </p>

      <p class="font-medium">
        Total:
        ${{ item.total_price }}
      </p>
    </div>
  </div>
</div>


  </section>
</template>
