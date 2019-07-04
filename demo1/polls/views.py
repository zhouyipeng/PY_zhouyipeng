from django.shortcuts import render, redirect, reverse
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

# Create your views here.

# 主页
def index(request):
    polls = PollsInfo.objects.all()
    return render(request, "booktest/pollIndex.html", {'polls': polls})
    # return HttpResponse("完成!")

# 投票页面
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
def outvote(request, id):
    out = PollsInfo.objects.get(id=id)
    return render(request, "booktest/outvote.html", {"out":out})







