from interface import user_interface
from interface import bank_interface
from interface import shop_interface
from lib import common

# 全局变量，记录用户是否已登录
login_user = None


# 1、注册功能
def register():
    while True:

        # 接收用户输入信息
        user_name = input('请输入用户名:').strip()
        user_passwd = input('请输入密码:').strip()
        re_user_passwd = input('请确认密码').strip()

        if user_passwd == re_user_passwd:
            # 调用用户注册接口
            flag, msg = user_interface.register_interface(user_name, user_passwd)

            if flag:
                print(msg)
                break
            else:
                print(msg)

        else:
            print('密码不一致')


# 2、登录功能
def login():
    while True:

        user_name = input('请输入用户名:').strip()
        user_passwd = input('请输入密码:').strip()

        # 调用用户登录接口
        flag, msg = user_interface.login_interface(user_name, user_passwd)
        if flag:
            print(msg)

            # 修改全局 login_user 变量,记录用户是否登录
            global login_user
            login_user = user_name
            break
        else:
            print(msg)


# 3、查看账户余额
@common.login_auth
def check_balance():
    # 调用用户余额查询接口
    balance = user_interface.check_bal_interface(login_user)
    print(f'用户 [{login_user}] 的余额为: {balance}$')


# 4、提现功能
@common.login_auth
def withdraw():
    while True:
        money = input('请输入提现金额').strip()
        if not money.isdigit():
            print('输入不合法,请重新输入')
            continue

        # 调用用户余额查询接口
        flag, msg = bank_interface.withdraw_interface(username=login_user,
                                                      money=float(money))

        if flag:
            print(msg)
            break
        else:
            print(msg)
            break


# 5、充值功能
@common.login_auth
def repay():
    while True:
        top_up_money = input('请输入充值金额:').strip()

        # 判断用户输入种植金额合法性
        if not top_up_money.isdigit():
            print('请输入正确的金额')
            continue

        # 调用充值接口
        flag, msg = bank_interface.top_up_interface(
            username=login_user,
            money=float(top_up_money)
        )

        if flag:
            print(msg)
            break


# 6、转账功能
@common.login_auth
def transfer():
    while True:
        # 获取目标用户账号以及转账金额
        to_user = input('转账账户:').strip()
        money = input('转账金额:').strip()

        # 判断专账金额
        if not money.isdigit():
            print('请输入合法金额类型')
            continue

        # 调用转账接口
        flag, msg = bank_interface.tranfser_interface(username=login_user,
                                                      touser=to_user,
                                                      money=float(money))

        if flag:
            print(msg)
            break
        else:
            print(msg)


# 7、查看流水
@common.login_auth
def check_flow():
    # 调用查看账户流水接口
    flow_list = bank_interface.check_flow_interface(username=login_user)

    # 判断并打印流水信息
    print('====================  账户流水  ====================')
    if flow_list:
        for flow in flow_list:
            print(flow)
    else:
        print('暂无流水')
    print('====================    END    ====================')


# 8、购物功能
@common.login_auth
def shopping():
    # 这里使用枚举类型,仅做演示,不建议使用
    shop_list = [
        ['上海灌汤包', 30],  # 0
        ['海底捞', 399],  # 1
        ['广东凤爪', 28],
        ['香港地道鱼丸', 9999],
    ]

    # 初始化购物车
    shopping_car = {}  # {'商品名称': ['单价', '数量']]}

    while True:
        print('====================  购物商城  ====================')
        for index, shop in enumerate(shop_list):
            shop_name, shop_price = shop
            print(f'商品编号为:[{index}]',
                  f'商品名称:[{shop_name}]',
                  f'商品单价:[{shop_price}]')
        print('====================    END    ====================')

        # 接收用户输入的指令
        choice = input('请输入商品编号（是否结账输入y or n）: ').strip()

        # 当指令为y时
        if choice == 'y':
            if not shopping_car:
                print("购物车为为空,无需支付,请重新输入")
                continue

            # 调用支付接口
            flag, msg = shop_interface.shopping_interface(username=login_user,
                                                          shopping_car=shopping_car)

            if flag:
                print(msg)
                break
            else:
                print(msg)
                # 将商品添加到购物车并退出
                break

        if choice == 'n':
            if not shopping_car:
                print("购物车为空,无需加入购物车,请先添加到购物车!!!")
                continue

            # 调用添加购物车功能
            falg, msg = shop_interface.add_shop_car_interface(username=login_user,
                                                              shopping_car=shopping_car)
            if falg:
                print(msg)
                break

        if not choice.isdigit():
            print('请输入正确的编号')
            continue

        choice = int(choice)
        if choice not in range(len(shop_list)):
            print("请输入正确的编号")
            continue

        # 获取选择商品名称和价格
        shop_name, shop_price = shop_list[choice]

        # 添加商品到购物车
        if shop_name not in shopping_car:
            # 判断商品是否存在购物车,不存在则添加购物车 {'商品名称': ['单价', '数量']]}
            shopping_car[shop_name] = [shop_price, 1]
        else:
            # 当购物车存在此类商品则商品数加一
            shopping_car[shop_name][1] += 1

        print('当前购物车: ', shopping_car)


# 9、查看购物车
@common.login_auth
def check_shop_car():
    # 获取商城信息,并打印
    shop_car = shop_interface.check_shop_car_interface(username=login_user)
    print(shop_car)


# 10、管理员功能
# from core import admin


@common.login_auth
def admin_function():
    # 在函数内调用该功能,避免因循环导入造成报错
    from core import admin
    admin.admin_run()


# 创建函数功能字典
func_dic = {
    '0': ['退出', exit],
    '1': ['注册功能', register],
    '2': ['登录功能', login],
    '3': ['查看余额', check_balance],
    '4': ['提现功能', withdraw],
    '5': ['充值功能', repay],
    '6': ['转账功能', transfer],
    '7': ['查看流水', check_flow],
    '8': ['购物功能', shopping],
    '9': ['查看购物车', check_shop_car],
    '10': ['管理员功能', admin_function]
}


def run():
    while True:
        # 打印功能目录
        for k in func_dic:
            print(k, func_dic[k][0])

        user_instruction = input('输入需要执行的指令').strip()

        if not user_instruction.isdigit():
            print('==请输入数字指令==')
            continue

        if user_instruction in func_dic:
            func_dic[user_instruction][1]()
        else:
            print('请输入正确编号')
