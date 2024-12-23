from typing import List
from fastapi import APIRouter
from fastapi import Request
from pydantic import BaseModel

from config.logging_config import get_logger
from routes.u.v1.model.v1_update_key import v1_update_key
from routes.u.v1.model.v1_update_model import v1_update_model

u_v1_router = APIRouter(prefix="/v1/update", tags=["update"])

# 获取日志记录器
logger = get_logger(__name__)

class Model(BaseModel):
    base_url: str
    Model_name: str
    Model_call: str
    Model_introduction: str
    Model_tag: List[str]
    Model_call_input: int
    Model_call_output: int
    limit: int
    residue_limit: int
    enable: bool
    charging: bool
    id: str
    user_name: str
    user_id: str

@u_v1_router.post("/model", response_model=Model)
async def model(Model: Model):
    """获取消息"""
    return await v1_update_model({
        "base_url": Model.base_url,
        "model_name": Model.Model_name,
        "model_call": Model.Model_call,
        "model_introduction": Model.Model_introduction,
        "model_tag": Model.Model_tag,
        "model_call_input": Model.Model_call_input,
        "model_call_output": Model.Model_call_output,
        "limit": Model.limit,
        "residue_limit": Model.residue_limit,
        "enable": Model.enable,
        "charging": Model.charging,
        "_id": Model.id,
        "user_name": Model.user_name,
        "user_id": Model.user_id,
    })

class Key(BaseModel):
    key: str
    key_introduction: str
    limit: int
    residue_limit: int
    availableModels: List[str]
    enable: bool
    charging: bool
    id: str
    user_name: str
    user_id: str


@u_v1_router.post("/key", response_model=Key)
async def key(Key: Key):
    """获取消息"""
    return await v1_update_key({
        "key": Key.key,
        "key_introduction": Key.key_introduction,
        "limit": Key.limit,
        "residue_limit": Key.residue_limit,
        "availableModels": Key.availableModels,
        "enable": Key.enable,
        "charging": Key.charging,
        "_id": Key.id,
        "user_name": Key.user_name,
        "user_id": Key.user_id,
    })
