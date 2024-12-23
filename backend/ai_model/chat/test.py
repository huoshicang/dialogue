import json
from typing import Dict, Any

from openai import OpenAI

client = OpenAI(
    api_key="sk-52NNK6XPLrn5mrPPFTOX0PtBru02PrSc2XrxkUgmzER1491s",
    base_url="https://api.moonshot.cn/v1",
)


# search 工具的具体实现，这里我们只需要返回参数即可
def search_impl(arguments: Dict[str, Any]) -> Any:
    """
    在使用 Moonshot AI 提供的 search 工具的场合，只需要原封不动返回 arguments 即可，
    不需要额外的处理逻辑。

    但如果你想使用其他模型，并保留联网搜索的功能，那你只需要修改这里的实现（例如调用搜索
    和获取网页内容等），函数签名不变，依然是 work 的。

    这最大程度保证了兼容性，允许你在不同的模型间切换，并且不需要对代码有破坏性的修改。
    """
    return arguments


tools = [
    {
        "type": "builtin_function",
        "function": {
            "name": "$web_search",
        },
    }
]

messages = [
    {"role": "user", "content": "请联网搜索 Context Caching 技术。"},
]

stream = client.chat.completions.create(
    model="moonshot-v1-auto",
    messages=messages,
    temperature=0.3,
    stream=True,
    tools=tools,
    n=1,
)

message = {
    "tool_calls": [],
}

for chunk in stream:
    for choice in chunk.choices:
        index = choice.index
        delta = choice.delta
        role = delta.role
        if role:
            message["role"] = role
        content = delta.content
        if content:
            if "content" not in message:
                message["content"] = content
            else:
                message["content"] = message["content"] + content
        if delta.tool_calls:
            for tool_call in delta.tool_calls:
                tool_call_index = tool_call.index
                if len(message["tool_calls"]) < (tool_call_index + 1):
                    message["tool_calls"].extend(
                        [{}] * (tool_call_index + 1 - len(message["tool_calls"]))
                    )
                tool_call_object = message["tool_calls"][tool_call_index]
                tool_call_object["index"] = tool_call_index
                tool_call_id = tool_call.id
                if tool_call_id:
                    tool_call_object["id"] = tool_call_id
                tool_call_type = tool_call.type
                if tool_call_type:
                    tool_call_object["type"] = tool_call_type
                tool_call_function = tool_call.function
                if tool_call_function:
                    if "function" not in tool_call_object:
                        tool_call_object["function"] = {}
                    tool_call_function_name = tool_call_function.name
                    if tool_call_function_name:
                        tool_call_object["function"]["name"] = tool_call_function_name
                    tool_call_function_arguments = tool_call_function.arguments
                    if tool_call_function_arguments:
                        if "arguments" not in tool_call_object["function"]:
                            tool_call_object["function"]["arguments"] = (
                                tool_call_function_arguments
                            )
                        else:
                            tool_call_object["function"]["arguments"] = (
                                tool_call_object["function"]["arguments"]
                                + tool_call_function_arguments
                            )
                message["tool_calls"][tool_call_index] = tool_call_object

tool_calls = message["tool_calls"]
if tool_calls:
    messages.append(message)
    for tool_call in tool_calls:
        tool_call_name = tool_call["function"]["name"]
        if tool_call_name == "$web_search":
            print(
                f"使用 $web_search 工具，参数为：{tool_call['function']['arguments']}\n"
            )
            tool_call_arguments = json.loads(tool_call["function"]["arguments"])
            tool_result = search_impl(tool_call_arguments)
            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call["id"],
                    "name": tool_call_name,
                    "content": json.dumps(tool_result),
                }
            )

next_stream = client.chat.completions.create(
    model="moonshot-v1-auto",
    messages=messages,
    temperature=0.3,
    stream=True,
    tools=tools,
    n=1,
)

for chunk in next_stream:
    if chunk.choices:
        delta = chunk.choices[0].delta
        if delta.content:
            print(delta.content, end="", flush=True)
