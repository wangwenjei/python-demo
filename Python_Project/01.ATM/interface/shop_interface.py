"""
    购物商城接口
"""
from interface import bank_interface
from db import db_handle
from lib import common

# 根据不同的接口类型传入不同的日志对象log_tye=
shop_logger = common.get_logger(log_type='shop')


# 商品结算接口
def shopping_interface(username, shopping_car):
    shopping_money = 0
    # 计算购物车消费总计
    for commodity_prices in shopping_car.values():  # dic.values()获取到字典所有值 [单价,商品数]
        prices = commodity_prices[0]
        money = commodity_prices[1]
        shopping_money += (prices * money)

    # 调用支付接口
    flag = bank_interface.pay_interface(username=username,
                                        money=shopping_money)

    if flag:
        msg = f'用户: [{username}] 支付 [{shopping_money}$] 成功, 准备发货!'
        shop_logger.info(msg)
        return True, msg

    msg = '支付失败:账户余额不足,请充值!!!'
    shop_logger.error(msg)
    return False, msg


# 商品添加购物车接口
def add_shop_car_interface(username, shopping_car):
    user_data_dir = db_handle.select_user(username)

    # {'海底捞': [399, 2], '广东凤爪': [28, 1]}

    shop_car = user_data_dir.get('shop_car')

    # 添加购物车
    for shop_name, price_number in shopping_car.items():
        # 获取每个商品添加个数
        count = price_number[1]

        # 计算购物车
        if shop_name in shop_car:
            # 统计 商品新增数 与 购物车已有商品数
            user_data_dir['shop_car'][shop_name][1] += count
        else:
            # 原购物车无该类商品则添加
            user_data_dir['shop_car'].update(
                {shop_name: price_number}
            )

    # 保存用户数据
    db_handle.update_user(user_data_dir)

    return True, '添加购物车成功'


# 查看购物车接口
def check_shop_car_interface(username):
    user_data_dic = db_handle.select_user(username)
    return user_data_dic.get('shop_car')
