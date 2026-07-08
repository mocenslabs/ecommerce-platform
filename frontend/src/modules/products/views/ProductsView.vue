<script setup>
import {
  computed,
  onMounted,
} from 'vue'

import {
  storeToRefs,
} from 'pinia'

import ProductGrid from '@/components/products/ProductGrid.vue'
import ProductSearch from '@/components/products/ProductSearch.vue'
import ProductSort from '@/components/products/ProductSort.vue'

import {
  useProductsStore,
} from '@/stores/products.store'

const productsStore =
  useProductsStore()

const {
  products,
} = storeToRefs(
  productsStore,
)

const search = computed({
  get: () =>
    productsStore.filters.search,

  set: value =>
    productsStore.updateSearch(
      value,
    ),
})

const ordering = computed({
  get: () =>
    productsStore.filters.ordering,

  set: value =>
    productsStore.updateOrdering(
      value,
    ),
})

onMounted(() => {
  productsStore.fetchProducts()
})
</script>

<template>
  <section
    class="mx-auto max-w-7xl px-4 py-12"
  >
    <h1
      class="mb-8 text-4xl font-bold"
    >
      Products
    </h1>

    <div
      class="mb-8 grid gap-4 md:grid-cols-2"
    >
      <ProductSearch
        v-model="search"
      />

      <ProductSort
        v-model="ordering"
      />
    </div>

    <ProductGrid
      :products="products"
    />
  </section>
</template>
