<template>
  <a-list :max-height="computedHeight" scrollbar :bordered="false"
    <a-list-item v-for="(item, index) in props.messageList" :key="index">
      <a-list-item-meta :title="item.role ? item.role : item['choices'][0]['delta']['role']" >
        <template #description>
            <MarkdownRenderer :markdown="item" />
        </template>
        <template #avatar>
          <a-avatar shape="square">
            <img
              alt="avatar"
              src="https://p1-arco.byteimg.com/tos-cn-i-uwbnlip3yd/3ee5f13fb09879ecb5185e440cef6eb9.png~tplv-uwbnlip3yd-webp.webp"
            />
          </a-avatar>
        </template>
      </a-list-item-meta>
      <template #actions>
        <icon-edit />
        <icon-delete />
      </template>
    </a-list-item>
  </a-list>
</template>
<script setup lang="ts">
import { computed, onBeforeUnmount, defineProps, ref } from "vue";
import MarkdownRenderer from "@/components/chat/content/MarkdownRenderer.vue";

const props = defineProps({
  messageList: {
    type: Array,
    required: true,
  },
});

/* 下面的就这样吧 */
// 创建响应式的窗口高度数据
const max_height = ref(window.innerHeight);

// 用于更新窗口高度的函数，当窗口大小变化时调用它来更新响应式数据的值
const updateWindowHeight = () => {
  max_height.value = window.innerHeight;
};

// 监听窗口大小变化
window.addEventListener("resize", updateWindowHeight);
updateWindowHeight();

// 在组件销毁前移除窗口大小变化的监听，避免内存泄漏
onBeforeUnmount(() => {
  window.removeEventListener("resize", updateWindowHeight);
});

// 计算属性，基于窗口高度的响应式数据进行计算，减去161再减去 footerHeight
const computedHeight = computed(() => {
  return max_height.value - 64 - 162;
});
</script>
<style scoped></style>
