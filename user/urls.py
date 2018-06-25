from django.conf.urls import include,url
from . import views

urlpatterns = [
    url(r'^$',views.home,name='user_home'),
    url(r'^home/$',views.home,name='user_home'),
    url(r'^user_dashboard/$',views.user_dashboard,name='user_dashboard'),
    url(r'^home_admin/$',views.home_admin,name='user_home_admin'),
]

