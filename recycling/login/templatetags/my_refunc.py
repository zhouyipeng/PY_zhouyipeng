from django.template import library
from ..models import UserMsg, Category, Brand, Order, OrderGoods, Ads

register = library.Library()


@register.simple_tag
def getallcategory():
    category = Category.objects.all()
    return category

@register.simple_tag
def getallbrand():
    brand = Brand.objects.all()
    return brand

@register.simple_tag
def getAds():
    ads = Ads.objects.all()
    return ads



