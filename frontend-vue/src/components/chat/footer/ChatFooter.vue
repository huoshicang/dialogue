<template>
  <div id="chatFooter">
    <a-layout class="chat-footer">
      <a-layout-sider>
        <!--清除消息-->
        <a-tooltip content="清除消息">
          <a-button @click="clearMessageFooter">
            <template #icon>
              <icon-delete />
            </template>
          </a-button>
        </a-tooltip>
      </a-layout-sider>
      <a-layout-content>
        <a-textarea
          ref="textarea"
          @keyup="handleKeyDown"
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
            @click="sendMessageFooter"
          >
            <template #icon>
              <icon-send />
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
import { Api } from "@/api/api";
import { useUserStore } from "@/store";
import { useRoute } from "vue-router";
import { Message } from "@arco-design/web-vue";

const UserStore = useUserStore().gettersUserInfo;
const route = useRoute();
const textarea = ref();

const props = defineProps({
  sendLoding: {
    type: Boolean,
    required: false,
  },
});

// 输入框文本
const text = ref<string>("");

// 父组件触发事件 发送消息
const emit = defineEmits(["sendMessage", "clearMessage"]);

// 发送消息
const sendMessageFooter = () => {
  emit("sendMessage", text.value);
  text.value = "";
};

/*
 * 清除消息
 * */
const clearMessageFooter = async () => {
  try {
    const res = await Api.clear_message({
      chat_id: route.params.id,
      user_id: UserStore._id,
    });
    if (res.status_code === 200) {
      Message.success(res.message);
      emit("clearMessage");
    } else Message.error(res.message);
  } catch (err) {
    console.log("获取失败");
  }
};

/*
 * 发送快捷键触发事件
 */
const handleKeyDown = (event) => {
  // 获取当前配置
  const submitKeyConfig =
    localStorage.getItem("submitKeyConfig") || "ctrlEnter";

  // 检查按键组合是否匹配当前配置，并返回是否应发送消息
  const shouldSendMessage = (config, event) => {
    console.log(config);
    console.log(config === "enter");

    if (config === "enter") return event.key === "Enter" && !event.ctrlKey;
    if (config === "ctrlEnter") return event.ctrlKey && event.key === "Enter";
    return false;
  };
  // 如果输入框为空，直接返回
  if (!text.value) return;

  // 根据配置判断是否应该发送消息
  if (shouldSendMessage(submitKeyConfig, event)) {
    sendMessageFooter();
    return;
  }

  if (event.key === "Enter") {
    event.preventDefault();
  }
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
      background-color: rgba(0, 0, 0, 0);
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
