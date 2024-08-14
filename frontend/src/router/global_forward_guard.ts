import {router} from "./index";
import {useUserStore} from "../store/index";
import ACCESS_ENUM from "./access-enum";
import checkAccess from "./check-access";

// 在每次路由切换之前执行的函数

router.beforeEach(async (to, from, next) => {
  let loginUser = useUserStore().user_info;

  // 如果loginUser不存在或者loginUser的userRole不存在
  if (loginUser.name === "未登录") {
    console.log("未登录 发出请求")
  }

  const needAccess = to.meta?.access ?? ACCESS_ENUM.LOGIN;


  // 要跳转的页面必须登录
  if (needAccess !== ACCESS_ENUM.NOT_LOGIN) {
  //  // 如果没登录 就跳转到登录
    if (loginUser.name === "未登录" || !loginUser.role) {
      next(`/login`);
      return;
    }
  }

  // 如果登录用户没有权限访问需要的资源
  if (!checkAccess(loginUser, needAccess as string)) {
    next("/noAuth");
    return;
  }

  // 进行正常的路由跳转
  next();
});
