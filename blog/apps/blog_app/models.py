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
    title = models.CharField(verbose_name="标题", max_length=40)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="类别")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作者")
    views = models.IntegerField(default=0, verbose_name="阅读量")
    # body = models.TextField()
    body = UEditorField(imagePath="articleimg/", width="100%", verbose_name="内容")
    tags = models.ManyToManyField(Tag, verbose_name="标签")

    def __str__(self):
        return self.title



