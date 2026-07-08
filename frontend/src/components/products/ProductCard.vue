<script setup>
import BaseCard from '@/components/ui/BaseCard.vue'

defineProps({
  product: {
    type: Object,
    required: true,
  },
})

const getImage = product => {
  return (
    product.primary_image?.image ??
    'https://placehold.co/600x400'
  )
}

const hasRating = product => {
  return Number(
    product.average_rating,
  ) > 0
}
</script>

<template>
  <BaseCard
    class="transition duration-300 hover:-translate-y-1 hover:shadow-xl"
  >
    <RouterLink
      :to="`/products/${product.slug}`"
    >
      <img
        :src="getImage(product)"
        :alt="product.name"
        class="h-56 w-full rounded-xl object-cover"
      >

      <div class="mt-4">
        <p
          class="text-xs uppercase tracking-wide text-slate-500"
        >
          {{ product.brand?.name }}
        </p>

        <h3
          class="mt-1 text-lg font-semibold"
        >
          {{ product.name }}
        </h3>

        <p
          class="mt-2 text-sm text-slate-500"
        >
          {{ product.short_description }}
        </p>

        <div
          class="mt-4 flex items-center justify-between"
        >
          <span
            class="text-sm text-slate-400"
          >
            {{ product.category?.name }}
          </span>

          <span
            v-if="hasRating(product)"
            class="text-sm"
          >
            ⭐ {{ product.average_rating }}
          </span>
        </div>

        <div
          class="mt-4 flex items-center justify-between"
        >
          <span
            class="text-xl font-bold"
          >
            ${{ product.price }}
          </span>
        </div>
      </div>
    </RouterLink>
  </BaseCard>
</template>
