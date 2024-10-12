from django.db import models

# Create your models here.
from django.db import models

class Member(models.Model):
  member_id = models.IntegerField(default=1)
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  def __str__(self):
        return f"{self.firstname} {self.lastname}"

class Total(models.Model):
  total = models.IntegerField()
  cloudinary_cloud_name = models.CharField(max_length=255, blank=True, null=True)
  cloudinary_api_key = models.CharField(max_length=255, blank=True, null=True)
  cloudinary_api_secret = models.CharField(max_length=255, blank=True, null=True)
  def __str__(self):
    return f"Total: {self.total}"