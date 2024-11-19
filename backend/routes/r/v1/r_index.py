from fastapi import APIRouter
from fastapi import Request
from pydantic import BaseModel

from config.logging_config import get_logger
from routes.r.v1.model.v1_retrieve_chat import v1_retrieve_chat
from routes.r.v1.model.v1_retrieve_message import v1_retrieve_message
from routes.r.v1.model.v1_retrieve_model import v1_retrieve_model

r_v1_router = APIRouter(prefix="/v1/retrieve", tags=["retrieve"])

# 获取日志记录器
logger = get_logger(__name__)

@r_v1_router.get("/chat")
async def chat(request: Request):
    """获取聊天"""
    return await v1_retrieve_chat(request.query_params)


@r_v1_router.get("/message")
async def message(request: Request):
    """获取消息"""
    return await v1_retrieve_message(request.query_params)


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
    return await v1_retrieve_model({
        "user_id": Model.user_id,
        "user_name": Model.user_name,
        "user_role": Model.user_role
    })
