<template>
  <div id="contentEmpty">
    <a-card :style="{ width: '80%', backgroundColor: 'rgba(255, 255, 255, 0)' }" :bordered="false">
      <a-typography>
        <a-typography-title> Dialogue</a-typography-title>
        <a-typography-paragraph>
          看见左边了吗？选一个。 没有？那就创建一个
        </a-typography-paragraph>
      </a-typography>
    </a-card>
  </div>
</template>

<script setup lang="ts">
</script>

<style scoped>


#contentEmpty {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  background-image: im;
}
</style>
