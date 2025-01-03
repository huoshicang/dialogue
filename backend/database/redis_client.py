import json
import os

import redis
from dotenv import load_dotenv
from redis.exceptions import ConnectionError
from config.logging_config import get_logger

logger = get_logger(__name__)


class RedisClient:
    def __init__(self, db=0):
        """
        初始化 Redis 连接
        :param db: 数据库编号，默认为0
        """
        load_dotenv()

        host = os.getenv("REDIS_HOST")
        password = os.getenv("REDIS_PASSWORD")
        port = os.getenv("REDIS_PORT")
        db = db

        try:
            self.r = redis.Redis(host=host, port=port, db=db, password=password)
            # 测试连接是否成功
            self.r.ping()
        except ConnectionError as e:
            logger.error(f"无法连接到Redis: {e}")
            self.r = None

    def set_key_value(self, key, value, ex=None):
        """
        设置键值对
        :param key: 键
        :param value: 值
        :param ex: 过期时间（秒）
        :return: 操作是否成功
        """
        try:
            if isinstance(value, dict):
                value = json.dumps(value)

            return self.r.set(key, value, ex=ex)
        except Exception as e:
            logger.error(f"设置键值对时出错: {e}")
            return None

    def get_value(self, key):
        """
        获取键对应的值
        :param key: 键
        :return: 值
        """
        try:
            value = self.r.get(key)
            try:
                return json.loads(value)
            except:
                return value
        except Exception as e:
            logger.error(f"获取值时出错: {e}")
            return None

    def delete_key(self, key):
        """
        删除键
        :param key: 键
        :return: 删除是否成功
        """
        try:
            return self.r.delete(key)
        except Exception as e:
            logger.error(f"删除键时出错: {e}")
            return None


    def exists_key(self, key):
        """
        检查键是否存在
        :param key: 键
        :return: 是否存在
        """
        try:
            return self.r.exists(key)
        except Exception as e:
            logger.error(f"检查键是否存在时出错: {e}")
            return None

    def rename_key(self, old_key, new_key):
        """
        重命名键
        :param old_key: 旧键名
        :param new_key: 新键名
        :return: 操作是否成功
        """
        try:
            return self.r.rename(old_key, new_key)
        except Exception as e:
            logger.error(f"重命名键时出错: {e}")
            return False

    def close_connection(self):
        """
        关闭 Redis 连接
        """
        try:
            self.r.connection_pool.disconnect()
            logger.info("Redis 连接已关闭")
        except Exception as e:
            logger.error(f"Redis 关闭失败：{e}")

# 示例使用
# if __name__ == "__main__":
#     client = RedisClient()
#
#     # 设置键值对
#     key = "example_key"
#     value = "example_value"
#     result = client.set_key_value(key, value, ex=3600)
#     if result:
#         print(f"设置键'{key}'与值'{value}'成功.")
#     else:
#         print(f"设置键'{key}'与值'{value}'失败.")
#
#     # # 获取值
#     # retrieved_value = client.get_value(key)
#     # if retrieved_value is not None:
#     #     print(f"获取键'{key}'的值为: {retrieved_value.decode('utf-8')}")
#     # else:
#     #     print(f"获取键'{key}'的值失败.")
#     #
#     # # 删除键
#     # deleted = client.delete_key(key)
#     # if deleted:
#     #     print(f"删除键'{key}'成功.")
#     # else:
#     #     print(f"删除键'{key}'失败.")
#
#     # 关闭连接
#     client.close_connection()
