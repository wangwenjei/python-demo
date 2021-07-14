"""
    程序入口文件
"""
import os
import sys

# 添加解释器环境变量
sys.path.append(os.path.dirname(__file__))

from core import src

if __name__ == '__main__':
    src.run()
