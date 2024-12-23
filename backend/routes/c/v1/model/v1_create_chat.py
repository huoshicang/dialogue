from fastapi import status
from fastapi.responses import JSONResponse

from config.logging_config import get_logger
from database.mongo import MongoDBClient
from utils.hash_password import hash_password

logger = get_logger(__name__)

"""
优先构建消息
创建聊天（获取key）

"""


async def v1_create_chat(data):
    try:

        # 构建消息
        if data['system'] != "":
            data['chat_parameters']['messages'] = [
                {
                    "role": "system",
                    "content": data['system']
                }
            ]

        # 参数
        chat_parameters = data['chat_parameters']

        # 获取key
        key_client = MongoDBClient("keys")
        key_find_info = key_client.find_data_many_sort(
            {
                "is_deleted": False,
                "availableModels": {
                    "$in": [chat_parameters['model']]
                }
            },
            {"key": True},
            'residue_limit')

        key_client.close_connection()

        if not key_find_info:
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "status_code": status.HTTP_400_BAD_REQUEST,
                    "message": "没有可用的key",
                })

        # 创建消息
        message_client = MongoDBClient("messages")
        message_insert_info = message_client.insert_data_one({
            "model": chat_parameters['model'],
            "messages": chat_parameters['messages'],
            "top_p": chat_parameters['top_p'],
            "temperature": chat_parameters['temperature'],
            "presence_penalty": chat_parameters['presence_penalty'],
            "max_tokens": chat_parameters['max_tokens'],
            "response_foramt": chat_parameters['response_foramt'],
            "seed": chat_parameters['seed'],
            "stream": chat_parameters['stream'],
            "stop": chat_parameters['stop'],
            "tools": chat_parameters['tools'],
            "stream_options": chat_parameters['stream_options'],
            "enable_search": chat_parameters['enable_search'],
            "key": str(key_find_info[0]['_id']),
            "user_id": data['user_id'],
        })
        message_client.close_connection()

        # 判断消息是否创建成功
        if not message_insert_info:
            logger.error(f"{data["user_name"]} : {data['chat_title']} 消息创建失败")
            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={
                    "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
                    "message": "消息创建失败",
                })

        # 创建对话
        chat_client = MongoDBClient("chats")
        chat_insert_info = chat_client.insert_data_one({
            "user_id": data['user_id'],
            "user_name": data['user_name'],
            "chat_title": data['chat_title'],
            "system": data['system'],
            "message_id": message_insert_info.get("_id", None),
        })
        chat_client.close_connection()

        # 判断对话是否创建完成
        if not chat_insert_info:
            logger.error(f"{data["user_name"]} : {data['chat_title']} 创建对话失败")
            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={
                    "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
                    "message": "创建对话失败",
                })

        logger.info(
            f"message_id: {message_insert_info.get("_id", None)}  chat_id: {chat_insert_info.get("_id", None)}, 创建成功")
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "status_code": status.HTTP_200_OK,
                "data": {
                    "message": "创建成功",
                    "chat_data": {
                        "message_id": message_insert_info.get("_id", None),
                        "chat_id": chat_insert_info.get("_id", None),
                    }
                },
            })

    except Exception as e:
        logger.error(e)
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "message": "执行失败",
            })
