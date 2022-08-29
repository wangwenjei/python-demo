import os
import sys

# 运行py脚本时获取 位置参数方法
# 	name = sys.argv[1]   获取第一个位置参数赋值给name


"""
    sys.path 下的目录为环境变量
"""
print(sys.path)

# 获取到当前文件的上上级目录并赋值给BASE_DIR
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# 将 BASE_DIR 添加到环境变量中
sys.path.append(BASE_DIR)

# 此时可以导入装饰器
import hello_python

hello_python.func()
