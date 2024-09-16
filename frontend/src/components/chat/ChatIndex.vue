<template>
  <a-layout>
    <a-layout-sider collapsible>
      <ChatMenu />
      <!-- trigger -->
      <template #trigger="{ collapsed }">
        <IconCaretRight v-if="collapsed"></IconCaretRight>
        <IconCaretLeft v-else></IconCaretLeft>
      </template>
    </a-layout-sider>
    <a-layout>
      <ChatContent />
    <a-layout-footer>Footer</a-layout-footer>
    </a-layout>
  </a-layout>
</template>

<script setup lang="ts">
import { IconCaretLeft, IconCaretRight } from "@arco-design/web-vue/es/icon";
import ChatMenu from "./menu/ChatMenu.vue";
import ChatContent from "./content/ChatContent.vue";
</script>
