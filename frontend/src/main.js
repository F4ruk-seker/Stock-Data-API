import { createApp } from 'vue'
import App from './App.vue'
import './registerServiceWorker'
import router from './router'
import store from './store'
import './assets/style.css'
import axios from './plugins/axios'; // Plugin olarak axios'u dahil edin


createApp(App).provide('$axios', axios).use(store).use(router).mount('#app')
