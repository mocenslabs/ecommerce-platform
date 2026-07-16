/**
 * Storage abstraction.
 *
 * This interface allows different storage implementations
 * (Local Storage, Session Storage, IndexedDB, etc.).
 */
export interface StorageDriver {
  get(key: string): string | null

  set(key: string, value: string): void

  remove(key: string): void

  clear(): void
}
