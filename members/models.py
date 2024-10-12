from django.db import models

# Create your models here.
from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  qr_code_url = models.URLField(null=True, blank=True)  # Ensure this line exists
  def __str__(self):
        return f"{self.firstname} {self.lastname}"

class Total(models.Model):
  total = models.IntegerField()
  cloudinary_cloud_name = models.CharField(max_length=255, blank=True, null=True)
  cloudinary_api_key = models.CharField(max_length=255, blank=True, null=True)
  cloudinary_api_secret = models.CharField(max_length=255, blank=True, null=True)
  def __str__(self):
    return f"Total: {self.total}"