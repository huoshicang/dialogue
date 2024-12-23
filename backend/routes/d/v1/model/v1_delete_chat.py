from datetime import datetime

from bson import ObjectId
from fastapi import status
from fastapi.responses import JSONResponse

from config.logging_config import get_logger
from database.mongo import MongoDBClient

logger = get_logger(__name__)


async def update_document(collection_name, query, update_data):
    try:
        async with MongoDBClient(collection_name) as client:
            result = client.update_data(query, update_data)
            if not result:
                return False
        return True
    except Exception as e:
        logger.error(f"更新错误 {collection_name}: {e}")
        return False


async def v1_delete_chat(data):
    try:
        chat_query = {
            "$and": [
                {"_id": ObjectId(data["chat_id"])},
                {"user_id": data["user_id"]},
            ]
        }
        chat_update_data = {
            '$set': {
                "is_deleted": True,
                "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
        }

        message_query = {"_id": ObjectId(data["message_id"])}
        message_update_data = {
            '$set': {
                "is_deleted": True,
                "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
        }

        chat_deleted = await update_document("chats", chat_query, chat_update_data)
        if not chat_deleted:
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "status_code": status.HTTP_400_BAD_REQUEST,
                    "message": "删除聊天失败",
                })

        message_deleted = await update_document("messages", message_query, message_update_data)
        if not message_deleted:
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "status_code": status.HTTP_400_BAD_REQUEST,
                    "message": "删除消息失败",
                })

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "status_code": status.HTTP_200_OK,
                "message": "删除成功",
            })

    except Exception as e:
        logger.error(f"执行失败: {e}")
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "message": "执行失败",
            })
