<template>
  <a-page-header
    :style="{ background: 'var(--color-bg-2)' }"
    :show-back="false"
  >
    <template #title>
      {{ user_info.username }}
    </template>
    <template #subtitle>
      {{ user_info.introduction }}
    </template>
    <template #extra>
      <a-button @click="bright_colors"> 亮色</a-button>
      <a-button @click="dark_colors"> 暗色</a-button>
    </template>
  </a-page-header>
</template>

<script setup lang="ts">
import { useUserStore } from "@/store";

const user_info = useUserStore().user_info;

const bright_colors = () => {
  // 设置为亮色主题
  document.body.removeAttribute("arco-theme");
};

const dark_colors = () => {
  // 设置为暗色主题
  document.body.setAttribute("arco-theme", "dark");
};
</script>

<style scoped>
#index {
}
</style>
