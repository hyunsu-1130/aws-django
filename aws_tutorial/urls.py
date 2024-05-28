from django.urls import path
from .views import upload_image, success

urlpatterns = [
    path('upload/', upload_image, name='upload'),
    path('success/', success, name='success'),
]