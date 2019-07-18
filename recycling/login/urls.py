from django.conf.urls import url
from . import views

app_name = 'login'

urlpatterns = [
    url('^$', views.index, name="index"),
    url('^register/$', views.register, name='register'),
    url('^login/$', views.userlogin, name="login"),
    url('^userloginout/$', views.userloginout, name="userloginout"),
    url('^waste/$', views.Waste.as_view(), name='waste'),
    url('^environ/$', views.environ, name="environ"),
    url('^hazard/$', views.hazard, name="hazard"),
    url('^brother/$', views.brother, name="brother"),
    url('^scrap/$', views.Scrap.as_view(), name="scrap"),
    url('^order/$', views.order, name="order"),
    url('^personal/$', views.personal, name="personal"),
    url('^envart/(\d+)/$', views.envart, name="envart"),
    url('^sc_category/(\d+)/$', views.sc_category, name='sc_category'),
    url('^sc_brand/(\d+)/$', views.sc_brand, name='sc_brand'),
    url('^sc_model/(\d+)/$', views.sc_model, name="sc_model"),
    url('^scrappost/(\d+)/$', views.scrappost, name="scrappost"),
    url('^basket/$', views.Basket.as_view(), name="basket"),
    url('^removebasket/(\d+)/$', views.removebasket, name="removebasket"),
    url('^overorder/$', views.overorder, name="overorder"),
    url('^okorder/(\d+)/$', views.okorder, name="okorder"),

]