import os
import secrets
from dotenv import load_dotenv
from starlette import status
from starlette.responses import JSONResponse
from config.logging_config import get_logger
from database.mongo import MongoDBClient
from database.redis_client import RedisClient
from utils.hash_password import hash_password

from utils.randomStringGenerator import generate_random_string
from utils.token import sign

logger = get_logger(__name__)


async def login_routes(data, request):

    try:
        load_dotenv()

        # 查询用户信息
        users_client = MongoDBClient("users")

        find_info = users_client.find_data(
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
                'confirm_password': False,
            })
        users_client.close_connection()

        # 用户信息不存在
        if not find_info:
            logger.error(f"{data["account"]} 用户名不存在 或密码错误")
            return JSONResponse(
                status_code=status.HTTP_409_CONFLICT,
                content={
                    "message": "用户名不存在 或密码错误",
                    "status_code": status.HTTP_409_CONFLICT,
                })

        # 获取用户id
        find_info['_id'] = str(find_info['_id'])

        # 创建信息键
        session_id = secrets.token_hex(32).upper()

        logger.info(f"{data["account"]} 登录成功")

        # 返回数据
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
                "Authorization": sign({
                    "sub": find_info['_id'],
                    "name": find_info['username'],
                    "jti": session_id[::2]
                }, session_id, int(os.getenv("EX", 604800))),
                "x-requested-url": "login",
                "Set-Cookie": f"sessionId={session_id}; Path=/; HttpOnly; Secure; SameSite=Lax; Max-Age={int(os.getenv("EX", 604800))}"
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
