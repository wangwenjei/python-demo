"""
    管理员接口
"""

from db import models


# 管理员注册接口
def admin_register_interface(username, password):
    # 判断用户是否存在
    admin_obj = models.Admin.select(name=username)

    if admin_obj:
        return False, '用户以存在'

    # 用户不存在则注册 调用类实例化得到对象并保存
    admin_obj = models.Admin(username=username,
                             password=password)
    # 对象调用save() 会将 admin_obj 传给 save 方法
    admin_obj.save()

    return True, '注册成功'


# 管理员登录接口
def admin_login_interface(username, password):
    # 判断用户是否存在
    admin_obj = models.Admin.select(username)

    if not admin_obj:
        return False, '不存在请注册'

    if password == admin_obj.pwd:
        return True, '登录成功'
    else:
        return False, '用户名或密码错误'


# 管理员创建学习接口
def create_school_interface(school_name, school_addr, login_name):
    # 查看学校是否存在
    school_obj = models.Admin.select(school_name)

    if school_obj:
        return False, '学习已注册'

    # 学校不存在则注册 实例化对象,通过管理员对象来创建学校
    admin_obj = models.Admin.select(login_name)
    # 由管理员来调用创建学校方法，并传入学校的名字与地址
    admin_obj.create_school(sch_name=school_name,
                            sch_addr=school_addr)

    return True, f'学校 [{school_name}] 创建成功'


# 管理员创建课程接口

# 管理员注册老师账户接口
def create_teacher_interface(teacher_name, login_name):
    # 查看该教师账户是否创建
    teahcer_obj = models.Admin.select(name=teacher_name)

    if teahcer_obj:
        return False, f'已教师[{teacher_name}] 创建了账户'

    admin_obj = models.Admin.select(name=login_name)
    admin_obj.create_teahcer(teacher_name=teacher_name,
                             teacher_pwd=123)

    return True, f'成功为[{teacher_name}]创建账户'
