import re

html = """
<!DOCTYPE html>
<html>
<head>
<title> 这是一个标题呀 </title>
</head>
<body>

<li>
    <div class="s">作者：微叶梧桐<br />大小：11.89MB<br>等级：<em class="lstar3"></em><br>更新：2021-08-25</div>
    <a href="/Shtml101221.html"><img src="/files/article/image/101/101221/101221s.jpg" onerror="this.src='/modules/article/images/nocover.jpg'">《四重分裂》全集</a>
    <div class="u">    作为个高智商精神分裂，墨檀表示自己压力很大。    而一款名为【无罪之界】的游戏对他而言则是个减压的好地方。    混乱中立的他轻浮而率性而为，是无数不可控事件的...</div>
    <div><a style="font-weight: normal;" href="/du/101/101221/">最新章节：第一千二百零六章：用不用？</a></div>
</li>

</body>
</html>
"""


# 去除所有HTML标签, 并匹配出所有 xx:xx 格式的信息
def all_label():
    re_all = re.compile('<[^>]+>')
    s = re_all.sub('', html)
    s_list = re.findall('[^\s].*：.*', s)

    print(s_list)  # ==> ['作者：微叶梧桐大小：11.89MB等级：更新：2021-08-25', '最新章节：第一千二百零六章：用不用？']


# 只保留img标签
def img_label():
    re_img = re.findall('<[^>]*>', html)
    for label in re_img:
        if 'img' in label:
            print(label)
            # ==> <img src="/files/article/image/101/101221/101221s.jpg" onerror="this.src='/modules/article/images/nocover.jpg'">


# 过滤出所有div标签下的内容
def div_label():
    # 先过滤出所有div标签及其标签内容
    re_div = re.findall('<[^>]*>+.*', html)
    for label in re_div:
        if 'div' in label:
            # 匹配出标签下的内容
            re_div_text = re.compile('<[^>]+>')
            s = re_div_text.sub('', label)
            print(s)
            """ ==>
            作者：微叶梧桐大小：11.89MB等级：更新：2021-08-25
            作为个高智商精神分裂，墨檀表示自己压力很大。    而一款名为【无罪之界】的游戏对他而言则是个减压的好地方。    混乱中立的他轻浮而率性而为，是无数不可控事件的...
            最新章节：第一千二百零六章：用不用？
            """


# 打印页面所有标签,展示页面布局
def label_format():
    format = re.findall('<[^>]+>', html)
    print(format)
    # ['<!DOCTYPE html>', '<html>', '<head>', '<title>', '</title>', '</head>', '<body>', '<li>', '<div class="s">', '<br />', '<br>', '<em class="lstar3">', '</em>', '<br>', '</div>', '<a href="/Shtml101221.html">', '<img src="/files/article/image/101/101221/101221s.jpg" onerror="this.src=\'/modules/article/images/nocover.jpg\'">', '</a>', '<div class="u">', '</div>', '<div>', '<a style="font-weight: normal;" href="/du/101/101221/">', '</a>', '</div>', '</li>', '</body>', '</html>']


