"""
    老师接口
"""
from db import models


# 添加课程
def add_course_interface(school_name, course_name, login_user):
    teacher_obj = models.Tearch.select(name=login_user)
    course_dict = teacher_obj.teacher_course_dict

    # 判断是否有校区
    if course_dict.get(school_name):
        # 判断该校区下课程是否重复选择
        if course_name in course_dict[school_name]:
            return False, f'{course_name} 选择过该课程'
    else:
        course_dict[school_name] = []

    teacher_obj.add_course(school_name=school_name,
                           course_name=course_name)
    teacher_obj.save()

    return True, f'成功为 {school_name} 添加课程 {course_name}'


# 查看课程
def query_course_interface(login_user):
    teacher_obj = models.Tearch.select(name=login_user)
    course_dict = teacher_obj.teacher_course_dict

    if course_dict:
        return True, course_dict
    else:
        return False, '教师还未选择课程'


# 获取课程下学生信息
def query_student_inetrface(school_name, courser_name, login_user):
    teacher_obj = models.Tearch.select(name=login_user)

    return True, [school_name,courser_name,login_user]
