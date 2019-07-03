from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *

# Create your views here.

def index(request):
    # return HttpResponse('这是一个首页 <a href="/list/" >跳转到列表页</a> ')
    # 1.获取模板
    temp1 = loader.get_template("booktest/index.html")
    # 2.使用模板渲染字典参数
    result = temp1.render({})
    # 3.将渲染的结果返回
    return HttpResponse(result)


def list(request):

    temp = loader.get_template("booktest/list.html")
    books = BookInfo.objects.all()
    result = temp.render({"books":books})
    return HttpResponse(result)




def detail(request, num):
    # return HttpResponse('这是%s详情页 <a href="/" >跳转到首页</a> '%num)

    temp = loader.get_template("booktest/detail.html")
    # get()后id为填入的参数
    book = BookInfo.objects.get(id=num)
    result = temp.render({"book":book})
    return HttpResponse(result)