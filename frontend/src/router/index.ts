import ACCESS_ENUM from "@/router/access-enum";
import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: "default-layout",
    components: {
      app_view: () => import("../layout/default-layout.vue"),
    },
    children: [
      {
        path: "chat",
        name: "chat",
        components: {
          layout_view: () => import("../components/chat/ChatIndex.vue"),
        },
        meta: {
          title: "聊天",
          label: true,
        },
      },
    ],
  },
  {
    path: "/login/:log",
    name: "login",
    components: {
      app_view: () => import("../components/login/LoginIndex.vue"),
    },
    meta: {
      title: "登录",
      label: false,
      access: ACCESS_ENUM.NOT_LOGIN,
    },
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
