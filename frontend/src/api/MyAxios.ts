import axios from "axios";
import { Buffer } from "buffer";
import router from "@/router";

// 设置全局 Buffer
globalThis.Buffer = Buffer;
globalThis.TextEncoder = globalThis.TextEncoder || require("util").TextEncoder;
globalThis.TextDecoder = globalThis.TextDecoder || require("util").TextDecoder;

const headers = {};

axios.defaults.headers.post["Content-Type"] = "application/json";
axios.defaults.headers.post["Access-Control-Allow-Origin"] = "*";
axios.defaults.baseURL = "/api";

export const my_get = (url: string, data: object): Promise<any> => {
  return axios
    .get(url, { params: data, headers })
    .then((res) => res)
    .catch((err) => err);
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
    const logValue = router.currentRoute.value.params.log;
    const fullPath = router.currentRoute.value.fullPath;
    console.log("路径参数值:", logValue);
    console.log("fullPath:", fullPath);

    return config;
  },
  (error) => {
    return Promise.reject(error);
  },
);

// 添加响应拦截器
axios.interceptors.response.use(
  (response) => {
    return response.data;
  },
  (error) => {
    return Promise.reject(error.response.data);
  },
);
