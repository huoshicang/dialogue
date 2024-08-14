import { createApp } from 'vue'
import './style.css'
import App from './App.vue'

import ArcoVue from '@arco-design/web-vue';
import ArcoVueIcon from '@arco-design/web-vue/es/icon';
import '@arco-design/web-vue/dist/arco.css';

import "./assets/arco-palette.less"

import 'highlight.js/styles/github-dark.css';

// 路由控制
import "./router/global_forward_guard"

import { router } from "./router"

import { createPinia } from 'pinia'

const pinia = createPinia()
const app = createApp(App);

app.use(ArcoVue);
app.use(ArcoVueIcon);
app.use(router);
app.use(pinia)
app.mount('#app');
