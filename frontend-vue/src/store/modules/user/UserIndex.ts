import { defineStore } from "pinia";
import { UserState, ModelState } from "./type";
import { Api } from "@/api/api";
import ACCESS_ENUM from "@/router/access-enum";

export const useUserStore = defineStore({
  id: "user",
  state: () => {
    return {
      user_info: <UserState>{
        username: "未登录",
        role: ACCESS_ENUM.NOT_LOGIN,
      },
      modelList: <ModelState[]>[],
    };
  },

  actions: {
    async fetchUserProfile() {
      try {
        const res = await Api.profile();
        if (res.status_code === 200) {
          this.user_info = res.data;
        } else {
          this.user_info = {
            username: "未登录",
            role: ACCESS_ENUM.NOT_LOGIN,
          } as UserState;
        }
      } catch (error) {
        this.user_info = {
          username: "未登录",
          role: ACCESS_ENUM.NOT_LOGIN,
        } as UserState;
      }
    },
    async getModelList() {
      try {
        const res = await Api.get_model_list();
        if (res.status_code === 200) this.modelList = res.data;
      } catch (error) {}
    },
  },
  getters: {
    gettersModelList: (state) => {
      return state.modelList;
    },
    gettersUserInfo: (state) => {
      return state.user_info;
    },
  },
});
