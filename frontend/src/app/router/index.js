import { createRouter, createWebHistory } from 'vue-router'

import { publicRoutes } from './public.routes'
import { adminRoutes } from './admin.routes'

import { authGuard } from './guards'

const router = createRouter({
  history: createWebHistory(),
  routes: [
    ...publicRoutes,
    ...adminRoutes,
  ],
})

router.beforeEach(authGuard)

export default router
