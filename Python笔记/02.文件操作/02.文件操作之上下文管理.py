"""
with 上下文管理
    with语法可以同时打开多个文件,并在结束时自动关闭文件回收资源
"""

# 读取a.txt 和 b.txt 文件
with open(r'./file/a.txt', mode='rt', encoding='utf-8') as f1, \
        open(r'file/b.txt', mode='rt', encoding='utf-8') as f2:
    res1 = f1.read()
    res2 = f2.read()
    print('这是a.txt: %s' % res1)  # ==> 这是a.txt: AAAA
    print('这是b.txt: %s' % res2)  # ==> 这是b.txt: BBBB

# 读取a.txt文件写入到c.txt文件
with open(r'file/a.txt', mode='rt', encoding='utf-8') as f1, \
        open(r'file/c.txt', mode='wt', encoding='utf-8') as f2:
    res = f1.read()
    f2.write(res)

# 读取多行文本,并拼接
with open(r'file/write.txt', mode='rt', encoding='utf-8') as f:
    res = f.readlines()
    old_num = ''
    for i in res:
        old_num += i.strip('\n') + '+'
    print(old_num.strip('+'))  # ===> aa+bb+cc

# b模式使用
with open(r'file/a.txt', mode='rb') as f:
    res = f.read().decode('utf-8')
    print(res)

# b模式是用bytes类型写入数据,写入时需要利用encode转字符集写入
with open(r'file/a.txt', mode='rb') as f1, \
        open(r'file/b_write.txt', mode='wb') as f2:
    res = f1.read()
    f2.write(res)

with open(r'file/b1_write.txt', mode='wb') as f:
    f.write('世界,你好'.encode('utf-8'))

"""
"""

# 实现复制文件功能
with open(r'file/img_1.png', mode='rb') as f1, \
        open(r'file/img_2.png', mode='wb') as f2:
    res = f1.read()
    f2.write(res)

""" 文件过大循环读取文件 """
# 方法一: 一字节大小为单位分隔
with open(r'file/img_1.png', mode='rb') as f1, \
        open(r'file/img_2.png', mode='wb') as f2:
    while True:
        res = f1.read(1024)  # 每次读取1024个字节
        if len(res) == 0:
            break
        f2.write(res)

# 方法二: 以行为单位做分隔;缺点是当一行内容过大时,会导致一次性读入到内存的数据量过大
with open(r'file/img_1.png', mode='rb') as f1, \
        open(r'file/img_3.png', mode='wb') as f2:
    for i in f1:
        f2.write(i)

"""
f.readline()  # 一次读一行
f.readlines()  # 将文件读取放到列表, 列表每个元素放的是文件每一行的内容

read() 与 readlines(), 都是一次性将内容读入到内存, 如果内容过大会导致内存溢出,
                      若想将内容全部读入内存,则必须分多次读入,有两种实现方式:
                        一: while循环, 二: for循环
                        
f.writelines()	将列表中的内容写到文件中
"""

with open(r'file/write.txt', mode='rt', encoding='utf-8') as f:
    while True:
        res = f.readline().strip('\n')
        if len(res) == 0:
            break
        print(res)

# flush 刷新,强制将文件写入到硬盘,多数情况下不使用
with open(r'file/d.txt', mode='wt', encoding='utf-8') as f:
    f.write('哈哈哈')
    f.flush()

"""
文件指针操作:
    指针移动的单位都是以bytes为单位.
    只有一种情况特殊:
        t 模式下的 read(n), n代表字符个数
        
        
f.seek(n,模式):  n指的是移动的字节个数,只有0模式可以再t下使用; 1,2必须在b模式下使用
                模式:
                    0: 参照物是文件开头位置  f.seek(3,0)
                    1: 参照物是当前指针所在位置  f.seek(9,1)
                    2: 参照物是文件末尾位置,应该倒着移动 f.seek(-5,2)
"""
