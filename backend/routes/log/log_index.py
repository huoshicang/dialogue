from fastapi import APIRouter
from pydantic import BaseModel
from fastapi import Request
from config.logging_config import get_logger
from routes.log.model.login import login_routes
from routes.log.model.profile import profile_routes
from routes.log.model.register import register_routes

log_router = APIRouter(prefix="/log", tags=["log"],)

# 获取日志记录器
logger = get_logger(__name__)


class Register(BaseModel):
    """
    注册
    """
    username: str
    email: str
    password: str
    confirm_password: str


class Login(BaseModel):
    """
    登录
    """
    account: str
    password: str


@log_router.post("/register")
async def register(register: Register):
    """注册"""
    return await register_routes({
        "username": register.username,
        "email": register.email,
        "password": register.password,
        "confirm_password": register.confirm_password
    })


@log_router.post("/login")
async def login(login: Login, request: Request):
    """登录"""
    return await login_routes({
        "account": login.account,
        "password": login.password
    }, request)


@log_router.get("/profile")
async def profile(request: Request):
    """验证"""
    return await profile_routes(request)
