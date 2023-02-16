from django.db import models


class Map(models.Model):
  id = models.BigAutoField(primary_key=True)
  name = models.CharField(max_length=30)
  owner = models.ForeignKey(User, on_delete=models.CASCADE)
  editors = models.ManyToManyField(User)
  viewers = models.ManyToManyField(User)
  
