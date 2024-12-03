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
          :auto-size="{ maxRows: 4, minRows: 4 }"
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
          <a-button :loading="props.sendLoding">
            <template #icon>
              <icon-send @click="sendMessageFooter" />
            </template>
          </a-button>
        </n-button-group>
      </a-layout-sider>
    </a-layout>

    <span class="information">项目开发中</span>
  </div>
</template>

<script setup lang="ts">
import { ref, defineProps } from "vue";

const props = defineProps({
  sendLoding: {
    type: Boolean,
    required: false,
  },
});

const text = ref("");

const emit = defineEmits(["sendMessage"]);

const sendMessageFooter = () => {
  emit("sendMessage", text.value);
  text.value = "";
};
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
