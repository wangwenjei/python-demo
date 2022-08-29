import socket

# 获取到一个基于TCP连接的对象
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 连接服务端,服务端的IP+端口
phone.connect(('127.0.0.1', 8086))

# 收发消息
while True:
    msg = input('输入要发送的消息>>>:').strip()
    if len(msg) == 0: continue
    phone.send(msg.encode('utf-8'))
    data = phone.recv(1024)
    print('服务端返回的数据:', data.decode('utf-8'))

# 关闭连接
phone.close()
