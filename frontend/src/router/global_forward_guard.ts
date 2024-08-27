import { useUserStore, useSettingsStore } from "@/store";
import ACCESS_ENUM from "./access-enum";
import checkAccess from "./check-access";
import router from "@/router/index";

// 在每次路由切换之前执行的函数

router.beforeEach(async (to, from, next): Promise<void> => {
  /*
   *
   * 根据用户信息判断是否需要获取用户信息
   *
   * 1. 如果用户信息不存在，则获取用户信息
   *
   *
   * 2. 如果用户信息存在，则放行
   *
   * 3. 判断权限
   *
   * */

  let UserStore = useUserStore();

  const Settings = useSettingsStore().login_id;

  // 如果loginUser不存在或者loginUser的userRole不存在
  if (UserStore.user_info.username === "未登录") {
    await UserStore.fetchUserProfile();

    UserStore.user_info = useUserStore().user_info;
  }

  const needAccess = to.meta?.access ?? ACCESS_ENUM.LOGIN;

  if (needAccess !== ACCESS_ENUM.NOT_LOGIN) {
    //  // 如果没登录 就跳转到登录
    if (
      UserStore.user_info.username === "未登录" ||
      !UserStore.user_info.role
    ) {
      next(`/login/${Settings}`);
      console.log("未登录");
      return;
    }
  }

  // 如果登录用户没有权限访问需要的资源
  if (!checkAccess(UserStore.user_info, needAccess as string)) {
    next("/noAuth");
    return;
  }

  // 进行正常的路由跳转
  next();
});
