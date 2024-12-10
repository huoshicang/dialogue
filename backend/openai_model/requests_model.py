from fastapi import WebSocket, APIRouter
import asyncio
import json

from config.logging_config import get_logger
from openai_model.utile import *
from openai_model.utile.getUserInfo import getUserInfo
from utils.count_tokens import count_tokens

logger = get_logger(__name__)

send_message = APIRouter()


@send_message.websocket("/message")
async def websocket_endpoint(websocket: WebSocket):
    """
    传入发送文本 用户id 聊天id
    通过用户id 聊天id 获取消息id，然后获取消息内容
    构建message
    通过消息内容中的key和model，获取真实key
    通过消息中的model，获取base_url
    :param websocket:
    :return:
    """
    await websocket.accept()
    data = json.loads(await websocket.receive_text())

    tokens = count_tokens(data['sendMessage'])

    logger.info(f"请求tokens：{tokens}")

    userInfo = getUserInfo(userId=data['userId'], tokens=tokens)
    if not userInfo:
        logger.error(f"用户{data['userId']}无额度")
        await websocket.send_text("用户无额度，请联系管理员")
        await websocket.close()
        return

    # 通过用户id 聊天id 获取消息id，然后获取消息内容
    messageInfo = getMessage(data=data)
    if not messageInfo:
        logger.error(f"用户{data['userId']}无消息")
        await websocket.send_text("找不到消息")
        await websocket.close()
        return

    # 构建 message
    messageInfo['messages'].append({
        "role": "user",
        "content": data['sendMessage']
    })

    # 通过消息内容中的key和model，获取真实key
    ketInfo = getKey(key=messageInfo['key'], model=messageInfo['model'], tokens=tokens)
    if not ketInfo:
        logger.error(f"密钥{messageInfo['key']}无额度")
        await websocket.send_text("密钥无额度，请联系管理员")
        await websocket.close()
        return

    # 通过消息中的model，获取base_url
    base_url = getBaseUrl(model=messageInfo['model'], tokens=tokens)
    if not base_url:
        logger.error(f"模型{messageInfo['model']}无额度")
        await websocket.send_text("模型无额度，请联系管理员")
        await websocket.close()
        return

    completion, completionSigns = getAssistant(ketInfo=ketInfo, base_url=base_url, messageInfo=messageInfo)
    assistantContentInfo = None

    # 获取错误信息
    # 无错误
    if completionSigns:
        logger.info(f"用户{data['userId']}请求模型{messageInfo['model']}")
        for chunk in completion:
            # 转为字典
            info = json.loads(chunk.model_dump_json())

            # 初始化回复内容
            if not assistantContentInfo:
                assistantContentInfo = info
            # 获取最后一条数据，包含tokens
            if len(info['choices']) == 0:
                assistantContentInfo['usage'] = info['usage']
            else:
                skipData = ["None"]
                # 发送数据
                sendText = str(info['choices'][0]['delta']['content'])
                if sendText not in skipData:
                    await websocket.send_text(sendText)
                    assistantContentInfo['choices'][0]['delta']['content'] += sendText
                # await asyncio.sleep(0.1)

        await websocket.close()
        TotalTokens = tokens + assistantContentInfo['usage']['total_tokens']
        logger.info(f"用户{data['userId']}合计tokens：{TotalTokens}")

        updateMessage(data, {
            "role": "user",
            "content": data['sendMessage']
        }, {
                          "role": "assistant",
                          "content": assistantContentInfo['choices'][0]['delta']['content']
                      })

        if userInfo['charging']:
            updateUserLimit(userId=data['userId'], total_tokens=TotalTokens)

        if ketInfo['charging']:
            updateKeyLimit(key=ketInfo['key'], userId=data['userId'], total_tokens=TotalTokens)

        if base_url['charging']:
            updateModelLimit(data['userId'], messageInfo['model'], total_tokens=TotalTokens)
    else:
        # 发生错误
        logger.error(f"用户{data['userId']}请求模型{messageInfo['model']}发生错误")
        logger.error(completion)
        await websocket.send_text(str(completion))
