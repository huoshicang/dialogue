from fastapi import status
from fastapi.responses import JSONResponse

from config.logging_config import get_logger
from database.mongo import MongoDBClient

logger = get_logger(__name__)


async def v1_retrieve_chat(data):
    """
    获取聊天
    :param data:
    :return:
    """
    try:
        user_id = data['user_id']

        chat_clone = MongoDBClient("chats")

        # 查找信息
        chat_find_info = chat_clone.find_data_many_sort(
            {
                "$and": [
                    {"user_id": user_id},
                    {"is_deleted": False}
                ]
            },
            {
                "_id": True,
                "chat_title": True,
                "message_id": True,
            },
            'created_at')

        chat_clone.close_connection()

        # 判断是否获取成功
        if not isinstance(chat_find_info, list):
            logger.error(f"{data["user_id"]} 获取聊天失败")
            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={
                    "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
                    "message": "获取失败",
                })

        for i in chat_find_info:
            i['_id'] = str(i['_id'])

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "status_code": status.HTTP_200_OK,
                "message": "获取成功",
                "data": chat_find_info,
                "total": len(chat_find_info)
            })

    except Exception as e:
        logger.error(e)
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "message": "执行失败",
            })
