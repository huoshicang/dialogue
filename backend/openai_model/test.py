from openai import OpenAI


def response_modelss(data):
    client = OpenAI(
        # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
        # api_key="sk-474a56d1d43140788d925a5888cda83a",
        # base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        api_key="sk-nqvvlQXTPvfCP0NOSYIZqATfLIqfWihKIviSDS5YdsvAhUpw",
        base_url="https://api.chatanywhere.tech",
    )
    completion = client.chat.completions.create(
        # model="qwen-turbo-1101",  # 模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
        model="gpt-3.5-turbo",  # 模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
        messages=[
            {'role': 'user', 'content': data}],
        stream=True,
        stream_options={"include_usage": True}
    )
    # return completion
    for chunk in completion:
        # print(chunk.model_dump_json())
        print(chunk.choices[0].delta.content)


# response_modelss("你好")