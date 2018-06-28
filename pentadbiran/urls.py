from django.conf.urls import include,url
from . import views

urlpatterns = [
    url(r'^sb/$',views.senarai_bhg,name='senarai_bahagian'),

]

