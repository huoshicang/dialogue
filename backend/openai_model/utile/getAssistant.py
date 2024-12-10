from openai import OpenAI

from config.logging_config import get_logger

logger = get_logger(__name__)

def getAssistant(ketInfo, base_url, messageInfo):
    """
    请求模型
    :param ketInfo: 密钥
    :param base_url: BaseUrl
    :param messageInfo:
    :return: completion
    """
    try:
        client = OpenAI(
            api_key=ketInfo['key'],
            base_url=base_url['base_url'],
        )

        completion = client.chat.completions.create(
            timeout=180,
            model=messageInfo['model'],
            messages=messageInfo['messages'],
            top_p=messageInfo['top_p'],
            temperature=messageInfo['temperature'],
            stream=True,
            stream_options={"include_usage": True},
            # tools=messageInfo['tools']
        )

        return completion, True
    except Exception as e:
        logger.error(e)
        return e, False