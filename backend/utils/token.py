import time
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


def sign(data, secret_key, expiration_time):
    data['iat'] = int(time.time())
    data['exp'] = data['iat'] + expiration_time
    try:
        token = jwt.encode(data, secret_key, algorithm='HS256')
        return token
    except Exception as e:
        logger.error(f'生成JWT时出错: {e}')
        return None
