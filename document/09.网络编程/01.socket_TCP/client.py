import socket

# 获取到一个基于TCP连接的对象
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接服务端,服务端的IP+端口
phone.connect(('127.0.0.1', 8085))

# 通信
# 发送消息
phone.send('Hello Jason 嗯'.encode('utf-8'))
# 接收消息
data = phone.recv(1024)
print('服务端返回的数据', data.decode('utf-8'))

# 关闭连接
phone.close()


"""
服务端返回的数据 HELLO JASON 嗯
"""