from bson import ObjectId

from database.mongo import MongoDBClient


def getUserInfo(userId):
    """
    查询用户信息
    :param userId: 用户ID
    :return: 用户是否有额度的信息
    """
    users_clone = MongoDBClient("users")
    users_find_info = users_clone.find_data(
        {
            "$and": [
                {"_id": ObjectId(userId)},
                {"is_deleted": False},
                {"limit": {"$gte": 0}}
            ],
        },{
            "limit": True,
            "charging": True
        })
    users_clone.close_connection()
    return users_find_info
