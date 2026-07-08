import { defineStore } from 'pinia'

import {
  customerDashboardService,
} from '@/services/customer-dashboard.service'

export const useCustomerDashboardStore =
  defineStore(
    'customerDashboard',
    {
      state: () => ({
        dashboard: null,

        loading: false,
      }),

      actions: {
        async fetchDashboard() {
          this.loading = true

          try {
            const { data } =
              await customerDashboardService.getDashboard()

            this.dashboard =
              data
          } finally {
            this.loading = false
          }
        },
      },
    }
  )
