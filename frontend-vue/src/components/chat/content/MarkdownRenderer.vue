<template>
  <div v-if="props.markdown['id']">
    <div v-html="marked.parse( props.markdown['choices'][0]['delta']['content'])" class="markdown-content" />
  </div>
  <div v-else>
    <div v-html="marked.parse(props.markdown['content'])" class="markdown-content" />
  </div>
</template>

<script setup>
import { marked } from "marked";

// 接收 props
const props = defineProps({
  markdown: {
    type: String,
    required: false,
    default: "",
  },
});

</script>

<style scoped>
.markdown-content {
  /* 你可以在这里添加样式 */
}
</style>
