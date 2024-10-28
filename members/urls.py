from django.urls import path
from . import views
from .views import cloudinary_config_view

from django.views.generic import RedirectView
urlpatterns = [
    # path('', views.members),
     path('', RedirectView.as_view(url='/admin/', permanent=False)),
     path('cloudinary-config/', cloudinary_config_view, name='cloudinary_config'),
]