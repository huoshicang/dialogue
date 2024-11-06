<template>
  <a-comment :author="get_role(message.role)" align="right">
    <template #actions v-if="message.role !== 'system'">
      <span class="action" key="heart">
        <icon-copy />
      </span>
      <span class="action" key="heart">
          <icon-edit />
      </span>
    </template>
    <template #avatar v-if="message.role !== 'system'">
      <a-avatar>
        <img
          alt="avatar"
          src="https://p1-arco.byteimg.com/tos-cn-i-uwbnlip3yd/3ee5f13fb09879ecb5185e440cef6eb9.png~tplv-uwbnlip3yd-webp.webp"
        />
      </a-avatar>
    </template>
    <template #content>
      <div>
        {{ message.content }}
      </div>
    </template>
  </a-comment>
</template>
<script setup lang="ts">
import { defineProps } from "vue";

const props = defineProps({
  message: {
    type: Object,
    required: true,
  },
});

const get_role = (role: string) => {
  switch (role) {
    case "user":
      return "我";
    case "assistant":
      return "AI";
    case "system":
      return "预设";
    default:
      return "未知";
  }
};

</script>
<style scoped>
.action {
  display: inline-block;
  padding: 0 4px;
  color: var(--color-text-1);
  line-height: 24px;
  background: transparent;
  border-radius: 2px;
  cursor: pointer;
  transition: all 0.1s ease;
}

.action:hover {
  background: var(--color-fill-3);
}
</style>
