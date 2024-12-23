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
