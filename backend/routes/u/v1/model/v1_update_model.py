from fastapi.responses import JSONResponse
from bson import ObjectId
from config.logging_config import get_logger
from fastapi import status
from database.mongo import MongoDBClient

logger = get_logger(__name__)

async def v1_update_model(data):
    try:

        print(data)

        _id  = data.pop("_id")
        user_id  = data.pop("user_id")
        del data["user_name"]

        models_client = MongoDBClient("models")
        models_updata_info = models_client.update_data(
            {
                "$and": [
                    {"_id": ObjectId(_id)},
                    {"user_id":user_id},
                    {"is_deleted": False},
                ]
            },
            {"$set": data}
        )
        models_client.close_connection()

        if not models_updata_info:
            logger.error("更新失败")
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={
                    "status_code": status.HTTP_401_UNAUTHORIZED,
                    "message": "更新失败",
                })

        logger.info("更新成功")
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "status_code": status.HTTP_200_OK,
                "message": "更新成功",
            })

    except Exception as e:
        logger.error(e)
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "message": "执行失败",
            })
