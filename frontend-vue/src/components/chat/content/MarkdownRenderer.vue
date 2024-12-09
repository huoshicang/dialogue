<template>
  <v-md-preview :text="props.markdown['content']"/>
</template>

<script setup>

// 接收 props
const props = defineProps({
  markdown: {
    type: String,
    required: false,
    default: "",
  },
});

</script>

<style scoped>
.markdown-content .github-markdown-body {
  padding: 0 !important;
}
</style>
