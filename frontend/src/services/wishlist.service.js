import api from './api'

export const wishlistService = {
  getWishlist() {
    return api.get('/wishlist/')
  },

  addProduct(productId) {
    return api.post('/wishlist/', {
      product_id: productId,
    })
  },

  removeProduct(productId) {
    return api.delete('/wishlist/', {
      data: {
        product_id: productId,
      },
    })
  },
}
