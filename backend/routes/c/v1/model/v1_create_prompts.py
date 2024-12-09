from database.mongo import MongoDBClient
from fastapi import status
from fastapi.responses import JSONResponse

from config.logging_config import get_logger
from utils.hash_password import hash_password

logger = get_logger(__name__)

async def v1_create_prompts(data):
    try:


        # 将 Prompt 对象列表转换为字典
        prompts_dict = [dict(item) for item in data]


        prompt_client = MongoDBClient("prompts")
        prompt_find_info = prompt_client.insert_data_many(prompts_dict)
        prompt_client.close_connection()

        if not prompt_find_info:
            logger.error("添加提示词失败")
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={
                    "status_code": status.HTTP_401_UNAUTHORIZED,
                    "message": "添加提示词失败",
                })

        logger.info("添加提示词成功")
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "status_code": status.HTTP_200_OK,
                "message": "添加提示词成功",
            })

    except Exception as e:
        logger.error(e)
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "message": "执行失败",
            })
