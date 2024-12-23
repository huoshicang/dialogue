<template>
  <div id="keyIndex">
    <!-- 表单 -->
    <KeysFrom
      @setLoading="setLoading"
      @setData="setData"
      @setVisible="setVisible"
      :loading="loading"
    />

    <!-- 表格 -->
    <a-table :columns="columns" :data="tableData" :loading="loading">
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
      <template #availableModels="{ record }">
        <a-space wrap>
          <a-tag v-for="(item, index) in record.availableModels" :key="index">
            {{ item }}
          </a-tag>
        </a-space>
      </template>
      <template #optional="{ record }">
        <a-button-group type="primary" size="mini">
          <a-button @click="editKeyInfo({ ...record })"> 编辑</a-button>
          <a-button> 删除</a-button>
        </a-button-group>
      </template>
    </a-table>

    <!-- 弹窗 -->
    <keysModal
      v-model:keyVisible="keyVisible"
      v-model:keyInfo="keyInfo"
      @setVisible="setVisible"
      @requestData="requestData"
    />
  </div>
</template>

<script setup lang="ts">
import KeysFrom from "@/components/backstage/pages/keys/KeysFrom.vue";
import keysModal from "@/components/backstage/pages/keys/KeysModal.vue";
import { onMounted, ref } from "vue";
import { useUserStore } from "@/store";
import { useRouter } from "vue-router";
import { Api } from "@/api/api";
import { Message } from "@arco-design/web-vue";
import { columns } from "@/components/backstage/pages/keys/config";

const router = useRouter();
const user_info = useUserStore().user_info;

// 表格数据
const tableData = ref<KeyInfo[] | []>([]);

// 表格加载
const loading = ref<boolean>(true);
// 弹窗控制
const keyVisible = ref<{
  visible: boolean | null;
  title: string | null;
}>({
  visible: false,
  title: null,
});

// 模型数据
const keyInfo = ref<KeyInfo>({
  user_name: "",
  key: "",
  key_introduction: "",
  availableModels: [],
  limit: 0,
  residue_limit: 0,
  enable: null,
  charging: null,
});

// 设置表格加载
const setLoading = (setLoading: boolean): void => {
  loading.value = setLoading;
};
// 设置表格数据
const setData = (data: KeyInfo[]): void => {
  tableData.value = data;
};
// 设置弹窗显示状态
const setVisible = (setVisible: { visible: boolean; title: string }): void => {
  keyVisible.value.visible = setVisible.visible;
  keyVisible.value.title = setVisible.title;
};

// 表格按钮选项
const editKeyInfo = (v) => {
  setVisible({ visible: true, title: "编辑密钥" });
  keyInfo.value = v;
};

// 点击编辑设置弹窗数据
const setKeyInfo = (data: KeyInfo): void => {
  keyInfo.value.user_name = data.user_name;
  keyInfo.value.key = data.key;
  keyInfo.value.key_introduction = data.key_introduction;
  keyInfo.value.availableModels = data.availableModels;
  keyInfo.value.limit = data.limit;
  keyInfo.value.residue_limit = data.residue_limit;
  keyInfo.value.charging = data.charging;
  keyInfo.value.enable = data.enable;
};

// 请求数据
const requestData = async () => {
  try {
    const res = await Api.get_key_list({
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
    console.log("密钥失败");
  } finally {
    loading.value = false;
  }
};

onMounted((): void => {
  requestData();
});
</script>

<style scoped>
#keyIndex {
}
</style>
