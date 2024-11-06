<template>
    <a-skeleton :animation="true" id="appIndex">
      <a-space direction="vertical" :style="{width:'80%'}" size="large">
        <a-button @click="to_chat">跳转</a-button>
        <a-skeleton-line :rows="3" />
      </a-space>
    </a-skeleton>
</template>

<script setup lang="ts">
import { useRouter } from "vue-router";

const router = useRouter();

const to_chat = () => {
  router.push("/chat");
};
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
</style>
