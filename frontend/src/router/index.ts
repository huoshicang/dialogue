import ACCESS_ENUM from "@/router/access-enum";
import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    components: {
      app_view: () => import("../layout/default-layout.vue"),
    },
    // redirect:'AppIndex',
    children: [
      {
        path: "",
        name: "AppIndex",
        components: {
          default_layout_view: () => import("../components/app/AppIndex.vue"),
        },
        meta: {
          title: "AppIndex",
          label: true,
          access: ACCESS_ENUM.NOT_LOGIN,
          keepAlive: true,
          remarks: "这是默认的首页,不写path是为了让url保持干净,所以用name进行导航",
        },
      },
      {
        path: "chat",
        name: "chat",
        components: {
          default_layout_view: () => import("../components/chat/ChatIndex.vue"),
        },
        meta: {
          title: "聊天",
          label: true,
          access: ACCESS_ENUM.USER,
          keepAlive: true,
          remarks: "这是聊天页面",
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
