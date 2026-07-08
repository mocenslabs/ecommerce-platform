import { defineStore } from 'pinia'
import { productsService } from '@/services/products.service'

export const useProductsStore =
  defineStore('products', {
    state: () => ({
      products: [],
      featuredProducts: [],
      currentProduct: null,

      loading: false,

      filters: {
        search: '',
        ordering: '',
      },
    }),

    actions: {
      async fetchProducts() {
        this.loading = true

        try {
          const { data } =
            await productsService.getProducts(
              this.filters,
            )

          this.products =
            data.results ?? data
        } finally {
          this.loading = false
        }
      },

      async fetchFeaturedProducts() {
        const { data } =
          await productsService.getFeaturedProducts()

        this.featuredProducts =
          data.results ?? data
      },

      async updateSearch(
        value,
      ) {
        this.filters.search =
          value

        await this.fetchProducts()
      },

      async updateOrdering(
        value,
      ) {
        this.filters.ordering =
          value

        await this.fetchProducts()
      },

      async fetchProduct(
        slug,
      ) {
        this.loading = true

        try {
        const { data } =
           await productsService.getProduct(
        slug,
      )

    this.currentProduct =
      data
  } finally {
    this.loading = false
  }
},
    },
  })
