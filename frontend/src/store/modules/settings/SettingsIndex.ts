import { ref } from "vue";
import { defineStore } from "pinia";
import { generateRandomString } from "@/tools/randomStringGenerator";

export const useSettingsStore = defineStore(
  "useSettings",
  () => {
    // 主题
    const login_id = ref<string>(generateRandomString());

    return {
      login_id,
    };
  },
  {
    persist: {
      key: "settings",
      storage: localStorage,
    },
  },
);
