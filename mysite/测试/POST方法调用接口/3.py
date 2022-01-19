# -*- coding: utf-8 -*-
from qiniu import QiniuMacAuth, http, urlsafe_base64_encode
import json

# 七牛账号 AK、SK
access_key = 'r0_GHWBaOY4cbuUfQHAOsj0KoGAo_648Xc1SYCfe'
secret_key = 'HVQvB-vB6w5HmwWZnIttXJ_DXyqCxC0HSPT56RSG'


def saveasPlayBack(access_key, secret_key, hub, streamTitle, body):
    """
    录制直播回放
    https://developer.qiniu.com/pili/api/2777/save-the-live-playback
    :param access_key: 公钥
    :param secret_key: 私钥
    :param hub: 直播空间
    :param streamTitle: 流名
    :param body: 请求体

    :return:
        200 {
            "fname": "<Fname>",
            "persistentID": "<PersistentID>"
        }
        612 {
            "error": "stream not found"
        }
        619 {
            "error": "no data" // 没有直播数据
        }
    """
    auth = QiniuMacAuth(access_key, secret_key)
    print('==')
    print(auth.__dict__)
    print('==')


    # 流名base64安全编码
    EncodedStreamTitle = urlsafe_base64_encode(streamTitle)

    # 请求URL
    url = f'http://pili.qiniuapi.com/v2/hubs/{hub}/streams/{EncodedStreamTitle}/saveas'

    # 发起POST请求
    ret, res = http._post_with_qiniu_mac(url, body, auth)
    headers = {"code": res.status_code, "reqid": res.req_id, "xlog": res.x_log}

    # 格式化响应体
    Headers = json.dumps(headers, indent=4, ensure_ascii=False)
    result = json.dumps(ret, indent=4, ensure_ascii=False)
    return Headers, result

# 直播空间名
hub = 'yihuibao-test'

# 流名
streamTitle = "yihuibao-test_20200310182423543_102867"
# streamTitle = "yihuibao-test_20220106092540333_1102140"

# 请求体
body = {
    "format": "mp4",
    "pipeline": "lIve-vedio-mq",
    "start": 1583837871,
    "end": 1583840707,
    "firstTsType": 3
}

headers, result = saveasPlayBack(access_key, secret_key, hub, streamTitle, body)
print(f'{headers}\n{result}')
