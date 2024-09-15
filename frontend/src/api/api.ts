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
  // 获取验证信息
  profile: async (): Promise<any> => {
    return await my_get("/profile", {});
  },

  /* 聊天 */
  get_chat_list: async (data: any): Promise<any> => {
    return await my_get("/v1/retrieve/chat", data);
  },
  // 添加聊天
  add_chat: async (data: object): Promise<any> => {
    return await my_post("/v1/create/chat", data);
  },
};
