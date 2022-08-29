import socket
import time


client = socket.socket()
client.connect(('127.0.0.1', 8899))

while True:
    client.send('hello world 001'.encode('utf-8'))
    time.sleep(0.5)

    data = client.recv(1024)
    print(data.decode('utf8'))

