<template>
  <div id="chatFooter" ref="myDiv">
    <a-space direction="vertical">
      <a-button-group type="primary">
        <a-button type="text" size="mini">copy</a-button>
      </a-button-group>
    </a-space>

    <a-layout class="chat-footer">
      <a-layout-content>
        <a-textarea
          v-model:model-value="text"
          placeholder="请输入内容"
          :max-length="{ length: 4000, errorOnly: true }"
          :auto-size="{ maxRows: 4 }"
          allow-clear
          show-word-limit
        />
      </a-layout-content>
      <a-layout-sider>
        <n-button-group vertical v-show="text">
          <a-button v-show="text.length > 400">
            <template #icon>
              <icon-expand />
            </template>
          </a-button>
          <a-button>
            <template #icon>
              <icon-send />
            </template>
          </a-button>
        </n-button-group>
      </a-layout-sider>
    </a-layout>

    <span class="information">啊啊</span>
  </div>
</template>

<script setup lang="ts">
import { onMounted, ref } from "vue";

const text = ref("");

const myDiv = ref(null);
const height = ref(0);

const emit = defineEmits(['update-height']);

let resizeObserver;

onMounted(() => {
  if (myDiv.value) {

    resizeObserver = new ResizeObserver((entries) => {
      for (let entry of entries) {
        emit('update-height',entry.contentRect.height);
      }
    });

    resizeObserver.observe(myDiv.value);
  }
});



</script>

<style scoped>
#chatFooter .information {
  padding: 5px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  color: var(--color-text-4);
  font-stretch: condensed;
  text-align: center;
}

#chatFooter .chat-footer :deep(.arco-layout-content) {
  padding: 0;
}

#chatFooter .chat-footer :deep(.arco-layout-sider-light) {
  box-shadow: None;
  width: auto !important;
}

#chatFooter .chat-footer :deep(.arco-btn-size-medium.arco-btn-only-icon) {
  height: 34px;
  width: 34px;
}
</style>
