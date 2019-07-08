from django.shortcuts import render, redirect, reverse
from .models import *
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.contrib.auth import login, logout, authenticate

# Create your views here.

# 限制登录装饰器
def checklogin(fun):
    # 注意填入被装饰函数拥有的参数(*args--可以有或者没有的参数)
    def check(requset, *args):
        username = requset.session.get("username")
        if username:
            return fun(requset, *args)
        else:
            return redirect(reverse('polls:userlogin'))
    return check



# 用户登录
def userlogin(request):
    if request.method == "GET":
        return render(request, "booktest/login.html")

    elif request.method == "POST":
        username = request.POST.get("username")
        # 1.使用cookies存储信息
        # 登录成功，存储cookie
        # response = redirect(reverse('polls:index'))
        # # set_cookie参数为键值对，第一个为键，第二个为值
        # response.set_cookie("username", username)
        # return response

        # 2.使用session进行存储
        request.session["username"] = username
        return redirect(reverse('polls:index'))




# 用户退出
def userout(request):
    # 依旧使用redirect获得页面，将页面中的cookie删除
    # response = redirect(reverse('booktest:index'))
    # response.delete_cookie("username")

    # 退出时session的删除
    request.session.flush()
    return redirect(reverse('booktest:index'))



# 主页
@checklogin
def index(request):

    username = request.session.get("username")
    # 判断是否读取到username，如果读取到进入首页，没有跳回登录界面
    if username:
        polls = PollsInfo.objects.all()
        return render(request, "booktest/pollIndex.html", locals())
    else:
        return redirect(reverse("polls:login"))

# 投票页面
@checklogin
def vote(request, id):
    if request.method == "GET":
        polls = PollsInfo.objects.get(pk=id)
        return render(request, "booktest/pollVote.html", {'polls': polls})
    elif request.method == "POST":
        num = request.POST.get("num")
        votes = VoteInfo.objects.get(pk=num)
        votes.num += 1
        votes.save()
        return redirect(reverse("polls:outvote", args=(id,)))


# 投票结果
@checklogin
def outvote(request, id):
    out = PollsInfo.objects.get(id=id)
    return render(request, "booktest/outvote.html", {"out":out})









