<template>
  <ChatMenuNewChat :getData="getData" />

  <a-menu
    :style="{ width: '100%' }"
    @menu-item-click="onClickMenuItem"
    :default-selected-keys="menuSelected"
  >
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
import { onMounted, ref, watch } from "vue";
import { Api } from "@/api/api";
import { useUserStore } from "@/store";
import router from "@/router";
import { useRoute, useRouter } from "vue-router";
// 用户信息
const user_info = useUserStore().user_info;
const menuSelected = ref<string[]>(["1"]);
const route = useRoute();

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

const onClickMenuItem = (key: string) => router.push(`/chat/${key}`);

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

const setMenuSelected = (id: string) => {
  menuSelected.value = [id]
};

// 侦听路由的参数，以便再次获取数据
watch(() => route.params.id, setMenuSelected, { immediate: true });

</script>

<style scoped></style>
