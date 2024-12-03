import { ref } from "vue";
import { defineStore } from "pinia";

export const useSettingsStore = defineStore(
  "useSettings",
  () => {


    return {

    };
  },
  {
    persist: {
      key: "settings",
      storage: localStorage,
    },
  },
);
