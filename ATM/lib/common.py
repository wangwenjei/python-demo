"""
    存放公共方法
"""
import hashlib


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



