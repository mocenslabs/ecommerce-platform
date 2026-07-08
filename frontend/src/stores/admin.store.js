import { defineStore } from 'pinia'

import {
  adminService,
} from '@/services/admin.service'

export const useAdminStore =
  defineStore('admin', {
    state: () => ({
      products: [],
      categories: [],
      brands: [],

      productImages: [],

      inventory: [],

      orders: [],
      currentOrder: null,

      customers: [],

      shippingMethods: [],

      payments: [],

      discounts: [],
      currentDiscount: null,

      reviews: [],
      currentReview: null,

      loading: false,
    }),

    actions: {
      // Products

      async fetchProducts() {
        this.loading = true

        try {
          const { data } =
            await adminService.getProducts()

          this.products =
            data.results ?? data
        } finally {
          this.loading = false
        }
      },

      async createProduct(
        payload
      ) {
        await adminService.createProduct(
          payload
        )

        await this.fetchProducts()
      },

      async updateProduct(
        id,
        payload
      ) {
        await adminService.updateProduct(
          id,
          payload
        )

        await this.fetchProducts()
      },

      async deleteProduct(id) {
        await adminService.deleteProduct(
          id
        )

        await this.fetchProducts()
      },

      // Categories

      async fetchCategories() {
        const { data } =
          await adminService.getCategories()

        this.categories =
          data.results ?? data
      },

      // Brands

      async fetchBrands() {
        const { data } =
          await adminService.getBrands()

        this.brands =
          data.results ?? data
      },

      // Product Images

      async fetchProductImages() {
        const { data } =
          await adminService.getProductImages()

        this.productImages =
          data.results ?? data
      },

      async createProductImage(
        payload
      ) {
        await adminService.createProductImage(
          payload
        )

        await this.fetchProductImages()
      },

      async deleteProductImage(id) {
        await adminService.deleteProductImage(
          id
        )

        await this.fetchProductImages()
      },

      // Inventory

      async fetchInventory() {
        const { data } =
          await adminService.getInventory()

        this.inventory =
          data.results ?? data
      },

      async updateInventory(
        id,
        payload
      ) {
        await adminService.updateInventory(
          id,
          payload
        )

        await this.fetchInventory()
      },

      // Orders

      async fetchOrders() {
        const { data } =
          await adminService.getOrders()

        this.orders =
          data.results ?? data
      },

      async fetchOrder(id) {
        const { data } =
          await adminService.getOrder(
            id
          )

        this.currentOrder =
          data
      },

      async updateOrder(
        id,
        payload
      ) {
        await adminService.updateOrder(
          id,
          payload
        )

        await this.fetchOrder(id)

        await this.fetchOrders()
      },

      // Customers

      async fetchCustomers() {
        const { data } =
          await adminService.getCustomers()

        this.customers =
          data.results ?? data
      },

      // Shipping Methods

      async fetchShippingMethods() {
        const { data } =
          await adminService.getShippingMethods()

        this.shippingMethods =
          data.results ?? data
      },

      async createShippingMethod(
        payload
      ) {
        await adminService.createShippingMethod(
          payload
        )

        await this.fetchShippingMethods()
      },

      async updateShippingMethod(
        id,
        payload
      ) {
        await adminService.updateShippingMethod(
          id,
          payload
        )

        await this.fetchShippingMethods()
      },

      async deleteShippingMethod(id) {
        await adminService.deleteShippingMethod(
          id
        )

        await this.fetchShippingMethods()
      },

      // Payments

      async fetchPayments() {
        const { data } =
          await adminService.getPayments()

        this.payments =
          data.results ?? data
      },

      // Discounts

      async fetchDiscounts() {
        const { data } =
          await adminService.getDiscounts()

        this.discounts =
          data.results ?? data
      },

      async fetchDiscount(id) {
        const { data } =
          await adminService.getDiscount(
            id
          )

        this.currentDiscount =
          data
      },

      async createDiscount(
        payload
      ) {
        await adminService.createDiscount(
          payload
        )

        await this.fetchDiscounts()
      },

      async updateDiscount(
        id,
        payload
      ) {
        await adminService.updateDiscount(
          id,
          payload
        )

        await this.fetchDiscounts()
      },

      async deleteDiscount(id) {
        await adminService.deleteDiscount(
          id
        )

        await this.fetchDiscounts()
      },

      // Reviews

      async fetchReviews() {
        const { data } =
          await adminService.getReviews()

        this.reviews =
          data.results ?? data
      },

      async fetchReview(id) {
        const { data } =
          await adminService.getReview(
            id
          )

        this.currentReview =
          data
      },

      async updateReview(
        id,
        payload
      ) {
        await adminService.updateReview(
          id,
          payload
        )

        await this.fetchReviews()
      },

      async deleteReview(id) {
        await adminService.deleteReview(
          id
        )

        await this.fetchReviews()
      },
    },
  })
