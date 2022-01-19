import hmac
import base64
import hashlib

access_key = 'r0_GHWBaOY4cbuUfQHAOsj0KoGAo_648Xc1SYCfe'
secret_key = 'HVQvB-vB6w5HmwWZnIttXJ_DXyqCxC0HSPT56RSG'


def create_token(access_key, hub, streamTitle, ):
    data = "POST" + " " + "\nHost: " + "pili.qiniuapi.com" + "\nContent-Type: " + "application/json" + "\n\n" + \
           "/v2/hubs/{hub}/streams/{encodedStreamTitle}/saveas".format(hub=hub, encodedStreamTitle=streamTitle)

    accessKey = access_key
    sign = hmac.new(accessKey, data, hashlib.sha1).digest()
    # uth_token = base64.b64encode(bytes(json.dumps(auth).encode('utf-8')))

    encodedSign = base64.urlsafe_b64encode(sign)
    # authorization = 'Qiniu ' + accessKey + ':' + encodedSign
    # return authorization
    print(data)


# 直播空间名
hub = 'yihuibao-test'
# 流名
streamTitle = "yihuibao-test_20220106092540333_1102140"

create_token(access_key, hub, streamTitle)
