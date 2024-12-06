<template>
  <!--  <div v-if="props.markdown['id']">-->
  <!--    <div v-html="marked.parse( props.markdown['choices'][0]['delta']['content'])" class="markdown-content" />-->
  <!--  </div>-->
  <!--  <div v-else>-->
  <!--    <div v-html="marked.parse(props.markdown['content'])" class="markdown-content" />-->
  <!--  </div>-->
  <div
    v-html="marked.parse(props.markdown['content'])"
    class="markdown-content"
  />
</template>

<script setup>
import { marked } from "marked";
import "github-markdown-css/github-markdown.css";
import hljs from "highlight.js";
import "highlight.js/styles/default.min.css";
import { markedHighlight } from "marked-highlight";

const options = {
  langPrefix: "hljs language-", // 给高亮的语言类名添加前缀，可按需修改
  highlight(code, lang) {
    const validLang = hljs.getLanguage(lang) ? lang : "plaintext";
    return hljs.highlight(code, { language: validLang, ignoreIllegals: true })
      .value;
  },
};
marked.use(markedHighlight, options);

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
