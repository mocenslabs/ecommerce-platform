import api from './api'

export const customerDashboardService = {
  getDashboard() {
    return api.get(
      '/users/dashboard/'
    )
  },
}
