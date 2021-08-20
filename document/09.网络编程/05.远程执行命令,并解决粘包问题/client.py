import socket
import struct

"""
粘包问题出现的原因
    1. TCP是流式协议, 数据像流水一样粘在一起,没有任何边界区分
    2. 收数据没收干净, 有残留, 就会与下一次的结果混淆在一起
    
不论是接收还是发送数据实际上都是先去本机的缓存做操作

解决粘包的思路:
    1. 先手固定长度的头: 解析出数据的描述信息,包括数据的总大小total_size
    2. 根据解析出的描述信息,接收真实的数据
        2.1: recv_size = 0, 循环接收, 每接收一次, recv_size+=接收的长度
        2.2: 直到 recv_size == total_size, 结束循环
"""

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8709))

while True:
    msg = input('输入命令>>>:').strip()
    if len(msg) == 0: continue
    client.send(msg.encode('utf-8'))

    header_size = client.recv(4)
    total_size = struct.unpack('i', header_size)[0]
    recv_size = 0
    while recv_size < total_size:
        recv_data = client.recv(1024)
        recv_size += len(recv_data)
        print(recv_data.decode('utf-8'), end='')
    else:
        print()

client.close()
