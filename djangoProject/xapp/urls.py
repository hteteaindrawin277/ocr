from django.urls import path
from . import views


urlpatterns = [
    path('login/',views.login,name='sss'),
    path('login/nextpage', views.nextpage, name='nextpage'),

    path('login/seclogin',views.seclogin,name='ccc'),
    path('login/success',views.comparedata,name='comparedata')
]
