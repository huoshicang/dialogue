import hashlib

import bcrypt


def hash_password(password: str) -> str:
    """
    对密码进行哈希处理
    :param password: 明文密码
    :return: 哈希后的密码
    """
    # 生成随机的盐
    SALE = "Miss"

    md = hashlib.md5(password.encode())  # 创建md5对象

    return md.hexdigest()
