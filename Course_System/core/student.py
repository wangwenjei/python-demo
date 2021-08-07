"""
    学生视图层
"""


# 学生注册
def register():
    pass


# 学生登录
def login():
    pass


# 选择校区
def choice_school():
    pass


# 选择课程
def choice_cource():
    pass


# 查看分数
def check_core():
    pass


func_dic = {
    '0': ['退出', exit],
    '1': ['注册', register],
    '2': ['登录', login],
    '3': ['选择校区', choice_school],
    '4': ['选择课程', choice_school],
    '5': ['查看分数', check_core]
}


def student_view():
    while True:
        for k in func_dic:
            print(k, func_dic[k][0])

        choice = input('请输入学生功能指令:').strip()

        if choice not in func_dic:
            print('== 请输入规范的控制指令 ==')

        func_dic[choice][1]()
