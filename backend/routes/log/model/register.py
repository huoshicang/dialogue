from fastapi import status
from fastapi.responses import JSONResponse

from config.logging_config import get_logger
from database.mongo import MongoDBClient
from utils.hash_password import hash_password

logger = get_logger(__name__)


async def register_routes(data):
    try:
        # 查询用户是否存在
        find_info = MongoDBClient("users").find_data(
            {
                "$or": [
                    {"username": data["username"]},
                    {"email": data["email"]}
                ]
            },
            {'id': True}
        )

        # 用户存在
        if find_info:
            logger.error(f"{data["username"]} : {data["email"]} 用户名或邮箱已存在")
            return JSONResponse(
                status_code=status.HTTP_409_CONFLICT,
                content={
                    "status_code": status.HTTP_409_CONFLICT,
                    "message": "用户名或邮箱已存在",
                })

        # MD5加密密码
        data['password'] = hash_password(data['password'])

        # 添加默认值
        data.update({
            "phone": "",
            "avatar": "",
            "role": "user",
        })

        # 插入数据
        insert_info = MongoDBClient("users").insert_data_one(data)

        # 插入失败
        if not insert_info:
            logger.error(f"{data["username"]} : {data["email"]} 注册失败")
            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={
                    "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
                    "message": "注册失败",
                })

        # 插入成功
        logger.info(f"{insert_info.get('_id', None)} 注册成功")
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "status_code": status.HTTP_200_OK,
                "data": {
                    "_id": insert_info.get("_id", None),
                    "message": "注册成功",
                }
            })

    except Exception as e:
        logger.error(e)
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "message": "执行失败",
            })
