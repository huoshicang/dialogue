from bson import ObjectId

from database.mongo import MongoDBClient


def updateUserLimit(userId, newLimit):
    """
    更新用户额度
    :param userId: 用户ID
    :param newLimit: 新的额度
    :return: None
    """

    users_clone = MongoDBClient("users")

    # 更新用户的 limit 字段
    users_clone.update_data(
        {
            "$and": [
                {"_id": ObjectId(userId), },
                {"is_deleted": False},
            ]
        },
        {"$set": {"limit": int(newLimit)}}
    )


    users_clone.close_connection()
