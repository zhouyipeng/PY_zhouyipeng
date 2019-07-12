from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import *

# Create your views here.

# 英雄界面
def hero(request):
    hero = HeroInfo.objects.all()
    return render(request, 'booktest/hero.html', {"hero": hero})

# 英雄详细
def herodetail(request, id):
    hero = HeroInfo.objects.get(id=id)
    return render(request, 'booktest/heroDetail.html', {"hero": hero})

# 添加英雄
def addhero(request):
    if request.method == "GET":
        return render(request, 'booktest/addhero.html')
    elif request.method == "POST":
        hero = HeroInfo()
        heroname = request.POST.get("heroname")
        hero.heroname = heroname
        hero.save()
        return redirect(reverse("booktest:hero"))

# 添加英雄技能
def addskill(request, id):
    name = request.POST.get("name")
    atk = request.POST.get("atk")
    skill = SkillsInfo()
    skill.skill = name
    skill.atk = atk
    skill.hero = HeroInfo.objects.get(id=id)
    skill.save()
    return redirect(reverse('booktest:herodetail', args=(id,)))

# 删除技能
def delskills(request, id):
    skill = SkillsInfo.objects.get(id=id)
    heroid = skill.hero.id
    skill.delete()
    return redirect(reverse('booktest:herodetail', args=(heroid,)))
    # return HttpResponse("成功")

# 删除英雄
def delhero(request, id):
    hero = HeroInfo.objects.get(id=id)
    hero.delete()
    return redirect(reverse('booktest:hero'))

# 修改技能
def modifyskill(request, id):
    skill = SkillsInfo.objects.get(id=id)
    heroid = skill.hero.id
    if request.method == "GET":
        return render(request, "booktest/modifyskill.html", {"skill":skill})
    elif request.method == "POST":
        skill.skill = request.POST.get("skill")
        skill.atk = request.POST.get("atk")
        skill.save()
        return redirect(reverse('booktest:herodetail', args=(heroid,)))

