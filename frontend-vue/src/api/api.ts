import { my_post, my_get } from "./MyAxios";
import { login_type, register_type } from "@/types/login/LogType";
import { add_chat_type, get_chat_list_type, get_model_table_type } from "@/types/Response/ApiTypes";

export const Api = {
  // 注册
  register: async (data: register_type): Promise<any> => {
    return await my_post("/log/register", data);
  },
  // 登录
  login: async (data: login_type): Promise<any> => {
    return await my_post("/log/login", data);
  },
  // 获取验证信息
  profile: async (): Promise<any> => {
    return await my_get("/log/profile", {});
  },

  // 获取聊天
  get_chat_list: async (data: get_chat_list_type): Promise<any> => {
    return await my_get("/v1/retrieve/chat", data);
  },
  // 添加聊天
  add_chat: async (data: object): Promise<any> => {
    return await my_post("/v1/create/chat", data);
  },
  // 删除聊天
  delete_chat: async (data: object): Promise<any> => {
    return await my_post("/v1/delete/chat", data);
  },

  // 获取模型表格
  get_model_table: async (data: get_model_table_type): Promise<any> => {
    return await my_post("/v1/retrieve/model", data);
  },

  // 添加模型
  add_model: async (data: ModelInfo): Promise<any> => {
    return await my_post("/v1/create/model", data);
  },

  // 获取模型列表
  get_model_list: async (): Promise<any> => {
    return await my_get("/v1/retrieve/models", {});
  },

  // 添加密钥
  add_key: async (data: KeyInfo): Promise<any> => {
    return await my_post("/v1/create/key", data);
  },

  // 获取密钥列表
  get_key_list: async (data: object): Promise<any> => {
    return await my_post("/v1/retrieve/key", data);
  },

  // 获取消息
  get_message: async (data: object): Promise<any> => {
    return await my_post("/v1/retrieve/message", data);
  },

  // 获取提示词
  get_prompt: async (): Promise<any> => {
    return await my_get("/v1/retrieve/prompts", {});
  },
};
