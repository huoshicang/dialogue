<template>
  <!--列表-->
  <a-list
    :virtualListProps="{
      height: computedHeight,
    }"
    :bordered="false"
    @scrollIntoView="scrollIntoView"
    :data="props.messageList"
  >
    <template #item="{ item, index }">
      <a-list-item
        :key="index"
        :style="{
          background: item.role === 'user' ? 'var(--color-fill-3)' : '',
        }"
      >
        <a-list-item-meta>
          <template #description>
            <TextComponent :error="false" :text="item.content" />
          </template>
          <!--头像-->
          <template #avatar>
            <a-avatar
              shape="square"
              :style="
                item.role === 'user' ? { backgroundColor: '#3370ff' } : {}
              "
            >
              <IconUser v-if="item.role === 'user'" />
              <IconRobot v-if="item.role === 'assistant'" />
              <IconBrush v-if="item.role === 'system'" />
            </a-avatar>
          </template>
        </a-list-item-meta>
        <template #actions v-if="item.role === 'user'">
          <icon-edit />
          <icon-delete />
        </template>
      </a-list-item>
    </template>
  </a-list>
</template>
<script setup lang="ts">
import 'katex/dist/katex.min.css'
import '@/styles/lib/tailwind.css'
import '@/styles/lib/highlight.less'
import '@/styles/lib/github-markdown.less'
import '@/styles/global.less'
import { computed, onBeforeUnmount, defineProps, ref } from "vue";
import { IconUser, IconRobot, IconBrush } from "@arco-design/web-vue/es/icon";
import TextComponent from "@/components/chat/content/Message/Text.vue";

const props = defineProps({
  messageList: {
    type: Array,
    required: true,
  },
});

const scrollIntoView = () => {};

// 创建响应式的窗口高度数据
const windowHeight = ref(window.innerHeight);

// 用于更新窗口高度的函数
const updateWindowHeight = () => {
  windowHeight.value = window.innerHeight;
};

// 监听窗口大小变化
window.addEventListener("resize", updateWindowHeight);
updateWindowHeight();

// 在组件销毁前移除窗口大小变化的监听
onBeforeUnmount(() => {
  window.removeEventListener("resize", updateWindowHeight);
});

// 计算属性，基于窗口高度进行计算
const computedHeight = computed(() => {
  const footerHeight = 162; // 假设 footerHeight 是一个固定的值
  return windowHeight.value - 64 - footerHeight;
});
</script>
<style scoped>
:deep(.arco-list-item-main) {
  margin-right: 10px;
}
</style>
