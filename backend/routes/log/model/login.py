import time

from starlette import status
from fastapi import Request
from starlette.responses import JSONResponse
from config.logging_config import get_logger
from database.mongo import MongoDBClient
from database.redis_client import RedisClient
from utils.hash_password import hash_password
import uuid
import jwt

logger = get_logger(__name__)


async def login_routes(data, request: Request):
    headers = dict(request.headers)  # 获取请求头

    try:
        find_info = MongoDBClient("users").find_data(
            {
                "$or": [
                    {"username": data["account"]},
                    {"email": data["account"]}
                ],
                "$and": [
                    {"password": hash_password(data['password'])},
                    {"is_deleted": False}
                ]
            },
            {
                'is_deleted': False,
                'password': False,
                'updated_at': False,
            })

        # 用户信息不存在
        if not find_info:
            return JSONResponse(
                status_code=status.HTTP_409_CONFLICT,
                content={
                    "status_code": status.HTTP_409_CONFLICT,
                    "message": "用户名不存在 或密码错误",
                })

        find_info['_id'] = str(find_info['_id'])

        UUID = str(uuid.uuid4())

        client = RedisClient().set_key_value(UUID, find_info, ex=36000)

        # 存储登录信息
        if not client:
            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={
                    "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
                    "message": "登录失败",
                })

        logger.info(f"{data["account"]} 登录成功")

        # 生成加密盐
        time_stamp = str(int(time.time()))

        # 生成token
        token = jwt.encode({
            "UUID": UUID
        }, time_stamp, algorithm='HS256')

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "status_code": status.HTTP_200_OK,
                "data": {
                    "message": "登录成功",
                    "user_data": find_info,
                },
            },
            headers={
                "Authorization": f"Bearer {token}",
                "X-Timestamp": time_stamp,
            },
        )

    except Exception as e:
        logger.error(e)
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "message": "执行失败",
            }
        )
