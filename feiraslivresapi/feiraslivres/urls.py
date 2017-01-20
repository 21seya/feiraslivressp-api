from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^feiras/$', views.FeiraList.as_view(),
        name=views.FeiraList.name),
    url(r'^feiras/(?P<pk>[0-9]+)/$', views.FeiraDetail.as_view(),
        name=views.FeiraDetail.name),

    url(r'^$', views.ApiRoot.as_view(),
        name=views.ApiRoot.name),
]
