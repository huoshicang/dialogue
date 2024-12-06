from starlette import status
from starlette.responses import JSONResponse
from config.logging_config import get_logger
from database.redis_client import RedisClient
from utils.token import verify

logger = get_logger(__name__)


async def profile_routes(request):
    try:
        cookie = request.headers.get('cookie', '')
        session_id = None

        # 解析Cookie头部以查找sessionId
        if not cookie:
            logger.error(f"登录失效")
            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={
                    "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
                    "message": "登录失效",
                }
            )

        cookies = {key.strip(): value.strip() for key, value in (item.split("=", 1) for item in cookie.split(";"))}
        session_id = cookies.get('sessionId')

        if not session_id:
            logger.error(f"会话失效")
            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={
                    "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
                    "message": "会话失效",
                }
            )

        redis_client = RedisClient().get_value(session_id)

        if not redis_client:
            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={
                    "status_code": status.HTTP_401_UNAUTHORIZED,
                    "message": "获取失败",
                }
            )

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "status_code": status.HTTP_200_OK,
                "data": redis_client,
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
            }
        )
