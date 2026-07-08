import { defineStore } from 'pinia'

import {
  orderService,
} from '@/services/order.service'

export const useOrderStore =
  defineStore('orders', {
    state: () => ({
      addresses: [],
      shippingMethods: [],

      orders: [],
      currentOrder: null,

      loading: false,

      checkoutLoading: false,

      lastOrder: null,
    }),

    actions: {
      async fetchAddresses() {
        const { data } =
          await orderService.getAddresses()

        this.addresses =
          data.results ?? data
      },

      async fetchShippingMethods() {
        const { data } =
          await orderService.getShippingMethods()

        this.shippingMethods =
          data.results ?? data
      },

      async fetchOrders() {
        this.loading = true

        try {
          const { data } =
            await orderService.getOrders()

          this.orders =
            data.results ?? data
        } finally {
          this.loading = false
        }
      },

      async fetchOrder(
        orderNumber,
      ) {
        this.loading = true

        try {
          const { data } =
            await orderService.getOrder(
              orderNumber,
            )

          this.currentOrder =
            data
        } finally {
          this.loading = false
        }
      },

      async checkout(payload) {
        this.checkoutLoading =
          true

        try {
          const { data } =
            await orderService.checkout(
              payload,
            )

          this.lastOrder =
            data

          return data
        } finally {
          this.checkoutLoading =
            false
        }
      },
    },
  })
