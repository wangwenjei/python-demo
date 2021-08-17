import socket

# 1.获取到一个基于TCP连接的对象
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2.服务端允许连接的网络
phone.bind(('127.0.0.1', 8085))  # 绑定服务端

# 3. 监听 5 指的是半连接池的大小
phone.listen(5)

# 4. 等待连接请求
conn, client_addr = phone.accept()

# 5. 收发消息
while True:
    data = conn.recv(1024)
    if len(data) == 0: break
    print('来自客户端发送的消息:', data.decode('utf-8'))
    conn.send(data.upper())

# 6. 关闭conn连接
conn.close()
