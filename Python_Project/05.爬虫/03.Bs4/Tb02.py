html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p id="my p" class="title"><b id="bbb" class="boldest">The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup
import re

soup = BeautifulSoup(html_doc, 'lxml')
# soup=BeautifulSoup(open('a.html'),'lxml')

# print(soup.p)  # 存在多个相同的标签则只返回第一个
# print(soup.a)

"获取标签名称"
# print(soup.p.name)

"获取标签属性"
# print(soup.p.attrs)  # ==> {'id': 'my p', 'class': ['title']}
# print(soup.p.attrs['class'])

"获取标签内容"
# 打印第一个p标签内容,不存在返回None
# print(soup.p.string, type(soup.p.string))  # ==> The Dormouse's story <class 'bs4.element.NavigableString'>
# print(soup.p.text, type(soup.p.text))  # ==> The Dormouse's story <class 'str'>


# 循环打印所有标签内容, stripped_strings 可去除多余空白行
# for string in soup.strings:
# for string in soup.stripped_strings:
#     print(string)


"""
如果tag包含了多个子节点,tag就无法确定.string方法应该调用哪个子节点的内容;此时.string的输出结果是None,
如果只有一个子节点那么就输出该子节点的文本,比如下面这种结构,soup.p.string 返回None, 但soup.p.strings可找到所有文本
"""

# h2 = """
# <p id='list-1'>
#     哈哈哈哈
#     <a class='sss'>
#         <span>
#             <h1>aaaa</h1>
#         </span>
#     </a>
#     <b>bbbbb</b>
# </p>
# """
# s2 = BeautifulSoup(h2, 'lxml')
# print(s2.p.string)
# for line in s2.p.stripped_strings:
#     print(line)


"嵌套选择"
# print(soup.head.title.string)  # The Dormouse's story
# print(soup.body.a.string)  # Elsie

"子节点,子孙节点"
# print(soup.p.contents)  # [<b class="boldest" id="bbb">The Dormouse's story</b>]
# print(soup.p.children)  # <list_iterator object at 0x1050c4280>
#
# for i, child in enumerate(soup.p.children):
#     print(i, child)
#
# # print(soup.p.descendants)  # 获取子孙节点,p下所有的标签都会选择出来
# for i, child in enumerate(soup.p.descendants):
#     print(i, child)

"父节点,祖先节点"
# print(soup.a.parent)
# print(soup.a.parents)
# for l in soup.a.parents:
#     print('======>')
#     print(l)
#     print('======>')
#     print('')
#     print('')
#     print('')

"兄弟节点"
print(soup.a.next_sibling)  # 下一个兄弟节点
print(soup.a.previous_sibling)  # 上一个兄弟节点

print(list(soup.a.next_siblings))  # 下面的兄弟们=>生成器对象
# [',\n', <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, ' and\n', <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>, ';\nand they lived at the bottom of a well.']

# print(soup.a.previous_siblings)  # 上面的兄弟们=>生成器对象
# print(list(soup.a.previous_siblings))  # ['Once upon a time there were three little sisters; and their names were\n']
