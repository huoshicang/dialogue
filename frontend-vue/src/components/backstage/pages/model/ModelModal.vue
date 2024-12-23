<template>
  <div id="modelModal">
    <a-modal width="auto" v-model:visible="props.modalVisible.visible" :footer="false">
      <template #title>{{ props.modalVisible.title }}</template>
      <a-form
        ref="formRef"
        :rules="rules"
        :style="{ width: '600px' }"
        :model="form"
        @submit="handleSubmit"
      >
        <a-form-item field="base_url" label="Base url" validate-trigger="blur">
          <a-input v-model="form.base_url" />
        </a-form-item>
        <a-form-item field="Model_name" label="模型名" validate-trigger="blur">
          <a-input v-model="form.Model_name" />
        </a-form-item>
        <a-form-item
          field="Model_call"
          label="模型调用名"
          validate-trigger="blur"
        >
          <a-input v-model="form.Model_call" />
        </a-form-item>
        <a-form-item
          field="Model_introduction"
          label="模型描述"
          validate-trigger="blur"
        >
          <a-textarea
            v-model:model-value="form.Model_introduction"
            :auto-size="{ maxRows: 4, minRows: 1 }"
            allow-clear
            show-word-limit
          />
        </a-form-item>
        <a-form-item
          field="Model_tag"
          label="模型标签"
          validate-trigger="blur"
        >
          <a-select
            v-model:model-value="form.Model_tag"
            placeholder="请选择模型"
            allow-clear multiple
          >
            <a-option
              v-for="(item, index) of modelTag"
              :key="index"
            >{{ item }}</a-option>
          </a-select>
        </a-form-item>
        <a-form-item field="Model_call_input" label="模型输入计费">
          <a-input-number v-model="form.Model_call_input" />
        </a-form-item>
        <a-form-item field="Model_call_output" label="模型输出计费">
          <a-input-number v-model="form.Model_call_output" />
        </a-form-item>
        <a-form-item field="limit" label="总额度">
          <a-input-number v-model="form.limit" />
        </a-form-item>
        <a-form-item field="residue_limit" label="剩余额度">
          <a-input-number v-model="form.residue_limit" />
        </a-form-item>
        <a-form-item
          field="enable"
          label="是否启用"
          v-if="props.modalVisible.title === '编辑模型'"
        >
          <a-switch v-model="form.enable" />
        </a-form-item>
        <a-form-item
          field="charging"
          label="是否进行计费"
          v-if="props.modalVisible.title === '编辑模型'"
        >
          <a-switch v-model="form.charging" />
        </a-form-item>
        <a-button type="primary" html-type="submit"> 确认</a-button>
      </a-form>
    </a-modal>
  </div>
</template>

<script setup lang="ts">
import { defineProps, defineEmits, reactive, watchEffect } from "vue";
import { ValidatedError } from "@arco-design/web-vue/es/form/interface";
import { Api } from "@/api/api";
import { Message } from "@arco-design/web-vue";
import { useUserStore } from "@/store";
import { modelTag, rules } from "@/components/backstage/pages/model/config";


const user_info = useUserStore().user_info;

const props = defineProps({
  modalVisible: {
    type: Object,
    required: true,
    default: {
      visible: false,
      title: null,
    },
  },
  modelInfo: {
    type: Object,
    required: true,
    default: {
      _id: "",
      user_name: "",
      base_url: "",
      model_name: "",
      model_call: "",
      model_introduction: "",
      Model_tag: [],
      model_call_input: 0,
      model_call_output: 0,
      limit: 0,
      residue_limit: 0,
    },
  },
});

const emit = defineEmits(["setVisible", "requestData"]);

// 表单数据
const form = reactive<ModelInfoForm>({
  base_url: "",
  Model_name: "",
  Model_call: "",
  Model_introduction: "",
  Model_tag: [],
  Model_call_input: null,
  Model_call_output: null,
  limit: null,
  residue_limit: null,
  enable: false,
  charging: false,
});

/**
 * 提交表单
 * @param values 表单数据
 * @param errors 表单验证错误
 * @returns void
 */
const handleSubmit = async ({
  errors,
  values,
}: {
  errors: Record<string, ValidatedError> | undefined;
  values: ModelInfoForm;
}) => {

  switch (props.modalVisible.title) {
    // 添加模型
    case "新建模型":
      if (!errors) {
        try {
          values.user_name = user_info.username;
          values.user_id = user_info._id;

          const res = await Api.add_model(values);

          if (res.status_code === 200) {
            Message.success(res.message);
            emit("requestData");
          } else {
            Message.error(res.message);
          }
        } catch (err) {
          console.log("添加失败");
        } finally {
          emit("setVisible", { visible: false, title: null });
        }
      }
      break;
    // 编辑模型
    case "编辑模型":
      if (!errors) {
        try {
          values.user_name = user_info.username;
          values.user_id = user_info._id;
          const res = await Api.update_model(values);
          if (res.status_code === 200) {
            Message.success(res.message);
            emit("requestData");
          } else {
            Message.error(res.message);
          }
        } catch (err) {
          console.log("添加失败");
        } finally {
          emit("setVisible", { visible: false, title: null });
        }
      }
      break;
    default:
      break;
  }


};

// 监听弹窗状态 改变时 重置表单数据
watchEffect(() => {
  // 初始化表单数据
  // 如果弹窗是打开的
  if (props.modalVisible.visible) {
    // 匹配弹窗标题
    switch (props.modalVisible.title) {
      // 添加模型
      case "新建模型":
        form.base_url = "";
        form.Model_name = "";
        form.Model_call = "";
        form.Model_introduction = "";
        form.Model_tag = [];
        form.Model_call_input = null;
        form.Model_call_output = null;
        form.limit = null;
        form.residue_limit = null;
        form.enable = true;
        form.charging = true;
        break;
      // 编辑模型
      case "编辑模型":
        form.id = props.modelInfo._id;
        form.user_name = props.modelInfo.user_name;
        form.user_id = props.modelInfo.user_id;
        form.base_url = props.modelInfo.base_url;
        form.Model_name = props.modelInfo.model_name;
        form.Model_call = props.modelInfo.model_call;
        form.Model_introduction = props.modelInfo.model_introduction;
        form.Model_tag = props.modelInfo.model_tag;
        form.Model_call_input = props.modelInfo.model_call_input;
        form.Model_call_output = props.modelInfo.model_call_output;
        form.limit = props.modelInfo.limit;
        form.residue_limit = props.modelInfo.residue_limit;
        form.enable = props.modelInfo.enable;
        form.charging = props.modelInfo.charging;
        break;
      default:
        break;
    }
  }
});
</script>

<style scoped>
#modelModal {
}
</style>
