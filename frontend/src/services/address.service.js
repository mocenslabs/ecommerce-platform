import api from './api'

export const addressService = {
  getAddresses() {
    return api.get(
      '/orders/addresses/'
    )
  },

  createAddress(payload) {
    return api.post(
      '/orders/addresses/',
      payload,
    )
  },

  updateAddress(
    id,
    payload,
  ) {
    return api.put(
      `/orders/addresses/${id}/`,
      payload,
    )
  },

  deleteAddress(id) {
    return api.delete(
      `/orders/addresses/${id}/`
    )
  },
}
