import socket

s = socket.socket()  # 创建 socket 对象
host = socket.gethostname()
prot = 8888

s.connect((host, prot))
print(s.recv(1024))
# s.recv(1024)
# s.close()
