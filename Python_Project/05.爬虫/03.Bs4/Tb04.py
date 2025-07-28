"""
CSS选择器
"""
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

soup = BeautifulSoup(html_doc, 'lxml')

# print(soup.select("title"))  # [<title>The Dormouse's story</title>]
# print(soup.select("p:nth-of-type(3)"))  # [<p class="story">...</p>]

"1.通过tag标签逐层查找"
# print(soup.select('body a'))
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

# print(soup.select('html head title'))
# [<title>The Dormouse's story</title>]

"2.找到某个tag标签下的直接子标签"
# print(soup.select("head > title"))
# # [<title>The Dormouse's story</title>]
# print(soup.select("p > a"))
# # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
# print(soup.select("p>a:nth-of-type(2)"))
# # [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]
# print(soup.select("p>#link1"))
# # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]
# print(soup.select("body>a"))
# # []

"3.找到兄弟标签"
# print(soup.select("#link1 ~. sister"))
# # [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
#
# print(soup.select("#link1 + .sister"))
# # [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

"4.通过CSS类名查找"
# print(soup.select('.sister'))
# # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
#
# print(soup.select('[class~="sister"]'))
# # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

"5.通过tag的Id查找"
# print(soup.select('#link1'))
# # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]
#
# print(soup.select('a#link2'))
# # [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

"6.同意是否存在某个属性查找"
# print(soup.select('a[href]'))
# # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

"7.通过属性值查找"
# print(soup.select('a[href="http://example.com/elsie"]'))
# # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]
#
# print(soup.select('a[href^="http://example.com"]'))
# # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
#
# print(soup.select('a[href$="tillie"]'))
# # [<a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]
#
# print(soup.select('a[href*=".com/el"]'))
# # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]


"8.通过语言设置查找"

# multilingual_markup = """
#  <p lang="en">Hello</p>
#  <p lang="en-us">Howdy, y'all</p>
#  <p lang="en-gb">Pip-pip, old fruit</p>
#  <p lang="fr">Bonjour mes amis</p>
# """
# multilingual_soup = BeautifulSoup(multilingual_markup, 'lxml')
#
# print(multilingual_soup.select('p[lang|=en]'))
# # [<p lang="en">Hello</p>, <p lang="en-us">Howdy, y'all</p>, <p lang="en-gb">Pip-pip, old fruit</p>]

"====----===="

f1 = {'a', 'b', 'c'}
f2 = {'e', 'f', 'c'}

