from fastapi.responses import FileResponse
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import base64

from starlette import status
from starlette.responses import JSONResponse

from config.logging_config import setup_logger, get_logger

from ai_model.chat.train_model import send_message
from routes.c.v1 import c_index
from routes.r.v1 import r_index
from routes.d.v1 import d_index
from routes.log import log_index
from routes.u import u_index

app = FastAPI()

setup_logger()

app.include_router(send_message)
app.include_router(log_index.log_router)
app.include_router(c_index.c_v1_router)
app.include_router(r_index.r_v1_router)
app.include_router(d_index.d_v1_router)
app.include_router(u_index.u_v1_router)
# 获取日志记录器
logger = get_logger(__name__)

# 跨域
app.add_middleware(
    middleware_class=CORSMiddleware,
    allow_origins=["localhost", '127.0.0.1'],  # 允许的源
    allow_credentials=True,
    allow_methods=["GET", "POST"],  # 允许的方法，如 GET, POST 等
    allow_headers=["*"],  # 允许的头
)


# app.mount("/", StaticFiles(directory="dist", html=True), name="vue_static")

@app.get("/")
async def catch_all(request: Request):
    return FileResponse("dist/index.html")


# 定义中间件
@app.middleware("http")
@app.middleware("https")
async def process_time_middleware(request: Request, call_next):

    if request.headers.get("debug") != "dF5vjy":
        nonce = request.headers.get("nonce")
        timestamp = request.headers.get('timestamp')
        if not nonce:
            logger.error("非法请求: 缺少nonce参数")
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "status_code": status.HTTP_400_BAD_REQUEST,
                    "message": "非法请求",
                },
            )

        nonce = int(base64.b64decode(nonce).decode()) - int(timestamp[::-1])

        if nonce != int(timestamp):
            logger.error("非法请求: 时间戳不匹配")
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "status_code": status.HTTP_400_BAD_REQUEST,
                    "message": "非法请求",
                },
            )

    response = await call_next(request)

    response.headers["X-Requested-Url"] = str(request.url).replace(str(request.base_url), "")

    return response


if __name__ == '__main__':
    for route in app.routes:
        print(f"Path: {route}")
    # 启动应用，开启热更新
    uvicorn.run(
        "main:app",
        host='0.0.0.0',
        port=8000,
        log_level="debug",
        reload=True)

# pip install -r requirements.txt
# pip freeze > requirements.txt
# pipreqs. --encoding=utf-8 --force
# pywin32
