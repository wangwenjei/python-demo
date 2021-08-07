"""
    老师视图层
"""


# 老师登录
def login():
    pass


# 查看教授课程
def check_course():
    pass


# 选择教授课程
def choice_course():
    pass


# 查看课程下学生
def check_stu_from_course():
    pass


# 修改学生分数
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
        for k in func_dic:
            print(k, func_dic[k][0])

        choice = input('请输入老师功能指令:').strip()

        if choice not in func_dic:
            print('== 请输入规范的控制指令 ==')

        func_dic[choice][1]()
