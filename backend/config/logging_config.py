import logging
import logging.config
import os
from datetime import datetime
import traceback
import yaml


# 定义配置类，包含日志和数据的配置
class Config:
    class Log:
        # 控制台日志级别配置
        console_log_level = "DEBUG"

    class Data:
        # 数据目录配置
        data_dir = "./data"

    # 是否打印堆栈信息的配置
    common = type('common', (object,), {'print_traceback': True})


current_dir = os.path.dirname(os.path.abspath(__file__))


# 从 YAML 文件中读取日志配置，并根据需要进行修改
def get_log_config():
    config_path = os.path.join(current_dir, 'logging_config.yaml')

    with open(config_path, 'r', encoding="utf-8") as f:
        log_config = yaml.safe_load(f.read())
    # 设置日志文件名
    log_config['handlers']['file_handler']['filename'] = g.server_log_filename
    # 设置控制台日志级别
    log_config['handlers']['console_handler']['level'] = Config.Log.console_log_level
    return log_config


# 设置日志记录器，包括日志目录的创建和日志配置的加载
def setup_logger():
    log_dir = os.path.join(Config.Data.data_dir, 'logs')
    os.makedirs(log_dir, exist_ok=True)
    # 生成带有时间戳的日志文件名
    g.server_log_filename = os.path.join(log_dir, f"{datetime.now().strftime('%Y%m%d')}.log")
    log_config = get_log_config()
    # 应用日志配置
    logging.config.dictConfig(log_config)


# 获取指定名称的日志记录器
def get_logger(name):
    return logging.getLogger(f"哎.{name}")


# 打印带有堆栈信息的异常，根据配置决定是否打印详细堆栈
def with_traceback(e: Exception):
    if Config.common.print_traceback:
        tb = traceback.extract_tb(e.__traceback__)
        last_frames = tb[-10:]
        formatted_traceback = ["traceback:"]
        for frame in last_frames:
            frame_info = f"{frame.filename}:{frame.lineno} in {frame.name}"
            formatted_traceback.append(frame_info)
        formatted_traceback = "\n".join(formatted_traceback)
        return f"<{e.__class__.__name__}> {str(e)}\n{formatted_traceback}"
    else:
        return str(e)


# 全局变量，用于存储日志文件名
class Globals:
    server_log_filename = ""


g = Globals()
