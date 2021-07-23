def func(*args, **kwargs):
    print(args, kwargs)


def user(user_name, age):
    func(user_name, age)


func(1, 2, 3, name='a', age='18')
# (1, 2, 3) {'name': 'a', 'age': '18'}

user('wwj', 18)
