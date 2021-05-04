from django.db import models

class Month(models.Model):
    name = models.CharField(max_length=20)

class Sales (models.Model):
    sales = models.IntegerField()
class Enquiry(models.Model):
    Student_name =models.CharField(max_length=50)
    Course_name=models.CharField(max_length=100)
    Contact_number=models.IntegerField()
    Enquiry_date=models.DateField()
