/**
 * Generic HTTP client contract.
 *
 * This abstraction allows replacing the underlying HTTP library
 * without affecting the rest of the application.
 */
export interface HttpClient {
  get<T>(url: string, config?: unknown): Promise<T>

  post<T>(url: string, data?: unknown, config?: unknown): Promise<T>

  put<T>(url: string, data?: unknown, config?: unknown): Promise<T>

  patch<T>(url: string, data?: unknown, config?: unknown): Promise<T>

  delete<T>(url: string, config?: unknown): Promise<T>
}
