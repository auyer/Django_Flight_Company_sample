from django.conf.urls import url
from . import views
from .models import com_aerea,cidade,voo

urlpatterns = [
    url(r'^$', views.home, name='Home'),
    url(r'^flights/$', views.voo_list, name='Full light List'),
    url(r'^flight/(?P<pk>\d+)/$', views.voo_info, name='Flight Number '),
    url(r'^searchTest/$', views.search_form),
    url(r'^sresults/$', views.search),
   
]
