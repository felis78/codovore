/**
 * main.ts
 *
 * Bootstraps Vuetify and other plugins then mounts the App`
 */

// Plugins
import { registerPlugins } from '@/plugins'

// Components
import App from './App.vue'

// Composables
import { createApp } from 'vue'
import { plugin, defaultConfig } from '@formkit/vue'
import config from '@/formkit.config'
import '@formkit/themes/genesis'
import router from './plugins/router'

createApp(App).use(plugin, defaultConfig(config)).use(registerPlugins).use(router).mount('#app')
