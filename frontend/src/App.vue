<template>
  <a-config-provider :locale="zhCN">
    <router-view name="app_view" v-slot="{ Component }">
      <transition name="fade">
        <keep-alive>
          <component :is="Component" />
        </keep-alive>
      </transition>
    </router-view>
  </a-config-provider>
</template>

<script setup>
import zhCN from "@arco-design/web-vue/es/locale/lang/zh-cn";
import { useRouter } from "vue-router";
import { onMounted } from "vue";

const router = useRouter();

onMounted(() => router.push({ path: "/chat" }));
</script>
