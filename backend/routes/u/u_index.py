from fastapi import APIRouter
from fastapi import Request
from pydantic import BaseModel

from config.logging_config import get_logger


u_v1_router = APIRouter(prefix="/v1/update", tags=["update"])

# 获取日志记录器
logger = get_logger(__name__)