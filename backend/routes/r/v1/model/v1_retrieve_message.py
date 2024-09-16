from bson import ObjectId
from fastapi import status
from fastapi.responses import JSONResponse

from config.logging_config import get_logger
from database.mongo import MongoDBClient
from utils.hash_password import hash_password

logger = get_logger(__name__)


async def v1_retrieve_message(data):
    """
    获取聊天
    :param data:
    :return:
    """
    try:
        message_id = data['message_id']

        # 查找信息
        chat_find_info = MongoDBClient("messages").find_data(
            {
                "$and": [
                    {"_id": ObjectId(message_id)},
                    {"is_deleted": False}
                ]
            },
            {
                "created_at": False,
                "updated_at": False,
                "is_deleted": False,
            })

        if not chat_find_info:
            logger.error(f"{data['message_id']} 获取消息失败")
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={
                    "status_code": status.HTTP_404_NOT_FOUND,
                    "message": "未找到信息",
                })

        chat_find_info['_id'] = str(chat_find_info['_id'])

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "status_code": status.HTTP_200_OK,
                "message": "执行成功",
                "data": chat_find_info
            })

    except Exception as e:
        logger.error(e)
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "message": "执行失败",
            })
