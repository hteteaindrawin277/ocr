from . import views
from django.urls import path

urlpatterns = [
    path('upload/', views.image_upload_view)
]