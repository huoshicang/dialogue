from datetime import datetime

from database.mongo import MongoDBClient
from bson.objectid import ObjectId


def updata_key_usenumber(id):
    """
    更新key的使用人数
    :param id: key的id
    :return: None
    """
    key_client = MongoDBClient("keys")

    key_client.update_data(
        {"_id": ObjectId(id)},
        {
            '$inc': {
                "use_number": 1
            },
            "$set": {
                "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
        }
    )

    key_client.close_connection()
