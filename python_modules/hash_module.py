import hashlib

# 选择加密算法 md5 sha1 sha256 sha512 ....
m = hashlib.md5()

# 添加字符串进行加密 可多次拼接 相当于对 Abcd1234 加密
m.update('Abcd'.encode('utf-8'))
m.update('1234'.encode('utf-8'))

# 取出加密后的值
res = m.hexdigest()
print(res)  # ===> 325a2cc052914ceeb8c19016c091d2ac

### 密码加盐

c = hashlib.md5()

#   为密码  Abcd1234  加盐
m.update('天王盖地虎'.encode('utf-8'))
m.update('Abcd'.encode('utf-8'))
m.update('宝塔镇河妖'.encode('utf-8'))
m.update('1234'.encode('utf-8'))

res1 = m.hexdigest()
print(res1)  # ===> ce1073cf3bc13b26863087e613c971df

