from django.db import models
from django.contrib.auth.models import User
from DjangoUeditor.models import UEditorField
# Create your models here.

# 广告轮播图
class Ads(models.Model):
    img = models.ImageField(upload_to="ads")
    index = models.IntegerField(default=0)

# 用户注册
class RecyclingUser(User):
    phone = models.IntegerField(default=0)


# 用户个人信息
class UserMsg(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    Zipcode = models.IntegerField(default=0)
    telephone = models.IntegerField(default=0)
    integral = models.IntegerField(default=0)
    # 碳减排
    carbonreduction = models.IntegerField(default=0)
    usergold = models.IntegerField(default=0)
    user = models.ForeignKey(RecyclingUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# 商品类别
class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

# 品牌
class Brand(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

# 单个商品
class oneGoods(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    goodsmodel = models.CharField(max_length=50)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.goodsmodel

# 商品类
class Goods(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    goodsmodel = models.CharField(max_length=40)
    detail = models.CharField(max_length=200)
    user = models.ForeignKey(RecyclingUser, on_delete=models.CASCADE)

# 购物车类
class CartGoods(models.Model):
    goodname = models.CharField(max_length=200)
    goodprice = models.IntegerField()
    integral = models.IntegerField(default=0)
    # 碳减排
    carbonreduction = models.IntegerField(default=0)
    user = models.ForeignKey(RecyclingUser, on_delete=models.CASCADE)

# 订单类
class Order(models.Model):
    address = models.CharField(max_length=50)
    name = models.CharField(max_length=20)
    userphone = models.IntegerField()
    allgold = models.IntegerField(default=0)
    allintegral = models.IntegerField(default=0)
    allcarbonreduction = models.IntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)
    appointment_time = models.CharField(max_length=50)
    over_time = models.CharField(max_length=50, null=True)
    status = models.BooleanField(default=False)
    user = models.ForeignKey(RecyclingUser, on_delete=models.CASCADE)

# 订单商品类
class OrderGoods(models.Model):
    goodname = models.CharField(max_length=200)
    goodprice = models.IntegerField()
    integral = models.IntegerField(default=0)
    # 碳减排
    carbonreduction = models.IntegerField(default=0)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)


# 文章标签
class ActivityTags(models.Model):
    title = models.CharField(max_length=20, default='文章')

    def __str__(self):
        return self.title

# 活动文章
class Activity(models.Model):
    title = models.CharField(max_length=50)
    create_time = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    body = UEditorField(imagePath="articleimg/", width='100%')
    tags = models.ForeignKey(ActivityTags, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# 碳积分兑换
class Pointsfor(models.Model):
    img = models.ImageField(upload_to="integral")
    gold = models.IntegerField()
    goodsname = models.CharField(max_length=100)
    consumption = models.IntegerField()








