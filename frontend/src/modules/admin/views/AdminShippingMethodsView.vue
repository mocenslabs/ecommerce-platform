<script setup>
import {
  ref,
  onMounted,
} from 'vue'

import {
  useAdminStore,
} from '@/stores/admin.store'

const adminStore =
  useAdminStore()

const showForm =
  ref(false)

const editingId =
  ref(null)

const form = ref({
  name: '',
  code: '',
  price: 0,
  estimated_days: 1,
  active: true,
})

onMounted(async () => {
  await adminStore.fetchShippingMethods()
})

const resetForm = () => {
  editingId.value = null

  form.value = {
    name: '',
    code: '',
    price: 0,
    estimated_days: 1,
    active: true,
  }
}

const createShippingMethod =
  async () => {
    await adminStore.createShippingMethod(
      form.value
    )

    resetForm()

    showForm.value = false
  }

const editShippingMethod =
  (method) => {
    editingId.value =
      method.id

    form.value = {
      name: method.name,
      code: method.code,
      price: method.price,
      estimated_days:
        method.estimated_days,
      active: method.active,
    }

    showForm.value = true
  }

const updateShippingMethod =
  async () => {
    await adminStore.updateShippingMethod(
      editingId.value,
      form.value
    )

    resetForm()

    showForm.value = false
  }

const deleteShippingMethod =
  async (id) => {
    if (
      !confirm(
        'Delete shipping method?'
      )
    ) {
      return
    }

    await adminStore.deleteShippingMethod(
      id
    )
  }
</script>

<template>
  <section
    class="mx-auto max-w-7xl p-6"
  >
    <div
      class="mb-6 flex items-center justify-between"
    >
      <h1
        class="text-3xl font-bold"
      >
        Shipping Methods
      </h1>

      <button
        class="rounded-lg bg-black px-4 py-2 text-white"
        @click="showForm = true"
      >
        New Method
      </button>
    </div>

    <div
      v-if="showForm"
      class="mb-8 rounded-xl border p-6"
    >
      <div
        class="grid gap-4"
      >
        <input
          v-model="form.name"
          placeholder="Name"
          class="rounded border p-2"
        >

        <input
          v-model="form.code"
          placeholder="Code"
          class="rounded border p-2"
        >

        <input
          v-model="form.price"
          type="number"
          class="rounded border p-2"
        >

        <input
          v-model="form.estimated_days"
          type="number"
          class="rounded border p-2"
        >

        <label>
          <input
            v-model="form.active"
            type="checkbox"
          >

          Active
        </label>

        <div
          class="flex gap-3"
        >
          <button
            v-if="!editingId"
            class="rounded bg-green-600 px-4 py-2 text-white"
            @click="
              createShippingMethod
            "
          >
            Create
          </button>

          <button
            v-else
            class="rounded bg-blue-600 px-4 py-2 text-white"
            @click="
              updateShippingMethod
            "
          >
            Update
          </button>

          <button
            class="rounded bg-slate-500 px-4 py-2 text-white"
            @click="
              showForm = false
            "
          >
            Cancel
          </button>
        </div>
      </div>
    </div>

    <div
      class="space-y-4"
    >
      <div
        v-for="method in adminStore.shippingMethods"
        :key="method.id"
        class="rounded-xl border p-4"
      >
        <div
          class="flex items-center justify-between"
        >
          <div>
            <h2
              class="font-bold"
            >
              {{ method.name }}
            </h2>

            <p>
              {{ method.code }}
            </p>

            <p>
              ${{ method.price }}
            </p>

            <p>
              {{ method.estimated_days }}
              days
            </p>
          </div>

          <div
            class="flex gap-2"
          >
            <button
              class="rounded bg-blue-600 px-3 py-1 text-white"
              @click="
                editShippingMethod(
                  method
                )
              "
            >
              Edit
            </button>

            <button
              class="rounded bg-red-600 px-3 py-1 text-white"
              @click="
                deleteShippingMethod(
                  method.id
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
