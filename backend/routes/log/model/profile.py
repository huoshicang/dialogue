from starlette import status
from starlette.responses import JSONResponse
from config.logging_config import get_logger
from database.redis_client import RedisClient
from utils.token import verify

logger = get_logger(__name__)


async def profile_routes(request):
    try:
        headers = request.headers

        if headers.get('authorization') and headers.get('login_id'):

            token_info = verify(str(headers.get('authorization')).replace("Bearer ", ""),
                                headers.get('login_id'))

            if token_info:
                UUID = token_info['UUID']

                redis_client = RedisClient().get_value(UUID)

                return JSONResponse(
                    status_code=status.HTTP_200_OK,
                    content={
                        "status_code": status.HTTP_200_OK,
                        "data": redis_client,
                        "message": "获取成功",
                    },
                )

            return JSONResponse(
                status_code=status.HTTP_401_UNAUTHORIZED,
                content={
                    "status_code": status.HTTP_401_UNAUTHORIZED,
                    "message": "获取失败",
                }
            )

        else:
            logger.error(f"token：{headers.get('authorization', "")} secret_key：{headers.get('login_id', "")}")
            return JSONResponse(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                content={
                    "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR,
                    "message": "获取失败",
                }
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
