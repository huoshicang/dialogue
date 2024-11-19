<template>
  <a-layout class="layout-demo-app">
    <a-layout-header>
      <GlobalHeader />
    </a-layout-header>
    <a-layout-content>
      <router-view name="default_layout_view" v-slot="{ Component }">
        <transition name="fade">
          <keep-alive>
            <component :is="Component" />
          </keep-alive>
        </transition>
      </router-view>
    </a-layout-content>
  </a-layout>
</template>
<script setup>
import GlobalHeader from "@/components/global/header/GlobalIndex.vue";
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
