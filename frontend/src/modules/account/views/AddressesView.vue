<script setup>
import {
  onMounted,
} from 'vue'

import {
  storeToRefs,
} from 'pinia'

import AddressForm from
  '@/modules/account/components/AddressForm.vue'

import {
  useAccountStore,
} from '@/stores/account.store'

const accountStore =
  useAccountStore()

const {
  addresses,
  loading,
} = storeToRefs(
  accountStore,
)

onMounted(() => {
  accountStore.fetchAddresses()
})

async function createAddress(
  payload,
) {
  await accountStore.createAddress(
    payload,
  )
}

async function deleteAddress(
  id,
) {
  const confirmed =
    confirm(
      'Delete address?',
    )

  if (!confirmed) {
    return
  }

  await accountStore.deleteAddress(
    id,
  )
}
</script>

<template>
  <section
    class="mx-auto max-w-6xl px-4 py-12"
  >
    <h1
      class="mb-8 text-4xl font-bold"
    >
      My Addresses
    </h1>


<div
  class="mb-10 rounded-xl border p-6"
>
  <h2
    class="mb-4 text-xl font-bold"
  >
    Add Address
  </h2>

  <AddressForm
    @submit="
      createAddress
    "
  />
</div>

<div
  v-if="loading"
  class="text-center"
>
  Loading...
</div>

<div
  v-else-if="addresses.length"
  class="space-y-4"
>
  <div
    v-for="address in addresses"
    :key="address.id"
    class="rounded-xl border p-6"
  >
    <div
      class="space-y-2"
    >
      <p
        class="font-semibold"
      >
        {{ address.first_name }}
        {{ address.last_name }}
      </p>

      <p>
        {{ address.line_1 }}
      </p>

      <p
        v-if="address.line_2"
      >
        {{ address.line_2 }}
      </p>

      <p>
        {{ address.city }},
        {{ address.state }}
      </p>

      <p>
        {{ address.postal_code }}
      </p>

      <p>
        {{ address.country }}
      </p>

      <p>
        {{ address.phone_number }}
      </p>
    </div>

    <div
      class="mt-4"
    >
      <button
        class="rounded-lg bg-red-500 px-4 py-2 text-white"
        @click="
          deleteAddress(
            address.id,
          )
        "
      >
        Delete
      </button>
    </div>
  </div>
</div>

<div
  v-else
  class="rounded-xl border p-8 text-center"
>
  No addresses found.
</div>

  </section>
</template>
