<template>
  <a-layout class="layout-demo-chat">
    <a-layout-sider collapsible>
      <ChatMenu />
      <!-- trigger -->
      <template #trigger="{ collapsed }">
        <IconCaretRight v-if="collapsed"></IconCaretRight>
        <IconCaretLeft v-else></IconCaretLeft>
      </template>
    </a-layout-sider>
    <a-layout>
      <a-layout-content>
        <ChatContent />
      </a-layout-content>
      <a-layout-footer>
        <ChatFooter />
      </a-layout-footer>
    </a-layout>
  </a-layout>
</template>

<script setup lang="ts">
import { IconCaretLeft, IconCaretRight } from "@arco-design/web-vue/es/icon";

import ChatMenu from "./menu/ChatMenu.vue";
import ChatContent from "./content/ChatContent.vue";
import ChatFooter from "./footer/ChatFooter.vue";
import { ref } from "vue";

const split = ref<string | number>(0.8);

const update_split = (size: string | number) => {
  split.value = size;
};
</script>

<style scoped>
.layout-demo-chat {
  display: flex;
  height: 100%;
}

.layout-demo-chat :deep(.arco-layout-content) {
  padding: 48px 48px 90px 48px;
  flex: 1;
}

.layout-demo-chat :deep(.arco-layout-footer) {
  background-color: var(--color-bg-2);
  border-top: 1px solid var(--color-border);
  height: 160px;
}
</style>
