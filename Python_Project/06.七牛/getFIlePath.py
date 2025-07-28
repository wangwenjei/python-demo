# -*- coding: utf-8 -*-
import os

from qiniu import Auth
from qiniu import BucketManager


# 获取文件路径
class QiNiuBackend(object, ):

    def __init__(self, AK, SK):
        q = Auth(access_key=AK, secret_key=SK)
        self.bucket = BucketManager(q)

    def list(self, bucket_name, file_name, prefix=None, marker=None, limit=1000, delimiter=None, isBreak=False):
        """
            前缀查询:
            1. 首次请求 marker = None
            2. 无论 err 值如何，均应该先看 ret.get('items') 是否有内容
            3. 如果后续没有更多数据，err 返回 EOF，marker 返回 None（但不通过该特征来判断是否结束）
            具体规格参考:
            https://developer.qiniu.com/kodo/api/list

            Args:
                bucket:     空间名
                prefix:     列举前缀
                marker:     列举标识符
                limit:      单次列举个数限制
                delimiter:  指定目录分隔符
                isBreak:    查询到第一个文件后是否继续查询,默认False继续查询

            Returns:
                list对象,list内保存文件的具体路径

        """

        eof = False
        fileList = []
        while eof is False:
            """对空间全文循环检索"""
            ret, eof, info = self.bucket.list(bucket_name, prefix, marker, limit, delimiter)
            marker = ret.get('marker')
            file_list = ret.get('items')

            # 对文件过滤
            for file_info in file_list:
                name = file_info.get('key')

                if name.endswith(file_name) is True:  # 判断文件是否存在,存在添加到fileList
                    fileList.append(name)

                if isBreak is True and len(fileList) == 1:  # isBreak为True 且 已查询到一个值 结束循环
                    eof = True

        return fileList


if __name__ == '__main__':
    AK = os.getenv('jasonQiNiuAK')
    SK = os.getenv('jasonQiNiuSK')

    wyAK = os.getenv('wyQiNiuAK')
    # wySK = os.getenv('wyQiNiuSK')

    a = QiNiuBackend(AK=AK, SK=SK)
    cc = a.list(bucket_name='jasonwang-configfile', file_name='1.txt')
    print(cc)

    # b = QiNiuBackend(AK=wyAK, SK=wySK)
    # dd = b.list(bucket_name='wy-vide-file', file_name='1717804680_1717837459.mp4')
    # print(dd)
    # print(AK)
    # print(os.environ.get('jasonQiNiuAK'))
