from fastapi import APIRouter
from pydantic import BaseModel

from config.logging_config import get_logger
from routes.d.v1.model.v1_delete_chat import v1_delete_chat
from routes.d.v1.model.v1_delete_message import v1_delete_message

d_v1_router = APIRouter(prefix="/v1/delete", tags=["delete"])

# 获取日志记录器
logger = get_logger(__name__)


class Chat(BaseModel):
    """
    聊天会话
    """
    chat_id: str | int
    message_id: str | int
    user_id: str | int


@d_v1_router.post("/chat")
async def delete_chat(chat_data: Chat):
    logger.info(
        f"删除聊天会话，chat_id: {chat_data.chat_id}, message_id: {chat_data.message_id}, user_id: {chat_data.user_id}")
    return await v1_delete_chat({
        "chat_id": chat_data.chat_id,
        "message_id": chat_data.message_id,
        "user_id": chat_data.user_id
    })


class Message(BaseModel):
    """
    消息
    """
    chat_id: str | int
    user_id: str | int


@d_v1_router.post("/message")
async def delete_message(message_data: Message):
    logger.info(f"删除消息，chat_id: {message_data.chat_id}, user_id: {message_data.user_id}")
    return await v1_delete_message({
        "chat_id": message_data.chat_id,
        "user_id": message_data.user_id
    })
