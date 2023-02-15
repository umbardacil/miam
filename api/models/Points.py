from django.db import models

from . import Maps


class Point(models.Model):
  id = models.BigAutoField(primary_key=True)
  name = models.CharField(max_length=30)
  address = models.CharField(max_length=100)  # a whole class for the address ?
  description = models.TextField()
  type = models.CharField(max_length=16)
  map = models.ForeignKey(Map, on_delete=models.CASCADE)
  
