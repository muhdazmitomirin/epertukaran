from django.conf.urls import include,url
from . import views

urlpatterns = [

    #SENARAI BAHAGIAN
    url(r'^sb/$',views.senarai_bhg,name='senarai_bahagian'), #Senarai Bahagian - senarai
    url(r'^sbnew/$', views.add_bhg, name='tambah_bahagian'), #Senarai Bahagian - tambah
    url(r'^(?P<pk>\d+)/editsb$', views.edit_bhg, name='kemaskini_bahagian'), #Senarai Bahagian - kemaskini
    url(r'^(?P<pk>\d+)/removesb$', views.del_bhg, name='hapus_bahagian'), #Senarai Bahagian - hapus
]

