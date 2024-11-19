from fastapi import status
from fastapi.responses import JSONResponse

from config.logging_config import get_logger
from database.mongo import MongoDBClient

logger = get_logger(__name__)


async def v1_create_model(data):
    try:

        # 模型查询
        model_client = MongoDBClient("models")

        # 模型查询
        model_find_info = model_client.find_data_many_sort(
            {"is_deleted": False},
            {
                "model_name": data['model_name'],
                "model_call": data['model_call']
            })

        # 如果模型已存在
        if model_find_info:
            logger.warning(f"模型已存在：{data['model_call']}")
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "status_code": status.HTTP_400_BAD_REQUEST,
                    "message": "模型已存在",
                })

        # 模型插入
        model_insert_info = model_client.insert_data_one(data)

        model_client.close_connection()

        # 插入失败
        if not model_insert_info:
            logger.warning(f"模型插入失败：{data['model_call']}")
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "status_code": status.HTTP_400_BAD_REQUEST,
                    "message": "模型插入失败",
                })

        logger.warning(f"模型插入成功：{data['model_call']}")
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "status_code": status.HTTP_200_OK,
                "message": "执行成功",
            })


    except Exception as e:
        logger.error(e)
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "message": "执行失败",
            })
