"""
    银行相关业务接口
"""
from db import db_handle


# 提现接口(手续费5%)
def withdraw_interface(username, money):
    # 获取用户数据
    user_data_dic = db_handle.select_user(username)

    # 获取用户账户余额
    user_balance = int(user_data_dic.get('balance'))

    # 提现本金加税费
    money2 = money * 1.05

    if user_balance >= money2:
        user_balance -= money2
        user_data_dic['balance'] = user_balance
        db_handle.update_user(user_data_dic)


        return True, f'用户 [{username}] 提现 [{money}$] 成功,手续费为: [{money2 - money}$]'
    else:
        return False, '账户余额不支持转账'
