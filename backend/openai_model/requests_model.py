from fastapi import WebSocket, APIRouter
import asyncio
import json

from config.logging_config import get_logger
from openai_model.utile import *
from openai_model.utile.getUserInfo import getUserInfo
from utils.count_tokens import count_tokens

logger = get_logger(__name__)

send_message = APIRouter()


def check_limit(charging, tokens, limit, error_message):
    """
    检查是否超出额度限制，如果是则发送错误信息并关闭连接。
    :param charging: 是否开启计费
    :param tokens: 当前请求的token数量
    :param limit: 剩余额度
    :param error_message: 错误信息
    :return: 如果超出额度返回False，否则返回True
    """
    if charging and tokens > limit:
        logger.error(error_message)
        return False
    return True


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
        tokens = count_tokens(data['sendMessage'])
        logger.info(f"请求tokens：{tokens}")

        # 获取用户信息并检查用户额度
        userInfo = getUserInfo(userId=data['userId'], tokens=tokens)
        if not check_limit(
                charging=userInfo['charging'],
                tokens=tokens, limit=userInfo['limit'],
                error_message=f"用户{data['userId']}无额度"):
            await websocket.send_text("额度不足")
            await websocket.close()
            return

        # 获取消息信息
        messageInfo = getMessage(data=data)
        if not messageInfo:
            logger.error(f"用户{data['userId']}无消息")
            await websocket.send_text("找不到消息")
            await websocket.close()
            return

        # 将用户发送的消息添加到消息列表中
        messageInfo['messages'].append({
            "role": "user",
            "content": data['sendMessage']
        })

        # 获取真实key并检查key额度
        ketInfo = getKey(key=messageInfo['key'], model=messageInfo['model'])
        if not check_limit(charging=ketInfo['charging'],
                           tokens=tokens, limit=ketInfo['residue_limit'],
                           error_message=f"密钥{messageInfo['key']}额度不足"):
            await websocket.send_text("密钥可用额度不足")
            await websocket.close()
            return

        # 获取base_url并检查模型额度
        base_url = getBaseUrl(model=messageInfo['model'], tokens=tokens)
        if not check_limit(charging=base_url['charging'],
                           tokens=tokens, limit=base_url['residue_limit'],
                           error_message=f"模型{messageInfo['model']}无额度",):
            await websocket.send_text("模型可用额度不足")
            await websocket.close()
            return

        # 调用OpenAI模型获取回复
        completion, completionSigns = getAssistant(ketInfo=ketInfo, base_url=base_url, messageInfo=messageInfo)
        assistantContentInfo = None

        # 处理模型回复
        if completionSigns:
            logger.info(f"用户{data['userId']}请求模型{messageInfo['model']}")
            for chunk in completion:
                info = json.loads(chunk.model_dump_json())
                if not assistantContentInfo:
                    assistantContentInfo = info
                if len(info['choices']) == 0:
                    assistantContentInfo['usage'] = info['usage']
                else:
                    skipData = ["None"]
                    sendText = str(info['choices'][0]['delta']['content'])
                    # 判断是否需要跳过
                    if sendText not in skipData:
                        await websocket.send_text(sendText)
                        assistantContentInfo['choices'][0]['delta']['content'] += sendText

            await websocket.close()
            TotalTokens = assistantContentInfo['usage']['total_tokens']
            logger.info(f"用户{data['userId']}合计tokens：{TotalTokens}")

            # 更新消息记录
            updateMessage(data, {
                "role": "user",
                "content": data['sendMessage']
            }, {
                              "role": "assistant",
                              "content": assistantContentInfo['choices'][0]['delta']['content']
                          })

            # 更新用户、key和模型的额度
            if userInfo['charging']:
                updateUserLimit(userId=data['userId'], newLimit=userInfo['limit'] - TotalTokens)

            if ketInfo['charging']:
                updateKeyLimit(key=ketInfo['key'], userId=data['userId'],
                               newLimit=ketInfo['residue_limit'] - TotalTokens)

            if base_url['charging']:
                updateModelLimit(userId=data['userId'], model=messageInfo['model'],
                                 newLimit=base_url['residue_limit'] - TotalTokens)
        else:
            logger.error(f"用户{data['userId']}请求模型{messageInfo['model']}发生错误")
            logger.error(completion)
            await websocket.send_text(str(completion))
    except Exception as e:
        logger.error(f"处理websocket请求时发生错误: {e}")
        await websocket.send_text("服务器内部错误")
        await websocket.close()
