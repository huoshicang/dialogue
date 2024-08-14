<template>
  <a-page-header :style="{ background: 'var(--color-bg-2)' }" :show-back="false">
    <template #title>
      {{name ?? "未登录"}}
    </template>
    <template #subtitle>
      {{introduction}}
    </template>
    <template #extra>
      <a-button @click="bright_colors"> 亮色</a-button>
      <a-button @click="dark_colors"> 暗色</a-button>
    </template>
  </a-page-header>
</template>

<script setup lang="ts">

import {useUserStore} from "../../../store/index"

const {name, introduction} = useUserStore().user_info


const bright_colors = () => {
  // 设置为亮色主题
  document.body.removeAttribute('arco-theme');
}


const dark_colors = () => {
  // 设置为暗色主题
  document.body.setAttribute('arco-theme', 'dark');
}


</script>

<style scoped>
#index {
}
</style>
