
from bson import ObjectId
from fastapi import status
from fastapi.responses import JSONResponse

from config.logging_config import get_logger
from database.mongo import MongoDBClient

logger = get_logger(__name__)

def handle_error(message, status_code=status.HTTP_400_BAD_REQUEST):
    logger.error(message)
    return JSONResponse(
        status_code=status_code,
        content={
            "status_code": status_code,
            "message": message,
        }
    )

async def find_message(client, collection_name, query, projection):
    result = client.find_data(query, projection)
    if not result:
        return None
    return result

async def v1_delete_message(data):
    try:
        async with MongoDBClient("chats") as chat_client:
            chat_query = {
                "$and": [
                    {"_id": ObjectId(data["chat_id"])},
                    {"user_id": data["user_id"]},
                ]
            }
            chat_projection = {
                "message_id": True
            }
            chat_find_info = await find_message(chat_client, "chats", chat_query, chat_projection)

            if not chat_find_info:
                return handle_error("删除失败：聊天记录未找到")

        async with MongoDBClient("messages") as message_client:
            message_query = {
                "$and": [
                    {"_id": ObjectId(chat_find_info["message_id"])},
                    {"user_id": data["user_id"]},
                ]
            }
            message_projection = {
                "messages": True
            }
            message_find_info = await find_message(message_client, "messages", message_query, message_projection)

            if not message_find_info:
                return handle_error("删除失败：消息记录未找到")

            # 定义一个过滤函数，用于处理消息数组
            def filter_array(arr):
                if arr and arr[0].get('role') == 'system':
                    # 如果第一项的role为'system'，则保留第一项，删除其他项
                    return [arr[0]]
                else:
                    # 如果第一项的role不为'system'，则清空数组
                    return []

            # 更新消息状态为已删除，并应用过滤规则
            update_query = {
                "$and": [
                    {"_id": ObjectId(chat_find_info["message_id"])},
                    {"user_id": data["user_id"]},
                    {"is_deleted": False},
                ]
            }
            update_data = {
                "$set": {
                    "messages": filter_array(message_find_info.get('messages')),
                    "is_deleted": True,
                }
            }
            message_del_info = message_client.update_data(update_query, update_data)

            if not message_del_info:
                return handle_error("删除失败：更新消息失败")

        # 返回成功响应
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "status_code": status.HTTP_200_OK,
                "message": "删除成功",
            })

    except Exception as e:
        logger.error(f"执行失败: {e}")  # 记录异常信息
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "message": "执行失败",
            })