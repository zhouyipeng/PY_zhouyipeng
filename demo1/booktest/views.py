from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import *

# Create your views here.

def index(request):
    # return HttpResponse('这是一个首页 <a href="/list/" >跳转到列表页</a> ')

    # 1.获取模板
    # temp1 = loader.get_template("booktest/index.html")
    # 2.使用模板渲染字典参数
    # result = temp1.render({})
    # 3.将渲染的结果返回
    # return HttpResponse(result)

    return render(request, "booktest/index.html", {})


def list(request):

    # temp = loader.get_template("booktest/list.html")
    books = BookInfo.objects.all()
    # result = temp.render({"books":books})
    # return HttpResponse(result)
    return render(request, "booktest/list.html", {"books": books})




def detail(request, num):
    # return HttpResponse('这是%s详情页 <a href="/" >跳转到首页</a> '%num)

    # temp = loader.get_template("booktest/detail.html")
    # # get()后id为填入的参数
    book = BookInfo.objects.get(id=num)
    # result = temp.render({"book":book})
    # return HttpResponse(result)
    return render(request, "booktest/detail.html", {"book": book})

def herodelete(request, id):
    hero = HeroInfo.objects.get(id=id)
    # 通过英雄获得书本id
    bookid = hero.book.id
    hero.delete()
    # return HttpResponse('删除成功')
    # return HttpResponseRedirect("/detail/" + str(bookid) + '/')
    return redirect( reverse("booktest:detail", args=(bookid,)))

# 添加英雄
def addhero(request, id):
    book = BookInfo.objects.get(id=id)
    if request.method == "GET":
        return render(request, "booktest/addhero.html", {"book":book})
    elif request.method == "POST":
        name = request.POST.get("heroname")
        content = request.POST.get("content")
        gender = request.POST.get("gender")
        h1 = HeroInfo()
        h1.name = name
        h1.centent = content
        h1.book = book
        h1.gender = gender
        h1.save()
        return redirect(reverse("booktest:detail", args=(id, )))
