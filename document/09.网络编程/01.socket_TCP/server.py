import socket

# socket.AF_INET 基于网络通信
# socket.SOCK_STREAM 流式协议(TCP协议)
# socket.SOCK_DGRAM  数据报协议(UDP协议)
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 获取到一个基于TCP连接的对象

# 服务端允许连接的网络
phone.bind(('127.0.0.1', 8085))  # 绑定服务端

# 5 指的是半连接池的大小
phone.listen(5)  # 监听

# 等待连接请求
conn, client_addr = phone.accept()

print(conn)
print('客户端IP和端口', client_addr)

# 收消息  1024 - 4096 就足够了
data = conn.recv(1024)  # 最大接收数据量为1024Bytes, 收到的结果是Bytes类型数据

print('来自客户端发送的消息', data.decode('utf-8'))
# 发消息,将收到的data消息转为大写发回
conn.send(data.upper())

# 关闭conn连接
conn.close()

"""
<socket.socket fd=5, 
    family=AddressFamily.AF_INET, 
    type=SocketKind.SOCK_STREAM, 
    proto=0, laddr=('127.0.0.1', 8085), 
    raddr=('127.0.0.1', 56698)
    >
客户端IP和端口 ('127.0.0.1', 56698)
来自客户端发送的消息 Hello Jason 嗯
"""
