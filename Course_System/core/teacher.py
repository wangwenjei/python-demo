"""
    老师视图层
"""
from interface import common_interface
from interface import teacher_interface
from lib import common

teacher_info = {
    'user': None
}


# 老师登录
def login():
    while True:
        tea_user = input('请输入教师账户:').strip()
        tea_pwd = input('请输入密码:').strip()

        flag, msg = common_interface.login_interface(login_name=tea_user,
                                                     login_pwd=tea_pwd,
                                                     login_type='teacher')

        if flag:
            print(msg)
            teacher_info['user'] = tea_user
            break
        else:
            print(msg)
            break


# 查看教授课程
@common.auth('teacher')
def check_course():
    while True:
        flag, msg = teacher_interface.query_course_interface(login_user=teacher_info.get('user'))

        if flag:
            print(msg)
            break
        else:
            print(msg)
            break


# 选择教授课程
@common.auth('teacher')
def choice_course():
    while True:
        # 获取想要授课的校区
        sch_flag, sch_list_msg = common_interface.get_all_school_interface()
        if not sch_flag:
            print(sch_list_msg)

        for index, school_name in enumerate(sch_list_msg):
            print(f'编号: {index}    学校名: {school_name}')

        choice_sch = input('请输入选择的学校编号').strip()

        if not choice_sch.isdigit():
            print('请输入合法指令')
            continue

        choice_sch = int(choice_sch)
        if choice_sch not in range(len(sch_list_msg)):
            print('请输入合法指令')
            continue

        # 获取学校下有哪些课程,并打印出该校区课程信息
        school_name = sch_list_msg[choice_sch]
        cou_flag, course_list_msg = common_interface.get_all_course_interface(school_name=school_name)
        for index, course_name in enumerate(course_list_msg):
            print(f'编号: {index}    学校名: {course_name}')

        if not cou_flag:
            print(course_list_msg)

        choice_cou = input('请输入选择的课程编号:').strip()

        if not choice_cou.isdigit():
            print('请输入合法指令')
            continue

        choice_cou = int(choice_cou)
        if choice_cou not in range(len(course_list_msg)):
            print('请输入有效课程编号')
            continue

        course_name = course_list_msg[choice_cou]
        flag, msg = teacher_interface.add_course_interface(school_name=school_name,
                                                           course_name=course_name,
                                                           login_user=teacher_info.get('user'))

        if flag:
            print(msg)
            break
        else:
            print(msg)
            break


# 查看课程下学生
@common.auth('teacher')
def check_stu_from_course():
    while True:
        # 获取老师所有的课程
        flag, course_list_msg = teacher_interface.query_course_interface(login_user=teacher_info.get('user'))

        if not flag:
            print(course_list_msg)

        school_name_list = list(course_list_msg.keys())

        for school_index, school_name in enumerate(school_name_list):
            print(f'编号: {school_index}    学校名: {school_name}')

        choise_school = input('请输入学校编号').strip()
        choise_school = int(choise_school)

        school_name = school_name_list[choise_school]
        for course_index, course_name in enumerate(course_list_msg[school_name]):
            print(f'编号: {course_index}    课程名: {course_name}')

        choise_course = input('请输入课程编号').strip()
        choise_course = int(choise_course)

        # 获取相应课程下学生
        course_name = course_list_msg[school_name][choise_school]
        stu_flag, stu_list_msg = teacher_interface.query_student_inetrface(school_name=school_name,
                                                                           courser_name=course_name,
                                                                           login_user=teacher_info.get('user'))
        if stu_flag:
            print(stu_list_msg)

# 修改学生分数
@common.auth('teacher')
def change_score_from_student():
    pass


func_dic = {
    '0': ['退出', exit],
    '1': ['登录', login],
    '2': ['查看教授课程', check_course],
    '3': ['选择教授课程', choice_course],
    '4': ['查看课程下学生', check_stu_from_course],
    '5': ['修改学生分数', change_score_from_student]
}


def teacher_view():
    while True:
        print('=== 欢迎来到老师视图 ===')
        for k in func_dic:
            print(k, func_dic[k][0])

        choice = input('请输入老师功能指令:').strip()

        if choice not in func_dic:
            print('== 请输入规范的控制指令 ==')
        else:
            func_dic[choice][1]()


teacher_view()
