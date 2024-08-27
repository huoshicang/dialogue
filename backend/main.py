from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from config.logging_config import setup_logger, get_logger
from starlette.requests import Request

from routes.log import log_index
from utils.middleware import LoggingMiddleware

app = FastAPI()

setup_logger()

app.include_router(log_index.log_router)

# 获取日志记录器
logger = get_logger(__name__)

# 跨域
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许的源
    allow_credentials=True,
    allow_methods=["*"],  # 允许的方法，如 GET, POST 等
    allow_headers=["*"],  # 允许的头
)


@app.get("/")
async def read_root(username: str = Query()):
    logger.info("Root endpoint was called")
    return {"Hello": "World"}


# 定义中间件
@app.middleware("http")
async def process_time_middleware(request: Request, call_next):
    # 记录路径参数
    path_params = request.path_params
    if path_params:
        logger.info(f"Path Parameters: {path_params}")

    # 记录请求体
    if request.method in ["POST", "PUT", "PATCH"]:
        try:
            body = await request.json()
            logger.info(f"Request Body: {body}")
        except Exception as e:
            logger.warning(f"Failed to parse JSON body: {e}")

    # 记录查询参数
    query_params = request.query_params
    if query_params:
        logger.info(f"Query Parameters: {query_params}")

    # 打印请求头信息
    headers = dict(request.headers)
    logger.info(f"token：{headers.get('authorization', "")} secret_key：{headers.get('login_id', "")}")

    # 将Request请求传回原路由
    response = await call_next(request)

    response.headers["X-Requested-Url"] = str(request.url).replace(str(request.base_url), "")

    return response


if __name__ == '__main__':
    # 启动应用，开启热更新
    uvicorn.run(
        "main:app",
        host='127.0.0.1',
        port=8000,
        log_level="debug",
        reload=True)

# pip install -r requirements.txt
