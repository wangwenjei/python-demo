"""
    银行相关业务接口
"""
from db import db_handle
from lib import common

# 根据不同的接口类型传入不同的日志对象log_tye=
bank_logger = common.get_logger(log_type='bank')


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

        # 记录流水
        flow = f'用户 [{username}] 提现 [{money}$] 成功,手续费为: [{money2 - money}$]'
        user_data_dic['flow'].append(flow)

        # 调用用户数据修改接口
        db_handle.update_user(user_data_dic)

        # 记录日志
        bank_logger.info(flow)

        return True, flow
    else:
        return False, '账户余额不支持转账'


# 充值接口
def top_up_interface(username, money):
    # 获取用户信息
    user_date_dic = db_handle.select_user(username)

    # 计算用户充值后账户余额
    user_date_dic['balance'] += money

    # 记录流水
    flow = f'用户 [{username}] 成功充值 [{money}$]'
    user_date_dic['flow'].append(flow)

    # 调用数据修改功能存储用户数据
    db_handle.update_user(user_date_dic)

    bank_logger.info(flow)

    return True, flow


# 转账接口
def tranfser_interface(username, touser, money):
    """
    判断用户是否存在,存在触发转账否则返回用户不存在
    判断用户余额是否支持转账,支持则转账否则账户余额不足
    :param username: 当前登录账户账号
    :param touser: 目标用户账户账号
    :param money: 转账金额
    :return:
    """
    # 获取登录用户以及目标用户数据信息
    login_user_data_dic = db_handle.select_user(username)
    to_user_data_dic = db_handle.select_user(touser)

    # 判断目标用户是否存在
    if not to_user_data_dic:
        return False, '目标用户不存在'

    # 判断账户余额大于等于转账金额则触发转账操作
    if login_user_data_dic['balance'] >= money:
        login_user_data_dic['balance'] -= money
        to_user_data_dic['balance'] += money

        # 记录流水
        flow_user = f'向用户 [{touser}] 成功转账 [{money}$],'
        login_user_data_dic['flow'].append(flow_user)

        flow_touser = f'用户 [{username}] 转入 [{money}$] ,'
        to_user_data_dic['flow'].append(flow_touser)

        # 调用数据修改接口,保存用户修改数据
        db_handle.update_user(login_user_data_dic)
        db_handle.update_user(to_user_data_dic)

        return True, flow_user
    return False, '转账失败,当前账户余额不足'


# 查看账户流水
def check_flow_interface(username):
    user_data_dic = db_handle.select_user(username)
    return user_data_dic.get('flow')


# 支付接口
def pay_interface(username, money):
    """

    :param username: 登录用户账户
    :param money: 购物车金额总计
    :return:
        True : 支付成功
        False : 支付失败
    """
    user_data_dic = db_handle.select_user(username)

    # 判断用户账户余额是否足够商品结算
    if user_data_dic.get('balance') >= money:
        # 商品结算
        user_data_dic['balance'] -= money

        # 记录流水
        flag = f'用户 [{username}] 总计消费 [{money}$]'
        user_data_dic['flow'].append(flag)

        # 保存用户数据
        db_handle.update_user(user_data_dic)

        return True
    return False
