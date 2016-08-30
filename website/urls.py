from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='Home'),
    url(r'^$', views.voo_list, name='voo_list'),
    url(r'^$', views.com_aerea_list, name='com_aerea_list'),
    url(r'^$', views.city_list, name='city_list'),
]
