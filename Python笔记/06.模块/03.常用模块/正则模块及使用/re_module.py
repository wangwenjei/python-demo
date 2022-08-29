import re

"""
正则表达式
"""

# re.findall 匹配所有字符
"""
    \w  匹配字母或数字或下划线或汉字
    \W  匹配非字母或数字或下划线或汉字
    
    \s  匹配任意空白字符 等价于 [\t \n \r \f]
    \S  匹配任意空白字符
    
    \d  匹配任意数字 等价于 [0-9]
    \D  匹配任意非数字
    
    \b 匹配单词的开始或结束
    \B 匹配不是单词开头或结束的位置


    ^  匹配字符串开头, 在[]内表示取反
    $  匹配字符串末尾
    
    .  匹配除了 \n(换行符) 之外的任意字符  指定 re.DOTALL 之后才能匹配换行符
    [^x] 匹配除了x以外的任意字符

# 重复匹配：| . | * | ? | .* | .*? | + | {n,m} |
    *  左侧字符重复0次或无穷次 性格贪婪
    +  左侧字符重复1次或无穷次 性格贪婪
    ?  左侧字符重复0次或1次 性格贪婪
    {n,m}  左侧字符重复n次到m次 性格贪婪
    .* 

    []  匹配指定字符 []内^ 代表取反
    ()  匹配
"""
print(re.findall('\d', 'abc123_*()-='))  # ['1', '2', '3']


print(re.findall('a.b', 'a\nb acdb acb', re.DOTALL))  # ['a\nb', 'acb']

# 匹配所有包含小数在内的数字
print(re.findall('\d+\.?\d*', "asdfasdf123as1.13dfa12adsf1asdf3"))  # ['123', '1.13', '12', '1', '3']

print(re.findall('a[0-9]b', 'a1b a*b a-b a=b'))  # ['a1b']
print(re.findall('a[^0-9]b', 'a1b a*b a-b a=b'))  # ['a*b', 'a-b', 'a=b']

# 获取 : 右边所有的值
print(re.findall(':.*', "项目:appserver")[1])  # ==> appserver
print(re.findall(':.*', "项目:appserver")[0].split(':')[1])  # ==> appserver
