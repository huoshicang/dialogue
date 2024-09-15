<template>
  <a-row class="grid-demo">
    <a-col flex="auto">
      <a-comment>
        <template #author>{{ parse_role }}</template>
        <template #content>{{ parse_content }}</template>
<!--        <template #datetime>{{ parse_id_token }}</template>-->
        <template #actions> 复制 编辑 </template>
        <template #avatar>
          <a-avatar>
            <img
              alt="avatar"
              src="https://p1-arco.byteimg.com/tos-cn-i-uwbnlip3yd/3ee5f13fb09879ecb5185e440cef6eb9.png~tplv-uwbnlip3yd-webp.webp"
            />
          </a-avatar>
        </template>
      </a-comment>
    </a-col>
  </a-row>
</template>
<script setup lang="ts">
import { defineProps, computed } from "vue";

const props = defineProps({
  message: {
    type: Object,
    required: true,
    default: {
      status_code: 500,
    },
  },
});

// 解析role
const parse_role = computed(() => {
  const message = props.message;

  if (!message) return "未知";

  if (message.role) {
    switch (message.role) {
      case "system":
        return "预设";
      case "user":
        return "用户";
      default:
        return "未知";
    }
  }

  if (message.output?.choices[0]?.message?.role === "assistant") return "回复";

  return "未知";
});

// 解析content
const parse_content = computed(() => {
  const message = props.message;

  if (!message) return "未知";

  if (message.content) return message.content;

  if (message.output?.choices?.[0]?.message?.content)
    return message.output?.choices?.[0]?.message?.content;

  return "未知";
});

// 解析id 和 token
const parse_id_token = computed(() => {
  const message = props.message;

  if (!message) return "未知";

  if (!message.request_id) return "";

  return `对话ID：${message.request_id}；token：${message.usage.input_tokens} + ${message.usage.output_tokens} = ${message.usage.total_tokens}`;
});
</script>
<style scoped>
.grid-demo .arco-col:nth-child(2n + 1) {
  background-color: rgba(0, 0, 0, 0);
}

.grid-demo .arco-col:nth-child(2n) {
  background-color: rgba(0, 0, 0, 0.1);
}
</style>
