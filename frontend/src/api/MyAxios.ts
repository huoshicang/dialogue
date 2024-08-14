import axios from "axios";

const headers = <{
  "X-Timestamp": string;
}>{
  "X-Timestamp": Math.round(new Date().getTime() / 1000).toString(),
};

axios.defaults.headers.post['Content-Type'] = 'application/json';
axios.defaults.headers.post['Access-Control-Allow-Origin'] = '*';
axios.defaults.baseURL = "/api"

export const my_get = (url: string, data: unknown) => {
  return axios
    .get(url, {params: data, headers})
    .then((res) => res)
    .catch((err) => err);
}

export const my_post = (url: string, data: unknown) => {
  return axios.post(url, data, {headers})
    .then((res) => res)
    .catch((err) => err)
}


// 添加响应拦截器
axios.interceptors.response.use(function (response) {
  // 2xx 范围内的状态码都会触发该函数。
  // 对响应数据做点什么

  console.log(response.headers)
  console.log(response.headers['authorization'])
  console.log(response.headers['x-timestamp'])
// todo 用时间戳 解密token 保存 uuid
  return response.data;
}, function (error) {
  // 超出 2xx 范围的状态码都会触发该函数。
  // 对响应错误做点什么
  return Promise.reject(error.response.data);
});
