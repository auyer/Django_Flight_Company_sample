from django.conf.urls import url
from . import views
from .models import com_aerea,cidade,voo

urlpatterns = [
    url(r'^$', views.home, name='Home'),
    url(r'^flights/$', views.voo_list, name='Full light List'),
    url(r'^flight/(?P<pk>\d+)/$', views.voo_info, name='Flight Number '),
    #url(r'^$', views.com_aerea_list, name='com_aerea_list'),
    #url(r'^$', views.city_list, name='city_list'),
]
