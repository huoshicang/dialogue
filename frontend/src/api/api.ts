import {my_get, my_post} from "./MyAxios";
import {login_type, register_type} from "../types/login";

export const Api = {
  // 注册
  register: async (data: register_type) => {
    return await my_post("/register", data);
  },
  // 登录
  login: async (data: login_type) => {
    return await my_post("/login", data);
  },
};


