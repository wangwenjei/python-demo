from app06 import settings
import importlib


def sed_all(content):
    for path_str in settings.NOTIFY_LIST:  # app06.notify.email.Email
        # module_path = app06.notify.email  class_name = Email
        module_path, class_name = path_str.rsplit('.', maxsplit=1)

        # 利用字符串导入模块
        # module = <module 'app06.notify.email' from '/Users/shaun/Healife/python/mysite/app06/notify/email.py'>
        module = importlib.import_module(module_path)  # 等同于 from app06.notify import email

        # 利用反射获取类名
        # cls = <class 'app06.notify.email.Email'>
        cls = getattr(module, class_name, None)  # Email  QQ  Wechat

        # 生成类的对象,类名加括号调用
        obj = cls()

        # 利用鸭子类型直接调用send方法
        res = obj.send(content)

        print(res)
        '''
            ===>
                Email通知: 端午放假三天
                QQ通知: 端午放假三天
                Wechat通知: 端午放假三天
        '''
