from bson import ObjectId
from database.mongo import MongoDBClient


def updateKeyLimit(key, userId, total_tokens):
    keys_clone = MongoDBClient("keys")

    # 根据 userId 和 keyId 查找 key
    key_info = keys_clone.find_data(
        {
            "key": key,
            "user_id": userId,
        },
        {
            "charging": True,
            "residue_limit": True
        }
    )

    if key_info and key_info.get("charging"):
        # 如果 charging 为 True，减少 limit 字段的值
        new_limit = key_info.get("limit", 0) - total_tokens

        # 更新 key 的 limit 字段
        keys_clone.update_data(
            {
                "key": key,
                "user_id": userId
            },
            {"$set": {"residue_limit": new_limit}}
        )

    keys_clone.close_connection()