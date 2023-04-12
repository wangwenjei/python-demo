import requests

# 请求连接
url = 'http://127.0.0.1:5000/user/info'
data = {'user': 'jason'}

# url = 'http://127.0.0.1:5000/user/info?user=jason' 当get参数较少时，可讲URL与Parmas写到一起

req = requests.get(url=url, params=data)
print(req.json())

"""
参考：https://blog.csdn.net/Dch19990825/article/details/87730252
GET请求参数：
    url：请求URL，必填；
    params: 请求参数，选填；
    headers：头信息，选填
    proxies：用于用户代理，访问服务器会以代理的IP访问服务器，可掩盖本机IP，选填
    verify：SSL证书验证是否跳过，用于访问有些页面出现证书验证错误的时候，选填
    timeout：通过timeout能够保证在指定时间内返回响应值，否则报错，单位：秒，选填
    cookies：显式的将cookies添加到请求头的cookies中，选填

"""
