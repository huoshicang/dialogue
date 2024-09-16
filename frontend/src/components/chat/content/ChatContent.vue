<template>
  <a-scrollbar style="height: 600px; overflow: auto">
    <a-layout-content>
      <!--      <ChatContentComment-->
      <!--        v-for="(item, index) in list_data"-->
      <!--        :key="index"-->
      <!--        :message="item"-->
      <!--      />-->
      <a-row
        class="grid-demo"
        style="margin-bottom: 16px"
        v-for="(item, index) in list_data"
        :key="index"
      >
        <a-col flex="100px"></a-col>
        <a-col flex="auto">
          {{ item }}
        </a-col>
        <a-col flex="100px"></a-col>
      </a-row>
    </a-layout-content>
  </a-scrollbar>
</template>
<script setup lang="ts">
import ChatContentComment from "@/components/chat/content/ChatContentComment.vue";

const list_data = [
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
    content: "请介绍一下通义千问",
  },
  {
    role: "user",
    content: "请介绍一下通义千问",
  },
];
</script>
<style scoped>
.grid-demo .arco-col {
  line-height: 30px;
  color: var(--color-white);
}

.grid-demo .arco-col:nth-child(2n + 1) {
  background-color: rgba(0, 0, 0, 0.1);
}

.grid-demo .arco-col:nth-child(2n) {
  background-color: rgba(0, 0, 0, 0.1);
}
</style>
