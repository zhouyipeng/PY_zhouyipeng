"""
自定义模板表达式
扩展Django原有功能
"""

from django.template import library
from blog_app.models import Article

register = library.Library()

@register.simple_tag
def getlatestarticles(num=4):
    return Article.objects.order_by("-create_time")[:num]