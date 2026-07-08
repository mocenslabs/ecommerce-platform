<script setup>
import {
  onMounted,
} from 'vue'

import {
  storeToRefs,
} from 'pinia'

import {
  useCartStore,
} from '@/stores/cart.store'

const cartStore =
  useCartStore()

const {
  items,
  subtotal,
  loading,
} = storeToRefs(
  cartStore,
)

onMounted(() => {
  cartStore.fetchCart()
})

const removeItem = async (
  id,
) => {
  await cartStore.removeItem(
    id,
  )
}
</script>

<template>
  <section
    class="mx-auto max-w-6xl px-4 py-12"
  >
    <h1
      class="mb-8 text-4xl font-bold"
    >
      Cart
    </h1>

    <div
      v-if="loading"
    >
      Loading...
    </div>

    <div
      v-else-if="!items.length"
    >
      Your cart is empty.
    </div>

    <div
      v-else
      class="space-y-4"
    >
      <div
        v-for="item in items"
        :key="item.id"
        class="flex items-center justify-between rounded-xl border p-4"
      >
        <div>
          <h3
            class="font-semibold"
          >
            {{ item.product_name }}
          </h3>

          <p
            class="text-sm text-slate-500"
          >
            Quantity:
            {{ item.quantity }}
          </p>

          <p
            class="text-sm text-slate-500"
          >
            Price:
            ${{ item.price }}
          </p>
        </div>

        <div
          class="text-right"
        >
          <p
            class="font-bold"
          >
            ${{ item.subtotal }}
          </p>

          <button
            class="mt-2 text-red-500"
            @click="
              removeItem(
                item.id,
              )
            "
          >
            Remove
          </button>
        </div>
      </div>

      <div
        class="border-t pt-6"
      >
        <p
          class="text-2xl font-bold"
        >
          Total:
          ${{ subtotal }}
        </p>
      </div>
    </div>
  </section>
</template>
