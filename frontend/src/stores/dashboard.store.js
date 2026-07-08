import { defineStore } from 'pinia'

import {
  dashboardService,
} from '@/services/dashboard.service'

export const useDashboardStore =
  defineStore('dashboard', {
    state: () => ({
      stats: null,

      recentOrders: [],

      topProducts: [],

      revenueTrend: [],

      ordersByStatus: [],

      lowStockProducts: [],

      loading: false,
    }),

    actions: {
      async fetchDashboard() {
        this.loading = true

        try {
          const [
            statsResponse,
            ordersResponse,
            productsResponse,
            revenueResponse,
            statusResponse,
            lowStockResponse,
          ] = await Promise.all([
            dashboardService.getStats(),
            dashboardService.getRecentOrders(),
            dashboardService.getTopProducts(),
            dashboardService.getRevenueTrend(),
            dashboardService.getOrdersByStatus(),
            dashboardService.getLowStockProducts(),
          ])

          this.stats =
            statsResponse.data

          this.recentOrders =
            ordersResponse.data

          this.topProducts =
            productsResponse.data

          this.revenueTrend =
            revenueResponse.data

          this.ordersByStatus =
            statusResponse.data

          this.lowStockProducts =
            lowStockResponse.data
        } finally {
          this.loading = false
        }
      },
    },
  })
