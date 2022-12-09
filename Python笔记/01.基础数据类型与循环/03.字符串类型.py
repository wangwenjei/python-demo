"""
字符串类型: str
    作用: 记录描述性质的状态，名字、一段话
    定义: 用引号（''，""，''' '''，""" """，）包含的一串字符   
    
由数字组成的字符串，是字符串类型，不是int类型
int类型可以被转为str类型,但str类型不能被转为int类型


常用内置方法:
    去除字符串左右符号,默认去除空格
        str.lstrip() 去除左边 
        str.rstrip() 去除右边
        
   字符串切分,默认按空格,切分次数为所有
         str.split()  从左往右切分为列表
         str.rsplit()  从右往左切分为列表
             
    str.lower() 字符串全转换为小写
    str.upper() 字符串全转换为大写
    
    str.startswith()  查看字符串是否以某字符串开头	返回 True False
    str.endswith()    查看字符串是否以某字符串结尾    
    
    str.format()    格式化字符串
    str.len()   计算字符串长度
    str.join()  按某个分隔符,将一个所有元素为字符串的列表拼接成一个大的字符串
 
    str.()   替换字符串,参数依次为,被替换的字符串,要替换成的字符串,替换次数
    str.isdigit()   判断字符串是否由数字组成   返回 True False  
    
    str.encode('utf-8')   将某一编码类型的字符串修改为Byte类型
    str.decode('utf-8')   将Bytel类型数据转码为原编码类型的数据
    
    str.index('c',5)   获取字符串序列位置,可以定义查询的初始位置从哪个下标开始 

bytes(str,encoding='utf-8')  将某一编码类型的字符串修改为Byte类型
"""

age = 18
print(type(str(age)))  # ==> <class 'str'>
# 字符串之间可以相加，但仅限于str与str之间进行，
# 代表字符串的拼接，了解即可，不推荐使用，因为str之间的相加效率极低
print('my name is ' + 'wwj')

print(':'.join(['name', 'jason']))
x = ['name', 'wwj']
print(':'.join(x))  # ==> name:wwj

a = "hello world "

# 切片
print(a[-2])  # ==> l   字符串类型可以按索引取值
print(a[0:8:2])  # ==>  hlow   切片顾头不顾尾,步长为2
print(a[::-1])  # ==>   dlrow olleh  翻转字符串

# 成员运算
print('hello' in 'a')  # ==> False
print('hello' not in 'a')  # ==> True

print(a.strip('hello'))  # ==>  world  去除左侧hello字符
print(a.split('o', 2))  # ==> ['hell', ' w', 'rld ']   按照字符 o 对字符串切分, 切分2次

print(a.lower())  # ==> hello world
print(a.upper())  # =>> HELLO WORLD

print(a.startswith('hello'))  # ==> True
print(a.endswith('abc'))  # ==> False

res = "my name is {name},age is {age}".format(age=18, name='wwj')
print(res)  # ==> my name is wwj,age is 18

print(len(a))  # ==> 12

print(a.replace('hello', 'HELLO'))  # ==> HELLO world

print(a.isdigit())  # ==> False

aa = 'aa'.encode('utf-8')
print(aa, type(aa))  # ==> b'aa' <class 'bytes'>

bb = aa.decode('utf-8')
print(bb, type(bb))  # ==> aa <class 'str'>

a = "hello"
print(bytes(a, encoding='utf-8'))  # ==> b'hello'

print('abcdabcd'.index('c', 5))  # ==> 6
