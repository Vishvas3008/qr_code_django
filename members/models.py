from django.db import models

# Create your models here.
from django.db import models

class Member(models.Model):
  member_id = models.IntegerField(default=1)
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)

class Total(models.Model):
  total = models.IntegerField()