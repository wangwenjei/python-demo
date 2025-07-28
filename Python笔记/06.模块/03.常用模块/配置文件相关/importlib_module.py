from myfile import setting

print(
    setting)  # ==> <module 'myfile.setting' from '/Users/shaun/Healife/python/python-demo/document/06.模块/配置文件相关/myfile/setting_logging.py'>
print(setting.name, type(setting.name))  # ==> jason <class 'str'>
print(setting.hobby, type(setting.hobby))  # ==>['Python', 'Go', 'Java'] <class 'list'>

# importlib高阶用法见app06
import importlib

res = 'myfile.setting'
res = importlib.import_module(res)
print(
    res)  # ==> <module 'myfile.setting' from '/Users/shaun/Healife/python/python-demo/document/06.模块/配置文件相关/myfile/setting_logging.py'>
print(res.name, type(res.name))  # ==> jason <class 'str'>
print(res.hobby, type(res.hobby))  # ==> ['Python', 'Go', 'Java'] <class 'list'>
