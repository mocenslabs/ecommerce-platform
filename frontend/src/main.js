import { createApp } from 'vue'
import App from './App.vue'

import router from './app/router'
import { createPinia } from 'pinia'

import './styles/main.css'


const app = createApp(App)

const pinia = createPinia()

app.use(pinia)
app.use(router)

//const authStore = useAuthStore(pinia)

//await authStore.initialize()

app.mount('#app')
