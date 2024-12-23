<template>
  <div id="keyModal">
    <a-modal
      width="auto"
      v-model:visible="props.keyVisible.visible"
      :footer="false"
    >
      <template #title>{{ props.keyVisible.title }}</template>
      <a-scrollbar style="overflow: auto">
        <a-form
          ref="formRef"
          :rules="rules"
          :style="{ width: '600px' }"
          :model="form"
          @submit="handleSubmit"
        >
          <a-form-item field="key" label="密钥" validate-trigger="blur">
            <a-input v-model="form.key" />
          </a-form-item>
          <a-form-item
            field="availableModels"
            label="可用模型"
            validate-trigger="blur"
          >
            <a-select
              v-model:model-value="form.availableModels"
              placeholder="请选择模型"
              allow-clear
              multiple
            >
              <a-option
                v-for="(item, index) of RegistryStore.gettersModelList"
                :key="index"
                >{{ item.model_call }}
              </a-option>
            </a-select>
          </a-form-item>
          <a-form-item
            field="key_introduction"
            label="密钥说明"
            validate-trigger="blur"
          >
            <a-textarea
              v-model:model-value="form.key_introduction"
              :auto-size="{ maxRows: 4, minRows: 1 }"
              allow-clear
              show-word-limit
            />
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
            v-if="props.keyVisible.title === '编辑密钥'"
          >
            <a-switch v-model="form.enable" />
          </a-form-item>
          <a-form-item
            field="charging"
            label="是否进行计费"
            v-if="props.keyVisible.title === '编辑密钥'"
          >
            <a-switch v-model="form.charging" />
          </a-form-item>
          <a-button type="primary" html-type="submit"> 确认</a-button>
        </a-form>
      </a-scrollbar>
    </a-modal>
  </div>
</template>

<script setup lang="ts">
import {
  defineProps,
  defineEmits,
  reactive,
  watchEffect,
  onMounted,
} from "vue";
import { ValidatedError } from "@arco-design/web-vue/es/form/interface";
import { Api } from "@/api/api";
import { Message } from "@arco-design/web-vue";
import { useRegistryStore, useUserStore } from "@/store";
import { rules } from "@/components/backstage/pages/keys/config";

const RegistryStore = useRegistryStore();
const user_info = useUserStore().user_info;

const props = defineProps({
  keyVisible: {
    type: Object,
    required: true,
    default: {
      visible: false,
      title: null,
    },
  },
  keyInfo: {
    type: Object,
    required: true,
    default: {
      user_name: "",
      base_url: "",
      model_name: "",
      model_call: "",
      model_introduction: "",
      model_call_input: 0,
      model_call_output: 0,
      limit: 0,
      residue_limit: 0,
    },
  },
});

const emit = defineEmits(["setVisible", "requestData"]);

// 表单数据
const form = reactive<KeyInfo>({
  key: "",
  key_introduction: "",
  limit: null,
  residue_limit: null,
  availableModels: [],
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
  values: KeyInfo;
}) => {
  // 匹配弹窗标题
  switch (props.keyVisible.title) {
    // 添加模型
    case "新建模型":
      if (!errors) {
        try {
          values.user_name = user_info.username;
          values.user_id = user_info._id;

          const res = await Api.add_key(values);

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
    // 编辑密钥
    case "编辑密钥":
      if (!errors) {
        try {
          const res = await Api.update_key(form);
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
  if (props.keyVisible.visible) {
    // 匹配弹窗标题
    switch (props.keyVisible.title) {
      // 添加模型
      case "新建模型":
        form.key = "";
        form.key_introduction = "";
        form.availableModels = [];
        form.limit = null;
        form.residue_limit = null;
        form.enable = true;
        form.charging = true;
        break;
      // 编辑密钥
      case "编辑密钥":
        form.id = props.keyInfo._id;
        form.user_id = props.keyInfo.user_id;
        form.key = props.keyInfo.key;
        form.user_name = props.keyInfo.user_name;
        form.key_introduction = props.keyInfo.key_introduction;
        form.availableModels = props.keyInfo.availableModels;
        form.limit = props.keyInfo.limit;
        form.residue_limit = props.keyInfo.residue_limit;
        form.enable = props.keyInfo.enable;
        form.charging = props.keyInfo.charging;
        break;
      default:
        break;
    }
  }
});

// 获取模型列表
onMounted(async () => {
  if (RegistryStore.gettersModelList.length === 0) {
    await RegistryStore.getModelList();
  }
});
</script>

<style scoped>
#keyModal {
}
</style>
