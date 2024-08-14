<template>
  <a-layout-content>
    <!--<a-row class="grid-demo" style="margin-bottom: 16px;">-->
    <!--  <a-col flex="100px">-->
    <!--    <div>100px</div>-->
    <!--  </a-col>-->
    <!--  <a-col flex="auto">-->
    <!--    <div>auto</div>-->
    <!--  </a-col>-->
    <!--  <a-col flex="100px">-->
    <!--    <div>100px</div>-->
    <!--  </a-col>-->
    <!--</a-row>-->
    
  </a-layout-content>
</template>
<script setup lang="ts">

</script>
<style scoped>
.grid-demo .arco-col {
  height: 48px;
  line-height: 48px;
  color: var(--color-white);
  text-align: center;
}

.grid-demo .arco-col:nth-child(2n + 1) {
  background-color: var(--color-primary-light-4);
}

.grid-demo .arco-col:nth-child(2n) {
  background-color: rgba(var(--arcoblue-6), 0.9);
}
</style>
