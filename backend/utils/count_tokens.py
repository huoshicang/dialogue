import tiktoken

def count_tokens(text, encoding_name='cl100k_base'):
    """
    计算给定文本中的 tokens 数量。

    参数:
    text (str): 要计算 tokens 的文本。
    encoding_name (str): 使用的编码名称，默认为 'cl100k_base'。

    返回:
    int: 文本中的 tokens 数量。
    """
    # 获取指定编码
    encoding = tiktoken.get_encoding(encoding_name)

    # 将文本编码为 tokens
    tokens = encoding.encode(text)

    # 返回 tokens 数量
    return len(tokens)
