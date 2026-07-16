import type { App } from 'vue'

import { createPinia } from 'pinia'

import { router } from '@/router'

/**
 * Registers all application plugins.
 *
 * This file centralizes the application's bootstrap process,
 * keeping main.ts as clean as possible.
 */
export function registerPlugins(app: App): void {
  registerState(app)
  registerRouter(app)
}

/**
 * Registers the global state management.
 */
function registerState(app: App): void {
  app.use(createPinia())
}

/**
 * Registers the application router.
 */
function registerRouter(app: App): void {
  app.use(router)
}
