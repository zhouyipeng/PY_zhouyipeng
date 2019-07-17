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

]