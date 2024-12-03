<template>
  <a-config-provider :locale="zhCN">
      <router-view name="app_view" v-slot="{ Component }">
        <transition name="fade">
          <keep-alive>
            <component :is="Component" />
          </keep-alive>
        </transition>
      </router-view>
  </a-config-provider>
</template>

<script setup lang="ts">
import zhCN from "@arco-design/web-vue/es/locale/lang/zh-cn";
import { darkTheme } from 'naive-ui'
import type { GlobalTheme } from 'naive-ui'
import { useRouter } from "vue-router";
import { onMounted, ref } from "vue";

const router = useRouter();

const theme = ref<GlobalTheme | null>(darkTheme)


// onMounted(() => router.push({ path: "/chat" }));
</script>
<style scoped>
.layout-demo-app {
  height: 100vh;
}

.layout-demo-app :deep(.arco-layout-header) {
  border-bottom: 1px solid var(--color-border-2);
}

.layout-demo-app :deep(.arco-layout-content) {
  justify-content: center;
  align-items: center;
  background-color: var(--color-bg-1);
}
</style>
