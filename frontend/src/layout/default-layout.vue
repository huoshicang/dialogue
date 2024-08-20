<template>
  <a-layout class="layout-demo">
    <a-layout-header>
      <GlobalHeader />
    </a-layout-header>
    <router-view name="layout_view" v-slot="{ Component }">
      <transition name="fade">
        <keep-alive>
          <component :is="Component" />
        </keep-alive>
      </transition>
    </router-view>
  </a-layout>
</template>
<script setup>
import GlobalHeader from "../components/global/header/GlobalIndex.vue";
</script>
<style scoped>
.layout-demo {
  height: 100vh;
  background-color: var(--color-bg-1);
}

.layout-demo :deep(.arco-layout-header) {
  border: 1px solid var(--color-border);
}

.layout-demo :deep(.arco-layout-content) {
  color: var(--color-text-1);
  background-color: var(--color-fill-2);
  display: flex;
  flex-direction: column;
  justify-content: center;

  font-stretch: condensed;
  text-align: center;
}
</style>
