from bson import ObjectId
from fastapi import status
from fastapi.responses import JSONResponse

from config.logging_config import get_logger
from database.mongo import MongoDBClient

logger = get_logger(__name__)


async def v1_delete_message(data):
    try:

        chat_client = MongoDBClient("chats")

        # 查找消息，确保消息存在且属于指定用户
        chat_find_info = chat_client.find_data(
            {
                "$and": [
                    {"_id": ObjectId(data["chat_id"])},
                    {"user_id": data["user_id"]},
                ]
            },
            {
                "message_id": True
            }
        )
        chat_client.close_connection()

        if not chat_find_info:
            logger.error(chat_find_info)
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "status_code": status.HTTP_400_BAD_REQUEST,
                    "message": "删除失败",
                })

        # 初始化MongoDB客户端并连接到"messages"集合
        message_client = MongoDBClient("messages")

        # 查找消息，确保消息存在且属于指定用户
        message_find_info = message_client.find_data(
            {
                "$and": [
                    {"_id": ObjectId(chat_find_info["message_id"])},
                    {"user_id": data["user_id"]},
                ]
            },
            {
                "messages": True
            }
        )


        # 如果未找到消息，关闭数据库连接并返回错误响应
        if not message_find_info:
            logger.error(message_find_info)
            message_client.close_connection()
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "status_code": status.HTTP_400_BAD_REQUEST,
                    "message": "删除失败",
                })

        # 定义一个过滤函数，用于处理消息数组
        def filter_array(arr):
            if arr and arr[0].get('role') == 'system':
                # 如果第一项的role为'system'，则保留第一项，删除其他项
                return [arr[0]]
            else:
                # 如果第一项的role不为'system'，则清空数组
                return []

        # 更新消息状态为已删除，并应用过滤规则
        message_del_info = message_client.update_data(
            {
                "$and": [
                    {"_id": ObjectId(chat_find_info["message_id"])},  # 使用一次ObjectId转换即可
                    {"user_id": data["user_id"]},
                    {"is_deleted": False},
                ]
            },
            {"$set": {
                "messages": filter_array(message_find_info.get('messages')),
            }}
        )

        message_client.close_connection()  # 关闭数据库连接

        # 如果更新失败，返回错误响应
        if not message_del_info:
            logger.error(message_del_info)
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "status_code": status.HTTP_400_BAD_REQUEST,
                    "message": "删除失败",
                })

        # 返回成功响应
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "status_code": status.HTTP_200_OK,
                "message": "删除成功",
            })

    except Exception as e:
        logger.error(e)  # 记录异常信息
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "message": "执行失败",
            })