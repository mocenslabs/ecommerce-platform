/**
 * Environment configuration.
 *
 * This file is the single source of truth for all environment variables.
 */

export const env = {
  apiUrl: import.meta.env.VITE_API_URL,

  appName: import.meta.env.VITE_APP_NAME,

  appVersion: import.meta.env.VITE_APP_VERSION,

  appEnvironment: import.meta.env.MODE,
} as const
