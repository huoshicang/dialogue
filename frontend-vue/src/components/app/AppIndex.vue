<template>
  <div id="appIndex">
    <a-card
      v-for="(item, index) in cardList"
      class="card-demo"
      :title="item.title"
      hoverable
      @click="router.push(item.cardPath)"
    >
      {{ item.description }}
    </a-card>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from "vue-router";

const router = useRouter();

const cardList = <{
    title: string;
    description: string;
    cardPath: string;
  }[]>[
  {
    title: "聊天",
    description: "点击去聊天室",
    cardPath: "/chat",
  },
];
</script>

<style scoped>
#appIndex {
  display: flex;
  height: 100%;
  width: 100%;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}

#appIndex .card-demo {
  width: 200px;
  transition-property: all;
}

#appIndex .card-demo:hover {
  transform: translateY(-10px);
}
</style>
