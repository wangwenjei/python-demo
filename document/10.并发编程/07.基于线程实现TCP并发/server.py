import socket
from threading import Thread
from multiprocessing import Process, set_start_method

server = socket.socket()  # 括号内不加参数默认是TCP协议
server.bind(('127.0.0.1', 8899))
server.listen(5)


def task(conn):
    # 通信循环
    while True:
        try:
            data = conn.recv(1024)
            if len(data) == 0: break
            print(data.decode('utf-8'))
            conn.send(data.upper())
        except ConnectionError as e:
            break

    conn.close()


# 链接循环
while True:
    conn, client_addr = server.accept()

    # 线程实现并发
    t = Thread(target=task, args=(conn,))
    t.start()

# # 进程实现并发
# set_start_method('fork')
# while True:
#     conn, cline_addr = server.accept()
#     p = Process(target=task, args=(conn,))
#     p.start()
