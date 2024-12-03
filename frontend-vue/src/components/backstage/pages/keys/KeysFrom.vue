<template>
  <div id="keyFrom">
    <a-form :model="form" layout="inline" @submit="handleSubmit">
      <a-form-item>
        <a-space>
          <a-button html-type="submit" disabled>搜索</a-button>
          <a-button
            @click="emit('setVisible', { visible: true, title: '新建模型' })"
          >
            新建
          </a-button>
        </a-space>
      </a-form-item>
    </a-form>
  </div>
</template>

<script setup lang="ts">
import { reactive, defineProps, defineEmits } from "vue";
import { ValidatedError } from "@arco-design/web-vue/es/form/interface";

// 表单数据
const form = reactive({});

// 设置加载状态
const emit = defineEmits(["setLoading", "setData", "setVisible"]);
const props = defineProps({
  loading: {
    type: Boolean,
    default: false,
  },
});

const handleSubmit = async ({
  errors,
  values,
}: {
  errors: Record<string, ValidatedError> | undefined;
  values: unknown;
}) => {
  if (props.loading) return;
  if (!errors) {
    emit("setLoading", true);

    try {
      console.log("搜索成功");
      emit("setData", []);
    } catch (err) {
      console.log("搜索失败");
    } finally {
      emit("setLoading", false);
    }
  }
};
</script>

<style scoped>
#keyFrom {
}
</style>
