import json
import requests
from qiniu import Auth, urlsafe_base64_encode, QiniuMacAuth

access_key = 'r0_GHWBaOY4cbuUfQHAOsj0KoGAo_648Xc1SYCfe'
secret_key = 'HVQvB-vB6w5HmwWZnIttXJ_DXyqCxC0HSPT56RSG'

hub = 'yihuibao-test'
encodedStreamTitle = "yihuibao-test_20220106092540333_1102140"

data = "POST /v2/hubs/{hub}/streams/{encodedStreamTitle}/saveas\nHost: pili.qiniuapi.com".format(hub=hub,
                                                                                                 encodedStreamTitle=encodedStreamTitle)


# 生成token
def create_token(data):
    q = Auth(access_key, secret_key)
    sign = q.token(data=data)
    encodedSign = urlsafe_base64_encode(sign)
    return "Qiniu " + access_key + ":" + encodedSign


def req():
    url = '{host}/v2/hubs/{hub}/streams/{encodedStreamTitle}/saveas'.format(host='https://pili.qiniuapi.com', hub=hub,
                                                                            encodedStreamTitle=encodedStreamTitle)
    headers = {
        "Host": "pili.qiniuapi.com",
        "Authorization": create_token(data),
        "Content-Type": "application/json"
    }
    vlaue = {
        "format": "mp4",
        "pipeline": "lIve-vedio-mq",
    }
    response = requests.post(url, data=json.dumps(vlaue), headers=headers)
    return response


res = req()
print(res)
