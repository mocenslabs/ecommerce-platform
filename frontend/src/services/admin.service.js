import api from './api'

export const adminService = {
  // Products

  getProducts() {
    return api.get(
      '/catalog/admin/products/'
    )
  },

  getProduct(id) {
    return api.get(
      `/catalog/admin/products/${id}/`
    )
  },

  createProduct(payload) {
    return api.post(
      '/catalog/admin/products/',
      payload
    )
  },

  updateProduct(
    id,
    payload
  ) {
    return api.patch(
      `/catalog/admin/products/${id}/`,
      payload
    )
  },

  deleteProduct(id) {
    return api.delete(
      `/catalog/admin/products/${id}/`
    )
  },

  // Categories

  getCategories() {
    return api.get(
      '/catalog/admin/categories/'
    )
  },

  // Brands

  getBrands() {
    return api.get(
      '/catalog/admin/brands/'
    )
  },

  // Product Images

  getProductImages() {
    return api.get(
      '/catalog/admin/product-images/'
    )
  },

  createProductImage(
    payload
  ) {
    return api.post(
      '/catalog/admin/product-images/',
      payload,
      {
        headers: {
          'Content-Type':
            'multipart/form-data',
        },
      }
    )
  },

  deleteProductImage(id) {
    return api.delete(
      `/catalog/admin/product-images/${id}/`
    )
  },

  // Inventory

  getInventory() {
    return api.get(
      '/inventory/admin/'
    )
  },

  updateInventory(
    id,
    payload
  ) {
    return api.patch(
      `/inventory/admin/${id}/`,
      payload
    )
  },

  // Orders

  getOrders() {
    return api.get(
      '/orders/admin/'
    )
  },

  getOrder(id) {
    return api.get(
      `/orders/admin/${id}/`
    )
  },

  updateOrder(
    id,
    payload
  ) {
    return api.patch(
      `/orders/admin/${id}/`,
      payload
    )
  },

  // Customers

  getCustomers() {
    return api.get(
      '/users/admin/customers/'
    )
  },

  // Shipping Methods

  getShippingMethods() {
    return api.get(
      '/orders/admin/shipping-methods/'
    )
  },

  createShippingMethod(
    payload
  ) {
    return api.post(
      '/orders/admin/shipping-methods/',
      payload
    )
  },

  updateShippingMethod(
    id,
    payload
  ) {
    return api.patch(
      `/orders/admin/shipping-methods/${id}/`,
      payload
    )
  },

  deleteShippingMethod(id) {
    return api.delete(
      `/orders/admin/shipping-methods/${id}/`
    )
  },

  // Payments

  getPayments() {
    return api.get(
      '/payments/admin/'
    )
  },

  // Discounts

  getDiscounts() {
    return api.get(
      '/discounts/admin/'
    )
  },

  getDiscount(id) {
    return api.get(
      `/discounts/admin/${id}/`
    )
  },

  createDiscount(payload) {
    return api.post(
      '/discounts/admin/',
      payload
    )
  },

  updateDiscount(
    id,
    payload
  ) {
    return api.patch(
      `/discounts/admin/${id}/`,
      payload
    )
  },

  deleteDiscount(id) {
    return api.delete(
      `/discounts/admin/${id}/`
    )
  },

  // Reviews

  getReviews() {
    return api.get(
      '/reviews/admin/'
    )
  },

  getReview(id) {
    return api.get(
      `/reviews/admin/${id}/`
    )
  },

  updateReview(
    id,
    payload
  ) {
    return api.patch(
      `/reviews/admin/${id}/`,
      payload
    )
  },

  deleteReview(id) {
    return api.delete(
      `/reviews/admin/${id}/`
    )
  },
}
