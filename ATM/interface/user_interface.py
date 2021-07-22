"""
    逻辑接口层
        用户接口
"""
from db import db_handle
from lib import common

# 根据不同的接口类型传入不同的日志对象log_tye=
user_logger = common.get_logger(log_type='user')


# 用户注册接口
def register_interface(user_name, user_passwd):
    """
    判断用户是否存在,存在返回False,不存在则注册新用户
    :param user_name: 用户名
    :param user_passwd: 用户密码
    :return:
    """

    # 查看用户是否存在
    user_dic = db_handle.select_user(user_name)

    # 判断用户是否存在,存在返回false以及提示信息
    if user_dic:
        msg = f'用户名 [f{user_name}] 重复,请重新输入新的用户名'
        user_logger.warn(msg)
        return False, msg

    # 用户密码MD5数据加密
    user_passwd = common.get_pwd_md5(user_passwd)

    # 用户不存在则注册
    db_handle.save_user(username=user_name,
                        userpasswd=user_passwd)
    # 记录日志功能
    msg = f'用户 [{user_name}] 注册成功!'
    user_logger.info(msg)
    return True, msg


# 用户登录接口
def login_interface(user_name, user_passwd):
    # 获取用户数据
    user_data_dic = db_handle.select_user(user_name)

    if user_data_dic:
        user_passwd = common.get_pwd_md5(user_passwd)
        if user_passwd == user_data_dic.get('password'):
            msg = f'用户 [{user_name}] 登录成功!'
            user_logger.info(msg)
            return True, msg
        else:
            msg = '用户名或密码错误'
            user_logger.warn(msg)
            return False, msg
    else:
        msg = '用户名或密码错误'
        user_logger.warn(msg)
        return False, msg


# 用户余额查询接口
def check_bal_interface(user_name):
    user_data_dic = db_handle.select_user(user_name)
    return user_data_dic['balance']
