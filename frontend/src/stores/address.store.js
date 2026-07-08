import { defineStore } from 'pinia'

import {
  addressService,
} from '@/services/address.service'

export const useAddressStore =
  defineStore('addresses', {
    state: () => ({
      addresses: [],
      loading: false,
    }),

    actions: {
      async fetchAddresses() {
        this.loading = true

        try {
          const { data } =
            await addressService.getAddresses()

          this.addresses =
            data.results ?? data
        } finally {
          this.loading = false
        }
      },

      async createAddress(
        payload,
      ) {
        await addressService.createAddress(
          payload,
        )

        await this.fetchAddresses()
      },

      async updateAddress(
        id,
        payload,
      ) {
        await addressService.updateAddress(
          id,
          payload,
        )

        await this.fetchAddresses()
      },

      async deleteAddress(id) {
        await addressService.deleteAddress(
          id,
        )

        await this.fetchAddresses()
      },
    },
  })
