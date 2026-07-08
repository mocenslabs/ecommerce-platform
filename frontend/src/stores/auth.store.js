import { defineStore } from 'pinia'
import { authService } from '@/services/auth.service'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    user: null,
    isAuthenticated: false,
    loading: false,
    initialized: false,
  }),

  getters: {
    isAdmin: (state) =>
      state.user?.role === 'admin',
  },

  actions: {
    async initialize() {
      if (this.initialized) {
        return
      }

      const token =
        localStorage.getItem(
          'access_token'
        )

      if (!token) {
        this.initialized = true
        return
      }

      try {
        await this.fetchCurrentUser()
      } catch {
        localStorage.removeItem(
          'access_token'
        )

        localStorage.removeItem(
          'refresh_token'
        )

        this.user = null
        this.isAuthenticated = false
      } finally {
        this.initialized = true
      }
    },

    async login(credentials) {
      this.loading = true

      try {
        const { data } =
          await authService.login(
            credentials
          )

        localStorage.setItem(
          'access_token',
          data.tokens.access
        )

        localStorage.setItem(
          'refresh_token',
          data.tokens.refresh
        )

        this.user = data.user
        this.isAuthenticated = true

        return true
      } finally {
        this.loading = false
      }
    },

    async fetchCurrentUser() {
      const { data } =
        await authService.me()

      this.user = data
      this.isAuthenticated = true
    },

    async logout() {
      try {
        await authService.logout()
      } catch {
        // ignore
      } finally {
        localStorage.removeItem(
          'access_token'
        )

        localStorage.removeItem(
          'refresh_token'
        )

        this.user = null
        this.isAuthenticated = false
      }
    },
  },
})
