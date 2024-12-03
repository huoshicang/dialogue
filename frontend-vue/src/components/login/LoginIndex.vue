<template>
  <div class="container">
    <div class="logo">
      <!--<img-->
      <!--  alt="logo"-->
      <!--  src="//p3-armor.byteimg.com/tos-cn-i-49unhts6dw/dfdba5317c0c20ce20e64fac803d52bc.svg~tplv-49unhts6dw-image.image"-->
      <!--/>-->
      <div class="logo-text">Dialogue</div>
    </div>
    <LoginBanner />
    <div class="content">
      <div class="content-inner">
        <a-space direction="vertical">
          <component :is="Component" />
          <a-button @click="changeContent" long>{{ button }}</a-button>
        </a-space>
      </div>
      <div class="footer">footer</div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { shallowRef, ref, provide } from "vue";
import LoginBanner from "./components/BannerContent.vue";
import LoginForm from "./components/LoginForm.vue";
import RegisterForm from "./components/RegisterForm.vue";

const Component = shallowRef(LoginForm);

const button = ref("去注册");

/**
 * 切换登录 注册
 * */
const changeContent = () => {
  if (button.value === "去注册") {
    button.value = "去登录";
    Component.value = RegisterForm;
  } else {
    button.value = "去注册";
    Component.value = LoginForm;
  }
};
// 注入方法
provide("changeContent", changeContent);
</script>

<style lang="less" scoped>
.container {
  display: flex;
  height: 100vh;
  color: var(--color-text-1);

  .banner {
    width: 550px;
    background: linear-gradient(163.85deg, #1d2129 0%, #00308f 100%);
  }

  .content {
    position: relative;
    display: flex;
    flex: 1;
    align-items: center;
    justify-content: center;
    padding-bottom: 40px;
    background-color: var(--color-bg-1);
  }

  .footer {
    position: absolute;
    right: 0;
    bottom: 5px;
    width: 100%;
    text-align: center;
  }
}

.logo {
  position: fixed;
  top: 24px;
  left: 22px;
  z-index: 1;
  display: inline-flex;
  align-items: center;

  &-text {
    margin-right: 4px;
    margin-left: 4px;
    color: var(--color-fill-1);
    font-size: 20px;
  }
}
</style>
