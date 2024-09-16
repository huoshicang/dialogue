from fastapi import APIRouter
from pydantic import BaseModel

from config.logging_config import get_logger
from fastapi import Request
from routes.d.v1.model.v1_delete_chat import v1_delete_chat

d_v1_router = APIRouter(prefix="/v1/delete", tags=["delete"])

# 获取日志记录器
logger = get_logger(__name__)


class Chat(BaseModel):
    """
    聊天
    """
    chat_id: str | int
    message_id: str | int
    user_id: str | int

@d_v1_router.post("/chat")
async def chat(Chat: Chat):
    return await v1_delete_chat({
        "chat_id": Chat.chat_id,
        "message_id": Chat.message_id,
        "user_id": Chat.user_id
    })