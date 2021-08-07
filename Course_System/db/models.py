"""
    存放类
"""

from db import db_handle


class Base:
    # 查看数据
    @classmethod
    def select(cls, name):  # School School_name
        """
        公共方法
        :param name: 接收需要查询的值,如用户名,学校名
        :return: 对象  or  None
        """
        obj = db_handle.select_data(cls, name=name)
        return obj

    # 保存数据 ---> 注册、保存、更新数据
    def save(self):
        # 让db_handler中的save_data 实现具体的数据存储
        db_handle.save_data(self)


class Admin(Base):
    def __init__(self, username, password):
        """

        :param username: 用户名
        :param password: 用户密码
        """
        self.name = username
        self.pwd = password

    def create_school(self, sch_name, sch_addr):
        """
        该方法内部来调用学校类实例化的得到对象，并保存

        :param sch_name: 学校名称
        :param sch_addr: 学校地址
        :return:
        """

        school_obj = School(sch_name, sch_addr)
        school_obj.save()

    def create_teahcer(self, teacher_name, teacher_pwd):
        teacher_obj = Tearch(teacher_name=teacher_name,
                             teacher_pwd=teacher_pwd)
        teacher_obj.save()


class School(Base):
    def __init__(self, name, addr):
        """
        # 必须写: self.name, 因为db_handler里面的select_data统一规范
        :param name: 学校名称
        :param addr: 学校地址
        """
        self.name = name
        self.addr = addr


class Course:
    pass


class Tearch(Base):
    def __init__(self, teacher_name, teacher_pwd):
        self.teacher_name = teacher_name
        self.teacher_pwd = teacher_pwd
