"""
    管理员视图层
"""
import pickle
from interface import admin_interface
from lib import common

admin_info = {
    'user': None
}


def logout():
    # from core import src
    print('=== 退出管理员视图 ===')
    # src.run()


# 管理员注册
def register():
    while True:
        username = input('请输入用户名:').strip()
        password = input('请输入用户密码').strip()
        re_password = input('请确认用户密码').strip()

        # 校验两次密码是否一致
        if password == re_password:
            falg, msg = admin_interface.admin_register_interface(
                username=username,
                password=password
            )
            if falg:
                print(msg)
                break
            else:
                print(msg)
                break
        else:
            print('密码不一致,请重新注册')


# 管理员登录
def login():
    while True:
        username = input('登录账户:').strip()
        passwd = input('登录密码:').strip()

        falg, msg = admin_interface.admin_login_interface(username=username,
                                                          password=passwd)

        if falg:
            print(msg)
            admin_info['user'] = username
            break
        else:
            print(msg)
            break


# 创建学校
@common.auth('admin')
def create_school():
    while True:
        sch_name = input('请输入学校名称:').strip()
        sch_addr = input('请输入学校地址:').strip()

        falg, msg = admin_interface.create_school_interface(school_name=sch_name,
                                                            school_addr=sch_addr,
                                                            login_name=admin_info.get('user'))

        if falg:
            print(msg)
            break
        else:
            print(msg)
            break


# 创建课程
@common.auth('admin')
def create_course():
    while True:
        # 选择不同的校区,创建不同的课程
        pass


# 注册讲师账户
@common.auth('admin')
def create_teacher():
    while True:
        tea_name = input('请输出教师姓名').strip()

        falg, msg = admin_interface.create_teacher_interface(teacher_name=tea_name,
                                                             login_name=admin_info.get('user'))

        if falg:
            print(msg)
            break
        else:
            print(msg)
            break


func_dic = {
    '0': ['退出', exit],
    '1': ['注册', register],
    '2': ['登录', login],
    '3': ['创建学校', create_school],
    '4': ['创建课程', create_course],
    '5': ['创建讲师', create_teacher]
}


def admin_view():
    while True:
        print('=== 欢迎来到管理员视图 ===')
        for k in func_dic:
            print(k, func_dic[k][0])

        choice = input('请输入管理员功能指令:').strip()

        if choice not in func_dic:
            print('== 请输入规范的控制指令 ==')
            continue
        else:
            func_dic[choice][1]()


admin_view()
