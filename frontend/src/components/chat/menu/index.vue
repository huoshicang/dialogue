<template>
  <a-menu :style="{ width: '100%' }"@menu-item-click="onClickMenuItem">
    <a-menu-item key="0_1">
      Menu 1
    </a-menu-item>
  </a-menu>
</template>

<script setup lang="ts">
import {Message} from "@arco-design/web-vue";

const onClickMenuItem = (key: string) => {
  Message.info({content: `You select ${key}`, showIcon: true});
}
</script>

<style scoped>
</style>
