from fastapi import status
from fastapi.responses import JSONResponse

from config.logging_config import get_logger
from database.mongo import MongoDBClient

logger = get_logger(__name__)


async def v1_create_key(data):
    try:

        # 模型查询
        key_client = MongoDBClient("keys")

        data['enable'] = True
        data['charging'] = True
        # 模型插入
        key_insert_info = key_client.insert_data_one(data)

        key_client.close_connection()

        # 插入失败
        if not key_insert_info:
            logger.warning(f"密钥插入失败")
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "status_code": status.HTTP_400_BAD_REQUEST,
                    "message": "密钥创建失败",
                })

        logger.info(f"密钥创建成功")
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "status_code": status.HTTP_200_OK,
                "message": "创建成功",
            })



    except Exception as e:
        logger.error(e)
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "message": "执行失败",
            })
