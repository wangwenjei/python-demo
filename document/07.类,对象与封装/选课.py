class School:
    school_name = 'QingHua'

    def __init__(self, nickname, addr):
        self.nickname = nickname
        self.addr = addr
        self.clesses = []

    def related_class(self, class_obj):
        self.clesses.append(class_obj)

    def check_class(self):
        print(self.nickname.center(60, "="))
        for class_obj in self.clesses:
            class_obj.check_course()


class Class():
    def __init__(self, name):
        self.name = name
        self.course = None

    def related_course(self, course_name):
        self.course = course_name

    def check_course(self):
        print('%s %s' % (self.name, self.course))


# 创建学习
school_obj1 = School('清华第一附属中学(北京)', '北京')
school_obj2 = School('清华第二附属中学(上海)', '上海')

# 创建班级
class_obj1 = Class('三年级一班')
class_obj2 = Class('三年级二班')
class_obj3 = Class('五年级一班')

# 学校关联班级
school_obj1.related_class(class_obj1)
school_obj1.related_class(class_obj2)
school_obj2.related_class(class_obj3)

# 为班级关联一门课程
class_obj1.related_course('Python')
class_obj2.related_course('Linux')
class_obj3.related_course('Go')

# 查看班级开设的课程信息
school_obj1.check_class()
school_obj2.check_class()
