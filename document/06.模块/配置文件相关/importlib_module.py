from myfile import setting

# print(setting)  # ==> <module 'myfile.setting' from '/Users/shaun/Healife/python/python-demo/document/06.模块/配置文件相关/myfile/setting.py'>
# print(setting.name)  # ==> jason


# importlib高阶用法见app06
import importlib
res = 'myfile.setting'
res = importlib.import_module(res)
print(res)  # ==> <module 'myfile.setting' from '/Users/shaun/Healife/python/python-demo/document/06.模块/配置文件相关/myfile/setting.py'>
print(res.name)  # ==> jason