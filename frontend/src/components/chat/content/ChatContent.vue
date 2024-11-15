<template>
<!--  <ChatContentComment-->
<!--    v-for="(item, index) in list_data"-->
<!--    :key="index"-->
<!--    :message="item"-->
<!--  />-->


</template>
<script setup lang="ts">
import ChatContentComment from "@/components/chat/content/ChatContentComment.vue";

const list_data = [
  {
    role: "system",
    content: "那是一个chatgpt",
  },
  {
    role: "user",
    content:
      "请介绍一下通义千问请介绍一下通义千问请介绍一下通义千问请介绍一下通义千问请介绍一下通义千问请介绍一下通义千问请介绍一下通义千问请介绍一下通义千问请介绍一下通义千问请介绍一下通义千问请介绍一下通义千问请介绍一下通义千问请介绍一下通义千问请介绍一下通义千问请介绍一下通义千问请介绍一下通义千问请介绍一下通义千问请介绍一下通义千问请介绍一下通义千问请介绍一下通义千问请介绍一下通义千问请介绍一下通义千问请介绍一下通义千问请介绍一下通义千问请介绍一下通义千问请介绍一下通义千问请介绍一下通义千问请介绍一下通义千问请介绍一下通义千问请介绍一下通义千问请介绍一下通义千问请介绍一下通义千问请介绍一下通义千问请介绍一下通义千问",
  },
  {
    role: "user",
    content: "请介绍一下通义千问",
  },
  {
    role: "user",
    content: "请介绍一下通义千问",
  },
  {
    role: "user",
    content: "请介绍一下通义千问",
  },
  {
    role: "user",
    content: "请介绍一下通义千问",
  },
  {
    role: "user",
    content: "请介绍一下通义千问",
  },
  {
    role: "user",
    content: "请介绍一下通义千问",
  },
  {
    role: "user",
    content: "请介绍一下通义千问结束",
  },
];
</script>
<style scoped>
.item {
  display: flex;
  align-items: center;
}
.avatar {
  width: 28px;
  border-radius: 50%;
  margin-right: 10px;
}
</style>
