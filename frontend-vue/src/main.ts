import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";

import ArcoVue from "@arco-design/web-vue";
import ArcoVueIcon from "@arco-design/web-vue/es/icon";
import "@arco-design/web-vue/dist/arco.css";
import NaiveUI from "naive-ui"

import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import { createPinia } from "pinia";

import { setupAssets, setupScrollbarStyle } from './plugins'
import "@/router/global_forward_guard";

const app = createApp(App);
const pinia = createPinia();

setupAssets()
setupScrollbarStyle()
pinia.use(piniaPluginPersistedstate)


app.use(router);
app.use(ArcoVue);
app.use(ArcoVueIcon);
app.use(NaiveUI);
app.use(pinia);
app.mount("#app");
