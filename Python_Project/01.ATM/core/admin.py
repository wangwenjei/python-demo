from core import src
from interface import admin_interface


# 添加用户
def add_user():
    # 调用src下完整的用户注册功能
    src.register()


# 修改用户额度
def change_balance():
    while True:
        change_balance_user = input('请输入需要修改账户金额的账户:').strip()
        change_balance_money = input('请输入修改后的账户余额').strip()

        if not change_balance_money.isdigit():
            print('请输入正确的金额')
            continue

        flag, msg = admin_interface.change_balance_interface(target_user=change_balance_user,
                                                             target_user_balance=change_balance_money)

        if flag:
            print(msg)
            break
        else:
            print(msg)
            break


# 冻结账号
def lock_user():
    while True:
        lock_username = input('请输入冻结账户账号').strip()
        flag, msg = admin_interface.lock_user_interface(username=lock_username)

        if flag:
            print(msg)
            break
        else:
            print(msg)
            break


admin_func = {
    '0': ['退出', exit],
    '1': ['添加用户', add_user],
    '2': ['修改用户额度', change_balance],
    '3': ['冻结账户', lock_user]
}


# 主运行文件
def admin_run():
    while True:
        print('========== admin 功能 ==========')
        for i in admin_func:
            print(i, admin_func[i][0])

        user_instruction = input('请输入需要的指令:').strip()

        if not user_instruction.isdigit() or \
                not user_instruction in admin_func:
            print('请输入合法指令')
            continue

        admin_func[user_instruction][1]()
