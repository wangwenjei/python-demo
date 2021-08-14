class Base:
    @classmethod
    def select(cls, username):
        print(username)

    def save(self):
        print(self.__dir__())
        print(self.__dict__)


class Admin(Base):
    def __init__(self, user, pwd):
        self.user = user
        self.pwd = pwd


obj = Admin('wwj', 123)
obj.save()
obj.select(username='www')
