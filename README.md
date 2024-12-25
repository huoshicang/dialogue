# Dialogue

> 声明：此项目只发布于 GitHub，基于 MIT 协议，免费且作为开源学习使用。并且不会有任何形式的卖号、付费服务、讨论群、讨论组等行为。谨防受骗。


- [Dialogue](#Dialogue)
	- [介绍](#介绍)
	- [前置要求](#前置要求)
		- [Node](#node)
	- [安装依赖](#安装依赖)
		- [后端](#后端)
		- [前端](#前端)
	- [测试环境运行](#测试环境运行)
		- [后端服务](#后端服务)
		- [前端网页](#前端网页)
	- [环境变量](#环境变量)
	- [打包](#打包)
		- [使用 Docker](#使用-docker)

		- [手动打包](#手动打包)
			- [后端服务](#后端服务-1)
			- [前端网页](#前端网页-1)

## 介绍
允许自定义任意模型，可根据模型设置baseURL和key；  
使用OpenAi库，所以符合Chat GPT格式的均可使用;  
可以控制模型、key的启用/关闭、tokens额度管理

## 前置要求

### Node

`node` 需要 `^21` 使用 [nvm](https://github.com/nvm-sh/nvm) 可管理本地多个 `node` 版本

```shell
node -v
```


## 安装依赖

### 前端
进入文件夹 `frontend-vue` 运行以下命令
根目录下运行以下命令
```shell
npm i
```

### 后端

进入文件夹 `backend` 运行以下命令

```shell
pip install -r requirements.txt
```

## 测试环境运行
### 后端服务

进入文件夹 `backend` 运行以下命令

```shell
python main.py
```

### 前端网页
进入文件夹 `frontend-vue` 运行以下命令
根目录下运行以下命令
```shell
npm run serve
```

## 环境变量
- `MONGODB_USERNAME`  mongodb的用户名
- `MONGODB_PASSWORD` mongodb的密码
- `MONGODB_HOST` mongodb的的地址
- `MONGODB_PORT` mongodb的端口
- `MONGODB_DATABASE` mongodb的集合名
- `EX` 登录过期时间


## 打包

### 使用 Docker

```env
MONGODB_USERNAME=
MONGODB_PASSWORD=
MONGODB_HOST=
MONGODB_PORT=
MONGODB_DATABASE=
EX=
```


### 手动打包
#### 后端服务
> 不需要打包，复制`backend`文件夹即可

#### 前端网页

1、修改根目录下 `.env` 文件中的 `VITE_GLOB_API_URL` 为你的实际后端接口地址

2、根目录下运行以下命令，然后将 `dist` 文件夹内的文件复制到你网站服务的根目录下

```shell
npm build
```

