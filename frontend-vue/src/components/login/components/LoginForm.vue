<template>
  <div class="login-form-wrapper">
    <div class="login-form-title">欢迎</div>
    <div class="login-form-sub-title">欢迎登录</div>
    <div class="login-form-error-msg" />
    <a-form
      ref="loginForm"
      :model="userInfo"
      class="login-form"
      layout="vertical"
      @submit="handleSubmit as any"
    >
      <a-form-item
        field="account"
        :rules="[{ required: true, message: '请输入用户名' }]"
        :validate-trigger="['change', 'blur']"
        hide-label
      >
        <a-input v-model="userInfo.account" placeholder="请输入用户名">
          <template #prefix>
            <icon-user />
          </template>
        </a-input>
      </a-form-item>
      <a-form-item
        field="password"
        :rules="[{ required: true, message: '请输入密码' }]"
        :validate-trigger="['change', 'blur']"
        hide-label
      >
        <a-input-password
          v-model="userInfo.password"
          placeholder="请输入密码"
          allow-clear
        >
        </a-input-password>
      </a-form-item>
      <a-space :size="16" direction="vertical">
        <div class="login-form-password-actions">
          <a-checkbox
            checked="rememberPassword"
            :model-value="loginConfig.rememberPassword"
            @change="setRememberPassword"
          >
            记住密码
          </a-checkbox>
          <a-link>忘记密码</a-link>
        </div>
        <a-button type="primary" html-type="submit" long :loading="loading">
          登录
        </a-button>
      </a-space>
    </a-form>
  </div>
</template>

<script lang="ts" setup>
import { ref, reactive } from "vue";
import { Api } from "@/api/api";
import { ValidatedError } from "@arco-design/web-vue/es/form/interface";
import { useRoute, useRouter } from "vue-router";

import { Message } from "@arco-design/web-vue";
import { login_type } from "@/types/login/LogType";

const route = useRoute();
const router = useRouter();

const loading = ref<boolean>(false);

const loginConfig = {
  rememberPassword: true,
};

// 表单数据
const userInfo = reactive<login_type>({
  account: "",
  password: "",
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
  values: login_type;
}) => {
  if (loading.value) return;
  if (!errors) {
    loading.value = true;
    try {
      const res = await Api.login(values);
      if (res.status_code === 200) {
        Message.success(res.data.message);
        await router.push({ path: "/" });
      } else Message.error(res.message);
    } catch (err) {
      console.log("登录失败");
    } finally {
      loading.value = false;
    }
  }
};
const setRememberPassword = (value: boolean) => {
  console.log(loginConfig, value);
};
</script>

<style lang="less" scoped>
.login-form {
  &-wrapper {
    width: 320px;
  }

  &-title {
    color: var(--color-text-1);
    font-weight: 500;
    font-size: 24px;
    line-height: 32px;
  }

  &-sub-title {
    color: var(--color-text-3);
    font-size: 16px;
    line-height: 24px;
  }

  &-error-msg {
    height: 32px;
    color: rgb(var(--red-6));
    line-height: 32px;
  }

  &-password-actions {
    display: flex;
    justify-content: space-between;
  }

  &-register-btn {
    color: var(--color-text-3) !important;
  }
}
</style>
