import socket
import subprocess
import struct
import json

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
            if len(data) == 0:
                # Unix系统h中,一旦data收到的是空,意味着是一种异常的行为: 客户端非法断开了链接
                break

            # 执行命令并接受结果
            obj = subprocess.Popen(data.decode('utf-8'),
                                   shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
            stdout_res = obj.stdout.read()
            stderr_res = obj.stderr.read()
            total_size = len(stdout_res) + len(stderr_res)

            # 头信息
            header = {
                'filename': '继续教育数据分析入库.txt',
                'total_size': total_size,
                'md5': 'ansdk12ednsla1280'
            }

            # 将头信息先通过json模块格式化数据,再将格式化后的数据转为bytes类型
            json_str = json.dumps(header)
            json_str_bytes = json_str.encode('utf-8')

            # 将转为bytes后的头信息,并将长度数字转为固定长度的bytes类型
            header_size = struct.pack('i', len(json_str_bytes))

            # 先把头的长度发过去
            conn.send(header_size)

            # 发送真正的头部信息
            conn.send(json_str_bytes)

            # 发送真实数据内容
            conn.send(stdout_res)
            conn.send(stderr_res)
        except Exception:
            break
    # 关闭当前的链接
    conn.close()
