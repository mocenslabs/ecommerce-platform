/**
 * Application logger.
 *
 * Console output is centralized here to make it replaceable
 * in production environments.
 */
export const logger = {
  info: (...args: unknown[]) => {
    console.info(...args)
  },

  warn: (...args: unknown[]) => {
    console.warn(...args)
  },

  error: (...args: unknown[]) => {
    console.error(...args)
  },
}
