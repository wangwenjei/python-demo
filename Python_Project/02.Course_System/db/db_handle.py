"""
    数据处理层
"""
import os
import pickle
from conf import settings


def save_data(obj):
    # print(obj)  # ==> <db.models.Admin object at 0x7ff9f4e426a0>
    """
    拼接数据存放路径
        获取对象的保存文件夹路径, 以类名 当做 文件夹的名字
        obj.__class__: 获取当前对象的类
        obj.__class__.__name__: 获取类的名字
    """
    class_name = obj.__class__.__name__
    user_dir_path = os.path.join(
        settings.DB_PATH, class_name
    )

    # 判断文件是否存在,不存在即穿件
    if not os.path.exists(user_dir_path):
        os.mkdir(user_dir_path)

    # 拼接当前用户的pickle文件路径,， 以用户名作为文件名
    user_path = os.path.join(
        user_dir_path, obj.name
    )

    # 将对象通过pickle序列化后写入文件
    with open(user_path, mode='wb', ) as f:
        pickle.dump(obj, f)


def select_data(obj, name):  # 调用类,name(user_name,school_name)
    """
    公共查询接口 当接收的是username就查询用户是否存在,当接收的是schoolname就查询学校是否存在

    :param obj: 实例化对象
    :param name: 接收需要查询参数
    :return: 对象数据 or None
    """
    # 通过cls获取类名, 并且拼接不同类保存的数据路径
    class_name = obj.__name__
    user_path = os.path.join(
        settings.DB_PATH, class_name, name
    )

    if os.path.exists(user_path):
        with open(user_path, mode='rb') as f:
            obj = pickle.load(f)
            return obj
