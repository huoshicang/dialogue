<template>
  <a-layout class="layout-demo-chat">
    <a-layout-sider collapsible>
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
        <ChatFooter @sendMessage="sendMessage" :sendLoding="sendLoding" />
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

const getMessage = async (id) => {
  if (!id) return;
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

const sendMessage = (sendMessage) => {
  sendLoding.value = true;
  const host = process.env.VUE_APP_WS_BALEURL !== "/dialogue/message" ? process.env.VUE_APP_BALEURL.replace(`${window.location.protocol}//`, "") : window.location.host;

  const protocol = window.location.protocol === "https:" ? "wss" : "ws";
  const socket = new WebSocket(
    `${protocol}://${host}${process.env.VUE_APP_WS_BALEURL}`,
  );
  let messageListIndex = null;

  socket.onopen = function () {
    messageList.value.push({
      content: sendMessage,
      role: "user",
    });
    messageList.value.push({
      content: "",
      role: "assistant",
    });
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

  socket.onmessage = function (event) {
    if (event.data)
      messageList.value[messageListIndex]["content"] += event.data;
  };

  socket.onerror = function (error) {
    messageList.value[messageListIndex]["content"] = error;
    sendLoding.value = false;
  };

  socket.onclose = function () {
    console.log("WebSocket连接已关闭");
    sendLoding.value = false;
  };
};

watch(() => route.params.id, getMessage, { immediate: true });

onMounted(() => {
  chatId.value = route.params.id as string;
});
</script>

<style scoped>
.layout-demo-chat {
  display: flex;
  height: 100%;
}

.layout-demo-chat :deep(.arco-layout-content) {
}

.layout-demo-chat :deep(.arco-layout-footer) {
  background-color: var(--color-bg-2);
  border-top: 1px solid var(--color-border);
  max-height: 160px;
}
</style>
