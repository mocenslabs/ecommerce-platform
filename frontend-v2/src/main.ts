import { createApp } from 'vue'

import '@/styles/index.css'

import App from './App.vue'

import { registerPlugins } from '@/app/registerPlugins'

const app = createApp(App)

registerPlugins(app)

app.mount('#app')
