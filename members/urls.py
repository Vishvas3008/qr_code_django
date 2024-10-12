from django.urls import path
from . import views
from .views import cloudinary_config_view
urlpatterns = [
    path('', views.members),
     path('cloudinary-config/', cloudinary_config_view, name='cloudinary_config'),
]