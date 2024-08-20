import jwt

from config.logging_config import get_logger

logger = get_logger(__name__)


def verify(token, secret_key):
    try:
        # 验证JWT
        return jwt.decode(token, secret_key, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        logger.error('JWT已过期')
        return False
    except jwt.InvalidTokenError:
        logger.error('JWT无效')
        return False


def sign(payload, secretKey):
    return jwt.encode(payload, secretKey, algorithm='HS256')
