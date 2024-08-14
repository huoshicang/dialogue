<template>
  <a-layout>
    <a-layout-sider collapsible breakpoint="xl">
      <ChatMenu/>
      <!-- trigger -->
      <template #trigger="{ collapsed }">
        <IconCaretRight v-if="collapsed"></IconCaretRight>
        <IconCaretLeft v-else></IconCaretLeft>
      </template>
    </a-layout-sider>
    <a-layout>
      <ChatContent/>
    </a-layout>
  </a-layout>
</template>

<script setup lang="ts">
import {IconCaretLeft, IconCaretRight} from "@arco-design/web-vue/es/icon";
import ChatMenu from "./menu/index.vue";
import ChatContent from "./content/index.vue"
</script>
