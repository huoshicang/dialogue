# 运行前请 pip install tiktoken
from dashscope import get_tokenizer  # dashscope版本 >= 1.14.0

# 获取tokenizer对象，目前只支持通义千问系列模型
tokenizer = get_tokenizer('qwen-plus')

input_str = '一只公鸡在水里游泳，然后下了一个蛋，水的水平面会上升吗'

# 将字符串切分成token并转换为token id
tokens = tokenizer.encode(input_str)
print(tokens)
print(len(tokens))
