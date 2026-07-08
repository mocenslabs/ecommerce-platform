import api from './api'

export const dashboardService = {
  getStats() {
    return api.get(
      '/dashboard/stats/'
    )
  },

  getRecentOrders() {
    return api.get(
      '/dashboard/recent-orders/'
    )
  },

  getTopProducts() {
    return api.get(
      '/dashboard/top-products/'
    )
  },

  getRevenueTrend() {
    return api.get(
      '/dashboard/revenue-trend/'
    )
  },

  getOrdersByStatus() {
    return api.get(
      '/dashboard/orders-by-status/'
    )
  },

  getLowStockProducts() {
    return api.get(
      '/dashboard/low-stock/'
    )
  },
}
