<template>
  <a-page-header
    :style="{ background: 'var(--color-bg-2)' }"
    show-back
    @back="back"
  >
    <template #title>
      <span @click="setVisible(true)" style="cursor: pointer">
        {{ user_info.username }}
      </span>
    </template>
    <template #subtitle>
      {{ user_info.introduction }}
      <a-breadcrumb>
        <a-breadcrumb-item>v1.1.2</a-breadcrumb-item>
      </a-breadcrumb>
    </template>
    <template #extra>
      <a-button @click="onChangeTheme" shape="circle">
        <template #icon>
          <icon-sun-fill v-if="theme === 'dark'" />
          <icon-moon-fill v-else />
        </template>
      </a-button>
    </template>
  </a-page-header>

  <!-- 弹窗 -->
  <HeaderModal v-model:visible="visible" @setVisible="setVisible" />
</template>

<script setup lang="ts">
import HeaderModal from "./HeaderModal.vue";
import { useUserStore } from "@/store";
import { useRouter } from "vue-router";
import { onMounted, ref } from "vue";

const router = useRouter();

const user_info = useUserStore().user_info;
const theme = ref<string>("")

const onChangeTheme = () => {
  theme.value = theme.value === "dark" ? "" : "dark";
  document.body.setAttribute("arco-theme", theme.value);
};

const visible = ref(false);

const setVisible = (setVisible) => (visible.value = setVisible);

const back = () => router.push("/");

onMounted(() => {
  if (localStorage.getItem("theme")){
    theme.value = localStorage.getItem("theme") as string
  }else {
    localStorage.setItem("theme", "")
  }
})
</script>

<style scoped>
#index {
}
</style>
