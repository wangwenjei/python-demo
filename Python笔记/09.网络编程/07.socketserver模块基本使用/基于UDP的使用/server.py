import socketserver


class MyRequestHandle(socketserver.BaseRequestHandler):
    def handle(self) -> None:
        """
        print(self.request)
        print(self.client_address)
        ===>
            (b'ls', <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_DGRAM, proto=0, laddr=('127.0.0.1', 8888)>)
            ('127.0.0.1', 65148)
        """
        client_data = self.request[0]
        server = self.request[1]
        client_address = self.client_address
        server.sendto(client_data.upper(), client_address)


s = socketserver.ThreadingUDPServer(('127.0.0.1', 8888), MyRequestHandle)
s.serve_forever()
