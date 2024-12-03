<template>
  <div id="noAuthIndex">
    <a-result status="warning" title="无权限">
      <template #subtitle> 您无权访问该页面，请返回。</template>

      <template #extra>
        <a-space>
          <a-button type="primary" status="warning" @click="back">
            返回
          </a-button>
        </a-space>
      </template>
    </a-result>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from "vue-router";

const router = useRouter();

const back = () => router.push("/");
</script>

<style scoped>
#noAuthIndex {
}
</style>
