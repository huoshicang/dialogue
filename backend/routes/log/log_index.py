from fastapi import APIRouter
from pydantic import BaseModel
from fastapi import Request
from config.logging_config import get_logger
from routes.log.model.login import login_routes
from routes.log.model.profile import profile_routes
from routes.log.model.register import register_routes

log_router = APIRouter()

# 获取日志记录器
logger = get_logger(__name__)


class Register(BaseModel):
    """
    注册字段
    """
    username: str
    email: str
    password: str
    confirm_password: str
    # 可选字段
    # address: str | None = None


class Login(BaseModel):
    """
    登录字段
    """
    account: str
    password: str


@log_router.post("/register")
async def register(register: Register):
    return await register_routes({
        "username": register.username,
        "email": register.email,
        "password": register.password,
    })


@log_router.post("/login")
async def login(login: Login, request: Request):
    return await login_routes({
        "account": login.account,
        "password": login.password
    }, request)


@log_router.get("/profile")
async def profile(request: Request):
    return await profile_routes(request)
