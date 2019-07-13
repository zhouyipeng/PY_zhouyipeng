from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import *
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.contrib.auth import login, logout, authenticate
import random, io
from PIL import Image, ImageDraw, ImageFont
from django.core.cache import cache
from django.core.mail import send_mail, send_mass_mail,  EmailMultiAlternatives
from django.conf import settings
from itsdangerous import TimedJSONWebSignatureSerializer






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
        password = request.POST.get("pwd")

        # 1.使用cookies存储信息
        # 登录成功，存储cookie
        # response = redirect(reverse('polls:index'))
        # # set_cookie参数为键值对，第一个为键，第二个为值
        # response.set_cookie("username", username)
        # return response

        # user = authenticate(request,username=username,password=password)
        user = PollsUser.objects.filter(username=username).first()
        print(PollsUser.objects.filter(username=123).first())
        if user.check_password(password):
            if user.is_active:
                # 验证码校验
                verifycode = request.POST.get("verify")

                if not verifycode.upper() == cache.get("verify").upper():
                    return render(request, 'booktest/login.html', {"errors": "验证码错误！"})
                # 登录成功存储session信息
                request.session["username"] = username
                login(request, user)
                return redirect(reverse('polls:index'))
            else:
                return render(request, 'booktest/login.html', {"errors": "账户未激活！"})
        else:
            return render(request, 'booktest/login.html', {"errors": "密码错误！"})




# 用户注册
def regist(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("pwd")
        password2 = request.POST.get("pwd2")
        if password == password2:
            # 如果账号已存在会报错，使用try捕捉
            try:
                user = PollsUser.objects.create_user(username=username, password=password)
                user.is_active = False
                user.save()
            except:
                user = None

            if user:
                # 账号注册成功后，进行邮件发送，用于验证账号

                # 创建接收邮件的邮箱
                usermail = request.POST.get("email")
                recvlist = [usermail]

                # 用户激活时的网址序列化，以及有效期
                serializer = TimedJSONWebSignatureSerializer(settings.SECRET_KEY)
                serializerstr = serializer.dumps({"userid":user.id}).decode("utf-8")
                try:

                    mail = EmailMultiAlternatives("python测试邮件", "<h1><a href='http://127.0.0.1:8000/polls/active/%s/'>django发来的邮件！</a></h1>"%serializerstr, settings.EMAIL_HOST_USER,
                                                  recvlist)
                    mail.content_subtype = "html"
                    mail.send()
                    # send_mail("这是一封测试邮件", "这是django发来的邮件", settings.EMAIL_HOST_USER, recvlist)

                    print("发送成功")

                except Exception as e:
                    print(e)

                return redirect(reverse('polls:userlogin'))
            else:
                return render(request, 'booktest/login.html', {"errors": "此账号已被注册"})
        else:
            return render(request, 'booktest/login.html', {"errors": "注册失败,两次密码不一致"})




# 用户退出
def userout(request):
    # 依旧使用redirect获得页面，将页面中的cookie删除
    # response = redirect(reverse('booktest:index'))
    # response.delete_cookie("username")

    # 退出时session的删除
    # request.session.flush()
    logout(request)

    return redirect(reverse('booktest:index'))



# 主页
@checklogin
def index(request):
    # print(request.user, request.user.is_authenticated)
    # print(request)
    # username = request.POST.get("username")
    # password = request.POST.get("pwd")
    # user = authenticate(request, username=username, password=password)
    # if user:
    #     print(user, user.is_authenticated)
    #     login(request, user)
    # else:
    #     print("授权失败")

    # username = request.session.get("username")
    # 判断是否读取到username，如果读取到进入首页，没有跳回登录界面

    polls = PollsInfo.objects.all()
    return render(request, "booktest/pollIndex.html", locals())


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


# 验证码生成
def verify(request):
    # 定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100),
               random.randrange(20, 100),
               random.randrange(20, 100))
    width = 100
    heigth = 30
    # 创建画面对象
    im = Image.new('RGB', (width, heigth), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, heigth))
    fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
    draw.point(xy, fill=fill)
    # 定义验证码的备选值
    str1 = 'abcdefghijklmnopqrstuvwxyzABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    # 将生成的验证码存入缓存
    cache.set("verify", rand_str)
    # 构造字体对象
    font = ImageFont.truetype('Inkfree.ttf', 23)
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    # 释放画笔
    del draw
    request.session['verifycode'] = rand_str
    f = io.BytesIO()
    im.save(f, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(f.getvalue(), 'image/png')


# 邮件验证激活用户
def active(request, id):
    # 将id反序列化
    serializer = TimedJSONWebSignatureSerializer(settings.SECRET_KEY)
    serializerobj = serializer.loads(id)
    id = serializerobj['userid']

    useractive = get_object_or_404(PollsUser, id=id)
    useractive.is_active = True
    useractive.save()
    return render(request, 'booktest/login.html', {"errors": "账户激活成功"})








