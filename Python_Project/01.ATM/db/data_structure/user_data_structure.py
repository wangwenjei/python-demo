# 用户数存储结构
user_dic = {
    'username': None,  # 用户名
    'password': None,  # 用户密码
    'balance': 10000.0,  # 用户存款
    'flow': [],  # 用于记录用户流水的列表
    'shop_car': {},  # 用于记录用户购物车
    'locked': False  # locked：用于记录用户是否被冻结   False: 未冻结   True: 已被冻结
}
