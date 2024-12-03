<template>
    <a-layout-sider>
      <a-menu @menu-item-click="onClickMenuItem">
        <a-menu-item key="model">模型</a-menu-item>
        <a-menu-item key="key">密钥</a-menu-item>
      </a-menu>
    </a-layout-sider>
</template>

<script setup lang="ts">
import { useRouter } from "vue-router";

const router = useRouter();

const onClickMenuItem = (key) => {
  router.push(`/backstage/${key}`);
};
</script>

<style scoped>
#backstageSlider {
}
</style>
