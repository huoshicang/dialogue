import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
// main.js
import process from "process";

// 或者，如果您需要全局可用的 `process` 变量
global.process = process;

import ArcoVue from "@arco-design/web-vue";
import ArcoVueIcon from "@arco-design/web-vue/es/icon";
import "@arco-design/web-vue/dist/arco.css";

import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import { createPinia } from "pinia";

import "@/router/global_forward_guard";

const pinia = createPinia();
pinia.use(piniaPluginPersistedstate)
const app = createApp(App);

app.use(router);
app.use(ArcoVue);
app.use(ArcoVueIcon);
app.use(pinia);
app.mount("#app");
