<template>
  <div id="backstageIndex">
    <a-layout class="backstage-layout-demo">
      <BackstageSider />
      <BackstageContent />
    </a-layout>
  </div>
</template>

<script setup lang="ts">
import BackstageSider from "@/components/backstage/sider/backstageSider.vue";
import BackstageContent from "@/components/backstage/content/backstageContent.vue";
</script>

<style scoped>
.backstage-layout-demo {
  height: calc(100vh - 70px);
  border: 1px solid var(--color-border);
  background: var(--color-bg-3);
}

.backstage-layout-demo :deep(.arco-layout-content) {
  color: var(--color-text-2);
  font-weight: 400;
  font-size: 14px;
  background: var(--color-bg-3);
}
</style>
