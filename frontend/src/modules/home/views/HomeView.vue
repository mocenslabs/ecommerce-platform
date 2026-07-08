<script setup>
import BaseButton from '@/components/ui/BaseButton.vue'

import FeaturedProductsSection
  from '@/components/home/FeaturedProductsSection.vue'
</script>

<template>
  <section
    class="mx-auto max-w-7xl px-4 py-24"
  >
    <div
      class="mx-auto max-w-4xl text-center"
    >
      <h1
        class="text-5xl font-bold tracking-tight md:text-7xl"
      >
        Premium
        E-Commerce
        Platform
      </h1>

      <p
        class="mt-8 text-lg text-slate-600 dark:text-slate-400"
      >
        Built with Vue 3,
        Django, TailwindCSS
        and modern architecture.
      </p>

      <div
        class="mt-10 flex flex-col items-center justify-center gap-4 sm:flex-row"
      >
        <BaseButton>
          Shop Now
        </BaseButton>

        <BaseButton
          variant="secondary"
        >
          Explore Products
        </BaseButton>

      </div>
    </div>
  </section>
  <FeaturedProductsSection />
</template>
