import { defineStore } from 'pinia'

import {
  wishlistService,
} from '@/services/wishlist.service'

export const useWishlistStore =
  defineStore('wishlist', {
    state: () => ({
      items: [],
      loading: false,
    }),

    getters: {
      count: (state) =>
        state.items.length,
    },

    actions: {
      async fetchWishlist() {
        this.loading = true

        try {
          const { data } =
            await wishlistService.getWishlist()

          this.items = data
        } finally {
          this.loading = false
        }
      },

      async addProduct(
        productId,
      ) {
        await wishlistService.addProduct(
          productId,
        )

        await this.fetchWishlist()
      },

      async removeProduct(
        productId,
      ) {
        await wishlistService.removeProduct(
          productId,
        )

        await this.fetchWishlist()
      },
    },
  })
