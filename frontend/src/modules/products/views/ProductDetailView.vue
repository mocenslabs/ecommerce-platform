<script setup>
import {
  computed,
  onMounted,
} from 'vue'

import {
  useRoute,
} from 'vue-router'

import {
  storeToRefs,
} from 'pinia'

import {
  useProductsStore,
} from '@/stores/products.store'

import {
  useCartStore,
} from '@/stores/cart.store'

import {
  useWishlistStore,
} from '@/stores/wishlist.store'

const wishlistStore =
  useWishlistStore()

async function addToWishlist() {
  await wishlistStore.addProduct(
    currentProduct.value.id,
  )
}

const route = useRoute()

const productsStore =
  useProductsStore()

const cartStore =
  useCartStore()

const {
  currentProduct,
  loading,
} = storeToRefs(
  productsStore,
)

onMounted(() => {
  productsStore.fetchProduct(
    route.params.slug,
  )
})

const primaryImage = computed(() => {
  return (
    currentProduct.value?.images?.[0]
      ?.image ??
    'https://placehold.co/900x700'
  )
})

const addToCart = async () => {
  const variant =
    currentProduct.value
      ?.variants?.[0]

  if (!variant) {
    return
  }

  await cartStore.addItem(
    variant.id,
    1,
  )
}
</script>

<template>
  <section class="mx-auto max-w-7xl px-4 py-12">
    <div v-if="loading" class="py-20 text-center">
      Loading...
    </div>

    <div v-else-if="currentProduct" class="grid gap-12 lg:grid-cols-2">
      <div>
        <img :src="primaryImage" :alt="currentProduct.name" class="w-full rounded-2xl">
      </div>

      <div>
        <p class="text-sm uppercase tracking-wide text-slate-500">
          {{ currentProduct.brand?.name }}
        </p>

        <h1 class="mt-2 text-4xl font-bold">
          {{ currentProduct.name }}
        </h1>

        <p class="mt-4 text-slate-500">
          {{ currentProduct.category?.name }}
        </p>

        <p class="mt-6 text-lg">
          {{ currentProduct.description }}
        </p>

        <div class="mt-8">
          <span class="text-3xl font-bold">
            ${{ currentProduct.variants?.[0]?.price }}
          </span>
        </div>

        <div class="mt-8 flex gap-4">
          <button class="rounded-xl bg-black px-6 py-3 text-white dark:bg-white dark:text-black">
            Add To Cart
          </button>

          <button class="rounded-xl border px-6 py-3" @click="addToWishlist">
            Add To Wishlist
          </button>
        </div>
      </div>
    </div>
  </section>
</template>
