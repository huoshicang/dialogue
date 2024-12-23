<template>
  <a-layout class="layout-demo-chat">
    <a-layout-sider collapsible hide-trigger>
      <ChatMenu />
      <!-- trigger -->
      <template #trigger="{ collapsed }">
        <IconCaretRight v-if="collapsed"></IconCaretRight>
        <IconCaretLeft v-else></IconCaretLeft>
      </template>
    </a-layout-sider>
    <a-layout>
      <a-layout-content>
        <ContentEmpty v-if="!chatId" />
        <ChatContent v-else :messageList="messageList" />
      </a-layout-content>
      <a-layout-footer>
        <ChatFooter @sendMessage="sendMessage" @clearMessage="clearMessage" :sendLoding="sendLoding" />
      </a-layout-footer>
    </a-layout>
  </a-layout>
</template>

<script setup lang="ts">
import { IconCaretLeft, IconCaretRight } from "@arco-design/web-vue/es/icon";
import ChatMenu from "./menu/ChatMenu.vue";
import ChatContent from "./content/ChatContent.vue";
import ContentEmpty from "./content/ContentEmpty.vue";
import ChatFooter from "./footer/ChatFooter.vue";
import { useRoute, useRouter } from "vue-router";
import { onMounted, ref, watch } from "vue";
import { useUserStore } from "@/store";
import { Api } from "@/api/api";
import { Message } from "@arco-design/web-vue";

const UserStore = useUserStore();
const route = useRoute();
const router = useRouter();
const sendLoding = ref(false);
const chatId = ref<string | undefined | null>(null);
const messageList = ref([]);

/*
 * 获取聊天记录
 * @param id 聊天id
 * @return void
 * */
const getMessage = async (id) => {
  if (!id) {
    chatId.value = null;
    return;
  }
  chatId.value = id;

  try {
    const res = await Api.get_message({
      chatId: id,
      userId: UserStore.gettersUserInfo._id,
    });
    if (res.status_code === 200) {
      Message.success(res.message);
      messageList.value = res.data.messages;
    } else Message.error(res.message);
  } catch (err) {
    console.log("获取失败");
  }
};

/*
 * 发送消息
 * @param sendMessage 发送的消息
 * @return void
 * */
const sendMessage = (sendMessage) => {
  sendLoding.value = true;
  const host =
    process.env.VUE_APP_WS_BALEURL !== "/dialogue/message"
      ? process.env.VUE_APP_BALEURL.replace(`${window.location.protocol}//`, "")
      : window.location.host;

  const protocol = window.location.protocol === "https:" ? "wss" : "ws";
  const socket = new WebSocket(
    `${protocol}://${host}${process.env.VUE_APP_WS_BALEURL}`,
  );
  let messageListIndex = null;

  socket.onopen = function () {
    // 添加消息到列表
    messageList.value.push({
      content: sendMessage,
      role: "user",
    });

    // 添加回复消息
    messageList.value.push({
      content: "",
      role: "assistant",
    });
    // 获取消息列表最后一项的索引
    messageListIndex = messageList.value.length - 1;
    // 发送初始消息或参数
    socket.send(
      JSON.stringify({
        chatId: chatId.value,
        userId: UserStore.gettersUserInfo._id,
        sendMessage: sendMessage,
      }),
    );
  };

  /*
   * 接收消息 拼接到最后一项
   * @param event 接收到的消息
   * @return void
   * */
  socket.onmessage = function (event) {
    if (event.data)
      messageList.value[messageListIndex]["content"] += event.data;
  };

  /*
   * 错误处理
   * @return void
   * */
  socket.onerror = function (error) {
    messageList.value[messageListIndex]["content"] = error;
    sendLoding.value = false;
  };

  socket.onclose = function () {
    sendLoding.value = false;
  };
};


/*
* 清空消息
* @return void
* */
const clearMessage = () => {
  if (messageList.value && messageList.value.length > 0 && messageList.value[0].role === 'system') {
    // 如果数组存在，长度大于0，且第一项的role为'system'，则保留第一项，删除其他项
    messageList.value = [messageList.value[0]];
  } else {
    // 如果第一项的role不为'system'，则清空数组
    messageList.value = [];
  }
}

watch(() => route.params.id, getMessage, { immediate: true });

onMounted(() => {
  chatId.value = route.params.id as string;
});
</script>

<style scoped lang="less">
.layout-demo-chat {
  display: flex;
  height: 100%;

  :deep(.arco-layout-footer) {
    background-color: var(--color-bg-2);
    max-height: 160px;
  }
}
</style>
