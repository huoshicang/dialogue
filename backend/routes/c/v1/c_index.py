import json

from fastapi import APIRouter, WebSocket
from pydantic import BaseModel
from typing import List

from config.logging_config import get_logger
from routes.c.v1.model.v1_create_key import v1_create_key
from routes.c.v1.model.v1_create_model import v1_create_model
from routes.c.v1.model.v1_create_chat import v1_create_chat
from routes.c.v1.model.v1_create_prompts import v1_create_prompts

c_v1_router = APIRouter(prefix="/v1/create", tags=["create"])

# 获取日志记录器
logger = get_logger(__name__)


class ChatParameters(BaseModel):
    """
    聊天参数
    """
    # 用户使用model参数指明对应的模型
    model: str

    # 用户与模型的对话历史
    messages: list = []

    # 生成过程中的核采样方法概率阈值
    top_p: str | float | int | None = None

    # 用于控制模型回复的随机性和多样性
    temperature: str | int | float | None = None

    # 用户控制模型生成时整个序列中的重复度
    presence_penalty: str | int | None = None

    # 指定模型可生成的最大token个数
    max_tokens: str | int | None = None

    # 用于指定返回内容的格式
    response_foramt: dict | str = "text"

    # 生成时使用的随机数种子，用于控制模型生成内容的随机性
    seed: str | int | None = None

    # 用于控制是否使用流式输出
    stream: bool | None = False

    # stop
    stop: list[str] | str | None = None

    # 用于指定可供模型调用的工具库
    tools: list | None = None

    # 该参数用于配置在流式输出时是否展示使用的token数目
    stream_options: dict | None = None

    # 用于控制模型在生成文本时是否使用互联网搜索结果进行参考
    enable_search: bool = False


class Chat(BaseModel):
    """
    聊天
    """
    user_id: str | int
    user_name: str
    chat_title: str
    system: str | None
    chat_parameters: ChatParameters


@c_v1_router.post("/chat", response_model=Chat)
async def chat(Chat: Chat):
    """创建聊天"""
    return await v1_create_chat({
        "user_id": Chat.user_id,
        "user_name": Chat.user_name,
        "chat_title": Chat.chat_title,
        "system": Chat.system,
        "chat_parameters": {
            "model": Chat.chat_parameters.model,
            "messages": Chat.chat_parameters.messages,
            "top_p": Chat.chat_parameters.top_p,
            "temperature": Chat.chat_parameters.temperature,
            "presence_penalty": Chat.chat_parameters.presence_penalty,
            "max_tokens": Chat.chat_parameters.max_tokens,
            "response_foramt": Chat.chat_parameters.response_foramt,
            "seed": Chat.chat_parameters.seed,
            "stream": Chat.chat_parameters.stream,
            "stop": Chat.chat_parameters.stop,
            "tools": Chat.chat_parameters.tools,
            "stream_options": Chat.chat_parameters.stream_options,
            "enable_search": Chat.chat_parameters.enable_search
        }
    })


class Model(BaseModel):
    """
    模型
    """
    # 用户id
    user_id: str | int

    # 用户名
    user_name: str

    # 模型地址
    base_url: str

    # 模型名称
    Model_name: str

    # 模型调用名
    Model_call: str

    # 模型标签
    Model_tag: list[str]

    # 模型介绍
    Model_introduction: str

    # 模型调用-输入 计费
    Model_call_input: str | int | float

    # 模型调用-输出 计费
    Model_call_output: str | int | float

    # 额度
    limit: str | int

    # 剩余额度
    residue_limit: str | int


@c_v1_router.post("/model", response_model=Model)
async def model(model: Model):
    """创建模型"""
    return await v1_create_model({
        "user_id": model.user_id,
        "user_name": model.user_name,
        "base_url": model.base_url,
        "model_name": model.Model_name,
        "model_call": model.Model_call,
        "model_introduction": model.Model_introduction,
        "model_tag": model.Model_tag,
        "model_call_input": model.Model_call_input,
        "model_call_output": model.Model_call_output,
        "limit": model.limit,
        "residue_limit": model.residue_limit
    })

class Key(BaseModel):
    """
    模型
    """
    # 用户id
    user_id: str | int

    # 用户名
    user_name: str

    # 密钥
    key: str

    # 密钥说明
    key_introduction: str

    # 可用模型
    availableModels: list[str]

    # 额度
    limit: str | int

    # 剩余额度
    residue_limit: str | int

@c_v1_router.post("/key", response_model=Key)
async def model(key: Key):
    """创建模型"""
    return await v1_create_key({
        "user_id": key.user_id,
        "user_name": key.user_name,
        "key": key.key,
        "key_introduction": key.key_introduction,
        "availableModels": key.availableModels,
        "limit": key.limit,
        "residue_limit": key.residue_limit
    })

class Prompt(BaseModel):
    cmd: str
    act: str
    prompt: str

@c_v1_router.post("/prompts", response_model=List[Prompt])
async def prompts(prompt: List[Prompt]):
    """创建提示词"""
    return await v1_create_prompts(prompt)