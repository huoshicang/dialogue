from bson import ObjectId

from database.mongo import MongoDBClient


def getUserInfo(userId, tokens):
    """
    查询用户信息
    :param tokens: 额度
    :param userId: 用户ID
    :return: 用户是否有额度的信息
    """
    users_clone = MongoDBClient("users")
    users_find_info = users_clone.find_data(
        {
            "$and": [
                {"_id": ObjectId(userId)},
                {"is_deleted": False},
                {"limit": {"$gte": tokens}}
            ],
        },{
            "limit": True,
            "charging": True
        })
    users_clone.close_connection()
    return users_find_info
