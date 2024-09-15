import dashscope

dashscope.api_key = 'sk-474a56d1d43140788d925a5888cda83a'


def get_response(messages):
    response = dashscope.Generation.call(
        model="qwen-plus",
        messages=messages,
        result_format='message',
    )
    return response


messages = []

# 您可以自定义设置对话轮数，当前为3
for i in range(3):
    user_input = input("请输入：")
    # 将用户问题信息添加到messages列表中
    messages.append({'role': 'user', 'content': "你好"})
    print(messages)
    assistant_output = get_response(messages)
    # assistant_output = get_response(messages).output.choices[0]['message']['content']
    # 将大模型的回复信息添加到messages列表中
    messages.append({'role': 'assistant', 'content': assistant_output})
    print(f'用户输入：{user_input}')
    print(f'模型输出：{assistant_output}')
    # print('\n')
