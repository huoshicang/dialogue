<template>
  <a-menu
    :style="{ width: '100%' }"
    :selected-keys="selected_keys"
    @menu-item-click="new_chat_visible = true"
  >
    <a-menu-item key="1"> 创建聊天</a-menu-item>
  </a-menu>

  <a-drawer
    :width="600"
    :visible="new_chat_visible"
    @ok="handleOk"
    @cancel="new_chat_visible = false"
    unmountOnClose
    :ok-loading="ok_loading"
    :hide-cancel="ok_loading"
  >
    <template #title>创建新的聊天</template>
    <a-form :model="form">
      <a-form-item field="chat_title" tooltip="用来命名对话" label="标题">
        <a-input v-model="form.chat_title" placeholder="请输入标题" />
      </a-form-item>

      <a-form-item field="system" label="预设" tooltip="请输入标题">
        <a-select v-model="form.system" placeholder="请选择预设" allow-clear>
          <a-option value="你好">你好</a-option>
          <a-option value="小红书">小红书</a-option>
        </a-select>
      </a-form-item>

      <a-form-item
        field="chat_parameters.model"
        label="模型"
        tooltip="进行对话的模型"
      >
        <a-select
          v-model="form.chat_parameters.model"
          placeholder="请选择模型"
          allow-clear
        >
          <a-option value="qwen-plus">qwen-plus</a-option>
          <a-option value="qwen-turbo">qwen-turbo</a-option>
        </a-select>
      </a-form-item>

      <a-form-item
        field="system"
        label="生成的随机性"
        tooltip="取值越大，生成的随机性越高；取值越低，生成的确定性越高。"
      >
        <a-slider
          v-model="form.chat_parameters.top_p"
          :min="0"
          :max="1.0"
          :step="0.1"
        />
      </a-form-item>

      <a-form-item
        field="system"
        label="多样性"
        tooltip="控制模型回复的随机性和多样性"
      >
        <a-slider
          v-model="form.chat_parameters.temperature"
          :min="0.1"
          :max="1.9"
          :step="0.1"
        />
      </a-form-item>

<!--      <a-form-item field="system" label="联网搜索" tooltip="是否开启联网搜索">-->
<!--        <a-switch v-model="form.chat_parameters.enable_search">-->
<!--          <template #checked> 开启 </template>-->
<!--          <template #unchecked> 关闭 </template>-->
<!--        </a-switch>-->
<!--      </a-form-item>-->
    </a-form>
  </a-drawer>
</template>

<script setup lang="ts">
import { reactive, ref, watch } from "vue";
import { useUserStore } from "@/store";
import { Api } from "@/api/api";
import { Message } from "@arco-design/web-vue";

const props = defineProps(["getData"])

// 用户信息
const user_info = useUserStore().user_info;

// 新建聊天的弹窗开关
const new_chat_visible = ref<boolean>(false);
// 是否选中
const selected_keys = ref<string[]>([""]);
// 加载
const ok_loading = ref<boolean>(false);

const form = reactive({
  user_id: user_info._id,
  user_name: user_info.username,
  chat_title: "",
  system: "",
  chat_parameters: {
    model: "qwen-plus",
    messages: [],
    top_p: 0.7,
    temperature: 0.7,
    presence_penalty: null,
    max_tokens: null,
    response_foramt: "text",
    seed: null,
    stream: false,
    stop: null,
    tools: null,
    stream_options: null,
    enable_search: false
  },
});

// 创建新的聊天
const handleOk = async () => {
  ok_loading.value = true
  if (form.chat_title === "") form.chat_title = "新的聊天"

  try {
    const res = await Api.add_chat(form);

    if (res.status_code === 200) {
      Message.success(res.data.message);
      props.getData()
    } else {
      Message.error(res.message);
    }
  } catch (err) {
    console.log("创建失败");
  } finally {
    new_chat_visible.value = false;
    ok_loading.value = false;
    form.chat_title = ""
  }

};

watch(new_chat_visible, (new_value) => {
  if (new_value) {
    selected_keys.value = ["1"];
  } else {
    selected_keys.value = [""];
  }
});


</script>

<style scoped></style>
