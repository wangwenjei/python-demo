import socketserver

"""
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8111))
server.listen(5)

while True:
    conn, client_addr = server.accept()

    while True:
        try:
            data = conn.recv(1024)
            if len(data) == 0: break
            conn.send(data.upper())
        except Exception:
            break

    conn.close()

"""


class MyRequestHandle(socketserver.BaseRequestHandler):
    def handle(self) -> None:  # 函数名必须要叫 handle
        """
        print(self.request)  # 如果是TCP协议,self.request 等同于 conn
        print(self.client_address)
        ===>
            <socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 8888), raddr=('127.0.0.1', 63120)>
            ('127.0.0.1', 63120)
        """
        # 第二件事:  拿到链接对象与其进行通信循环
        while True:
            try:
                data = self.request.recv(1024)
                if len(data) == 0: break
                self.request.send(data.upper())
            except Exception:
                break


# ThreadingTCPServer 线程
# 第一件事: 循环的从半连接池中取出链接请求,与其建立双向链接请求,拿到链接对象
s = socketserver.ThreadingTCPServer(('127.0.0.1', 8811), MyRequestHandle)
s.serveforever()
# 等同于
# while True:
#     conn, client_addr = server.accept()
#     启动一个线程(conn, client_addr)
