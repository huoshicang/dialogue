<template>
  <ChatMenuNewChat :getData="getData" />

  <a-menu :style="{ width: '100%' }" @menu-item-click="onClickMenuItem">
    <!--加载-->
    <a-skeleton animation v-if="chat_list_loading">
      <a-space direction="vertical" :style="{ width: '100%' }" size="large">
        <a-skeleton-line :rows="3" />
      </a-space>
    </a-skeleton>

    <!-- 空 -->
    <a-empty v-if="chat_list.length == 0" />

    <!--历史-->
    <template v-else>
      <a-dropdown
        trigger="contextMenu"
        alignPoint
        v-for="(item, index) in chat_list"
        :key="index"
      >
        <a-menu-item :key="item._id">{{ item.chat_title }}</a-menu-item>
        <template #content>
          <a-doption
            @click="
              deleteChat({
                chat_id: item._id,
                message_id: item.message_id,
              })
            "
            >删除此记录
          </a-doption>
        </template>
      </a-dropdown>
    </template>
  </a-menu>
</template>

<script setup lang="ts">
import { Message } from "@arco-design/web-vue";
import ChatMenuNewChat from "@/components/chat/menu/ChatMenuNewChat.vue";
import { onMounted, ref } from "vue";
import { Api } from "@/api/api";
import { useUserStore } from "@/store";
// 用户信息
const user_info = useUserStore().user_info;

// 历史聊天
const chat_list = ref<
  {
    _id: string;
    chat_title: string;
    message_id: string;
  }[]
>([]);

// 加载状态
const chat_list_loading = ref(true);

// todo 获取消息
const onClickMenuItem = (key: string) => {
  Message.info({ content: `You select ${key}`, showIcon: true });
};

// 请求数据
const getData = async () => {
  try {
    const res = await Api.get_chat_list({
      user_id: user_info._id,
    });

    if (res.status_code === 200) {
      chat_list.value = res.data;
    } else {
      Message.error(res.message);
    }
  } catch (err) {
    console.log("获取聊天失败");
  } finally {
    chat_list_loading.value = false;
  }
};

// 删除聊天
const deleteChat = async (data) => {
  try {
    const res = await Api.delete_chat({
      user_id: user_info._id,
      ...data,
    });

    console.log(res);

    if (res.status_code === 200) {
      Message.success(res.message);
      await getData();
    } else {
      Message.error(res.message);
    }
  } catch (err) {
    Message.error("删除失败");
  }
};

// todo历史聊天需要滚动

onMounted(async () => getData());
</script>

<style scoped></style>
