import { useAuthStore } from '@/stores/auth.store'

export async function authGuard(to) {
  const authStore = useAuthStore()

  await authStore.initialize()

  if (
    to.meta.requiresAuth &&
    !authStore.isAuthenticated
  ) {
    return '/login'
  }

  if (
    to.meta.requiresAdmin &&
    !authStore.isAdmin
  ) {
    return '/'
  }
}
