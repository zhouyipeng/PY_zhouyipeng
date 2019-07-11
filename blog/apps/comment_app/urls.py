from django.conf.urls import url
from . import views

app_name = "comment"

urlpatterns = [
    url('^comment/(\d+)/$', views.Addcomment.as_view(), name="comment"),
]