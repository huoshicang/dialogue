<template>
  <a-layout class="layout-demo-app">
    <a-layout-header>
      <GlobalHeader />
    </a-layout-header>
    <a-layout-content>
      <a-config-provider :locale="zhCN">
        <router-view name="app_view" v-slot="{ Component }">
          <transition name="fade">
            <keep-alive>
              <component :is="Component" />
            </keep-alive>
          </transition>
        </router-view>
      </a-config-provider>
    </a-layout-content>
  </a-layout>
</template>

<script setup>
import zhCN from "@arco-design/web-vue/es/locale/lang/zh-cn";
import GlobalHeader from "@/components/global/header/GlobalIndex.vue";
// import { useRouter } from "vue-router";
// import { onMounted } from "vue";

// const router = useRouter();

// onMounted(() => router.push({ path: "/chat" }));
</script>
<style scoped>
.layout-demo-app{
  height: 100vh;
}

.layout-demo-app :deep(.arco-layout-header) {
  border-bottom: 1px solid var(--color-border-2);
}

.layout-demo-app :deep(.arco-layout-content) {
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: var(--color-bg-1);
}
</style>
