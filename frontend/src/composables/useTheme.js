import { computed } from 'vue'
import { useUiStore } from '@/stores/ui.store'

export function useTheme() {
  const uiStore = useUiStore()

  const isDark = computed(
    () => uiStore.darkMode
  )

  const toggleTheme = () => {
    uiStore.toggleDarkMode()

    document.documentElement.classList.toggle(
      'dark',
      uiStore.darkMode
    )

    localStorage.setItem(
      'theme',
      uiStore.darkMode ? 'dark' : 'light'
    )
  }

  const initializeTheme = () => {
    const stored =
      localStorage.getItem('theme')

    if (stored === 'dark') {
      uiStore.darkMode = true

      document.documentElement.classList.add(
        'dark'
      )
    }
  }

  return {
    isDark,
    toggleTheme,
    initializeTheme,
  }
}
