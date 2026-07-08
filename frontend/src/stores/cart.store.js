import { defineStore } from 'pinia'

import {
  cartService,
} from '@/services/cart.service'

export const useCartStore =
  defineStore('cart', {
    state: () => ({
      items: [],
      subtotal: 0,
      loading: false,
    }),

    getters: {
      itemCount: (state) =>
        state.items.reduce(
          (
            total,
            item,
          ) =>
            total +
            item.quantity,
          0,
        ),
    },

    actions: {
      async fetchCart() {
        this.loading = true

        try {
          const { data } =
            await cartService.getCart()

          this.items =
            data.items ?? []

          this.subtotal =
            data.subtotal ?? 0
        } finally {
          this.loading = false
        }
      },

      async addItem(
        variantId,
        quantity = 1,
      ) {
        await cartService.addItem({
          variant_id:
            variantId,
          quantity,
        })

        await this.fetchCart()
      },

      async removeItem(
        itemId,
      ) {
        await cartService.removeItem(
          itemId,
        )

        await this.fetchCart()
      },
    },
  })
