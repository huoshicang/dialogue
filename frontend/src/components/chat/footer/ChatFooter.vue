<template>
  <div id="chatFooter">
    <a-space>
      <a-button-group type="primary">
        <a-button size="mini">copy</a-button>
        <a-button size="mini">cut</a-button>
        <a-button size="mini">find</a-button>
      </a-button-group>
    </a-space>

    <!--    <a-textarea-->
    <!--      placeholder="Please enter something"-->
    <!--      :max-length="{length:4000,errorOnly:true}"-->
    <!--      :auto-size="{-->
    <!--        minRows: 4,-->
    <!--        maxRows: 4,-->
    <!--      }"-->
    <!--      allow-clear-->
    <!--      show-word-limit-->
    <!--    />-->

    <n-input-group style="align-items: flex-end;">
      <n-input
        :maxlength="4000"
        :autosize="{
          minRows: 4,
          maxRows: 4,
        }"
        allow-clear
        show-count
        type="textarea"
        placeholder="基本的 Textarea"
      />
      <n-button-group vertical>
        <n-button> 幸福 </n-button>
        <n-button> 刚好 </n-button>
      </n-button-group>
    </n-input-group>

    <span class="information">版权</span>
  </div>
</template>

<script setup lang="ts"></script>

<style scoped>
#chatFooter .information {
  padding: 5px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  color: var(--color-text-4);
  font-stretch: condensed;
  text-align: center;
}
</style>
