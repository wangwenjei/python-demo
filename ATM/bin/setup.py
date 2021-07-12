import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

# 想要在该目录执行导入需要将目录路径添加到环境变量中
from core import src
if __name__ == '__main__':
    src.run()

