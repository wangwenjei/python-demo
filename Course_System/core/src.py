"""
    用户视图层 主视图
"""

from core import admin
from core import student
from core import teacher

func_dic = {
    '0': ['退出', exit],
    '1': ['管理员功能', admin.admin_view],
    '2': ['学生功能', student.student_view],
    '3': ['老师功能', teacher.teacher_view],
}


def run():
    while True:

        for k in func_dic:
            print(k, func_dic[k][0])

        choice = input('请输入功能编号:').strip()

        if choice.isdigit() or choice not in func_dic:
            print('== 请输入规范的指令 ==')
            continue


run()