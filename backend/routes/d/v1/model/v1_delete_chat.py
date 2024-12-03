from datetime import datetime

from bson import ObjectId
from fastapi import status
from fastapi.responses import JSONResponse

from config.logging_config import get_logger
from database.mongo import MongoDBClient
from utils.hash_password import hash_password

logger = get_logger(__name__)


async def v1_delete_chat(data):
    try:
        chat_clinet = MongoDBClient("chats")
        chat_del_info = chat_clinet.update_data(
            {
                "$and": [
                    {"_id": ObjectId(data["chat_id"])},
                    {"user_id": data["user_id"]},
                ]
            },
            {
                '$set': {
                    "is_deleted": True,
                    "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
            }
        )
        chat_clinet.close_connection()

        message_clinet = MongoDBClient("messages")
        message_clinet.update_data(
            {"_id": ObjectId(data["message_id"])},
            {
                '$set': {
                    "is_deleted": True,
                    "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
            }
        )
        message_clinet.close_connection()

        if not chat_del_info:
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "status_code": status.HTTP_400_BAD_REQUEST,
                    "message": "删除失败",
                })

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "status_code": status.HTTP_200_OK,
                "message": "删除成功",
            })

    except Exception as e:
        logger.error(e)
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "message": "执行失败",
            })
