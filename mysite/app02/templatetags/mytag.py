from django import template

register = template.Library()


# 自定义过滤器(参数只能有两个)
@register.filter(name='baby')
def my_sum(v1, v2):
    return v1 + v2


# 自定义标签(参数可以有多个)
@register.simple_tag(name='plus')
def index(a, b, c, d):
    return '%s-%s-%s-%s' % (a, b, c, d)


# 自定义inclusion_tag
# @register.inclusion_tag('app02/模板传值.html')
@register.inclusion_tag('app02/template_views/left_menu.html')
def left(n):
    data = ['第{}项'.format(i) for i in range(n)]
    return locals()
