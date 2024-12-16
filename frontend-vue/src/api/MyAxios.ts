import axios from "axios";
import { generateRandomString } from "@/tools/randomStringGenerator";
import { useUserStore } from "@/store";

const headers = {};

axios.defaults.headers.post["Content-Type"] = "application/json";
axios.defaults.headers.post["Access-Control-Allow-Origin"] = "*";
axios.defaults.baseURL = process.env.VUE_APP_API_URL ?? "";

export const my_get = async (url: string, data: object): Promise<any> => {
  try {
    return await axios.get(url, { params: data, headers });
  } catch (err) {
    return err;
  }
};

export const my_post = async (url: string, data: object): Promise<any> => {
  return await axios
    .post(url, data, { headers })
    .then((res) => res)
    .catch((err) => err);
};

//添加请求拦截器
axios.interceptors.request.use(
  (config) => {
    const user_info = useUserStore().gettersUserInfo;
    const caesarCipher = (text: number): string => {
      // 将数字转换为字符串
      const numStr = text.toString();

      // 反转字符串
      const reversedStr = numStr.split('').reverse().join('');

      // 将反转后的字符串转换回数字
      const reversedNum = parseInt(reversedStr, 10);

      // 将反转后的数字与原始数字相加
      return btoa(String(text + reversedNum))
    };

    config.headers["userId"] = user_info._id ?? "";
    config.headers["Authorization"] =
      `Bearer ${localStorage.getItem("token") ?? ""}`;
    config.headers["timestamp"] = Math.floor(Date.now() / 1000);
    config.headers["nonce"] = caesarCipher(config.headers["timestamp"]);
    return config;
  },
  (error) => {
    return Promise.reject(error);
  },
);

// 添加响应拦截器
axios.interceptors.response.use(
  (response) => {
    // 如果请求地址是/log/login，则保存响应头里的Authorization
    if (response.config.url === "/log/login") {
      localStorage.setItem("token", response.headers.authorization);
    }
    return response.data;
  },
  (error) => {
    return Promise.reject(error.response.data);
  },
);
