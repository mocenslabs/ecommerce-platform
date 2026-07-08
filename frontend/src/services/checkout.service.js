import api from './api'

export const checkoutService = {
  createOrder(payload) {
    return api.post('/checkout/', payload)
  },
}
