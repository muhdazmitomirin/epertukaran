from django.conf.urls import include,url
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [

    url(r'^$',login_required(views.home2),name='pentadbiran_home'),

    #SENARAI BAHAGIAN
    # url(r'^sb/$',views.senarai_bhg,name='senarai_bahagian'), #Senarai Bahagian - senarai
    # url(r'^sbnew/$', views.add_bhg, name='tambah_bahagian'), #Senarai Bahagian - tambah
    # url(r'^(?P<pk>\d+)/editsb$', views.edit_bhg, name='kemaskini_bahagian'), #Senarai Bahagian - kemaskini
    # url(r'^(?P<pk>\d+)/removesb$', views.del_bhg, name='hapus_bahagian'), #Senarai Bahagian - hapus
    url(r'^list_json/$',views.bahagian_list_json.as_view(), name="bahagian_list_json"),
	url(r'^bahagian/$',views.home_bahagian,name='bahagian_home_json'),
    url(r'^bahagian/new/$', views.bahagian_new, name='bahagian_new'),
    url(r'^bahagian/(?P<pk>\d+)/edit$', views.bahagian_edit, name='bahagian_edit'),
    url(r'^bahagian/(?P<pk>\d+)/remove$', views.bahagian_remove, name='bahagian_remove'),
    url(r'^akaun/', views.my_acc, name='my_acc'),
    # url(r'^bahagian/(?P<pk>\d+)/$', views.bahagian_detail, name='bahagian_detail'),


]
