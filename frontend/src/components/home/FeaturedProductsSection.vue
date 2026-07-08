<script setup>
import {
  onMounted,
} from 'vue'

import {
  storeToRefs,
} from 'pinia'

import ProductGrid from '@/components/products/ProductGrid.vue'

import {
  useProductsStore,
} from '@/stores/products.store'

const productsStore =
  useProductsStore()

const {
  featuredProducts,
} = storeToRefs(productsStore)

onMounted(() => {
  productsStore.fetchFeaturedProducts()
})
</script>

<template>
  <section
    class="mx-auto max-w-7xl px-4 py-20"
  >
    <h2
      class="mb-10 text-3xl font-bold"
    >
      Featured Products
    </h2>

    <ProductGrid
      :products="featuredProducts"
    />
  </section>
</template>
