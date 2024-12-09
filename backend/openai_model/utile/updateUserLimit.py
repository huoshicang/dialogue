from bson import ObjectId

from database.mongo import MongoDBClient


def updateUserLimit(data, total_tokens):
    users_clone = MongoDBClient("users")

    # 根据 userId 查找用户
    user_info = users_clone.find_data(
        {
            "$and": [
                {"_id": ObjectId(data['userId']), },
                {"is_deleted": False},
                {"enable": True},
                {"limit": {"$gte": 0}}
            ]
        },
        {"charging": True, "limit": True}
    )

    if user_info and user_info.get("charging"):
        # 如果 charging 为 True，减少 limit 字段的值
        new_limit = user_info.get("limit", 0) - total_tokens

        # 更新用户的 limit 字段
        users_clone.update_data(
            {
                "$and": [
                    {"_id": ObjectId(data['userId']), },
                    {"is_deleted": False},
                    {"enable": True},
                ]
            },
            {"$set": {"limit": int(new_limit)}}
        )

        users_clone.close_connection()

    users_clone.close_connection()
