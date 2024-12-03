<template>
  <div id="headerModal">
    <a-modal
      width="auto"
      v-model:visible="props.visible"
      :footer="user_info.role == 'admin'"
      @cancel="emit('setVisible', false);">
      <template #title> Title</template>
      <template #footer>
          <a-button @click="toBackstage"  v-if="user_info.role == 'admin'">
            管理后台
          </a-button>
      </template>
      <div>
        You can customize modal body text by the current situation. This modal
        will be closed immediately once you press the OK button.
      </div>
    </a-modal>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from "vue-router";
import { defineProps, defineEmits } from "vue";
import { useUserStore } from "@/store";
const user_info = useUserStore().user_info;
const router = useRouter();

const props = defineProps({
  visible: {
    type: Boolean,
    required: true,
    default: false,
  },
});

const emit = defineEmits(["setVisible"]);

const handleOk = () => {
  emit("setVisible", false);
};

const toBackstage = () => {
  emit("setVisible", false);
  router.push("/backstage");
};
</script>

<style scoped>
#headerModal {
}
</style>
