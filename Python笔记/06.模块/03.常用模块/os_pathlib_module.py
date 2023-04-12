"""
os 文件和路径操作功能库
pathlib Py3.5后支持的 文件路径处理库
"""
import os

# 执行系统命令
os.system('touch ./add.txt')  # Hello Python 返回值为错误码 0为成功

# 获取某一文件夹下所有子文件以及子文件夹的名字
print(os.listdir(r'../../../ATM'))

# 统计某个目录文件大小,单位为字节
print(os.path.getsize(r'../../../ATM'))

# 删除一个文件
os.remove('./add.txt')

# 给一个文件重命名
# os.rename('old_name','new_name')

# 环境变量(规定 key 与 value 必须都为字符串 )
os.environ['aaa'] = '111'
print(os.environ['aaa'])  # 111

# 获取文件路径
print(os.path.dirname('/Users/python/python-demo/03.常用模块/os_pathlib_module.py'))
# ===>  /Users/python/python-demo/03.常用模块

# 获取最后一级文件名
print(os.path.basename('/Users/python/python-demo/03.常用模块/os_pathlib_module.py'))
# ===> os_pathlib_module.py

# 只能判断文件是否存在
print(os.path.isfile(r'os_pathlib_module.py'))  # True

# 判断文件夹是否存在
print(os.path.isdir(r'../../../ATM'))  # True

# 判断文件 或 文件夹是否存在
print(os.path.exists(r'logging_module'))  # True

# 把字符拼接成路径,以 / 为起始,
print(os.path.join('/a', '/', 'b', 'c.txt'))  # /b/c.txt

# 获取当前文件上一级目录
print(os.path.dirname(__file__))

import pathlib

# 获取当前文件路径
print(pathlib.Path(__file__))

# .parent 获取文件上一级路径
print(pathlib.Path(__file__).parent)
