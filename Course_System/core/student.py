"""
    学生视图层
"""
from interface import student_interface
from interface import common_interface
from lib import common

student_info = {
    'user': None
}


# 学生注册
def register():
    while True:
        stu_name = input('请输入账户名:').strip()
        stu_pwd = input('请输入密码:').strip()
        re_pwd = input('请确认密码').strip()

        if not stu_pwd == re_pwd:
            print('密码不一致请重新注册')
            continue

        flag, msg = student_interface.student_register_interface(stu_username=stu_name,
                                                                 stu_password=stu_pwd)

        if flag:
            print(msg)
            break
        else:
            print(msg)
            break


# 学生登录
def login():
    while True:
        stu_name = input('请输入登录账户:').strip()
        stu_pwd = input('请输入账户密码').strip()

        flag, msg = common_interface.login_interface(login_name=stu_name,
                                                     login_pwd=stu_pwd,
                                                     login_type='student')

        if flag:
            print(msg)
            student_info['user'] = stu_name
            break
        else:
            print(msg)
            break


# 选择校区
@common.auth('student')
def choice_school():
    while True:
        # 获取校区
        flag, sch_list_msg = common_interface.get_all_school_interface()
        if not flag:
            print(sch_list_msg)

        for index, school_name in enumerate(sch_list_msg):
            print(f'编号: {index}    学校名: {school_name}')

        choice_sch = input('请输入学校编号:').strip()

        if not choice_sch.isdigit():
            print('请输入合法指令')
            continue

        choice_sch = int(choice_sch)
        if choice_sch not in range(len(sch_list_msg)):
            print('请输入正确编号')
            continue

        # 获取学校名称
        school_name = sch_list_msg[choice_sch]
        flag, msg = student_interface.choice_school_interface(school_name=school_name,
                                                              login_user=student_info.get('user'))

        if flag:
            print(msg)
            break
        else:
            print(msg)
            break


# 选择课程
@common.auth('student')
def choice_cource():
    while True:
        # 获取当前登录学生所在学校的所有课程
        flag, course_list_msg = student_interface.get_course_list_interface(student_name=student_info.get('user'))

        if not flag:
            print(course_list_msg)

        for index, course_name in enumerate(course_list_msg):
            print(f'课程编号: {index}   课程名: {course_name}')

        choice_cou = input('请输入课程编号:').strip()

        if not choice_cou.isdigit():
            print('请输入合法指令')
            continue

        choice_cou = int(choice_cou)
        if choice_cou not in range(len(course_list_msg)):
            print('请输入合法指令')
            continue

        # 获取选择课程的名称
        course_name = course_list_msg[choice_cou]

        flag, msg = student_interface.choice_course_interface(course_name=course_name,
                                                              login_user=student_info.get('user'))

        if flag:
            print(msg)
            break
        else:
            print(msg)
            break


# 查看分数
@common.auth('student')
def check_core():
    while True:
        flag, msg = student_interface.query_score_interface(login_user=student_info.get('user'))
        if flag:
            print(msg)
            break
        else:
            print(msg)
            break


func_dic = {
    '0': ['退出', exit],
    '1': ['注册', register],
    '2': ['登录', login],
    '3': ['选择校区', choice_school],
    '4': ['选择课程', choice_cource],
    '5': ['查看分数', check_core]
}


def student_view():
    while True:
        print('=== 欢迎来到学生视图 ===')
        for k in func_dic:
            print(k, func_dic[k][0])

        choice = input('请输入学生功能指令:').strip()

        if choice not in func_dic:
            print('== 请输入规范的控制指令 ==')
        else:
            func_dic[choice][1]()


student_view()
