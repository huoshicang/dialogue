from fastapi import status
from fastapi.responses import JSONResponse
from bson import ObjectId
from config.logging_config import get_logger
from database.mongo import MongoDBClient

logger = get_logger(__name__)


async def v1_retrieve_model(data):
    """
    获取聊天
    :param data:
    :return:
    """
    try:
        user_cline = MongoDBClient("users")

        user_find_info = user_cline.find_data(
            {
                "$and": [
                    {"_id": ObjectId(data['user_id'])},
                ]
            },
            {
                "role": True,
                "username": True,
            }
        )
        user_cline.close_connection()

        if not user_find_info or user_find_info['role'] != "admin":
            logger.warning(f"用户权限不足：{data['username']}")
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={
                    "status_code": status.HTTP_404_NOT_FOUND,
                    "message": "用户权限不足",
                })

        model_cline = MongoDBClient("models")
        model_find_info = model_cline.find_data_many_sort(
            {"is_deleted": False},
            {
                "created_at": False,
                "is_deleted": False,
                "updated_at": False,
                "user_id": False,
            })
        model_cline.close_connection()

        for i in model_find_info:
            i['_id'] = str(i['_id'])

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "status_code": status.HTTP_200_OK,
                "message": "获取成功",
                "data": model_find_info,
                "total": len(model_find_info)
            })



    except Exception as e:
        logger.error(e)
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "message": "执行失败",
            })
