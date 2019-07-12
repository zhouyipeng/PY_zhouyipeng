from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from django.views.generic import View
from .models import *
from .forms import ArticleForm, CommentForm
from django.core.paginator import Paginator, Page

# Create your views here.

def getpage(request, object_list, per_num):
    pagenum = request.GET.get("page")
    pagenum = 1 if not pagenum else pagenum
    page = Paginator(object_list, per_num).get_page(pagenum)
    return page


# 首页
class indexView(View):
    def get(self, request):
        ads = Ads.objects.all()
        articles = Article.objects.all()
        page = getpage(request, articles, 1)
        return render(request, 'blog/index.html', {"ads":ads, "page":page})


# 文章
class SingleView(View):
    def get(self, request, id):
        article = get_object_or_404(Article, id=id)
        # 阅读文章后，文章阅读量+1
        article.views += 1
        article.save()
        # 创建评论表单
        cf = CommentForm()
        return render(request, 'blog/single.html', locals())

    def post(self, request, id):
        article = get_object_or_404(Article, id=id)
        cf = CommentForm(request.POST)
        comment = cf.save(commit=False)
        comment.article = article
        comment.save()
        return redirect(reverse("blog:single", args=(article.id, )))


# 添加文章
class Addarticle(View):
    def get(self, request):
        af = ArticleForm()
        return render(request, 'blog/addarticle.html', locals())

    def post(self, request):
        af = ArticleForm(request.POST)
        if af.is_valid():
            article = af.save(commit=False)
            article.category = Category.objects.first()
            article.author = User.objects.first()
            article.save()
            return redirect(reverse('blog:index'))


# 归档（按发布时间查看文章）
class ArchivesView(View):
    def get(self, request, year, month):
        article = Article.objects.filter(create_time__year=year, create_time__month=month)
        page = getpage(request, article, 1)
        return render(request, "blog/index.html", {"article": article, "page":page})


# 由类别查找文章
class findarticle(View):
    def get(self, request, title):
        categorys = Category.objects.filter(title=title)[0].article_set.all()
        page = getpage(request, categorys, 1)
        return render(request, "blog/index.html", {"page":page})


# 由标签查找文章
class findtag(View):
    def get(self, request, title):
        tags = Tag.objects.filter(title=title)[0].article_set.all()
        page = getpage(request, tags, 1)
        return render(request, "blog/index.html", {"page": page})