from bson import ObjectId
from database.mongo import MongoDBClient


def updateModelLimit(userId, model, newLimit):
    """
    更新模型的额度
    :param userId: 用户ID
    :param model: 模型名称
    :param newLimit: 新的额度
    :return: None
    """
    models_clone = MongoDBClient("models")
    # 更新 model 的 limit 字段
    models_clone.update_data(
        {
            "$and": [
                {"user_id": userId, },
                {"is_deleted": False},
                {"enable": True},
                {"model_call": model, }
            ]
        },
        {"$set": {"residue_limit": newLimit}}
    )

    models_clone.close_connection()
