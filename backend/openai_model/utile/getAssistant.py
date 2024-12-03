from openai import OpenAI


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
            model=messageInfo['model'],
            messages=messageInfo['messages'],
            top_p=messageInfo['top_p'],
            temperature=messageInfo['temperature'],
            stream=True,
            stream_options={"include_usage": True}
        )

        return completion, True
    except Exception as e:
        return e, False