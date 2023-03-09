import base64

s = '人生苦短，我学python！'
# 加密
b = base64.b64encode(s.encode('utf-8'))
print(b)

# 解密
c = base64.b64decode(b).decode('utf-8')
print(c)

# https://blog.csdn.net/weixin_44799217/article/details/125949538