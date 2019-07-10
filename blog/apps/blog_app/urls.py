from django.conf.urls import url
from . import views

app_name = "blog"

urlpatterns = [
    url('^$', views.indexView.as_view(), name="index"),
    url(r'^single/(\d+)/$', views.SingleView.as_view(), name="single"),
    url(r'^addarticle/$', views.Addarticle.as_view(), name="addarticle"),


]