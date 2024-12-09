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
import NaiveUI from "naive-ui"

// @ts-ignore
import VMdPreview from '@kangc/v-md-editor/lib/preview';
import '@kangc/v-md-editor/lib/style/preview.css';
// @ts-ignore
import githubTheme from '@kangc/v-md-editor/lib/theme/github.js';
import '@kangc/v-md-editor/lib/theme/style/github.css';


// highlightjs
import hljs from 'highlight.js';

VMdPreview.use(githubTheme, {
  Hljs: hljs,
});


import piniaPluginPersistedstate from 'pinia-plugin-persistedstate'
import { createPinia } from "pinia";


import "@/router/global_forward_guard";

const pinia = createPinia();
pinia.use(piniaPluginPersistedstate)
const app = createApp(App);

app.use(VMdPreview);
app.use(router);
app.use(ArcoVue);
app.use(ArcoVueIcon);
app.use(NaiveUI);
app.use(pinia);
app.mount("#app");
