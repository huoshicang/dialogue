<template>
  <div id="chatFooter">
    <a-space>
      <a-button-group type="primary">
        <a-button size="mini">copy</a-button>
        <a-button size="mini">cut</a-button>
        <a-button size="mini">find</a-button>
      </a-button-group>
    </a-space>

    <a-textarea
      placeholder="Please enter something"
      :max-length="{length:4000,errorOnly:true}"
      :auto-size="{
        minRows: 4,
        maxRows: 4,
      }"
      allow-clear
      show-word-limit
    />
  </div>
</template>

<script setup lang="ts"></script>

<style scoped>
#chatFooter {
}
</style>
