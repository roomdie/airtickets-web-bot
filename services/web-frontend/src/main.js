import { createApp } from 'vue'
import App from './App'
import router from "@/router";
import store from "./store"
// Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
// import * as labsComponents from 'vuetify/labs/components'
import * as directives from 'vuetify/directives'
import '@mdi/font/css/materialdesignicons.css'
// import { VDatePicker } from 'vuetify/labs/VDatePicker'
// import {Sortable, Swap} from "sortablejs/modular/sortable.core.esm";
// Sortable.mount(new Swap());

const vuetify = createVuetify({
    icons: {
    defaultSet: 'mdi', // This is already the default value - only for display purposes
  },
  components,
  directives,
})


createApp(App)
    .use(router)
    .use(vuetify)
    .use(store)
    .mount('#app');