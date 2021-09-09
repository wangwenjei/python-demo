login_tag = False


def check_login(func):
    def wrapper(*args, **kwargs):
        # global login_tag
        if login_tag:
            res = func(*args, **kwargs)
            return res
        else:
            print('请先登录')

    return wrapper


def login():
    while True:
        username = input('user_name>>>').strip()
        passwd = input('user_passwd').strip()

        if username == 'jason' and passwd == '123':
            print('登录成功')
            global login_tag
            login_tag = True
        else:
            print('用户名或密码失败')


@check_login
def a():
    print('功能函数A')


@check_login
def b():
    print('功能函数B')


@check_login
def c():
    print('功能函数C')


func_dic = {
    '0': ['退出', exit],
    '1': ['功能函数A', a],
    '2': ['功能函数A', b],
    '3': ['功能函数A', c],
    '4': ['登录', login]

}


def run():
    while True:
        for i in func_dic:
            print(i, func_dic[i][0])
        res = input('请输入功能指令').strip()

        func_dic[res][1]()


if __name__ == '__main__':
    run()
