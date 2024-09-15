<template>
  <a-scrollbar style="height: 600px; overflow: auto">
    <a-layout-content>
      <ChatContentComment
        v-for="(item, index) in list_data"
        :key="index"
        :message="item"
      />
    </a-layout-content>
  </a-scrollbar>
</template>
<script setup lang="ts">
import ChatContentComment from "@/components/chat/content/ChatContentComment.vue";

const list_data = [
  {
    role: "system",
    content: "You are a helpful assistant.",
  },
  {
    role: "user",
    content: "请介绍一下通义千问",
  },
  {
    status_code: 200,
    request_id: "a75a1b22-e512-957d-891b-37db858ae738",
    code: "",
    message: "",
    output: {
      text: null,
      finish_reason: null,
      choices: [
        {
          finish_reason: "stop",
          message: {
            role: "assistant",
            content:
              "通义千问是阿里云自主研发的超大规模语言模型，能够回答问题、创作文字，还能表达观点、撰写代码。作为一个大型预训练语言模型，我能够根据您提出的指令产出相关的回复，并尽可能提供准确和有用的信息。我会不断学习和进步，不断提升自己的能力，为用户提供更好的服务。如果您有任何问题或需要帮助，请随时告诉我。",
          },
        },
      ],
    },
    usage: {
      input_tokens: 25,
      output_tokens: 77,
      total_tokens: 102,
    },
  },
  {
    role: "user",
    content: "请介绍一下通义千问",
  },
  {
    status_code: 200,
    request_id: "a75a1b22-e512-957d-891b-37db858ae738",
    code: "",
    message: "",
    output: {
      text: null,
      finish_reason: null,
      choices: [
        {
          finish_reason: "stop",
          message: {
            role: "assistant",
            content:
              "通义千问是阿里云自主研发的超大规模语言模型，能够回答问题、创作文字，还能表达观点、撰写代码。作为一个大型预训练语言模型，我能够根据您提出的指令产出相关的回复，并尽可能提供准确和有用的信息。我会不断学习和进步，不断提升自己的能力，为用户提供更好的服务。如果您有任何问题或需要帮助，请随时告诉我。",
          },
        },
      ],
    },
    usage: {
      input_tokens: 25,
      output_tokens: 77,
      total_tokens: 102,
    },
  },
  {
    role: "user",
    content: "请介绍一下通义千问",
  },
  {
    status_code: 200,
    request_id: "a75a1b22-e512-957d-891b-37db858ae738",
    code: "",
    message: "",
    output: {
      text: null,
      finish_reason: null,
      choices: [
        {
          finish_reason: "stop",
          message: {
            role: "assistant",
            content:
              "通义千问是阿里云自主研发的超大规模语言模型，能够回答问题、创作文字，还能表达观点、撰写代码。作为一个大型预训练语言模型，我能够根据您提出的指令产出相关的回复，并尽可能提供准确和有用的信息。我会不断学习和进步，不断提升自己的能力，为用户提供更好的服务。如果您有任何问题或需要帮助，请随时告诉我。",
          },
        },
      ],
    },
    usage: {
      input_tokens: 25,
      output_tokens: 77,
      total_tokens: 102,
    },
  },
  {
    role: "user",
    content: "请介绍一下通义千问",
  },
  {
    status_code: 200,
    request_id: "a75a1b22-e512-957d-891b-37db858ae738",
    code: "",
    message: "",
    output: {
      text: null,
      finish_reason: null,
      choices: [
        {
          finish_reason: "stop",
          message: {
            role: "assistant",
            content:
              "通义千问是阿里云自主研发的超大规模语言模型，能够回答问题、创作文字，还能表达观点、撰写代码。作为一个大型预训练语言模型，我能够根据您提出的指令产出相关的回复，并尽可能提供准确和有用的信息。我会不断学习和进步，不断提升自己的能力，为用户提供更好的服务。如果您有任何问题或需要帮助，请随时告诉我。",
          },
        },
      ],
    },
    usage: {
      input_tokens: 25,
      output_tokens: 77,
      total_tokens: 102,
    },
  },
];
</script>
<style scoped>
.arco-layout-content {
  padding: 20px 100px;
}
</style>
