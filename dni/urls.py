from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^dni/$', views.dni_list),
    url(r'^dni/(?P<pk>[0-9]+)/$', views.dni_detail),
]
