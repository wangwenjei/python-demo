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

"标签"
# print(soup.find('b'))  # <b class="boldest" id="bbb">The Dormouse's story</b>
# print(soup.find_all('b'))  # [<b class="boldest" id="bbb">The Dormouse's story</b>]

"正则"
# print(soup.find(re.compile('^b')))
# print(soup.find_all(re.compile('^b')))

"列表"
# print(soup.find_all(['a', 'b']))

"True"
# print(soup.find(True))
# print(soup.find_all(True))

# for tag in soup.find_all(True):
#     print(tag.name)

"方法"

# def class_but_no_id(tag):
#     """返回只有class属性,没有id属性的标签"""
#     return tag.has_attr('class') and not tag.has_attr('id')


# print(soup.find_all(class_but_no_id))

# "find_all"
"name"
# print(soup.find_all(name=re.compile('^t')))

"keyword"
# print(soup.find_all(id='link2'))
# print(soup.find_all(href=re.compile('elsie'), id=re.compile('^link')))
# print(soup.find_all(id=True))

# 有些tag属性在搜索不能使用,比如HTML5中的 data-* 属性:
# data_soup = BeautifulSoup('<div data-foo="value">foo!</div>', 'lxml')
# print(data_soup.find_all(attrs={"data-foo": "value"}))

"CSS查找"
# print(soup.find_all('a',class_='sister')) #查找类为sister的a标签
# print(soup.find_all('a',class_='sister ssss')) #查找类为sister和sss的a标签，顺序错误也匹配不成功
# print(soup.find_all(class_=re.compile('^sis'))) #查找类为sister的所有标签


# 查找类为sister的a标签
# print(soup.find_all('a', class_="sister"))
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

# 查找类为sister和sss的a标签，顺序错误也匹配不成功
# print(soup.find_all('a', class_="sister ssss"))
# []

# 查找类为包含 itl 的所有标签
# print(soup.find_all(class_=re.compile('itl')))


# def has_six_characters(css_class):
#     return css_class is not None and len(css_class) == 6
#
#
# print(soup.find_all(class_=has_six_characters))

"多class 属性"
css_soup = BeautifulSoup('<p class="body strikeout"></p>', 'lxml')
# print(css_soup.find_all("p", class_="strikeout"))  # [<p class="body strikeout"></p>]
# print(css_soup.find_all("p", class_="body"))  # [<p class="body strikeout"></p>]
# print(css_soup.find_all("p", class_="body strikeout"))  # [<p class="body strikeout"></p>]

# print(css_soup.find_all("p", class_="body strikeout"))  # [<p class="body strikeout"></p>]
# print(css_soup.find_all("p", class_="strikeout body"))  # []

"#2.5、text: 值可以是：字符，列表，True，正则"
# print(soup.find_all(string='Elsie'))  # ['Elsie']
# print(soup.find_all(string=["Tillie", "Elsie", "Lacie"]))  # ['Elsie', 'Lacie', 'Tillie']
# print(soup.find_all('a', string='Elsie'))  # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]

"limit"
# print(soup.find_all('a', limit=2))

"recursive"
# print(soup.find_all('title'))
# print(soup.find_all('title', recursive=False))


# print(soup.find_all('p'))
# print(soup.find_all('html', recursive=False))


# print(soup.find_all('a'))
# print(soup('a'))
#
# print(soup.title.find_all(text=True))
# print(soup.title(text=True))

"""
find
"""

# print(soup.find_all('title', limit=1))
# print(soup.find('title'))
#
# print(soup.find("nosuchtag"))
#
# print(soup.head.title)
# print(soup.find('head').find('title'))


# print(soup.select("p:nth-of-type(3)"))


"=="
from pyecharts.charts import Bar

bar = (
    Bar()
    .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
    .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
)
a = bar.render()
print(a)
