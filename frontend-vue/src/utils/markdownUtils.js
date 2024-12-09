import shiki from "shiki";
import MarkdownIt from "markdown-it";

const md = MarkdownIt();
// 异步函数来初始化Shiki并返回语法高亮后的HTML
const markdownToHtmlWithHighlight = async (markdownText) => {
  const highlighter = await shiki.getHighlighter({ theme: "nord" });
  md.set({
    highlight: (str, lang) => {
      if (lang && highlighter) {
        return highlighter.codeToHtml(str, lang);
      }
      return "";
    },
  });
  return md.render(markdownText);
};
export { markdownToHtmlWithHighlight };
