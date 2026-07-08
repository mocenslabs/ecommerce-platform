<script setup>
import { onMounted } from 'vue'
import { useTheme } from '@/composables/useTheme'
import {
  useCartStore,
} from '@/stores/cart.store'

const cartStore =
  useCartStore()

const {
  initializeTheme,
} = useTheme()

onMounted(async () => {
  initializeTheme()

  await cartStore.fetchCart()
})


</script>

<template>
  <router-view />
</template>
