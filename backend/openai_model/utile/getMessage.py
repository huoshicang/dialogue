from bson import ObjectId

from database.mongo import MongoDBClient
from openai_model.utile.getMessagesId import getMessagesId


def getMessage(data):
    """
    获取message
    :param data: 聊天id 用户id
    :return: messages_find_info
    """
    messages_clone = MongoDBClient("messages")
    messages_find_info = messages_clone.find_data(
        {
            "$and": [
                # 获取messageid
                {"_id": ObjectId(getMessagesId(data['chatId'], data['userId']))},
                {"is_deleted": False}
            ]
        },
        {
            "messages": True,
            "key": True,
            "model": True,
            "temperature": True,
            "top_p": True,
        })
    messages_clone.close_connection()

    return messages_find_info
