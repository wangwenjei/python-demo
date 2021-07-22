"""
    存放公共方法
"""
import configparser
import hashlib
import logging
from logging import config,getLogger
from conf import settings



# MD5密码加密功能
def get_pwd_md5(user_passwd):
    md5_obj = hashlib.md5()
    md5_obj.update(user_passwd.encode('utf-8'))
    salt = "密码加盐"
    md5_obj.update(salt.encode('utf-8'))

    return md5_obj.hexdigest()


# 登录认证装饰器
def login_auth(func):
    from core import src
    def wrapper(*args, **kwargs):
        if src.login_user:
            res = func(*args, **kwargs)
            return res
        else:
            print("请先登录账户")
            src.login()

    return wrapper


def get_logger(log_type):
    """
    根据传入名称打印不同的日志类型
    :param log_type: 日志类型
    :return:
        logger : 日志内容
    """
    config.dictConfig(settings.LOGGING_DIC)
    logger = getLogger(log_type)

    return logger
