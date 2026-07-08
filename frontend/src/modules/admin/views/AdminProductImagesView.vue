<script setup>
import {
  ref,
  onMounted,
} from 'vue'

import {
  useAdminStore,
} from '@/stores/admin.store'

import AdminPageHeader from
  '@/modules/admin/components/AdminPageHeader.vue'

import AdminEmptyState from
  '@/modules/admin/components/AdminEmptyState.vue'

const adminStore =
  useAdminStore()

const selectedFile =
  ref(null)

const productId =
  ref('')

const altText =
  ref('')

const isPrimary =
  ref(false)

const sortOrder =
  ref(0)

const handleFileChange = (
  event
) => {
  selectedFile.value =
    event.target.files[0]
}

const uploadImage =
  async () => {
    if (
      !selectedFile.value ||
      !productId.value
    ) {
      return
    }

    const formData =
      new FormData()

    formData.append(
      'product',
      productId.value
    )

    formData.append(
      'image',
      selectedFile.value
    )

    formData.append(
      'alt_text',
      altText.value
    )

    formData.append(
      'is_primary',
      isPrimary.value
    )

    formData.append(
      'sort_order',
      sortOrder.value
    )

    await adminStore.createProductImage(
      formData
    )

    selectedFile.value = null
    productId.value = ''
    altText.value = ''
    isPrimary.value = false
    sortOrder.value = 0
  }

const removeImage =
  async (id) => {
    if (
      !confirm(
        'Delete image?'
      )
    ) {
      return
    }

    await adminStore.deleteProductImage(
      id
    )
  }

onMounted(async () => {
  await Promise.all([
    adminStore.fetchProducts(),
    adminStore.fetchProductImages(),
  ])
})
</script>

<template>
  <section>
    <AdminPageHeader
      title="Product Images"
      subtitle="Manage product galleries and visual assets."
    />

    <!-- Upload -->

    <div
      class="mb-8 rounded-2xl border border-slate-200 bg-white p-6 shadow-sm dark:border-slate-800 dark:bg-slate-900"
    >
      <h2
        class="mb-6 text-lg font-semibold"
      >
        Upload Image
      </h2>

      <div
        class="grid gap-4 md:grid-cols-2"
      >
        <select
          v-model="productId"
          class="rounded-xl border p-3"
        >
          <option value="">
            Select Product
          </option>

          <option
            v-for="product in adminStore.products"
            :key="product.id"
            :value="product.id"
          >
            {{ product.name }}
          </option>
        </select>

        <input
          type="file"
          class="rounded-xl border p-3"
          @change="handleFileChange"
        />

        <input
          v-model="altText"
          placeholder="Alt text"
          class="rounded-xl border p-3"
        />

        <input
          v-model="sortOrder"
          type="number"
          placeholder="Sort order"
          class="rounded-xl border p-3"
        />

        <label
          class="flex items-center gap-2"
        >
          <input
            v-model="isPrimary"
            type="checkbox"
          />

          Primary Image
        </label>
      </div>

      <button
        class="mt-6 rounded-xl bg-slate-900 px-5 py-3 text-white transition hover:opacity-90"
        @click="uploadImage"
      >
        Upload Image
      </button>
    </div>

    <!-- Empty State -->

    <AdminEmptyState
      v-if="
        !adminStore.productImages.length
      "
      title="No images uploaded"
      description="Product images will appear here after upload."
    />

    <!-- Gallery -->

    <div
      v-else
      class="grid gap-6 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4"
    >
      <div
        v-for="image in adminStore.productImages"
        :key="image.id"
        class="overflow-hidden rounded-2xl border border-slate-200 bg-white shadow-sm transition hover:shadow-md dark:border-slate-800 dark:bg-slate-900"
      >
        <img
          :src="image.image"
          class="h-56 w-full object-cover"
        />

        <div
          class="space-y-2 p-4"
        >
          <h3
            class="font-semibold"
          >
            {{
              image.product_name
            }}
          </h3>

          <div
            class="text-sm text-slate-500"
          >
            Sort:
            {{ image.sort_order }}
          </div>

          <div
            v-if="
              image.is_primary
            "
            class="inline-flex rounded-full bg-green-100 px-3 py-1 text-xs font-medium text-green-700"
          >
            Primary
          </div>

          <button
            class="mt-3 w-full rounded-xl bg-red-600 px-4 py-2 text-white transition hover:bg-red-700"
            @click="
              removeImage(
                image.id
              )
            "
          >
            Delete
          </button>
        </div>
      </div>
    </div>
  </section>
</template>
