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
          remarks:
            "这是默认的首页,不写path是为了让url保持干净,所以用name进行导航",
        },
      },
      {
        path: "chat/:id?",
        name: "chat",
        props: true,
        components: {
          default_layout_view: () => import("../components/chat/ChatIndex.vue"),
        },
        // children: [
        //   {
        //     path: ":id",
        //     name: "chat_id",
        //     props: true,
        //     components: {
        //       chat_content_view: () =>
        //         import("../components/chat/content/ChatContent.vue"),
        //     },
        //   },
        //   {
        //     path: "",
        //     name: "empty",
        //     props: true,
        //     components: {
        //       chat_content_view: () =>
        //         import("../components/chat/content/ContentEmpty.vue"),
        //     },
        //   },
        // ],
        meta: {
          title: "聊天",
          label: true,
          access: ACCESS_ENUM.USER,
          keepAlive: true,
          remarks: "这是聊天页面",
        },
      },
      {
        path: "backstage",
        name: "backstage",
        redirect: "/backstage/model",
        components: {
          default_layout_view: () =>
            import("../components/backstage/BackstageIndex.vue"),
        },
        meta: {
          title: "管理",
          label: false,
          access: ACCESS_ENUM.ADMIN,
          remarks: "这是管理页面",
        },
        children: [
          {
            path: "model",
            name: "model",
            components: {
              backstage_content_view: () =>
                import("../components/backstage/pages/model/ModelIndex.vue"),
            },
            meta: {
              title: "模型",
              label: true,
              access: ACCESS_ENUM.ADMIN,
              keepAlive: true,
              remarks: "这是模型页面",
            },
          },
          {
            path: "key",
            name: "key",
            components: {
              backstage_content_view: () =>
                import("../components/backstage/pages/keys/KeysIndex.vue"),
            },
            meta: {
              title: "密钥",
              label: true,
              access: ACCESS_ENUM.ADMIN,
              keepAlive: true,
              remarks: "这是密钥页面",
            },
          },
        ],
      },
      {
        path: "noAuth",
        name: "无权限",
        components: {
          default_layout_view: () =>
            import("../components/noAuth/noAuthIndex.vue"),
        },
        meta: {
          title: "权限",
          label: false,
          access: ACCESS_ENUM.NOT_LOGIN,
          remarks: "无权限",
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
