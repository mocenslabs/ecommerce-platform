import { defineStore } from 'pinia'

import {
accountService,
} from '@/services/account.service'

export const useAccountStore =
defineStore('account', {
state: () => ({
orders: [],


  currentOrder: null,

  addresses: [],

  loading: false,
}),

actions: {
  // Orders

  async fetchOrders() {
    this.loading = true

    try {
      const { data } =
        await accountService.getOrders()

      this.orders =
        data.results ?? data
    } finally {
      this.loading = false
    }
  },

  async fetchOrder(
    orderNumber
  ) {
    const { data } =
      await accountService.getOrder(
        orderNumber
      )

    this.currentOrder =
      data
  },

  // Addresses

  async fetchAddresses() {
    const { data } =
      await accountService.getAddresses()

    this.addresses =
      data.results ?? data
  },

  async createAddress(
    payload
  ) {
    await accountService.createAddress(
      payload
    )

    await this.fetchAddresses()
  },

  async updateAddress(
    id,
    payload
  ) {
    await accountService.updateAddress(
      id,
      payload
    )

    await this.fetchAddresses()
  },

  async deleteAddress(id) {
    await accountService.deleteAddress(
      id
    )

    await this.fetchAddresses()
  },
},


})
