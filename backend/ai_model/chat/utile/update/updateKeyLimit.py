from bson import ObjectId
from database.mongo import MongoDBClient


def updateKeyLimit(key, userId, newLimit):
    """
    更新 key 的剩余额度
    :param key: key
    :param userId: 用户ID
    :param newLimit: 新的额度
    :return: None
    """
    keys_clone = MongoDBClient("keys")

    # 更新 key 的 limit 字段
    keys_clone.update_data(
        {
            "$and": [
                {"key": key, },
                {"user_id": userId, },
                {"enable": True, },
            ]
        },
        {"$set": {"residue_limit": newLimit}}
    )

    keys_clone.close_connection()
