from django.db import models
from django.contrib.auth.models import User
# 导入富文本
from DjangoUeditor.models import UEditorField

# Create your models here.

# 广告显示
class Ads(models.Model):
    img = models.ImageField(upload_to="ads")
    desc = models.CharField(max_length=40)
    index = models.IntegerField(default=0)

    def __str__(self):
        return self.desc

# 文章类别
class Category(models.Model):
    title = models.CharField(max_length=40)

    def __str__(self):
        return self.title

# 标签
class Tag(models.Model):
    title = models.CharField(max_length=40)

    def __str__(self):
        return self.title


# 文章
class Article(models.Model):
    title = models.CharField(max_length=40)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)
    # body = models.TextField()
    body = UEditorField(imagePath="articleimg/", width="100%")
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


