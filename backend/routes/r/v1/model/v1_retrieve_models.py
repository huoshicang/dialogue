from fastapi import status
from fastapi.responses import JSONResponse
from bson import ObjectId
from config.logging_config import get_logger
from database.mongo import MongoDBClient

logger = get_logger(__name__)


async def v1_retrieve_models():
    """
    获取聊天
    :return:
    """
    try:
        # 连接数据库
        models_cline = MongoDBClient("models")

        # 查找信息
        model_find_info = models_cline.find_data_many(
            {
                'is_deleted': False,
                'enable': True
            },
            {
                "_id": False,
                "model_name": True,
                "model_call": True,
                "limit": True,
                "residue_limit": True,
                "model_introduction": True,
            })
        models_cline.close_connection()

        # 判断是否获取成功
        if not model_find_info:
            logger.error("获取模型列表失败")
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={
                    "status_code": status.HTTP_404_NOT_FOUND,
                    "message": "未找到信息",
                })

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
