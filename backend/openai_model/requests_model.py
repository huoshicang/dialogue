from fastapi import WebSocket, APIRouter
import asyncio
import json
from openai_model.utile import *

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

    # 通过用户id 聊天id 获取消息id，然后获取消息内容
    messageInfo = getMessage(data)

    print("messageInfo", messageInfo)

    # 构建 message
    messageInfo['messages'].append({
        "role": "user",
        "content": data['sendMessage']
    })

    # 通过消息内容中的key和model，获取真实key
    ketInfo = getKey(messageInfo['key'], messageInfo['model'])

    print("ketInfo", ketInfo)

    if not ketInfo:
        await websocket.send_text("key发生错误，请联系管理员")
        return

    # 通过消息中的model，获取base_url
    base_url = getBaseUrl(messageInfo['model'])

    print("base_url", base_url)

    if not base_url:
        await websocket.send_text("model发生错误，请联系管理员")
        return

    completion, completionSigns = getAssistant(ketInfo, base_url, messageInfo)
    print("completion", completion, completionSigns)
    assistantContentInfo = None

    # 获取错误信息
    # 无错误
    if completionSigns:
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

        updateMessage(data, {
            "role": "user",
            "content": data['sendMessage']
        }, {
            "role": "assistant",
            "content": assistantContentInfo['choices'][0]['delta']['content']
        })

        # todo 更新用户的额度
        userCharging = updateUserLimit(data, assistantContentInfo['usage']['total_tokens'])

        # todo 更新key的额度
        if userCharging and ketInfo['charging']:
            updateKeyLimit(ketInfo['key'], data['userId'], assistantContentInfo['usage']['total_tokens'])

        # todo 更新模型的额度
        if userCharging and base_url['charging']:
            updateModelLimit(messageInfo['model'], data['userId'], assistantContentInfo['usage']['total_tokens'])
    # 发生错误
    else:
        await websocket.send_text(str(completion))
