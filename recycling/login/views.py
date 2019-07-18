from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.views.generic import View
from .models import *
from django.contrib.auth import login, logout, authenticate
from datetime import datetime

# Create your views here.

# 登录装饰器
def checklogin(fun):
    def check(request, *args):
        if request.user and request.user.is_authenticated:
            return fun(request, *args)
        else:
            return render(request, "recycling/login.html", {'ok': '请先登录'})
    return check


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
        return HttpResponse("完成")


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
        return render(request, 'recycling/scrap-details.html')

# 废品放入废品框
@checklogin
def scrappost(request, id):
    if request.method == "POST":
        parts1 = request.POST.get("1")
        parts2 = request.POST.get("2")
        parts3 = request.POST.get("3")
        parts4 = request.POST.get("4")
        parts5 = request.POST.get("5")
        parts6 = request.POST.get("6")
        goods = oneGoods.objects.get(id=id)
        goodsname = oneGoods.objects.get(id=id).goodsmodel
        goodsprice = goods.price
        minus = goodsprice * 0.1
        if parts1:
            goodsprice -= minus
            goodsname += '/' + parts1
        if parts2:
            goodsprice -= minus
            goodsname += '/' + parts2
        if parts3:
            goodsprice -= minus
            goodsname += '/' + parts3
        if parts4:
            goodsprice -= minus
            goodsname += '/' + parts4
        if parts5:
            goodsprice -= minus
            goodsname += '/' + parts5
        if parts6:
            goodsprice -= minus
            goodsname += '/' + parts6


        user = RecyclingUser.objects.filter(username=request.user).first()
        cart = CartGoods(goodname=goodsname, goodprice=goodsprice, integral=goodsprice, carbonreduction=150, user=user)
        cart.save()
        return render(request, 'recycling/scrap-details.html', {"over":'添加成功'})

# 废品框

class Basket(View):
    @checklogin
    def get(self, request):
        user = RecyclingUser.objects.filter(username=request.user).first()
        usermsg = user.usermsg_set.first()
        cart = CartGoods.objects.filter(user=user)
        total = 0
        allintegral = 0
        allcarbonreduction = 0
        for i in cart:
            total += i.goodprice
            allintegral += i.integral
            allcarbonreduction += i.carbonreduction
        return render(request, 'recycling/waste-baskets.html', locals())

    # 提交订单
    @checklogin
    def post(self, request):
        try:
            address = request.POST.get("address")
            name = request.POST.get("name")
            phone = request.POST.get("phone")
            date = request.POST.get("date")
            time = request.POST.get("time")
            datetime = date+time
            if date == '' or time == '':
                datetime = None
            user = RecyclingUser.objects.filter(username=request.user).first()

            order = Order(address=address, name=name, userphone=phone, appointment_time=datetime, user=user)
            order.save()
            allgoods = CartGoods.objects.filter(user=user).all()

            allintegral = 0
            allcarbonreduction = 0
            allprice = 0

            for i in allgoods:
                ordergoods = OrderGoods(goodname=i.goodname, goodprice=i.goodprice, integral=i.integral, carbonreduction=i.carbonreduction,
                                        order = order)
                ordergoods.save()
                allintegral += i.integral
                allcarbonreduction += i.carbonreduction
                allprice += i.goodprice
            order.allgold = allprice
            order.allintegral = allintegral
            order.allcarbonreduction = allcarbonreduction
            order.save()

            CartGoods.objects.filter(user=user).delete()

            return redirect(reverse('recycling:order'), {"ok": '结算成功'})
        except:
            user = RecyclingUser.objects.filter(username=request.user).first()
            usermsg = user.usermsg_set.first()
            cart = CartGoods.objects.filter(user=user)
            total = 0
            allintegral = 0
            allcarbonreduction = 0
            for i in cart:
                total += i.goodprice
                allintegral += i.integral
                allcarbonreduction += i.carbonreduction
            error = "信息错误，请重新填写！"
            return render(request, 'recycling/waste-baskets.html', locals())


# 购物车删除
@checklogin
def removebasket(request, id):
    CartGoods.objects.filter(id=id).first().delete()

    user = RecyclingUser.objects.filter(username=request.user).first()
    cart = CartGoods.objects.filter(user=user)
    total = 0
    allintegral = 0
    allcarbonreduction = 0
    for i in cart:
        total += i.goodprice
        allintegral += i.integral
        allcarbonreduction += i.carbonreduction
    return render(request, 'recycling/waste-baskets.html', locals())

# 订单中心
@checklogin
def order(request):
    order = Order.objects.filter(user=request.user)
    return render(request, 'recycling/order-details.html', {"order":order})

# 个人中心
@checklogin
def personal(request):
    if request.method == "GET":

        myuser1 = RecyclingUser.objects.filter(username=request.user.username).first()
        myuser = myuser1.usermsg_set.all()

        user = UserMsg.objects.filter(user=request.user).first()

        return render(request, 'recycling/personal.html', {"myuser": myuser, "user": user, "myuser1": myuser1})
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

# 类别搜索
def sc_category(request, id):
    goods = Category.objects.filter(id=id).first().onegoods_set.all()
    return render(request, 'recycling/scrap-details.html', {"goods":goods})

# 品牌搜索
def sc_brand(request, id):
    goods = Brand.objects.filter(id=id).first().onegoods_set.all()
    return render(request, 'recycling/scrap-details.html', {"goods": goods})

# 型号搜索
def sc_model(request, id):
    onegoods = oneGoods.objects.get(id=id)
    return render(request, 'recycling/scrap-details.html', {"onegoods": onegoods})

# 回收人员订单界面
def overorder(request):
    order = Order.objects.filter(status=False)
    order2 = Order.objects.filter(status=True)
    return render(request, 'recycling/order-list.html', locals())

# 回收人员订单完成
def okorder(request, id):
    oneorder = Order.objects.get(id=id)

    usermsg = oneorder.user.usermsg_set.first()
    usermsg.usergold += oneorder.allgold
    usermsg.integral += oneorder.allintegral
    usermsg.carbonreduction += oneorder.allcarbonreduction
    usermsg.save()

    oneorder.status = True
    oneorder.over_time = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
    oneorder.save()

    return redirect(reverse('recycling:overorder'))


