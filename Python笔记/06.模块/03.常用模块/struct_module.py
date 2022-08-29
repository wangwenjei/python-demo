import struct

"""
该模块可以把一个类型，如数字，转成固定长度的bytes

'i' int类型   format requires -2147483648 <= number <= 2147483647 #这个是范围
"""

# 将一个数字转换为固定长度的bytes
x = struct.pack('i', 1024)
print(x, len(x))  # ==> b'\x00\x04\x00\x00' 4

# 将转换后的解压
q = struct.unpack('i', x)
print(q)  # ==> (1024,)
