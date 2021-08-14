"""
    公共接口
"""
import os
from conf import settings
from db import models


# 登录接口
def login_interface(login_name, login_pwd, login_type):
    if login_type == 'admin':
        # 查看用户是否存在
        obj = models.Admin.select(name=login_name)

    elif login_type == 'student':
        obj = models.Student.select(name=login_name)

    elif login_type == 'teacher':
        obj = models.Tearch.select(name=login_name)

    else:
        return False, '登录角色不对，请输入角色'

    if obj:
        if login_pwd == obj.pwd:
            return True, f'用户 [{obj.name}] 登录成功'
        else:
            return False, '用户名或密码错误'
    else:
        return False, '用户名不存在请先注册!'


# 获取所有学校名
def get_all_school_interface():
    # 获取学校文件夹路径
    school_dir = os.path.join(
        settings.DB_PATH, 'School'
    )

    # 判断文件是否存在
    if not os.path.exists(school_dir):
        return False, '还未有学校被创建'

    # 若文件存在返回所有文件名
    return True, os.listdir(school_dir)


# 获取课程名
def get_all_course_interface(school_name):
    # 获取学校对象
    sch_obj = models.School.select(name=school_name)
    course_list = sch_obj.course_list

    if not course_list:
        return False, '该学校还未被创建课程'
    else:
        return True, course_list
