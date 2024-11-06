<template>
  <a-page-header :style="{ background: 'var(--color-bg-2)' }" show-back @back="back">
    <template #title>
      {{ user_info.username }}

    </template>
    <template #subtitle>
      {{ user_info.introduction }}
      <a-breadcrumb>
        <a-breadcrumb-item>聊天1</a-breadcrumb-item>
        <a-breadcrumb-item>聊天2</a-breadcrumb-item>
        <a-breadcrumb-item>聊天3</a-breadcrumb-item>
      </a-breadcrumb>
    </template>
    <template #extra>
      <a-button @click="bright_colors"> 亮色</a-button>
      <a-button @click="dark_colors"> 暗色</a-button>
    </template>
  </a-page-header>
</template>

<script setup lang="ts">
import { useUserStore } from "@/store";
import { useRouter } from "vue-router";

const router = useRouter();

const user_info = useUserStore().user_info;

const bright_colors = () => {
  // 设置为亮色主题
  document.body.removeAttribute("arco-theme");
};

const dark_colors = () => {
  // 设置为暗色主题
  document.body.setAttribute("arco-theme", "dark");
};

const back = () => router.push("/");

</script>

<style scoped>
#index {
}
</style>
