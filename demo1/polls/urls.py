from django.conf.urls import url
from . import views

app_name = "polls"

urlpatterns = [
    url('^index/$', views.index, name="index"),
    url('^vote/(\d+)/$', views.vote, name="vote"),
    url('^outvote/(\d+)/$', views.outvote, name="outvote"),

]