from fastapi import APIRouter
from fastapi import Request
from config.logging_config import get_logger
from routes.r.v1.model.v1_retrieve_chat import v1_retrieve_chat

r_v1_router = APIRouter(prefix="/v1/retrieve", tags=["retrieve"])

# 获取日志记录器
logger = get_logger(__name__)

@r_v1_router.get("/chat")
async def chat(request: Request):
    return await v1_retrieve_chat(request.query_params)