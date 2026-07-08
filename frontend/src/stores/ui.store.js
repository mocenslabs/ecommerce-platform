import { defineStore } from 'pinia'

export const useUiStore = defineStore('ui', {
  state: () => ({
    darkMode: false,

    mobileMenuOpen: false,

    adminSidebarOpen: false,
  }),

  actions: {
    toggleDarkMode() {
      this.darkMode = !this.darkMode
    },

    toggleMobileMenu() {
      this.mobileMenuOpen =
        !this.mobileMenuOpen
    },

    openMobileMenu() {
      this.mobileMenuOpen = true
    },

    closeMobileMenu() {
      this.mobileMenuOpen = false
    },

    toggleAdminSidebar() {
      this.adminSidebarOpen =
        !this.adminSidebarOpen
    },

    openAdminSidebar() {
      this.adminSidebarOpen = true
    },

    closeAdminSidebar() {
      this.adminSidebarOpen = false
    },
  },
})
