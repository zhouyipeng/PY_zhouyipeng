from django.template import library
from ..models import UserMsg

register = library.Library()

@register.simple_tag
def myusermsg():
    myuser = UserMsg.objects.all()
    return myuser


