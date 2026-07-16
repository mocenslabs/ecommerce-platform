import { env } from './env'

export const appConfig = {
  name: env.appName,

  version: env.appVersion,

  apiUrl: env.apiUrl,
} as const
