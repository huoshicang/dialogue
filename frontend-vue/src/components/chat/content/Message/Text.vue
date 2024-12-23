<template>
  <div class="text-black" :class="wrapClass">
    <div ref="textRef" class="leading-relaxed break-words">
      <div>
        <div v-if="!asRawText" class="markdown-body" v-html="text" />
        <div v-else class="whitespace-pre-wrap" v-text="text" />
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { computed, onMounted, onUnmounted, onUpdated, ref, defineProps } from "vue";
import MarkdownIt from "markdown-it";
import MdKatex from "@vscode/markdown-it-katex";
import MdLinkAttributes from "markdown-it-link-attributes";
import MdMermaid from "mermaid-it-markdown";
import hljs from "highlight.js";
import { useBasicLayout } from "@/hooks/useBasicLayout";
import { copyToClip } from "@/utils/copy";

const props = defineProps({
  // 是否为错误信息
  error: {
    type: Boolean,
    default: false,
  },

  // 文本内容
  text: {
    type: String,
    default: "",
  },

  // 是否为纯文本
  asRawText: {
    type: Boolean,
    default: false,
  },
});

const { isMobile } = useBasicLayout();

const textRef = ref<HTMLElement>();

const mdi = new MarkdownIt({
  html: false,
  linkify: true,
  highlight(code, language) {
    const validLang = !!(language && hljs.getLanguage(language));
    if (validLang) {
      const lang = language ?? "";
      return highlightBlock(
        hljs.highlight(code, { language: lang }).value,
        lang,
      );
    }
    return highlightBlock(hljs.highlightAuto(code).value, "");
  },
});

mdi
  .use(MdLinkAttributes, { attrs: { target: "_blank", rel: "noopener" } })
  .use(MdKatex)
  .use(MdMermaid);

const wrapClass = computed(() => {
  return [
    "text-wrap",
    "min-w-[20px]",
    "rounded-md",
    isMobile.value ? "p-2" : "px-3 py-2",
    { "text-red-500": props.error },
  ];
});

const text = computed(() => {
  const value = props.text ?? "";
  if (!props.asRawText) {
    // 对数学公式进行处理，自动添加 $$ 符号
    const escapedText = escapeBrackets(escapeDollarNumber(value));
    return mdi.render(escapedText);
  }
  return value;
});

/*
* 高亮块
* @param str 文本
* @param lang 语言
* */
const highlightBlock = (str: string, lang?: string) => {
  return `<pre class="code-block-wrapper"><div class="code-block-header"><span class="code-block-header__lang">${lang}</span><span class="code-block-header__copy">复制代码</span></div><code class="hljs code-block-body ${lang}">${str}</code></pre>`;
}

/*
* 添加复制事件
* */
const addCopyEvents = () => {
  if (textRef.value) {
    const copyBtn = textRef.value.querySelectorAll(".code-block-header__copy");
    copyBtn.forEach((btn) => {
      btn.addEventListener("click", () => {
        const code = btn.parentElement?.nextElementSibling?.textContent;
        if (code) {
          copyToClip(code).then(() => {
            btn.textContent = "复制成功";
            setTimeout(() => {
              btn.textContent = "复制代码";
            }, 1000);
          });
        }
      });
    });
  }
}

/*
* 移除复制事件
* */
function removeCopyEvents() {
  if (textRef.value) {
    const copyBtn = textRef.value.querySelectorAll(".code-block-header__copy");
    copyBtn.forEach((btn) => {
      btn.removeEventListener("click", () => {});
    });
  }
}

function escapeDollarNumber(text: string) {
  let escapedText = "";

  for (let i = 0; i < text.length; i += 1) {
    let char = text[i];
    const nextChar = text[i + 1] || " ";

    if (char === "$" && nextChar >= "0" && nextChar <= "9") char = "\\$";

    escapedText += char;
  }

  return escapedText;
}

function escapeBrackets(text: string) {
  const pattern =
    /(```[\s\S]*?```|`.*?`)|\\\[([\s\S]*?[^\\])\\\]|\\\((.*?)\\\)/g;
  return text.replace(
    pattern,
    (match, codeBlock, squareBracket, roundBracket) => {
      if (codeBlock) return codeBlock;
      else if (squareBracket) return `$$${squareBracket}$$`;
      else if (roundBracket) return `$${roundBracket}$`;
      return match;
    },
  );
}

onMounted(() => {
  addCopyEvents();
});

onUpdated(() => {
  addCopyEvents();
});

onUnmounted(() => {
  removeCopyEvents();
});
</script>

<style lang="less">
@import url(./style.less);
</style>
