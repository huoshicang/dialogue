import { my_post } from "./MyAxios";
import { login_type, register_type } from "@/types/login/LogType";

export const Api = {
  // 注册
  register: async (data: register_type): Promise<any> => {
    return await my_post("/register", data);
  },
  // 登录
  login: async (data: login_type): Promise<any> => {
    return await my_post("/login", data);
  },
};
