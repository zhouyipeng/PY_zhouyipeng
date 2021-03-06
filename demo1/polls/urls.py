from django.conf.urls import url
from . import views

app_name = "polls"

urlpatterns = [
    url('^index/$', views.index, name="index"),
    url('^vote/(\d+)/$', views.vote, name="vote"),
    url('^outvote/(\d+)/$', views.outvote, name="outvote"),
    url('^userlogin/$', views.userlogin, name="userlogin"),
    url('^userout/$', views.userout, name="userout"),
    url('^regist/$', views.regist, name="regist"),
    url('^verify/$', views.verify, name="verify"),
    url('^active/(.*?)/$', views.active, name="active"),



]