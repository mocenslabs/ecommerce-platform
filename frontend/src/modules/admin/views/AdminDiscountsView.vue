<script setup>
import { ref, onMounted } from 'vue'
import { storeToRefs } from 'pinia'

import { useAdminStore } from '@/stores/admin.store'

const adminStore = useAdminStore()

const { discounts } = storeToRefs(adminStore)

const showForm = ref(false)

const editingId = ref(null)

const form = ref({
  code: '',
  discount_type: 'percentage',
  value: '',
  minimum_amount: '',
  usage_limit: '',
  active: true,
  starts_at: '',
  expires_at: '',
})

onMounted(async () => {
  await adminStore.fetchDiscounts()
})

const resetForm = () => {
  editingId.value = null

  form.value = {
    code: '',
    discount_type: 'percentage',
    value: '',
    minimum_amount: '',
    usage_limit: '',
    active: true,
    starts_at: '',
    expires_at: '',
  }
}

const createDiscount = async () => {
  await adminStore.createDiscount(form.value)

  resetForm()

  showForm.value = false
}

const editDiscount = (discount) => {
  editingId.value = discount.id

  form.value = {
    code: discount.code,
    discount_type: discount.discount_type,
    value: discount.value,
    minimum_amount: discount.minimum_amount,
    usage_limit: discount.usage_limit,
    active: discount.active,
    starts_at: discount.starts_at,
    expires_at: discount.expires_at,
  }

  showForm.value = true
}

const updateDiscount = async () => {
  await adminStore.updateDiscount(
    editingId.value,
    form.value
  )

  resetForm()

  showForm.value = false
}

const deleteDiscount = async (id) => {
  if (!confirm('Delete discount?')) {
    return
  }

  await adminStore.deleteDiscount(id)
}
</script>

<template>
  <section class="mx-auto max-w-7xl p-6">
    <div class="mb-6 flex items-center justify-between">
      <h1 class="text-3xl font-bold">
        Discounts
      </h1>

      <button
        class="rounded-lg bg-black px-4 py-2 text-white"
        @click="() => {
          resetForm()
          showForm = true
        }"
      >
        New Discount
      </button>
    </div>

    <div
      v-if="showForm"
      class="mb-8 rounded-xl border p-6"
    >
      <div class="grid gap-4">
        <input
          v-model="form.code"
          placeholder="Code"
          class="rounded border p-2"
        >

        <select
          v-model="form.discount_type"
          class="rounded border p-2"
        >
          <option value="percentage">
            Percentage
          </option>

          <option value="fixed">
            Fixed
          </option>
        </select>

        <input
          v-model="form.value"
          type="number"
          placeholder="Value"
          class="rounded border p-2"
        >

        <input
          v-model="form.minimum_amount"
          type="number"
          placeholder="Minimum Amount"
          class="rounded border p-2"
        >

        <input
          v-model="form.usage_limit"
          type="number"
          placeholder="Usage Limit"
          class="rounded border p-2"
        >

        <input
          v-model="form.starts_at"
          type="datetime-local"
          class="rounded border p-2"
        >

        <input
          v-model="form.expires_at"
          type="datetime-local"
          class="rounded border p-2"
        >

        <label>
          <input
            v-model="form.active"
            type="checkbox"
          >

          Active
        </label>

        <div class="flex gap-3">
          <button
            v-if="!editingId"
            class="rounded bg-green-600 px-4 py-2 text-white"
            @click="createDiscount"
          >
            Create
          </button>

          <button
            v-else
            class="rounded bg-blue-600 px-4 py-2 text-white"
            @click="updateDiscount"
          >
            Update
          </button>

          <button
            class="rounded bg-slate-500 px-4 py-2 text-white"
            @click="() => {
              resetForm()
              showForm = false
            }"
          >
            Cancel
          </button>
        </div>
      </div>
    </div>

    <div class="space-y-4">
      <div
        v-for="discount in discounts"
        :key="discount.id"
        class="rounded-xl border p-4"
      >
        <div class="flex items-center justify-between">
          <div>
            <h2 class="font-bold">
              {{ discount.code }}
            </h2>

            <p>
              {{ discount.discount_type }}
            </p>

            <p>
              Value: {{ discount.value }}
            </p>

            <p>
              Used:
              {{ discount.used_count }}
              /
              {{ discount.usage_limit }}
            </p>
          </div>

          <div class="flex gap-2">
            <button
              class="rounded bg-blue-600 px-3 py-1 text-white"
              @click="editDiscount(discount)"
            >
              Edit
            </button>

            <button
              class="rounded bg-red-600 px-3 py-1 text-white"
              @click="deleteDiscount(discount.id)"
            >
              Delete
            </button>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
