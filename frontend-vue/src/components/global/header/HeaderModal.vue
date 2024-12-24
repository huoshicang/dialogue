<template>
  <div id="headerModal">
    <a-modal
      width="80%"
      v-model:visible="props.visible"
      :footer="user_info.role == 'admin'"
      @cancel="emit('setVisible', false)"
    >
      <template #title>个人信息</template>
      <template #footer>
        <a-button @click="toBackstage" v-if="user_info.role == 'admin'">
          管理后台
        </a-button>
      </template>
      <div>
        <n-descriptions label-placement="top">
          <n-descriptions-item label="用户名">
            <a-tag size="large"> {{ user_info.username }}</a-tag>
          </n-descriptions-item>
          <n-descriptions-item label="邮箱">
            <a-tag size="large">{{ user_info.email }}</a-tag>
          </n-descriptions-item>
          <n-descriptions-item label="手机">
            <a-tag size="large">{{ user_info.phone ?? "无" }}</a-tag>
          </n-descriptions-item>
          <n-descriptions-item label="角色">
            <a-tag
              size="large"
              :color="user_info.role === 'user' ? '#00b42a' : '#165dff'"
            >
              {{ user_info.role === "user" ? "用户" : "管理员" }}
            </a-tag>
          </n-descriptions-item>
          <n-descriptions-item label="是否开启计费">
            <a-tag
              size="large"
              :color="user_info.charging ? '#00b42a' : '#f53f3f'"
            >
              {{ user_info.charging ? "是" : "否" }}
            </a-tag>
          </n-descriptions-item>
          <n-descriptions-item label="额度">
            <a-statistic
              :value="user_info.limit"
              :value-style="
                user_info.limit > 500 ? { color: '#0fbf60' } : { color: 'red' }
              "
            >
              <template #prefix> 剩余</template>
            </a-statistic>
          </n-descriptions-item>
          <n-descriptions-item label="创建时间">
            <a-tag size="large">{{ user_info.created_at }}</a-tag>
          </n-descriptions-item>
          <n-descriptions-item label="更新时间">
            <a-tag size="large"> {{ user_info.updated_at }}</a-tag>
          </n-descriptions-item>
        </n-descriptions>
        <a-card :bordered="false">
          <n-descriptions>
            <n-descriptions-item label="发送快捷键">
              <a-switch unchecked-color="#14C9C9" @change="handleSwitch" :v-model:model-value='submitKeyConfig'>
                <template #checked> Ctrl + Enter </template>
                <template #unchecked> Enter </template>
              </a-switch>
            </n-descriptions-item>
          </n-descriptions>
        </a-card>
      </div>
    </a-modal>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from "vue-router";
import { defineProps, defineEmits, ref } from "vue";
import { useUserStore } from "@/store";

const user_info = useUserStore().user_info;
const router = useRouter();

const props = defineProps({
  visible: {
    type: Boolean,
    required: true,
    default: false,
  },
});

const emit = defineEmits(["setVisible"]);

const handleOk = () => {
  emit("setVisible", false);
};

const submitKeyConfig = ref(localStorage.getItem("submitKeyConfig") || "ctrlEnter")

// 跳转后台
const toBackstage = () => {
  emit("setVisible", false);
  router.push("/backstage");
};

// 切换快捷键
const handleSwitch = (value: boolean | string | number, ev: Event) => {
  const submitKeyConfig = value ? "ctrlEnter" : "enter";
  localStorage.setItem("submitKeyConfig", submitKeyConfig)
};
</script>

<style scoped>
#headerModal {
}
</style>
