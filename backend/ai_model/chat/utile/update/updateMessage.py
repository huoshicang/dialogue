from bson import ObjectId

from database.mongo import MongoDBClient
from ai_model.chat.utile.get.getMessagesId import getMessagesId


def updateMessage(data, userContentInfo, assistantContentInfo):
    messages_clone = MongoDBClient("messages")
    messages_clone.update_data(
        {
            "$and": [
                {"_id": ObjectId(getMessagesId(data['chatId'], data['userId']))},
                {"is_deleted": False}
            ]
        },
        {
            "$push": {
                "messages": {"$each": [userContentInfo, assistantContentInfo]}
            }
        }
    )
    messages_clone.close_connection()
