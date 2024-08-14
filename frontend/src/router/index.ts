import {createRouter, createWebHistory, RouteRecordRaw} from 'vue-router'
//import "./global_forward_guard"

import {
  ChatbubbleOutline as Chat,
} from '@vicons/ionicons5'
import ACCESS_ENUM from "./access-enum";

const routes: readonly RouteRecordRaw[] = [
  {
    path: '/',
    name: 'default-layout',
    components: {
      app_view: () => import("../layout/default-layout.vue"),
    },
    children: [
      {
        path: 'chat',
        name: 'chat',
        components: {
          layout_view: () => import("../components/chat/index.vue")
        },
        meta: {
          title: '聊天',
          label: true,
          icon: Chat,
        }
      },
    ]
  },
  {
    path: '/login',
    name: 'login',
    components: {
      app_view: () => import("../components/login/index.vue")
    },
    meta: {
      title: '登录',
      label: false,
      access: ACCESS_ENUM.NOT_LOGIN,
    },
  },
]

export const router = createRouter({
  history: createWebHistory(),
  routes,
})
