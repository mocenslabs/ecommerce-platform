import api from './api'

export const cartService = {
  getCart() {
    return api.get('/cart/')
  },

  addItem(payload) {
    return api.post(
      '/cart/items/',
      payload
    )
  },

  updateItem(id, payload) {
    return api.put(
      `/cart/items/${id}/update/`,
      payload
    )
  },

  removeItem(id) {
    return api.delete(
      `/cart/items/${id}/delete/`
    )
  },
}
