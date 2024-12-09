import { defineStore } from "pinia";
import { ModelState } from "./type";
import { Api } from "@/api/api";
import ACCESS_ENUM from "@/router/access-enum";

export const useRegistryStore = defineStore({
  id: "registry",
  state: () => {
    return {
      modelList: <ModelState[]>[],
      promptList: <ModelState[]>[],
    };
  },

  actions: {
    async getModelList() {
      try {
        const res = await Api.get_model_list();
        if (res.status_code === 200) this.modelList = res.data;
      } catch (error) {}
    },
    async getPromptList() {
      try {
        const res = await Api.get_prompt();
        if (res.status_code === 200) this.promptList = res.data;
      } catch (error) {}
    },
  },
  getters: {
    gettersModelList: (state) => {
      return state.modelList;
    },
    gettersPromptList: (state) => {
      return state.promptList;
    },
  },
});
