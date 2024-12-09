from database.mongo import MongoDBClient


def getBaseUrl(model):
    """
    获取baseUrl
    :param model: 模型名
    :return: {
            "base_url": https://xxx.xx,
            "charging": True,
        }
    """
    model_clone = MongoDBClient("models")
    model_find_info = model_clone.find_data(
        {
            "$and": [
                {"model_call": model},
                {"is_deleted": False},
                {"enable": True},
                {"residue_limit": {"$gte": 0}}
            ]
        },
        {
            "base_url": True,
            "charging": True,
        })
    model_clone.close_connection()
    return model_find_info
