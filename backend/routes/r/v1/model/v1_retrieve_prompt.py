from fastapi import status
from fastapi.responses import JSONResponse
from bson import ObjectId
from config.logging_config import get_logger
from database.mongo import MongoDBClient

logger = get_logger(__name__)


async def v1_retrieve_prompt():
    """
    获取聊天
    :return:
    """
    try:
        # 连接数据库
        prompt_cline = MongoDBClient("prompts")

        # 查找信息
        prompt_find_info = prompt_cline.find_data_many(
            {
                'is_deleted': False,
            },
            {
                "_id": False,
                "act": True,
                "prompt": True,
            })
        prompt_cline.close_connection()

        # 判断是否获取成功
        if not prompt_find_info:
            logger.error("获取提示词失败")
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
                "data": prompt_find_info,
                "total": len(prompt_find_info)
            })

    except Exception as e:
        logger.error(e)
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "message": "执行失败",
            })
