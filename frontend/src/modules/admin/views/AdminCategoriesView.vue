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
  categories,
} = storeToRefs(
  adminStore,
)

onMounted(async () => {
  await adminStore.fetchCategories()
})
</script>

<template>
  <section>
    <AdminPageHeader
      title="Categories"
      subtitle="Manage product categories."
    />

    <AdminEmptyState
      v-if="!categories.length"
      title="No categories found"
      description="Categories will appear here once they are created."
    />

    <div
      v-else
      class="grid gap-4 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4"
    >
      <div
        v-for="category in categories"
        :key="category.id"
        class="rounded-2xl border border-slate-200 bg-white p-6 shadow-sm transition hover:shadow-md dark:border-slate-800 dark:bg-slate-900"
      >
        <h3
          class="text-lg font-semibold"
        >
          {{ category.name }}
        </h3>

        <p
          class="mt-2 text-sm text-slate-500"
        >
          Category ID:
          {{ category.id }}
        </p>
      </div>
    </div>
  </section>
</template>
