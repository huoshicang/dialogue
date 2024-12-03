import axios from "axios";
import { Buffer } from "buffer";
import { generateRandomString } from "@/tools/randomStringGenerator";

// 设置全局 Buffer
globalThis.Buffer = Buffer;
globalThis.TextEncoder = globalThis.TextEncoder || require("util").TextEncoder;
globalThis.TextDecoder = globalThis.TextDecoder || require("util").TextDecoder;

const headers = {};

axios.defaults.headers.post["Content-Type"] = "application/json";
axios.defaults.headers.post["Access-Control-Allow-Origin"] = "*";
// axios.defaults.baseURL = "/api";
axios.defaults.baseURL = process.env.VUE_APP_API_URL ?? "";
//
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
    //const logValue = router.currentRoute.value.params.log;
    //const fullPath = router.currentRoute.value.fullPath;
    //console.log("路径参数值:", logValue);
    //console.log("fullPath:", fullPath);

    if (localStorage.getItem("login_id") === null) {
      localStorage.setItem("login_id", generateRandomString());
    }

    // 添加请求头
    config.headers.set("login_id", localStorage.getItem("login_id") ?? "");
    config.headers.set(
      "Authorization",
      `Bearer ${localStorage.getItem("token") ?? ""}`,
    );

    return config;
  },
  (error) => {
    return Promise.reject(error);
  },
);

// 添加响应拦截器
axios.interceptors.response.use(
  (response) => {
    if (response.headers["x-requested-url"] === "log/login") {
      const token = response.headers["authorization"].replace("Bearer ", "");

      // 判断是否是同一用户
      if (response.headers["login_id"] !== localStorage.getItem("login_id")) {
        localStorage.setItem("login_id", response.headers["login_id"]);
      }

      // 存储
      localStorage.setItem("token", token);
    }

    return response.data;
  },
  (error) => {
    return Promise.reject(error.response.data);
  },
);
