"""
    学生接口
"""
from db import models


# 学生注册接口
def student_register_interface(stu_username, stu_password):
    """
    学生注册接口,存在返回False,不存在创建
    :param stu_username: 注册账户名
    :param stu_password: 账户密码
    :return:
    """
    # 查看账户是否被注册
    stu_obj = models.Student.select(name=stu_username)

    if stu_obj:
        return False, f'学生[{stu_username}] 已存在'

    # 不存在则创建用户
    stu_obj = models.Student(stu_uaername=stu_username,
                             stu_password=stu_password)
    stu_obj.save()

    return True, f'学生[{stu_username}] 注册成功'


# 学生选择校区接口
def choice_school_interface(school_name, login_user):
    """

    :param school_name: 学校名称
    :param login_user: 当前登录的学生账户名
    :return:
    """
    # 判断当前学生是否存在学校
    stu_obj = models.Student.select(name=login_user)

    if stu_obj.school:
        return False, f'你已经选择过[{stu_obj.school}]学校了!'

    stu_obj.add_school(school_name=school_name)
    return True, f'成功选择学校: {school_name}'


# 获取学生所在学校所有课程
def get_course_list_interface(student_name):
    stu_obj = models.Student.select(name=student_name)
    school_name = stu_obj.school
    # 查看学生是否选择过学校
    if not school_name:
        return False, '学生没有选择学校，请先选择学校'

    # 获取选择学校下的所有课程
    school_obj = models.School.select(name=school_name)
    course_list = school_obj.course_list
    if not course_list:
        return False, '该校区暂无课程，请先联系管理员创建'
    else:
        return True, course_list


# 选择课程接口
def choice_course_interface(course_name, login_user):
    stu_obj = models.Student.select(name=login_user)
    school_name = stu_obj.school

    # 查看课程是否存在
    if course_name in stu_obj.course_list:
        return False, '该课程已经选择过了!'

    stu_obj.add_course(course_name=course_name)
    return True, f'[{course_name}] -- 课程添加成功!'


# 查看成绩
def query_score_interface(login_user):
    stu_obj = models.Student.select(name=login_user)
    score_dict = stu_obj.score_dict
    if not score_dict:
        return False, '学生还未选择课程'
    else:
        return True, score_dict
