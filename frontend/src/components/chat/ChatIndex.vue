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
          <ChatContent :footerHeight="footerHeight"  />
      </a-layout-content>
      <a-layout-footer  >
        <ChatFooter  @update-height="handleUpdateFooterHeight" />
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

const footerHeight = ref(0);

const handleUpdateFooterHeight = (height) => {
  // console.log(height);
  footerHeight.value = height;
};

</script>

<style scoped>
.layout-demo-chat {
  display: flex;
  height: 100%;
}

.layout-demo-chat :deep(.arco-layout-content) {
}

.layout-demo-chat :deep(.arco-layout-footer) {
  background-color: var(--color-bg-2);
  border-top: 1px solid var(--color-border);
  max-height: 160px;
}
</style>
