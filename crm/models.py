from django.db import models

class Month(models.Model):
    name = models.CharField(max_length=20)

class Sales(models.Model):
    sales = models.IntegerField()

