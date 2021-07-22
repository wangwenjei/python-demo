"""
    admin功能相关接口
"""

from lib import common
from db import db_handle

# 根据不同的接口类型传入不同的日志对象log_tye=
admin_logger = common.get_logger(log_type='admin')


# 修改额度接口
def change_balance_interface(target_user, target_user_balance):
    user_data_dir = db_handle.select_user(target_user)

    if user_data_dir:
        user_data_dir['balance'] = target_user_balance

        db_handle.update_user(user_data_dir)

        msg = f'管理员修改用户:[{target_user}] 账户余额修改为 [{target_user_balance}$]'
        admin_logger.info(msg)
        return True, msg

    else:
        msg = f'查询无 [{target_user}] 用户 '
        admin_logger.error(msg)
        return False


# 冻结账户接口
def lock_user_interface(username):
    user_data_dir = db_handle.select_user(username)
    if user_data_dir:
        user_data_dir['locked'] = True
        db_handle.update_user(user_data_dir)

        msg = f'管理员冻结用户[{username}]'
        admin_logger.log(msg)
        return True,msg

    else:
        msg = f'冻结账户[{username}]不存在'
        admin_logger.error(msg)
        return False, msg
