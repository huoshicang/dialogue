import { my_post, my_get } from "./MyAxios";
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

  profile: async (): Promise<any> => {
    return await my_get("/profile", {});
  },
};
