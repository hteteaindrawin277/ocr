from django.urls import path
from . import views


urlpatterns = [
    path('form/',views.form,name='sss'),
    path('form/next',views.next)
]
