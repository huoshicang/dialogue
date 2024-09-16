from fastapi import APIRouter
from fastapi import Request
from config.logging_config import get_logger
from routes.r.v1.model.v1_retrieve_chat import v1_retrieve_chat
from routes.r.v1.model.v1_retrieve_message import v1_retrieve_message

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
