# -*- coding: utf-8 -*-
"""
批量拷贝文件
https://developer.qiniu.com/kodo/api/1250/batch

wordpress-wwj   华东浙江
hebei-wwj       华北河北  t1.txt t2.txt t3.txt
https://store-picss.medmeeting.com/00076ed3ebf6456894a0a2664a8111b4.jpeg
https://store-picss.medmeeting.com/000d2d89662148a8b6fbdc8f68326cde.jpeg
https://store-picss.medmeeting.com/000af09bf92849279ee89ae7425c1310.png
"""

from qiniu import Auth
from qiniu import BucketManager
import os

access_key = os.getenv('jasonQiNiuAK')
secret_key = os.getenv('jasonQiNiuSK')

bucket_name = 'hebei-wwj'
q = Auth(access_key, secret_key)
bucket = BucketManager(q)

url = 'https://store-pics.medmeeting.com/ZwxyhRPGQ0R6ngS88Ln03RSyoLmpvSvB_1668132373282'
key = 'webbucketImgCopyBackup/1911655/ZwxyhRPGQ0R6ngS88Ln03RSyoLmpvSvB_1668132373282'
ret, info = bucket.fetch(url, bucket_name, key)
print(info)
assert ret['key'] == key

"""
webbucketImgCopyBackup
bucketManager.fetch("https://store-pics.medmeeting.com/ZwxyhRPGQ0R6ngS88Ln03RSyoLmpvSvB_1668132373282", 
                    "yihuibao",
                    "webbucketImgCopyBackup/ZwxyhRPGQ0R6ngS88Ln03RSyoLmpvSvB_1668132373282");
 
"""
