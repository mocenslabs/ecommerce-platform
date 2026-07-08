<script setup>
import {
  onMounted,
} from 'vue'

import {
  storeToRefs,
} from 'pinia'

import {
  useAdminStore,
} from '@/stores/admin.store'

import AdminPageHeader from
  '@/modules/admin/components/AdminPageHeader.vue'

import AdminEmptyState from
  '@/modules/admin/components/AdminEmptyState.vue'

const adminStore =
  useAdminStore()

const {
  brands,
} = storeToRefs(
  adminStore,
)

onMounted(async () => {
  await adminStore.fetchBrands()
})
</script>

<template>
  <section>
    <AdminPageHeader
      title="Brands"
      subtitle="Manage product brands."
    />

    <AdminEmptyState
      v-if="!brands.length"
      title="No brands found"
      description="Brands will appear here once they are created."
    />

    <div
      v-else
      class="grid gap-4 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4"
    >
      <div
        v-for="brand in brands"
        :key="brand.id"
        class="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm transition hover:shadow-md dark:border-slate-800 dark:bg-slate-900"
      >
        <h3
          class="text-lg font-semibold"
        >
          {{ brand.name }}
        </h3>

        <p
          class="mt-2 text-sm text-slate-500"
        >
          Product brand
        </p>
      </div>
    </div>
  </section>
</template>
