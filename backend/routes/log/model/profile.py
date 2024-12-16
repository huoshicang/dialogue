from bson import ObjectId
from starlette import status
from starlette.responses import JSONResponse
from config.logging_config import get_logger
from database.mongo import MongoDBClient
from utils.token import verify

logger = get_logger(__name__)


async def profile_routes(request):
    try:

        # 获取cooike
        cookie = request.headers.get("cookie", "")
        # 验证cookie
        if not cookie:
            logger.error("登录失效")
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={
                    "status_code": status.HTTP_401_UNAUTHORIZED,
                    "message": "登录失效",
                },
            )

        # 获取session_id
        cookies = {
            key.strip(): value.strip()
            for key, value in (item.split("=", 1) for item in cookie.split(";"))
        }
        session_id = cookies.get("sessionId")
        # 验证session_id
        if not session_id:
            logger.error("会话失效")
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={
                    "status_code": status.HTTP_401_UNAUTHORIZED,
                    "message": "会话失效",
                },
            )

        # 获取并验证token
        token = request.headers.get("authorization", "").replace("Bearer ", "")
        info = verify(token, session_id)
        # 如果token失效
        if not info:
            logger.error("登录失效")
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={
                    "status_code": status.HTTP_401_UNAUTHORIZED,
                    "message": "需要重新登录",
                },
            )

        # 查询用户信息
        users_client = MongoDBClient("users")
        find_info = users_client.find_data(
            {"_id": ObjectId(info["sub"])},
            {"is_deleted": False, "password": False, "confirm_password": False},
        )
        users_client.close_connection()

        # 用户信息不存在
        if not find_info:
            logger.error("用户不存在")
            return JSONResponse(
                status_code=status.HTTP_404_NOT_FOUND,
                content={
                    "status_code": status.HTTP_404_NOT_FOUND,
                    "message": "用户不存在",
                },
            )

        # 返回用户信息
        find_info["_id"] = str(find_info["_id"])
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "status_code": status.HTTP_200_OK,
                "data": find_info,
                "message": "获取成功",
            },
        )

    except Exception as e:
        logger.error(e)
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "message": "执行失败",
            },
        )
