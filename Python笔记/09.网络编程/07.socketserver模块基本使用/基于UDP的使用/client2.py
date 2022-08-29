import socket

server_ip = '127.0.0.1'
server_port = 8888
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input('>>>:').strip()

    client.sendto(msg.encode('utf-8'), (server_ip, server_port))
    data = client.recvfrom(1024)

    print(data[0].decode('utf-8'))
