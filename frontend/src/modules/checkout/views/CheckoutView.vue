<script setup>
import {
  ref,
  onMounted,
} from 'vue'

import {
  storeToRefs,
} from 'pinia'

import {
  useOrderStore,
} from '@/stores/order.store'

const orderStore =
  useOrderStore()

const {
  addresses,
  shippingMethods,
  checkoutLoading,
  lastOrder,
} = storeToRefs(
  orderStore,
)

const shippingAddress =
  ref('')

const shippingMethod =
  ref('')

onMounted(async () => {
  await Promise.all([
    orderStore.fetchAddresses(),
    orderStore.fetchShippingMethods(),
  ])
})

async function submitCheckout() {
  await orderStore.checkout({
    shipping_address_id:
      shippingAddress.value,

    shipping_method_id:
      shippingMethod.value,
  })
}
</script>

<template>
  <section
    class="mx-auto max-w-4xl px-4 py-12"
  >
    <h1
      class="mb-8 text-3xl font-bold"
    >
      Checkout
    </h1>

    <div
      class="space-y-6 rounded-2xl border p-6"
    >
      <div>
        <label
          class="mb-2 block"
        >
          Shipping Address
        </label>

        <select
          v-model="
            shippingAddress
          "
          class="w-full rounded-xl border p-3"
        >
          <option value="">
            Select address
          </option>

          <option
            v-for="address in addresses"
            :key="address.id"
            :value="address.id"
          >
            {{ address.line_1 }}
            -
            {{ address.city }}
          </option>
        </select>
      </div>

      <div>
        <label
          class="mb-2 block"
        >
          Shipping Method
        </label>

        <select
          v-model="
            shippingMethod
          "
          class="w-full rounded-xl border p-3"
        >
          <option value="">
            Select shipping
          </option>

          <option
            v-for="method in shippingMethods"
            :key="method.id"
            :value="method.id"
          >
            {{ method.name }}
            -
            ${{ method.price }}
          </option>
        </select>
      </div>

      <button
        :disabled="
          checkoutLoading
        "
        @click="
          submitCheckout
        "
        class="rounded-xl bg-black px-6 py-3 text-white dark:bg-white dark:text-black"
      >
        {{
          checkoutLoading
            ? 'Processing...'
            : 'Place Order'
        }}
      </button>
    </div>

    <div
      v-if="lastOrder"
      class="mt-8 rounded-2xl border p-6"
    >
      <h2
        class="mb-4 text-xl font-bold"
      >
        Order Created
      </h2>

      <p>
        Order:
        {{ lastOrder.order_id }}
      </p>

      <p>
        Status:
        {{ lastOrder.status }}
      </p>

      <p>
        Total:
        ${{ lastOrder.total }}
      </p>
    </div>
  </section>
</template>
