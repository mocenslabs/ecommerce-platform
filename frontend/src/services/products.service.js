import api from './api'

export const productsService = {
  getProducts(params = {}) {
    return api.get('/catalog/products/', {
      params,
    })
  },

  getFeaturedProducts() {
    return api.get(
      '/catalog/products/featured/'
    )
  },

  getProduct(slug) {
    return api.get(
      `/catalog/products/${slug}/`
    )
  },
}
