<template>
  <a-page-header
    :style="{ background: 'var(--color-bg-2)' }"
    show-back
    @back="back"
  >
    <template #title>
      <span @click="setVisible(true)" style="cursor: pointer">{{
        user_info.username
      }}</span>
    </template>
    <template #subtitle>
      {{ user_info.introduction }}
      <a-breadcrumb>
        <a-breadcrumb-item>v1.0.0</a-breadcrumb-item>
      </a-breadcrumb>
    </template>
    <template #extra>
      <a-button @click="bright_colors"> 亮色</a-button>
      <a-button @click="dark_colors"> 暗色</a-button>
    </template>
  </a-page-header>

  <!-- 弹窗 -->
  <HeaderModal v-model:visible="visible" @setVisible="setVisible" />
</template>

<script setup lang="ts">
import HeaderModal from "./HeaderModal.vue";
import { useUserStore } from "@/store";
import { useRouter } from "vue-router";
import { ref } from "vue";

const router = useRouter();

const user_info = useUserStore().user_info;
// 设置为亮色主题
const bright_colors = () => document.body.removeAttribute("arco-theme");
// 设置为暗色主题
const dark_colors = () => document.body.setAttribute("arco-theme", "dark");

const visible = ref(false);

const setVisible = (setVisible) => (visible.value = setVisible);

const back = () => router.push("/");
</script>

<style scoped>
#index {
}
</style>
