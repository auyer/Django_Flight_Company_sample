from django.conf.urls import url
from . import views
from .models import com_aerea,cidade,voo

urlpatterns = [
    url(r'^$', views.home, name='Home'),
    url(r'^flights/$', views.voo_list, name='Full light List'),
    url(r'^flight/(?P<pk>\d+)/$', views.voo_info, name='Flight Number '),
    url(r'^searchTest/$', views.search_form),#link para a view que redireciona ao formulario de busca
    url(r'^sresults/$', views.search),#link para a view dos resultados da busca
    url(r'^twoflight/(?P<ctf>\w+)/(?P<ctt>\w+)$', views.advanced_Search, name='Two Way Flights'),
    #url(r'^$', views.city_list, name='city_list'),

]
