import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('127.0.0.1', 8086))

while True:
    # 收消息
    data, client_addr = server.recvfrom(1024)
    print(data.decode('utf-8'))
    # 发消息
    server.sendto(data.upper(), client_addr)

