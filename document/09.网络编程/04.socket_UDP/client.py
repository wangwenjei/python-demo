import socket

server_ip = '127.0.0.1'
server_port = 8086

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input('输入要发送的消息>>>:').strip()
    # 发消息
    client.sendto(msg.encode('utf-8'), (server_ip, server_port))
    # 收消息
    # data, server_addr = client.recvfrom(1024)
    # print(data.decode('utf-8'))
    res= client.recvfrom(1024)
    print(res)
