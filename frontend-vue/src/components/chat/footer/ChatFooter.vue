<template>
  <div id="chatFooter">
    <a-layout class="chat-footer">
      <a-layout-sider>
        <a-button-group type="primary">
          <!--清除消息-->
          <a-tooltip content="清除消息">
            <a-button type="outline">
              <template #icon>
                <icon-delete @click="sendMessageFooter" />
              </template>
            </a-button>
          </a-tooltip>
        </a-button-group>
      </a-layout-sider>
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
        <n-button-group vertical>
          <a-button
            :loading="props.sendLoding"
            type="outline"
            :disabled="!text"
          >
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

// 输入框文本
const text = ref<string>("");

// 父组件触发事件 发送消息
const emit = defineEmits(["sendMessage"]);

// 发送消息
const sendMessageFooter = () => {
  emit("sendMessage", text.value);
  text.value = "";
};
</script>

<style scoped lang="less">
#chatFooter {
  padding: 0 10px;

  .information {
    padding: 5px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    color: var(--color-text-4);
    font-stretch: condensed;
    text-align: center;
  }

  .chat-footer {
    padding-top: 10px;
    display: flex;
    align-items: center;

    .arco-layout-content {
      margin: 0 10px;
    }

    :deep(.arco-layout-content) {
      padding: 0;
    }

    :deep(.arco-layout-sider-light) {
      box-shadow: None;
      width: auto !important;
    }

    :deep(.arco-btn-size-medium.arco-btn-only-icon) {
      height: 34px;
      width: 34px;
    }
  }
}
</style>
