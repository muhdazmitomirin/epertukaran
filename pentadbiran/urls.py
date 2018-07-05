from django.conf.urls import include,url
from . import views

urlpatterns = [
    url(r'^sb/$',views.senarai_bhg,name='senarai_bahagian'),
    url(r'^(?P<pk>\d+)/remove$', views.del_bhg, name='hapus_bahagian'),
    url(r'^sbnew/$', views.add_bhg, name='tambah_bahagian'),
]

