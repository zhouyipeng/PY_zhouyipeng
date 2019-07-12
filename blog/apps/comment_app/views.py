from django.views.generic import View
from django.http import JsonResponse
from .models import Comment
from blog_app.models import Article
# Create your views here.



class Addcomment(View):
    def post(self, request, id):
        name = request.POST.get("name")
        url = request.POST.get("url")
        email = request.POST.get("email")
        content = request.POST.get("content")

        article = Article.objects.get(id=id)
        comment = Comment(name=name, url=url, email=email, content=content, article=article)
        comment.save()
        return JsonResponse({
            "name": comment.name,
            "url" : comment.url,
            "create_time": comment.create_time,
            "email": comment.email,
            "content": comment.content
        })

