from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^feiraslivres/$', views.feira_list),
    url(r'^feiraslivres/(?P<pk>[0-9]+)/$', views.feira_detail),
]

