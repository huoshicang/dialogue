import ACCESS_ENUM from "./access-enum";
import { UserState } from "@/store/modules/user/type";

/**
 * 检查权限
 * @param {any} loginUser - 当前登录用户
 * @param {string} needAccess - 需要有的权限
 * @returns {boolean} 是否有无权限
 */

const checkAccess = (
  loginUser: UserState,
  needAccess: string = ACCESS_ENUM.NOT_LOGIN
): boolean => {
  // 获取登录用户的角色，如果用户未登录，则角色为 NOT_LOGIN
  const loginUserAccess = loginUser?.role ?? ACCESS_ENUM.NOT_LOGIN;

  if (needAccess === ACCESS_ENUM.NOT_LOGIN) {
    // 如果需要的访问权限为 NOT_LOGIN
    return true;
  }

  // 如果需要的访问权限为 USER
  if (needAccess === ACCESS_ENUM.USER) {
    // 如果用户没登录，那么表示无权限
    if (loginUserAccess === ACCESS_ENUM.NOT_LOGIN) {
      return false;
    }
  }

  // 如果需要的访问权限为 ADMIN
  if (needAccess === ACCESS_ENUM.ADMIN) {
    // 如果不为管理员，表示无权限
    if (loginUserAccess !== ACCESS_ENUM.ADMIN) {
      return false;
    }
  }

  return true;
};

export default checkAccess;
