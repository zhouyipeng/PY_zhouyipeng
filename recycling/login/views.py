from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views.generic import View
from .models import *
from django.contrib.auth import login, logout, authenticate

# Create your views here.

# 主页
def index(request):
    return render(request, 'recycling/index.html')

# 注册
def register(request):
    if request.method == "GET":
        return render(request, 'recycling/register.html')
    elif request.method == "POST":
        if request.POST.get("agreed"):
            username = request.POST.get("username")
            pwd1 = request.POST.get("password")
            pwd2 = request.POST.get("password2")
            if pwd1 == pwd2:
                try:
                    peo1 = RecyclingUser.objects.create_user(username=username, password=pwd1)
                    peo1.save()
                    return render(request, 'recycling/login.html', {'error': '注册成功'})
                except:
                    return render(request, 'recycling/register.html', {'error': '账号已存在'})
            else:
                return render(request, 'recycling/register.html', {'error': '两次密码不一致'})
        else:
            return render(request, 'recycling/register.html', {'error':'请同意服务协议'})


# 用户登录
def userlogin(request):
    if request.method == "GET":
        return render(request, 'recycling/login.html')
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return render(request,'recycling/index.html', {"ok":'登录成功'})
        else:
            return render(request, 'recycling/login.html', {'ok': '账号或密码错误!'})

# 用户退出
def userloginout(request):
    logout(request)
    return render(request, 'recycling/index.html', {"ok":"账号已退出!"})

# 废品交投
class Waste(View):
    def get(self, request):
        return render(request, 'recycling/waste-recycling.html')
    def post(self, request):
        pass

# 成为回收员
def brother(request):
    return render(request, 'recycling/recycling-brother.html')

# 环境价值--线下活动.格林美风采
def environ(request):
    activity = Activity.objects.filter(tags=1)
    activity2 = Activity.objects.filter(tags=2)
    return render(request, 'recycling/environmental.html', {"activity": activity, "activity2": activity2})


# 废品危害---普及知识
def hazard(request):
    activity = Activity.objects.filter(tags=3)
    activity2 = Activity.objects.filter(tags=4)
    return render(request, 'recycling/hazardous-waste.html', {"activity": activity, "activity2": activity2})


# 文章内容
def envart(request, id):
    oneactivity = Activity.objects.get(id=id)
    return render(request, 'recycling/environmental-art.html', {"oneactivity": oneactivity})

# 废品回收
class Scrap(View):
    def get(self, request):
        category = Category.objects.all()
        brand = Brand.objects.all()
        return render(request, 'recycling/scrap-details.html', locals())
    def post(self, request):
        return HttpResponse("完成")

# 订单中心
def order(request):
    return render(request, 'recycling/order-details.html')

# 个人中心
def personal(request):
    if request.method == "GET":
        myuser1 = RecyclingUser.objects.filter(username=request.user.username).first()
        myuser = myuser1.usermsg_set.all()
        return render(request, 'recycling/personal.html', {"myuser": myuser})
    elif request.method == "POST":
        nowuser = RecyclingUser.objects.filter(username=request.user).first()
        usermsg = UserMsg()
        usermsg.name = request.POST.get("name")
        usermsg.address = request.POST.get("address")
        usermsg.Zipcode = request.POST.get("zipcode")
        usermsg.telephone = request.POST.get("phone")
        usermsg.user = nowuser
        usermsg.save()
        return redirect(reverse('recycling:personal'))



