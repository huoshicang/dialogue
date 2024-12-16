<template>
  <div
    ref="messageRef"
    class="flex w-full mb-6 overflow-hidden"
    :class="[{ 'flex-row-reverse': rendering }]"
  >
    <div
      class="overflow-hidden text-sm"
      :class="[rendering ? 'items-end' : 'items-start']"
    >
      <div
        class="flex items-end gap-1 mt-2"
        :class="[rendering ? 'flex-row-reverse' : 'flex-row']"
      >
        <TextComponent
          ref="textRef"
          :inversion="rendering"
          :error="false"
          :text="text"
          :as-raw-text="asRawText"
        />
      </div>
    </div>
  </div>
</template>
<script setup lang="ts">
import { onMounted, ref } from "vue";
import { useMessage } from "naive-ui";
import TextComponent from "./Text.vue";

interface Props {
  text?: string;
}

const rendering = ref(false);

const props = defineProps<Props>();

const message = useMessage();

const textRef = ref<HTMLElement>();

const asRawText = ref(rendering);

const messageRef = ref<HTMLElement>();

onMounted(() => {
  if (rendering) {
    asRawText.value = localStorage.getItem("rendering") === "true";
  }
});
</script>
