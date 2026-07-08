import api from './api'

export const orderService = {
  getAddresses() {
    return api.get('/orders/addresses/')
  },

  getShippingMethods() {
    return api.get(
      '/orders/shipping-methods/'
    )
  },

  checkout(payload) {
    return api.post(
      '/orders/checkout/',
      payload,
    )
  },

  getOrders() {
    return api.get('/orders/')
  },

  getOrder(orderNumber) {
    return api.get(
      `/orders/${orderNumber}/`
    )
  },
}
