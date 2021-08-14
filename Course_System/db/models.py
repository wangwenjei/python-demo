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

    def create_course(self, school_obj, course_name):
        # 调用课程类，实例化创建课程
        course_obj = Course(course_name=course_name)
        course_obj.save()

        # 2.获取当前学校对象，并将课程添加到课程列表中
        school_obj.course_list.append(course_name)

        # 3.更新学校数据
        school_obj.save()

    def create_teahcer(self, teacher_name, teacher_pwd):
        """
        内部调用老师类实例化得到对象并保存
        :param teacher_name: 教师账户名
        :param teacher_pwd: 教师账户密码
        :return:
        """
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
        # 存储校区下创建的课程
        self.course_list = []


class Student(Base):
    def __init__(self, stu_uaername, stu_password):
        """

        :param stu_uaername:
        :param stu_password:
        """
        self.name = stu_uaername
        self.pwd = stu_password
        # 每个学生只能有一个校区
        self.school = None
        # 一个学生可以选择多门课程
        self.course_list = []
        # 学生课程分数
        self.score_dict = {}  # {"course_name": 0}

    def add_school(self, school_name):
        self.school = school_name
        self.save()

    def add_course(self, course_name):
        # 学生课程列表添加课程
        self.course_list.append(course_name)
        # 为课程设置初始分数,默认为0
        self.score_dict[course_name] = 0
        self.save()


class Course(Base):
    def __init__(self, course_name):
        self.name = course_name


class Tearch(Base):
    def __init__(self, teacher_name, teacher_pwd):
        self.name = teacher_name
        self.pwd = teacher_pwd
        self.teacher_course_dict = {}  # {school_name:[course1,course2]}

    def add_course(self, school_name, course_name):
        self.teacher_course_dict[school_name].append(course_name)

    def get_student(self,):
        pass

