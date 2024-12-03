<template>
  <a-layout style="padding: 24px">
    <a-layout-content>
      <router-view name="backstage_content_view" v-slot="{ Component }">
        <transition name="fade">
          <keep-alive>
            <component :is="Component" />
          </keep-alive>
        </transition>
      </router-view>
    </a-layout-content>
  </a-layout>
</template>

<script setup lang="ts"></script>

<style scoped>
#backstageContent {
}
</style>
