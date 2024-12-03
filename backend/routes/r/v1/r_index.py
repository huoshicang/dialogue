from fastapi import APIRouter
from fastapi import Request
from pydantic import BaseModel

from config.logging_config import get_logger
from routes.r.v1.model.v1_retrieve_chat import v1_retrieve_chat
from routes.r.v1.model.v1_retrieve_key import v1_retrieve_key
from routes.r.v1.model.v1_retrieve_message import v1_retrieve_message
from routes.r.v1.model.v1_retrieve_model_table import v1_retrieve_model_table
from routes.r.v1.model.v1_retrieve_models import v1_retrieve_models

r_v1_router = APIRouter(prefix="/v1/retrieve", tags=["retrieve"])

# 获取日志记录器
logger = get_logger(__name__)


@r_v1_router.get("/chat")
async def chat(request: Request):
    """获取聊天"""
    return await v1_retrieve_chat(request.query_params)


class Message(BaseModel):
    """
    模型
    """
    # 用户id
    userId: str | int

    # 用户名
    chatId: str


@r_v1_router.post("/message", response_model=Message)
async def message(Message: Message):
    """获取消息"""
    return await v1_retrieve_message({
        "userId": Message.userId,
        "chatId": Message.chatId,
    })


class Model(BaseModel):
    """
    模型
    """
    # 用户id
    user_id: str | int

    # 用户名
    user_name: str

    # 模型名称
    user_role: str


@r_v1_router.post("/model", response_model=Model)
async def model(Model: Model):
    """获取消息"""
    return await v1_retrieve_model_table({
        "user_id": Model.user_id,
        "user_name": Model.user_name,
        "user_role": Model.user_role
    })


@r_v1_router.get("/models")
async def model():
    """获取消息"""
    return await v1_retrieve_models()


class Key(BaseModel):
    """
    模型
    """
    # 用户id
    user_id: str | int

    # 用户名
    user_name: str

    # 模型名称
    user_role: str


@r_v1_router.post("/key", response_model=Key)
async def model(Key: Key):
    """获取消息"""
    return await v1_retrieve_key({
        "user_id": Key.user_id,
        "user_name": Key.user_name,
        "user_role": Key.user_role
    })
