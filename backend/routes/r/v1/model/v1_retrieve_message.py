from bson import ObjectId
from fastapi import status
from fastapi.responses import JSONResponse

from config.logging_config import get_logger
from database.mongo import MongoDBClient

logger = get_logger(__name__)


async def v1_retrieve_message(data):
    """
    获取聊天
    :param data:
    :return:
    """
    try:
        # 根据userid和chatid获取messageid
        chat_clone = MongoDBClient("chats")
        chat_find_info = chat_clone.find_data(
            {
                "$and": [
                    {"_id": ObjectId(data['chatId'])},
                    {"user_id": data['userId']},
                    {"is_deleted": False}
                ]
            },
            {
                "_id": False,
                "message_id": True,
            })
        chat_clone.close_connection()

        if not chat_find_info:
            logger.error(f"{data['chatId']} 获取信息失败")
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={
                    "status_code": status.HTTP_404_NOT_FOUND,
                    "message": "未找到信息",
                })

        messages_clone = MongoDBClient("messages")

        # 查找信息
        messages_find_info = messages_clone.find_data(
            {
                "$and": [
                    {"_id": ObjectId(chat_find_info['message_id'])},
                    {"is_deleted": False}
                ]
            },
            {
                # "created_at": False,
                # "updated_at": False,
                # "is_deleted": False,
                "messages": True,
            })
        messages_clone.close_connection()

        if not messages_find_info:
            logger.error(f"{chat_find_info['message_id']} 获取消息失败")
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={
                    "status_code": status.HTTP_404_NOT_FOUND,
                    "message": "未找到信息",
                })

        messages_find_info['_id'] = str(messages_find_info['_id'])

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "status_code": status.HTTP_200_OK,
                "message": "执行成功",
                "data": messages_find_info
            })

    except Exception as e:
        logger.error(e)
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "message": "执行失败",
            })
