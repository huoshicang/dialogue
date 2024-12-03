<template>
<!--  <a-comment align="right">-->
<!--    <template #actions v-if="message.role !== 'system'">-->
<!--      <span class="action" key="heart">-->
<!--        <icon-copy />-->
<!--      </span>-->
<!--      <span class="action" key="heart">-->
<!--          <icon-edit />-->
<!--      </span>-->
<!--    </template>-->
<!--    <template #avatar v-if="message.role !== 'system'">-->
<!--      <a-avatar>-->
<!--        <img-->
<!--          alt="avatar"-->
<!--          src="https://p1-arco.byteimg.com/tos-cn-i-uwbnlip3yd/3ee5f13fb09879ecb5185e440cef6eb9.png~tplv-uwbnlip3yd-webp.webp"-->
<!--        />-->
<!--      </a-avatar>-->
<!--    </template>-->
<!--    <template #content>-->
<!--      <div>-->
<!--        {{ message.content }}-->
<!--      </div>-->
<!--    </template>-->
<!--  </a-comment>-->



</template>
<script setup lang="ts">
import { defineProps } from "vue";

const props = defineProps({
  message: {
    type: Object,
    required: true,
  },
});

</script>
<style scoped>

</style>
