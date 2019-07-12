from django.db import models
from blog_app.models import Article

# Create your models here.

class Comment(models.Model):
    name = models.CharField(max_length=40)
    url = models.URLField(blank=True, null=True, default="http://www.baidu.com")
    email = models.EmailField(blank=True, null=True)
    content = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    # 用于将评论按时间进行倒叙排列
    class Meta:
        ordering = ("-create_time", )


