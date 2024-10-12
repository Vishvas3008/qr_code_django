from django import forms
from .models import Total

class CloudinaryConfigForm(forms.ModelForm):
    class Meta:
        model = Total
        fields = ['cloudinary_cloud_name', 'cloudinary_api_key', 'cloudinary_api_secret']
    