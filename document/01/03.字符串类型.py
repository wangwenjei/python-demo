"""
字符串类型: str
    作用：记录描述性质的状态，名字、一段话
    定义：用引号（''，""，''' '''，""" """，）包含的一串字符   
    
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
 
    str.replace()   替换字符串,参数依次为,被替换的字符串,要替换成的字符串,替换次数
    str.isdigit()   判断字符串是否由数字组成   返回 True False  
"""

age = 18
print(type(str(age)))  # ==> <class 'str'>
# 字符串之间可以相加，但仅限于str与str之间进行，
# 代表字符串的拼接，了解即可，不推荐使用，因为str之间的
# 相加效率极低
print('my name is ' + 'wwj')

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

x = ['name', 'wwj']
print(':'.join(x))  # ==> name:wwj

print(a.replace('hello', 'HELLO'))  # ==> HELLO world

print(a.isdigit())  # ==> False
