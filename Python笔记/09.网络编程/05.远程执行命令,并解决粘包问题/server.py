import socket
import subprocess
import struct

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8709))
server.listen(5)

# 循环的从半连接池中取出链接请求,与其建立创建双向链接,拿到链接对象
while True:
    conn, client_addr = server.accept()

    # 拿到链接对象,与其进行通信循环
    while True:
        try:
            data = conn.recv(1024)
            if len(data) == 0: break

            obj = subprocess.Popen(data.decode('utf-8'),
                                   shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
            stdout_res = obj.stdout.read()
            stderr_res = obj.stderr.read()

            # 将返回的结果统计数据长度,并将长度数字转为固定长度的bytes类型
            total_size = len(stdout_res) + len(stderr_res)
            header = struct.pack('i', total_size)
            # 发送的是头部信息
            conn.send(header)

            # 发送真实数据内容
            conn.send(stdout_res)
            conn.send(stderr_res)


        except Exception:
            break
    server.close()
