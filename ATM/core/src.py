from interface import user_interface
from interface import bank_interface
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

        # 调用用户余额查询接口
        flag, msg = bank_interface.withdraw_interface(username=login_user,
                                                      money=float(money))

        if flag:
            print(msg)
            break
        else:
            print(msg)
            break


# 5、还款功能
@common.login_auth
def repay():
    print('还款功能')


# 6、转账功能
@common.login_auth
def transfer():
    pass


# 7、查看流水
@common.login_auth
def check_flow():
    pass


# 8、购物功能
@common.login_auth
def shopping():
    pass


# 9、查看购物车
@common.login_auth
def check_shop_car():
    pass


# 10、管理员功能
def admin():
    pass


# 创建函数功能字典
func_dic = {
    '0': ['退出', exit],
    '1': ['注册功能', register],
    '2': ['登录功能', login],
    '3': ['查看余额', check_balance],
    '4': ['提现功能', withdraw],
    '5': ['还款功能', repay],
    '6': ['转账功能', transfer],
    '7': ['查看流水', check_flow],
    '8': ['购物功能', shopping],
    '9': ['查看购物车', check_shop_car],
    '10': ['管理员功能', admin]
}


def run():
    while True:

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


run()
