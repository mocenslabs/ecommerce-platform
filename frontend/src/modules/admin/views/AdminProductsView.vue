```vue
<script setup>
import {
  ref,
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

import AdminStatsCard from
  '@/modules/admin/components/AdminStatsCard.vue'

const adminStore =
  useAdminStore()

const {
  products,
  categories,
  brands,
} = storeToRefs(
  adminStore
)

const showForm = ref(false)

const editingId = ref(null)

const form = ref({
  name: '',
  short_description: '',
  description: '',
  category: '',
  brand: '',
  is_featured: false,
  is_active: true,
})

onMounted(async () => {
  await adminStore.fetchProducts()

  await adminStore.fetchCategories()

  await adminStore.fetchBrands()
})

const resetForm = () => {
  editingId.value = null

  form.value = {
    name: '',
    short_description: '',
    description: '',
    category: '',
    brand: '',
    is_featured: false,
    is_active: true,
  }
}

const createProduct = async () => {
  await adminStore.createProduct(
    form.value
  )

  resetForm()

  showForm.value = false
}

const editProduct = (
  product
) => {
  editingId.value =
    product.id

  form.value = {
    name: product.name,
    short_description:
      product.short_description,
    description:
      product.description ?? '',
    category:
      product.category,
    brand:
      product.brand,
    is_featured:
      product.is_featured,
    is_active:
      product.is_active,
  }

  showForm.value = true
}

const updateProduct =
  async () => {
    await adminStore.updateProduct(
      editingId.value,
      form.value
    )

    resetForm()

    showForm.value = false
  }

const deleteProduct =
  async (id) => {
    if (
      !confirm(
        'Delete product?'
      )
    )
      return

    await adminStore.deleteProduct(
      id
    )
  }
</script>

<template>
  <section>
    <AdminPageHeader
      title="Products"
      subtitle="Manage your catalog products."
    />

    <!-- KPI Cards -->

    <div
      class="mb-8 grid gap-4 md:grid-cols-2 xl:grid-cols-4"
    >
      <AdminStatsCard
        title="Products"
        :value="products.length"
      />

      <AdminStatsCard
        title="Categories"
        :value="categories.length"
      />

      <AdminStatsCard
        title="Brands"
        :value="brands.length"
      />

      <AdminStatsCard
        title="Featured"
        :value="
          products.filter(
            p => p.is_featured
          ).length
        "
      />
    </div>

    <!-- Toolbar -->

    <div
      class="mb-6 flex flex-col gap-4 md:flex-row md:items-center md:justify-between"
    >
      <input
        type="text"
        placeholder="Search products..."
        class="w-full rounded-xl border border-slate-300 px-4 py-3 md:max-w-md"
      >

      <button
        class="rounded-xl bg-slate-900 px-5 py-3 text-white transition hover:opacity-90"
        @click="
          () => {
            resetForm()
            showForm = true
          }
        "
      >
        New Product
      </button>
    </div>

    <!-- Form -->

    <div
      v-if="showForm"
      class="mb-8 rounded-2xl border border-slate-200 bg-white p-6 shadow-sm dark:border-slate-800 dark:bg-slate-900"
    >
      <h2
        class="mb-6 text-xl font-semibold"
      >
        {{
          editingId
            ? 'Edit Product'
            : 'Create Product'
        }}
      </h2>

      <div
        class="grid gap-4"
      >
        <input
          v-model="form.name"
          placeholder="Name"
          class="rounded-xl border p-3"
        >

        <input
          v-model="
            form.short_description
          "
          placeholder="Short Description"
          class="rounded-xl border p-3"
        >

        <textarea
          v-model="
            form.description
          "
          placeholder="Description"
          rows="4"
          class="rounded-xl border p-3"
        />

        <select
          v-model="
            form.category
          "
          class="rounded-xl border p-3"
        >
          <option value="">
            Select Category
          </option>

          <option
            v-for="category in categories"
            :key="category.id"
            :value="
              category.id
            "
          >
            {{ category.name }}
          </option>
        </select>

        <select
          v-model="form.brand"
          class="rounded-xl border p-3"
        >
          <option value="">
            Select Brand
          </option>

          <option
            v-for="brand in brands"
            :key="brand.id"
            :value="
              brand.id
            "
          >
            {{ brand.name }}
          </option>
        </select>

        <label
          class="flex items-center gap-2"
        >
          <input
            v-model="
              form.is_featured
            "
            type="checkbox"
          >

          Featured
        </label>

        <label
          class="flex items-center gap-2"
        >
          <input
            v-model="
              form.is_active
            "
            type="checkbox"
          >

          Active
        </label>

        <div
          class="flex flex-wrap gap-3"
        >
          <button
            v-if="
              !editingId
            "
            class="rounded-xl bg-green-600 px-4 py-2 text-white"
            @click="
              createProduct
            "
          >
            Create
          </button>

          <button
            v-else
            class="rounded-xl bg-blue-600 px-4 py-2 text-white"
            @click="
              updateProduct
            "
          >
            Update
          </button>

          <button
            class="rounded-xl bg-slate-500 px-4 py-2 text-white"
            @click="
              () => {
                resetForm()
                showForm = false
              }
            "
          >
            Cancel
          </button>
        </div>
      </div>
    </div>

    <!-- Products -->

    <div
      class="space-y-4"
    >
      <div
        v-for="product in products"
        :key="product.id"
        class="rounded-2xl border border-slate-200 bg-white p-5 shadow-sm dark:border-slate-800 dark:bg-slate-900"
      >
        <div
          class="flex flex-col gap-4 md:flex-row md:items-center md:justify-between"
        >
          <div>
            <h2
              class="text-lg font-bold"
            >
              {{ product.name }}
            </h2>

            <p
              class="mt-1 text-sm text-slate-500"
            >
              {{
                product.short_description
              }}
            </p>

            <div
              class="mt-3 flex flex-wrap gap-2"
            >
              <span
                class="rounded-full bg-slate-100 px-3 py-1 text-xs"
              >
                {{
                  product.category_name
                }}
              </span>

              <span
                class="rounded-full bg-slate-100 px-3 py-1 text-xs"
              >
                {{
                  product.brand_name
                }}
              </span>

              <span
                v-if="
                  product.is_featured
                "
                class="rounded-full bg-yellow-100 px-3 py-1 text-xs font-medium text-yellow-700"
              >
                Featured
              </span>

              <span
                v-if="
                  product.is_active
                "
                class="rounded-full bg-green-100 px-3 py-1 text-xs font-medium text-green-700"
              >
                Active
              </span>

              <span
                v-else
                class="rounded-full bg-red-100 px-3 py-1 text-xs font-medium text-red-700"
              >
                Inactive
              </span>
            </div>
          </div>

          <div
            class="flex gap-2"
          >
            <button
              class="rounded-xl bg-blue-600 px-4 py-2 text-white"
              @click="
                editProduct(
                  product
                )
              "
            >
              Edit
            </button>

            <button
              class="rounded-xl bg-red-600 px-4 py-2 text-white"
              @click="
                deleteProduct(
                  product.id
                )
              "
            >
              Delete
            </button>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
```
