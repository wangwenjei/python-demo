"""
    数据处理层
"""
import os
import json
from conf import settings
from db.data_structure import user_data_structure


# 查看数据
def select_user(user_name):
    """
    查看用户数据,存在返回用户信息字典,不存在则返回None
    :param user_name: 用户名
    :return: None or user_data_dic
    """

    # 接收接口层传入的用户名,拼接用户数据保存文件路径
    user_data_path = os.path.join(
        settings.USER_DATA_PATH, f'{user_name}.json'
    )

    # 校验用户数据文件是否存在,存在则查看用户数据
    if os.path.exists(user_data_path):
        with open(user_data_path, mode='rt', encoding='utf-8') as f:
            user_data_dic = json.load(f)
            return user_data_dic

    # 用户不存在返回None,默认不return 返回None
    # return None


# 保存数据
def save_user(**kwargs):
    user_name = kwargs['username']
    user_passwd = kwargs['userpasswd']

    # 获取数据结构,并填充数据
    user_dic = user_data_structure.user_dic
    user_dic['username'] = user_name
    user_dic['password'] = user_passwd

    # 数据存储文件路径
    user_data_path = os.path.join(
        settings.USER_DATA_PATH, f'{user_name}.json'
    )

    # 保存用户数据
    with open(user_data_path, mode='wt', encoding='utf-8') as f:
        # ensure_ascii=False让文件中的中文数据，显示更美观
        json.dump(user_dic, f, ensure_ascii=False)


# 用户修改数据
def update_user(user_data_dic):
    user_name = user_data_dic.get('username')

    user_data_path = os.path.join(
        settings.USER_DATA_PATH, f'{user_name}.json'
    )

    with open(user_data_path,mode='wt',encoding='utf-8') as f:
        json.dump(user_data_dic,f,ensure_ascii=False)
