"""
    存放配置信息
"""
import os

BACE_PATH = os.path.dirname(os.path.dirname(__file__))

USER_DATE_PATH = os.path.join(
    BACE_PATH,'db','user_data'
)

print(USER_DATE_PATH)

