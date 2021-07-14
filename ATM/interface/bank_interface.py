"""
    银行相关业务接口
"""
from db import db_handle


# 提现接口(手续费5%)
def withdraw_interface(username, money):
    """
    :param username: 已登录用户的用户名
    :param money: 提现金额
    :return:
        True ,  成功提示
        False , 失败提示
    """
    # 获取用户数据
    user_data_dic = db_handle.select_user(username)

    # 获取用户账户余额
    user_balance = int(user_data_dic.get('balance'))

    # 提现本金加税费
    money2 = money * 1.05

    # 判断账户余额是否大于等于提现金额加税费
    if user_balance >= money2:

        # 用户提余额计算
        user_balance -= money2
        user_data_dic['balance'] = user_balance

        # 调用用户数据修改接口
        db_handle.update_user(user_data_dic)

        return True, f'用户 [{username}] 提现 [{money}$] 成功,手续费为: [{money2 - money}$]'
    else:
        return False, '账户余额不支持转账'
