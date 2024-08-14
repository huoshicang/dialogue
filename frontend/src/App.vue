<template>
  <a-config-provider :locale="zhCN">
    <router-view name="app_view" v-slot="{ Component }">
      <transition name="fade">
        <keep-alive>
          <component :is="Component"/>
        </keep-alive>
      </transition>
    </router-view>
  </a-config-provider>
</template>

<script setup>
import zhCN from '@arco-design/web-vue/es/locale/lang/zh-cn';
import {useUserStore} from "./store/index"
import { useRouter, useRoute } from 'vue-router'

const router = useRouter()
const route = useRoute()

const {name} = useUserStore().user_info

// onMounted(() => {
//
//   console.login(route.path)
//
//   if (!name) {
//     router.push({
//       path: '/login'
//     })
//   }
// })

</script>
