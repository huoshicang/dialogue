import { defineStore } from "pinia";
import { UserState } from "./type";
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
  },
  getters: {
    gettersUserInfo: (state) => {
      return state.user_info;
    },
  },
});
