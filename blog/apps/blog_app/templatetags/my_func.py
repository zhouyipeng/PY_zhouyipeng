"""
自定义模板表达式
扩展Django原有功能
"""

from django.template import library
from blog_app.models import Article, Tag, Category

register = library.Library()


# 获得文章创建日期
@register.simple_tag
def getlatestarticles(num=4):
    return Article.objects.order_by("-create_time")[:num]

# 获得回档日期
@register.simple_tag
def gettime(num=4):
    times = Article.objects.dates("create_time", "month", "DESC")[:num]
    print(times)
    return times

# 获得文章类别
@register.simple_tag
def getcategory():
    category = Category.objects.all()
    return category

# 获得标签
@register.simple_tag
def gettags():
    tags = Tag.objects.all()
    return tags

@register.filter
def mysplit(value):
    return value.split('.')

@register.filter
def myjoin(value, uvalue):
    return uvalue.join(value)

