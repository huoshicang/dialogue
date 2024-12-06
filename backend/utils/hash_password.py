import hashlib
import os

import bcrypt


def hash_password(password: str) -> str:
    """
    使用SHA-256算法对密码进行散列，并可选择性地添加盐。
    :param password: 要散列的密码字符串。
    :return: 一个包含盐和散列后密码的元组。
    """
    # 生成随机的盐
    SALT = str(os.getenv("SALE", "gH4gG0nO3xI6yG0o")).encode('utf-8')

    # 使用 pbkdf2_hmac 进行散列
    hashed_password = hashlib.pbkdf2_hmac(
        'sha256',  # 散列算法
        password.encode('utf-8'),  # 密码的字节串表示
        SALT,  # 盐的字节串表示
        100000  # 迭代次数
    ).hex()

    return hashed_password

