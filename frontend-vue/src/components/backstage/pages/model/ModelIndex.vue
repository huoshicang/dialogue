<template>
  <div id="modelIndex">
    <!-- 表单 -->
    <ModelFrom
      @setLoading="setLoading"
      @setData="setData"
      @setVisible="setVisible"
      :loading="loading"
    />

    <!-- 表格 -->
    <a-table
      :columns="columns"
      :data="tableData"
      :loading="loading"
      :scroll="{
        x: 2000,
      }"
    >
      <template #user_name="{ record }">
        <a-tag size="large">{{ record.user_name }}</a-tag>
      </template>
      <template #charging="{ record }">
        <a-tag color="green" v-if="record.charging">启用</a-tag>
        <a-tag color="red" v-else>禁用</a-tag>
      </template>
      <template #enable="{ record }">
        <a-tag color="green" v-if="record.enable">启用</a-tag>
        <a-tag color="red" v-else>禁用</a-tag>
      </template>
      <template #limit="{ record }">
        {{ record.limit }}/{{ record.residue_limit }}
      </template>
      <template #modelTag="{ record }">
        <a-space wrap>
          <a-tag v-for="(item, index) in record.model_tag" :key="index">
            {{ item }}
          </a-tag>
        </a-space>
      </template>
      <template #optional="{ record }">
        <a-dropdown @select="handleSelect">
          <a-button>操作</a-button>
          <template #content>
            <a-doption
              :value="{ value: '编辑' }"
              @click="setModelInfo({ ...record })"
              >编辑
            </a-doption>
            <a-doption :value="{ value: '删除' }">删除</a-doption>
          </template>
        </a-dropdown>
      </template>
    </a-table>

    <!-- 弹窗 -->
    <ModelModal
      v-model:modalVisible="modalVisible"
      v-model:modelInfo="modelInfo"
      @setVisible="setVisible"
      @requestData="requestData"
    />
  </div>
</template>

<script setup lang="ts">
import ModelFrom from "@/components/backstage/pages/model/ModelFrom.vue";
import ModelModal from "@/components/backstage/pages/model/ModelModal.vue";
import { onMounted, ref } from "vue";
import { useUserStore } from "@/store";
import { useRouter } from "vue-router";
import { Api } from "@/api/api";
import { Message } from "@arco-design/web-vue";
import { get_model_table_type } from "@/types/Response/ApiTypes";

const router = useRouter();
const user_info = useUserStore().user_info;

// 表头
const columns = [
  {
    title: "创建人",
    dataIndex: "user_name",
    slotName: "user_name",
    width: 60,
    align: "center",
  },
  {
    title: "模型名",
    dataIndex: "model_name",
    ellipsis: true,
    tooltip: true,
    width: 90,
    align: "center",
  },
  {
    title: "调用名",
    dataIndex: "model_call",
    ellipsis: true,
    tooltip: true,
    width: 90,
    align: "center",
  },
  {
    title: "Base URL",
    dataIndex: "base_url",
    ellipsis: true,
    tooltip: true,
    width: 100,
    align: "center",
  },
  {
    title: "输入",
    dataIndex: "model_call_input",
    width: 50,
    align: "center",
  },
  {
    title: "输出",
    dataIndex: "model_call_output",
    width: 50,
    align: "center",
  },
  {
    title: "额度",
    slotName: "limit",
    width: 120,
    align: "center",
  },
  {
    title: "计费",
    slotName: "charging",
    width: 50,
    align: "center",
  },
  {
    title: "状态",
    slotName: "enable",
    width: 50,
    align: "center",
  },
  {
    title: "描述",
    dataIndex: "model_introduction",
    ellipsis: true,
    tooltip: true,
    width: 100,
    align: "center",
  },
  {
    title: "标签",
    slotName: "modelTag",
    align: "center",
    width: 110,
  },
  {
    title: "操作",
    slotName: "optional",
    width: 60,
    align: "center",
  },
];

// 表格数据
const tableData = ref<ModelInfo[] | []>([]);

// 表格加载
const loading = ref<boolean>(true);
// 弹窗控制
const modalVisible = ref<{
  visible: boolean | null;
  title: string | null;
}>({
  visible: false,
  title: null,
});

// 模型数据
const modelInfo = ref<ModelInfo>({
  user_name: "",
  base_url: "",
  model_name: "",
  model_call: "",
  model_introduction: "",
  model_call_input: 0,
  model_call_output: 0,
  limit: 0,
  residue_limit: 0,
  charging: null,
  enable: null,
});

// 设置表格加载
const setLoading = (setLoading: boolean): void => {
  loading.value = setLoading;
};
// 设置表格数据
const setData = (data: ModelInfo[]): void => {
  tableData.value = data;
};
// 设置弹窗显示状态
const setVisible = (setVisible: { visible: boolean; title: string }): void => {
  modalVisible.value.visible = setVisible.visible;
  modalVisible.value.title = setVisible.title;
};

// 表格按钮选项
const handleSelect = (v) => {
  if (v.value === "编辑") {
    setVisible({
      visible: true,
      title: "编辑模型",
    });
  }
};

// 点击编辑设置弹窗数据
const setModelInfo = (data: ModelInfo): void => {
  modelInfo.value.user_name = data.user_name;
  modelInfo.value.base_url = data.base_url;
  modelInfo.value.model_name = data.model_name;
  modelInfo.value.model_call = data.model_call;
  modelInfo.value.model_introduction = data.model_introduction;
  modelInfo.value.model_call_input = data.model_call_input;
  modelInfo.value.model_call_output = data.model_call_output;
  modelInfo.value.limit = data.limit;
  modelInfo.value.residue_limit = data.residue_limit;
  modelInfo.value.charging = data.charging;
  modelInfo.value.enable = data.enable;
};

// 请求数据
const requestData = async () => {
  try {
    const res = await Api.get_model_table<get_model_table_type>({
      user_id: user_info._id,
      user_name: user_info.username,
      user_role: user_info.role,
    });

    if (res.status_code === 200) {
      setData(res.data);
      Message.success(res.message);
    } else {
      Message.error(res.message);
    }
  } catch (err) {
    console.log("模型获取失败");
  } finally {
    loading.value = false;
  }
};

onMounted((): void => {
  requestData();
});
</script>

<style scoped>
#modelIndex {
}
</style>
