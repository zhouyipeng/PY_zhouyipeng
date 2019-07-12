from django.conf.urls import url
from . import views

app_name = 'booktest'

urlpatterns = [
    url('^$', views.hero, name='hero'),
    url('^herodetail/(\d+)/$', views.herodetail, name='herodetail'),
    url('^addhero/$', views.addhero, name='addhero'),
    url('^addskill/(\d+)/$', views.addskill, name='addskill'),
    url('^delhero/(\d+)/$', views.delhero, name='delhero'),
    url('^delskills/(\d+)/$', views.delskills, name='delskills'),
    url('^modifyskill/(\d+)/$', views.modifyskill, name='modifyskill'),


]
