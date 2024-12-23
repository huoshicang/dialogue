from fastapi import WebSocket, APIRouter
import json

from config.logging_config import get_logger
from ai_model.chat import *
from utils.count_tokens import count_tokens

logger = get_logger(__name__)

send_message = APIRouter()


@send_message.websocket("/message")
async def websocket_endpoint(websocket: WebSocket):
    """
    处理WebSocket消息请求，包括验证用户额度、获取消息内容、构建消息、调用OpenAI模型并返回结果。
    :param websocket: WebSocket对象
    """
    await websocket.accept()
    try:
        # 接收并解析客户端发送的JSON数据
        data = json.loads(await websocket.receive_text())
        tokens = count_tokens(data["sendMessage"])
        logger.info(f"请求tokens：{tokens}")

        # 获取用户信息并检查用户额度
        user_info = getUserInfo(userId=data["userId"], tokens=tokens)
        if not check_limit(
            charging=user_info["charging"],
            tokens=tokens,
            limit=user_info["limit"],
            error_message=f"用户{data['userId']}无额度",
        ):
            await websocket.send_text("额度不足")
            await websocket.close()
            return

        # 获取消息信息
        message_info = getMessage(data=data)
        if not message_info:
            logger.error(f"用户{data['userId']}无消息")
            await websocket.send_text("找不到消息")
            await websocket.close()
            return

        # 将用户发送的消息添加到消息列表中
        message_info["messages"].append(
            {"role": "user", "content": data["sendMessage"]}
        )

        # 获取真实key并检查key额度
        key_info = getKey(key=message_info["key"], model=message_info["model"])
        if not check_limit(
            charging=key_info["charging"],
            tokens=tokens,
            limit=key_info["residue_limit"],
            error_message=f"密钥{message_info['key']}额度不足",
        ):
            await websocket.send_text("密钥可用额度不足")
            await websocket.close()
            return

        # 获取base_url并检查模型额度
        base_url = getBaseUrl(model=message_info["model"], tokens=tokens)
        if not check_limit(
            charging=base_url["charging"],
            tokens=tokens,
            limit=base_url["residue_limit"],
            error_message=f"模型{message_info['model']}无额度",
        ):
            await websocket.send_text("模型可用额度不足")
            await websocket.close()
            return

        # 调用OpenAI模型获取回复
        completion, completion_signs = getAssistant(
            ketInfo=key_info, base_url=base_url, messageInfo=message_info
        )
        assistant_content_info = None

        # 处理模型回复
        if completion_signs:
            logger.info(f"用户{data['userId']}请求模型{message_info['model']}")
            for chunk in completion:
                info = json.loads(chunk.model_dump_json())
                if not assistant_content_info:
                    assistant_content_info = info
                if len(info["choices"]) == 0:
                    assistant_content_info["usage"] = info["usage"]
                else:
                    send_text = str(info["choices"][0]["delta"]["content"])
                    # 判断是否需要跳过
                    if send_text not in ['None', None]:
                        await websocket.send_text(send_text)
                        assistant_content_info["choices"][0]["delta"][
                            "content"
                        ] += send_text

            await websocket.close()
            total_tokens = assistant_content_info["usage"]["total_tokens"]
            logger.info(f"用户{data['userId']}合计tokens：{total_tokens}")

            # 更新消息记录
            updateMessage(
                data,
                {"role": "user", "content": data["sendMessage"]},
                {
                    "role": "assistant",
                    "content": assistant_content_info["choices"][0]["delta"]["content"],
                },
            )

            # 更新用户、key和模型的额度
            if user_info["charging"]:
                updateUserLimit(
                    userId=data["userId"], newLimit=user_info["limit"] - total_tokens
                )

            if key_info["charging"]:
                updateKeyLimit(
                    key=key_info["key"],
                    userId=data["userId"],
                    newLimit=key_info["residue_limit"] - total_tokens,
                )

            if base_url["charging"]:
                updateModelLimit(
                    userId=data["userId"],
                    model=message_info["model"],
                    newLimit=base_url["residue_limit"] - total_tokens,
                )
        else:
            logger.error(f"用户{data['userId']}请求模型{message_info['model']}发生错误")
            logger.error(completion)
            await websocket.send_text(str(completion))
    except Exception as e:
        logger.error(f"处理websocket请求时发生错误: {e}")
        await websocket.send_text("服务器内部错误")
        await websocket.close()
