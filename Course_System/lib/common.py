"""
    存放公共方法
"""


# 多用户登录认证装饰器
def auth(role):
    from core import admin

    def login_auth(func):
        def wrapper(*args, **kwargs):
            if role == 'admin':
                if admin.admin_info['user']:
                    res = func(*args, **kwargs)
                    return res
                else:
                    admin.login()
            else:
                print('当前视图没有权限')

        return wrapper

    return login_auth
