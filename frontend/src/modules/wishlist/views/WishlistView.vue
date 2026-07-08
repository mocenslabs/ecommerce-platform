<script setup>
import {
  onMounted,
} from 'vue'

import {
  storeToRefs,
} from 'pinia'

import {
  useWishlistStore,
} from '@/stores/wishlist.store'

const wishlistStore =
  useWishlistStore()

const {
  items,
  loading,
} = storeToRefs(
  wishlistStore,
)

onMounted(() => {
  wishlistStore.fetchWishlist()
})
</script>

<template>
  <section
    class="mx-auto max-w-6xl px-4 py-12"
  >
    <h1
      class="mb-8 text-4xl font-bold"
    >
      Wishlist
    </h1>

    <div
      v-if="loading"
      class="text-center"
    >
      Loading...
    </div>

    <div
      v-else-if="items.length"
      class="grid gap-6"
    >
      <div
        v-for="item in items"
        :key="item.id"
        class="rounded-2xl border p-6"
      >
        <h2
          class="font-semibold"
        >
          {{ item.product.name }}
        </h2>

        <p
          class="mt-2 text-slate-500"
        >
          {{ item.product.category?.name }}
        </p>
      </div>
    </div>

    <div
      v-else
      class="text-slate-500"
    >
      Your wishlist is empty.
    </div>
  </section>
</template>
