import {reactive} from "vue"
import { defineStore } from 'pinia';
import {UserState} from "./type";

const useUserStore = defineStore('user', () => {
  const user_info = reactive<UserState>({
    name: '未登录',
    avatar: undefined,
    introduction: undefined,
    phone: undefined,
    registrationDate: undefined,
    accountId: undefined,
    certification: undefined,
    role: undefined,
  })

  return {user_info}
})

export default useUserStore
