from interface import user_interface

# 1、注册功能
def register():
    while True:
        user_name = input('请输入用户名:').strip()
        user_passwd = input('请输入密码:').strip()
        re_user_passwd = input('请确认密码').strip()

        if user_passwd == re_user_passwd:

            pass
            # user_interface.register_interface()
        else:
            print('密码不一致')


# 2、登录功能
def login():
    print('登录功能')


# 3、查看余额
def check_balance():
    print('查询余额功能')


# 4、提现功能
def withdraw():
    print('提现功能')


# 5、还款功能
def repay():
    print('还款功能')


# 6、转账功能
def transfer():
    pass


# 7、查看流水
def check_flow():
    pass


# 8、购物功能
def shopping():
    pass


# 9、查看购物车
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


