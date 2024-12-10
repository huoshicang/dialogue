from bson import ObjectId

from database.mongo import MongoDBClient


def getKey(key, model, tokens):
    """
    获取key
    :param tokens: 额度
    :param key: keyID
    :param model: 模型
    :return: {
            "key": sk-xxx,
            "charging": True,
        }
    """
    keys_clone = MongoDBClient("keys")
    keys_find_info = keys_clone.find_data(
        {
            "$and": [
                {"_id": ObjectId(key)},
                {"is_deleted": False},
                {"enable": True},
                {"residue_limit": {"$gte": tokens}}
            ],
            "availableModels": {
                "$in": [model]
            }
        },
        {
            "key": True,
            "charging": True,
        })
    keys_clone.close_connection()
    return keys_find_info
