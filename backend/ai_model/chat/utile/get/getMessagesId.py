from bson import ObjectId

from database.mongo import MongoDBClient


def getMessagesId(chatId, userId):
    """
    获取messageid
    :param chatId: 聊天id
    :param userId: 用户id
    :return: message_id
    """
    chat_clone = MongoDBClient("chats")
    chat_find_info = chat_clone.find_data(
        {
            "$and": [
                {"_id": ObjectId(chatId)},
                {"user_id": userId},
                {"is_deleted": False}
            ]
        },
        {
            "_id": False,
            "message_id": True,
        })
    chat_clone.close_connection()

    return str(chat_find_info['message_id'])
