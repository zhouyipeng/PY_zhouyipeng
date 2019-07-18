from django.template import library
from ..models import UserMsg, Category, Brand, Order, OrderGoods

register = library.Library()


@register.simple_tag
def getallcategory():
    category = Category.objects.all()
    return category

@register.simple_tag
def getallbrand():
    brand = Brand.objects.all()
    return brand




