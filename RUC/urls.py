from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^ruc/$', views.RUC_list),
    url(r'^ruc/(?P<pk>[0-9]+)/$', views.RUC_detail),
    url(r'^ruc/dni/(?P<pk>[0-9]+)/$', views.RUC_DNI_detail),
]
