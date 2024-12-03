from bson import ObjectId
from database.mongo import MongoDBClient


def updateModelLimit(userId, model, total_tokens):
    models_clone = MongoDBClient("models")

    # 根据 userId 和 model 查找 model
    model_info = models_clone.find_data(
        {
            "user_id": userId,
            "name": model
        },
        {
            "charging": True,
            "limit": True
        }
    )

    if model_info and model_info.get("charging"):
        # 如果 charging 为 True，减少 limit 字段的值
        new_limit = model_info.get("limit", 0) - total_tokens

        # 更新 model 的 limit 字段
        update_result = models_clone.update_data(
            {
                "user_id": userId,
                "name": model
            },
            {"$set": {"limit": new_limit}}
        )
    models_clone.close_connection()
