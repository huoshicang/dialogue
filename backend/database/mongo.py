import os
from datetime import datetime

from bson import ObjectId
from dotenv import load_dotenv
from pymongo import MongoClient, errors

from config.logging_config import get_logger

logger = get_logger(__name__)


class MongoDBClient:
    def __init__(self, collection_name):
        """
        初始化 MongoDB 连接
        :param collection_name: 集合名称
        """
        load_dotenv()

        username = os.getenv("MONGODB_USERNAME")
        password = os.getenv("MONGODB_PASSWORD")
        host = os.getenv("MONGODB_HOST")
        port = os.getenv("MONGODB_PORT")
        self.uri = f"mongodb://{username}:{password}@{host}:{port}/"

        # 创建MongoClient实例
        self.client = MongoClient(self.uri)

        # 连接到数据库
        self.db = self.client[os.getenv("MONGODB_DATABASE", "dialogue")]

        # 连接到集合
        self.collection = self.db[collection_name]

    def insert_data_many(self, data):
        """
        插入多个数据
        :param data: 插入的数据，必须是字典或字典列表
        :return: 插入结果
        """
        try:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            for item in data:
                item['created_at'] = current_time
                item['updated_at'] = current_time
                item['is_deleted'] = False

            result = self.collection.insert_many(data)
            return result
        except errors.PyMongoError as e:
            logger.error(f"插入数据时出错: {e}")
            return None

    def insert_data_one(self, data):
        """
        插入数据
        :param data: 插入的数据，必须是字典或字典列表
        :return: 插入结果
        """
        try:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # 添加默认值
            data['created_at'] = current_time
            data['updated_at'] = current_time
            data['is_deleted'] = False

            result = self.collection.insert_one(data)
            return {
                "_id": str(result.inserted_id)
            }
        except errors.PyMongoError as e:
            logger.error(f"插入数据时出错: {e}")
            return None

    def delete_data_many(self, query):
        """
        删除多个数据
        :param query: 查询条件，必须是字典
        :return: 删除结果
        """
        try:
            result = self.collection.delete_many(query)
            return result
        except errors.PyMongoError as e:
            logger.error(f"删除数据时出错: {e}")
            return None

    def delete_data(self, query):
        """
        删除数据
        :param query: 查询条件，必须是字典
        :return: 删除结果
        """
        try:
            result = self.collection.delete_one(query)
            return result
        except errors.PyMongoError as e:
            logger.error(f"删除数据时出错: {e}")
            return None

    def update_data(self, query, update):
        """
        更新数据
        :param query: 查询条件，必须是字典
        :param update: 更新操作，必须是字典
        :return: 更新结果
        """
        try:
            if update.get("$set"):
                update['$set']['updated_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            else:
                update['$set'] = {
                    "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }

            result = self.collection.update_one(query, update)
            return result
        except errors.PyMongoError as e:
            logger.error(f"更新数据时出错: {e}")
            return None

    def find_data_many(self, query, projection=None):
        """
        查找多个数据
        :param query: 查询条件，必须是字典
        :param projection: 查询字段，必须是字典
        :return: 查找结果
        """
        try:
            cursor = self.collection.find(query, projection)
            results = list(cursor)
            return results
        except errors.PyMongoError as e:
            logger.error(f"查找数据时出错: {e}")
            return None

    def find_data_many_sort(self, query, projection=None, sort_field=None, sort_order=-1):
        """
        查找多个数据
        :param query: 查询条件，必须是字典
        :param projection: 查询字段，必须是字典
        :param sort_field: 排序字段名
        :param sort_order: 排序顺序，1为升序，-1为降序
        :return: 查找结果
        """
        try:
            cursor = self.collection.find(query, projection)

            if sort_field is not None and sort_order is not None:
                cursor = cursor.sort(sort_field, sort_order)

            results = list(cursor)
            return results
        except errors.PyMongoError as e:
            logger.error(f"查找数据时出错: {e}")
            return None

    def find_data(self, query, projection=None):
        """
        查找数据一个
        :param query: 查询条件，必须是字典
        :param projection: 查询字段，必须是字典
        :return: 查找结果
        """
        try:

            if "_id" in query.keys():
                query['_id'] = ObjectId(query['_id'])

            result = self.collection.find_one(query, projection)
            return result
        except errors.PyMongoError as e:
            logger.error(f"查找数据时出错: {e}")
            return None

    def close_connection(self):
        """关闭 MongoDB 连接"""
        try:
            self.client.close()
        except errors.PyMongoError as e:
            logger.error(f"MongoDB 关闭失败：{e}")




# MongoDBClient("keys").insert_data_one({
#     "username": "离无歌",
#     "user_id": "",
#     "key": "sk-key",
#     "use_number": 0,
# })