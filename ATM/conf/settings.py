"""
    存放配置信息
"""
import os

# 获取项目根目录路径

BACE_PATH = os.path.dirname(os.path.dirname(__file__))

# 获取user_data文件夹目录路径
USER_DATA_PATH = os.path.join(
    BACE_PATH,'db','user_data'
)





