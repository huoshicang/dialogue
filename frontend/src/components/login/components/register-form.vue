<template>
  <div class="login-form-wrapper">
    <div class="login-form-title">欢迎</div>
    <div class="login-form-sub-title">欢迎注册</div>
    <div class="login-form-error-msg"/>
    
    <a-form ref="loginForm" :model="userInfo" class="login-form"
            layout="vertical" @submit="handleSubmit" :rules="rules">
      
      <a-form-item field="username" :validate-trigger="['change', 'blur']" label="用户名">
        <a-input v-model="userInfo.username" placeholder="请输入用户名" allow-clear/>
      </a-form-item>
      <a-form-item field="email" :validate-trigger="['change', 'blur']" label="邮箱">
        <a-input v-model="userInfo.email" placeholder="请输入邮箱" allow-clear/>
      </a-form-item>
      <a-form-item field="password" :validate-trigger="['change', 'blur']" label="密码">
        <a-input-password v-model="userInfo.password" placeholder="请输入密码" allow-clear/>
      </a-form-item>
      <a-form-item field="confirm_password" :validate-trigger="['change', 'blur']" label="确认密码">
        <a-input-password v-model="userInfo.confirm_password" placeholder="再次输入密码" allow-clear/>
      </a-form-item>
      
      <a-space :size="16" direction="vertical">
        <a-button type="primary" html-type="submit" long :loading="loading">
          注册
        </a-button>
      </a-space>
    
    </a-form>
  </div>
</template>

<script lang="ts" setup>
import {ref, reactive, inject} from 'vue';
import {ValidatedError} from '@arco-design/web-vue/es/form/interface';
import {Message} from '@arco-design/web-vue';
import {register_type} from "../../../types/login";
import {Api} from "../../../api/api";
import * as async_hooks from "async_hooks";

const changeContent = inject('changeContent')

const loading = ref<boolean>(false); // 登录按钮loading状态

// 表单数据
const userInfo = reactive<register_type>({
  username: "",
  email: "",
  password: "",
  confirm_password: "",
});

// 表单验证规则
const rules = {
  username: [
    {
      required: true,
      message: '请输入用户名',
    },
  ],
  password: [
    {
      required: true,
      message: '请输入密码',
    },
  ],
  confirm_password: [
    {
      required: true,
      message: '再次输入密码',
    },
    {
      validator: (value: string, cb: any) => {
        if (value !== userInfo.password) {
          cb('两次输入的密码不一致')
        } else {
          cb()
        }
      }
    }
  ],
  email: [
    {
      type: 'email',
      required: true,
      message: '请输入邮箱',
    },
  ],
}

// 提交表单
const handleSubmit = async ({errors, values}: {
  errors: Record<string, ValidatedError> | undefined;
  values: register_type;
}) => {
  // 登录按钮loading状态
  if (loading.value) return;
  
  // 表单验证
  if (!errors) {
    loading.value = true;
    try {
      
      const res = await Api.register(values)
      
      if (res.status_code === 200) {
        Message.success(res.message)
        changeContent()
      } else {
        Message.error(res.message)
      }
      
    } catch (err) {
      Message.warning(err)
    } finally {
      loading.value = false;
    }
  }
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
