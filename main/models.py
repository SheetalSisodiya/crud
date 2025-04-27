from django.db import models

class StudentModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField( max_length=254)
    course = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True, null=True, blank=True)

